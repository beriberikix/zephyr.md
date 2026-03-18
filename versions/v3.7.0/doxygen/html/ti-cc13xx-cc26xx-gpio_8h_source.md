---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ti-cc13xx-cc26xx-gpio_8h_source.html
original_path: doxygen/html/ti-cc13xx-cc26xx-gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti-cc13xx-cc26xx-gpio.h

[Go to the documentation of this file.](ti-cc13xx-cc26xx-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_TI\_CC13XX\_CC26XX\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_TI\_CC13XX\_CC26XX\_GPIO\_H\_

8

[ 16](ti-cc13xx-cc26xx-gpio_8h.md#a7fd876bbceee04263d760146333d3b56)#define CC13XX\_CC26XX\_GPIO\_DEBOUNCE (1U << 8)

17

32#define CC13XX\_CC26XX\_GPIO\_DS\_POS 9

33#define CC13XX\_CC26XX\_GPIO\_DS\_MASK (0x3U << CC13XX\_CC26XX\_GPIO\_DS\_POS)

35

[ 37](ti-cc13xx-cc26xx-gpio_8h.md#a038b78d724a2344c100e99ef66fa4613)#define CC13XX\_CC26XX\_GPIO\_DS\_DFLT (0x0U << CC13XX\_CC26XX\_GPIO\_DS\_POS)

38

[ 40](ti-cc13xx-cc26xx-gpio_8h.md#a287f8063ecbc0672818d7b813b37e855)#define CC13XX\_CC26XX\_GPIO\_DS\_ALT (0x3U << CC13XX\_CC26XX\_GPIO\_DS\_POS)

41

43

44#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_TI\_CC13XX\_CC26XX\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [ti-cc13xx-cc26xx-gpio.h](ti-cc13xx-cc26xx-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
