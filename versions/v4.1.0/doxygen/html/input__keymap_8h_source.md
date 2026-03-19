---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/input__keymap_8h_source.html
original_path: doxygen/html/input__keymap_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_keymap.h

[Go to the documentation of this file.](input__keymap_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INPUT\_INPUT\_KEYMAP\_H\_

8#define ZEPHYR\_INCLUDE\_INPUT\_INPUT\_KEYMAP\_H\_

9

[ 10](input__keymap_8h.md#afd3fd33c07ccb96c0c88c1a8d340fee3)#define MATRIX\_ROW(keymap\_entry) (((keymap\_entry) >> 24) & 0xff)

[ 11](input__keymap_8h.md#ad3b19ba368920538444393be76bf7214)#define MATRIX\_COL(keymap\_entry) (((keymap\_entry) >> 16) & 0xff)

12

13#endif /\* ZEPHYR\_INCLUDE\_INPUT\_INPUT\_KEYMAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_keymap.h](input__keymap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
