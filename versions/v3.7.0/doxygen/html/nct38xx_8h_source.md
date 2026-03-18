---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nct38xx_8h_source.html
original_path: doxygen/html/nct38xx_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nct38xx.h

[Go to the documentation of this file.](nct38xx_8h.md)

1/\*

2 \* Copyright (c) 2023 Google, LLC

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NCT38XX\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NCT38XX\_H\_

8

9#include <[zephyr/device.h](device_8h.md)>

10#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 25](nct38xx_8h.md#a14924372c0c4ffb5cb5d7f69cf22df7d)struct k\_sem \*[mfd\_nct38xx\_get\_lock\_reference](nct38xx_8h.md#a14924372c0c4ffb5cb5d7f69cf22df7d)(const struct [device](structdevice.md) \*dev);

26

[ 34](nct38xx_8h.md#af32ad6d2c437c5a1ebb4abe660903bde)const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*[mfd\_nct38xx\_get\_i2c\_dt\_spec](nct38xx_8h.md#af32ad6d2c437c5a1ebb4abe660903bde)(const struct [device](structdevice.md) \*dev);

35

36#ifdef \_\_cplusplus

37}

38#endif

39

40#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NCT38XX\_H\_ \*/

[device.h](device_8h.md)

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mfd\_nct38xx\_get\_lock\_reference](nct38xx_8h.md#a14924372c0c4ffb5cb5d7f69cf22df7d)

struct k\_sem \* mfd\_nct38xx\_get\_lock\_reference(const struct device \*dev)

Get the semaphore reference for a NCT38xx instance.

[mfd\_nct38xx\_get\_i2c\_dt\_spec](nct38xx_8h.md#af32ad6d2c437c5a1ebb4abe660903bde)

const struct i2c\_dt\_spec \* mfd\_nct38xx\_get\_i2c\_dt\_spec(const struct device \*dev)

Get the I2C DT spec reference for a NCT38xx instance.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[i2c\_dt\_spec](structi2c__dt__spec.md)

Complete I2C DT information.

**Definition** i2c.h:77

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [nct38xx.h](nct38xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
