---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pinctrl__esp32__common_8h_source.html
original_path: doxygen/html/pinctrl__esp32__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_esp32\_common.h

[Go to the documentation of this file.](pinctrl__esp32__common_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_ESP32\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_ESP32\_COMMON\_H\_

9

[ 10](pinctrl__esp32__common_8h.md#a2126dde6e9ab7d1a67fb1c4cc66f03a0)#define ESP32\_PORT\_IDX(\_pin) \

11 (((\_pin) < 32) ? 0 : 1)

12

[ 13](pinctrl__esp32__common_8h.md#a38701de31ad20d7bf76c619ec7c42649)#define ESP32\_PIN\_NUM(\_mux) \

14 (((\_mux) >> ESP32\_PIN\_NUM\_SHIFT) & ESP32\_PIN\_NUM\_MASK)

15

[ 16](pinctrl__esp32__common_8h.md#a1e12a6dec8edef8d13d02d57b1af2be8)#define ESP32\_PIN\_SIGI(\_mux) \

17 (((\_mux) >> ESP32\_PIN\_SIGI\_SHIFT) & ESP32\_PIN\_SIGI\_MASK)

18

[ 19](pinctrl__esp32__common_8h.md#a51eba3c904687c6ca113f83623498357)#define ESP32\_PIN\_SIGO(\_mux) \

20 (((\_mux) >> ESP32\_PIN\_SIGO\_SHIFT) & ESP32\_PIN\_SIGO\_MASK)

21

[ 22](pinctrl__esp32__common_8h.md#acce125cecd6af2debe225c2127188e62)#define ESP32\_PIN\_BIAS(\_cfg) \

23 (((\_cfg) >> ESP32\_PIN\_BIAS\_SHIFT) & ESP32\_PIN\_BIAS\_MASK)

24

[ 25](pinctrl__esp32__common_8h.md#a11ee4c4491be52a383c773be7631769d)#define ESP32\_PIN\_DRV(\_cfg) \

26 (((\_cfg) >> ESP32\_PIN\_DRV\_SHIFT) & ESP32\_PIN\_DRV\_MASK)

27

[ 28](pinctrl__esp32__common_8h.md#a0e05c5abc28558d0a351f661f5c37d09)#define ESP32\_PIN\_MODE\_OUT(\_cfg) \

29 (((\_cfg) >> ESP32\_PIN\_OUT\_SHIFT) & ESP32\_PIN\_OUT\_MASK)

30

[ 31](pinctrl__esp32__common_8h.md#a2283009110fe8c4eb6fe2855c2bb3451)#define ESP32\_PIN\_EN\_DIR(\_cfg) \

32 (((\_cfg) >> ESP32\_PIN\_EN\_DIR\_SHIFT) & ESP32\_PIN\_EN\_DIR\_MASK)

33

34#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_ESP32\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_esp32\_common.h](pinctrl__esp32__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
