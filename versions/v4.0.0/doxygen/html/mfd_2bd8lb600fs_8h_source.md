---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mfd_2bd8lb600fs_8h_source.html
original_path: doxygen/html/mfd_2bd8lb600fs_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bd8lb600fs.h

[Go to the documentation of this file.](mfd_2bd8lb600fs_8h.md)

1/\*

2 \* Copyright (c) 2024 SILA Embedded Solutions GmbH

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_BD8LB600FS\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_BD8LB600FS\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13#include <[zephyr/device.h](device_8h.md)>

14

20

[ 29](group__mdf__interface__bd8lb600fs.md#gaf155a458b77540f991d53c0827fad5cd)int [mfd\_bd8lb600fs\_set\_outputs](group__mdf__interface__bd8lb600fs.md#gaf155a458b77540f991d53c0827fad5cd)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) values);

[ 49](group__mdf__interface__bd8lb600fs.md#ga478f99d83f78a0ec0fcabeb3103df015)int [mfd\_bd8lb600fs\_get\_output\_diagnostics](group__mdf__interface__bd8lb600fs.md#ga478f99d83f78a0ec0fcabeb3103df015)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*old,

50 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ocp\_or\_tsd);

51

55

56#ifdef \_\_cplusplus

57}

58#endif

59

60#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_BD8LB600FS\_H\_ \*/

[device.h](device_8h.md)

[mfd\_bd8lb600fs\_get\_output\_diagnostics](group__mdf__interface__bd8lb600fs.md#ga478f99d83f78a0ec0fcabeb3103df015)

int mfd\_bd8lb600fs\_get\_output\_diagnostics(const struct device \*dev, uint32\_t \*old, uint32\_t \*ocp\_or\_tsd)

get output diagnostics

[mfd\_bd8lb600fs\_set\_outputs](group__mdf__interface__bd8lb600fs.md#gaf155a458b77540f991d53c0827fad5cd)

int mfd\_bd8lb600fs\_set\_outputs(const struct device \*dev, uint32\_t values)

set outputs

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [bd8lb600fs.h](mfd_2bd8lb600fs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
