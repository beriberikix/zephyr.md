---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lis2ds12_8h_source.html
original_path: doxygen/html/lis2ds12_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2ds12.h

[Go to the documentation of this file.](lis2ds12_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DS12\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DS12\_H\_

8

9/\* power-modes \*/

[ 10](lis2ds12_8h.md#aebfdbefbdc2f17440413ba44911e8f3c)#define LIS2DS12\_DT\_POWER\_DOWN 0

[ 11](lis2ds12_8h.md#a93264cc6b09ef363a51a77d81e365083)#define LIS2DS12\_DT\_LOW\_POWER 1

[ 12](lis2ds12_8h.md#aa94a782ff303956dbbc99dbcf59819f8)#define LIS2DS12\_DT\_HIGH\_RESOLUTION 2

[ 13](lis2ds12_8h.md#ac66a29d7065bb2b94b471f704cd6ca58)#define LIS2DS12\_DT\_HIGH\_FREQUENCY 3

14

15/\* Data rate \*/

[ 16](lis2ds12_8h.md#a18ee240515cce324ee31ff7d8201a933)#define LIS2DS12\_DT\_ODR\_OFF 0

[ 17](lis2ds12_8h.md#ab222c78221c0a9d4ab1ce502c09103a5)#define LIS2DS12\_DT\_ODR\_1Hz\_LP 1 /\* available in LP mode only \*/

[ 18](lis2ds12_8h.md#a304edbdda283cb5274988054c969ca43)#define LIS2DS12\_DT\_ODR\_12Hz5 2 /\* available in LP and HR mode \*/

[ 19](lis2ds12_8h.md#ad37986618e794a9f7d59f521972ebc3b)#define LIS2DS12\_DT\_ODR\_25Hz 3 /\* available in LP and HR mode \*/

[ 20](lis2ds12_8h.md#a428a9dea9f3bbd9e60ad533cdae334f8)#define LIS2DS12\_DT\_ODR\_50Hz 4 /\* available in LP and HR mode \*/

[ 21](lis2ds12_8h.md#a07c6d9c6b044b749eed4db77d899d5ce)#define LIS2DS12\_DT\_ODR\_100Hz 5 /\* available in LP and HR mode \*/

[ 22](lis2ds12_8h.md#afc77b3b419461fa4744a83643ece77d4)#define LIS2DS12\_DT\_ODR\_200Hz 6 /\* available in LP and HR mode \*/

[ 23](lis2ds12_8h.md#a97749570c84f44060280b17b1b42b19b)#define LIS2DS12\_DT\_ODR\_400Hz 7 /\* available in LP and HR mode \*/

[ 24](lis2ds12_8h.md#ab7d0fb3bc0c15b714bda52d6e3435afc)#define LIS2DS12\_DT\_ODR\_800Hz 8 /\* available in LP and HR mode \*/

[ 25](lis2ds12_8h.md#a11f5aede52debdbc639791b28777504a)#define LIS2DS12\_DT\_ODR\_1600Hz 9 /\* available in HF mode only \*/

[ 26](lis2ds12_8h.md#a191a8680a6dff5ed459fbfd24aa04c2f)#define LIS2DS12\_DT\_ODR\_3200Hz\_HF 10 /\* available in HF mode only \*/

[ 27](lis2ds12_8h.md#a3e06d2a0811d0aa1544e77eb5ee6a4a9)#define LIS2DS12\_DT\_ODR\_6400Hz\_HF 11 /\* available in HF mode only \*/

28

29#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DS12\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2ds12.h](lis2ds12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
