---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/nxp-imx-igpio_8h_source.html
original_path: doxygen/html/nxp-imx-igpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-imx-igpio.h

[Go to the documentation of this file.](nxp-imx-igpio_8h.md)

1/\*

2 \* Copyright (c) 2025 Feniex Industries Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_IMX\_IGPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_IMX\_IGPIO\_H\_

8

23#define NXP\_IGPIO\_PULL\_STRENGTH\_POS 8

24#define NXP\_IGPIO\_PULL\_STRENGTH\_MASK (0x1U << NXP\_IGPIO\_PULL\_STRENGTH\_POS)

26

[ 28](nxp-imx-igpio_8h.md#a0cdc8d4cade4e2411fa3686a5375a276)#define NXP\_IGPIO\_PULL\_WEAK (0x0U << NXP\_IGPIO\_PULL\_STRENGTH\_POS)

[ 29](nxp-imx-igpio_8h.md#a59c07b2a497ed2f8659d456986cc0702)#define NXP\_IGPIO\_PULL\_STRONG (0x1U << NXP\_IGPIO\_PULL\_STRENGTH\_POS)

30

32

33#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_IMX\_IGPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nxp-imx-igpio.h](nxp-imx-igpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
