---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch_2arm64_2thread__stack_8h.html
original_path: doxygen/html/arch_2arm64_2thread__stack_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_stack.h File Reference

`#include <[zephyr/arch/arm64/mm.h](arch_2arm64_2mm_8h_source.md)>`

[Go to the source code of this file.](arch_2arm64_2thread__stack_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   16 |
| #define | [ARCH\_THREAD\_STACK\_OBJ\_ALIGN](#ab6c1d96f5e018ed166ee401dc84b7ab7)(size) |
| #define | [ARCH\_THREAD\_STACK\_SIZE\_ADJUST](#ab76d60bd06e5c5a0f995c6b11bf97fd8)(size) |
| #define | [ARCH\_THREAD\_STACK\_RESERVED](#ace8831316d471ccfb06eeddb6d69d817) |
| #define | [ARCH\_KERNEL\_STACK\_RESERVED](group__arch-threads.md#ga75b8e6cce01f5a34e9f3d649e561c3af)   Z\_ARM64\_STACK\_GUARD\_SIZE |
|  | MPU guard size for kernel-only stacks. |
| #define | [ARCH\_KERNEL\_STACK\_OBJ\_ALIGN](#ac5a3684c543902ec50373d2c774c5bf6)   Z\_ARM64\_K\_STACK\_BASE\_ALIGN |

## Macro Definition Documentation

## [◆ ](#ac5a3684c543902ec50373d2c774c5bf6)ARCH\_KERNEL\_STACK\_OBJ\_ALIGN

| #define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN   Z\_ARM64\_K\_STACK\_BASE\_ALIGN |
| --- |

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   16 |
| --- |

## [◆ ](#ab6c1d96f5e018ed166ee401dc84b7ab7)ARCH\_THREAD\_STACK\_OBJ\_ALIGN

| #define ARCH\_THREAD\_STACK\_OBJ\_ALIGN | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

Z\_ARM64\_STACK\_BASE\_ALIGN

## [◆ ](#ace8831316d471ccfb06eeddb6d69d817)ARCH\_THREAD\_STACK\_RESERVED

| #define ARCH\_THREAD\_STACK\_RESERVED |
| --- |

**Value:**

CONFIG\_PRIVILEGED\_STACK\_SIZE + \

Z\_ARM64\_STACK\_GUARD\_SIZE

## [◆ ](#ab76d60bd06e5c5a0f995c6b11bf97fd8)ARCH\_THREAD\_STACK\_SIZE\_ADJUST

| #define ARCH\_THREAD\_STACK\_SIZE\_ADJUST | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)((size), Z\_ARM64\_STACK\_SIZE\_ALIGN)

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:322

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [thread\_stack.h](arch_2arm64_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
