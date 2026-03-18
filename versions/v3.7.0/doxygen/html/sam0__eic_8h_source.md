---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sam0__eic_8h_source.html
original_path: doxygen/html/sam0__eic_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sam0\_eic.h

[Go to the documentation of this file.](sam0__eic_8h.md)

1/\*

2 \* Copyright (c) 2019 Derek Hageman <hageman@inthat.cloud>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_SAM0\_EIC\_H\_

9#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_SAM0\_EIC\_H\_

10

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12

13/\* callback for EIC interrupt \*/

[ 14](sam0__eic_8h.md#a689981657e7012bca040dac40c5bf28f)typedef void (\*[sam0\_eic\_callback\_t](sam0__eic_8h.md#a689981657e7012bca040dac40c5bf28f))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pins, void \*data);

15

[ 19](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34)enum [sam0\_eic\_trigger](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34) {

20 /\* Rising edge \*/

[ 21](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a1c8d428daca3fb7b76bae9ecb5427511) [SAM0\_EIC\_RISING](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a1c8d428daca3fb7b76bae9ecb5427511),

22 /\* Falling edge \*/

[ 23](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a7fb8fbeb7d3300080b1e54d656b990bc) [SAM0\_EIC\_FALLING](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a7fb8fbeb7d3300080b1e54d656b990bc),

24 /\* Both edges \*/

[ 25](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34ad5a9871d1afcbd200a0b3e2e2b7e9871) [SAM0\_EIC\_BOTH](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34ad5a9871d1afcbd200a0b3e2e2b7e9871),

26 /\* High level detection \*/

[ 27](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a61aac8fcb51758fd69b77c3b938d6486) [SAM0\_EIC\_HIGH](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a61aac8fcb51758fd69b77c3b938d6486),

28 /\* Low level detection \*/

[ 29](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a207804f632e291be19b237dde2fd15a9) [SAM0\_EIC\_LOW](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a207804f632e291be19b237dde2fd15a9),

30};

31

[ 47](sam0__eic_8h.md#a6b6009bc8a688ac395ec579d52c25359)int [sam0\_eic\_acquire](sam0__eic_8h.md#a6b6009bc8a688ac395ec579d52c25359)(int port, int pin, enum [sam0\_eic\_trigger](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34) trigger,

48 bool filter, [sam0\_eic\_callback\_t](sam0__eic_8h.md#a689981657e7012bca040dac40c5bf28f) cb, void \*data);

49

[ 60](sam0__eic_8h.md#aa6e652726d154e5cda1108aa31d60f26)int [sam0\_eic\_release](sam0__eic_8h.md#aa6e652726d154e5cda1108aa31d60f26)(int port, int pin);

61

[ 68](sam0__eic_8h.md#a7a65e580827b8e0d3f788cc1aaba7ea7)int [sam0\_eic\_enable\_interrupt](sam0__eic_8h.md#a7a65e580827b8e0d3f788cc1aaba7ea7)(int port, int pin);

69

[ 76](sam0__eic_8h.md#a5019df444a31531292fbf2fe5af160ef)int [sam0\_eic\_disable\_interrupt](sam0__eic_8h.md#a5019df444a31531292fbf2fe5af160ef)(int port, int pin);

77

[ 83](sam0__eic_8h.md#a7dd3052cd7fb8074ad0b1233ecaa5708)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sam0\_eic\_interrupt\_pending](sam0__eic_8h.md#a7dd3052cd7fb8074ad0b1233ecaa5708)(int port);

84

85#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_SAM0\_EIC\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[sam0\_eic\_disable\_interrupt](sam0__eic_8h.md#a5019df444a31531292fbf2fe5af160ef)

int sam0\_eic\_disable\_interrupt(int port, int pin)

Disable the EIC interrupt for a specific port and pin combination.

[sam0\_eic\_trigger](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34)

sam0\_eic\_trigger

EIC trigger condition.

**Definition** sam0\_eic.h:19

[SAM0\_EIC\_RISING](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a1c8d428daca3fb7b76bae9ecb5427511)

@ SAM0\_EIC\_RISING

**Definition** sam0\_eic.h:21

[SAM0\_EIC\_LOW](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a207804f632e291be19b237dde2fd15a9)

@ SAM0\_EIC\_LOW

**Definition** sam0\_eic.h:29

[SAM0\_EIC\_HIGH](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a61aac8fcb51758fd69b77c3b938d6486)

@ SAM0\_EIC\_HIGH

**Definition** sam0\_eic.h:27

[SAM0\_EIC\_FALLING](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34a7fb8fbeb7d3300080b1e54d656b990bc)

@ SAM0\_EIC\_FALLING

**Definition** sam0\_eic.h:23

[SAM0\_EIC\_BOTH](sam0__eic_8h.md#a679adca86ca5da9a49b88bd3110f2f34ad5a9871d1afcbd200a0b3e2e2b7e9871)

@ SAM0\_EIC\_BOTH

**Definition** sam0\_eic.h:25

[sam0\_eic\_callback\_t](sam0__eic_8h.md#a689981657e7012bca040dac40c5bf28f)

void(\* sam0\_eic\_callback\_t)(uint32\_t pins, void \*data)

**Definition** sam0\_eic.h:14

[sam0\_eic\_acquire](sam0__eic_8h.md#a6b6009bc8a688ac395ec579d52c25359)

int sam0\_eic\_acquire(int port, int pin, enum sam0\_eic\_trigger trigger, bool filter, sam0\_eic\_callback\_t cb, void \*data)

Acquire an EIC interrupt for specific port and pin combination.

[sam0\_eic\_enable\_interrupt](sam0__eic_8h.md#a7a65e580827b8e0d3f788cc1aaba7ea7)

int sam0\_eic\_enable\_interrupt(int port, int pin)

Enable the EIC interrupt for a specific port and pin combination.

[sam0\_eic\_interrupt\_pending](sam0__eic_8h.md#a7dd3052cd7fb8074ad0b1233ecaa5708)

uint32\_t sam0\_eic\_interrupt\_pending(int port)

Test if there is an EIC interrupt pending for a port.

[sam0\_eic\_release](sam0__eic_8h.md#aa6e652726d154e5cda1108aa31d60f26)

int sam0\_eic\_release(int port, int pin)

Release the EIC interrupt for a specific port and pin combination.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [sam0\_eic.h](sam0__eic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
