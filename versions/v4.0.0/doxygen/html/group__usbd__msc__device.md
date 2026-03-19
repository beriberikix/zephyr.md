---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__usbd__msc__device.html
original_path: doxygen/html/group__usbd__msc__device.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB Mass Storage Class device API

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

USB Mass Storage Class device API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [USBD\_DEFINE\_MSC\_LUN](#ga7923a2f33e3dd8455f8f47cea08f1752)(id, disk\_name, t10\_vendor, t10\_product, t10\_revision) |
|  | Define USB Mass Storage Class logical unit. |

## Detailed Description

USB Mass Storage Class device API.

Since
:   3.4

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga7923a2f33e3dd8455f8f47cea08f1752)USBD\_DEFINE\_MSC\_LUN

| #define USBD\_DEFINE\_MSC\_LUN | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *disk\_name*, |
|  |  |  | *t10\_vendor*, |
|  |  |  | *t10\_product*, |
|  |  |  | *t10\_revision* ) |

`#include <[usbd_msc.h](usbd__msc_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([usbd\_msc\_lun](structusbd__msc__lun.md), usbd\_msc\_lun\_##id) = { \

.disk = disk\_name, \

.vendor = t10\_vendor, \

.product = t10\_product, \

.revision = t10\_revision, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[usbd\_msc\_lun](structusbd__msc__lun.md)

**Definition** usbd\_msc.h:19

Define USB Mass Storage Class logical unit.

Use this macro to create Logical Unit mapping in USB MSC for selected disk. Up to CONFIG\_USBD\_MSC\_LUNS\_PER\_INSTANCE disks can be registered on single USB MSC instance. Currently only one USB MSC instance is supported.

Parameters
:   | id | Identifier by which the linker sorts registered LUNs |
    | --- | --- |
    | disk\_name | Disk name as used in [Disk Access Interface](group__disk__access__interface.md "Disk Access Interface") |
    | t10\_vendor | T10 Vendor Indetification |
    | t10\_product | T10 Product Identification |
    | t10\_revision | T10 Product Revision Level |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
