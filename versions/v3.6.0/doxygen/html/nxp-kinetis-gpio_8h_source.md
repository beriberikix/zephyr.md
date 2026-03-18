---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nxp-kinetis-gpio_8h_source.html
original_path: doxygen/html/nxp-kinetis-gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-kinetis-gpio.h

[Go to the documentation of this file.](nxp-kinetis-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_KINETIS\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_KINETIS\_GPIO\_H\_

8

23#define KINETIS\_GPIO\_DS\_POS 9

24#define KINETIS\_GPIO\_DS\_MASK (0x3U << KINETIS\_GPIO\_DS\_POS)

26

[ 28](nxp-kinetis-gpio_8h.md#afc2673bf88bc72dda4effbf1d9d0015a)#define KINETIS\_GPIO\_DS\_DFLT (0x0U << KINETIS\_GPIO\_DS\_POS)

29

[ 31](nxp-kinetis-gpio_8h.md#a1c4baa298474c0cdc731c4a5cf9f0364)#define KINETIS\_GPIO\_DS\_ALT (0x3U << KINETIS\_GPIO\_DS\_POS)

32

34

35#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_KINETIS\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nxp-kinetis-gpio.h](nxp-kinetis-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
