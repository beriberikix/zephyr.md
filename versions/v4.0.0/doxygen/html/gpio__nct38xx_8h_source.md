---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gpio__nct38xx_8h_source.html
original_path: doxygen/html/gpio__nct38xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_nct38xx.h

[Go to the documentation of this file.](gpio__nct38xx_8h.md)

1/\*

2 \* Copyright (c) 2021 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_NCT38XX\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_NCT38XX\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 19](gpio__nct38xx_8h.md#a05e658cb957b13402371054aa9f59302)void [nct38xx\_gpio\_alert\_handler](gpio__nct38xx_8h.md#a05e658cb957b13402371054aa9f59302)(const struct [device](structdevice.md) \*dev);

20

21#ifdef \_\_cplusplus

22}

23#endif

24

25#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_NCT38XX\_H\_ \*/

[nct38xx\_gpio\_alert\_handler](gpio__nct38xx_8h.md#a05e658cb957b13402371054aa9f59302)

void nct38xx\_gpio\_alert\_handler(const struct device \*dev)

Dispatch all GPIO ports ISR in the NCT38XX device.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_nct38xx.h](gpio__nct38xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
