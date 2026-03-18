---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gd32__exti_8h_source.html
original_path: doxygen/html/gd32__exti_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32\_exti.h

[Go to the documentation of this file.](gd32__exti_8h.md)

1/\*

2 \* Copyright (c) 2021 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_GD32\_EXTI\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_GD32\_EXTI\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

13

19

[ 21](gd32__exti_8h.md#aa2b7ef2f0b43317c7c58fe4d53e07a19)#define GD32\_EXTI\_TRIG\_NONE 0U

[ 23](gd32__exti_8h.md#a8d9e9cd3451d66f8d6df889ea8d50a3c)#define GD32\_EXTI\_TRIG\_RISING BIT(0)

[ 25](gd32__exti_8h.md#aab892d582f9f266f7d942d238786e306)#define GD32\_EXTI\_TRIG\_FALLING BIT(1)

[ 27](gd32__exti_8h.md#a6e09a28174e0c4b9ec7a79e89199f7e4)#define GD32\_EXTI\_TRIG\_BOTH (GD32\_EXTI\_TRIG\_RISING | GD32\_EXTI\_TRIG\_FALLING)

28

30

[ 32](gd32__exti_8h.md#aac1a418b49c19fcf6e0dff2c0a3b7f75)typedef void (\*[gd32\_exti\_cb\_t](gd32__exti_8h.md#aac1a418b49c19fcf6e0dff2c0a3b7f75))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, void \*user);

33

[ 39](gd32__exti_8h.md#ad63c2b15a0f2e0f703255b00b9368232)void [gd32\_exti\_enable](gd32__exti_8h.md#ad63c2b15a0f2e0f703255b00b9368232)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line);

40

[ 46](gd32__exti_8h.md#a3f0333dce2621c7fed721e37a2413d80)void [gd32\_exti\_disable](gd32__exti_8h.md#a3f0333dce2621c7fed721e37a2413d80)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line);

47

[ 54](gd32__exti_8h.md#ac543badc8874861f866b3bf3eba37e9a)void [gd32\_exti\_trigger](gd32__exti_8h.md#ac543badc8874861f866b3bf3eba37e9a)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) trigger);

55

[ 66](gd32__exti_8h.md#a014fba07d150faa8270493bb8257b31b)int [gd32\_exti\_configure](gd32__exti_8h.md#a014fba07d150faa8270493bb8257b31b)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, [gd32\_exti\_cb\_t](gd32__exti_8h.md#aac1a418b49c19fcf6e0dff2c0a3b7f75) cb, void \*user);

67

68#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_INTERRUPT\_CONTROLLER\_GD32\_EXTI\_H\_ \*/

[gd32\_exti\_configure](gd32__exti_8h.md#a014fba07d150faa8270493bb8257b31b)

int gd32\_exti\_configure(uint8\_t line, gd32\_exti\_cb\_t cb, void \*user)

Configure EXTI interrupt callback.

[gd32\_exti\_disable](gd32__exti_8h.md#a3f0333dce2621c7fed721e37a2413d80)

void gd32\_exti\_disable(uint8\_t line)

Disable EXTI interrupt for the given line.

[gd32\_exti\_cb\_t](gd32__exti_8h.md#aac1a418b49c19fcf6e0dff2c0a3b7f75)

void(\* gd32\_exti\_cb\_t)(uint8\_t line, void \*user)

Callback for EXTI interrupt.

**Definition** gd32\_exti.h:32

[gd32\_exti\_trigger](gd32__exti_8h.md#ac543badc8874861f866b3bf3eba37e9a)

void gd32\_exti\_trigger(uint8\_t line, uint8\_t trigger)

Configure EXTI interrupt trigger mode for the given line.

[gd32\_exti\_enable](gd32__exti_8h.md#ad63c2b15a0f2e0f703255b00b9368232)

void gd32\_exti\_enable(uint8\_t line)

Enable EXTI interrupt for the given line.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [gd32\_exti.h](gd32__exti_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
