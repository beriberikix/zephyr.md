---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/interrupt__util_8h_source.html
original_path: doxygen/html/interrupt__util_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

[ 10](interrupt__util_8h.md#a265deca5cd25f2aba7fc942965b01158)#define MS\_TO\_US(ms) (ms \* USEC\_PER\_MSEC)

11

12#if defined(CONFIG\_CPU\_CORTEX\_M)

13#include <cmsis\_core.h>

14

15static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) get\_available\_nvic\_line([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) initial\_offset)

16{

17 int i;

18

19 for (i = initial\_offset - 1; i >= 0; i--) {

20

21 if (NVIC\_GetEnableIRQ(i) == 0) {

22 /\*

23 \* Interrupts configured statically with IRQ\_CONNECT(.)

24 \* are automatically enabled. NVIC\_GetEnableIRQ()

25 \* returning false, here, implies that the IRQ line is

26 \* either not implemented or it is not enabled, thus,

27 \* currently not in use by Zephyr.

28 \*/

29

30 /\* Set the NVIC line to pending. \*/

31 NVIC\_SetPendingIRQ(i);

32

33 if (NVIC\_GetPendingIRQ(i)) {

34 /\*

35 \* If the NVIC line is pending, it is

36 \* guaranteed that it is implemented; clear the

37 \* line.

38 \*/

39 NVIC\_ClearPendingIRQ(i);

40

41 if (!NVIC\_GetPendingIRQ(i)) {

42 /\*

43 \* If the NVIC line can be successfully

44 \* un-pended, it is guaranteed that it

45 \* can be used for software interrupt

46 \* triggering. Return the NVIC line

47 \* number.

48 \*/

49 break;

50 }

51 }

52 }

53 }

54

55 [zassert\_true](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)(i >= 0, "No available IRQ line\n");

56

57 return i;

58}

59

60static inline void trigger\_irq(int irq)

61{

62 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Triggering irq : %d\n", irq);

63#if defined(CONFIG\_SOC\_TI\_LM3S6965\_QEMU) || defined(CONFIG\_CPU\_CORTEX\_M0) \

64 || defined(CONFIG\_CPU\_CORTEX\_M0PLUS) || defined(CONFIG\_CPU\_CORTEX\_M1)\

65 || defined(CONFIG\_ARMV6\_M\_ARMV8\_M\_BASELINE)

66 /\* QEMU does not simulate the STIR register: this is a workaround \*/

67 NVIC\_SetPendingIRQ(irq);

68#else

69 NVIC->STIR = irq;

70#endif

71}

72

73#elif defined(CONFIG\_GIC)

74#include <[zephyr/drivers/interrupt\_controller/gic.h](gic_8h.md)>

75#include <[zephyr/dt-bindings/interrupt-controller/arm-gic.h](arm-gic_8h.md)>

76

77static inline void trigger\_irq(int irq)

