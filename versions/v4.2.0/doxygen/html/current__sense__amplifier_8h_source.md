---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/current__sense__amplifier_8h_source.html
original_path: doxygen/html/current__sense__amplifier_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

[ 14](structcurrent__sense__amplifier__dt__spec.md#aed51d08ce3824d91f31b7ad64926c667) struct [adc\_dt\_spec](structadc__dt__spec.md) [port](structcurrent__sense__amplifier__dt__spec.md#aed51d08ce3824d91f31b7ad64926c667);

[ 15](structcurrent__sense__amplifier__dt__spec.md#af35fab6c94e4d95ba850e8ba2e4a0961) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [power\_gpio](structcurrent__sense__amplifier__dt__spec.md#af35fab6c94e4d95ba850e8ba2e4a0961);

[ 16](structcurrent__sense__amplifier__dt__spec.md#ad6efaf2c197a7ca3db1085aa900aed23) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sense\_milli\_ohms](structcurrent__sense__amplifier__dt__spec.md#ad6efaf2c197a7ca3db1085aa900aed23);

[ 17](structcurrent__sense__amplifier__dt__spec.md#a8c7af3b111721f0b654a3943670c5614) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sense\_gain\_mult](structcurrent__sense__amplifier__dt__spec.md#a8c7af3b111721f0b654a3943670c5614);

[ 18](structcurrent__sense__amplifier__dt__spec.md#a3f94f49afc001c36ed42ae640bb7b157) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sense\_gain\_div](structcurrent__sense__amplifier__dt__spec.md#a3f94f49afc001c36ed42ae640bb7b157);

[ 19](structcurrent__sense__amplifier__dt__spec.md#a140af0a4a6bcf73149dc7eec69b87e7b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [noise\_threshold](structcurrent__sense__amplifier__dt__spec.md#a140af0a4a6bcf73149dc7eec69b87e7b);

[ 20](structcurrent__sense__amplifier__dt__spec.md#a4f1e3b2bba6178fa5d36f1d734ce1111) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [zero\_current\_voltage\_mv](structcurrent__sense__amplifier__dt__spec.md#a4f1e3b2bba6178fa5d36f1d734ce1111);

[ 21](structcurrent__sense__amplifier__dt__spec.md#a37f6a98c94ec822854608fef74df8ee7) bool [enable\_calibration](structcurrent__sense__amplifier__dt__spec.md#a37f6a98c94ec822854608fef74df8ee7);

22};

23

[ 34](current__sense__amplifier_8h.md#a17093e63c3ccd1e08e38ad1e0aeb9d8c)#define CURRENT\_SENSE\_AMPLIFIER\_DT\_SPEC\_GET(node\_id) \

35 { \

36 .port = ADC\_DT\_SPEC\_GET(node\_id), \

37 .power\_gpio = GPIO\_DT\_SPEC\_GET\_OR(node\_id, power\_gpios, {0}), \

38 .sense\_milli\_ohms = DT\_PROP(node\_id, sense\_resistor\_milli\_ohms), \

39 .sense\_gain\_mult = DT\_PROP(node\_id, sense\_gain\_mult), \

40 .sense\_gain\_div = DT\_PROP(node\_id, sense\_gain\_div), \

41 .noise\_threshold = DT\_PROP(node\_id, zephyr\_noise\_threshold), \

42 .zero\_current\_voltage\_mv = DT\_PROP(node\_id, zero\_current\_voltage\_mv), \

43 .enable\_calibration = DT\_PROP\_OR(node\_id, enable\_calibration, false), \

44 }

45

53static inline void

[ 54](current__sense__amplifier_8h.md#aeaa2149527103e5c0e6a636cb3e9aad4)[current\_sense\_amplifier\_scale\_dt](current__sense__amplifier_8h.md#aeaa2149527103e5c0e6a636cb3e9aad4)(const struct [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md) \*spec,

55 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*v\_to\_i)

56{

57 /\* store in a temporary 64 bit variable to prevent overflow during calculation \*/

58 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) tmp = \*v\_to\_i;

59

60 /\* (INT32\_MAX \* 1000 \* UINT16\_MAX) < INT64\_MAX

61 \* Therefore all multiplications can be done before divisions, preserving resolution.

62 \*/

63 tmp = tmp - spec->[zero\_current\_voltage\_mv](structcurrent__sense__amplifier__dt__spec.md#a4f1e3b2bba6178fa5d36f1d734ce1111);

64 tmp = tmp \* 1000 \* spec->[sense\_gain\_div](structcurrent__sense__amplifier__dt__spec.md#a3f94f49afc001c36ed42ae640bb7b157) / spec->[sense\_milli\_ohms](structcurrent__sense__amplifier__dt__spec.md#ad6efaf2c197a7ca3db1085aa900aed23) / spec->[sense\_gain\_mult](structcurrent__sense__amplifier__dt__spec.md#a8c7af3b111721f0b654a3943670c5614);

65

66 \*v\_to\_i = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))tmp;

67}

68

69#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_CURRENT\_SENSE\_AMPLIFIER\_H\_ \*/

[current\_sense\_amplifier\_scale\_dt](current__sense__amplifier_8h.md#aeaa2149527103e5c0e6a636cb3e9aad4)

static void current\_sense\_amplifier\_scale\_dt(const struct current\_sense\_amplifier\_dt\_spec \*spec, int32\_t \*v\_to\_i)

Calculates the actual amperage from the measured voltage.

**Definition** current\_sense\_amplifier.h:54

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

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[adc\_dt\_spec](structadc__dt__spec.md)

Container for ADC channel information specified in devicetree.

**Definition** adc.h:282

[current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md)

**Definition** current\_sense\_amplifier.h:13

[current\_sense\_amplifier\_dt\_spec::noise\_threshold](structcurrent__sense__amplifier__dt__spec.md#a140af0a4a6bcf73149dc7eec69b87e7b)

uint16\_t noise\_threshold

**Definition** current\_sense\_amplifier.h:19

[current\_sense\_amplifier\_dt\_spec::enable\_calibration](structcurrent__sense__amplifier__dt__spec.md#a37f6a98c94ec822854608fef74df8ee7)

bool enable\_calibration

**Definition** current\_sense\_amplifier.h:21

[current\_sense\_amplifier\_dt\_spec::sense\_gain\_div](structcurrent__sense__amplifier__dt__spec.md#a3f94f49afc001c36ed42ae640bb7b157)

uint16\_t sense\_gain\_div

**Definition** current\_sense\_amplifier.h:18

[current\_sense\_amplifier\_dt\_spec::zero\_current\_voltage\_mv](structcurrent__sense__amplifier__dt__spec.md#a4f1e3b2bba6178fa5d36f1d734ce1111)

int16\_t zero\_current\_voltage\_mv

**Definition** current\_sense\_amplifier.h:20

[current\_sense\_amplifier\_dt\_spec::sense\_gain\_mult](structcurrent__sense__amplifier__dt__spec.md#a8c7af3b111721f0b654a3943670c5614)

uint16\_t sense\_gain\_mult

**Definition** current\_sense\_amplifier.h:17

[current\_sense\_amplifier\_dt\_spec::sense\_milli\_ohms](structcurrent__sense__amplifier__dt__spec.md#ad6efaf2c197a7ca3db1085aa900aed23)

uint32\_t sense\_milli\_ohms

**Definition** current\_sense\_amplifier.h:16

[current\_sense\_amplifier\_dt\_spec::port](structcurrent__sense__amplifier__dt__spec.md#aed51d08ce3824d91f31b7ad64926c667)

struct adc\_dt\_spec port

**Definition** current\_sense\_amplifier.h:14

[current\_sense\_amplifier\_dt\_spec::power\_gpio](structcurrent__sense__amplifier__dt__spec.md#af35fab6c94e4d95ba850e8ba2e4a0961)

struct gpio\_dt\_spec power\_gpio

**Definition** current\_sense\_amplifier.h:15

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:289

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [current\_sense\_amplifier.h](current__sense__amplifier_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
