---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nordic-npm2100-gpio_8h_source.html
original_path: doxygen/html/nordic-npm2100-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nordic-npm2100-gpio.h

[Go to the documentation of this file.](nordic-npm2100-gpio_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM2100\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM2100\_GPIO\_H\_

8

22

28

31#define NPM2100\_GPIO\_DRIVE\_MSK 0x0100U

33

[ 35](group__gpio__interface__npm2100.md#gaaba391246c0041ce40cf9a9826cc2dbd)#define NPM2100\_GPIO\_DRIVE\_NORMAL (0U << 8U)

[ 37](group__gpio__interface__npm2100.md#ga281cd37a16ba12b56850ea98d9b543d5)#define NPM2100\_GPIO\_DRIVE\_HIGH (1U << 8U)

38

40

46

49#define NPM2100\_GPIO\_DEBOUNCE\_MSK 0x0200U

51

[ 53](group__gpio__interface__npm2100.md#ga79471e04dd5ed29a8a819403ab6d83d0)#define NPM2100\_GPIO\_DEBOUNCE\_OFF (0U << 9U)

[ 55](group__gpio__interface__npm2100.md#ga4b1336ed15dc7ed906d1aa69fddff33d)#define NPM2100\_GPIO\_DEBOUNCE\_ON (1U << 9U)

56

58

60

61#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM2100\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nordic-npm2100-gpio.h](nordic-npm2100-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
