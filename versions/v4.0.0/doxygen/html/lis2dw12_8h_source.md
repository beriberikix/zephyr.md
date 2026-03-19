---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lis2dw12_8h_source.html
original_path: doxygen/html/lis2dw12_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2dw12.h

[Go to the documentation of this file.](lis2dw12_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DW12\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DW12\_H\_

8

9/\* power-modes \*/

[ 10](lis2dw12_8h.md#a0c03f55d1b6ebbf1d48e0c34d9122a74)#define LIS2DW12\_DT\_LP\_M1 0

[ 11](lis2dw12_8h.md#aeb6d34d3c11a1f3e7dc2cfe5f7405aae)#define LIS2DW12\_DT\_LP\_M2 1

[ 12](lis2dw12_8h.md#ab9ab746af6c8dfa384671ee313c7eea4)#define LIS2DW12\_DT\_LP\_M3 2

[ 13](lis2dw12_8h.md#ada20bc2633adb3ae955c2f709d727154)#define LIS2DW12\_DT\_LP\_M4 3

[ 14](lis2dw12_8h.md#a0307502b4dee186f1945636c713eee4d)#define LIS2DW12\_DT\_HP\_MODE 4

15

16/\* Filter bandwidth \*/

[ 17](lis2dw12_8h.md#a88efe563d0f4d704773886d7670bea31)#define LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_2 0

[ 18](lis2dw12_8h.md#a4433ccc00389f58d30b9998b11915848)#define LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_4 1

[ 19](lis2dw12_8h.md#aad4197948abbd4587f6c9810f34e0c49)#define LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_10 2

[ 20](lis2dw12_8h.md#a9972d8b7618f39c9ddff273ecd80616a)#define LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_20 3

21

22/\* Tap mode \*/

[ 23](lis2dw12_8h.md#a71fc2ff7108bd85a86fd82c0ff002c18)#define LIS2DW12\_DT\_SINGLE\_TAP 0

[ 24](lis2dw12_8h.md#a4011203a9d243f9650cecab3d9ecf34d)#define LIS2DW12\_DT\_SINGLE\_DOUBLE\_TAP 1

25

26/\* Free-Fall threshold \*/

[ 27](lis2dw12_8h.md#ac0420687b2a5ef0b886534b183d9b2f7)#define LIS2DW12\_DT\_FF\_THRESHOLD\_156\_mg 0

[ 28](lis2dw12_8h.md#a6afc0cf0328630c3bcdaf4cc579d8988)#define LIS2DW12\_DT\_FF\_THRESHOLD\_219\_mg 1

[ 29](lis2dw12_8h.md#a25b0e004ef448952083e417b0c77f97d)#define LIS2DW12\_DT\_FF\_THRESHOLD\_250\_mg 2

[ 30](lis2dw12_8h.md#a5ab3d56ad2ab84179316f3706780d716)#define LIS2DW12\_DT\_FF\_THRESHOLD\_312\_mg 3

[ 31](lis2dw12_8h.md#a429524e40340eb36610b7c0b4a449298)#define LIS2DW12\_DT\_FF\_THRESHOLD\_344\_mg 4

[ 32](lis2dw12_8h.md#a9a7a1520051a5b6107e6e0adbfb1d837)#define LIS2DW12\_DT\_FF\_THRESHOLD\_406\_mg 5

[ 33](lis2dw12_8h.md#ac336d6955333fc41ce21b9d68dfde4e5)#define LIS2DW12\_DT\_FF\_THRESHOLD\_469\_mg 6

[ 34](lis2dw12_8h.md#a7de449940954836ff3c48ef192662760)#define LIS2DW12\_DT\_FF\_THRESHOLD\_500\_mg 7

35

36/\* wakeup duration \*/

[ 37](lis2dw12_8h.md#a1bcffaa1b8439f626164b736be17f9db)#define LIS2DW12\_DT\_WAKEUP\_1\_ODR 0

[ 38](lis2dw12_8h.md#a53457e3a0d24bf3599ff779f3a559fb4)#define LIS2DW12\_DT\_WAKEUP\_2\_ODR 1

[ 39](lis2dw12_8h.md#a580dd3e03a377fce36db7916c254b52a)#define LIS2DW12\_DT\_WAKEUP\_3\_ODR 2

[ 40](lis2dw12_8h.md#aae58921652443e8f7757b38ade589c49)#define LIS2DW12\_DT\_WAKEUP\_4\_ODR 3

41

42/\* sleep duration \*/

[ 43](lis2dw12_8h.md#aa9df8cef65e33e117a8de9eb2df745c3)#define LIS2DW12\_DT\_SLEEP\_0\_ODR 0

[ 44](lis2dw12_8h.md#af43f42617789c1482e1ddf1d9abd7c3d)#define LIS2DW12\_DT\_SLEEP\_1\_ODR 1

[ 45](lis2dw12_8h.md#a6c76600bf9baff0483d5865ba98aa75e)#define LIS2DW12\_DT\_SLEEP\_2\_ODR 2

[ 46](lis2dw12_8h.md#af294baab225caba1e4931abfee9660b8)#define LIS2DW12\_DT\_SLEEP\_3\_ODR 3

[ 47](lis2dw12_8h.md#ac45de707e5c1ee485b5cdd95ce3332af)#define LIS2DW12\_DT\_SLEEP\_4\_ODR 4

[ 48](lis2dw12_8h.md#a904ec47239d01ac05218bee5fa2f4235)#define LIS2DW12\_DT\_SLEEP\_5\_ODR 5

[ 49](lis2dw12_8h.md#a552a71243df2cfe6dcc6f9ca5a4208c9)#define LIS2DW12\_DT\_SLEEP\_6\_ODR 6

[ 50](lis2dw12_8h.md#a72ced204873bfce192b6bcfc9d823ffc)#define LIS2DW12\_DT\_SLEEP\_7\_ODR 7

[ 51](lis2dw12_8h.md#a9078b4d1fa77dd53871ddbc7715b3f0c)#define LIS2DW12\_DT\_SLEEP\_8\_ODR 8

[ 52](lis2dw12_8h.md#a979e47f3dda9c72b92d87bb3fc5b3e4f)#define LIS2DW12\_DT\_SLEEP\_9\_ODR 9

[ 53](lis2dw12_8h.md#a15982beb9fce8268a056fb2f088f6724)#define LIS2DW12\_DT\_SLEEP\_10\_ODR 10

[ 54](lis2dw12_8h.md#ad3546f54d5eee5d7d9cb9318a6104a9c)#define LIS2DW12\_DT\_SLEEP\_11\_ODR 11

[ 55](lis2dw12_8h.md#a97614b907ca69fd13f0e8a9b61e15904)#define LIS2DW12\_DT\_SLEEP\_12\_ODR 12

[ 56](lis2dw12_8h.md#abff45bcd009134ee4da471e9e915584a)#define LIS2DW12\_DT\_SLEEP\_13\_ODR 13

[ 57](lis2dw12_8h.md#a8ba46d92426bf168d6b9da5acee6668f)#define LIS2DW12\_DT\_SLEEP\_14\_ODR 14

[ 58](lis2dw12_8h.md#a39ddac85ed26346de4272157ce2533a8)#define LIS2DW12\_DT\_SLEEP\_15\_ODR 15

59

60#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DW12\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2dw12.h](lis2dw12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
