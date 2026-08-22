---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/gpio__mcux__lpc_8h_source.html
original_path: doxygen/html/gpio__mcux__lpc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_mcux\_lpc.h

[Go to the documentation of this file.](gpio__mcux__lpc_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_MCUX\_LPC\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_MCUX\_LPC\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12

[ 22](gpio__mcux__lpc_8h.md#a6ce1efd70bb2996ac993f2a322d74ac3)void [gpio\_mcux\_lpc\_trigger\_cb](gpio__mcux__lpc_8h.md#a6ce1efd70bb2996ac993f2a322d74ac3)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pins);

23

24#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_MCUX\_LPC\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[gpio\_mcux\_lpc\_trigger\_cb](gpio__mcux__lpc_8h.md#a6ce1efd70bb2996ac993f2a322d74ac3)

void gpio\_mcux\_lpc\_trigger\_cb(const struct device \*dev, uint32\_t pins)

Trigger a callback for a given pin.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_mcux\_lpc.h](gpio__mcux__lpc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
