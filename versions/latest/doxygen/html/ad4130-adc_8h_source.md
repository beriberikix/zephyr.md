---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ad4130-adc_8h_source.html
original_path: doxygen/html/ad4130-adc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ad4130-adc.h

[Go to the documentation of this file.](ad4130-adc_8h.md)

1/\*

2 \* Copyright (c) 2025 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_AD4130\_ADC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_AD4130\_ADC\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

[ 12](ad4130-adc_8h.md#a61b8f834f97265f648ea6ca9976a2d58)#define AD4130\_ADC\_AIN0 0

[ 13](ad4130-adc_8h.md#af32d85ca8446d76a21ceba65ba2290ae)#define AD4130\_ADC\_AIN1 1

[ 14](ad4130-adc_8h.md#a5ac6aee617b3b563e1bd59267e54afa2)#define AD4130\_ADC\_AIN2 2

[ 15](ad4130-adc_8h.md#a3b91a25f4ea670770a9fd39773ddb6cc)#define AD4130\_ADC\_AIN3 3

[ 16](ad4130-adc_8h.md#ab6c30a79ea1bcd791ce9c4c4ece4136c)#define AD4130\_ADC\_AIN4 4

[ 17](ad4130-adc_8h.md#a26ad9e6689a867a03b839f547d50c7dd)#define AD4130\_ADC\_AIN5 5

[ 18](ad4130-adc_8h.md#a3c85a99258621c0f1e5a364072c477d1)#define AD4130\_ADC\_AIN6 6

[ 19](ad4130-adc_8h.md#ad6a18b66d294ae40c46d193797d065f7)#define AD4130\_ADC\_AIN7 7

[ 20](ad4130-adc_8h.md#a14853b94ecdd3ed71b421b81b5336512)#define AD4130\_ADC\_AIN8 8

[ 21](ad4130-adc_8h.md#a61755cbbc9896a290579f94a77c550b1)#define AD4130\_ADC\_AIN9 9

[ 22](ad4130-adc_8h.md#ab4eaffb5eb0ab4f47897f7bec527deef)#define AD4130\_ADC\_AIN10 10

[ 23](ad4130-adc_8h.md#a6285962876e282dfeb3bdba7d9a1012f)#define AD4130\_ADC\_AIN11 11

[ 24](ad4130-adc_8h.md#a5ff35034c041f261f58c073ee7c8d643)#define AD4130\_ADC\_AIN12 12

[ 25](ad4130-adc_8h.md#a78465ee29e6add5267c3e9d7e6dbebe8)#define AD4130\_ADC\_AIN13 13

[ 26](ad4130-adc_8h.md#accf168ca2da344079b5a1566ee0cd317)#define AD4130\_ADC\_AIN14 14

[ 27](ad4130-adc_8h.md#a3c153b4e2586efd1fd0908c0779abf5f)#define AD4130\_ADC\_AIN15 15

[ 28](ad4130-adc_8h.md#adc5fa5a23477c9839c27adb53611b3e5)#define AD4130\_ADC\_TEMP\_SENSOR 16

[ 29](ad4130-adc_8h.md#add463860e51c2b75c02331d946a3ca91)#define AD4130\_ADC\_AVSS 17

[ 30](ad4130-adc_8h.md#a58e33d9965acb6d229093405775693ee)#define AD4130\_ADC\_INTERNAL\_REF 18

[ 31](ad4130-adc_8h.md#a144b117cd2490b5bb7bf81ba7fac0bcf)#define AD4130\_ADC\_DGND 19

[ 32](ad4130-adc_8h.md#a8c58b63ece27a54e67ef3eed17932729)#define AD4130\_ADC\_AVDD\_AVSS\_DIV6\_PLUS 20

[ 33](ad4130-adc_8h.md#a47bfd72c13e1e3e21ac87e655b50c8b0)#define AD4130\_ADC\_AVDD\_AVSS\_DIV6\_MINUS 21

[ 34](ad4130-adc_8h.md#a0245369813adc98117fa48615d7e561f)#define AD4130\_ADC\_IOVDD\_DGND\_DIV6\_PLUS 22

[ 35](ad4130-adc_8h.md#acc23a71afaf9c4adff4682386caa144c)#define AD4130\_ADC\_IOVDD\_DGND\_DIV6\_MINUS 23

[ 36](ad4130-adc_8h.md#ae56c484271dcaa82abba9f882f4c582b)#define AD4130\_ADC\_ALDO\_AVSS\_DIV6\_PLUS 24

[ 37](ad4130-adc_8h.md#a3f0e165664c592c15246e1f1e5a29d66)#define AD4130\_ADC\_ALDO\_AVSS\_DIV6\_MINUS 25

[ 38](ad4130-adc_8h.md#ae284d9e0b235edaf6ce0fc3931e026b9)#define AD4130\_ADC\_DLDO\_DGND\_DIV6\_PLUS 26

[ 39](ad4130-adc_8h.md#adf030537bc18d2a1e7eda1425e73ead9)#define AD4130\_ADC\_DLDO\_DGND\_DIV6\_MINUS 27

[ 40](ad4130-adc_8h.md#ac7130a2f7604cf6ee2115d683d83f6fc)#define AD4130\_ADC\_V\_MV\_P 28

[ 41](ad4130-adc_8h.md#a0942d3fbc71b9af2c362850e6e458536)#define AD4130\_ADC\_V\_MV\_M 29

42

43#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_AD4130\_ADC\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [ad4130-adc.h](ad4130-adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
