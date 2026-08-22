---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arch_2xtensa_2irq_8h_source.html
original_path: doxygen/html/arch_2xtensa_2irq_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h

[Go to the documentation of this file.](arch_2xtensa_2irq_8h.md)

1/\*

2 \* Copyright (c) 2016 Cadence Design Systems, Inc.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_IRQ\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_IRQ\_H\_

8

9#include <[stdint.h](stdint_8h.md)>

10

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12#include <xtensa/config/core-isa.h>

13

[ 14](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)#define CONFIG\_GEN\_IRQ\_START\_VECTOR 0

15

19

20/\*

21 \* Call these functions to enable the specified interrupts.

22 \*

23 \* mask - Bit mask of interrupts to be enabled.

24 \*/

25static inline void z\_xt\_ints\_on(unsigned int mask)

26{

27 int val;

28

29 \_\_asm\_\_ volatile("rsr.intenable %0" : "=r"(val));

30 val |= mask;

31 \_\_asm\_\_ volatile("wsr.intenable %0; rsync" : : "r"(val));

32}

33#if XCHAL\_NUM\_INTERRUPTS > 32

34static inline void z\_xt\_ints1\_on(unsigned int mask)

35{

36 int val;

37

38 \_\_asm\_\_ volatile("rsr.intenable1 %0" : "=r"(val));

39 val |= mask;

40 \_\_asm\_\_ volatile("wsr.intenable1 %0; rsync" : : "r"(val));

41}

42#endif

43#if XCHAL\_NUM\_INTERRUPTS > 64

44static inline void z\_xt\_ints2\_on(unsigned int mask)

45{

46 int val;

47

48 \_\_asm\_\_ volatile("rsr.intenable2 %0" : "=r"(val));

49 val |= mask;

50 \_\_asm\_\_ volatile("wsr.intenable2 %0; rsync" : : "r"(val));

51}

52#endif

53#if XCHAL\_NUM\_INTERRUPTS > 96

54static inline void z\_xt\_ints3\_on(unsigned int mask)

55{

56 int val;

57

58 \_\_asm\_\_ volatile("rsr.intenable3 %0" : "=r"(val));

59 val |= mask;

60 \_\_asm\_\_ volatile("wsr.intenable3 %0; rsync" : : "r"(val));

61}

62#endif

63

64

65/\*

66 \* Call these functions to disable the specified interrupts.

67 \*

68 \* mask - Bit mask of interrupts to be disabled.

69 \*/

70static inline void z\_xt\_ints\_off(unsigned int mask)

71{

72 int val;

73

74 \_\_asm\_\_ volatile("rsr.intenable %0" : "=r"(val));

75 val &= ~mask;

76 \_\_asm\_\_ volatile("wsr.intenable %0; rsync" : : "r"(val));

77}

78#if XCHAL\_NUM\_INTERRUPTS > 32

79static inline void z\_xt\_ints1\_off(unsigned int mask)

80{

81 int val;

82

83 \_\_asm\_\_ volatile("rsr.intenable1 %0" : "=r"(val));

84 val &= ~mask;

85 \_\_asm\_\_ volatile("wsr.intenable1 %0; rsync" : : "r"(val));

86}

87#endif

88#if XCHAL\_NUM\_INTERRUPTS > 64

89static inline void z\_xt\_ints2\_off(unsigned int mask)

90{

91 int val;

92

93 \_\_asm\_\_ volatile("rsr.intenable2 %0" : "=r"(val));

94 val &= ~mask;

95 \_\_asm\_\_ volatile("wsr.intenable2 %0; rsync" : : "r"(val));

96}

97#endif

98#if XCHAL\_NUM\_INTERRUPTS > 96

99static inline void z\_xt\_ints3\_off(unsigned int mask)

100{

101 int val;

102

103 \_\_asm\_\_ volatile("rsr.intenable3 %0" : "=r"(val));

104 val &= ~mask;

105 \_\_asm\_\_ volatile("wsr.intenable3 %0; rsync" : : "r"(val));

106}

107#endif

108

109

110/\*

111 \* Call these functions to set the specified (s/w) interrupt.

112 \*/

113static inline void z\_xt\_set\_intset(unsigned int arg)

114{

115#if XCHAL\_HAVE\_INTERRUPTS

116 \_\_asm\_\_ volatile("wsr.intset %0; rsync" : : "r"(arg));

117#else

118 ARG\_UNUSED(arg);

119#endif

120}

121#if XCHAL\_NUM\_INTERRUPTS > 32

122static inline void z\_xt\_set\_intset1(unsigned int arg)

123{

124 \_\_asm\_\_ volatile("wsr.intset1 %0; rsync" : : "r"(arg));

125}

126#endif

127#if XCHAL\_NUM\_INTERRUPTS > 64

128static inline void z\_xt\_set\_intset2(unsigned int arg)

129{

130 \_\_asm\_\_ volatile("wsr.intset2 %0; rsync" : : "r"(arg));

131}

132#endif

133#if XCHAL\_NUM\_INTERRUPTS > 96

134static inline void z\_xt\_set\_intset3(unsigned int arg)

135{

136 \_\_asm\_\_ volatile("wsr.intset3 %0; rsync" : : "r"(arg));

137}

138#endif

139

140

144

145#ifdef CONFIG\_MULTI\_LEVEL\_INTERRUPTS

146

147/\* for \_soc\_irq\_\*() \*/

148#include <soc.h>

149

150#ifdef CONFIG\_2ND\_LEVEL\_INTERRUPTS

151#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

152#define CONFIG\_NUM\_IRQS (XCHAL\_NUM\_INTERRUPTS +\

153 (CONFIG\_NUM\_2ND\_LEVEL\_AGGREGATORS +\

154 CONFIG\_NUM\_3RD\_LEVEL\_AGGREGATORS) \*\

