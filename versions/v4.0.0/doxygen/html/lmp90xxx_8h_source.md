---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lmp90xxx_8h_source.html
original_path: doxygen/html/lmp90xxx_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lmp90xxx.h

[Go to the documentation of this file.](lmp90xxx_8h.md)

1/\*

2 \* Copyright (c) 2019 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_LMP90XXX\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_LMP90XXX\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12

13/\* LMP90xxx supports GPIO D0..D6 \*/

[ 14](lmp90xxx_8h.md#a4d1a76d266a648aa9ea4f831a37b2f78)#define LMP90XXX\_GPIO\_MAX 6

15

[ 16](lmp90xxx_8h.md#a1e17998cc9fcded05d18c5bf15ee4289)int [lmp90xxx\_gpio\_set\_output](lmp90xxx_8h.md#a1e17998cc9fcded05d18c5bf15ee4289)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

17

[ 18](lmp90xxx_8h.md#a8a0f64db753e7d5d789563b1521cb795)int [lmp90xxx\_gpio\_set\_input](lmp90xxx_8h.md#a8a0f64db753e7d5d789563b1521cb795)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

19

[ 20](lmp90xxx_8h.md#a0d516dc704a18efde862c5eef73d571c)int [lmp90xxx\_gpio\_set\_pin\_value](lmp90xxx_8h.md#a0d516dc704a18efde862c5eef73d571c)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin,

21 bool value);

22

[ 23](lmp90xxx_8h.md#a8ac7fc5e8fb30e4789f40ecaf4c37a3e)int [lmp90xxx\_gpio\_get\_pin\_value](lmp90xxx_8h.md#a8ac7fc5e8fb30e4789f40ecaf4c37a3e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin,

24 bool \*value);

25

[ 26](lmp90xxx_8h.md#a43342a79e50eb313a17e7c81aeda86e5)int [lmp90xxx\_gpio\_port\_get\_raw](lmp90xxx_8h.md#a43342a79e50eb313a17e7c81aeda86e5)(const struct [device](structdevice.md) \*dev,

27 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value);

28

[ 29](lmp90xxx_8h.md#a1b16f4a754035047e4fb614905203a97)int [lmp90xxx\_gpio\_port\_set\_masked\_raw](lmp90xxx_8h.md#a1b16f4a754035047e4fb614905203a97)(const struct [device](structdevice.md) \*dev,

30 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask,

31 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value);

32

[ 33](lmp90xxx_8h.md#adff5b68dbf1ac67c274f77de7b72e64e)int [lmp90xxx\_gpio\_port\_set\_bits\_raw](lmp90xxx_8h.md#adff5b68dbf1ac67c274f77de7b72e64e)(const struct [device](structdevice.md) \*dev,

34 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

35

[ 36](lmp90xxx_8h.md#a3fc83c28427940e410f11558fa8208ad)int [lmp90xxx\_gpio\_port\_clear\_bits\_raw](lmp90xxx_8h.md#a3fc83c28427940e410f11558fa8208ad)(const struct [device](structdevice.md) \*dev,

37 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

38

[ 39](lmp90xxx_8h.md#a0a1d236bdb7e1a1a0ab472963a61627e)int [lmp90xxx\_gpio\_port\_toggle\_bits](lmp90xxx_8h.md#a0a1d236bdb7e1a1a0ab472963a61627e)(const struct [device](structdevice.md) \*dev,

40 [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins);

41

42#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_LMP90XXX\_H\_ \*/

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

[lmp90xxx\_gpio\_port\_toggle\_bits](lmp90xxx_8h.md#a0a1d236bdb7e1a1a0ab472963a61627e)

int lmp90xxx\_gpio\_port\_toggle\_bits(const struct device \*dev, gpio\_port\_pins\_t pins)

[lmp90xxx\_gpio\_set\_pin\_value](lmp90xxx_8h.md#a0d516dc704a18efde862c5eef73d571c)

int lmp90xxx\_gpio\_set\_pin\_value(const struct device \*dev, uint8\_t pin, bool value)

[lmp90xxx\_gpio\_port\_set\_masked\_raw](lmp90xxx_8h.md#a1b16f4a754035047e4fb614905203a97)

int lmp90xxx\_gpio\_port\_set\_masked\_raw(const struct device \*dev, gpio\_port\_pins\_t mask, gpio\_port\_value\_t value)

[lmp90xxx\_gpio\_set\_output](lmp90xxx_8h.md#a1e17998cc9fcded05d18c5bf15ee4289)

int lmp90xxx\_gpio\_set\_output(const struct device \*dev, uint8\_t pin)

[lmp90xxx\_gpio\_port\_clear\_bits\_raw](lmp90xxx_8h.md#a3fc83c28427940e410f11558fa8208ad)

int lmp90xxx\_gpio\_port\_clear\_bits\_raw(const struct device \*dev, gpio\_port\_pins\_t pins)

[lmp90xxx\_gpio\_port\_get\_raw](lmp90xxx_8h.md#a43342a79e50eb313a17e7c81aeda86e5)

int lmp90xxx\_gpio\_port\_get\_raw(const struct device \*dev, gpio\_port\_value\_t \*value)

[lmp90xxx\_gpio\_set\_input](lmp90xxx_8h.md#a8a0f64db753e7d5d789563b1521cb795)

int lmp90xxx\_gpio\_set\_input(const struct device \*dev, uint8\_t pin)

[lmp90xxx\_gpio\_get\_pin\_value](lmp90xxx_8h.md#a8ac7fc5e8fb30e4789f40ecaf4c37a3e)

int lmp90xxx\_gpio\_get\_pin\_value(const struct device \*dev, uint8\_t pin, bool \*value)

[lmp90xxx\_gpio\_port\_set\_bits\_raw](lmp90xxx_8h.md#adff5b68dbf1ac67c274f77de7b72e64e)

int lmp90xxx\_gpio\_port\_set\_bits\_raw(const struct device \*dev, gpio\_port\_pins\_t pins)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [lmp90xxx.h](lmp90xxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
