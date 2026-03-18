---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/keymap_8h_source.html
original_path: doxygen/html/keymap_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

keymap.h

[Go to the documentation of this file.](keymap_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_KEYMAP\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_KEYMAP\_H\_

9

[ 10](keymap_8h.md#ab43c29335b0939bfa3e770c86d1622a0)#define MATRIX\_KEY(row, col, code) \

11 ((((row) & 0xff) << 24) | (((col) & 0xff) << 16) | ((code) & 0xffff))

12

13#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_KEYMAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [input](dir_ab844d62c7a22d129cc80e6c359d2c21.md)
- [keymap.h](keymap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
