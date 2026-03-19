---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/esp32-touch-sensor-input_8h_source.html
original_path: doxygen/html/esp32-touch-sensor-input_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32-touch-sensor-input.h

[Go to the documentation of this file.](esp32-touch-sensor-input_8h.md)

1/\*

2 \* Copyright (c) 2023 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_ESP32\_TOUCH\_SENSOR\_INPUT\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_ESP32\_TOUCH\_SENSOR\_INPUT\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

12/\* Touch sensor IIR filter mode \*/

[ 13](esp32-touch-sensor-input_8h.md#ae2a0cd54094572c8656231a5838cb66a)#define ESP32\_TOUCH\_FILTER\_MODE\_IIR\_4 0

[ 14](esp32-touch-sensor-input_8h.md#aaa4e199eb00344994a8f1545122bec4f)#define ESP32\_TOUCH\_FILTER\_MODE\_IIR\_8 1

[ 15](esp32-touch-sensor-input_8h.md#a2d049eb351a0d74411c267495a838c43)#define ESP32\_TOUCH\_FILTER\_MODE\_IIR\_16 2

[ 16](esp32-touch-sensor-input_8h.md#a734fd0678fa616ba49888e073ce2867e)#define ESP32\_TOUCH\_FILTER\_MODE\_IIR\_32 3

[ 17](esp32-touch-sensor-input_8h.md#a79399dd378771854335172d42bec75ff)#define ESP32\_TOUCH\_FILTER\_MODE\_IIR\_64 4

[ 18](esp32-touch-sensor-input_8h.md#a34af295d6874b7a48bea0a33b775bf5b)#define ESP32\_TOUCH\_FILTER\_MODE\_IIR\_128 5

[ 19](esp32-touch-sensor-input_8h.md#af80cda7abfcf1d87383b0857eb3d2b7d)#define ESP32\_TOUCH\_FILTER\_MODE\_IIR\_256 6

[ 20](esp32-touch-sensor-input_8h.md#a0191397c82bd5b2e178b39192d197a5a)#define ESP32\_TOUCH\_FILTER\_MODE\_JITTER 7

21

22/\* Touch sensor level of filter noise threshold coefficient\*/

[ 23](esp32-touch-sensor-input_8h.md#ab7600d5876774079f3ed910eccdecfef)#define ESP32\_TOUCH\_FILTER\_NOISE\_THR\_4\_8TH 0

[ 24](esp32-touch-sensor-input_8h.md#a69c5b8f22ee5c81d4994690f2d033dac)#define ESP32\_TOUCH\_FILTER\_NOISE\_THR\_3\_8TH 1

[ 25](esp32-touch-sensor-input_8h.md#a9b9e8a6dc207ce34f2feecb833e272a4)#define ESP32\_TOUCH\_FILTER\_NOISE\_THR\_2\_8TH 2

[ 26](esp32-touch-sensor-input_8h.md#ac2d469b684700c9936ffb60da244d124)#define ESP32\_TOUCH\_FILTER\_NOISE\_THR\_8\_8TH 3

27

28/\* Touch sensor level of filter applied on the original data \*/

[ 29](esp32-touch-sensor-input_8h.md#a800b1f8f2f1c7b6e0dc10b8421487b91)#define ESP32\_TOUCH\_FILTER\_SMOOTH\_MODE\_OFF 0

[ 30](esp32-touch-sensor-input_8h.md#a708831f2ca6d7bbf92dda0903aa9eab7)#define ESP32\_TOUCH\_FILTER\_SMOOTH\_MODE\_IIR\_2 1

[ 31](esp32-touch-sensor-input_8h.md#aadcde8afbbb880f9ae297cfe01d437bd)#define ESP32\_TOUCH\_FILTER\_SMOOTH\_MODE\_IIR\_4 2

[ 32](esp32-touch-sensor-input_8h.md#a11620309c1ce775346fa6eb9c6ac4c77)#define ESP32\_TOUCH\_FILTER\_SMOOTH\_MODE\_IIR\_8 3

33

34#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INPUT\_ESP32\_TOUCH\_SENSOR\_INPUT\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [input](dir_ab844d62c7a22d129cc80e6c359d2c21.md)
- [esp32-touch-sensor-input.h](esp32-touch-sensor-input_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
