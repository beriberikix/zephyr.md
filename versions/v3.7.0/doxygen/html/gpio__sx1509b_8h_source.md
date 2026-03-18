---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gpio__sx1509b_8h_source.html
original_path: doxygen/html/gpio__sx1509b_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_sx1509b.h

[Go to the documentation of this file.](gpio__sx1509b_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_SX1509B\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_SX1509B\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12

[ 29](gpio__sx1509b_8h.md#ac2ed2f915a7e507e49abc82b6f4f09d5)int [sx1509b\_led\_intensity\_pin\_configure](gpio__sx1509b_8h.md#ac2ed2f915a7e507e49abc82b6f4f09d5)(const struct [device](structdevice.md) \*dev,

30 [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin);

31

[ 42](gpio__sx1509b_8h.md#a5fe77cf7261b831b4cb010c48da982bf)int [sx1509b\_led\_intensity\_pin\_set](gpio__sx1509b_8h.md#a5fe77cf7261b831b4cb010c48da982bf)(const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

43 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) intensity\_val);

44

45#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_SX1509B\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[sx1509b\_led\_intensity\_pin\_set](gpio__sx1509b_8h.md#a5fe77cf7261b831b4cb010c48da982bf)

int sx1509b\_led\_intensity\_pin\_set(const struct device \*dev, gpio\_pin\_t pin, uint8\_t intensity\_val)

Set LED intensity of selected pin.

[sx1509b\_led\_intensity\_pin\_configure](gpio__sx1509b_8h.md#ac2ed2f915a7e507e49abc82b6f4f09d5)

int sx1509b\_led\_intensity\_pin\_configure(const struct device \*dev, gpio\_pin\_t pin)

Configure a pin for LED intensity.

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:254

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_sx1509b.h](gpio__sx1509b_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
