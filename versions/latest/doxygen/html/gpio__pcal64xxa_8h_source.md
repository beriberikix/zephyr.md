---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gpio__pcal64xxa_8h_source.html
original_path: doxygen/html/gpio__pcal64xxa_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_pcal64xxa.h

[Go to the documentation of this file.](gpio__pcal64xxa_8h.md)

1/\*

2 \* Copyright (c) 2024 SILA Embedded Solutions GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_PCAL64XXA\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_PCAL64XXA\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 27](gpio__pcal64xxa_8h.md#a43c22f38602347e2e95f63fd9b31dc96)int [pcal64xxa\_reset](gpio__pcal64xxa_8h.md#a43c22f38602347e2e95f63fd9b31dc96)(const struct [device](structdevice.md) \*dev);

28

29#ifdef \_\_cplusplus

30}

31#endif

32

33#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_PCAL64XXA\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[pcal64xxa\_reset](gpio__pcal64xxa_8h.md#a43c22f38602347e2e95f63fd9b31dc96)

int pcal64xxa\_reset(const struct device \*dev)

Manually reset a PCAL64XXA.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_pcal64xxa.h](gpio__pcal64xxa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
