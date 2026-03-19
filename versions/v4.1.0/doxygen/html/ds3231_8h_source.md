---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ds3231_8h_source.html
original_path: doxygen/html/ds3231_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ds3231.h

[Go to the documentation of this file.](ds3231_8h.md)

1/\*

2 \* Copyright (c) 2024 Gergo Vari <work@gergovari.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_DS3231\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_DS3231\_H\_

9

10#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

11

[ 23](ds3231_8h.md#aa7f2419f0d2555e24cd94ed8c7b67ccf)int [mfd\_ds3231\_i2c\_get\_registers](ds3231_8h.md#aa7f2419f0d2555e24cd94ed8c7b67ccf)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

24 const size\_t buf\_size);

25

[ 36](ds3231_8h.md#a478705fd7794fa3002ac36fb2fcef17e)int [mfd\_ds3231\_i2c\_set\_registers](ds3231_8h.md#a478705fd7794fa3002ac36fb2fcef17e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_reg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

37 const size\_t buf\_size);

38

39#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_DS3231\_H\_ \*/

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[mfd\_ds3231\_i2c\_set\_registers](ds3231_8h.md#a478705fd7794fa3002ac36fb2fcef17e)

int mfd\_ds3231\_i2c\_set\_registers(const struct device \*dev, uint8\_t start\_reg, const uint8\_t \*buf, const size\_t buf\_size)

Set a register on an I2C device at the given register address.

[mfd\_ds3231\_i2c\_get\_registers](ds3231_8h.md#aa7f2419f0d2555e24cd94ed8c7b67ccf)

int mfd\_ds3231\_i2c\_get\_registers(const struct device \*dev, uint8\_t start\_reg, uint8\_t \*buf, const size\_t buf\_size)

Get specified number of registers from an I2C device starting at the given register address.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [ds3231.h](ds3231_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
