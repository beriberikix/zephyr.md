---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/current__sense__amplifier_8h_source.html
original_path: doxygen/html/current__sense__amplifier_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

current\_sense\_amplifier.h

[Go to the documentation of this file.](current__sense__amplifier_8h.md)

1/\*

2 \* Copyright (c) 2023 The ChromiumOS Authors

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_CURRENT\_SENSE\_AMPLIFIER\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_CURRENT\_SENSE\_AMPLIFIER\_H\_

9

10#include <[zephyr/drivers/adc.h](drivers_2adc_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12

[ 13](structcurrent__sense__amplifier__dt__spec.md)struct [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md) {

[ 14](structcurrent__sense__amplifier__dt__spec.md#a98bdc38aeb90906cf2536408ba90aa7e) const struct [adc\_dt\_spec](structadc__dt__spec.md) [port](structcurrent__sense__amplifier__dt__spec.md#a98bdc38aeb90906cf2536408ba90aa7e);

[ 15](structcurrent__sense__amplifier__dt__spec.md#ad1af3e088bcdff151b4fc1a71fadf58f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sense\_micro\_ohms](structcurrent__sense__amplifier__dt__spec.md#ad1af3e088bcdff151b4fc1a71fadf58f);

[ 16](structcurrent__sense__amplifier__dt__spec.md#aa0b6eecdad6c809ff548d21f0626a5ff) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sense\_gain\_mult](structcurrent__sense__amplifier__dt__spec.md#aa0b6eecdad6c809ff548d21f0626a5ff);

[ 17](structcurrent__sense__amplifier__dt__spec.md#a1b1a7e7558ad17b5fb55c48a30de6a1c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sense\_gain\_div](structcurrent__sense__amplifier__dt__spec.md#a1b1a7e7558ad17b5fb55c48a30de6a1c);

[ 18](structcurrent__sense__amplifier__dt__spec.md#af35fab6c94e4d95ba850e8ba2e4a0961) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [power\_gpio](structcurrent__sense__amplifier__dt__spec.md#af35fab6c94e4d95ba850e8ba2e4a0961);

19};

20

[ 31](current__sense__amplifier_8h.md#a17093e63c3ccd1e08e38ad1e0aeb9d8c)#define CURRENT\_SENSE\_AMPLIFIER\_DT\_SPEC\_GET(node\_id) \

32 { \

33 .port = ADC\_DT\_SPEC\_GET(node\_id), \

34 .sense\_micro\_ohms = DT\_PROP(node\_id, sense\_resistor\_micro\_ohms), \

35 .sense\_gain\_mult = DT\_PROP(node\_id, sense\_gain\_mult), \

36 .sense\_gain\_div = DT\_PROP(node\_id, sense\_gain\_div), \

37 .power\_gpio = GPIO\_DT\_SPEC\_GET\_OR(node\_id, power\_gpios, {0}), \

38 }

39

47static inline void

[ 48](current__sense__amplifier_8h.md#aeaa2149527103e5c0e6a636cb3e9aad4)[current\_sense\_amplifier\_scale\_dt](current__sense__amplifier_8h.md#aeaa2149527103e5c0e6a636cb3e9aad4)(const struct [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md) \*spec,

49 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*v\_to\_i)

50{

51 /\* store in a temporary 64 bit variable to prevent overflow during calculation \*/

52 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) tmp = \*v\_to\_i;

53

54 /\* multiplies by 1,000,000 before dividing by sense resistance in micro-ohms. \*/

55 tmp = tmp \* 1000000 / spec->[sense\_micro\_ohms](structcurrent__sense__amplifier__dt__spec.md#ad1af3e088bcdff151b4fc1a71fadf58f) \* spec->[sense\_gain\_div](structcurrent__sense__amplifier__dt__spec.md#a1b1a7e7558ad17b5fb55c48a30de6a1c) / spec->[sense\_gain\_mult](structcurrent__sense__amplifier__dt__spec.md#aa0b6eecdad6c809ff548d21f0626a5ff);

56

57 \*v\_to\_i = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))tmp;

58}

59

60#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_CURRENT\_SENSE\_AMPLIFIER\_H\_ \*/

[current\_sense\_amplifier\_scale\_dt](current__sense__amplifier_8h.md#aeaa2149527103e5c0e6a636cb3e9aad4)

static void current\_sense\_amplifier\_scale\_dt(const struct current\_sense\_amplifier\_dt\_spec \*spec, int32\_t \*v\_to\_i)

Calculates the actual amperage from the measured voltage.

**Definition** current\_sense\_amplifier.h:48

[adc.h](drivers_2adc_8h.md)

ADC public API header file.

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

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

**Definition** adc.h:264

[current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md)

**Definition** current\_sense\_amplifier.h:13

[current\_sense\_amplifier\_dt\_spec::sense\_gain\_div](structcurrent__sense__amplifier__dt__spec.md#a1b1a7e7558ad17b5fb55c48a30de6a1c)

uint32\_t sense\_gain\_div

**Definition** current\_sense\_amplifier.h:17

[current\_sense\_amplifier\_dt\_spec::port](structcurrent__sense__amplifier__dt__spec.md#a98bdc38aeb90906cf2536408ba90aa7e)

const struct adc\_dt\_spec port

**Definition** current\_sense\_amplifier.h:14

[current\_sense\_amplifier\_dt\_spec::sense\_gain\_mult](structcurrent__sense__amplifier__dt__spec.md#aa0b6eecdad6c809ff548d21f0626a5ff)

uint32\_t sense\_gain\_mult

**Definition** current\_sense\_amplifier.h:16

[current\_sense\_amplifier\_dt\_spec::sense\_micro\_ohms](structcurrent__sense__amplifier__dt__spec.md#ad1af3e088bcdff151b4fc1a71fadf58f)

uint32\_t sense\_micro\_ohms

**Definition** current\_sense\_amplifier.h:15

[current\_sense\_amplifier\_dt\_spec::power\_gpio](structcurrent__sense__amplifier__dt__spec.md#af35fab6c94e4d95ba850e8ba2e4a0961)

struct gpio\_dt\_spec power\_gpio

**Definition** current\_sense\_amplifier.h:18

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:288

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [current\_sense\_amplifier.h](current__sense__amplifier_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
