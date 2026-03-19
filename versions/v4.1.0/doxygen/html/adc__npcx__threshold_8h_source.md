---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/adc__npcx__threshold_8h_source.html
original_path: doxygen/html/adc__npcx__threshold_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_npcx\_threshold.h

[Go to the documentation of this file.](adc__npcx__threshold_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_ADC\_NPCX\_THRESHOLD\_H\_

8#define \_ADC\_NPCX\_THRESHOLD\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11

[ 12](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eec)enum [adc\_npcx\_threshold\_param\_l\_h](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eec) {

[ 13](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eeca7f0b6e9c183da7426bee511d71622ce6) [ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_HIGHER](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eeca7f0b6e9c183da7426bee511d71622ce6),

[ 14](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eeca66fe94a1fc6250b615a49bc282ec31b2) [ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_LOWER](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eeca66fe94a1fc6250b615a49bc282ec31b2),

15};

16

[ 17](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461)enum [adc\_npcx\_threshold\_param\_type](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461) {

18 /\* Selects ADC channel to be used for measurement \*/

[ 19](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ab00b9cf39929edf5221af6bf147fb79b) [ADC\_NPCX\_THRESHOLD\_PARAM\_CHNSEL](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ab00b9cf39929edf5221af6bf147fb79b),

20 /\* Sets relation between measured value and assetion threshold value.\*/

[ 21](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ad5183bef3339ba7ee07f32c34e7d7713) [ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ad5183bef3339ba7ee07f32c34e7d7713),

22 /\* Sets the threshold value to which measured data is compared. \*/

[ 23](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ae260faa6cb77b1466898a47de1cc35eb) [ADC\_NPCX\_THRESHOLD\_PARAM\_THVAL](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ae260faa6cb77b1466898a47de1cc35eb),

24 /\* Sets worker queue thread to be notified \*/

[ 25](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461a20f6e3a525932decdedae74b73ce62b3) [ADC\_NPCX\_THRESHOLD\_PARAM\_WORK](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461a20f6e3a525932decdedae74b73ce62b3),

26

[ 27](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461a61da0191e7147c0634a954ba543f1004) [ADC\_NPCX\_THRESHOLD\_PARAM\_MAX](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461a61da0191e7147c0634a954ba543f1004),

28};

29

[ 30](structadc__npcx__threshold__param.md)struct [adc\_npcx\_threshold\_param](structadc__npcx__threshold__param.md) {

31 /\* Threshold ocntrol parameter \*/

[ 32](structadc__npcx__threshold__param.md#a737a6f60a6bcf9fe952f957b0b67c777) enum [adc\_npcx\_threshold\_param\_type](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461) [type](structadc__npcx__threshold__param.md#a737a6f60a6bcf9fe952f957b0b67c777);

33 /\* Parameter value \*/

[ 34](structadc__npcx__threshold__param.md#a250120d513253a21c9581b74093ca2c7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [val](structadc__npcx__threshold__param.md#a250120d513253a21c9581b74093ca2c7);

35};

36

[ 51](adc__npcx__threshold_8h.md#ad0d9a6c968a0699e270d07cb35a54834)int [adc\_npcx\_threshold\_mv\_to\_thrval](adc__npcx__threshold_8h.md#ad0d9a6c968a0699e270d07cb35a54834)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val\_mv,

52 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*thrval);

53

[ 68](adc__npcx__threshold_8h.md#a8cb8e7d8947eaae2503e742cbd747f7f)int [adc\_npcx\_threshold\_ctrl\_set\_param](adc__npcx__threshold_8h.md#a8cb8e7d8947eaae2503e742cbd747f7f)(const struct [device](structdevice.md) \*dev,

69 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) th\_sel,

70 const struct [adc\_npcx\_threshold\_param](structadc__npcx__threshold__param.md)

71 \*param);

72

[ 87](adc__npcx__threshold_8h.md#acd6441b45603ce1b3766a0ef24ffbe69)int [adc\_npcx\_threshold\_ctrl\_enable](adc__npcx__threshold_8h.md#acd6441b45603ce1b3766a0ef24ffbe69)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) th\_sel,

88 const bool enable);

89

90#endif /\*\_ADC\_NPCX\_THRESHOLD\_H\_ \*/

[adc\_npcx\_threshold\_param\_l\_h](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eec)

adc\_npcx\_threshold\_param\_l\_h

**Definition** adc\_npcx\_threshold.h:12

[ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_LOWER](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eeca66fe94a1fc6250b615a49bc282ec31b2)

@ ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_LOWER

**Definition** adc\_npcx\_threshold.h:14

[ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_HIGHER](adc__npcx__threshold_8h.md#a38f7d862a13c7894b71ff6750ab56eeca7f0b6e9c183da7426bee511d71622ce6)

@ ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H\_HIGHER

**Definition** adc\_npcx\_threshold.h:13

[adc\_npcx\_threshold\_param\_type](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461)

adc\_npcx\_threshold\_param\_type

**Definition** adc\_npcx\_threshold.h:17

[ADC\_NPCX\_THRESHOLD\_PARAM\_WORK](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461a20f6e3a525932decdedae74b73ce62b3)

@ ADC\_NPCX\_THRESHOLD\_PARAM\_WORK

**Definition** adc\_npcx\_threshold.h:25

[ADC\_NPCX\_THRESHOLD\_PARAM\_MAX](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461a61da0191e7147c0634a954ba543f1004)

@ ADC\_NPCX\_THRESHOLD\_PARAM\_MAX

**Definition** adc\_npcx\_threshold.h:27

[ADC\_NPCX\_THRESHOLD\_PARAM\_CHNSEL](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ab00b9cf39929edf5221af6bf147fb79b)

@ ADC\_NPCX\_THRESHOLD\_PARAM\_CHNSEL

**Definition** adc\_npcx\_threshold.h:19

[ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ad5183bef3339ba7ee07f32c34e7d7713)

@ ADC\_NPCX\_THRESHOLD\_PARAM\_L\_H

**Definition** adc\_npcx\_threshold.h:21

[ADC\_NPCX\_THRESHOLD\_PARAM\_THVAL](adc__npcx__threshold_8h.md#a7da5b595bef1edfb12ad8223fb7fc461ae260faa6cb77b1466898a47de1cc35eb)

@ ADC\_NPCX\_THRESHOLD\_PARAM\_THVAL

**Definition** adc\_npcx\_threshold.h:23

[adc\_npcx\_threshold\_ctrl\_set\_param](adc__npcx__threshold_8h.md#a8cb8e7d8947eaae2503e742cbd747f7f)

int adc\_npcx\_threshold\_ctrl\_set\_param(const struct device \*dev, const uint8\_t th\_sel, const struct adc\_npcx\_threshold\_param \*param)

Set ADC threshold parameter.

[adc\_npcx\_threshold\_ctrl\_enable](adc__npcx__threshold_8h.md#acd6441b45603ce1b3766a0ef24ffbe69)

int adc\_npcx\_threshold\_ctrl\_enable(const struct device \*dev, uint8\_t th\_sel, const bool enable)

Enables/Disables ADC threshold interruption.

[adc\_npcx\_threshold\_mv\_to\_thrval](adc__npcx__threshold_8h.md#ad0d9a6c968a0699e270d07cb35a54834)

int adc\_npcx\_threshold\_mv\_to\_thrval(const struct device \*dev, uint32\_t val\_mv, uint32\_t \*thrval)

Convert input value in millivolts to corresponding threshold register value.

[device.h](device_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[adc\_npcx\_threshold\_param](structadc__npcx__threshold__param.md)

**Definition** adc\_npcx\_threshold.h:30

[adc\_npcx\_threshold\_param::val](structadc__npcx__threshold__param.md#a250120d513253a21c9581b74093ca2c7)

uint32\_t val

**Definition** adc\_npcx\_threshold.h:34

[adc\_npcx\_threshold\_param::type](structadc__npcx__threshold__param.md#a737a6f60a6bcf9fe952f957b0b67c777)

enum adc\_npcx\_threshold\_param\_type type

**Definition** adc\_npcx\_threshold.h:32

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [adc\_npcx\_threshold.h](adc__npcx__threshold_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
