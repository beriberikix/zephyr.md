---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/memory-attr-arm_8h.html
original_path: doxygen/html/memory-attr-arm_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr-arm.h File Reference

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h_source.md)>`

[Go to the source code of this file.](memory-attr-arm_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_MEM\_ARM\_MASK](#a9a01f8cd34e900d2074c23bec1020bf1)   [DT\_MEM\_ARCH\_ATTR\_MASK](memory-attr_8h.md#aa180a5da02572a4fe600573e2521abbe) |
| #define | [DT\_MEM\_ARM\_GET](#ac9237bf43ea0801606a72bb1aa408952)(x) |
| #define | [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)(x) |
| #define | [ATTR\_MPU\_RAM](#a7da536df6516679b7256651cd76a3ce0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ATTR\_MPU\_RAM\_NOCACHE](#a0539bc3fbc9a9ed421869b7a88bc01bf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ATTR\_MPU\_FLASH](#a42ee73c11a945c9d636a3806d5bf7eb6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [ATTR\_MPU\_PPB](#a5d7a78767be0cff6b4c6523761cf3055)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [ATTR\_MPU\_IO](#ac5fd54c9e182c46e6d48cd94713fb164)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [ATTR\_MPU\_EXTMEM](#ac7e9b3c506fd8ba0170c248cb681e347)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [DT\_MEM\_ARM\_MPU\_RAM](#ab3669734951faa3f55f85db9fe005daa)   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_RAM](#a7da536df6516679b7256651cd76a3ce0)) |
| #define | [DT\_MEM\_ARM\_MPU\_RAM\_NOCACHE](#af60fb9c11ef84238647855f52a338904)   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_RAM\_NOCACHE](#a0539bc3fbc9a9ed421869b7a88bc01bf)) |
| #define | [DT\_MEM\_ARM\_MPU\_FLASH](#a2bc421f5582d90604dc95b796a475221)   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_FLASH](#a42ee73c11a945c9d636a3806d5bf7eb6)) |
| #define | [DT\_MEM\_ARM\_MPU\_PPB](#a7b0f983bdde1aab0cf703006aa79c363)   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_PPB](#a5d7a78767be0cff6b4c6523761cf3055)) |
| #define | [DT\_MEM\_ARM\_MPU\_IO](#a21a8d85ff9c329bb4ebd9f9f4a9b2e9c)   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_IO](#ac5fd54c9e182c46e6d48cd94713fb164)) |
| #define | [DT\_MEM\_ARM\_MPU\_EXTMEM](#add7dd0c9f14a8696d1827d3d5bfbb263)   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_EXTMEM](#ac7e9b3c506fd8ba0170c248cb681e347)) |
| #define | [DT\_MEM\_ARM\_MPU\_UNKNOWN](#ab24037ec20705fdf979d453046cd979a)   [DT\_MEM\_ARCH\_ATTR\_UNKNOWN](memory-attr_8h.md#aaefc7bf33d8fa6d5151338cd23b84474) |

## Macro Definition Documentation

## [◆ ](#ac7e9b3c506fd8ba0170c248cb681e347)ATTR\_MPU\_EXTMEM

| #define ATTR\_MPU\_EXTMEM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a42ee73c11a945c9d636a3806d5bf7eb6)ATTR\_MPU\_FLASH

| #define ATTR\_MPU\_FLASH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ac5fd54c9e182c46e6d48cd94713fb164)ATTR\_MPU\_IO

| #define ATTR\_MPU\_IO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a5d7a78767be0cff6b4c6523761cf3055)ATTR\_MPU\_PPB

| #define ATTR\_MPU\_PPB   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a7da536df6516679b7256651cd76a3ce0)ATTR\_MPU\_RAM

| #define ATTR\_MPU\_RAM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a0539bc3fbc9a9ed421869b7a88bc01bf)ATTR\_MPU\_RAM\_NOCACHE

| #define ATTR\_MPU\_RAM\_NOCACHE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a4676991c272cbdae9890dc320a827a11)DT\_MEM\_ARM

| #define DT\_MEM\_ARM | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) << [DT\_MEM\_ARCH\_ATTR\_SHIFT](memory-attr_8h.md#a06e4088178d1ec01ec5cafe289c8eebe))

[DT\_MEM\_ARCH\_ATTR\_SHIFT](memory-attr_8h.md#a06e4088178d1ec01ec5cafe289c8eebe)

#define DT\_MEM\_ARCH\_ATTR\_SHIFT

**Definition** memory-attr.h:48

## [◆ ](#ac9237bf43ea0801606a72bb1aa408952)DT\_MEM\_ARM\_GET

| #define DT\_MEM\_ARM\_GET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & [DT\_MEM\_ARM\_MASK](#a9a01f8cd34e900d2074c23bec1020bf1))

[DT\_MEM\_ARM\_MASK](#a9a01f8cd34e900d2074c23bec1020bf1)

#define DT\_MEM\_ARM\_MASK

**Definition** memory-attr-arm.h:21

## [◆ ](#a9a01f8cd34e900d2074c23bec1020bf1)DT\_MEM\_ARM\_MASK

| #define DT\_MEM\_ARM\_MASK   [DT\_MEM\_ARCH\_ATTR\_MASK](memory-attr_8h.md#aa180a5da02572a4fe600573e2521abbe) |
| --- |

## [◆ ](#add7dd0c9f14a8696d1827d3d5bfbb263)DT\_MEM\_ARM\_MPU\_EXTMEM

| #define DT\_MEM\_ARM\_MPU\_EXTMEM   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_EXTMEM](#ac7e9b3c506fd8ba0170c248cb681e347)) |
| --- |

## [◆ ](#a2bc421f5582d90604dc95b796a475221)DT\_MEM\_ARM\_MPU\_FLASH

| #define DT\_MEM\_ARM\_MPU\_FLASH   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_FLASH](#a42ee73c11a945c9d636a3806d5bf7eb6)) |
| --- |

## [◆ ](#a21a8d85ff9c329bb4ebd9f9f4a9b2e9c)DT\_MEM\_ARM\_MPU\_IO

| #define DT\_MEM\_ARM\_MPU\_IO   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_IO](#ac5fd54c9e182c46e6d48cd94713fb164)) |
| --- |

## [◆ ](#a7b0f983bdde1aab0cf703006aa79c363)DT\_MEM\_ARM\_MPU\_PPB

| #define DT\_MEM\_ARM\_MPU\_PPB   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_PPB](#a5d7a78767be0cff6b4c6523761cf3055)) |
| --- |

## [◆ ](#ab3669734951faa3f55f85db9fe005daa)DT\_MEM\_ARM\_MPU\_RAM

| #define DT\_MEM\_ARM\_MPU\_RAM   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_RAM](#a7da536df6516679b7256651cd76a3ce0)) |
| --- |

## [◆ ](#af60fb9c11ef84238647855f52a338904)DT\_MEM\_ARM\_MPU\_RAM\_NOCACHE

| #define DT\_MEM\_ARM\_MPU\_RAM\_NOCACHE   [DT\_MEM\_ARM](#a4676991c272cbdae9890dc320a827a11)([ATTR\_MPU\_RAM\_NOCACHE](#a0539bc3fbc9a9ed421869b7a88bc01bf)) |
| --- |

## [◆ ](#ab24037ec20705fdf979d453046cd979a)DT\_MEM\_ARM\_MPU\_UNKNOWN

| #define DT\_MEM\_ARM\_MPU\_UNKNOWN   [DT\_MEM\_ARCH\_ATTR\_UNKNOWN](memory-attr_8h.md#aaefc7bf33d8fa6d5151338cd23b84474) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr-arm.h](memory-attr-arm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
