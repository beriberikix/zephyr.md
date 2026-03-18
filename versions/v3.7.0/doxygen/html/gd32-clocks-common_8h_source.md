---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gd32-clocks-common_8h_source.html
original_path: doxygen/html/gd32-clocks-common_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32-clocks-common.h

[Go to the documentation of this file.](gd32-clocks-common_8h.md)

1/\*

2 \* Copyright (c) 2022 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32\_COMMON\_H\_

9

[ 20](gd32-clocks-common_8h.md#a8b1e411caae3c88322d85671558b2bbc)#define GD32\_CLOCK\_CONFIG(reg, bit) \

21 (((GD32\_ ## reg ## \_OFFSET) << 6U) | (bit))

22

23#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_GD32\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [gd32-clocks-common.h](gd32-clocks-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
