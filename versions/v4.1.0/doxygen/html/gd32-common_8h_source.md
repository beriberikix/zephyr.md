---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gd32-common_8h_source.html
original_path: doxygen/html/gd32-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32-common.h

[Go to the documentation of this file.](gd32-common_8h.md)

1/\*

2 \* Copyright (c) 2022 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32\_RESET\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32\_RESET\_COMMON\_H\_

9

[ 20](gd32-common_8h.md#a518d3150ddd85f37ae028ee744378594)#define GD32\_RESET\_CONFIG(reg, bit) \

21 (((GD32\_ ## reg ## \_OFFSET) << 6U) | (bit))

22

23#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_GD32\_RESET\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [gd32-common.h](gd32-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
