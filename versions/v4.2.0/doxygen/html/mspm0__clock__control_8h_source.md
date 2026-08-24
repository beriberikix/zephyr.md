---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mspm0__clock__control_8h_source.html
original_path: doxygen/html/mspm0__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspm0\_clock\_control.h

[Go to the documentation of this file.](mspm0__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2025 Texas Instruments Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_MSPM0\_CLOCK\_CONTROL

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_MSPM0\_CLOCK\_CONTROL

9

10#include <[zephyr/dt-bindings/clock/mspm0\_clock.h](mspm0__clock_8h.md)>

11

[ 12](structmspm0__sys__clock.md)struct [mspm0\_sys\_clock](structmspm0__sys__clock.md) {

[ 13](structmspm0__sys__clock.md#ac48292bef828c08f7da17a376e491c79) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk](structmspm0__sys__clock.md#ac48292bef828c08f7da17a376e491c79);

14};

15

[ 16](mspm0__clock__control_8h.md#a438e7623f4a0dde8f48ce81cc9ecb4d5)#define MSPM0\_CLOCK\_SUBSYS\_FN(index) {.clk = DT\_INST\_CLOCKS\_CELL(index, clk)}

17

18#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_MSPM0\_CLOCK\_CONTROL \*/

[mspm0\_clock.h](mspm0__clock_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[mspm0\_sys\_clock](structmspm0__sys__clock.md)

**Definition** mspm0\_clock\_control.h:12

[mspm0\_sys\_clock::clk](structmspm0__sys__clock.md#ac48292bef828c08f7da17a376e491c79)

uint32\_t clk

**Definition** mspm0\_clock\_control.h:13

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [mspm0\_clock\_control.h](mspm0__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
