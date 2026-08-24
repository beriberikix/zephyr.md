---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/microchip__sam__pmc_8h_source.html
original_path: doxygen/html/microchip__sam__pmc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

microchip\_sam\_pmc.h

[Go to the documentation of this file.](microchip__sam__pmc_8h.md)

1/\*

2 \* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MICROCHIP\_SAM\_PMC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MICROCHIP\_SAM\_PMC\_H\_

9

[ 10](microchip__sam__pmc_8h.md#a2b1fc195c22e06289bfe1955086d42dd)#define PMC\_TYPE\_CORE 0

[ 11](microchip__sam__pmc_8h.md#a5745534115e0096059c693406055573b)#define PMC\_TYPE\_SYSTEM 1

[ 12](microchip__sam__pmc_8h.md#a60e3c44dd11ea566f718972995374019)#define PMC\_TYPE\_PERIPHERAL 2

[ 13](microchip__sam__pmc_8h.md#ab998f9758b4c3e603ca20bfd262f3327)#define PMC\_TYPE\_GCK 3

[ 14](microchip__sam__pmc_8h.md#a7fc62d1954529184d102cb7585973fb5)#define PMC\_TYPE\_PROGRAMMABLE 4

15

[ 16](microchip__sam__pmc_8h.md#a854154863c97c71801ff4684a407e237)#define PMC\_SLOW 0

[ 17](microchip__sam__pmc_8h.md#a2d6b8cadcedb6522e88264b09da73d7d)#define PMC\_MCK 1

[ 18](microchip__sam__pmc_8h.md#a5a54df8ddd142b8e6ed67b72d7bab401)#define PMC\_UTMI 2

[ 19](microchip__sam__pmc_8h.md#a072e63108608597768994a00b21d955d)#define PMC\_MAIN 3

20

21/\* SAMA7G5 \*/

[ 22](microchip__sam__pmc_8h.md#a1f28358ab0151521b3121ff4d57ca700)#define PMC\_CPUPLL (PMC\_MAIN + 1)

[ 23](microchip__sam__pmc_8h.md#a996cc1d45786ee499ccc23355a05db37)#define PMC\_SYSPLL (PMC\_MAIN + 2)

[ 24](microchip__sam__pmc_8h.md#ab8a01a73ca6952f39be1ed7a3791feb3)#define PMC\_DDRPLL (PMC\_MAIN + 3)

[ 25](microchip__sam__pmc_8h.md#a441d7b97d246e52e75bf348ac3b90c76)#define PMC\_IMGPLL (PMC\_MAIN + 4)

[ 26](microchip__sam__pmc_8h.md#aae1ca2d39f81fa9fc9094619ce3b19c4)#define PMC\_BAUDPLL (PMC\_MAIN + 5)

[ 27](microchip__sam__pmc_8h.md#af716bb9061d8d6a5a96ade2c0102f4c0)#define PMC\_AUDIOPMCPLL (PMC\_MAIN + 6)

[ 28](microchip__sam__pmc_8h.md#a2374e2a9b2baf97196cb9900ab41f2b1)#define PMC\_AUDIOIOPLL (PMC\_MAIN + 7)

[ 29](microchip__sam__pmc_8h.md#a2707b5189d0c0a383e8765aa4dc0c702)#define PMC\_ETHPLL (PMC\_MAIN + 8)

[ 30](microchip__sam__pmc_8h.md#a79ea6d33c03bc659e505516f10dd4909)#define PMC\_CPU (PMC\_MAIN + 9)

[ 31](microchip__sam__pmc_8h.md#a373a027bd6c4c22ba1bb333109c4b4b5)#define PMC\_MCK1 (PMC\_MAIN + 10)

[ 32](microchip__sam__pmc_8h.md#acf4ff24d07135ac8ba9095f4b0e8202f)#define UTMI1 0

[ 33](microchip__sam__pmc_8h.md#a536bbd6e8cf19611a64b62a6173bebae)#define UTMI2 1

[ 34](microchip__sam__pmc_8h.md#ab950647ecce7b6ed9a94770434a9504c)#define UTMI3 2

35

36#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MICROCHIP\_SAM\_PMC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [microchip\_sam\_pmc.h](microchip__sam__pmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
