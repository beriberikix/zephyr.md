---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/memory-attr-xtensa_8h.html
original_path: doxygen/html/memory-attr-xtensa_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr-xtensa.h File Reference

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h_source.md)>`

[Go to the source code of this file.](memory-attr-xtensa_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_MEM\_XTENSA\_MASK](#a90663eb795734c0f1f8f7cdc50584d87)   [DT\_MEM\_ARCH\_ATTR\_MASK](memory-attr_8h.md#aa180a5da02572a4fe600573e2521abbe) |
| #define | [DT\_MEM\_XTENSA\_GET](#aebb8ec5798ba120fd7f2c020a81349f4)(x) |
| #define | [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)(x) |
| #define | [ATTR\_XTENSA\_INSTR\_ROM](#a4698c95aff86fd63ba1e35b7b195fa07)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ATTR\_XTENSA\_INSTR\_RAM](#a674b85213c6aee2f9078c45d5e21bff3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ATTR\_XTENSA\_DATA\_ROM](#a22e41d116f0a78fc13ed4d3f344e2490)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [ATTR\_XTENSA\_DATA\_RAM](#ac22caa2071000be7deb736dd6340ac4c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [ATTR\_XTENSA\_XLMI](#a2c2b3b4c4421e704ef7f015500a5fc53)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [DT\_MEM\_XTENSA\_INSTR\_ROM](#aa9a1851e86f36be439f024af0d998ee4)   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_INSTR\_ROM](#a4698c95aff86fd63ba1e35b7b195fa07)) |
| #define | [DT\_MEM\_XTENSA\_INSTR\_RAM](#a2566e023ccb0cb9529bc9b1d710d27c3)   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_INSTR\_RAM](#a674b85213c6aee2f9078c45d5e21bff3)) |
| #define | [DT\_MEM\_XTENSA\_DATA\_ROM](#a94f99c060768b249c055eb88bf551de8)   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_DATA\_ROM](#a22e41d116f0a78fc13ed4d3f344e2490)) |
| #define | [DT\_MEM\_XTENSA\_DATA\_RAM](#a3b64411ba4c118b0ef9058e3f8c9ebc8)   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_DATA\_RAM](#ac22caa2071000be7deb736dd6340ac4c)) |
| #define | [DT\_MEM\_XTENSA\_XLMI](#a9e63ac329fa36ad194865c40695bad09)   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_XLMI](#a2c2b3b4c4421e704ef7f015500a5fc53)) |
| #define | [DT\_MEM\_XTENSA\_UNKNOWN](#a272c0689cf885783d2c25598d9506eae)   [DT\_MEM\_ARCH\_ATTR\_UNKNOWN](memory-attr_8h.md#aaefc7bf33d8fa6d5151338cd23b84474) |

## Macro Definition Documentation

## [◆ ](#ac22caa2071000be7deb736dd6340ac4c)ATTR\_XTENSA\_DATA\_RAM

| #define ATTR\_XTENSA\_DATA\_RAM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a22e41d116f0a78fc13ed4d3f344e2490)ATTR\_XTENSA\_DATA\_ROM

| #define ATTR\_XTENSA\_DATA\_ROM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a674b85213c6aee2f9078c45d5e21bff3)ATTR\_XTENSA\_INSTR\_RAM

| #define ATTR\_XTENSA\_INSTR\_RAM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a4698c95aff86fd63ba1e35b7b195fa07)ATTR\_XTENSA\_INSTR\_ROM

| #define ATTR\_XTENSA\_INSTR\_ROM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a2c2b3b4c4421e704ef7f015500a5fc53)ATTR\_XTENSA\_XLMI

| #define ATTR\_XTENSA\_XLMI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a4d678d277f4a6dacf2057bae24c2d3c0)DT\_MEM\_XTENSA

| #define DT\_MEM\_XTENSA | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) << [DT\_MEM\_ARCH\_ATTR\_SHIFT](memory-attr_8h.md#a06e4088178d1ec01ec5cafe289c8eebe))

[DT\_MEM\_ARCH\_ATTR\_SHIFT](memory-attr_8h.md#a06e4088178d1ec01ec5cafe289c8eebe)

#define DT\_MEM\_ARCH\_ATTR\_SHIFT

**Definition** memory-attr.h:48

## [◆ ](#a3b64411ba4c118b0ef9058e3f8c9ebc8)DT\_MEM\_XTENSA\_DATA\_RAM

| #define DT\_MEM\_XTENSA\_DATA\_RAM   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_DATA\_RAM](#ac22caa2071000be7deb736dd6340ac4c)) |
| --- |

## [◆ ](#a94f99c060768b249c055eb88bf551de8)DT\_MEM\_XTENSA\_DATA\_ROM

| #define DT\_MEM\_XTENSA\_DATA\_ROM   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_DATA\_ROM](#a22e41d116f0a78fc13ed4d3f344e2490)) |
| --- |

## [◆ ](#aebb8ec5798ba120fd7f2c020a81349f4)DT\_MEM\_XTENSA\_GET

| #define DT\_MEM\_XTENSA\_GET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & [DT\_MEM\_XTENSA\_MASK](#a90663eb795734c0f1f8f7cdc50584d87))

[DT\_MEM\_XTENSA\_MASK](#a90663eb795734c0f1f8f7cdc50584d87)

#define DT\_MEM\_XTENSA\_MASK

**Definition** memory-attr-xtensa.h:15

## [◆ ](#a2566e023ccb0cb9529bc9b1d710d27c3)DT\_MEM\_XTENSA\_INSTR\_RAM

| #define DT\_MEM\_XTENSA\_INSTR\_RAM   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_INSTR\_RAM](#a674b85213c6aee2f9078c45d5e21bff3)) |
| --- |

## [◆ ](#aa9a1851e86f36be439f024af0d998ee4)DT\_MEM\_XTENSA\_INSTR\_ROM

| #define DT\_MEM\_XTENSA\_INSTR\_ROM   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_INSTR\_ROM](#a4698c95aff86fd63ba1e35b7b195fa07)) |
| --- |

## [◆ ](#a90663eb795734c0f1f8f7cdc50584d87)DT\_MEM\_XTENSA\_MASK

| #define DT\_MEM\_XTENSA\_MASK   [DT\_MEM\_ARCH\_ATTR\_MASK](memory-attr_8h.md#aa180a5da02572a4fe600573e2521abbe) |
| --- |

## [◆ ](#a272c0689cf885783d2c25598d9506eae)DT\_MEM\_XTENSA\_UNKNOWN

| #define DT\_MEM\_XTENSA\_UNKNOWN   [DT\_MEM\_ARCH\_ATTR\_UNKNOWN](memory-attr_8h.md#aaefc7bf33d8fa6d5151338cd23b84474) |
| --- |

## [◆ ](#a9e63ac329fa36ad194865c40695bad09)DT\_MEM\_XTENSA\_XLMI

| #define DT\_MEM\_XTENSA\_XLMI   [DT\_MEM\_XTENSA](#a4d678d277f4a6dacf2057bae24c2d3c0)([ATTR\_XTENSA\_XLMI](#a2c2b3b4c4421e704ef7f015500a5fc53)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr-xtensa.h](memory-attr-xtensa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
