---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2x86_2thread__stack_8h.html
original_path: doxygen/html/arch_2x86_2thread__stack_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_stack.h File Reference

`#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h_source.md)>`

[Go to the source code of this file.](arch_2x86_2thread__stack_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   4UL |
| #define | [ARCH\_THREAD\_STACK\_OBJ\_ALIGN](#ab6c1d96f5e018ed166ee401dc84b7ab7)(size) |
| #define | [ARCH\_THREAD\_STACK\_SIZE\_ADJUST](#ab76d60bd06e5c5a0f995c6b11bf97fd8)(size) |
| #define | [ARCH\_THREAD\_STACK\_RESERVED](#ace8831316d471ccfb06eeddb6d69d817)   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct z\_x86\_thread\_stack\_header) |
| #define | [ARCH\_KERNEL\_STACK\_RESERVED](#a75b8e6cce01f5a34e9f3d649e561c3af)   0 |
| #define | [ARCH\_KERNEL\_STACK\_OBJ\_ALIGN](#ac5a3684c543902ec50373d2c774c5bf6)   [ARCH\_STACK\_PTR\_ALIGN](arch_2arm64_2thread__stack_8h.md#af0f8ad93611d93cd0626914837e761d3) |

## Macro Definition Documentation

## [◆ ](#ac5a3684c543902ec50373d2c774c5bf6)ARCH\_KERNEL\_STACK\_OBJ\_ALIGN

| #define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN   [ARCH\_STACK\_PTR\_ALIGN](arch_2arm64_2thread__stack_8h.md#af0f8ad93611d93cd0626914837e761d3) |
| --- |

## [◆ ](#a75b8e6cce01f5a34e9f3d649e561c3af)ARCH\_KERNEL\_STACK\_RESERVED

| #define ARCH\_KERNEL\_STACK\_RESERVED   0 |
| --- |

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   4UL |
| --- |

## [◆ ](#ab6c1d96f5e018ed166ee401dc84b7ab7)ARCH\_THREAD\_STACK\_OBJ\_ALIGN

| #define ARCH\_THREAD\_STACK\_OBJ\_ALIGN | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

Z\_X86\_STACK\_BASE\_ALIGN

## [◆ ](#ace8831316d471ccfb06eeddb6d69d817)ARCH\_THREAD\_STACK\_RESERVED

| #define ARCH\_THREAD\_STACK\_RESERVED   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct z\_x86\_thread\_stack\_header) |
| --- |

## [◆ ](#ab76d60bd06e5c5a0f995c6b11bf97fd8)ARCH\_THREAD\_STACK\_SIZE\_ADJUST

| #define ARCH\_THREAD\_STACK\_SIZE\_ADJUST | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)((size), Z\_X86\_STACK\_SIZE\_ALIGN)

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:322

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [thread\_stack.h](arch_2x86_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
