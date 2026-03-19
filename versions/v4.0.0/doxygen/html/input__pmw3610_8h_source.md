---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/input__pmw3610_8h_source.html
original_path: doxygen/html/input__pmw3610_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_pmw3610.h

[Go to the documentation of this file.](input__pmw3610_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INPUT\_PMW3610\_H\_

8#define ZEPHYR\_INCLUDE\_INPUT\_PMW3610\_H\_

9

[ 16](input__pmw3610_8h.md#a7c20acd4c9ed5b1e16ebc2e093119e0b)int [pmw3610\_set\_resolution](input__pmw3610_8h.md#a7c20acd4c9ed5b1e16ebc2e093119e0b)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_cpi);

17

[ 24](input__pmw3610_8h.md#aa70dd183377503db716ec6277dade83a)int [pmw3610\_force\_awake](input__pmw3610_8h.md#aa70dd183377503db716ec6277dade83a)(const struct [device](structdevice.md) \*dev, bool enable);

25

26#endif /\* ZEPHYR\_INCLUDE\_INPUT\_PMW3610\_H\_ \*/

[pmw3610\_set\_resolution](input__pmw3610_8h.md#a7c20acd4c9ed5b1e16ebc2e093119e0b)

int pmw3610\_set\_resolution(const struct device \*dev, uint16\_t res\_cpi)

Set resolution on a pmw3610 device.

[pmw3610\_force\_awake](input__pmw3610_8h.md#aa70dd183377503db716ec6277dade83a)

int pmw3610\_force\_awake(const struct device \*dev, bool enable)

Set force awake mode on a pmw3610 device.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_pmw3610.h](input__pmw3610_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
