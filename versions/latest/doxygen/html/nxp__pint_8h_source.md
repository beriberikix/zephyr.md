---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nxp__pint_8h_source.html
original_path: doxygen/html/nxp__pint_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_pint.h

[Go to the documentation of this file.](nxp__pint_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_NXP\_PINT\_H\_

20#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_NXP\_PINT\_H\_

21

22#include <fsl\_pint.h>

23

[ 29](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7c)enum [nxp\_pint\_trigger](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7c) {

30 /\* Do not generate Pin Interrupt \*/

[ 31](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca8594c4bbe2858dd19a176d851a6175c5) [NXP\_PINT\_NONE](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca8594c4bbe2858dd19a176d851a6175c5) = kPINT\_PinIntEnableNone,

32 /\* Generate Pin Interrupt on rising edge \*/

[ 33](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca20ed11aa9c65c91d30b169ae8a754d40) [NXP\_PINT\_RISING](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca20ed11aa9c65c91d30b169ae8a754d40) = kPINT\_PinIntEnableRiseEdge,

34 /\* Generate Pin Interrupt on falling edge \*/

[ 35](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7caf77211604686c8e8f16616b25b9ada9e) [NXP\_PINT\_FALLING](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7caf77211604686c8e8f16616b25b9ada9e) = kPINT\_PinIntEnableFallEdge,

36 /\* Generate Pin Interrupt on both edges \*/

[ 37](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7caabce56e3c8a6ba8801b0700bfbf52ec2) [NXP\_PINT\_BOTH](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7caabce56e3c8a6ba8801b0700bfbf52ec2) = kPINT\_PinIntEnableBothEdges,

38 /\* Generate Pin Interrupt on low level \*/

[ 39](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca115385d1645fa1901b7ffeab07ff6ce7) [NXP\_PINT\_LOW](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca115385d1645fa1901b7ffeab07ff6ce7) = kPINT\_PinIntEnableLowLevel,

40 /\* Generate Pin Interrupt on high level \*/

[ 41](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7cad94f208bdf7029063172c88673d28b24) [NXP\_PINT\_HIGH](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7cad94f208bdf7029063172c88673d28b24) = kPINT\_PinIntEnableHighLevel

42};

43

44/\* Callback for NXP PINT interrupt \*/

[ 45](nxp__pint_8h.md#a5ceee20d9c423fe9f80e1d72540b4c73)typedef void (\*[nxp\_pint\_cb\_t](nxp__pint_8h.md#a5ceee20d9c423fe9f80e1d72540b4c73)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*user);

46

[ 54](nxp__pint_8h.md#ada0cadfd131f47f9c17033f3b9a31ebc)int [nxp\_pint\_pin\_enable](nxp__pint_8h.md#ada0cadfd131f47f9c17033f3b9a31ebc)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, enum [nxp\_pint\_trigger](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7c) trigger);

55

56

[ 62](nxp__pint_8h.md#a45daffb706e6e51fb805d1bfbd1c4144)void [nxp\_pint\_pin\_disable](nxp__pint_8h.md#a45daffb706e6e51fb805d1bfbd1c4144)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

63

[ 72](nxp__pint_8h.md#a086336be48bc780034f74dbd5aff0bd9)int [nxp\_pint\_pin\_set\_callback](nxp__pint_8h.md#a086336be48bc780034f74dbd5aff0bd9)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [nxp\_pint\_cb\_t](nxp__pint_8h.md#a5ceee20d9c423fe9f80e1d72540b4c73) cb, void \*data);

73

[ 79](nxp__pint_8h.md#ad7ec8dddcc5a404f38d8d5bb16775a9a)void [nxp\_pint\_pin\_unset\_callback](nxp__pint_8h.md#ad7ec8dddcc5a404f38d8d5bb16775a9a)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

80

81

82#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_NXP\_PINT\_H\_ \*/

[nxp\_pint\_pin\_set\_callback](nxp__pint_8h.md#a086336be48bc780034f74dbd5aff0bd9)

int nxp\_pint\_pin\_set\_callback(uint8\_t pin, nxp\_pint\_cb\_t cb, void \*data)

Install PINT callback.

[nxp\_pint\_pin\_disable](nxp__pint_8h.md#a45daffb706e6e51fb805d1bfbd1c4144)

void nxp\_pint\_pin\_disable(uint8\_t pin)

disable PINT interrupt source.

[nxp\_pint\_cb\_t](nxp__pint_8h.md#a5ceee20d9c423fe9f80e1d72540b4c73)

void(\* nxp\_pint\_cb\_t)(uint8\_t pin, void \*user)

**Definition** nxp\_pint.h:45

[nxp\_pint\_pin\_unset\_callback](nxp__pint_8h.md#ad7ec8dddcc5a404f38d8d5bb16775a9a)

void nxp\_pint\_pin\_unset\_callback(uint8\_t pin)

Remove PINT callback.

[nxp\_pint\_pin\_enable](nxp__pint_8h.md#ada0cadfd131f47f9c17033f3b9a31ebc)

int nxp\_pint\_pin\_enable(uint8\_t pin, enum nxp\_pint\_trigger trigger)

Enable PINT interrupt source.

[nxp\_pint\_trigger](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7c)

nxp\_pint\_trigger

Driver for Pin interrupt and pattern match engine in NXP MCUs.

**Definition** nxp\_pint.h:29

[NXP\_PINT\_LOW](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca115385d1645fa1901b7ffeab07ff6ce7)

@ NXP\_PINT\_LOW

**Definition** nxp\_pint.h:39

[NXP\_PINT\_RISING](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca20ed11aa9c65c91d30b169ae8a754d40)

@ NXP\_PINT\_RISING

**Definition** nxp\_pint.h:33

[NXP\_PINT\_NONE](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7ca8594c4bbe2858dd19a176d851a6175c5)

@ NXP\_PINT\_NONE

**Definition** nxp\_pint.h:31

[NXP\_PINT\_BOTH](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7caabce56e3c8a6ba8801b0700bfbf52ec2)

@ NXP\_PINT\_BOTH

**Definition** nxp\_pint.h:37

[NXP\_PINT\_HIGH](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7cad94f208bdf7029063172c88673d28b24)

@ NXP\_PINT\_HIGH

**Definition** nxp\_pint.h:41

[NXP\_PINT\_FALLING](nxp__pint_8h.md#aea62e6522d0de4c0ce63ae04b2d36f7caf77211604686c8e8f16616b25b9ada9e)

@ NXP\_PINT\_FALLING

**Definition** nxp\_pint.h:35

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [nxp\_pint.h](nxp__pint_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
