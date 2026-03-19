---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/adi__max32__clock_8h_source.html
original_path: doxygen/html/adi__max32__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adi\_max32\_clock.h

[Go to the documentation of this file.](adi__max32__clock_8h.md)

1/\*

2 \* Copyright (c) 2023-2024 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ADI\_MAX32\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ADI\_MAX32\_CLOCK\_H\_

9

[ 11](adi__max32__clock_8h.md#afe3578f3122163009070220def865b17)#define ADI\_MAX32\_CLOCK\_BUS0 0

[ 12](adi__max32__clock_8h.md#a5b6d4b5a184d286e2353adc8fec22d94)#define ADI\_MAX32\_CLOCK\_BUS1 1

[ 13](adi__max32__clock_8h.md#ad6f25e814a9f2d91c4050cfd4db96975)#define ADI\_MAX32\_CLOCK\_BUS2 2

14

[ 16](adi__max32__clock_8h.md#ad28575fff49c4cb3c4b8c4180cd387de)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_PCLK 0 /\* Peripheral clock \*/

[ 17](adi__max32__clock_8h.md#a6bc3da20a61d735c15894c7cb7f6fb88)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_EXTCLK 1 /\* External clock \*/

[ 18](adi__max32__clock_8h.md#a0ec9e4fb6e4522325b7c26b1aa6ff4ae)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO 2 /\* Internal Baud Rate Oscillator\*/

[ 19](adi__max32__clock_8h.md#af9ad74e5aff66314ef7ea4bcbd58a12f)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_ERFO 3 /\* External RF Oscillator \*/

[ 20](adi__max32__clock_8h.md#ae22725273956cf339a7aa1ab99ec9d64)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_ERTCO 4 /\* External RTC Oscillator \*/

[ 21](adi__max32__clock_8h.md#ad6039fb9117f11753b062ce70ab6086c)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_INRO 5 /\* Internal Nano Ring Oscillator \*/

[ 22](adi__max32__clock_8h.md#a7cc83f5e0a532b4f59909167562042f0)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_ISO 6 /\* Internal Secondary Oscillator \*/

[ 23](adi__max32__clock_8h.md#a79b4ec22a2ad744b20511fd72f00b88b)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO\_DIV8 7 /\* IBRO/8 \*/

[ 24](adi__max32__clock_8h.md#abf12d2334614747738816c67aa32b4e6)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_IPLL 8 /\* Internal Phase Lock Loop Oscillator \*/

[ 25](adi__max32__clock_8h.md#ada66413c52e2d3c1d166569fb9d52a84)#define ADI\_MAX32\_PRPH\_CLK\_SRC\_EBO 9 /\* External Base Oscillator \*/

26

27#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ADI\_MAX32\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [adi\_max32\_clock.h](adi__max32__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
