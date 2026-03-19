---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ads1x4s0x__adc_8h_source.html
original_path: doxygen/html/ads1x4s0x__adc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ads1x4s0x\_adc.h

[Go to the documentation of this file.](ads1x4s0x__adc_8h.md)

1/\*

2 \* Copyright (c) 2023 SILA Embedded Solutions GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_ADS1X4S0X\_ADC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_ADS1X4S0X\_ADC\_H\_

9

10/\*

11 \* These are the available data rates described as samples per second. They

12 \* can be used with the time unit ticks for the acquisition time.

13 \*/

[ 14](ads1x4s0x__adc_8h.md#ab4008a6f7e0af79e4e2281d950ca1cea)#define ADS1X4S0X\_CONFIG\_DR\_2\_5 0

[ 15](ads1x4s0x__adc_8h.md#a59c2103463123737693f12ca3a0fb709)#define ADS1X4S0X\_CONFIG\_DR\_5 1

[ 16](ads1x4s0x__adc_8h.md#af53189327d8565c0ca5057c0840782f6)#define ADS1X4S0X\_CONFIG\_DR\_10 2

[ 17](ads1x4s0x__adc_8h.md#acfcd26405d1840c6f64a0300bac656e9)#define ADS1X4S0X\_CONFIG\_DR\_16\_6 3

[ 18](ads1x4s0x__adc_8h.md#a6f30983bf73ed95f186aef27e84b50f6)#define ADS1X4S0X\_CONFIG\_DR\_20 4

[ 19](ads1x4s0x__adc_8h.md#a5066e29a46c2acf6ff35102ad0386691)#define ADS1X4S0X\_CONFIG\_DR\_50 5

[ 20](ads1x4s0x__adc_8h.md#afaafe40f49c783d91f54bf90bd114629)#define ADS1X4S0X\_CONFIG\_DR\_60 6

[ 21](ads1x4s0x__adc_8h.md#a23fcbdddcd18d3a50e883f7926f0ccde)#define ADS1X4S0X\_CONFIG\_DR\_100 7

[ 22](ads1x4s0x__adc_8h.md#ad04d6cb3429d4c0b9247e57f9b587e55)#define ADS1X4S0X\_CONFIG\_DR\_200 8

[ 23](ads1x4s0x__adc_8h.md#a77f766a1ded7be1de435c027e45e6c68)#define ADS1X4S0X\_CONFIG\_DR\_400 9

[ 24](ads1x4s0x__adc_8h.md#a15e869a53480c2652bb9c8aa5dd41f57)#define ADS1X4S0X\_CONFIG\_DR\_800 10

[ 25](ads1x4s0x__adc_8h.md#a113c878ed4e1e4921499e0112ab28b29)#define ADS1X4S0X\_CONFIG\_DR\_1000 11

[ 26](ads1x4s0x__adc_8h.md#a75ae507fb527f362db909eec73b62bb4)#define ADS1X4S0X\_CONFIG\_DR\_2000 12

[ 27](ads1x4s0x__adc_8h.md#a67d5ebb5009cf6c28b2946e20ead5d18)#define ADS1X4S0X\_CONFIG\_DR\_4000 13

28

29#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_ADS1X4S0X\_ADC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [ads1x4s0x\_adc.h](ads1x4s0x__adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
