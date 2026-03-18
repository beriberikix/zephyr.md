---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/smartbond-adc_8h_source.html
original_path: doxygen/html/smartbond-adc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smartbond-adc.h

[Go to the documentation of this file.](smartbond-adc_8h.md)

1/\*

2 \* Copyright (c) 2023 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_SMARTBOND\_ADC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_SMARTBOND\_ADC\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

12/\* Values for DT zephyr,input-positive \*/

[ 13](smartbond-adc_8h.md#a5a88c8653e3ede14d2024faf298c917a)#define SMARTBOND\_GPADC\_P1\_09 0

[ 14](smartbond-adc_8h.md#accd024f3103bb6876f58d68fe1bb6bd7)#define SMARTBOND\_GPADC\_P0\_25 1

[ 15](smartbond-adc_8h.md#afb07ad4b6a2568464b5950c1bf3e176e)#define SMARTBOND\_GPADC\_P0\_08 2

[ 16](smartbond-adc_8h.md#ad077fbaafcefa2a3ac390fdffd86cd23)#define SMARTBOND\_GPADC\_P0\_09 3

[ 17](smartbond-adc_8h.md#ab4a9c920d6b88dc3f717f83d19fff822)#define SMARTBOND\_GPADC\_VDD 4

[ 18](smartbond-adc_8h.md#af459054a6e0128ce5b3a5406687fb9d0)#define SMARTBOND\_GPADC\_V30 5

[ 19](smartbond-adc_8h.md#ac1cfed07ae527d07aa339e65ea4950b7)#define SMARTBOND\_GPADC\_VBAT 8

[ 20](smartbond-adc_8h.md#a85229fb209179394e8796fae8f2fcc0a)#define SMARTBOND\_GPADC\_VSSA 9

[ 21](smartbond-adc_8h.md#a7bc0d3430a444f484f37133fd7d45439)#define SMARTBOND\_GPADC\_P1\_13 16

[ 22](smartbond-adc_8h.md#af8028c134a2398eba020b3b0f68294c6)#define SMARTBOND\_GPADC\_P1\_12 17

[ 23](smartbond-adc_8h.md#ad860145eb6e933ca69d4e1f421d3121a)#define SMARTBOND\_GPADC\_P1\_18 18

[ 24](smartbond-adc_8h.md#a3c7184d2a3c9eb9e5b503781a56fb1fd)#define SMARTBOND\_GPADC\_P1\_19 19

[ 25](smartbond-adc_8h.md#ad839283b380fcdc7d377d4ee294018c2)#define SMARTBOND\_GPADC\_TEMP 20

26

27/\* Values for DT zephyr,input-positive or input-negative \*/

[ 28](smartbond-adc_8h.md#ac3df3ec24988b7598965e7efe4a4c6b4)#define SMARTBOND\_SDADC\_P1\_09 0

[ 29](smartbond-adc_8h.md#aa50c58335f6f801a9d4b42a302972874)#define SMARTBOND\_SDADC\_P0\_25 1

[ 30](smartbond-adc_8h.md#acc8ff717e7778259b64d41820ce45071)#define SMARTBOND\_SDADC\_P0\_08 2

[ 31](smartbond-adc_8h.md#a348443a019423fd812548f0211a811d1)#define SMARTBOND\_SDADC\_P0\_09 3

[ 32](smartbond-adc_8h.md#a2e4f6d361ec9c2850750b0b58499e070)#define SMARTBOND\_SDADC\_P1\_14 4

[ 33](smartbond-adc_8h.md#a916ae13bfee8a78be4b9da3a91e66ad6)#define SMARTBOND\_SDADC\_P1\_20 5

[ 34](smartbond-adc_8h.md#a84a1c8191740dbd800ae3579ca03be21)#define SMARTBOND\_SDADC\_P1\_21 6

[ 35](smartbond-adc_8h.md#a94c18fb6d0f3af60e61dfa9a75d747fd)#define SMARTBOND\_SDADC\_P1\_22 7

36/\* Values for DT zephyr,input-positive only \*/

[ 37](smartbond-adc_8h.md#a083fd0f458f0441649f21909aba78d35)#define SMARTBOND\_SDADC\_VBAT 8

38

39#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_SMARTBOND\_ADC\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [smartbond-adc.h](smartbond-adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
