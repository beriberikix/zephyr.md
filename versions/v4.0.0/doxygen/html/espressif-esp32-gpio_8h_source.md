---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/espressif-esp32-gpio_8h_source.html
original_path: doxygen/html/espressif-esp32-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espressif-esp32-gpio.h

[Go to the documentation of this file.](espressif-esp32-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ESPRESSIF\_ESP32\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ESPRESSIF\_ESP32\_GPIO\_H\_

8

23#define ESP32\_GPIO\_DS\_POS 9

24#define ESP32\_GPIO\_DS\_MASK (0x3U << ESP32\_GPIO\_DS\_POS)

26

[ 28](espressif-esp32-gpio_8h.md#adbe5a19bf5ce3d57e5e8fe592022cefb)#define ESP32\_GPIO\_DS\_DFLT (0x0U << ESP32\_GPIO\_DS\_POS)

29

[ 31](espressif-esp32-gpio_8h.md#a20175204db3e520b54ceeafb5029db0c)#define ESP32\_GPIO\_DS\_ALT (0x3U << ESP32\_GPIO\_DS\_POS)

32

34

35#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ESPRESSIF\_ESP32\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [espressif-esp32-gpio.h](espressif-esp32-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
