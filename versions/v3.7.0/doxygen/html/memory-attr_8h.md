---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/memory-attr_8h.html
original_path: doxygen/html/memory-attr_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr.h File Reference

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](memory-attr_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_MEM\_ATTR\_MASK](#adf502f055c516d85610d8a9b5bb7e546)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [DT\_MEM\_ATTR\_GET](#a971bc033e3971ff32aec78a917590f1a)(x) |
| #define | [DT\_MEM\_ATTR\_SHIFT](#ada810aa72a8c0f34fcab7ffe3a3a582e)   (0) |
| #define | [DT\_MEM\_CACHEABLE](#a74b1e3dceed92cf63ed018e971c89573)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* cacheable \*/ |
| #define | [DT\_MEM\_NON\_VOLATILE](#a6090422ffdac9177b6a6528b3ea4cc77)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* non-volatile \*/ |
| #define | [DT\_MEM\_OOO](#a2d0c09a13622358e4ef50da93455e5dd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* out-of-order \*/ |
| #define | [DT\_MEM\_DMA](#a292b651c06018870fb199b61eb2a20e3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) /\* DMA-able \*/ |
| #define | [DT\_MEM\_UNKNOWN](#acedd7086cb2240a69896611c58a654a1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) /\* must be last \*/ |
| #define | [DT\_MEM\_SW\_ATTR\_MASK](#a2020f22247371f4200f9968f75ac9bcb)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 16) |
| #define | [DT\_MEM\_SW\_ATTR\_GET](#a05f246d5ab8ac568eb4174584d543c56)(x) |
| #define | [DT\_MEM\_SW\_ATTR\_SHIFT](#a0586962ab2fa5990de15ea20c727f224)   (16) |
| #define | [DT\_MEM\_SW\_ATTR\_UNKNOWN](#ae3f39518836c19ee2616f0ad11fda5dc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| #define | [DT\_MEM\_ARCH\_ATTR\_MASK](#aa180a5da02572a4fe600573e2521abbe)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 20) |
| #define | [DT\_MEM\_ARCH\_ATTR\_GET](#a5c56e38ef80dc9feb6f3353cac1ddbdf)(x) |
| #define | [DT\_MEM\_ARCH\_ATTR\_SHIFT](#a06e4088178d1ec01ec5cafe289c8eebe)   (20) |
| #define | [DT\_MEM\_ARCH\_ATTR\_UNKNOWN](#aaefc7bf33d8fa6d5151338cd23b84474)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |

## Macro Definition Documentation

## [◆ ](#a5c56e38ef80dc9feb6f3353cac1ddbdf)DT\_MEM\_ARCH\_ATTR\_GET

| #define DT\_MEM\_ARCH\_ATTR\_GET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & [DT\_MEM\_ARCH\_ATTR\_MASK](#aa180a5da02572a4fe600573e2521abbe))

[DT\_MEM\_ARCH\_ATTR\_MASK](#aa180a5da02572a4fe600573e2521abbe)

#define DT\_MEM\_ARCH\_ATTR\_MASK

**Definition** memory-attr.h:46

## [◆ ](#aa180a5da02572a4fe600573e2521abbe)DT\_MEM\_ARCH\_ATTR\_MASK

| #define DT\_MEM\_ARCH\_ATTR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 20) |
| --- |

## [◆ ](#a06e4088178d1ec01ec5cafe289c8eebe)DT\_MEM\_ARCH\_ATTR\_SHIFT

| #define DT\_MEM\_ARCH\_ATTR\_SHIFT   (20) |
| --- |

## [◆ ](#aaefc7bf33d8fa6d5151338cd23b84474)DT\_MEM\_ARCH\_ATTR\_UNKNOWN

| #define DT\_MEM\_ARCH\_ATTR\_UNKNOWN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| --- |

## [◆ ](#a971bc033e3971ff32aec78a917590f1a)DT\_MEM\_ATTR\_GET

| #define DT\_MEM\_ATTR\_GET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & [DT\_MEM\_ATTR\_MASK](#adf502f055c516d85610d8a9b5bb7e546))

[DT\_MEM\_ATTR\_MASK](#adf502f055c516d85610d8a9b5bb7e546)

#define DT\_MEM\_ATTR\_MASK

**Definition** memory-attr.h:16

## [◆ ](#adf502f055c516d85610d8a9b5bb7e546)DT\_MEM\_ATTR\_MASK

| #define DT\_MEM\_ATTR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

## [◆ ](#ada810aa72a8c0f34fcab7ffe3a3a582e)DT\_MEM\_ATTR\_SHIFT

| #define DT\_MEM\_ATTR\_SHIFT   (0) |
| --- |

## [◆ ](#a74b1e3dceed92cf63ed018e971c89573)DT\_MEM\_CACHEABLE

| #define DT\_MEM\_CACHEABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* cacheable \*/ |
| --- |

## [◆ ](#a292b651c06018870fb199b61eb2a20e3)DT\_MEM\_DMA

| #define DT\_MEM\_DMA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) /\* DMA-able \*/ |
| --- |

## [◆ ](#a6090422ffdac9177b6a6528b3ea4cc77)DT\_MEM\_NON\_VOLATILE

| #define DT\_MEM\_NON\_VOLATILE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* non-volatile \*/ |
| --- |

## [◆ ](#a2d0c09a13622358e4ef50da93455e5dd)DT\_MEM\_OOO

| #define DT\_MEM\_OOO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* out-of-order \*/ |
| --- |

## [◆ ](#a05f246d5ab8ac568eb4174584d543c56)DT\_MEM\_SW\_ATTR\_GET

| #define DT\_MEM\_SW\_ATTR\_GET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & [DT\_MEM\_SW\_ATTR\_MASK](#a2020f22247371f4200f9968f75ac9bcb))

[DT\_MEM\_SW\_ATTR\_MASK](#a2020f22247371f4200f9968f75ac9bcb)

#define DT\_MEM\_SW\_ATTR\_MASK

**Definition** memory-attr.h:33

## [◆ ](#a2020f22247371f4200f9968f75ac9bcb)DT\_MEM\_SW\_ATTR\_MASK

| #define DT\_MEM\_SW\_ATTR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 16) |
| --- |

## [◆ ](#a0586962ab2fa5990de15ea20c727f224)DT\_MEM\_SW\_ATTR\_SHIFT

| #define DT\_MEM\_SW\_ATTR\_SHIFT   (16) |
| --- |

## [◆ ](#ae3f39518836c19ee2616f0ad11fda5dc)DT\_MEM\_SW\_ATTR\_UNKNOWN

| #define DT\_MEM\_SW\_ATTR\_UNKNOWN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| --- |

## [◆ ](#acedd7086cb2240a69896611c58a654a1)DT\_MEM\_UNKNOWN

| #define DT\_MEM\_UNKNOWN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) /\* must be last \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr.h](memory-attr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
