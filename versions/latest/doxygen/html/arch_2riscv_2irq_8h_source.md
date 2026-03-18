---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2riscv_2irq_8h_source.html
original_path: doxygen/html/arch_2riscv_2irq_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

21#ifndef \_ASMLANGUAGE

22#include <[zephyr/irq.h](irq_8h.md)>

23#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

24#include <[stdbool.h](stdbool_8h.md)>

25#endif /\* !\_ASMLANGUAGE \*/

26

27/\* Exceptions 0-15 (MCAUSE interrupt=0) \*/

28

29/\* Environment Call from U-mode \*/

[ 30](arch_2riscv_2irq_8h.md#a863dbd3dec399c9997dcabd96fe72330)#define RISCV\_EXC\_ECALLU 8

[ 32](arch_2riscv_2irq_8h.md#a29b9547cc078c8cb9ddcd234119df2dc)#define RISCV\_EXC\_ECALLM 11

33

34/\* IRQs 0-15 (MCAUSE interrupt=1) \*/

35

[ 37](arch_2riscv_2irq_8h.md#a720c7c1a9f6cea6575635614882c64f2)#define RISCV\_IRQ\_MSOFT 3

[ 39](arch_2riscv_2irq_8h.md#aeb7cd87a790fd623f63e098115da5d48)#define RISCV\_IRQ\_MEXT 11

40

41#ifdef CONFIG\_64BIT

42#define RISCV\_MCAUSE\_IRQ\_POS 63U

43#define RISCV\_MCAUSE\_IRQ\_BIT BIT64(RISCV\_MCAUSE\_IRQ\_POS)

44#else

[ 45](arch_2riscv_2irq_8h.md#ae8e815069f84cc2c7e4f7c98046c7726)#define RISCV\_MCAUSE\_IRQ\_POS 31U

[ 46](arch_2riscv_2irq_8h.md#a9a0d46c6f9f854a12aa13111ec9bc1bc)#define RISCV\_MCAUSE\_IRQ\_BIT BIT(RISCV\_MCAUSE\_IRQ\_POS)

47#endif

48

49#ifndef \_ASMLANGUAGE

50

[ 51](arch_2riscv_2irq_8h.md#aa278d630653b33cb339621d725ed295a)extern void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 52](arch_2riscv_2irq_8h.md#a216d692e87bfba955a60f8e570e127df)extern void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

[ 53](arch_2riscv_2irq_8h.md#a3bd8e963a124421bb372dab4bdc6cd83)extern int [arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)(unsigned int irq);

54

55#if defined(CONFIG\_RISCV\_HAS\_PLIC) || defined(CONFIG\_RISCV\_HAS\_CLIC)

56extern void z\_riscv\_irq\_priority\_set(unsigned int irq,

57 unsigned int prio,

58 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

59#else

60#define z\_riscv\_irq\_priority\_set(i, p, f) /\* Nothing \*/

61#endif /\* CONFIG\_RISCV\_HAS\_PLIC || CONFIG\_RISCV\_HAS\_CLIC \*/

62

[ 63](arch_2riscv_2irq_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

64{ \

65 Z\_ISR\_DECLARE(irq\_p + CONFIG\_RISCV\_RESERVED\_IRQ\_ISR\_TABLES\_OFFSET, \

66 0, isr\_p, isr\_param\_p); \

67 z\_riscv\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

68}

69

[ 70](arch_2riscv_2irq_8h.md#a875f2b1ca924721fe3854796bd96c2db)#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

71{ \

72 Z\_ISR\_DECLARE\_DIRECT(irq\_p + CONFIG\_RISCV\_RESERVED\_IRQ\_ISR\_TABLES\_OFFSET, \

73 ISR\_FLAG\_DIRECT, isr\_p); \

74 z\_riscv\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

75}

76

[ 77](arch_2riscv_2irq_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() arch\_isr\_direct\_header()

[ 78](arch_2riscv_2irq_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)#define ARCH\_ISR\_DIRECT\_FOOTER(swap) arch\_isr\_direct\_footer(swap)

79

80#ifdef CONFIG\_TRACING\_ISR

81extern void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

82extern void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

83#endif

84

[ 85](arch_2riscv_2irq_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)static inline void [arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)(void)

86{

87#ifdef CONFIG\_TRACING\_ISR

88 [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)();

89#endif

90 /\* We need to increment this so that arch\_is\_in\_isr() keeps working \*/

91 ++([arch\_curr\_cpu](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2)()->nested);

92}

93

94extern void \_\_soc\_handle\_irq(unsigned long mcause);

95

[ 96](arch_2riscv_2irq_8h.md#a13a88acdff251283bf6f364e4393adaf)static inline void [arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)(int swap)

97{

98 ARG\_UNUSED(swap);

99 unsigned long mcause;

100

101 /\* Get the IRQ number \*/

102 \_\_asm\_\_ volatile("csrr %0, mcause" : "=r" (mcause));

103 mcause &= CONFIG\_RISCV\_MCAUSE\_EXCEPTION\_MASK;

104

105 /\* Clear the pending IRQ \*/

106 \_\_soc\_handle\_irq(mcause);

107

108 /\* We are not in the ISR anymore \*/

109 --([arch\_curr\_cpu](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2)()->nested);

110

111#ifdef CONFIG\_TRACING\_ISR

112 [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)();

113#endif

114}

115

116/\*

117 \* TODO: Add support for rescheduling

118 \*/

[ 119](arch_2riscv_2irq_8h.md#a5279598e93dd914614a2ae52557be1a5)#define ARCH\_ISR\_DIRECT\_DECLARE(name) \

120 static inline int name##\_body(void); \

121 \_\_attribute\_\_ ((interrupt)) void name(void) \

122 { \

123 ISR\_DIRECT\_HEADER(); \

124 name##\_body(); \

125 ISR\_DIRECT\_FOOTER(0); \

126 } \

127 static inline int name##\_body(void)

128

129#endif /\* \_ASMLANGUAGE \*/

130

131#ifdef \_\_cplusplus

132}

133#endif

134

135#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_IRQ\_H\_ \*/

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

[arch\_curr\_cpu](group__arch-smp.md#gad42138d41dff6a4aad8abf7d77fcd8b2)

static struct \_cpu \* arch\_curr\_cpu(void)

Return the CPU struct for the currently executing CPU.

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [irq.h](arch_2riscv_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
