---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2xtensa_2thread__stack_8h.html
original_path: doxygen/html/arch_2xtensa_2thread__stack_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_stack.h File Reference

`#include <xtensa/config/core-isa.h>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](arch_2xtensa_2thread__stack_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   16 |
| #define | [XTENSA\_STACK\_BASE\_ALIGN](#abfd32aa6dffa0ba9a14e925eac1b57ba)   CONFIG\_MMU\_PAGE\_SIZE |
| #define | [XTENSA\_STACK\_SIZE\_ALIGN](#afe73e9fabd5171efb0e480ad1035c21c)   CONFIG\_MMU\_PAGE\_SIZE |
| #define | [ARCH\_THREAD\_STACK\_OBJ\_ALIGN](#ab6c1d96f5e018ed166ee401dc84b7ab7)(size) |
| #define | [ARCH\_THREAD\_STACK\_SIZE\_ADJUST](#ab76d60bd06e5c5a0f995c6b11bf97fd8)(size) |
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

| #define ARCH\_STACK\_PTR\_ALIGN   16 |
| --- |

## [◆ ](#ab6c1d96f5e018ed166ee401dc84b7ab7)ARCH\_THREAD\_STACK\_OBJ\_ALIGN

| #define ARCH\_THREAD\_STACK\_OBJ\_ALIGN | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[XTENSA\_STACK\_BASE\_ALIGN](#abfd32aa6dffa0ba9a14e925eac1b57ba)

[XTENSA\_STACK\_BASE\_ALIGN](#abfd32aa6dffa0ba9a14e925eac1b57ba)

#define XTENSA\_STACK\_BASE\_ALIGN

**Definition** thread\_stack.h:21

## [◆ ](#ab76d60bd06e5c5a0f995c6b11bf97fd8)ARCH\_THREAD\_STACK\_SIZE\_ADJUST

| #define ARCH\_THREAD\_STACK\_SIZE\_ADJUST | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)((size), [XTENSA\_STACK\_SIZE\_ALIGN](#afe73e9fabd5171efb0e480ad1035c21c))

[XTENSA\_STACK\_SIZE\_ALIGN](#afe73e9fabd5171efb0e480ad1035c21c)

#define XTENSA\_STACK\_SIZE\_ALIGN

**Definition** thread\_stack.h:22

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:288

## [◆ ](#abfd32aa6dffa0ba9a14e925eac1b57ba)XTENSA\_STACK\_BASE\_ALIGN

| #define XTENSA\_STACK\_BASE\_ALIGN   CONFIG\_MMU\_PAGE\_SIZE |
| --- |

## [◆ ](#afe73e9fabd5171efb0e480ad1035c21c)XTENSA\_STACK\_SIZE\_ALIGN

| #define XTENSA\_STACK\_SIZE\_ALIGN   CONFIG\_MMU\_PAGE\_SIZE |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [thread\_stack.h](arch_2xtensa_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
