---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arch_2arm_2irq_8h_source.html
original_path: doxygen/html/arch_2arm_2irq_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

28GTEXT([arch\_irq\_enable](arch_2arm_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa))

29GTEXT([arch\_irq\_disable](arch_2arm_2irq_8h.md#a19b436a206500c3748ad5c32050db241))

30GTEXT([arch\_irq\_is\_enabled](arch_2arm_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369))

31#if defined(CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER)

32GTEXT(z\_soc\_irq\_get\_active)

33GTEXT(z\_soc\_irq\_eoi)

34#endif /\* CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER \*/

35#else

36

37#if !defined(CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER)

[ 38](arch_2arm_2irq_8h.md#a9bdba7b8dc9e2f1fa15309f7ed5be0e3)extern void [arm\_irq\_enable](arch_2arm_2irq_8h.md#a9bdba7b8dc9e2f1fa15309f7ed5be0e3)(unsigned int irq);

[ 39](arch_2arm_2irq_8h.md#ab21a38f95ce639a300012017626d715c)extern void [arm\_irq\_disable](arch_2arm_2irq_8h.md#ab21a38f95ce639a300012017626d715c)(unsigned int irq);

[ 40](arch_2arm_2irq_8h.md#a7a9dd209281ffee41f196ac973972aa3)extern int [arm\_irq\_is\_enabled](arch_2arm_2irq_8h.md#a7a9dd209281ffee41f196ac973972aa3)(unsigned int irq);

[ 41](arch_2arm_2irq_8h.md#a5541a808bd36f598c9f4f93cee1231e5)extern void [arm\_irq\_priority\_set](arch_2arm_2irq_8h.md#a5541a808bd36f598c9f4f93cee1231e5)(unsigned int irq, unsigned int prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

42#if !defined(CONFIG\_MULTI\_LEVEL\_INTERRUPTS)

[ 43](arch_2arm_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)#define arch\_irq\_enable(irq) arm\_irq\_enable(irq)

[ 44](arch_2arm_2irq_8h.md#a19b436a206500c3748ad5c32050db241)#define arch\_irq\_disable(irq) arm\_irq\_disable(irq)

[ 45](arch_2arm_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)#define arch\_irq\_is\_enabled(irq) arm\_irq\_is\_enabled(irq)

46#define z\_arm\_irq\_priority\_set(irq, prio, flags) arm\_irq\_priority\_set(irq, prio, flags)

47#endif

48#endif

49

50#if defined(CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER) || defined(CONFIG\_MULTI\_LEVEL\_INTERRUPTS)

51/\*

52 \* When a custom interrupt controller or multi-level interrupts is specified,

53 \* map the architecture interrupt control functions to the SoC layer interrupt

54 \* control functions.

55 \*/

56

57void z\_soc\_irq\_init(void);

58void z\_soc\_irq\_enable(unsigned int irq);

59void z\_soc\_irq\_disable(unsigned int irq);

60int z\_soc\_irq\_is\_enabled(unsigned int irq);

61

62void z\_soc\_irq\_priority\_set(

63 unsigned int irq, unsigned int prio, unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

64

65unsigned int z\_soc\_irq\_get\_active(void);

66void z\_soc\_irq\_eoi(unsigned int irq);

67

68#define arch\_irq\_enable(irq) z\_soc\_irq\_enable(irq)

69#define arch\_irq\_disable(irq) z\_soc\_irq\_disable(irq)

70#define arch\_irq\_is\_enabled(irq) z\_soc\_irq\_is\_enabled(irq)

71

72#define z\_arm\_irq\_priority\_set(irq, prio, flags) \

73 z\_soc\_irq\_priority\_set(irq, prio, flags)

74

75#endif

76

77extern void z\_arm\_int\_exit(void);

78

79extern void z\_arm\_interrupt\_init(void);

80

81/\* Flags for use with IRQ\_CONNECT() \*/

[ 89](arch_2arm_2irq_8h.md#a1b5d8b88524f2fd81f32ed675c832a57)#define IRQ\_ZERO\_LATENCY BIT(0)

90

91#ifdef CONFIG\_CPU\_CORTEX\_M

92

93#if defined(CONFIG\_ZERO\_LATENCY\_LEVELS)

94#define ZERO\_LATENCY\_LEVELS CONFIG\_ZERO\_LATENCY\_LEVELS

95#else

96#define ZERO\_LATENCY\_LEVELS 1

97#endif

98

99#define \_CHECK\_PRIO(priority\_p, flags\_p) \

100 BUILD\_ASSERT(((flags\_p & IRQ\_ZERO\_LATENCY) && \

101 ((ZERO\_LATENCY\_LEVELS == 1) || \

102 (priority\_p < ZERO\_LATENCY\_LEVELS))) || \

103 (priority\_p <= IRQ\_PRIO\_LOWEST), \

104 "Invalid interrupt priority. Values must not exceed IRQ\_PRIO\_LOWEST");

105#else

106#define \_CHECK\_PRIO(priority\_p, flags\_p)

107#endif

108

109/\* All arguments must be computable by the compiler at build time.

110 \*

111 \* Z\_ISR\_DECLARE will populate the .intList section with the interrupt's

112 \* parameters, which will then be used by gen\_irq\_tables.py to create

113 \* the vector table and the software ISR table. This is all done at

114 \* build-time.

115 \*

116 \* We additionally set the priority in the interrupt controller at

117 \* runtime.

118 \*/

[ 119](arch_2arm_2irq_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

120{ \

121 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_ZERO\_LATENCY\_IRQS) || !(flags\_p & IRQ\_ZERO\_LATENCY), \

122 "ZLI interrupt registered but feature is disabled"); \

123 \_CHECK\_PRIO(priority\_p, flags\_p) \

124 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

125 z\_arm\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

126}

127

[ 128](arch_2arm_2irq_8h.md#a875f2b1ca924721fe3854796bd96c2db)#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

129{ \

130 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_ZERO\_LATENCY\_IRQS) || !(flags\_p & IRQ\_ZERO\_LATENCY), \

131 "ZLI interrupt registered but feature is disabled"); \

132 \_CHECK\_PRIO(priority\_p, flags\_p) \

133 Z\_ISR\_DECLARE\_DIRECT(irq\_p, ISR\_FLAG\_DIRECT, isr\_p); \

134 z\_arm\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

135}

136

137#ifdef CONFIG\_PM

138extern void \_arch\_isr\_direct\_pm(void);

139#define ARCH\_ISR\_DIRECT\_PM() \_arch\_isr\_direct\_pm()

140#else

[ 141](arch_2arm_2irq_8h.md#a491cb79acec18c83b9a61b0b45dfab69)#define ARCH\_ISR\_DIRECT\_PM() do { } while (false)

142#endif

143

[ 144](arch_2arm_2irq_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() arch\_isr\_direct\_header()

[ 145](arch_2arm_2irq_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)#define ARCH\_ISR\_DIRECT\_FOOTER(swap) arch\_isr\_direct\_footer(swap)

146

147/\* arch/arm/core/exc\_exit.S \*/

148extern void z\_arm\_int\_exit(void);

149

150#ifdef CONFIG\_TRACING\_ISR

151extern void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

152extern void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

153#endif

154

[ 155](arch_2arm_2irq_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)static inline void [arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)(void)

156{

157#ifdef CONFIG\_TRACING\_ISR

158 [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)();

159#endif

160}

161

[ 162](arch_2arm_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)static inline void [arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)(int maybe\_swap)

163{

164#ifdef CONFIG\_TRACING\_ISR

165 [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)();

166#endif

167 if (maybe\_swap != 0) {

168 z\_arm\_int\_exit();

169 }

170}

171

[ 172](arch_2arm_2irq_8h.md#aea327928797d5f8a059ee3578cff9f91)#define ARCH\_ISR\_DIAG\_OFF \

173 TOOLCHAIN\_DISABLE\_CLANG\_WARNING(TOOLCHAIN\_WARNING\_EXTRA) \

174 TOOLCHAIN\_DISABLE\_GCC\_WARNING(TOOLCHAIN\_WARNING\_ATTRIBUTES) \

175 TOOLCHAIN\_DISABLE\_IAR\_WARNING(TOOLCHAIN\_WARNING\_ATTRIBUTES)

[ 176](arch_2arm_2irq_8h.md#ad6a5dc7416190e63eb601df2d3eab164)#define ARCH\_ISR\_DIAG\_ON \

177 TOOLCHAIN\_ENABLE\_CLANG\_WARNING(TOOLCHAIN\_WARNING\_EXTRA) \

178 TOOLCHAIN\_ENABLE\_GCC\_WARNING(TOOLCHAIN\_WARNING\_ATTRIBUTES) \

179 TOOLCHAIN\_ENABLE\_IAR\_WARNING(TOOLCHAIN\_WARNING\_ATTRIBUTES)

180

[ 181](arch_2arm_2irq_8h.md#a5279598e93dd914614a2ae52557be1a5)#define ARCH\_ISR\_DIRECT\_DECLARE(name) \

182 static inline int name##\_body(void); \

183 ARCH\_ISR\_DIAG\_OFF \

184 \_\_attribute\_\_ ((interrupt ("IRQ"))) void name(void) \

185 { \

186 int check\_reschedule; \

187 ISR\_DIRECT\_HEADER(); \

188 check\_reschedule = name##\_body(); \

189 ISR\_DIRECT\_FOOTER(check\_reschedule); \

190 } \

191 ARCH\_ISR\_DIAG\_ON \

192 static inline int name##\_body(void)

193

194#if defined(CONFIG\_DYNAMIC\_DIRECT\_INTERRUPTS)

195

196extern void z\_arm\_irq\_direct\_dynamic\_dispatch\_reschedule(void);

197extern void z\_arm\_irq\_direct\_dynamic\_dispatch\_no\_reschedule(void);

198

251#define ARM\_IRQ\_DIRECT\_DYNAMIC\_CONNECT(irq\_p, priority\_p, flags\_p, resch) \

252 IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, \

253 \_CONCAT(z\_arm\_irq\_direct\_dynamic\_dispatch\_, resch), flags\_p)

254

255#endif /\* CONFIG\_DYNAMIC\_DIRECT\_INTERRUPTS \*/

256

257#if defined(CONFIG\_ARM\_SECURE\_FIRMWARE)

258/\* Architecture-specific definition for the target security

259 \* state of an NVIC IRQ line.

260 \*/

261typedef enum {

262 IRQ\_TARGET\_STATE\_SECURE = 0,

263 IRQ\_TARGET\_STATE\_NON\_SECURE

264} irq\_target\_state\_t;

265

266#endif /\* CONFIG\_ARM\_SECURE\_FIRMWARE \*/

267

268#endif /\* \_ASMLANGUAGE \*/

269

270#ifdef \_\_cplusplus

271}

272#endif

273

274#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_IRQ\_H\_ \*/

[arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)

static void arch\_isr\_direct\_header(void)

**Definition** irq.h:91

[arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)

static void arch\_isr\_direct\_footer(int maybe\_swap)

**Definition** irq.h:98

[arch\_irq\_disable](arch_2arm_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:44

[arm\_irq\_priority\_set](arch_2arm_2irq_8h.md#a5541a808bd36f598c9f4f93cee1231e5)

void arm\_irq\_priority\_set(unsigned int irq, unsigned int prio, uint32\_t flags)

[arch\_irq\_enable](arch_2arm_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:43

[arm\_irq\_is\_enabled](arch_2arm_2irq_8h.md#a7a9dd209281ffee41f196ac973972aa3)

int arm\_irq\_is\_enabled(unsigned int irq)

[arm\_irq\_enable](arch_2arm_2irq_8h.md#a9bdba7b8dc9e2f1fa15309f7ed5be0e3)

void arm\_irq\_enable(unsigned int irq)

[arm\_irq\_disable](arch_2arm_2irq_8h.md#ab21a38f95ce639a300012017626d715c)

void arm\_irq\_disable(unsigned int irq)

[arch\_irq\_is\_enabled](arch_2arm_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)

#define arch\_irq\_is\_enabled(irq)

**Definition** irq.h:45

[sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)

void sys\_trace\_isr\_enter(void)

Called when entering an ISR.

[sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)

void sys\_trace\_isr\_exit(void)

Called when exiting an ISR.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

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
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
