---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32__wkup__pins_8h.html
original_path: doxygen/html/stm32__wkup__pins_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_wkup\_pins.h File Reference

Public APIs for STM32 PWR wake-up pins configuration.
[More...](#details)

`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](stm32__wkup__pins_8h_source.md)

| Functions | |
| --- | --- |
| int | [stm32\_pwr\_wkup\_pin\_cfg\_gpio](#aecb5d4773c1c9409ecbb2c2d67fd60c2) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*gpio) |
|  | Configure a GPIO pin as a source for STM32 PWR wake-up pins. |
| void | [stm32\_pwr\_wkup\_pin\_cfg\_pupd](#ad666ce6394d022f2270c263d52c707f8) (void) |
|  | Enable or Disable pull-up and pull-down configuration for GPIO Ports that are associated with STM32 PWR wake-up pins. |

## Detailed Description

Public APIs for STM32 PWR wake-up pins configuration.

## Function Documentation

## [◆ ](#aecb5d4773c1c9409ecbb2c2d67fd60c2)stm32\_pwr\_wkup\_pin\_cfg\_gpio()

| int stm32\_pwr\_wkup\_pin\_cfg\_gpio | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *gpio* | ) |  |
| --- | --- | --- | --- | --- | --- |

Configure a GPIO pin as a source for STM32 PWR wake-up pins.

Parameters
:   | gpio | Container for GPIO pin information specified in devicetree |
    | --- | --- |

Returns
:   0 on success, -EINVAL on invalid values

## [◆ ](#ad666ce6394d022f2270c263d52c707f8)stm32\_pwr\_wkup\_pin\_cfg\_pupd()

| void stm32\_pwr\_wkup\_pin\_cfg\_pupd | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable or Disable pull-up and pull-down configuration for GPIO Ports that are associated with STM32 PWR wake-up pins.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [stm32\_wkup\_pins](dir_6b6ef3fbec1eba38a97eeee785d34dc8.md)
- [stm32\_wkup\_pins.h](stm32__wkup__pins_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
