---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/segmentation_8h.html
original_path: doxygen/html/segmentation_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

segmentation.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](segmentation_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [task\_state\_segment](structtask__state__segment.md) |
| struct | [segment\_descriptor](structsegment__descriptor.md) |
| struct | [pseudo\_descriptor](structpseudo__descriptor.md) |
| struct | [far\_ptr](structfar__ptr.md) |

| Macros | |
| --- | --- |
| #define | [SEG\_TYPE\_LDT](#a1123609025ff8c35fcebbeefc627fe40)   0x2 |
| #define | [SEG\_TYPE\_TASK\_GATE](#a09b28d129d4935e1ac79010ad2ed845c)   0x5 |
| #define | [SEG\_TYPE\_TSS](#a9526fd354b043f1d989133fb51584ca5)   0x9 |
| #define | [SEG\_TYPE\_TSS\_BUSY](#a358e9557d55f44b1e0c48f56e9bb8eb8)   0xB |
| #define | [SEG\_TYPE\_CALL\_GATE](#a06659cf84f44e085e88adf1f249ea958)   0xC |
| #define | [SEG\_TYPE\_IRQ\_GATE](#a62c20d09a1f35aadbffc000ce695aca5)   0xE |
| #define | [SEG\_TYPE\_TRAP\_GATE](#a24ba226f5d7c4a2d0e73d129b811d009)   0xF |
| #define | [DT\_GRAN\_BYTE](#a93b8e20c30316e0b31ce2d72ee429267)   0 |
| #define | [DT\_GRAN\_PAGE](#abd17be4fcc2b1627fdd9fce4f2616034)   1 |
| #define | [DT\_READABLE](#adb3a30ddf8c9e70de7f2f4e9532012c2)   1 |
| #define | [DT\_NON\_READABLE](#a440b0121a23eaee4a6da138464598332)   0 |
| #define | [DT\_WRITABLE](#a9fed0f1041479b83a2177ce758026e01)   1 |
| #define | [DT\_NON\_WRITABLE](#a06578eef93a325c17c431c4e30358f68)   0 |
| #define | [DT\_EXPAND\_DOWN](#aafd044e471668a2ad5d65d375fcb037b)   1 |
| #define | [DT\_EXPAND\_UP](#a42725696f61f6c208aad358e0ef99521)   0 |
| #define | [DT\_CONFORM](#a1bf28de4d983377685927df65ada05fc)   1 |
| #define | [DT\_NONCONFORM](#a829d7ba32b7ff93ee11394e198412fb6)   0 |
| #define | [DT\_TYPE\_SYSTEM](#a7e6ddc88924ea43b4d89f367cee558d4)   0 |
| #define | [DT\_TYPE\_CODEDATA](#adde93db381ef8fc598457a3cef782aa1)   1 |
| #define | [SEG\_SELECTOR](#a7ac21eabd74b9b1e132d0925841a162d)(index, table, dpl) |
| #define | [DT\_ZERO\_ENTRY](#abe841886ae3cb0d59ceb52885d1283c7)   { { 0 } } |
| #define | [DT\_CODE\_SEG\_ENTRY](#ab5c6bcde7b78dff38fcb2c4f3933e976)(base\_p, limit\_p, granularity\_p, dpl\_p, readable\_p, conforming\_p) |
| #define | [DT\_DATA\_SEG\_ENTRY](#a91d1151f098e25c090d23d837c7aab05)(base\_p, limit\_p, granularity\_p, dpl\_p, writable\_p, direction\_p) |
| #define | [DT\_LDT\_ENTRY](#af27ff503d122d2da7548544833ec8549)(base\_p, limit\_p, granularity\_p, dpl\_p) |
| #define | [DT\_TSS\_ENTRY](#ae5739136f793ed325e29441584ea65a5)(base\_p, limit\_p, granularity\_p, dpl\_p) |
| #define | [DT\_TSS\_STD\_ENTRY](#a80cfbaa5c30032fafa5507255a2910e4)(base\_p, dpl\_p) |
| #define | [DT\_TASK\_GATE\_ENTRY](#a3d598069efca9fad4537f5184f65a1a4)(segment\_p, dpl\_p) |
| #define | [DT\_IRQ\_GATE\_ENTRY](#a75b12840f3c26ab2de1240874c6ffc82)(segment\_p, offset\_p, dpl\_p) |
| #define | [DT\_TRAP\_GATE\_ENTRY](#a21a76c871381dce14ff5f35520db7cf0)(segment\_p, offset\_p, dpl\_p) |
| #define | [DT\_CALL\_GATE\_ENTRY](#a275e217de9e845c8c9ac717120883796)(segment\_p, offset\_p, dpl\_p, param\_count\_p) |
| #define | [DTE\_BASE](#a1ea5335d043ecfb349e0a97da0734a51)(dt\_entry) |
| #define | [DTE\_LIMIT](#a0f68ae723f072069a290b322aee9a133)(dt\_entry) |
| #define | [DTE\_OFFSET](#a1539f29629508325e28796d3226630cc)(dt\_entry) |
| #define | [DT\_INIT](#a76e349fa3b5b4263cf2fbe93e11ece50)(entries) |

## Macro Definition Documentation

## [◆ ](#a275e217de9e845c8c9ac717120883796)DT\_CALL\_GATE\_ENTRY

| #define DT\_CALL\_GATE\_ENTRY | ( |  | *segment\_p*, |
| --- | --- | --- | --- |
|  |  |  | *offset\_p*, |
|  |  |  | *dpl\_p*, |
|  |  |  | *param\_count\_p* ) |

