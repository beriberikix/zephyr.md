---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas-ra-gpio-ioport_8h_source.html
original_path: doxygen/html/renesas-ra-gpio-ioport_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-ra-gpio-ioport.h

[Go to the documentation of this file.](renesas-ra-gpio-ioport_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RA\_GPIO\_IOPORT\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RA\_GPIO\_IOPORT\_H\_

9

[ 10](renesas-ra-gpio-ioport_8h.md#ad701020b8e65bcf186ab7c9ad8d1e2a6)#define RENESAS\_GPIO\_DS\_POS (8)

[ 11](renesas-ra-gpio-ioport_8h.md#aef3b3d784f238736bba562cb5f7de761)#define RENESAS\_GPIO\_DS\_MSK (0x3U << RENESAS\_GPIO\_DS\_POS)

12/\* GPIO Drive strength \*/

[ 13](renesas-ra-gpio-ioport_8h.md#a63c670eeaf1d139697837d2ee803df07)#define RENESAS\_GPIO\_DS\_LOW (0x0 << RENESAS\_GPIO\_DRIVE\_POS)

[ 14](renesas-ra-gpio-ioport_8h.md#aac91a54a2a51a66c59cdbd7ba369d1a5)#define RENESAS\_GPIO\_DS\_MIDDLE (0x1 << RENESAS\_GPIO\_DRIVE\_POS)

[ 15](renesas-ra-gpio-ioport_8h.md#add76df360c72847d0e419b9a769b4673)#define RENESAS\_GPIO\_DS\_HIGH\_SPEED\_HIGH\_DRIVE (0x2 << RENESAS\_GPIO\_DRIVE\_POS)

[ 16](renesas-ra-gpio-ioport_8h.md#a3a225686d5fe71a85d3f8d1798433065)#define RENESAS\_GPIO\_DS\_HIGH\_DRIVE (0x3 << RENESAS\_GPIO\_DRIVE\_POS)

17

18#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_RENESAS\_RA\_GPIO\_IOPORT\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-ra-gpio-ioport.h](renesas-ra-gpio-ioport_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