155 CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR)

156#else

157#define CONFIG\_NUM\_IRQS (XCHAL\_NUM\_INTERRUPTS +\

158 CONFIG\_NUM\_2ND\_LEVEL\_AGGREGATORS \*\

159 CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR)

160#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

161#else

162#define CONFIG\_NUM\_IRQS XCHAL\_NUM\_INTERRUPTS

163#endif /\* CONFIG\_2ND\_LEVEL\_INTERRUPTS \*/

164

165void z\_soc\_irq\_init(void);

166void z\_soc\_irq\_enable(unsigned int irq);

167void z\_soc\_irq\_disable(unsigned int irq);

168int z\_soc\_irq\_is\_enabled(unsigned int irq);

169

170#define arch\_irq\_enable(irq) z\_soc\_irq\_enable(irq)

171#define arch\_irq\_disable(irq) z\_soc\_irq\_disable(irq)

172

173#define arch\_irq\_is\_enabled(irq) z\_soc\_irq\_is\_enabled(irq)

174

175#ifdef CONFIG\_DYNAMIC\_INTERRUPTS

176extern int z\_soc\_irq\_connect\_dynamic(unsigned int irq, unsigned int priority,

177 void (\*routine)(const void \*parameter),

178 const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

179#endif

180

181#else

182

[ 183](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837)#define CONFIG\_NUM\_IRQS XCHAL\_NUM\_INTERRUPTS

184

[ 185](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)#define arch\_irq\_enable(irq) xtensa\_irq\_enable(irq)

[ 186](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)#define arch\_irq\_disable(irq) xtensa\_irq\_disable(irq)

187

[ 188](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)#define arch\_irq\_is\_enabled(irq) xtensa\_irq\_is\_enabled(irq)

189

190#endif

191

[ 197](arch_2xtensa_2irq_8h.md#a9d6c92219fd2390f777aff106d2eafa9)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [xtensa\_irq\_enable](arch_2xtensa_2irq_8h.md#a9d6c92219fd2390f777aff106d2eafa9)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq)

198{

199#if XCHAL\_NUM\_INTERRUPTS > 32

200 switch (irq >> 5) {

201 case 0:

202 z\_xt\_ints\_on(1 << irq);

203 break;

204 case 1:

205 z\_xt\_ints1\_on(1 << irq);

206 break;

207#if XCHAL\_NUM\_INTERRUPTS > 64

208 case 2:

209 z\_xt\_ints2\_on(1 << irq);

210 break;

211#endif

212#if XCHAL\_NUM\_INTERRUPTS > 96

213 case 3:

214 z\_xt\_ints3\_on(1 << irq);

215 break;

216#endif

217 default:

218 break;

219 }

220#else

221 z\_xt\_ints\_on(1 << irq);

222#endif

223}

224

[ 230](arch_2xtensa_2irq_8h.md#a37d1c0641f471e9492c2493c77327c96)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [xtensa\_irq\_disable](arch_2xtensa_2irq_8h.md#a37d1c0641f471e9492c2493c77327c96)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq)

231{

232#if XCHAL\_NUM\_INTERRUPTS > 32

233 switch (irq >> 5) {

234 case 0:

235 z\_xt\_ints\_off(1 << irq);

236 break;

237 case 1:

238 z\_xt\_ints1\_off(1 << irq);

239 break;

240#if XCHAL\_NUM\_INTERRUPTS > 64

241 case 2:

242 z\_xt\_ints2\_off(1 << irq);

243 break;

244#endif

245#if XCHAL\_NUM\_INTERRUPTS > 96

246 case 3:

247 z\_xt\_ints3\_off(1 << irq);

248 break;

249#endif

250 default:

251 break;

252 }

253#else

254 z\_xt\_ints\_off(1 << irq);

255#endif

256}

257

[ 259](arch_2xtensa_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

260{

261 unsigned int key;

262

263 \_\_asm\_\_ volatile("rsil %0, %1"

264 : "=r"(key) : "i"(XCHAL\_EXCM\_LEVEL) : "memory");

265 return key;

266}

267

[ 269](arch_2xtensa_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

270{

271 \_\_asm\_\_ volatile("wsr.ps %0; rsync"

272 :: "r"(key) : "memory");

273}

274

[ 276](arch_2xtensa_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

277{

278 return (key & 0xf) == 0; /\* INTLEVEL field \*/

279}

280

[ 288](arch_2xtensa_2irq_8h.md#ae6e10f2a35e679c41c11700330ce8b7a)int [xtensa\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae6e10f2a35e679c41c11700330ce8b7a)(unsigned int irq);

289

290#include <[zephyr/irq.h](irq_8h.md)>

291

292#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_IRQ\_H\_ \*/

[arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

Disable all interrupts on the local CPU.

**Definition** irq.h:168

[arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** irq.h:176

[arch\_irq\_unlocked](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** irq.h:181

[xtensa\_irq\_disable](arch_2xtensa_2irq_8h.md#a37d1c0641f471e9492c2493c77327c96)

static ALWAYS\_INLINE void xtensa\_irq\_disable(uint32\_t irq)

Disable interrupt on Xtensa core.

**Definition** irq.h:230

[xtensa\_irq\_enable](arch_2xtensa_2irq_8h.md#a9d6c92219fd2390f777aff106d2eafa9)

static ALWAYS\_INLINE void xtensa\_irq\_enable(uint32\_t irq)

Enable interrupt on Xtensa core.

**Definition** irq.h:197

[xtensa\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae6e10f2a35e679c41c11700330ce8b7a)

int xtensa\_irq\_is\_enabled(unsigned int irq)

Query if an interrupt is enabled on Xtensa core.

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [irq.h](arch_2xtensa_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
