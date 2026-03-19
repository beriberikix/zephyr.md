---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/current__sense__shunt_8h_source.html
original_path: doxygen/html/current__sense__shunt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

current\_sense\_shunt.h

[Go to the documentation of this file.](current__sense__shunt_8h.md)

1/\*

2 \* Copyright (c) 2023 The ChromiumOS Authors

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_CURRENT\_SENSE\_SHUNT\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_CURRENT\_SENSE\_SHUNT\_H\_

9

10#include <[zephyr/drivers/adc.h](drivers_2adc_8h.md)>

11

[ 12](structcurrent__sense__shunt__dt__spec.md)struct [current\_sense\_shunt\_dt\_spec](structcurrent__sense__shunt__dt__spec.md) {

[ 13](structcurrent__sense__shunt__dt__spec.md#ae57fb2bf3633908eef2597e33fd61d95) const struct [adc\_dt\_spec](structadc__dt__spec.md) [port](structcurrent__sense__shunt__dt__spec.md#ae57fb2bf3633908eef2597e33fd61d95);

[ 14](structcurrent__sense__shunt__dt__spec.md#ae58c3e0159b056cb0370141665869bf1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [shunt\_micro\_ohms](structcurrent__sense__shunt__dt__spec.md#ae58c3e0159b056cb0370141665869bf1);

15};

16

[ 27](current__sense__shunt_8h.md#a104c330fc7acfd17c7778aef24f399b8)#define CURRENT\_SENSE\_SHUNT\_DT\_SPEC\_GET(node\_id) \

28 { \

29 .port = ADC\_DT\_SPEC\_GET(node\_id), \

30 .shunt\_micro\_ohms = DT\_PROP(node\_id, shunt\_resistor\_micro\_ohms), \

31 }

32

[ 40](current__sense__shunt_8h.md#a2315a1aa2db9dafaff8c272b06d2c6b0)static inline void [current\_sense\_shunt\_scale\_dt](current__sense__shunt_8h.md#a2315a1aa2db9dafaff8c272b06d2c6b0)(const struct [current\_sense\_shunt\_dt\_spec](structcurrent__sense__shunt__dt__spec.md) \*spec,

41 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*v\_to\_i)

42{

43 /\* store in a temporary 64 bit variable to prevent overflow during calculation \*/

44 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) tmp = \*v\_to\_i;

45

46 /\* multiplies by 1,000,000 before dividing by shunt resistance in micro-ohms. \*/

47 tmp = tmp \* 1000000 / spec->[shunt\_micro\_ohms](structcurrent__sense__shunt__dt__spec.md#ae58c3e0159b056cb0370141665869bf1);

48

49 \*v\_to\_i = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))tmp;

50}

51

52#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_CURRENT\_SENSE\_SHUNT\_H\_ \*/

[current\_sense\_shunt\_scale\_dt](current__sense__shunt_8h.md#a2315a1aa2db9dafaff8c272b06d2c6b0)

static void current\_sense\_shunt\_scale\_dt(const struct current\_sense\_shunt\_dt\_spec \*spec, int32\_t \*v\_to\_i)

Calculates the actual amperage from the measured voltage.

**Definition** current\_sense\_shunt.h:40

[adc.h](drivers_2adc_8h.md)

ADC public API header file.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[adc\_dt\_spec](structadc__dt__spec.md)

Container for ADC channel information specified in devicetree.

**Definition** adc.h:265

[current\_sense\_shunt\_dt\_spec](structcurrent__sense__shunt__dt__spec.md)

**Definition** current\_sense\_shunt.h:12

[current\_sense\_shunt\_dt\_spec::port](structcurrent__sense__shunt__dt__spec.md#ae57fb2bf3633908eef2597e33fd61d95)

const struct adc\_dt\_spec port

**Definition** current\_sense\_shunt.h:13

[current\_sense\_shunt\_dt\_spec::shunt\_micro\_ohms](structcurrent__sense__shunt__dt__spec.md#ae58c3e0159b056cb0370141665869bf1)

uint32\_t shunt\_micro\_ohms

**Definition** current\_sense\_shunt.h:14

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [current\_sense\_shunt.h](current__sense__shunt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
