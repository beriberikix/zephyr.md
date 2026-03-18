---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dt-bindings_2adc_2adc_8h_source.html
original_path: doxygen/html/dt-bindings_2adc_2adc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc.h

[Go to the documentation of this file.](dt-bindings_2adc_2adc_8h.md)

1/\*

2 \* Copyright 2021 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_ADC\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_ADC\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

[ 12](dt-bindings_2adc_2adc_8h.md#aa80dca07e438ccb1c4f45b9a8052f44e)#define ADC\_ACQ\_TIME\_MICROSECONDS (1)

[ 14](dt-bindings_2adc_2adc_8h.md#a1d7580e098809a5ba2dec139a05af988)#define ADC\_ACQ\_TIME\_NANOSECONDS (2)

[ 16](dt-bindings_2adc_2adc_8h.md#acff5af9f7a7b49bbfeab1b6716c7c18f)#define ADC\_ACQ\_TIME\_TICKS (3)

[ 18](dt-bindings_2adc_2adc_8h.md#a313a316cb91adcef0125679220efe2b7)#define ADC\_ACQ\_TIME(unit, value) (((unit) << 14) | ((value) & BIT\_MASK(14)))

[ 20](dt-bindings_2adc_2adc_8h.md#a3f0840d3d6300e9c26be1b2889ecbd54)#define ADC\_ACQ\_TIME\_DEFAULT 0

[ 21](dt-bindings_2adc_2adc_8h.md#a5c89f077922d9b84229b5525f5408ebe)#define ADC\_ACQ\_TIME\_MAX BIT\_MASK(14)

22

[ 23](dt-bindings_2adc_2adc_8h.md#ae66e4a40b8e4b1e34c68b806363b95cf)#define ADC\_ACQ\_TIME\_UNIT(time) (((time) >> 14) & BIT\_MASK(2))

[ 24](dt-bindings_2adc_2adc_8h.md#a720640550d3a29e0181819ec31d5dda6)#define ADC\_ACQ\_TIME\_VALUE(time) ((time) & BIT\_MASK(14))

25

26#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_ADC\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [adc.h](dt-bindings_2adc_2adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
