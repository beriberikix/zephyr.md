---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32g0__b1x__c1x__clock_8h_source.html
original_path: doxygen/html/stm32g0__b1x__c1x__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32g0\_b1x\_c1x\_clock.h

[Go to the documentation of this file.](stm32g0__b1x__c1x__clock_8h.md)

1/\*

2 \* Copyright (c) 2025 Andreas Schuster <andreas.schuster@schuam.de>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G0\_B1X\_C1X\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G0\_B1X\_C1X\_CLOCK\_H\_

9

10/\* MCO prescaler : division factor \*/

[ 11](stm32g0__b1x__c1x__clock_8h.md#aaaccd25cab308cd0a5da467e3c28acb3)#define MCO\_PRE\_DIV\_256 8

[ 12](stm32g0__b1x__c1x__clock_8h.md#a59a17981d4e337c950cd258f9ba464cf)#define MCO\_PRE\_DIV\_512 9

[ 13](stm32g0__b1x__c1x__clock_8h.md#a08087a5c8c099ba45e3b7e83d200e9a0)#define MCO\_PRE\_DIV\_1024 10

14

15/\* MCO clock output \*/

[ 16](stm32g0__b1x__c1x__clock_8h.md#ab74b0b6d5a187d6542339aa2204d46cb)#define MCO\_SEL\_HSI48 2

[ 17](stm32g0__b1x__c1x__clock_8h.md#a05dd5a084157dfc52a879af729536bf8)#define MCO\_SEL\_PLLPCLK 8

[ 18](stm32g0__b1x__c1x__clock_8h.md#a2d0f0eac3d83b0d547822d91a258f913)#define MCO\_SEL\_PLLQCLK 9

[ 19](stm32g0__b1x__c1x__clock_8h.md#a9a636acc7d3d17f4c6e338d7a060db1b)#define MCO\_SEL\_RTCCLK 10

[ 20](stm32g0__b1x__c1x__clock_8h.md#ab92e31fc0923b1d21f3c4cee7a4a356e)#define MCO\_SEL\_RTCWAKEUP 11

21

22#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32G0\_B1X\_C1X\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32g0\_b1x\_c1x\_clock.h](stm32g0__b1x__c1x__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
