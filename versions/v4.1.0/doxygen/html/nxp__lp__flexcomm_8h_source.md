---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp__lp__flexcomm_8h_source.html
original_path: doxygen/html/nxp__lp__flexcomm_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_lp\_flexcomm.h

[Go to the documentation of this file.](nxp__lp__flexcomm_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_DRIVERS\_NXP\_LP\_FLEXCOMM\_H\_

7#define ZEPHYR\_DRIVERS\_NXP\_LP\_FLEXCOMM\_H\_

8

9#include "fsl\_lpflexcomm.h"

10

[ 11](nxp__lp__flexcomm_8h.md#af38501b5aa1350ebc2c03be9b6623353)typedef void (\*[child\_isr\_t](nxp__lp__flexcomm_8h.md#af38501b5aa1350ebc2c03be9b6623353))(const struct [device](structdevice.md) \*dev);

12

[ 13](nxp__lp__flexcomm_8h.md#a259055f21461b4dead75cdec3243719e)void [nxp\_lp\_flexcomm\_setirqhandler](nxp__lp__flexcomm_8h.md#a259055f21461b4dead75cdec3243719e)(const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*child\_dev,

14 LP\_FLEXCOMM\_PERIPH\_T periph, [child\_isr\_t](nxp__lp__flexcomm_8h.md#af38501b5aa1350ebc2c03be9b6623353) handler);

15

16#endif /\* ZEPHYR\_DRIVERS\_NXP\_LP\_FLEXCOMM\_H\_ \*/

[nxp\_lp\_flexcomm\_setirqhandler](nxp__lp__flexcomm_8h.md#a259055f21461b4dead75cdec3243719e)

void nxp\_lp\_flexcomm\_setirqhandler(const struct device \*dev, const struct device \*child\_dev, LP\_FLEXCOMM\_PERIPH\_T periph, child\_isr\_t handler)

[child\_isr\_t](nxp__lp__flexcomm_8h.md#af38501b5aa1350ebc2c03be9b6623353)

void(\* child\_isr\_t)(const struct device \*dev)

**Definition** nxp\_lp\_flexcomm.h:11

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [nxp\_lp\_flexcomm.h](nxp__lp__flexcomm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
