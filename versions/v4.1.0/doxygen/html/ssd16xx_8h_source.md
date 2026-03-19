---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ssd16xx_8h_source.html
original_path: doxygen/html/ssd16xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ssd16xx.h

[Go to the documentation of this file.](ssd16xx_8h.md)

1/\*

2 \* Copyright (c) 2022 Andreas Sandberg

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DISPLAY\_SSD16XX\_H\_

8#define ZEPHYR\_INCLUDE\_DISPLAY\_SSD16XX\_H\_

9

10#include <[zephyr/drivers/display.h](display_8h.md)>

11

[ 15](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765)enum [ssd16xx\_ram](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765) {

[ 20](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765ae3ae0ce9601034f1030f7114dcfedab0) [SSD16XX\_RAM\_BLACK](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765ae3ae0ce9601034f1030f7114dcfedab0) = 0,

21 /\* The red RAM buffer. This is typically the old frame buffer

22 \* when performing partial refreshes or an additional color

23 \* channel.

24 \*/

[ 25](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765a54fddbd6e9f2207ff228ccfcde65f466) [SSD16XX\_RAM\_RED](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765a54fddbd6e9f2207ff228ccfcde65f466),

26};

27

[ 41](ssd16xx_8h.md#a876bae07401b2ccc3889414706ae4d97)int [ssd16xx\_read\_ram](ssd16xx_8h.md#a876bae07401b2ccc3889414706ae4d97)(const struct [device](structdevice.md) \*dev, enum [ssd16xx\_ram](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765) ram\_type,

42 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

43 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

44 void \*buf);

45

46#endif /\* ZEPHYR\_INCLUDE\_DISPLAY\_SSD16XX\_H\_ \*/

[display.h](display_8h.md)

Public API for display drivers and applications.

[ssd16xx\_read\_ram](ssd16xx_8h.md#a876bae07401b2ccc3889414706ae4d97)

int ssd16xx\_read\_ram(const struct device \*dev, enum ssd16xx\_ram ram\_type, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, void \*buf)

Read data directly from the display controller's internal RAM.

[ssd16xx\_ram](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765)

ssd16xx\_ram

SSD16xx RAM type for direct RAM access.

**Definition** ssd16xx.h:15

[SSD16XX\_RAM\_RED](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765a54fddbd6e9f2207ff228ccfcde65f466)

@ SSD16XX\_RAM\_RED

**Definition** ssd16xx.h:25

[SSD16XX\_RAM\_BLACK](ssd16xx_8h.md#af3596acb60f20fbecef01e82672ea765ae3ae0ce9601034f1030f7114dcfedab0)

@ SSD16XX\_RAM\_BLACK

The black RAM buffer.

**Definition** ssd16xx.h:20

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[display\_buffer\_descriptor](structdisplay__buffer__descriptor.md)

Structure to describe display data buffer layout.

**Definition** display.h:121

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [display](dir_dbe0bbdb2da2eed929c1e8ee8e4a99ef.md)
- [ssd16xx.h](ssd16xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
