---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h_source.html
original_path: doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

it8xxx2\_vcmp.h

[Go to the documentation of this file.](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md)

1/\*

2 \* Copyright (c) 2022 ITE Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_IT8XXX2\_VCMP\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_IT8XXX2\_VCMP\_H\_

8

13

[ 14](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a04c6b4af3a7fa2c266f9bc4cf8f580f8)#define VCMP\_CHANNEL\_0 0

[ 15](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#ab284eddb8412223f865380f69311884c)#define VCMP\_CHANNEL\_1 1

[ 16](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#abf666272da5df739c38349f8dc0673d7)#define VCMP\_CHANNEL\_2 2

[ 17](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#aad5d65c9659dedf702b54d8a7d3857ea)#define VCMP\_CHANNEL\_3 3

[ 18](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a3148e4a63af5791c0d88e3ede54c1443)#define VCMP\_CHANNEL\_4 4

[ 19](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a1460631599e37050e844032297578d2c)#define VCMP\_CHANNEL\_5 5

[ 20](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#ad7d3ef8e2a0157c43c68ef12f02b6181)#define VCMP\_CHANNEL\_CNT 6

21

23

28

[ 29](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#afee8d841314119709484eeb1a7919fc4)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_100US 0x10

[ 30](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#ac22de93d09665b40b736f638bb106143)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_200US 0x20

[ 31](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#ac4cd52baa765f7f9e148f49e3a5eb137)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_400US 0x30

[ 32](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a3e98391265d430652e996798979d6e32)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_600US 0x40

[ 33](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#ace0bbf4e49fe2e939926c8973b1d9e6c)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_800US 0x50

[ 34](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#add00ffb6d51398fb9207d9709d35f294)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_1MS 0x60

[ 35](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a1aa53f56577acc7cbd34f9f37d166e7c)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_1\_5MS 0x70

[ 36](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a012e4fcc993d9aed16203e1cdbbeca05)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_2MS 0x80

[ 37](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#aa702079843ff113a79589c6daca88587)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_2\_5MS 0x90

[ 38](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#aad950cc6bec74a685ec3d37f451e1a10)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_3MS 0xa0

[ 39](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a4f296f81c2a751d53977abf2aff5d6dd)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_4MS 0xb0

[ 40](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a7c31ca003dc472e5e567c6274f62dceb)#define IT8XXX2\_VCMP\_SCAN\_PERIOD\_5MS 0xc0

41

43

48

[ 49](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a46e65d3ca651e9a75d90d0d456e6bc28)#define IT8XXX2\_VCMP\_LESS\_OR\_EQUAL 0

[ 50](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#a2f1ccc3b8b3d0ff5b1fab7d401adb2c7)#define IT8XXX2\_VCMP\_GREATER 1

[ 51](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md#ac54b4d008105b4d2ad956cf076c29acc)#define IT8XXX2\_VCMP\_UNDEFINED 0xffff

52

54#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_SENSOR\_IT8XXX2\_VCMP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [it8xxx2\_vcmp.h](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
