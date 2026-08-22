---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/i2c__nrfx__twim_8h_source.html
original_path: doxygen/html/i2c__nrfx__twim_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_nrfx\_twim.h

[Go to the documentation of this file.](i2c__nrfx__twim_8h.md)

1/\*

2 \* Copyright (c) 2025 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_NRFX\_TWIM\_H

8#define ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_NRFX\_TWIM\_H

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

12

[ 24](i2c__nrfx__twim_8h.md#a465c42f64eb7d2dd4c5e173f9ae11745)int [i2c\_nrfx\_twim\_exclusive\_access\_acquire](i2c__nrfx__twim_8h.md#a465c42f64eb7d2dd4c5e173f9ae11745)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

25

[ 32](i2c__nrfx__twim_8h.md#a924fddc00479f92f98b05a91d08fa7da)void [i2c\_nrfx\_twim\_exclusive\_access\_release](i2c__nrfx__twim_8h.md#a924fddc00479f92f98b05a91d08fa7da)(const struct [device](structdevice.md) \*dev);

33

34#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_NRFX\_TWIM\_H \*/

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[i2c\_nrfx\_twim\_exclusive\_access\_acquire](i2c__nrfx__twim_8h.md#a465c42f64eb7d2dd4c5e173f9ae11745)

int i2c\_nrfx\_twim\_exclusive\_access\_acquire(const struct device \*dev, k\_timeout\_t timeout)

Acquires exclusive access to the i2c bus controller.

[i2c\_nrfx\_twim\_exclusive\_access\_release](i2c__nrfx__twim_8h.md#a924fddc00479f92f98b05a91d08fa7da)

void i2c\_nrfx\_twim\_exclusive\_access\_release(const struct device \*dev)

Releases exclusive access to the i2c bus controller.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c](dir_d0e9f61c1b95aed307ec1c726ffb3f96.md)
- [i2c\_nrfx\_twim.h](i2c__nrfx__twim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
