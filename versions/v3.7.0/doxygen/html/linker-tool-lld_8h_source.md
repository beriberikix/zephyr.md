---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/linker-tool-lld_8h_source.html
original_path: doxygen/html/linker-tool-lld_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-tool-lld.h

[Go to the documentation of this file.](linker-tool-lld_8h.md)

1/\*

2 \* Copyright (c) 2023, Google, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_LLD\_H\_

16#define ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_LLD\_H\_

17

18#include <[zephyr/linker/linker-tool-gcc.h](linker-tool-gcc_8h.md)>

19

38#undef SECTION\_PROLOGUE

[ 39](linker-tool-lld_8h.md#a784c696b95848c5f070e257a50fbe23a)#define SECTION\_PROLOGUE(name, options, align) \

40 name options : align

41

57#undef SECTION\_DATA\_PROLOGUE

[ 58](linker-tool-lld_8h.md#a0d8981d3817b2563846735c90d50240c)#define SECTION\_DATA\_PROLOGUE(name, options, align) \

59 SECTION\_PROLOGUE(name, options, align)

60

61#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_LLD\_H\_ \*/

[linker-tool-gcc.h](linker-tool-gcc_8h.md)

GCC toolchain linker defs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-tool-lld.h](linker-tool-lld_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
