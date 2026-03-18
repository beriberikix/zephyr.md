---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32__wkup__pins_8h_source.html
original_path: doxygen/html/stm32__wkup__pins_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_wkup\_pins.h

[Go to the documentation of this file.](stm32__wkup__pins_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_MISC\_STM32\_WKUP\_PINS\_H\_

13#define ZEPHYR\_DRIVERS\_MISC\_STM32\_WKUP\_PINS\_H\_

14

15#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 28](stm32__wkup__pins_8h.md#aecb5d4773c1c9409ecbb2c2d67fd60c2)int [stm32\_pwr\_wkup\_pin\_cfg\_gpio](stm32__wkup__pins_8h.md#aecb5d4773c1c9409ecbb2c2d67fd60c2)(const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*gpio);

29

[ 34](stm32__wkup__pins_8h.md#ad666ce6394d022f2270c263d52c707f8)void [stm32\_pwr\_wkup\_pin\_cfg\_pupd](stm32__wkup__pins_8h.md#ad666ce6394d022f2270c263d52c707f8)(void);

35

36#ifdef \_\_cplusplus

37}

38#endif

39

40#endif /\* ZEPHYR\_DRIVERS\_MISC\_STM32\_WKUP\_PINS\_H\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[stm32\_pwr\_wkup\_pin\_cfg\_pupd](stm32__wkup__pins_8h.md#ad666ce6394d022f2270c263d52c707f8)

void stm32\_pwr\_wkup\_pin\_cfg\_pupd(void)

Enable or Disable pull-up and pull-down configuration for GPIO Ports that are associated with STM32 P...

[stm32\_pwr\_wkup\_pin\_cfg\_gpio](stm32__wkup__pins_8h.md#aecb5d4773c1c9409ecbb2c2d67fd60c2)

int stm32\_pwr\_wkup\_pin\_cfg\_gpio(const struct gpio\_dt\_spec \*gpio)

Configure a GPIO pin as a source for STM32 PWR wake-up pins.

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:288

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [stm32\_wkup\_pins](dir_6b6ef3fbec1eba38a97eeee785d34dc8.md)
- [stm32\_wkup\_pins.h](stm32__wkup__pins_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
