---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvideo__ctrl__range.html
original_path: doxygen/html/structvideo__ctrl__range.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_ctrl\_range Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Controls](group__video__controls.md)

`#include <[zephyr/drivers/video-controls.h](video-controls_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [min](#a0814e901d0edfcfa8be5419eb5bf063e) |  |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)   [min64](#a25e816ab3403881ea1b0db70fbe736f1) |  |
| }; |  |
|  | control minimum value, inclusive |
| union { |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [max](#a3c2108ece802872716abf1672ccde5fa) |  |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)   [max64](#a7acb36bff57836f7bffd3ccbb2e4691e) |  |
| }; |  |
|  | control maximum value, inclusive |
| union { |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [step](#ab1ca560d28446134189cd7d585bd146a) |  |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)   [step64](#a9912a5060e6615388b5c8f013eaa3c51) |  |
| }; |  |
|  | control value step |
| union { |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [def](#ac41aad65e524036c1f01f164726dc209) |  |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)   [def64](#a9f339e7fce8f61b939d68421169a7030) |  |
| }; |  |
|  | control default value for VIDEO\_CTRL\_TYPE\_INTEGER, \_BOOLEAN, \_MENU or \_INTEGER\_MENU, not valid for other types |

## Field Documentation

## [◆ ](#a80da7a3fd565e24c3d9b78c71d3428f9)[union]

| union { ... } [video\_ctrl\_range](structvideo__ctrl__range.md) |
| --- |

control default value for VIDEO\_CTRL\_TYPE\_INTEGER, \_BOOLEAN, \_MENU or \_INTEGER\_MENU, not valid for other types

## [◆ ](#a435797587c2da64340f15477dec00204)[union]

| union { ... } [video\_ctrl\_range](structvideo__ctrl__range.md) |
| --- |

control maximum value, inclusive

## [◆ ](#a6b786db095604200e72489662d0f11c7)[union]

| union { ... } [video\_ctrl\_range](structvideo__ctrl__range.md) |
| --- |

control minimum value, inclusive

## [◆ ](#afc9ca7cde863e773f3f9a150cf70854d)[union]

| union { ... } [video\_ctrl\_range](structvideo__ctrl__range.md) |
| --- |

control value step

## [◆ ](#ac41aad65e524036c1f01f164726dc209)def

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) video\_ctrl\_range::def |
| --- |

## [◆ ](#a9f339e7fce8f61b939d68421169a7030)def64

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) video\_ctrl\_range::def64 |
| --- |

## [◆ ](#a3c2108ece802872716abf1672ccde5fa)max

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) video\_ctrl\_range::max |
| --- |

## [◆ ](#a7acb36bff57836f7bffd3ccbb2e4691e)max64

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) video\_ctrl\_range::max64 |
| --- |

## [◆ ](#a0814e901d0edfcfa8be5419eb5bf063e)min

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) video\_ctrl\_range::min |
| --- |

## [◆ ](#a25e816ab3403881ea1b0db70fbe736f1)min64

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) video\_ctrl\_range::min64 |
| --- |

## [◆ ](#ab1ca560d28446134189cd7d585bd146a)step

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) video\_ctrl\_range::step |
| --- |

## [◆ ](#a9912a5060e6615388b5c8f013eaa3c51)step64

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) video\_ctrl\_range::step64 |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video-controls.h](video-controls_8h_source.md)

- [video\_ctrl\_range](structvideo__ctrl__range.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
