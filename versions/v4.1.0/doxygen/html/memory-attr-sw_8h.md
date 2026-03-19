---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/memory-attr-sw_8h.html
original_path: doxygen/html/memory-attr-sw_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr-sw.h File Reference

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h_source.md)>`

[Go to the source code of this file.](memory-attr-sw_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_MEM\_SW\_MASK](#a35cd6e6c03a9304267a6a33edaae65b8)   [DT\_MEM\_SW\_ATTR\_MASK](memory-attr_8h.md#a2020f22247371f4200f9968f75ac9bcb) |
| #define | [DT\_MEM\_SW\_GET](#ad6c8b22aa5dc6c5bb8abd5c3ed297478)(x) |
| #define | [DT\_MEM\_SW](#ad7c4ae7ee3908612be90ef166d417881)(x) |
| #define | [ATTR\_SW\_ALLOC\_CACHE](#adccfc787238048f59167e5913bf74e41)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ATTR\_SW\_ALLOC\_NON\_CACHE](#af308d88c0732fb69e96577c594ca1a48)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ATTR\_SW\_ALLOC\_DMA](#a92d7fb61ed72428bfaf9d397fb6c32c6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [DT\_MEM\_SW\_ALLOC\_CACHE](#a616d67585f6370117e5e341861b0baad)   [DT\_MEM\_SW](#ad7c4ae7ee3908612be90ef166d417881)([ATTR\_SW\_ALLOC\_CACHE](#adccfc787238048f59167e5913bf74e41)) |
| #define | [DT\_MEM\_SW\_ALLOC\_NON\_CACHE](#aa1dbfaea4961ee2545831d585ba0c710)   [DT\_MEM\_SW](#ad7c4ae7ee3908612be90ef166d417881)([ATTR\_SW\_ALLOC\_NON\_CACHE](#af308d88c0732fb69e96577c594ca1a48)) |
| #define | [DT\_MEM\_SW\_ALLOC\_DMA](#a308104aa9d2ef98de2d024e7186e35b8)   [DT\_MEM\_SW](#ad7c4ae7ee3908612be90ef166d417881)([ATTR\_SW\_ALLOC\_DMA](#a92d7fb61ed72428bfaf9d397fb6c32c6)) |

## Macro Definition Documentation

## [◆ ](#adccfc787238048f59167e5913bf74e41)ATTR\_SW\_ALLOC\_CACHE

| #define ATTR\_SW\_ALLOC\_CACHE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a92d7fb61ed72428bfaf9d397fb6c32c6)ATTR\_SW\_ALLOC\_DMA

| #define ATTR\_SW\_ALLOC\_DMA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#af308d88c0732fb69e96577c594ca1a48)ATTR\_SW\_ALLOC\_NON\_CACHE

| #define ATTR\_SW\_ALLOC\_NON\_CACHE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ad7c4ae7ee3908612be90ef166d417881)DT\_MEM\_SW

| #define DT\_MEM\_SW | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) << [DT\_MEM\_SW\_ATTR\_SHIFT](memory-attr_8h.md#a0586962ab2fa5990de15ea20c727f224))

[DT\_MEM\_SW\_ATTR\_SHIFT](memory-attr_8h.md#a0586962ab2fa5990de15ea20c727f224)

#define DT\_MEM\_SW\_ATTR\_SHIFT

**Definition** memory-attr.h:35

## [◆ ](#a616d67585f6370117e5e341861b0baad)DT\_MEM\_SW\_ALLOC\_CACHE

| #define DT\_MEM\_SW\_ALLOC\_CACHE   [DT\_MEM\_SW](#ad7c4ae7ee3908612be90ef166d417881)([ATTR\_SW\_ALLOC\_CACHE](#adccfc787238048f59167e5913bf74e41)) |
| --- |

## [◆ ](#a308104aa9d2ef98de2d024e7186e35b8)DT\_MEM\_SW\_ALLOC\_DMA

| #define DT\_MEM\_SW\_ALLOC\_DMA   [DT\_MEM\_SW](#ad7c4ae7ee3908612be90ef166d417881)([ATTR\_SW\_ALLOC\_DMA](#a92d7fb61ed72428bfaf9d397fb6c32c6)) |
| --- |

## [◆ ](#aa1dbfaea4961ee2545831d585ba0c710)DT\_MEM\_SW\_ALLOC\_NON\_CACHE

| #define DT\_MEM\_SW\_ALLOC\_NON\_CACHE   [DT\_MEM\_SW](#ad7c4ae7ee3908612be90ef166d417881)([ATTR\_SW\_ALLOC\_NON\_CACHE](#af308d88c0732fb69e96577c594ca1a48)) |
| --- |

## [◆ ](#ad6c8b22aa5dc6c5bb8abd5c3ed297478)DT\_MEM\_SW\_GET

| #define DT\_MEM\_SW\_GET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & [DT\_MEM\_SW\_ATTR\_MASK](memory-attr_8h.md#a2020f22247371f4200f9968f75ac9bcb))

[DT\_MEM\_SW\_ATTR\_MASK](memory-attr_8h.md#a2020f22247371f4200f9968f75ac9bcb)

#define DT\_MEM\_SW\_ATTR\_MASK

**Definition** memory-attr.h:33

## [◆ ](#a35cd6e6c03a9304267a6a33edaae65b8)DT\_MEM\_SW\_MASK

| #define DT\_MEM\_SW\_MASK   [DT\_MEM\_SW\_ATTR\_MASK](memory-attr_8h.md#a2020f22247371f4200f9968f75ac9bcb) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr-sw.h](memory-attr-sw_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
