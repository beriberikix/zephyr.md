---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nordic-npm6001-gpio_8h_source.html
original_path: doxygen/html/nordic-npm6001-gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nordic-npm6001-gpio.h

[Go to the documentation of this file.](nordic-npm6001-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM6001\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM6001\_GPIO\_H\_

8

22

28

31#define NPM6001\_GPIO\_DRIVE\_MSK 0x0100U

33

[ 35](group__gpio__interface__npm6001.md#gaa127d582ea7095b4d7a435ee5ea427c9)#define NPM6001\_GPIO\_DRIVE\_NORMAL (0U << 8U)

[ 37](group__gpio__interface__npm6001.md#ga097b6c75d981ad5ecf38a2133d076178)#define NPM6001\_GPIO\_DRIVE\_HIGH (1U << 8U)

38

40

46

49#define NPM6001\_GPIO\_SENSE\_MSK 0x0200U

51

[ 53](group__gpio__interface__npm6001.md#ga3cde51b59da0f8bf4693ef18b9ee8a30)#define NPM6001\_GPIO\_SENSE\_SCHMITT (0U << 9U)

[ 55](group__gpio__interface__npm6001.md#ga98c66bc1cf5a8c0f83b82c830a817fa2)#define NPM6001\_GPIO\_SENSE\_CMOS (1U << 9U)

56

58

60

61#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NRF\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nordic-npm6001-gpio.h](nordic-npm6001-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
