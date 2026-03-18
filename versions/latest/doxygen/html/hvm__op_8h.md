---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hvm__op_8h.html
original_path: doxygen/html/hvm__op_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hvm\_op.h File Reference

`#include "[../xen.h](xen_8h_source.md)"`

[Go to the source code of this file.](hvm__op_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [xen\_hvm\_param](structxen__hvm__param.md) |

| Macros | |
| --- | --- |
| #define | [HVMOP\_set\_param](#a9714e13adc338e97a811ac1beba162bd)   0 |
| #define | [HVMOP\_get\_param](#a96465a9f2e2437aa398c72bfc357d928)   1 |

| Typedefs | |
| --- | --- |
| typedef struct [xen\_hvm\_param](structxen__hvm__param.md) | [xen\_hvm\_param\_t](#af8a7ad2e0c2c0be2175f3fc396e41a0e) |

| Functions | |
| --- | --- |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a6d8f5f9367028a68a627d0bc78c47450) ([xen\_hvm\_param\_t](#af8a7ad2e0c2c0be2175f3fc396e41a0e)) |

## Macro Definition Documentation

## [◆ ](#a96465a9f2e2437aa398c72bfc357d928)HVMOP\_get\_param

| #define HVMOP\_get\_param   1 |
| --- |

## [◆ ](#a9714e13adc338e97a811ac1beba162bd)HVMOP\_set\_param

| #define HVMOP\_set\_param   0 |
| --- |

## Typedef Documentation

## [◆ ](#af8a7ad2e0c2c0be2175f3fc396e41a0e)xen\_hvm\_param\_t

| typedef struct [xen\_hvm\_param](structxen__hvm__param.md) [xen\_hvm\_param\_t](#af8a7ad2e0c2c0be2175f3fc396e41a0e) |
| --- |

## Function Documentation

## [◆ ](#a6d8f5f9367028a68a627d0bc78c47450)DEFINE\_XEN\_GUEST\_HANDLE()

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [xen\_hvm\_param\_t](#af8a7ad2e0c2c0be2175f3fc396e41a0e) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [hvm](dir_18c76ebef650877b932e646710239d41.md)
- [hvm\_op.h](hvm__op_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
