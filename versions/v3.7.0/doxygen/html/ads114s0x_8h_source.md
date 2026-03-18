---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ads114s0x_8h_source.html
original_path: doxygen/html/ads114s0x_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ads114s0x.h

[Go to the documentation of this file.](ads114s0x_8h.md)

1/\*

2 \* Copyright (c) 2023 SILA Embedded Solutions GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADS114S0X\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADS114S0X\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12

[ 13](ads114s0x_8h.md#aae01af45d1f620e1fba7f352732cbdfe)int [ads114s0x\_gpio\_set\_output](ads114s0x_8h.md#aae01af45d1f620e1fba7f352732cbdfe)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, bool initial\_value);

14

[ 15](ads114s0x_8h.md#a772a6f07c12f310c1648351b38062dfa)int [ads114s0x\_gpio\_set\_input](ads114s0x_8h.md#a772a6f07c12f310c1648351b38062dfa)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

16

[ 17](ads114s0x_8h.md#ab8dc4eec4cad38cc25aeadef3c810b0b)int [ads114s0x\_gpio\_deconfigure](ads114s0x_8h.md#ab8dc4eec4cad38cc25aeadef3c810b0b)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

18

[ 19](ads114s0x_8h.md#a92d0aa7dbfba1f6337ba1f871a328c4d)int [ads114s0x\_gpio\_set\_pin\_value](ads114s0x_8h.md#a92d0aa7dbfba1f6337ba1f871a328c4d)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin,

20 bool value);

21

[ 22](ads114s0x_8h.md#acfdec18269fb677f17ecde631e2e0eb1)int [ads114s0x\_gpio\_get\_pin\_value](ads114s0x_8h.md#acfdec18269fb677f17ecde631e2e0eb1)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin,

23 bool \*value);

24

[ 25](ads114s0x_8h.md#aea152628b28b208d251c7286e7ea72b9)int [ads114s0x\_gpio\_port\_get\_raw](ads114s0x_8h.md#aea152628b28b208d251c7286e7ea72b9)(const struct [device](structdevice.md) \*dev,

26 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

27

[ 28](ads114s0x_8h.md#a9e285db925feafd10038c893e6544a7f)int [ads114s0x\_gpio\_port\_set\_masked\_raw](ads114s0x_8h.md#a9e285db925feafd10038c893e6544a7f)(const struct [device](structdevice.md) \*dev,

29 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

30 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

31

[ 32](ads114s0x_8h.md#ac59eee61e1b0dd988343461884436140)int [ads114s0x\_gpio\_port\_toggle\_bits](ads114s0x_8h.md#ac59eee61e1b0dd988343461884436140)(const struct [device](structdevice.md) \*dev,

33 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

34

35#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_ADS114S0X\_H\_ \*/

[ads114s0x\_gpio\_set\_input](ads114s0x_8h.md#a772a6f07c12f310c1648351b38062dfa)

int ads114s0x\_gpio\_set\_input(const struct device \*dev, uint8\_t pin)

[ads114s0x\_gpio\_set\_pin\_value](ads114s0x_8h.md#a92d0aa7dbfba1f6337ba1f871a328c4d)

int ads114s0x\_gpio\_set\_pin\_value(const struct device \*dev, uint8\_t pin, bool value)

[ads114s0x\_gpio\_port\_set\_masked\_raw](ads114s0x_8h.md#a9e285db925feafd10038c893e6544a7f)

int ads114s0x\_gpio\_port\_set\_masked\_raw(const struct device \*dev, gpio\_port\_pins\_t mask, gpio\_port\_value\_t value)

[ads114s0x\_gpio\_set\_output](ads114s0x_8h.md#aae01af45d1f620e1fba7f352732cbdfe)

int ads114s0x\_gpio\_set\_output(const struct device \*dev, uint8\_t pin, bool initial\_value)

[ads114s0x\_gpio\_deconfigure](ads114s0x_8h.md#ab8dc4eec4cad38cc25aeadef3c810b0b)

int ads114s0x\_gpio\_deconfigure(const struct device \*dev, uint8\_t pin)

[ads114s0x\_gpio\_port\_toggle\_bits](ads114s0x_8h.md#ac59eee61e1b0dd988343461884436140)

int ads114s0x\_gpio\_port\_toggle\_bits(const struct device \*dev, gpio\_port\_pins\_t pins)

[ads114s0x\_gpio\_get\_pin\_value](ads114s0x_8h.md#acfdec18269fb677f17ecde631e2e0eb1)

int ads114s0x\_gpio\_get\_pin\_value(const struct device \*dev, uint8\_t pin, bool \*value)

[ads114s0x\_gpio\_port\_get\_raw](ads114s0x_8h.md#aea152628b28b208d251c7286e7ea72b9)

int ads114s0x\_gpio\_port\_get\_raw(const struct device \*dev, gpio\_port\_value\_t \*value)

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:233

[gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)

uint32\_t gpio\_port\_value\_t

Provides values for a set of pins associated with a port.

**Definition** gpio.h:246

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [ads114s0x.h](ads114s0x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
