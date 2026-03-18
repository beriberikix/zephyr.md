---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ti-vim_8h_source.html
original_path: doxygen/html/ti-vim_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti-vim.h

[Go to the documentation of this file.](ti-vim_8h.md)

1/\* Copyright (C) 2023 BeagleBoard.org Foundation

2 \* Copyright (C) 2023 S Prashanth

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_DT\_BINDING\_TI\_VIM\_H

8#define \_\_DT\_BINDING\_TI\_VIM\_H

9

10#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

11

[ 12](ti-vim_8h.md#a296e915831223a614a6ea87dbe7735e7)#define IRQ\_TYPE\_LEVEL BIT(1)

[ 13](ti-vim_8h.md#aff68b0efbc719bc28f0d56c9ba8607bc)#define IRQ\_TYPE\_EDGE BIT(2)

14

[ 15](ti-vim_8h.md#a2dbeaa0c017cdff0982b381cc96f0a6c)#define IRQ\_DEFAULT\_PRIORITY 0xf

16

17#endif /\* \_\_DT\_BINDING\_TI\_VIM\_H \*/

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [ti-vim.h](ti-vim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
