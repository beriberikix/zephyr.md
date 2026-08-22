---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/interrupt__util_8h_source.html
original_path: doxygen/html/interrupt__util_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

interrupt\_util.h

[Go to the documentation of this file.](interrupt__util_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef INTERRUPT\_UTIL\_H\_

8#define INTERRUPT\_UTIL\_H\_

9

10#if defined(CONFIG\_CPU\_CORTEX\_M)

11#include <cmsis\_core.h>

12

13static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) get\_available\_nvic\_line([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) initial\_offset)

14{

15 int i;

16

17 for (i = initial\_offset - 1; i >= 0; i--) {

18

19 if (NVIC\_GetEnableIRQ(i) == 0) {

20 /\*

21 \* Interrupts configured statically with IRQ\_CONNECT(.)

22 \* are automatically enabled. NVIC\_GetEnableIRQ()

23 \* returning false, here, implies that the IRQ line is

24 \* either not implemented or it is not enabled, thus,

25 \* currently not in use by Zephyr.

26 \*/

27

28 /\* Set the NVIC line to pending. \*/

29 NVIC\_SetPendingIRQ(i);

30

31 if (NVIC\_GetPendingIRQ(i)) {

32 /\*

33 \* If the NVIC line is pending, it is

34 \* guaranteed that it is implemented; clear the

35 \* line.

36 \*/

37 NVIC\_ClearPendingIRQ(i);

38

39 if (!NVIC\_GetPendingIRQ(i)) {

40 /\*

41 \* If the NVIC line can be successfully

42 \* un-pended, it is guaranteed that it

43 \* can be used for software interrupt

44 \* triggering. Return the NVIC line

45 \* number.

46 \*/

47 break;

48 }

49 }

50 }

51 }

52

53 [zassert\_true](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)(i >= 0, "No available IRQ line\n");

54

55 return i;

56}

57

58static inline void trigger\_irq(int irq)

59{

60 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Triggering irq : %d\n", irq);

61#if defined(CONFIG\_SOC\_TI\_LM3S6965\_QEMU) || defined(CONFIG\_CPU\_CORTEX\_M0) || \

62 defined(CONFIG\_CPU\_CORTEX\_M0PLUS) || defined(CONFIG\_CPU\_CORTEX\_M1) || \

63 defined(CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE)

64 /\* QEMU does not simulate the STIR register: this is a workaround \*/

65 NVIC\_SetPendingIRQ(irq);

66#else

67 NVIC->STIR = irq;

68#endif

69}

70

71#elif defined(CONFIG\_GIC)

72#include <[zephyr/drivers/interrupt\_controller/gic.h](gic_8h.md)>

73#include <[zephyr/dt-bindings/interrupt-controller/arm-gic.h](arm-gic_8h.md)>

74

75static inline void trigger\_irq(int irq)

