---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbd__msc_8h.html
original_path: doxygen/html/usbd__msc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_msc.h File Reference

USBD Mass Storage Class public header.
[More...](#details)

`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](usbd__msc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usbd\_msc\_lun](structusbd__msc__lun.md) |

| Macros | |
| --- | --- |
| #define | [USBD\_DEFINE\_MSC\_LUN](#a10b23a57fa6635ad41fb31532d940753)(disk\_name, t10\_vendor, t10\_product, t10\_revision) |

## Detailed Description

USBD Mass Storage Class public header.

Header exposes API for registering LUNs.

## Macro Definition Documentation

## [◆ ](#a10b23a57fa6635ad41fb31532d940753)USBD\_DEFINE\_MSC\_LUN

| #define USBD\_DEFINE\_MSC\_LUN | ( |  | *disk\_name*, |
| --- | --- | --- | --- |
|  |  |  | *t10\_vendor*, |
|  |  |  | *t10\_product*, |
|  |  |  | *t10\_revision* ) |

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([usbd\_msc\_lun](structusbd__msc__lun.md), usbd\_msc\_lun\_##disk\_name) = { \

.disk = [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(disk\_name), \

.vendor = t10\_vendor, \

.product = t10\_product, \

.revision = t10\_revision, \

}

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[usbd\_msc\_lun](structusbd__msc__lun.md)

**Definition** usbd\_msc.h:19

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_msc.h](usbd__msc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
