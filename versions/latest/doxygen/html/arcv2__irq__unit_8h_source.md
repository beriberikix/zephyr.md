---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arcv2__irq__unit_8h_source.html
original_path: doxygen/html/arcv2__irq__unit_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arcv2\_irq\_unit.h

[Go to the documentation of this file.](arcv2__irq__unit_8h.md)

1/\* arcv2\_irq\_unit.h - ARCv2 Interrupt Unit device driver \*/

2

3/\*

4 \* Copyright (c) 2014 Wind River Systems, Inc.

5 \* Copyright (c) 2020 Synopsys.

6 \*

7 \* SPDX-License-Identifier: Apache-2.0

8 \*/

9

10#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ARCV2\_IRQ\_UNIT\_H\_

11#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ARCV2\_IRQ\_UNIT\_H\_

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17/\* configuration flags for interrupt unit \*/

18#define \_ARC\_V2\_INT\_PRIO\_MASK 0xf

19#define \_ARC\_V2\_INT\_DISABLE 0

20#define \_ARC\_V2\_INT\_ENABLE 1

21

22#define \_ARC\_V2\_INT\_LEVEL 0

23#define \_ARC\_V2\_INT\_PULSE 1

24

25#ifndef \_ASMLANGUAGE

26

27/\*

28 \* NOTE:

29 \*

30 \* All APIs provided by this file are protected with INTERRUPTS LOCKED. The

31 \* APIs themselves are writing the IRQ\_SELECT, selecting which IRQ's registers

32 \* it wants to write to, then write to them: THIS IS NOT AN ATOMIC OPERATION.

33 \*

34 \* Locking the interrupts inside of the APIs are some kind of self-protection

35 \* to guarantee the correctness of operation if the callers don't lock

36 \* the interrupt.

37 \*

38 \*/

39

45

46static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

47void z\_arc\_v2\_irq\_unit\_irq\_enable\_set(

48 int irq,

49 unsigned char enable

50 )

51{

52 unsigned int key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

53

54 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

55 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_ENABLE, enable);

56

57 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

58}

59

65

66static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

67void z\_arc\_v2\_irq\_unit\_int\_enable(int irq)

68{

69 z\_arc\_v2\_irq\_unit\_irq\_enable\_set(irq, \_ARC\_V2\_INT\_ENABLE);

70}

71

77

78static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

79void z\_arc\_v2\_irq\_unit\_int\_disable(int irq)

80{

81 z\_arc\_v2\_irq\_unit\_irq\_enable\_set(irq, \_ARC\_V2\_INT\_DISABLE);

82}

83

91

92static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

93bool z\_arc\_v2\_irq\_unit\_int\_enabled(int irq)

94{

95 bool ret;

96 unsigned int key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

97

98 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

99 ret = z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_ENABLE) & 0x1;

100

101 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

102

103 return ret;

104}

105

106

112

113static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

114void z\_arc\_v2\_irq\_unit\_prio\_set(int irq, unsigned char prio)

115{

116

117 unsigned int key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

118

119 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

120#if defined(CONFIG\_ARC\_SECURE\_FIRMWARE)

121 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PRIORITY,

122 (z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_PRIORITY) & (~\_ARC\_V2\_INT\_PRIO\_MASK))

123 | prio);

124#else

125 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PRIORITY, prio);

126#endif

127 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

128}

129

130#if defined(CONFIG\_ARC\_SECURE\_FIRMWARE)

136static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

137void z\_arc\_v2\_irq\_uinit\_secure\_set(int irq, bool secure)

138{

139 unsigned int key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

140

141 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

142

143 if (secure) {

144 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PRIORITY,

145 z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_PRIORITY) |

146 \_ARC\_V2\_IRQ\_PRIORITY\_SECURE);

147 } else {

148 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PRIORITY,

149 z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_PRIORITY) &

150 \_ARC\_V2\_INT\_PRIO\_MASK);

151 }

152

153 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

154}

155#endif

156

165

166static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

167void z\_arc\_v2\_irq\_unit\_sensitivity\_set(int irq, int [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))

168{

169 unsigned int key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

170

171 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

172 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_TRIGGER, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

173

174 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

175}

176

177/\*

178 \* @brief Check whether processor in interrupt/exception state

179 \*

180 \* Check whether processor in interrupt/exception state

181 \*

182 \* @return 1 in interrupt/exception state; 0 not in

183 \*/

184static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

185bool z\_arc\_v2\_irq\_unit\_is\_in\_isr(void)

186{

187 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) act = z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_AUX\_IRQ\_ACT);

188

189 /\* in exception ?\*/

190 if (z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_STATUS32) & \_ARC\_V2\_STATUS32\_AE) {

191 return true;

192 }

193

194 return ((act & 0xffff) != 0U);

195}

196

204static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

205void z\_arc\_v2\_irq\_unit\_trigger\_set(int irq, unsigned int trigger)

206{

207 unsigned int key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

208

209 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

210 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_TRIGGER, trigger);

211

212 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

213}

214

223static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

224unsigned int z\_arc\_v2\_irq\_unit\_trigger\_get(int irq)

225{

226 unsigned int ret;

227 unsigned int key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

228

229 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

230 ret = z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_TRIGGER);

231

232 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

233

234 return ret;

235}

236

243static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

244void z\_arc\_v2\_irq\_unit\_int\_eoi(int irq)

245{

246 unsigned int key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

247

248 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

249 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PULSE\_CANCEL, 1);

250

251 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

252}

253

254#endif /\* \_ASMLANGUAGE \*/

255

256#ifdef \_\_cplusplus

257}

258#endif

259

260#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ARCV2\_IRQ\_UNIT\_H\_ \*/

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)

static unsigned int arch\_irq\_lock(void)

Lock interrupts on the current CPU.

[arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)

static void arch\_irq\_unlock(unsigned int key)

Unlock interrupts on the current CPU.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [arcv2\_irq\_unit.h](arcv2__irq__unit_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
