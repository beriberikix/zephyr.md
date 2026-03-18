---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gcc_8h.html
original_path: doxygen/html/gcc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gcc.h File Reference

GCC toolchain abstraction.
[More...](#details)

[Go to the source code of this file.](gcc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TOOLCHAIN\_GCC\_VERSION](#acbf8a21b471b2086cbe276789c5061d5)   ((\_\_GNUC\_\_ \* 10000) + (\_\_GNUC\_MINOR\_\_ \* 100) + \_\_GNUC\_PATCHLEVEL\_\_) |
| #define | [TOOLCHAIN\_HAS\_ZLA](#a90e5fd6ed234d1494c7f156635c2e6e1)   1 |

## Detailed Description

GCC toolchain abstraction.

Macros to abstract compiler capabilities for GCC toolchain.

## Macro Definition Documentation

## [◆ ](#acbf8a21b471b2086cbe276789c5061d5)TOOLCHAIN\_GCC\_VERSION

| #define TOOLCHAIN\_GCC\_VERSION   ((\_\_GNUC\_\_ \* 10000) + (\_\_GNUC\_MINOR\_\_ \* 100) + \_\_GNUC\_PATCHLEVEL\_\_) |
| --- |

## [◆ ](#a90e5fd6ed234d1494c7f156635c2e6e1)TOOLCHAIN\_HAS\_ZLA

| #define TOOLCHAIN\_HAS\_ZLA   1 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [gcc.h](gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
