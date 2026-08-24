---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/wch__exti_8h_source.html
original_path: doxygen/html/wch__exti_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wch\_exti.h

[Go to the documentation of this file.](wch__exti_8h.md)

1/\*

2 \* Copyright (c) 2025 Michael Hope <michaelh@juju.nz>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_WCH\_EXTI\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_WCH\_EXTI\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

13

14/\* Callback for EXTI interrupt. \*/

[ 15](wch__exti_8h.md#aa1c9d73d6337b6fd8dc95187f739b768)typedef void (\*[wch\_exti\_callback\_handler\_t](wch__exti_8h.md#aa1c9d73d6337b6fd8dc95187f739b768))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, void \*user);

16

[ 17](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1)enum [wch\_exti\_trigger](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1) {

18 /\*

19 \* Note that this is a flag set and these values can be ORed to trigger on

20 \* both edges.

21 \*/

22

23 /\* Trigger on rising edge \*/

[ 24](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1ac64106e333e2172f25bcbf5c201acb28) [WCH\_EXTI\_TRIGGER\_RISING\_EDGE](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1ac64106e333e2172f25bcbf5c201acb28) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

25 /\* Trigger on falling edge \*/

[ 26](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1a3b2c0bd85bbfed5d0bed4d495534e518) [WCH\_EXTI\_TRIGGER\_FALLING\_EDGE](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1a3b2c0bd85bbfed5d0bed4d495534e518) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

27};

28

29/\* Enable the EXTI interrupt for `line` \*/

[ 30](wch__exti_8h.md#a36723b918e6ddb225e05c041a6127369)void [wch\_exti\_enable](wch__exti_8h.md#a36723b918e6ddb225e05c041a6127369)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line);

31

32/\* Disable the EXTI interrupt for `line` \*/

[ 33](wch__exti_8h.md#a2b90b358d0ee8445e1257c636cfbd931)void [wch\_exti\_disable](wch__exti_8h.md#a2b90b358d0ee8445e1257c636cfbd931)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line);

34

35/\* Set the trigger mode for `line` \*/

[ 36](wch__exti_8h.md#aa7c5d9dff440158faad0c33da28f8777)void [wch\_exti\_set\_trigger](wch__exti_8h.md#aa7c5d9dff440158faad0c33da28f8777)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, enum [wch\_exti\_trigger](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1) trigger);

37

38/\* Register a callback for `line` \*/

[ 39](wch__exti_8h.md#a7ff8c5c40b36a6974c535e54fbff311f)int [wch\_exti\_configure](wch__exti_8h.md#a7ff8c5c40b36a6974c535e54fbff311f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, [wch\_exti\_callback\_handler\_t](wch__exti_8h.md#aa1c9d73d6337b6fd8dc95187f739b768) callback, void \*user);

40

41#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_WCH\_EXTI\_H\_ \*/

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[util\_macro.h](util__macro_8h.md)

Macro utilities.

[wch\_exti\_disable](wch__exti_8h.md#a2b90b358d0ee8445e1257c636cfbd931)

void wch\_exti\_disable(uint8\_t line)

[wch\_exti\_enable](wch__exti_8h.md#a36723b918e6ddb225e05c041a6127369)

void wch\_exti\_enable(uint8\_t line)

[wch\_exti\_configure](wch__exti_8h.md#a7ff8c5c40b36a6974c535e54fbff311f)

int wch\_exti\_configure(uint8\_t line, wch\_exti\_callback\_handler\_t callback, void \*user)

[wch\_exti\_callback\_handler\_t](wch__exti_8h.md#aa1c9d73d6337b6fd8dc95187f739b768)

void(\* wch\_exti\_callback\_handler\_t)(uint8\_t line, void \*user)

**Definition** wch\_exti.h:15

[wch\_exti\_set\_trigger](wch__exti_8h.md#aa7c5d9dff440158faad0c33da28f8777)

void wch\_exti\_set\_trigger(uint8\_t line, enum wch\_exti\_trigger trigger)

[wch\_exti\_trigger](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1)

wch\_exti\_trigger

**Definition** wch\_exti.h:17

[WCH\_EXTI\_TRIGGER\_FALLING\_EDGE](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1a3b2c0bd85bbfed5d0bed4d495534e518)

@ WCH\_EXTI\_TRIGGER\_FALLING\_EDGE

**Definition** wch\_exti.h:26

[WCH\_EXTI\_TRIGGER\_RISING\_EDGE](wch__exti_8h.md#ab41aa3ea720735eb77fc4aaa59659db1ac64106e333e2172f25bcbf5c201acb28)

@ WCH\_EXTI\_TRIGGER\_RISING\_EDGE

**Definition** wch\_exti.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [wch\_exti.h](wch__exti_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
