---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/gpio__ambiq_8h_source.html
original_path: doxygen/html/gpio__ambiq_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_ambiq.h

[Go to the documentation of this file.](gpio__ambiq_8h.md)

1/\*

2 \* Copyright (c) 2025 Ambiq Micro Inc. <www.ambiq.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_GPIO\_GPIO\_AMBIQ\_H\_

8#define ZEPHYR\_DRIVERS\_GPIO\_GPIO\_AMBIQ\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 25](gpio__ambiq_8h.md#aaaf57fd1692176a44714852f7593913d)[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [ambiq\_gpio\_get\_pinnum](gpio__ambiq_8h.md#aaaf57fd1692176a44714852f7593913d)(const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin);

26

27#ifdef \_\_cplusplus

28}

29#endif

30

31#endif /\* ZEPHYR\_DRIVERS\_GPIO\_GPIO\_AMBIQ\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[ambiq\_gpio\_get\_pinnum](gpio__ambiq_8h.md#aaaf57fd1692176a44714852f7593913d)

gpio\_pin\_t ambiq\_gpio\_get\_pinnum(const struct device \*dev, gpio\_pin\_t pin)

Get the actual gpio pin number.

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:255

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_ambiq.h](gpio__ambiq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
