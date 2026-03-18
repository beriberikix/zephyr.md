---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cbprintf__internal_8h.html
original_path: doxygen/html/cbprintf__internal_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cbprintf\_internal.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <stdarg.h>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <zephyr/arch/cpu.h>`  
`#include <[zephyr/sys/cbprintf_cxx.h](cbprintf__cxx_8h_source.md)>`

[Go to the source code of this file.](cbprintf__internal_8h_source.md)

| Macros | |
| --- | --- |
| #define | [VA\_STACK\_MIN\_ALIGN](#a0ec36f3c06add6c091c8f552ef3736e1)   1 |
| #define | [VA\_STACK\_ALIGN](#acfc4e20989d254f61e85b8e2e5e6701a)(type) |

## Macro Definition Documentation

## [◆ ](#acfc4e20989d254f61e85b8e2e5e6701a)VA\_STACK\_ALIGN

| #define VA\_STACK\_ALIGN | ( |  | *type* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)([VA\_STACK\_MIN\_ALIGN](#a0ec36f3c06add6c091c8f552ef3736e1), \_\_alignof\_\_(type))

[VA\_STACK\_MIN\_ALIGN](#a0ec36f3c06add6c091c8f552ef3736e1)

#define VA\_STACK\_MIN\_ALIGN

**Definition** cbprintf\_internal.h:48

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

#define MAX(a, b)

Obtain the maximum of two values.

**Definition** util.h:358

## [◆ ](#a0ec36f3c06add6c091c8f552ef3736e1)VA\_STACK\_MIN\_ALIGN

| #define VA\_STACK\_MIN\_ALIGN   1 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [cbprintf\_internal.h](cbprintf__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
