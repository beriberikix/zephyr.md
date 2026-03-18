---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32-common_8h_source.html
original_path: doxygen/html/stm32-common_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-common.h

[Go to the documentation of this file.](stm32-common_8h.md)

1/\*

2 \* Copyright (c) 2022 Google Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32\_RESET\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32\_RESET\_COMMON\_H\_

9

[ 20](stm32-common_8h.md#a6a12a4b8c042157a88ddf7da442c137c)#define STM32\_RESET(bus, bit) (((STM32\_RESET\_BUS\_##bus) << 5U) | (bit))

21

22#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32\_RESET\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32-common.h](stm32-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