**Value:**

{ \

\_DESC\_COMMON(dpl\_p), \

\_SEGMENT\_AND\_OFFSET(segment\_p, offset\_p), \

\_SYS\_DESC([SEG\_TYPE\_TRAP\_GATE](#a24ba226f5d7c4a2d0e73d129b811d009)), \

.reserved\_or\_param = (param\_count\_p), \

.always\_0\_0 = 0 \

}

[SEG\_TYPE\_TRAP\_GATE](#a24ba226f5d7c4a2d0e73d129b811d009)

#define SEG\_TYPE\_TRAP\_GATE

**Definition** segmentation.h:31

## [◆ ](#ab5c6bcde7b78dff38fcb2c4f3933e976)DT\_CODE\_SEG\_ENTRY

| #define DT\_CODE\_SEG\_ENTRY | ( |  | *base\_p*, |
| --- | --- | --- | --- |
|  |  |  | *limit\_p*, |
|  |  |  | *granularity\_p*, |
|  |  |  | *dpl\_p*, |
|  |  |  | *readable\_p*, |
|  |  |  | *conforming\_p* ) |

**Value:**

{ \

\_DESC\_COMMON(dpl\_p), \

\_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p), \

.accessed = 0, \

.rw = (readable\_p), \

.cd = (conforming\_p), \

.executable = 1, \

.descriptor\_type = 1 \

}

## [◆ ](#a1bf28de4d983377685927df65ada05fc)DT\_CONFORM

| #define DT\_CONFORM   1 |
| --- |

## [◆ ](#a91d1151f098e25c090d23d837c7aab05)DT\_DATA\_SEG\_ENTRY

| #define DT\_DATA\_SEG\_ENTRY | ( |  | *base\_p*, |
| --- | --- | --- | --- |
|  |  |  | *limit\_p*, |
|  |  |  | *granularity\_p*, |
|  |  |  | *dpl\_p*, |
|  |  |  | *writable\_p*, |
|  |  |  | *direction\_p* ) |

**Value:**

{ \

\_DESC\_COMMON(dpl\_p), \

\_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p), \

.accessed = 0, \

.rw = (writable\_p), \

.cd = (direction\_p), \

.executable = 0, \

.descriptor\_type = 1 \

}

## [◆ ](#aafd044e471668a2ad5d65d375fcb037b)DT\_EXPAND\_DOWN

| #define DT\_EXPAND\_DOWN   1 |
| --- |

## [◆ ](#a42725696f61f6c208aad358e0ef99521)DT\_EXPAND\_UP

| #define DT\_EXPAND\_UP   0 |
| --- |

## [◆ ](#a93b8e20c30316e0b31ce2d72ee429267)DT\_GRAN\_BYTE

| #define DT\_GRAN\_BYTE   0 |
| --- |

## [◆ ](#abd17be4fcc2b1627fdd9fce4f2616034)DT\_GRAN\_PAGE

| #define DT\_GRAN\_PAGE   1 |
| --- |

## [◆ ](#a76e349fa3b5b4263cf2fbe93e11ece50)DT\_INIT

| #define DT\_INIT | ( |  | *entries* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ sizeof(entries) - 1, &entries[0] }

## [◆ ](#a75b12840f3c26ab2de1240874c6ffc82)DT\_IRQ\_GATE\_ENTRY

