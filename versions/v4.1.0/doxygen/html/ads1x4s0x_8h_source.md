---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ads1x4s0x_8h_source.html
original_path: doxygen/html/ads1x4s0x_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ads1x4s0x.h

[Go to the documentation of this file.](ads1x4s0x_8h.md)

1/\*

2 \* Copyright (c) 2023 SILA Embedded Solutions GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADS1X4S0X\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADS1X4S0X\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12

[ 13](ads1x4s0x_8h.md#a703c9abdb26bef488c14c20825610a6d)int [ads1x4s0x\_gpio\_set\_output](ads1x4s0x_8h.md#a703c9abdb26bef488c14c20825610a6d)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, bool initial\_value);

14

[ 15](ads1x4s0x_8h.md#aeb9e6682f27b2c6d605cc64f92bd6b8c)int [ads1x4s0x\_gpio\_set\_input](ads1x4s0x_8h.md#aeb9e6682f27b2c6d605cc64f92bd6b8c)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

16

[ 17](ads1x4s0x_8h.md#a18a225e3609dbfee4a2c910fb8784ab8)int [ads1x4s0x\_gpio\_deconfigure](ads1x4s0x_8h.md#a18a225e3609dbfee4a2c910fb8784ab8)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

18

[ 19](ads1x4s0x_8h.md#ad303897d9eaffd6c0cc8e402cb8c45ad)int [ads1x4s0x\_gpio\_set\_pin\_value](ads1x4s0x_8h.md#ad303897d9eaffd6c0cc8e402cb8c45ad)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin,

20 bool value);

21

[ 22](ads1x4s0x_8h.md#af93b1e5324774fea17271c3e54a190e0)int [ads1x4s0x\_gpio\_get\_pin\_value](ads1x4s0x_8h.md#af93b1e5324774fea17271c3e54a190e0)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin,

23 bool \*value);

24

[ 25](ads1x4s0x_8h.md#aae6dca79ac3425a471962cc6f736eeed)int [ads1x4s0x\_gpio\_port\_get\_raw](ads1x4s0x_8h.md#aae6dca79ac3425a471962cc6f736eeed)(const struct [device](structdevice.md) \*dev,

26 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

27

[ 28](ads1x4s0x_8h.md#aa5f025a7f772c0787f22ced0ed761e0e)int [ads1x4s0x\_gpio\_port\_set\_masked\_raw](ads1x4s0x_8h.md#aa5f025a7f772c0787f22ced0ed761e0e)(const struct [device](structdevice.md) \*dev,

29 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

30 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

31

[ 32](ads1x4s0x_8h.md#a60438c9501fcece5548a1195fa3f77a0)int [ads1x4s0x\_gpio\_port\_toggle\_bits](ads1x4s0x_8h.md#a60438c9501fcece5548a1195fa3f77a0)(const struct [device](structdevice.md) \*dev,

33 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

34

35#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADS1X4S0X\_H\_ \*/

[ads1x4s0x\_gpio\_deconfigure](ads1x4s0x_8h.md#a18a225e3609dbfee4a2c910fb8784ab8)

int ads1x4s0x\_gpio\_deconfigure(const struct device \*dev, uint8\_t pin)

[ads1x4s0x\_gpio\_port\_toggle\_bits](ads1x4s0x_8h.md#a60438c9501fcece5548a1195fa3f77a0)

int ads1x4s0x\_gpio\_port\_toggle\_bits(const struct device \*dev, gpio\_port\_pins\_t pins)

[ads1x4s0x\_gpio\_set\_output](ads1x4s0x_8h.md#a703c9abdb26bef488c14c20825610a6d)

int ads1x4s0x\_gpio\_set\_output(const struct device \*dev, uint8\_t pin, bool initial\_value)

[ads1x4s0x\_gpio\_port\_set\_masked\_raw](ads1x4s0x_8h.md#aa5f025a7f772c0787f22ced0ed761e0e)

int ads1x4s0x\_gpio\_port\_set\_masked\_raw(const struct device \*dev, gpio\_port\_pins\_t mask, gpio\_port\_value\_t value)

[ads1x4s0x\_gpio\_port\_get\_raw](ads1x4s0x_8h.md#aae6dca79ac3425a471962cc6f736eeed)

int ads1x4s0x\_gpio\_port\_get\_raw(const struct device \*dev, gpio\_port\_value\_t \*value)

[ads1x4s0x\_gpio\_set\_pin\_value](ads1x4s0x_8h.md#ad303897d9eaffd6c0cc8e402cb8c45ad)

int ads1x4s0x\_gpio\_set\_pin\_value(const struct device \*dev, uint8\_t pin, bool value)

[ads1x4s0x\_gpio\_set\_input](ads1x4s0x_8h.md#aeb9e6682f27b2c6d605cc64f92bd6b8c)

int ads1x4s0x\_gpio\_set\_input(const struct device \*dev, uint8\_t pin)

[ads1x4s0x\_gpio\_get\_pin\_value](ads1x4s0x_8h.md#af93b1e5324774fea17271c3e54a190e0)

int ads1x4s0x\_gpio\_get\_pin\_value(const struct device \*dev, uint8\_t pin, bool \*value)

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:234

[gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)

uint32\_t gpio\_port\_value\_t

Provides values for a set of pins associated with a port.

**Definition** gpio.h:247

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [ads1x4s0x.h](ads1x4s0x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
