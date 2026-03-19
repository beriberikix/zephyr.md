---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__esp32c3_8h_source.html
original_path: doxygen/html/intc__esp32c3_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_esp32c3.h

[Go to the documentation of this file.](intc__esp32c3_8h.md)

1/\*

2 \* Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_ESP32C3\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_ESP32C3\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12#include <soc.h>

13/\*

14 \* Interrupt allocation flags - These flags can be used to specify

15 \* which interrupt qualities the code calling esp\_intr\_alloc\* needs.

16 \*/

17

18/\* Keep the LEVELx values as they are here; they match up with (1<<level) \*/

[ 19](intc__esp32c3_8h.md#ab1ef5952bffcb1811d4f831b98ecf42a)#define ESP\_INTR\_FLAG\_LEVEL1 (1<<1) /\* Accept a Level 1 int vector, lowest priority \*/

[ 20](intc__esp32c3_8h.md#a8e4478d65d49a4f17fb77599764239e2)#define ESP\_INTR\_FLAG\_LEVEL2 (1<<2) /\* Accept a Level 2 int vector \*/

[ 21](intc__esp32c3_8h.md#a88ed1ea08351b07086a6e73a0487b0d8)#define ESP\_INTR\_FLAG\_LEVEL3 (1<<3) /\* Accept a Level 3 int vector \*/

[ 22](intc__esp32c3_8h.md#abb43226aa7d32763f17ee6a56090b322)#define ESP\_INTR\_FLAG\_LEVEL4 (1<<4) /\* Accept a Level 4 int vector \*/

[ 23](intc__esp32c3_8h.md#a44a1013070e7d9a06e8f08ed3f2cbca9)#define ESP\_INTR\_FLAG\_LEVEL5 (1<<5) /\* Accept a Level 5 int vector \*/

[ 24](intc__esp32c3_8h.md#a8defb5130273462e32ed399dece67024)#define ESP\_INTR\_FLAG\_LEVEL6 (1<<6) /\* Accept a Level 6 int vector \*/

[ 25](intc__esp32c3_8h.md#a9e57c700cf362161d807657571280abe)#define ESP\_INTR\_FLAG\_NMI (1<<7) /\* Accept a Level 7 int vector, highest priority \*/

[ 26](intc__esp32c3_8h.md#afc7bfcea2e621d81336ea6dd23310363)#define ESP\_INTR\_FLAG\_SHARED (1<<8) /\* Interrupt can be shared between ISRs \*/

[ 27](intc__esp32c3_8h.md#a0ab957dd5055fe20725624db223f9535)#define ESP\_INTR\_FLAG\_EDGE (1<<9) /\* Edge-triggered interrupt \*/

[ 28](intc__esp32c3_8h.md#a3fb8d6fa8b5e33b3503e86917bc8367b)#define ESP\_INTR\_FLAG\_IRAM (1<<10) /\* ISR can be called if cache is disabled \*/

[ 29](intc__esp32c3_8h.md#a76d024609ecd48dc17b586b91e779b88)#define ESP\_INTR\_FLAG\_INTRDISABLED (1<<11) /\* Return with this interrupt disabled \*/

30

31/\* Low and medium prio interrupts. These can be handled in C. \*/

[ 32](intc__esp32c3_8h.md#a9b0bc1a2b5cc22b499e041742ae1b17b)#define ESP\_INTR\_FLAG\_LOWMED (ESP\_INTR\_FLAG\_LEVEL1|ESP\_INTR\_FLAG\_LEVEL2|ESP\_INTR\_FLAG\_LEVEL3)

33

34/\* High level interrupts. Need to be handled in assembly. \*/

[ 35](intc__esp32c3_8h.md#a63b4eee1d70d2e9cb1dc0ecb41f40aa4)#define ESP\_INTR\_FLAG\_HIGH (ESP\_INTR\_FLAG\_LEVEL4|ESP\_INTR\_FLAG\_LEVEL5|ESP\_INTR\_FLAG\_LEVEL6| \

36 ESP\_INTR\_FLAG\_NMI)

37

38/\* Mask for all level flags \*/

[ 39](intc__esp32c3_8h.md#a610949ce2bf8d7adae528f816acc5725)#define ESP\_INTR\_FLAG\_LEVELMASK (ESP\_INTR\_FLAG\_LEVEL1|ESP\_INTR\_FLAG\_LEVEL2|ESP\_INTR\_FLAG\_LEVEL3| \

40 ESP\_INTR\_FLAG\_LEVEL4|ESP\_INTR\_FLAG\_LEVEL5|ESP\_INTR\_FLAG\_LEVEL6| \

41 ESP\_INTR\_FLAG\_NMI)

42

[ 43](intc__esp32c3_8h.md#a0da8577e46721fb23629536f175b6661)#define IRQ\_NA 0xFF /\* IRQ not available \*/

[ 44](intc__esp32c3_8h.md#aac65746f3615e2b6c23cfc6344293012)#define IRQ\_FREE 0xFE /\* IRQ available for use \*/

45

46/\*

47 \* Get the interrupt flags from the supplied priority.

48 \*/

[ 49](intc__esp32c3_8h.md#a447e94d9632ed5c38f1ea36cbc283c4a)#define ESP\_PRIO\_TO\_FLAGS(priority) \

50 ((priority) > 0 ? ((1 << (priority)) & ESP\_INTR\_FLAG\_LEVELMASK) : 0)

51

52/\*

53 \* Check interrupt flags from input and filter unallowed values.

54 \*/

[ 55](intc__esp32c3_8h.md#a4dac251442759ec39f07862b435e3dc1)#define ESP\_INT\_FLAGS\_CHECK(int\_flags) ((int\_flags) & ESP\_INTR\_FLAG\_SHARED)

56

57

58/\* Function prototype for interrupt handler function \*/

[ 59](intc__esp32c3_8h.md#ae96c682b20638830cd816926696e781a)typedef void (\*[isr\_handler\_t](intc__esp32c3_8h.md#ae96c682b20638830cd816926696e781a))(const void \*arg);

60

[ 64](intc__esp32c3_8h.md#aede8e7c90fd3138cf165a0eea1c920fe)void [esp\_intr\_initialize](intc__esp32c3_8h.md#aede8e7c90fd3138cf165a0eea1c920fe)(void);

65

[ 91](intc__esp32c3_8h.md#aa2dbfcb97856d74deaf1054cdc5521a5)int [esp\_intr\_alloc](intc__esp32c3_8h.md#aa2dbfcb97856d74deaf1054cdc5521a5)(int source,

92 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

93 [isr\_handler\_t](intc__esp32c3_8h.md#ae96c682b20638830cd816926696e781a) handler,

94 void \*arg,

95 void \*\*ret\_handle);

96

[ 105](intc__esp32c3_8h.md#abaf6326b21c234959e34e8bef32987be)int [esp\_intr\_disable](intc__esp32c3_8h.md#abaf6326b21c234959e34e8bef32987be)(int source);

106

[ 114](intc__esp32c3_8h.md#af52c1b16bd4c4d05167401e34bf03983)int [esp\_intr\_enable](intc__esp32c3_8h.md#af52c1b16bd4c4d05167401e34bf03983)(int source);

115

[ 122](intc__esp32c3_8h.md#ae5cd92e8d61acc30607bf4acdb992aaa)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esp\_intr\_get\_enabled\_intmask](intc__esp32c3_8h.md#ae5cd92e8d61acc30607bf4acdb992aaa)(int status\_mask\_number);

123

124#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_ESP32C3\_H\_ \*/

[esp\_intr\_alloc](intc__esp32c3_8h.md#aa2dbfcb97856d74deaf1054cdc5521a5)

int esp\_intr\_alloc(int source, int flags, isr\_handler\_t handler, void \*arg, void \*\*ret\_handle)

Allocate an interrupt with the given parameters.

[esp\_intr\_disable](intc__esp32c3_8h.md#abaf6326b21c234959e34e8bef32987be)

int esp\_intr\_disable(int source)

Disable the interrupt associated with the source.

[esp\_intr\_get\_enabled\_intmask](intc__esp32c3_8h.md#ae5cd92e8d61acc30607bf4acdb992aaa)

uint32\_t esp\_intr\_get\_enabled\_intmask(int status\_mask\_number)

Gets the current enabled interrupts.

[isr\_handler\_t](intc__esp32c3_8h.md#ae96c682b20638830cd816926696e781a)

void(\* isr\_handler\_t)(const void \*arg)

**Definition** intc\_esp32c3.h:59

[esp\_intr\_initialize](intc__esp32c3_8h.md#aede8e7c90fd3138cf165a0eea1c920fe)

void esp\_intr\_initialize(void)

Initializes interrupt table to its defaults.

[esp\_intr\_enable](intc__esp32c3_8h.md#af52c1b16bd4c4d05167401e34bf03983)

int esp\_intr\_enable(int source)

Enable the interrupt associated with the source.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_esp32c3.h](intc__esp32c3_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
