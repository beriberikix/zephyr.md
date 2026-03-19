---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dt-bindings_2battery_2battery_8h_source.html
original_path: doxygen/html/dt-bindings_2battery_2battery_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

battery.h

[Go to the documentation of this file.](dt-bindings_2battery_2battery_8h.md)

1/\*

2 \* Copyright 2024 Embeint Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \* The following open-circuit voltage curves have been extracted from the datasheets of the

7 \* listed battery parts. They will not be 100% correct for all batteries of the chemistry,

8 \* but should provide a good baseline. These curves will also be affected by ambient temperature

9 \* and discharge current.

10 \*

11 \* Each curve is 11 elements representing the OCV voltage in microvolts for each charge percentage

12 \* from 0% to 100% inclusive in 10% increments.

13 \*/

14#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_BATTERY\_BATTERY\_H\_

15#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_BATTERY\_BATTERY\_H\_

16

17/\* Panasonic KR-1800SCE \*/

[ 18](dt-bindings_2battery_2battery_8h.md#afd350d75e55db298ff1d932bde4ba160)#define BATTERY\_OCV\_CURVE\_NICKEL\_CADMIUM\_DEFAULT \

19 800000 1175000 1207000 1217000 1221000 1226000 1233000 1245000 1266000 1299000 1366000

20

21/\* Panasonic BK-1100FHU \*/

[ 22](dt-bindings_2battery_2battery_8h.md#a50639c3c3616d264e7ab7b4e1d4ab779)#define BATTERY\_OCV\_CURVE\_NICKEL\_METAL\_HYDRIDE\_DEFAULT \

23 1004000 1194000 1231000 1244000 1254000 1257000 1263000 1266000 1274000 1315000 1420000

24

25/\* Panasonic NCR18650BF \*/

[ 26](dt-bindings_2battery_2battery_8h.md#a9d4b97f71573f6eb691ec8ee015c981d)#define BATTERY\_OCV\_CURVE\_LITHIUM\_ION\_POLYMER\_DEFAULT \

27 2502000 3146000 3372000 3449000 3532000 3602000 3680000 3764000 3842000 3936000 4032000

28

29/\* Drypower IFR18650 E1600 \*/

[ 30](dt-bindings_2battery_2battery_8h.md#added3b21db841fe6e4b9473a6474b2c6)#define BATTERY\_OCV\_CURVE\_LITHIUM\_IRON\_PHOSPHATE\_DEFAULT \

31 2013000 3068000 3159000 3194000 3210000 3221000 3229000 3246000 3256000 3262000 3348000

32

33/\* FDK CR14250SE \*/

[ 34](dt-bindings_2battery_2battery_8h.md#a4aa3f2a3faa1f6fc8417ddebc743db3c)#define BATTERY\_OCV\_CURVE\_LITHIUM\_MANGANESE\_DEFAULT \

35 1906000 2444000 2689000 2812000 2882000 2927000 2949000 2955000 2962000 2960000 2985000

36

37#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_BATTERY\_BATTERY\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [battery](dir_0206a40ad47d2a4f5d05a6f925b14d32.md)
- [battery.h](dt-bindings_2battery_2battery_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
