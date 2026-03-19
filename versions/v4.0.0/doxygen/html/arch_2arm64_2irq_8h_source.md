---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2arm64_2irq_8h_source.html
original_path: doxygen/html/arch_2arm64_2irq_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h

[Go to the documentation of this file.](arch_2arm64_2irq_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_IRQ\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_IRQ\_H\_

17

18#include <[zephyr/irq.h](irq_8h.md)>

19#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

20#include <[stdbool.h](stdbool_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26#ifdef \_ASMLANGUAGE

27GTEXT([arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa))

28GTEXT([arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241))

29GTEXT([arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369))

30#if defined(CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER)

31GTEXT(z\_soc\_irq\_get\_active)

32GTEXT(z\_soc\_irq\_eoi)

33#endif /\* CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER \*/

34#else

35

36#if !defined(CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER)

37

[ 38](arch_2arm64_2irq_8h.md#aa278d630653b33cb339621d725ed295a)extern void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 39](arch_2arm64_2irq_8h.md#a216d692e87bfba955a60f8e570e127df)extern void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

[ 40](arch_2arm64_2irq_8h.md#a3bd8e963a124421bb372dab4bdc6cd83)extern int [arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)(unsigned int irq);

41

42/\* internal routine documented in C file, needed by IRQ\_CONNECT() macro \*/

43extern void z\_arm64\_irq\_priority\_set(unsigned int irq, unsigned int prio,

44 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

45

46#else

47

48/\*

49 \* When a custom interrupt controller is specified, map the architecture

50 \* interrupt control functions to the SoC layer interrupt control functions.

51 \*/

52

53void z\_soc\_irq\_init(void);

54void z\_soc\_irq\_enable(unsigned int irq);

55void z\_soc\_irq\_disable(unsigned int irq);

56int z\_soc\_irq\_is\_enabled(unsigned int irq);

57

58void z\_soc\_irq\_priority\_set(

59 unsigned int irq, unsigned int prio, unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

60

61unsigned int z\_soc\_irq\_get\_active(void);

62void z\_soc\_irq\_eoi(unsigned int irq);

63

64#define arch\_irq\_enable(irq) z\_soc\_irq\_enable(irq)

65#define arch\_irq\_disable(irq) z\_soc\_irq\_disable(irq)

66#define arch\_irq\_is\_enabled(irq) z\_soc\_irq\_is\_enabled(irq)

67

68#define z\_arm64\_irq\_priority\_set(irq, prio, flags) \

69 z\_soc\_irq\_priority\_set(irq, prio, flags)

70

71#endif /\* !CONFIG\_ARM\_CUSTOM\_INTERRUPT\_CONTROLLER \*/

72

73extern void z\_arm64\_interrupt\_init(void);

74

75/\* All arguments must be computable by the compiler at build time.

76 \*

77 \* Z\_ISR\_DECLARE will populate the .intList section with the interrupt's

78 \* parameters, which will then be used by gen\_irq\_tables.py to create

79 \* the vector table and the software ISR table. This is all done at

80 \* build-time.

81 \*

82 \* We additionally set the priority in the interrupt controller at

83 \* runtime.

84 \*/

[ 85](arch_2arm64_2irq_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

86{ \

87 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

88 z\_arm64\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

89}

90

91#endif /\* \_ASMLANGUAGE \*/

92

93#ifdef \_\_cplusplus

94}

95#endif

96

97#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_IRQ\_H\_ \*/

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:107

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:106

[arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)

#define arch\_irq\_is\_enabled(irq)

**Definition** irq.h:109

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
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [irq.h](arch_2arm64_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
