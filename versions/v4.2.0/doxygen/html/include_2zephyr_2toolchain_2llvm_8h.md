---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2toolchain_2llvm_8h.html
original_path: doxygen/html/include_2zephyr_2toolchain_2llvm_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llvm.h File Reference

`#include <[zephyr/toolchain/gcc.h](include_2zephyr_2toolchain_2gcc_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2toolchain_2llvm_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TOOLCHAIN\_CLANG\_VERSION](#acdbda8f5e81a320dfdbc32bda1b33fad) |
| #define | [TOOLCHAIN\_HAS\_PRAGMA\_DIAG](#a763b60a74b3b8917b8a91614f1d443e4)   1 |
| #define | [TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY](#a056ed97bac0f04be423885dc21b9df00)   "-Wsizeof-array-decay" |
| #define | [TOOLCHAIN\_WARNING\_UNNEEDED\_INTERNAL\_DECLARATION](#a486884c167e8aa780419637b44ae18e6)   "-Wunneeded-internal-declaration" |
| #define | [TOOLCHAIN\_DISABLE\_CLANG\_WARNING](#ac4bfe24556e3dd2bfb093434a4e98517)(warning) |
| #define | [TOOLCHAIN\_ENABLE\_CLANG\_WARNING](#a35eaaf7a69eae890687c196e81304667)(warning) |

## Macro Definition Documentation

## [◆ ](#acdbda8f5e81a320dfdbc32bda1b33fad)TOOLCHAIN\_CLANG\_VERSION

| #define TOOLCHAIN\_CLANG\_VERSION |
| --- |

**Value:**

((\_\_clang\_major\_\_ \* 10000) + (\_\_clang\_minor\_\_ \* 100) + \

\_\_clang\_patchlevel\_\_)

## [◆ ](#ac4bfe24556e3dd2bfb093434a4e98517)TOOLCHAIN\_DISABLE\_CLANG\_WARNING

| #define TOOLCHAIN\_DISABLE\_CLANG\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_TOOLCHAIN\_DISABLE\_WARNING(clang, warning)

## [◆ ](#a35eaaf7a69eae890687c196e81304667)TOOLCHAIN\_ENABLE\_CLANG\_WARNING

| #define TOOLCHAIN\_ENABLE\_CLANG\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_TOOLCHAIN\_ENABLE\_WARNING(clang, warning)

## [◆ ](#a763b60a74b3b8917b8a91614f1d443e4)TOOLCHAIN\_HAS\_PRAGMA\_DIAG

| #define TOOLCHAIN\_HAS\_PRAGMA\_DIAG   1 |
| --- |

## [◆ ](#a056ed97bac0f04be423885dc21b9df00)TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY

| #define TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY   "-Wsizeof-array-decay" |
| --- |

## [◆ ](#a486884c167e8aa780419637b44ae18e6)TOOLCHAIN\_WARNING\_UNNEEDED\_INTERNAL\_DECLARATION

| #define TOOLCHAIN\_WARNING\_UNNEEDED\_INTERNAL\_DECLARATION   "-Wunneeded-internal-declaration" |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [llvm.h](include_2zephyr_2toolchain_2llvm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
