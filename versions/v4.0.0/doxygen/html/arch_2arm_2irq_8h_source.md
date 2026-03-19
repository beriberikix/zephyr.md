---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2arm_2irq_8h_source.html
original_path: doxygen/html/arch_2arm_2irq_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h

[Go to the documentation of this file.](arch_2arm_2irq_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \* Copyright (c) 2019 Nordic Semiconductor ASA.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_IRQ\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_IRQ\_H\_

18

19#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

20#include <[stdbool.h](stdbool_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26#ifdef \_ASMLANGUAGE

27GTEXT(z\_arm\_int\_exit);

28GTEXT([arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa))

29GTEXT([arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241))

30GTEXT([arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369))

31#if defined(CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER)

32GTEXT(z\_soc\_irq\_get\_active)

33GTEXT(z\_soc\_irq\_eoi)

34#endif /\* CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER \*/

35#else

36

37#if !defined(CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER)

38

[ 39](arch_2arm_2irq_8h.md#aa278d630653b33cb339621d725ed295a)extern void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 40](arch_2arm_2irq_8h.md#a216d692e87bfba955a60f8e570e127df)extern void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

[ 41](arch_2arm_2irq_8h.md#a3bd8e963a124421bb372dab4bdc6cd83)extern int [arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)(unsigned int irq);

42

43/\* internal routine documented in C file, needed by IRQ\_CONNECT() macro \*/

44extern void z\_arm\_irq\_priority\_set(unsigned int irq, unsigned int prio,

45 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

46

47#else

48

49/\*

50 \* When a custom interrupt controller is specified, map the architecture

51 \* interrupt control functions to the SoC layer interrupt control functions.

52 \*/

53

54void z\_soc\_irq\_init(void);

55void z\_soc\_irq\_enable(unsigned int irq);

56void z\_soc\_irq\_disable(unsigned int irq);

57int z\_soc\_irq\_is\_enabled(unsigned int irq);

58

59void z\_soc\_irq\_priority\_set(

60 unsigned int irq, unsigned int prio, unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

61

62unsigned int z\_soc\_irq\_get\_active(void);

63void z\_soc\_irq\_eoi(unsigned int irq);

64

65#define arch\_irq\_enable(irq) z\_soc\_irq\_enable(irq)

66#define arch\_irq\_disable(irq) z\_soc\_irq\_disable(irq)

67#define arch\_irq\_is\_enabled(irq) z\_soc\_irq\_is\_enabled(irq)

68

69#define z\_arm\_irq\_priority\_set(irq, prio, flags) \

70 z\_soc\_irq\_priority\_set(irq, prio, flags)

71

72#endif /\* !CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER \*/

73

74extern void z\_arm\_int\_exit(void);

75

76extern void z\_arm\_interrupt\_init(void);

77

78/\* Flags for use with IRQ\_CONNECT() \*/

[ 86](arch_2arm_2irq_8h.md#a1b5d8b88524f2fd81f32ed675c832a57)#define IRQ\_ZERO\_LATENCY BIT(0)

87

88#ifdef CONFIG\_CPU\_CORTEX\_M

89

90#if defined(CONFIG\_ZERO\_LATENCY\_LEVELS)

91#define ZERO\_LATENCY\_LEVELS CONFIG\_ZERO\_LATENCY\_LEVELS

92#else

93#define ZERO\_LATENCY\_LEVELS 1

94#endif

95

96#define \_CHECK\_PRIO(priority\_p, flags\_p) \

97 BUILD\_ASSERT(((flags\_p & IRQ\_ZERO\_LATENCY) && \

98 ((ZERO\_LATENCY\_LEVELS == 1) || \

99 (priority\_p < ZERO\_LATENCY\_LEVELS))) || \

100 (priority\_p <= IRQ\_PRIO\_LOWEST), \

101 "Invalid interrupt priority. Values must not exceed IRQ\_PRIO\_LOWEST");

102#else

103#define \_CHECK\_PRIO(priority\_p, flags\_p)

104#endif

105

106/\* All arguments must be computable by the compiler at build time.

107 \*

108 \* Z\_ISR\_DECLARE will populate the .intList section with the interrupt's

109 \* parameters, which will then be used by gen\_irq\_tables.py to create

110 \* the vector table and the software ISR table. This is all done at

111 \* build-time.

112 \*

113 \* We additionally set the priority in the interrupt controller at

114 \* runtime.

115 \*/

[ 116](arch_2arm_2irq_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

117{ \

118 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_ZERO\_LATENCY\_IRQS) || !(flags\_p & IRQ\_ZERO\_LATENCY), \

119 "ZLI interrupt registered but feature is disabled"); \

120 \_CHECK\_PRIO(priority\_p, flags\_p) \

121 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

122 z\_arm\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

123}

124

[ 125](arch_2arm_2irq_8h.md#a875f2b1ca924721fe3854796bd96c2db)#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

126{ \

127 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_ZERO\_LATENCY\_IRQS) || !(flags\_p & IRQ\_ZERO\_LATENCY), \

128 "ZLI interrupt registered but feature is disabled"); \

129 \_CHECK\_PRIO(priority\_p, flags\_p) \

130 Z\_ISR\_DECLARE\_DIRECT(irq\_p, ISR\_FLAG\_DIRECT, isr\_p); \

131 z\_arm\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

132}

133

134#ifdef CONFIG\_PM

135extern void \_arch\_isr\_direct\_pm(void);

136#define ARCH\_ISR\_DIRECT\_PM() \_arch\_isr\_direct\_pm()

137#else

[ 138](arch_2arm_2irq_8h.md#a491cb79acec18c83b9a61b0b45dfab69)#define ARCH\_ISR\_DIRECT\_PM() do { } while (false)

139#endif

140

[ 141](arch_2arm_2irq_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() arch\_isr\_direct\_header()

[ 142](arch_2arm_2irq_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)#define ARCH\_ISR\_DIRECT\_FOOTER(swap) arch\_isr\_direct\_footer(swap)

143

144/\* arch/arm/core/exc\_exit.S \*/

145extern void z\_arm\_int\_exit(void);

146

147#ifdef CONFIG\_TRACING\_ISR

148extern void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

149extern void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

150#endif

151

[ 152](arch_2arm_2irq_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)static inline void [arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)(void)

153{

154#ifdef CONFIG\_TRACING\_ISR

155 [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)();

156#endif

157}

158

[ 159](arch_2arm_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)static inline void [arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)(int maybe\_swap)

160{

161#ifdef CONFIG\_TRACING\_ISR

162 [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)();

163#endif

164 if (maybe\_swap != 0) {

165 z\_arm\_int\_exit();

166 }

167}

168

169#if defined(\_\_clang\_\_)

170#define ARCH\_ISR\_DIAG\_OFF \

171 \_Pragma("clang diagnostic push") \

172 \_Pragma("clang diagnostic ignored \"-Wextra\"")

173#define ARCH\_ISR\_DIAG\_ON \_Pragma("clang diagnostic pop")

174#elif defined(\_\_GNUC\_\_)

175#define ARCH\_ISR\_DIAG\_OFF \

176 \_Pragma("GCC diagnostic push") \

177 \_Pragma("GCC diagnostic ignored \"-Wattributes\"")

178#define ARCH\_ISR\_DIAG\_ON \_Pragma("GCC diagnostic pop")

179#else

[ 180](arch_2arm_2irq_8h.md#aea327928797d5f8a059ee3578cff9f91)#define ARCH\_ISR\_DIAG\_OFF

[ 181](arch_2arm_2irq_8h.md#ad6a5dc7416190e63eb601df2d3eab164)#define ARCH\_ISR\_DIAG\_ON

182#endif

183

[ 184](arch_2arm_2irq_8h.md#a5279598e93dd914614a2ae52557be1a5)#define ARCH\_ISR\_DIRECT\_DECLARE(name) \

185 static inline int name##\_body(void); \

186 ARCH\_ISR\_DIAG\_OFF \

187 \_\_attribute\_\_ ((interrupt ("IRQ"))) void name(void) \

188 { \

189 int check\_reschedule; \

190 ISR\_DIRECT\_HEADER(); \

191 check\_reschedule = name##\_body(); \

192 ISR\_DIRECT\_FOOTER(check\_reschedule); \

193 } \

194 ARCH\_ISR\_DIAG\_ON \

195 static inline int name##\_body(void)

196

197#if defined(CONFIG\_DYNAMIC\_DIRECT\_INTERRUPTS)

198

199extern void z\_arm\_irq\_direct\_dynamic\_dispatch\_reschedule(void);

200extern void z\_arm\_irq\_direct\_dynamic\_dispatch\_no\_reschedule(void);

201

248#define ARM\_IRQ\_DIRECT\_DYNAMIC\_CONNECT(irq\_p, priority\_p, flags\_p, resch) \

249 IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, \

250 \_CONCAT(z\_arm\_irq\_direct\_dynamic\_dispatch\_, resch), flags\_p)

251

252#endif /\* CONFIG\_DYNAMIC\_DIRECT\_INTERRUPTS \*/

253

254#if defined(CONFIG\_ARM\_SECURE\_FIRMWARE)

255/\* Architecture-specific definition for the target security

256 \* state of an NVIC IRQ line.

257 \*/

258typedef enum {

259 IRQ\_TARGET\_STATE\_SECURE = 0,

260 IRQ\_TARGET\_STATE\_NON\_SECURE

261} irq\_target\_state\_t;

262

263#endif /\* CONFIG\_ARM\_SECURE\_FIRMWARE \*/

264

265#endif /\* \_ASMLANGUAGE \*/

266

267#ifdef \_\_cplusplus

268}

269#endif

270

271#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_IRQ\_H\_ \*/

[arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)

static void arch\_isr\_direct\_header(void)

**Definition** irq.h:91

[arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)

static void arch\_isr\_direct\_footer(int maybe\_swap)

**Definition** irq.h:98

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:107

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:106

[arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)

#define arch\_irq\_is\_enabled(irq)

**Definition** irq.h:109

[sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)

void sys\_trace\_isr\_enter(void)

Called when entering an ISR.

[sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)

void sys\_trace\_isr\_exit(void)

Called when exiting an ISR.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [irq.h](arch_2arm_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
