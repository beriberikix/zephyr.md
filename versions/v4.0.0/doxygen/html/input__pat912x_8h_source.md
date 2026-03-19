---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/input__pat912x_8h_source.html
original_path: doxygen/html/input__pat912x_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_pat912x.h

[Go to the documentation of this file.](input__pat912x_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INPUT\_PAT912X\_H\_

8#define ZEPHYR\_INCLUDE\_INPUT\_PAT912X\_H\_

9

[ 19](input__pat912x_8h.md#a1c9f11b31312dbaf5cf24ddaaad7eada)int [pat912x\_set\_resolution](input__pat912x_8h.md#a1c9f11b31312dbaf5cf24ddaaad7eada)(const struct [device](structdevice.md) \*dev,

20 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) res\_x\_cpi, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) res\_y\_cpi);

21

22#endif /\* ZEPHYR\_INCLUDE\_INPUT\_PAT912X\_H\_ \*/

[pat912x\_set\_resolution](input__pat912x_8h.md#a1c9f11b31312dbaf5cf24ddaaad7eada)

int pat912x\_set\_resolution(const struct device \*dev, int16\_t res\_x\_cpi, int16\_t res\_y\_cpi)

Set resolution on a pat912x device.

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_pat912x.h](input__pat912x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
