---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mchp__xec__pcr_8h_source.html
original_path: doxygen/html/mchp__xec__pcr_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp\_xec\_pcr.h

[Go to the documentation of this file.](mchp__xec__pcr_8h.md)

1/\*

2 \* Copyright (c) 2021 Microchip Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCHP\_XEC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCHP\_XEC\_H\_

9

10/\* PLL 32KHz clock source VTR rail ON. \*/

[ 11](mchp__xec__pcr_8h.md#a648809d3dcf2e2aa84641d1dcaaa333f)#define MCHP\_XEC\_PLL\_CLK32K\_SRC\_SIL\_OSC 0U

[ 12](mchp__xec__pcr_8h.md#a701353ae9e33d97be76c9ee0273c87fa)#define MCHP\_XEC\_PLL\_CLK32K\_SRC\_XTAL 1U

[ 13](mchp__xec__pcr_8h.md#aa4c445cdf962557f71765cad287cb215)#define MCHP\_XEC\_PLL\_CLK32K\_SRC\_PIN 2U

14

15/\* Peripheral 32KHz clock source for VTR rail ON and off(VBAT operation) \*/

[ 16](mchp__xec__pcr_8h.md#ac71939dc0ab9d064ea43fd8fd898257c)#define MCHP\_XEC\_PERIPH\_CLK32K\_SRC\_SO\_SO 0U

[ 17](mchp__xec__pcr_8h.md#a6bc8a1b96df3f9077e6b00da8ea8af22)#define MCHP\_XEC\_PERIPH\_CLK32K\_SRC\_XTAL\_XTAL 1U

[ 18](mchp__xec__pcr_8h.md#a569039424af967d8445fa62e28f20229)#define MCHP\_XEC\_PERIPH\_CLK32K\_SRC\_PIN\_SO 2U

[ 19](mchp__xec__pcr_8h.md#abdee7a88e189e89bc4c721e2e5222d80)#define MCHP\_XEC\_PERIPH\_CLK32K\_SRC\_PIN\_XTAL 3U

20

21/\* clocks supported by the driver \*/

[ 22](mchp__xec__pcr_8h.md#abc3c97c553f70c6925bb07c546ad1694)#define MCHP\_XEC\_PCR\_CLK\_CORE 0

[ 23](mchp__xec__pcr_8h.md#a713a1fd7de2fe9c20e69da59e16c5f28)#define MCHP\_XEC\_PCR\_CLK\_CPU 1

[ 24](mchp__xec__pcr_8h.md#a645c476e2d0506aed4842d077a538a16)#define MCHP\_XEC\_PCR\_CLK\_BUS 2

[ 25](mchp__xec__pcr_8h.md#ac772778bad2aaa564299f884150173f7)#define MCHP\_XEC\_PCR\_CLK\_PERIPH 3

[ 26](mchp__xec__pcr_8h.md#ad313fc38e1fb56d5a9251a771e8a1119)#define MCHP\_XEC\_PCR\_CLK\_PERIPH\_FAST 4

[ 27](mchp__xec__pcr_8h.md#a504da1d12b02d9cbfe5de72adce02da1)#define MCHP\_XEC\_PCR\_CLK\_PERIPH\_SLOW 5

28

29#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCHP\_XEC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [mchp\_xec\_pcr.h](mchp__xec__pcr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
