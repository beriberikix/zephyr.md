---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bq274xx_8h_source.html
original_path: doxygen/html/bq274xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bq274xx.h

[Go to the documentation of this file.](bq274xx_8h.md)

1/\*

2 \* Copyright (c) 2023 The Zephyr Contributors.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \* Relevant documents:

7 \* - BQ27421

8 \* Datasheet: https://www.ti.com/lit/gpn/bq27421-g1

9 \* Technical reference manual: https://www.ti.com/lit/pdf/sluuac5

10 \* - BQ27427

11 \* Datasheet: https://www.ti.com/lit/gpn/bq27427

12 \* Technical reference manual: https://www.ti.com/lit/pdf/sluucd5

13 \*/

14#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_BQ274XX\_H\_

15#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_BQ274XX\_H\_

16

17/\* Chemistry IDs for BQ27427 \*/

[ 18](bq274xx_8h.md#afd885c85ac533a7640f93e97fec8ccb9)#define BQ27427\_CHEM\_ID\_A 0x3230

[ 19](bq274xx_8h.md#aafd294ad5ecf988c816ed258e61fa781)#define BQ27427\_CHEM\_ID\_B 0x1202

[ 20](bq274xx_8h.md#ac932a2d227876901d5a001a46b0aba07)#define BQ27427\_CHEM\_ID\_C 0x3142

21

22/\* Chemistry IDs for BQ27421 variants \*/

[ 23](bq274xx_8h.md#a8f812e864a406e7ac743bedeecc9ddf3)#define BQ27421\_G1A\_CHEM\_ID 0x0128

[ 24](bq274xx_8h.md#af337b60f20d3c986c353293596d7c2f6)#define BQ27421\_G1B\_CHEM\_ID 0x0312

[ 25](bq274xx_8h.md#a3f58b290a4556f6a74da8b4759262fc0)#define BQ27421\_G1D\_CHEM\_ID 0x3142

26

27#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_BQ274XX\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [bq274xx.h](bq274xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
