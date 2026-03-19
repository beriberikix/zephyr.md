---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2riscv_2irq_8h_source.html
original_path: doxygen/html/arch_2riscv_2irq_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h

[Go to the documentation of this file.](arch_2riscv_2irq_8h.md)

1/\*

2 \* Copyright (c) 2022 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_IRQ\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_IRQ\_H\_

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

22

23#ifndef \_ASMLANGUAGE

24#include <[zephyr/irq.h](irq_8h.md)>

25#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

26#include <[stdbool.h](stdbool_8h.md)>

27#endif /\* !\_ASMLANGUAGE \*/

28

29/\* Exceptions 0-15 (MCAUSE interrupt=0) \*/

30

31/\* Environment Call from U-mode \*/

[ 32](arch_2riscv_2irq_8h.md#a863dbd3dec399c9997dcabd96fe72330)#define RISCV\_EXC\_ECALLU 8

[ 34](arch_2riscv_2irq_8h.md#a29b9547cc078c8cb9ddcd234119df2dc)#define RISCV\_EXC\_ECALLM 11

35

36/\* IRQs 0-15 (MCAUSE interrupt=1) \*/

37

[ 39](arch_2riscv_2irq_8h.md#a720c7c1a9f6cea6575635614882c64f2)#define RISCV\_IRQ\_MSOFT 3

[ 41](arch_2riscv_2irq_8h.md#aeb7cd87a790fd623f63e098115da5d48)#define RISCV\_IRQ\_MEXT 11

42

43#ifdef CONFIG\_64BIT

44#define RISCV\_MCAUSE\_IRQ\_POS 63U

45#define RISCV\_MCAUSE\_IRQ\_BIT BIT64(RISCV\_MCAUSE\_IRQ\_POS)

46#else

[ 47](arch_2riscv_2irq_8h.md#ae8e815069f84cc2c7e4f7c98046c7726)#define RISCV\_MCAUSE\_IRQ\_POS 31U

[ 48](arch_2riscv_2irq_8h.md#a9a0d46c6f9f854a12aa13111ec9bc1bc)#define RISCV\_MCAUSE\_IRQ\_BIT BIT(RISCV\_MCAUSE\_IRQ\_POS)

49#endif

50

51#ifndef \_ASMLANGUAGE

52

[ 53](arch_2riscv_2irq_8h.md#aa278d630653b33cb339621d725ed295a)extern void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 54](arch_2riscv_2irq_8h.md#a216d692e87bfba955a60f8e570e127df)extern void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

[ 55](arch_2riscv_2irq_8h.md#a3bd8e963a124421bb372dab4bdc6cd83)extern int [arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)(unsigned int irq);

56

57#if defined(CONFIG\_RISCV\_HAS\_PLIC) || defined(CONFIG\_RISCV\_HAS\_CLIC)

58extern void z\_riscv\_irq\_priority\_set(unsigned int irq,

59 unsigned int prio,

60 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

61#else

62#define z\_riscv\_irq\_priority\_set(i, p, f) /\* Nothing \*/

63#endif /\* CONFIG\_RISCV\_HAS\_PLIC || CONFIG\_RISCV\_HAS\_CLIC \*/

64

65#ifdef CONFIG\_RISCV\_HAS\_CLIC

66extern void z\_riscv\_irq\_vector\_set(unsigned int irq);

67#else

68#define z\_riscv\_irq\_vector\_set(i) /\* Nothing \*/

69#endif /\* CONFIG\_RISCV\_HAS\_CLIC \*/

70

[ 71](arch_2riscv_2irq_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

72{ \

73 Z\_ISR\_DECLARE(irq\_p + CONFIG\_RISCV\_RESERVED\_IRQ\_ISR\_TABLES\_OFFSET, \

74 0, isr\_p, isr\_param\_p); \

75 z\_riscv\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

76}

77

[ 78](arch_2riscv_2irq_8h.md#a875f2b1ca924721fe3854796bd96c2db)#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

79{ \

80 Z\_ISR\_DECLARE\_DIRECT(irq\_p + CONFIG\_RISCV\_RESERVED\_IRQ\_ISR\_TABLES\_OFFSET, \

81 ISR\_FLAG\_DIRECT, isr\_p); \

82 z\_riscv\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

83 z\_riscv\_irq\_vector\_set(irq\_p); \

84}

85

[ 86](arch_2riscv_2irq_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() arch\_isr\_direct\_header()

[ 87](arch_2riscv_2irq_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)#define ARCH\_ISR\_DIRECT\_FOOTER(swap) arch\_isr\_direct\_footer(swap)

88

89#ifdef CONFIG\_TRACING\_ISR

90extern void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

91extern void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

92#endif

93

[ 94](arch_2riscv_2irq_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)static inline void [arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)(void)

95{

96#ifdef CONFIG\_TRACING\_ISR

97 [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)();

98#endif

99 /\* We need to increment this so that arch\_is\_in\_isr() keeps working \*/

100 ++([arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)()->nested);

101}

102

103extern void \_\_soc\_handle\_irq(unsigned long mcause);

104

[ 105](arch_2riscv_2irq_8h.md#a13a88acdff251283bf6f364e4393adaf)static inline void [arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)(int swap)

106{

107 ARG\_UNUSED(swap);

108 unsigned long mcause;

109

110 /\* Get the IRQ number \*/

111 \_\_asm\_\_ volatile("csrr %0, mcause" : "=r" (mcause));

112 mcause &= CONFIG\_RISCV\_MCAUSE\_EXCEPTION\_MASK;

113

114 /\* Clear the pending IRQ \*/

115 \_\_soc\_handle\_irq(mcause);

116

117 /\* We are not in the ISR anymore \*/

118 --([arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)()->nested);

119

120#ifdef CONFIG\_TRACING\_ISR

121 [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)();

122#endif

123}

124

125/\*

126 \* TODO: Add support for rescheduling

127 \*/

[ 128](arch_2riscv_2irq_8h.md#a5279598e93dd914614a2ae52557be1a5)#define ARCH\_ISR\_DIRECT\_DECLARE(name) \

129 static inline int name##\_body(void); \

130 \_\_attribute\_\_ ((interrupt)) void name(void) \

131 { \

132 ISR\_DIRECT\_HEADER(); \

133 name##\_body(); \

134 ISR\_DIRECT\_FOOTER(0); \

135 } \

136 static inline int name##\_body(void)

137

138#endif /\* \_ASMLANGUAGE \*/

139

140#ifdef \_\_cplusplus

141}

142#endif

143

144#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_IRQ\_H\_ \*/

[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)

static ALWAYS\_INLINE \_cpu\_t \* arch\_curr\_cpu(void)

**Definition** arch\_inlines.h:17

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

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [irq.h](arch_2riscv_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
