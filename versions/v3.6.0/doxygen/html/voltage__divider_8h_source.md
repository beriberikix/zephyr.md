---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/voltage__divider_8h_source.html
original_path: doxygen/html/voltage__divider_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

voltage\_divider.h

[Go to the documentation of this file.](voltage__divider_8h.md)

1/\*

2 \* Copyright (c) 2023 The ChromiumOS Authors

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_VOLTAGE\_DIVIDER\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_VOLTAGE\_DIVIDER\_H\_

9

10#include <[zephyr/drivers/adc.h](drivers_2adc_8h.md)>

11

[ 12](structvoltage__divider__dt__spec.md)struct [voltage\_divider\_dt\_spec](structvoltage__divider__dt__spec.md) {

[ 13](structvoltage__divider__dt__spec.md#a3492bc4b95943a2848dbb05f0b3fb355) const struct [adc\_dt\_spec](structadc__dt__spec.md) [port](structvoltage__divider__dt__spec.md#a3492bc4b95943a2848dbb05f0b3fb355);

[ 14](structvoltage__divider__dt__spec.md#a22eb443d2dd34dcf04c2badb94f00816) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [full\_ohms](structvoltage__divider__dt__spec.md#a22eb443d2dd34dcf04c2badb94f00816);

[ 15](structvoltage__divider__dt__spec.md#a8960e3614c0a3d9ddc543037a51e7a8e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [output\_ohms](structvoltage__divider__dt__spec.md#a8960e3614c0a3d9ddc543037a51e7a8e);

16};

17

[ 28](voltage__divider_8h.md#a4ed91297930bbf6b865075a9e9ba2bce)#define VOLTAGE\_DIVIDER\_DT\_SPEC\_GET(node\_id) \

29 { \

30 .port = ADC\_DT\_SPEC\_GET(node\_id), \

31 .full\_ohms = DT\_PROP\_OR(node\_id, full\_ohms, 0), \

32 .output\_ohms = DT\_PROP(node\_id, output\_ohms), \

33 }

34

[ 45](voltage__divider_8h.md#a891c6ee6073582761e63cadeaf228563)static inline int [voltage\_divider\_scale\_dt](voltage__divider_8h.md#a891c6ee6073582761e63cadeaf228563)(const struct [voltage\_divider\_dt\_spec](structvoltage__divider__dt__spec.md) \*spec,

46 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*v\_to\_v)

47{

48 /\* cannot be scaled if "full\_ohms" is not specified \*/

49 if (spec->[full\_ohms](structvoltage__divider__dt__spec.md#a22eb443d2dd34dcf04c2badb94f00816) == 0) {

50 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

51 }

52

53 /\* voltage scaled by voltage divider values using DT binding \*/

54 \*v\_to\_v = \*v\_to\_v \* spec->[full\_ohms](structvoltage__divider__dt__spec.md#a22eb443d2dd34dcf04c2badb94f00816) / spec->[output\_ohms](structvoltage__divider__dt__spec.md#a8960e3614c0a3d9ddc543037a51e7a8e);

55

56 return 0;

57}

58

59#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ADC\_VOLTAGE\_DIVIDER\_H\_ \*/

[adc.h](drivers_2adc_8h.md)

ADC public API header file.

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[adc\_dt\_spec](structadc__dt__spec.md)

Container for ADC channel information specified in devicetree.

**Definition** adc.h:247

[voltage\_divider\_dt\_spec](structvoltage__divider__dt__spec.md)

**Definition** voltage\_divider.h:12

[voltage\_divider\_dt\_spec::full\_ohms](structvoltage__divider__dt__spec.md#a22eb443d2dd34dcf04c2badb94f00816)

uint32\_t full\_ohms

**Definition** voltage\_divider.h:14

[voltage\_divider\_dt\_spec::port](structvoltage__divider__dt__spec.md#a3492bc4b95943a2848dbb05f0b3fb355)

const struct adc\_dt\_spec port

**Definition** voltage\_divider.h:13

[voltage\_divider\_dt\_spec::output\_ohms](structvoltage__divider__dt__spec.md#a8960e3614c0a3d9ddc543037a51e7a8e)

uint32\_t output\_ohms

**Definition** voltage\_divider.h:15

[voltage\_divider\_scale\_dt](voltage__divider_8h.md#a891c6ee6073582761e63cadeaf228563)

static int voltage\_divider\_scale\_dt(const struct voltage\_divider\_dt\_spec \*spec, int32\_t \*v\_to\_v)

Calculates the actual voltage from the measured voltage.

**Definition** voltage\_divider.h:45

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [voltage\_divider.h](voltage__divider_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