78{

79 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Triggering irq : %d\n", irq);

80

81 /\* Ensure that the specified IRQ number is a valid SGI interrupt ID \*/

82 [zassert\_true](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)(irq <= 15, "%u is not a valid SGI interrupt ID", irq);

83

84 /\*

85 \* Generate a software generated interrupt and forward it to the

86 \* requesting CPU.

87 \*/

88#if CONFIG\_GIC\_VER <= 2

89 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)([GICD\_SGIR\_TGTFILT\_REQONLY](gic_8h.md#ae759ef6f311a7279db5e7ccd68c80863) | [GICD\_SGIR\_SGIINTID](gic_8h.md#ae388207ec492448a22511cee6dcecedc)(irq),

90 [GICD\_SGIR](gic_8h.md#a5125b5f77951f0e882e002aac406beec));

91#else

92 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mpidr = [GET\_MPIDR](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a958d9c5f047f5dc318ecf4b171a68949)();

93 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aff0 = [MPIDR\_AFFLVL](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a35278aa57b0b98cd0cb541cfea58b177)(mpidr, 0);

94

95 [gic\_raise\_sgi](gic_8h.md#a08291705f002f01687cf507abbb410dc)(irq, mpidr, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(aff0));

96#endif

97}

98

99#elif defined(CONFIG\_ARC)

100static inline void trigger\_irq(int irq)

101{

102 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Triggering irq : %d\n", irq);

103 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_AUX\_IRQ\_HINT, irq);

104}

105

106#elif defined(CONFIG\_X86)

107

108#ifdef CONFIG\_X2APIC

109#include <[zephyr/drivers/interrupt\_controller/loapic.h](loapic_8h.md)>

110#define VECTOR\_MASK 0xFF

111#else

112#include <[zephyr/sys/arch\_interface.h](arch__interface_8h.md)>

113#define LOAPIC\_ICR\_IPI\_TEST 0x00004000U

114#endif

115

116/\*

117 \* We can emulate the interrupt by sending the IPI to

118 \* core itself by the LOAPIC for x86 platform.

119 \*

120 \* In APIC mode, Write LOAPIC's ICR to trigger IPI,

121 \* the LOAPIC\_ICR\_IPI\_TEST 0x00004000U means:

122 \* Delivery Mode: Fixed

123 \* Destination Mode: Physical

124 \* Level: Assert

125 \* Trigger Mode: Edge

126 \* Destination Shorthand: No Shorthand

127 \* Destination: depends on cpu\_id

128 \*

129 \* In X2APIC mode, this no longer works. We emulate the

130 \* interrupt by writing the IA32\_X2APIC\_SELF\_IPI MSR

131 \* to send IPI to the core itself via LOAPIC also.

132 \* According to SDM vol.3 chapter 10.12.11, the bit[7:0]

133 \* for setting the vector is only needed.

134 \*/

135static inline void trigger\_irq(int vector)

136{

137 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i;

138

139#ifdef CONFIG\_X2APIC

140 [x86\_write\_x2apic](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)([LOAPIC\_SELF\_IPI](loapic_8h.md#aeea0b064b955e73205f882cd80132455), ((VECTOR\_MASK & vector)));

141#else

142

143#ifdef CONFIG\_SMP

144 int cpu\_id = [arch\_curr\_cpu](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2)()->id;

145#else

146 int cpu\_id = 0;

147#endif

148 z\_loapic\_ipi(cpu\_id, LOAPIC\_ICR\_IPI\_TEST, vector);

149#endif /\* CONFIG\_X2APIC \*/

150

151 /\*

152 \* add some nop operations here to cost some cycles to make sure

153 \* the IPI interrupt is handled before do our check.

154 \*/

155 for (i = 0; i < 10; i++) {

156 [arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)();

157 }

158}

159

160#elif defined(CONFIG\_ARCH\_POSIX)

161#include <[zephyr/arch/posix/posix\_soc\_if.h](posix__soc__if_8h.md)>

162

163static inline void trigger\_irq(int irq)

164{

165 [posix\_sw\_set\_pending\_IRQ](posix__soc__if_8h.md#a8aa652da8beecd80c6036e1ad6f8fddd)(irq);

166}

167

168#elif defined(CONFIG\_RISCV)

169#if defined(CONFIG\_NUCLEI\_ECLIC)

170void riscv\_clic\_irq\_set\_pending([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

171static inline void trigger\_irq(int irq)

172{

173 riscv\_clic\_irq\_set\_pending(irq);

174}

175#else

176static inline void trigger\_irq(int irq)

177{

178 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mip;

179

180 \_\_asm\_\_ volatile ("csrrs %0, mip, %1\n"

181 : "=r" (mip)

182 : "r" (1 << irq));

183}

184#endif

185#elif defined(CONFIG\_XTENSA)

186static inline void trigger\_irq(int irq)

187{

188 z\_xt\_set\_intset([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)((unsigned int)irq));

189}

190

191#elif defined(CONFIG\_SPARC)

192extern void z\_sparc\_enter\_irq(int);

193

194static inline void trigger\_irq(int irq)

195{

196 z\_sparc\_enter\_irq(irq);

197}

198

199#elif defined(CONFIG\_MIPS)

200extern void z\_mips\_enter\_irq(int);

201

202static inline void trigger\_irq(int irq)

203{

204 z\_mips\_enter\_irq(irq);

205}

206

207#elif defined(CONFIG\_CPU\_CORTEX\_R5) && defined(CONFIG\_VIM)

208

209extern void z\_vim\_arm\_enter\_irq(int);

210

211static inline void trigger\_irq(int irq)

212{

213 z\_vim\_arm\_enter\_irq(irq);

214}

215

216#else

217/\* So far, Nios II does not support this \*/

[ 218](interrupt__util_8h.md#a3bef33fb908a7ffd30a3f9b433dacf18)#define NO\_TRIGGER\_FROM\_SW

219#endif

220

221#endif /\* INTERRUPT\_UTIL\_H\_ \*/

[arch\_interface.h](arch__interface_8h.md)

[arm-gic.h](arm-gic_8h.md)

[gic.h](gic_8h.md)

Driver for ARM Generic Interrupt Controller.

[gic\_raise\_sgi](gic_8h.md#a08291705f002f01687cf507abbb410dc)

void gic\_raise\_sgi(unsigned int sgi\_id, uint64\_t target\_aff, uint16\_t target\_list)

raise SGI to target cores

[GICD\_SGIR](gic_8h.md#a5125b5f77951f0e882e002aac406beec)

#define GICD\_SGIR

**Definition** gic.h:127

[GICD\_SGIR\_SGIINTID](gic_8h.md#ae388207ec492448a22511cee6dcecedc)

#define GICD\_SGIR\_SGIINTID(x)

**Definition** gic.h:207

[GICD\_SGIR\_TGTFILT\_REQONLY](gic_8h.md#ae759ef6f311a7279db5e7ccd68c80863)

#define GICD\_SGIR\_TGTFILT\_REQONLY

**Definition** gic.h:199

[arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154)

static void arch\_nop(void)

Do nothing and return.

[arch\_curr\_cpu](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2)

static struct \_cpu \* arch\_curr\_cpu(void)

Return the CPU struct for the currently executing CPU.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[zassert\_true](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)

#define zassert\_true(cond,...)

Assert that cond is true.

**Definition** ztest\_assert.h:269

[MPIDR\_AFFLVL](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a35278aa57b0b98cd0cb541cfea58b177)

#define MPIDR\_AFFLVL(mpidr, aff\_level)

**Definition** cpu.h:93

[GET\_MPIDR](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a958d9c5f047f5dc318ecf4b171a68949)

#define GET\_MPIDR()

**Definition** cpu.h:96

[loapic.h](loapic_8h.md)

[x86\_write\_x2apic](loapic_8h.md#a060a375336bf44c2dde9537d32f9416d)

static void x86\_write\_x2apic(unsigned int reg, uint64\_t val)

Write 64-bit value to the local APIC in x2APIC mode.

**Definition** loapic.h:117

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
