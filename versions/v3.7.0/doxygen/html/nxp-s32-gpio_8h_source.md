---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nxp-s32-gpio_8h_source.html
original_path: doxygen/html/nxp-s32-gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-s32-gpio.h

[Go to the documentation of this file.](nxp-s32-gpio_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_S32\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_S32\_GPIO\_H\_

8

20

22#define NXP\_S32\_GPIO\_INT\_CONTROLLER\_POS 8

23#define NXP\_S32\_GPIO\_INT\_CONTROLLER\_MASK (0x1U << NXP\_S32\_GPIO\_INT\_CONTROLLER\_POS)

25

31

[ 33](nxp-s32-gpio_8h.md#a2e1b254b390cdd2ca038ff4e930680f5)#define NXP\_S32\_GPIO\_INT\_WKPU (0x1U << NXP\_S32\_GPIO\_INT\_CONTROLLER\_POS)

34

36

38

39#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NXP\_S32\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nxp-s32-gpio.h](nxp-s32-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