76{

77 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Triggering irq : %d\n", irq);

78

79 /\* Ensure that the specified IRQ number is a valid SGI interrupt ID \*/

80 [zassert\_true](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)(irq <= 15, "%u is not a valid SGI interrupt ID", irq);

81

82 /\*

83 \* Generate a software generated interrupt and forward it to the

84 \* requesting CPU.

85 \*/

86#if CONFIG\_GIC\_VER <= 2

87 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)([GICD\_SGIR\_TGTFILT\_REQONLY](gic_8h.md#ae759ef6f311a7279db5e7ccd68c80863) | [GICD\_SGIR\_SGIINTID](gic_8h.md#ae388207ec492448a22511cee6dcecedc)(irq), [GICD\_SGIR](gic_8h.md#a5125b5f77951f0e882e002aac406beec));

88#else

89 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mpidr = [GET\_MPIDR](arch_2arm_2cortex__a__r_2cpu_8h.md#a958d9c5f047f5dc318ecf4b171a68949)();

90 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aff0 = [MPIDR\_AFFLVL](arch_2arm_2cortex__a__r_2cpu_8h.md#a35278aa57b0b98cd0cb541cfea58b177)(mpidr, 0);

91

92 [gic\_raise\_sgi](gic_8h.md#a08291705f002f01687cf507abbb410dc)(irq, mpidr, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(aff0));

93#endif

94}

95

96#elif defined(CONFIG\_ARC)

97static inline void trigger\_irq(int irq)

98{

99 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Triggering irq : %d\n", irq);

100 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_AUX\_IRQ\_HINT, irq);

101}

102

103#elif defined(CONFIG\_X86)

104

105#ifdef CONFIG\_X2APIC

106#include <[zephyr/drivers/interrupt\_controller/loapic.h](loapic_8h.md)>

107#define VECTOR\_MASK 0xFF

108#else

109#include <[zephyr/arch/arch\_interface.h](arch__interface_8h.md)>

110#define LOAPIC\_ICR\_IPI\_TEST 0x00004000U

111#endif

112

113/\*

114 \* We can emulate the interrupt by sending the IPI to

115 \* core itself by the LOAPIC for x86 platform.

116 \*

117 \* In APIC mode, Write LOAPIC's ICR to trigger IPI,

118 \* the LOAPIC\_ICR\_IPI\_TEST 0x00004000U means:

119 \* Delivery Mode: Fixed

120 \* Destination Mode: Physical

121 \* Level: Assert

122 \* Trigger Mode: Edge

123 \* Destination Shorthand: No Shorthand

124 \* Destination: depends on cpu\_id

125 \*

126 \* In X2APIC mode, this no longer works. We emulate the

127 \* interrupt by writing the IA32\_X2APIC\_SELF\_IPI MSR

128 \* to send IPI to the core itself via LOAPIC also.

129 \* According to SDM vol.3 chapter 10.12.11, the bit[7:0]

130 \* for setting the vector is only needed.

131 \*/

132static inline void trigger\_irq(int vector)

133{

134 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i;

135

136#ifdef CONFIG\_X2APIC

137 [x86\_write\_x2apic](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)([LOAPIC\_SELF\_IPI](loapic_8h.md#aeea0b064b955e73205f882cd80132455), ((VECTOR\_MASK & vector)));

138#else

139

140#ifdef CONFIG\_SMP

141 int cpu\_id = [arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)()->id;

142#else

143 int cpu\_id = 0;

144#endif

145 z\_loapic\_ipi(cpu\_id, LOAPIC\_ICR\_IPI\_TEST, vector);

146#endif /\* CONFIG\_X2APIC \*/

147

148 /\*

149 \* add some nop operations here to cost some cycles to make sure

150 \* the IPI interrupt is handled before do our check.

151 \*/

152 for (i = 0; i < 10; i++) {

153 [arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)();

154 }

155}

156

157#elif defined(CONFIG\_ARCH\_POSIX)

158#include <[zephyr/arch/posix/posix\_soc\_if.h](posix__soc__if_8h.md)>

159

160static inline void trigger\_irq(int irq)

161{

162 [posix\_sw\_set\_pending\_IRQ](posix__soc__if_8h.md#a8aa652da8beecd80c6036e1ad6f8fddd)(irq);

163}

164

165#elif defined(CONFIG\_RISCV)

166#if defined(CONFIG\_CLIC) || defined(CONFIG\_NRFX\_CLIC)

167void riscv\_clic\_irq\_set\_pending([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

168static inline void trigger\_irq(int irq)

169{

170 riscv\_clic\_irq\_set\_pending(irq);

171}

172#else

173static inline void trigger\_irq(int irq)

174{

175 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mip;

176

177 \_\_asm\_\_ volatile("csrrs %0, mip, %1\n" : "=r"(mip) : "r"(1 << irq));

178}

179#endif

180#elif defined(CONFIG\_XTENSA)

181static inline void trigger\_irq(int irq)

182{

183#if XCHAL\_NUM\_INTERRUPTS > 32

184 switch (irq >> 5) {

185 case 0:

186 z\_xt\_set\_intset(1 << irq);

187 break;

188 case 1:

189 z\_xt\_set\_intset1(1 << irq);

190 break;

191#if XCHAL\_NUM\_INTERRUPTS > 64

192 case 2:

193 z\_xt\_set\_intset2(1 << irq);

194 break;

195#endif

196#if XCHAL\_NUM\_INTERRUPTS > 96

197 case 3:

198 z\_xt\_set\_intset3(1 << irq);

199 break;

200#endif

201 default:

202 break;

203 }

204#else

205 z\_xt\_set\_intset(1 << irq);

206#endif

207}

208

209#elif defined(CONFIG\_SPARC)

210extern void z\_sparc\_enter\_irq(int);

211

212static inline void trigger\_irq(int irq)

213{

214 z\_sparc\_enter\_irq(irq);

215}

216

217#elif defined(CONFIG\_MIPS)

218extern void z\_mips\_enter\_irq(int);

219

220static inline void trigger\_irq(int irq)

221{

222 z\_mips\_enter\_irq(irq);

223}

224

225#elif defined(CONFIG\_CPU\_CORTEX\_R5) && defined(CONFIG\_VIM)

226

227extern void z\_vim\_arm\_enter\_irq(int);

228

229static inline void trigger\_irq(int irq)

230{

231 z\_vim\_arm\_enter\_irq(irq);

232}

233

234#elif defined(CONFIG\_RX)

235#define IR\_BASE\_ADDRESS DT\_REG\_ADDR\_BY\_NAME(DT\_NODELABEL(icu), IR)

236static inline void trigger\_irq(int irq)

237{

238 \_\_ASSERT(irq < [CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837), "attempting to trigger invalid IRQ (%u)", irq);

239 \_\_ASSERT(irq >= [CONFIG\_GEN\_IRQ\_START\_VECTOR](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c), "attempting to trigger reserved IRQ (%u)",

240 irq);

241 \_sw\_isr\_table[irq - [CONFIG\_GEN\_IRQ\_START\_VECTOR](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)].isr(

242 \_sw\_isr\_table[irq - [CONFIG\_GEN\_IRQ\_START\_VECTOR](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)].arg);

243}

244

245#else

[ 246](interrupt__util_8h.md#a3bef33fb908a7ffd30a3f9b433dacf18)#define NO\_TRIGGER\_FROM\_SW

247#endif

248

249#endif /\* INTERRUPT\_UTIL\_H\_ \*/

[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)

static ALWAYS\_INLINE \_cpu\_t \* arch\_curr\_cpu(void)

**Definition** arch\_inlines.h:17

[MPIDR\_AFFLVL](arch_2arm_2cortex__a__r_2cpu_8h.md#a35278aa57b0b98cd0cb541cfea58b177)

#define MPIDR\_AFFLVL(mpidr, aff\_level)

**Definition** cpu.h:101

[GET\_MPIDR](arch_2arm_2cortex__a__r_2cpu_8h.md#a958d9c5f047f5dc318ecf4b171a68949)

#define GET\_MPIDR()

**Definition** cpu.h:104

[CONFIG\_GEN\_IRQ\_START\_VECTOR](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)

#define CONFIG\_GEN\_IRQ\_START\_VECTOR

**Definition** irq.h:14

[CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837)

#define CONFIG\_NUM\_IRQS

**Definition** irq.h:183

[arch\_interface.h](arch__interface_8h.md)

[arm-gic.h](arm-gic_8h.md)

[gic.h](gic_8h.md)

Driver for ARM Generic Interrupt Controller.

[gic\_raise\_sgi](gic_8h.md#a08291705f002f01687cf507abbb410dc)

void gic\_raise\_sgi(unsigned int sgi\_id, uint64\_t target\_aff, uint16\_t target\_list)

raise SGI to target cores

[GICD\_SGIR](gic_8h.md#a5125b5f77951f0e882e002aac406beec)

#define GICD\_SGIR

**Definition** gic.h:181

[GICD\_SGIR\_SGIINTID](gic_8h.md#ae388207ec492448a22511cee6dcecedc)

#define GICD\_SGIR\_SGIINTID(x)

**Definition** gic.h:259

[GICD\_SGIR\_TGTFILT\_REQONLY](gic_8h.md#ae759ef6f311a7279db5e7ccd68c80863)

#define GICD\_SGIR\_TGTFILT\_REQONLY

**Definition** gic.h:251

[arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)

static void arch\_nop(void)

Do nothing and return.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[zassert\_true](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)

#define zassert\_true(cond,...)

Assert that cond is true.

**Definition** ztest\_assert.h:275

[loapic.h](loapic_8h.md)

[x86\_write\_x2apic](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)

static void x86\_write\_x2apic(unsigned int reg, uint64\_t val)

Write 64-bit value to the local APIC in x2APIC mode.

**Definition** loapic.h:118

[LOAPIC\_SELF\_IPI](loapic_8h.md#aeea0b064b955e73205f882cd80132455)

#define LOAPIC\_SELF\_IPI

**Definition** loapic.h:42

[posix\_soc\_if.h](posix__soc__if_8h.md)

[posix\_sw\_set\_pending\_IRQ](posix__soc__if_8h.md#a8aa652da8beecd80c6036e1ad6f8fddd)

void posix\_sw\_set\_pending\_IRQ(unsigned int IRQn)

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mem\_addr\_t addr)

**Definition** sys-io-common.h:70

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [interrupt\_util.h](interrupt__util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
