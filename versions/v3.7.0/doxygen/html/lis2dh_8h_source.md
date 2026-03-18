---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/lis2dh_8h_source.html
original_path: doxygen/html/lis2dh_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2dh.h

[Go to the documentation of this file.](lis2dh_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DH\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DH\_H\_

8

9/\* GPIO interrupt configuration \*/

[ 10](lis2dh_8h.md#a673dad0efc816668086fc88983c13cbb)#define LIS2DH\_DT\_GPIO\_INT\_EDGE\_BOTH 0

[ 11](lis2dh_8h.md#afbf7948886682093cbc8034720bbabd5)#define LIS2DH\_DT\_GPIO\_INT\_EDGE\_RISING 1

[ 12](lis2dh_8h.md#a61b4f2c56b4bc253148340c52b1dca74)#define LIS2DH\_DT\_GPIO\_INT\_EDGE\_FALLING 2

[ 13](lis2dh_8h.md#a044d5fee79faaafcb2ed0363cce9329c)#define LIS2DH\_DT\_GPIO\_INT\_LEVEL\_HIGH 3

[ 14](lis2dh_8h.md#a06837f6473ace3107383e076903fde19)#define LIS2DH\_DT\_GPIO\_INT\_LEVEL\_LOW 4

15

16/\* Any Motion mode \*/

[ 17](lis2dh_8h.md#a97fdffadeb9f76118134e9c1bc1e1fb5)#define LIS2DH\_DT\_ANYM\_OR\_COMBINATION 0

[ 18](lis2dh_8h.md#a236b804ce12742583a07dd7e342467a3)#define LIS2DH\_DT\_ANYM\_6D\_MOVEMENT 1

[ 19](lis2dh_8h.md#addcd38964fcc1d465fa6d5b4a09ee47a)#define LIS2DH\_DT\_ANYM\_AND\_COMBINATION 2

[ 20](lis2dh_8h.md#a78a545b550b5ec39729cf283afb676ae)#define LIS2DH\_DT\_ANYM\_6D\_POSITION 3

21

22#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DH\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2dh.h](lis2dh_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
