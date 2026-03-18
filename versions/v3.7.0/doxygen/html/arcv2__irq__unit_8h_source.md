---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arcv2__irq__unit_8h_source.html
original_path: doxygen/html/arcv2__irq__unit_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

47

48static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

49void z\_arc\_v2\_irq\_unit\_irq\_enable\_set(

50 int irq,

51 unsigned char enable

52 )

53{

54 unsigned int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

55

56 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

57 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_ENABLE, enable);

58

59 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

60}

61

67

68static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

69void z\_arc\_v2\_irq\_unit\_int\_enable(int irq)

70{

71 z\_arc\_v2\_irq\_unit\_irq\_enable\_set(irq, \_ARC\_V2\_INT\_ENABLE);

72}

73

79

80static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

81void z\_arc\_v2\_irq\_unit\_int\_disable(int irq)

82{

83 z\_arc\_v2\_irq\_unit\_irq\_enable\_set(irq, \_ARC\_V2\_INT\_DISABLE);

84}

85

93

94static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

95bool z\_arc\_v2\_irq\_unit\_int\_enabled(int irq)

96{

97 bool ret;

98 unsigned int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

99

100 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

101 ret = z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_ENABLE) & 0x1;

102

103 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

104

105 return ret;

106}

107

108

114

115static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

116void z\_arc\_v2\_irq\_unit\_prio\_set(int irq, unsigned char prio)

117{

118

119 unsigned int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

120

121 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

122#if defined(CONFIG\_ARC\_SECURE\_FIRMWARE)

123 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PRIORITY,

124 (z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_PRIORITY) & (~\_ARC\_V2\_INT\_PRIO\_MASK))

125 | prio);

126#else

127 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PRIORITY, prio);

128#endif

129 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

130}

131

132#if defined(CONFIG\_ARC\_SECURE\_FIRMWARE)

138static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

139void z\_arc\_v2\_irq\_uinit\_secure\_set(int irq, bool secure)

140{

141 unsigned int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

142

143 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

144

145 if (secure) {

146 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PRIORITY,

147 z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_PRIORITY) |

148 \_ARC\_V2\_IRQ\_PRIORITY\_SECURE);

149 } else {

150 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PRIORITY,

151 z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_PRIORITY) &

152 \_ARC\_V2\_INT\_PRIO\_MASK);

153 }

154

155 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

156}

157#endif

158

167

168static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

169void z\_arc\_v2\_irq\_unit\_sensitivity\_set(int irq, int [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))

170{

171 unsigned int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

172

173 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

174 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_TRIGGER, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

175

176 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

177}

178

179/\*

180 \* @brief Check whether processor in interrupt/exception state

181 \*

182 \* Check whether processor in interrupt/exception state

183 \*

184 \* @return 1 in interrupt/exception state; 0 not in

185 \*/

186static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

187bool z\_arc\_v2\_irq\_unit\_is\_in\_isr(void)

188{

189 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) act = z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_AUX\_IRQ\_ACT);

190

191 /\* in exception ?\*/

192 if (z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_STATUS32) & \_ARC\_V2\_STATUS32\_AE) {

193 return true;

194 }

195

196 return ((act & 0xffff) != 0U);

197}

198

206static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

207void z\_arc\_v2\_irq\_unit\_trigger\_set(int irq, unsigned int trigger)

208{

209 unsigned int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

210

211 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

212 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_TRIGGER, trigger);

213

214 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

215}

216

225static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

226unsigned int z\_arc\_v2\_irq\_unit\_trigger\_get(int irq)

227{

228 unsigned int ret;

229 unsigned int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

230

231 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

232 ret = z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_IRQ\_TRIGGER);

233

234 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

235

236 return ret;

237}

238

245static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

246void z\_arc\_v2\_irq\_unit\_int\_eoi(int irq)

247{

248 unsigned int key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

249

250 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_SELECT, irq);

251 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_IRQ\_PULSE\_CANCEL, 1);

252

253 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

254}

255

256#endif /\* \_ASMLANGUAGE \*/

257

258#ifdef \_\_cplusplus

259}

260#endif

261

262#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_ARCV2\_IRQ\_UNIT\_H\_ \*/

[arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

Disable all interrupts on the local CPU.

**Definition** irq.h:168

[arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** irq.h:176

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [arcv2\_irq\_unit.h](arcv2__irq__unit_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
