---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/seagate__legend__b1414_8h_source.html
original_path: doxygen/html/seagate__legend__b1414_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

seagate\_legend\_b1414.h

[Go to the documentation of this file.](seagate__legend__b1414_8h.md)

1/\*

2 \* Copyright (c) 2021, Seagate Technology LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_SAMPLES\_DRIVERS\_LED\_B1414\_H\_

8#define ZEPHYR\_SAMPLES\_DRIVERS\_LED\_B1414\_H\_

9

10/\*

11 \* At 6 MHz: 1 bit in 166.666 ns

12 \* 1200 ns -> 7.2 bits

13 \* 300 ns -> 1.8 bits

14 \* 900 ns -> 5.4 bits

15 \*/

[ 16](seagate__legend__b1414_8h.md#a6254a4e77c7f2f980d5f49538893d0ab)#define SPI\_FREQ 6000000

[ 17](seagate__legend__b1414_8h.md#ada4655bb5f9b877b2cf6e48206abf5d1)#define ZERO\_FRAME 0x60

[ 18](seagate__legend__b1414_8h.md#a2359d4eb2386a3eef432e601e7726f90)#define ONE\_FRAME 0x7C

19

20#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [led](dir_43259d1800ff16a5cdd32a96a4c7d34d.md)
- [seagate\_legend\_b1414.h](seagate__legend__b1414_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
