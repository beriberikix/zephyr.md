---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/linker-tool_8h_source.html
original_path: doxygen/html/linker-tool_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-tool.h

[Go to the documentation of this file.](linker-tool_8h.md)

1/\*

2 \* Copyright (c) 2013-2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_H\_

16#define ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_H\_

17

18#if defined(\_LINKER)

19#if defined(\_\_GCC\_LINKER\_CMD\_\_)

20#include <[zephyr/linker/linker-tool-gcc.h](linker-tool-gcc_8h.md)>

21#elif defined(\_\_MWDT\_LINKER\_CMD\_\_)

22#include <[zephyr/linker/linker-tool-mwdt.h](linker-tool-mwdt_8h.md)>

23#elif defined(\_\_LLD\_LINKER\_CMD\_\_)

24#include <[zephyr/linker/linker-tool-lld.h](linker-tool-lld_8h.md)>

25#else

26#error "Unknown toolchain"

27#endif

28#endif

29

30#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_TOOL\_H\_ \*/

[linker-tool-gcc.h](linker-tool-gcc_8h.md)

GCC toolchain linker defs.

[linker-tool-lld.h](linker-tool-lld_8h.md)

LLVM LLD linker defs.

[linker-tool-mwdt.h](linker-tool-mwdt_8h.md)

Metware toolchain linker defs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-tool.h](linker-tool_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
