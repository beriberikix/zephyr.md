---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2arc_2v2_2irq_8h_source.html
original_path: doxygen/html/arch_2arc_2v2_2irq_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h

[Go to the documentation of this file.](arch_2arc_2v2_2irq_8h.md)

1/\*

2 \* Copyright (c) 2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_IRQ\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_IRQ\_H\_

16

17#include <[zephyr/arch/arc/v2/aux\_regs.h](aux__regs_8h.md)>

18#include <[zephyr/toolchain/common.h](common_8h.md)>

19#include <[zephyr/irq.h](irq_8h.md)>

20#include <[zephyr/sys/util.h](util_8h.md)>

21#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 27](arch_2arc_2v2_2irq_8h.md#a55147bf8ba1fd1bb0beef93b7c21c6c2)#define ARC\_MP\_PRIMARY\_CPU\_ID 0

28

29#ifndef \_ASMLANGUAGE

30

31extern void z\_arc\_firq\_stack\_set(void);

[ 32](arch_2arc_2v2_2irq_8h.md#aa278d630653b33cb339621d725ed295a)extern void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 33](arch_2arc_2v2_2irq_8h.md#a216d692e87bfba955a60f8e570e127df)extern void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

[ 34](arch_2arc_2v2_2irq_8h.md#a3bd8e963a124421bb372dab4bdc6cd83)extern int [arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)(unsigned int irq);

35#ifdef CONFIG\_TRACING\_ISR

36extern void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

37extern void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

38#endif

39

40extern void z\_irq\_priority\_set(unsigned int irq, unsigned int prio,

41 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

42

43/\* Z\_ISR\_DECLARE will populate the .intList section with the interrupt's

44 \* parameters, which will then be used by gen\_irq\_tables.py to create

45 \* the vector table and the software ISR table. This is all done at

46 \* build-time.

47 \*

48 \* We additionally set the priority in the interrupt controller at

49 \* runtime.

50 \*/

[ 51](arch_2arc_2v2_2irq_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

52{ \

53 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

54 z\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

55}

56

[ 78](arch_2arc_2v2_2irq_8h.md#a875f2b1ca924721fe3854796bd96c2db)#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

79{ \

80 Z\_ISR\_DECLARE\_DIRECT(irq\_p, ISR\_FLAG\_DIRECT, isr\_p); \

81 BUILD\_ASSERT(priority\_p || !IS\_ENABLED(CONFIG\_ARC\_FIRQ) || \

82 (IS\_ENABLED(CONFIG\_ARC\_FIRQ\_STACK) && \

83 !IS\_ENABLED(CONFIG\_ARC\_STACK\_CHECKING)), \

84 "irq priority cannot be set to 0 when CONFIG\_ARC\_FIRQ\_STACK" \

85 "is not configured or CONFIG\_ARC\_FIRQ\_STACK " \

86 "and CONFIG\_ARC\_STACK\_CHECKING are configured together"); \

87 z\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

88}

89

90

[ 91](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)static inline void [arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)(void)

92{

93#ifdef CONFIG\_TRACING\_ISR

94 [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)();

95#endif

96}

97

[ 98](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)static inline void [arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)(int maybe\_swap)

99{

100 /\* clear SW generated interrupt \*/

101 if (z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_ICAUSE) ==

102 z\_arc\_v2\_aux\_reg\_read(\_ARC\_V2\_AUX\_IRQ\_HINT)) {

103 z\_arc\_v2\_aux\_reg\_write(\_ARC\_V2\_AUX\_IRQ\_HINT, 0);

104 }

105#ifdef CONFIG\_TRACING\_ISR

106 [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)();

107#endif

108}

109

[ 110](arch_2arc_2v2_2irq_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() arch\_isr\_direct\_header()

111extern void [arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)(void);

112

[ 113](arch_2arc_2v2_2irq_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)#define ARCH\_ISR\_DIRECT\_FOOTER(swap) arch\_isr\_direct\_footer(swap)

114

115#if defined(\_\_CCAC\_\_)

116#define \_ARC\_DIRECT\_ISR\_FUNC\_ATTRIBUTE \_\_interrupt\_\_

117#else

118#define \_ARC\_DIRECT\_ISR\_FUNC\_ATTRIBUTE interrupt("ilink")

119#endif

120

121/\*

122 \* Scheduling can not be done in direct isr. If required, please use kernel

123 \* aware interrupt handling

124 \*/

[ 125](arch_2arc_2v2_2irq_8h.md#a5279598e93dd914614a2ae52557be1a5)#define ARCH\_ISR\_DIRECT\_DECLARE(name) \

126 static inline int name##\_body(void); \

127 \_\_attribute\_\_ ((\_ARC\_DIRECT\_ISR\_FUNC\_ATTRIBUTE))void name(void) \

128 { \

129 ISR\_DIRECT\_HEADER(); \

130 name##\_body(); \

131 ISR\_DIRECT\_FOOTER(0); \

132 } \

133 static inline int name##\_body(void)

134

135

167

[ 168](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

169{

170 unsigned int key;

171

172 \_\_asm\_\_ volatile("clri %0" : "=r"(key):: "memory");

173 return key;

174}

175

[ 176](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

177{

178 \_\_asm\_\_ volatile("seti %0" : : "ir"(key) : "memory");

179}

180

[ 181](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

182{

183 /\* ARC irq lock uses instruction "clri r0",

184 \* r0 == {26’d0, 1’b1, STATUS32.IE, STATUS32.E[3:0] }

185 \* bit4 is used to record IE (Interrupt Enable) bit

186 \*/

187 return (key & 0x10) == 0x10;

188}

189

190#endif /\* \_ASMLANGUAGE \*/

191

192#ifdef \_\_cplusplus

193}

194#endif

195

196#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_IRQ\_H\_ \*/

[arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

Disable all interrupts on the local CPU.

**Definition** irq.h:168

[arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** irq.h:176

[arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)

static void arch\_isr\_direct\_header(void)

**Definition** irq.h:91

[arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)

static void arch\_isr\_direct\_footer(int maybe\_swap)

**Definition** irq.h:98

[arch\_irq\_unlocked](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** irq.h:181

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:107

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:106

[arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)

#define arch\_irq\_is\_enabled(irq)

**Definition** irq.h:109

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

[common.h](common_8h.md)

Common toolchain abstraction.

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)

void sys\_trace\_isr\_enter(void)

Called when entering an ISR.

[sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)

void sys\_trace\_isr\_exit(void)

Called when exiting an ISR.

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [irq.h](arch_2arc_2v2_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