| #define DT\_IRQ\_GATE\_ENTRY | ( |  | *segment\_p*, |
| --- | --- | --- | --- |
|  |  |  | *offset\_p*, |
|  |  |  | *dpl\_p* ) |

**Value:**

{ \

\_DESC\_COMMON(dpl\_p), \

\_SEGMENT\_AND\_OFFSET(segment\_p, offset\_p), \

\_SYS\_DESC([SEG\_TYPE\_IRQ\_GATE](#a62c20d09a1f35aadbffc000ce695aca5)), \

.always\_0\_0 = 0 \

}

[SEG\_TYPE\_IRQ\_GATE](#a62c20d09a1f35aadbffc000ce695aca5)

#define SEG\_TYPE\_IRQ\_GATE

**Definition** segmentation.h:30

## [◆ ](#af27ff503d122d2da7548544833ec8549)DT\_LDT\_ENTRY

| #define DT\_LDT\_ENTRY | ( |  | *base\_p*, |
| --- | --- | --- | --- |
|  |  |  | *limit\_p*, |
|  |  |  | *granularity\_p*, |
|  |  |  | *dpl\_p* ) |

**Value:**

{ \

\_DESC\_COMMON(dpl\_p), \

\_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p), \

\_SYS\_DESC([SEG\_TYPE\_LDT](#a1123609025ff8c35fcebbeefc627fe40)) \

}

[SEG\_TYPE\_LDT](#a1123609025ff8c35fcebbeefc627fe40)

#define SEG\_TYPE\_LDT

**Definition** segmentation.h:25

## [◆ ](#a440b0121a23eaee4a6da138464598332)DT\_NON\_READABLE

| #define DT\_NON\_READABLE   0 |
| --- |

## [◆ ](#a06578eef93a325c17c431c4e30358f68)DT\_NON\_WRITABLE

| #define DT\_NON\_WRITABLE   0 |
| --- |

## [◆ ](#a829d7ba32b7ff93ee11394e198412fb6)DT\_NONCONFORM

| #define DT\_NONCONFORM   0 |
| --- |

## [◆ ](#adb3a30ddf8c9e70de7f2f4e9532012c2)DT\_READABLE

| #define DT\_READABLE   1 |
| --- |

## [◆ ](#a3d598069efca9fad4537f5184f65a1a4)DT\_TASK\_GATE\_ENTRY

| #define DT\_TASK\_GATE\_ENTRY | ( |  | *segment\_p*, |
| --- | --- | --- | --- |
|  |  |  | *dpl\_p* ) |

**Value:**

{ \

\_DESC\_COMMON(dpl\_p), \

\_SYS\_DESC([SEG\_TYPE\_TASK\_GATE](#a09b28d129d4935e1ac79010ad2ed845c)), \

.segment\_selector = (segment\_p) \

}

[SEG\_TYPE\_TASK\_GATE](#a09b28d129d4935e1ac79010ad2ed845c)

#define SEG\_TYPE\_TASK\_GATE

**Definition** segmentation.h:26

## [◆ ](#a21a76c871381dce14ff5f35520db7cf0)DT\_TRAP\_GATE\_ENTRY

| #define DT\_TRAP\_GATE\_ENTRY | ( |  | *segment\_p*, |
| --- | --- | --- | --- |
|  |  |  | *offset\_p*, |
|  |  |  | *dpl\_p* ) |

**Value:**

{ \

\_DESC\_COMMON(dpl\_p), \

\_SEGMENT\_AND\_OFFSET(segment\_p, offset\_p), \

\_SYS\_DESC([SEG\_TYPE\_TRAP\_GATE](#a24ba226f5d7c4a2d0e73d129b811d009)), \

.always\_0\_0 = 0 \

}

## [◆ ](#ae5739136f793ed325e29441584ea65a5)DT\_TSS\_ENTRY

| #define DT\_TSS\_ENTRY | ( |  | *base\_p*, |
| --- | --- | --- | --- |
|  |  |  | *limit\_p*, |
|  |  |  | *granularity\_p*, |
|  |  |  | *dpl\_p* ) |

**Value:**

{ \

\_DESC\_COMMON(dpl\_p), \

\_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p), \

\_SYS\_DESC([SEG\_TYPE\_TSS](#a9526fd354b043f1d989133fb51584ca5)) \

}

[SEG\_TYPE\_TSS](#a9526fd354b043f1d989133fb51584ca5)

#define SEG\_TYPE\_TSS

**Definition** segmentation.h:27

## [◆ ](#a80cfbaa5c30032fafa5507255a2910e4)DT\_TSS\_STD\_ENTRY

| #define DT\_TSS\_STD\_ENTRY | ( |  | *base\_p*, |
| --- | --- | --- | --- |
|  |  |  | *dpl\_p* ) |

**Value:**

[DT\_TSS\_ENTRY](#ae5739136f793ed325e29441584ea65a5)(base\_p, sizeof(struct [task\_state\_segment](structtask__state__segment.md)), [DT\_GRAN\_BYTE](#a93b8e20c30316e0b31ce2d72ee429267), \

dpl\_p)

[DT\_GRAN\_BYTE](#a93b8e20c30316e0b31ce2d72ee429267)

#define DT\_GRAN\_BYTE

**Definition** segmentation.h:33

[DT\_TSS\_ENTRY](#ae5739136f793ed325e29441584ea65a5)

#define DT\_TSS\_ENTRY(base\_p, limit\_p, granularity\_p, dpl\_p)

**Definition** segmentation.h:298

[task\_state\_segment](structtask__state__segment.md)

**Definition** segmentation.h:54

## [◆ ](#adde93db381ef8fc598457a3cef782aa1)DT\_TYPE\_CODEDATA

| #define DT\_TYPE\_CODEDATA   1 |
| --- |

## [◆ ](#a7e6ddc88924ea43b4d89f367cee558d4)DT\_TYPE\_SYSTEM

| #define DT\_TYPE\_SYSTEM   0 |
| --- |

## [◆ ](#a9fed0f1041479b83a2177ce758026e01)DT\_WRITABLE

| #define DT\_WRITABLE   1 |
| --- |

## [◆ ](#abe841886ae3cb0d59ceb52885d1283c7)DT\_ZERO\_ENTRY

| #define DT\_ZERO\_ENTRY   { { 0 } } |
| --- |

## [◆ ](#a1ea5335d043ecfb349e0a97da0734a51)DTE\_BASE

| #define DTE\_BASE | ( |  | *dt\_entry* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((dt\_entry)->base\_low | \

((dt\_entry)->base\_mid << 16) | \

((dt\_entry)->base\_hi << 24))

## [◆ ](#a0f68ae723f072069a290b322aee9a133)DTE\_LIMIT

| #define DTE\_LIMIT | ( |  | *dt\_entry* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((dt\_entry)->limit\_low | \

((dt\_entry)->limit\_hi << 16))

## [◆ ](#a1539f29629508325e28796d3226630cc)DTE\_OFFSET

| #define DTE\_OFFSET | ( |  | *dt\_entry* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((dt\_entry)->offset\_low | \

((dt\_entry)->offset\_hi << 16))

## [◆ ](#a7ac21eabd74b9b1e132d0925841a162d)SEG\_SELECTOR

| #define SEG\_SELECTOR | ( |  | *index*, |
| --- | --- | --- | --- |
|  |  |  | *table*, |
|  |  |  | *dpl* ) |

**Value:**

(index << 3 | table << 2 | dpl)

## [◆ ](#a06659cf84f44e085e88adf1f249ea958)SEG\_TYPE\_CALL\_GATE

| #define SEG\_TYPE\_CALL\_GATE   0xC |
| --- |

## [◆ ](#a62c20d09a1f35aadbffc000ce695aca5)SEG\_TYPE\_IRQ\_GATE

| #define SEG\_TYPE\_IRQ\_GATE   0xE |
| --- |

## [◆ ](#a1123609025ff8c35fcebbeefc627fe40)SEG\_TYPE\_LDT

| #define SEG\_TYPE\_LDT   0x2 |
| --- |

## [◆ ](#a09b28d129d4935e1ac79010ad2ed845c)SEG\_TYPE\_TASK\_GATE

| #define SEG\_TYPE\_TASK\_GATE   0x5 |
| --- |

## [◆ ](#a24ba226f5d7c4a2d0e73d129b811d009)SEG\_TYPE\_TRAP\_GATE

| #define SEG\_TYPE\_TRAP\_GATE   0xF |
| --- |

## [◆ ](#a9526fd354b043f1d989133fb51584ca5)SEG\_TYPE\_TSS

| #define SEG\_TYPE\_TSS   0x9 |
| --- |

## [◆ ](#a358e9557d55f44b1e0c48f56e9bb8eb8)SEG\_TYPE\_TSS\_BUSY

| #define SEG\_TYPE\_TSS\_BUSY   0xB |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [segmentation.h](segmentation_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
