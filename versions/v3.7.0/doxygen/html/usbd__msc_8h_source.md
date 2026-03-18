---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/usbd__msc_8h_source.html
original_path: doxygen/html/usbd__msc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_msc.h

[Go to the documentation of this file.](usbd__msc_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

15

16#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_MSC\_H\_

17#define ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_MSC\_H\_

18

[ 19](structusbd__msc__lun.md)struct [usbd\_msc\_lun](structusbd__msc__lun.md) {

[ 20](structusbd__msc__lun.md#a20c6b15b6ac9c09e1aa4369dd477ebba) const char \*[disk](structusbd__msc__lun.md#a20c6b15b6ac9c09e1aa4369dd477ebba);

[ 21](structusbd__msc__lun.md#a13325438f09bff0d3070e5614b736bed) const char \*[vendor](structusbd__msc__lun.md#a13325438f09bff0d3070e5614b736bed);

[ 22](structusbd__msc__lun.md#a9cb7ba0f92f36944585eac23ed283ab6) const char \*[product](structusbd__msc__lun.md#a9cb7ba0f92f36944585eac23ed283ab6);

[ 23](structusbd__msc__lun.md#a94eb2dc151b476e733aea388255e198d) const char \*[revision](structusbd__msc__lun.md#a94eb2dc151b476e733aea388255e198d);

24};

25

32

[ 45](group__usbd__msc__device.md#ga10b23a57fa6635ad41fb31532d940753)#define USBD\_DEFINE\_MSC\_LUN(disk\_name, t10\_vendor, t10\_product, t10\_revision) \

46 STRUCT\_SECTION\_ITERABLE(usbd\_msc\_lun, usbd\_msc\_lun\_##disk\_name) = { \

47 .disk = STRINGIFY(disk\_name), \

48 .vendor = t10\_vendor, \

49 .product = t10\_product, \

50 .revision = t10\_revision, \

51 }

52

56

57#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_MSC\_H\_ \*/

[usbd\_msc\_lun](structusbd__msc__lun.md)

**Definition** usbd\_msc.h:19

[usbd\_msc\_lun::vendor](structusbd__msc__lun.md#a13325438f09bff0d3070e5614b736bed)

const char \* vendor

**Definition** usbd\_msc.h:21

[usbd\_msc\_lun::disk](structusbd__msc__lun.md#a20c6b15b6ac9c09e1aa4369dd477ebba)

const char \* disk

**Definition** usbd\_msc.h:20

[usbd\_msc\_lun::revision](structusbd__msc__lun.md#a94eb2dc151b476e733aea388255e198d)

const char \* revision

**Definition** usbd\_msc.h:23

[usbd\_msc\_lun::product](structusbd__msc__lun.md#a9cb7ba0f92f36944585eac23ed283ab6)

const char \* product

**Definition** usbd\_msc.h:22

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_msc.h](usbd__msc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
