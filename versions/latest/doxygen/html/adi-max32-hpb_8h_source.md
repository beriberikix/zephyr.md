---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/adi-max32-hpb_8h_source.html
original_path: doxygen/html/adi-max32-hpb_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adi-max32-hpb.h

[Go to the documentation of this file.](adi-max32-hpb_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_ADI\_MAX32\_HPB\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_ADI\_MAX32\_HPB\_H\_

9

[ 10](adi-max32-hpb_8h.md#a29f8811b2bb98e86f404ef03138f9516)#define ADI\_MAX32\_HPB\_CS\_HIGH\_1\_5 0

[ 11](adi-max32-hpb_8h.md#a78013a485fea4f2a1004ec8971095b20)#define ADI\_MAX32\_HPB\_CS\_HIGH\_2\_5 1

[ 12](adi-max32-hpb_8h.md#a9b089dcef4024bfc56b823b13371a421)#define ADI\_MAX32\_HPB\_CS\_HIGH\_3\_5 2

[ 13](adi-max32-hpb_8h.md#ab76dd0e494deb35a34a531086331f065)#define ADI\_MAX32\_HPB\_CS\_HIGH\_4\_5 3

[ 14](adi-max32-hpb_8h.md#a991dcc311ebb6893b91ad3af474b3967)#define ADI\_MAX32\_HPB\_CS\_HIGH\_5\_5 4

[ 15](adi-max32-hpb_8h.md#acd7a7c048306431eedbd97795ddfa1c5)#define ADI\_MAX32\_HPB\_CS\_HIGH\_6\_5 5

[ 16](adi-max32-hpb_8h.md#ae9d5818cd728567eaa6c4ea1f16bd15e)#define ADI\_MAX32\_HPB\_CS\_HIGH\_7\_5 6

[ 17](adi-max32-hpb_8h.md#a248dfd6ef0cf9f427b2fbf4098423ea6)#define ADI\_MAX32\_HPB\_CS\_HIGH\_8\_5 7

[ 18](adi-max32-hpb_8h.md#a0fdc843a0f7851aa44d4f201df2a9a49)#define ADI\_MAX32\_HPB\_CS\_HIGH\_9\_5 8

[ 19](adi-max32-hpb_8h.md#af8afbddb460005e15e73c3c227c9223b)#define ADI\_MAX32\_HPB\_CS\_HIGH\_10\_5 9

[ 20](adi-max32-hpb_8h.md#a551ae9f52cbafdce83266b02d9ac02d9)#define ADI\_MAX32\_HPB\_CS\_HIGH\_11\_5 10

[ 21](adi-max32-hpb_8h.md#a4b7a7d5b6a25cec055abddcab45e5086)#define ADI\_MAX32\_HPB\_CS\_HIGH\_12\_5 11

[ 22](adi-max32-hpb_8h.md#a0d4d2fd4e92c96fd7b5f2355854f84ff)#define ADI\_MAX32\_HPB\_CS\_HIGH\_13\_5 12

[ 23](adi-max32-hpb_8h.md#a6c8d018e9e498f2383abd9a34c489c1d)#define ADI\_MAX32\_HPB\_CS\_HIGH\_14\_5 13

[ 24](adi-max32-hpb_8h.md#a68e6e4ddc1e7db8b27c5921c4a46ba17)#define ADI\_MAX32\_HPB\_CS\_HIGH\_15\_5 14

[ 25](adi-max32-hpb_8h.md#a112be64bc37cdc17ffb649ef6dd887fe)#define ADI\_MAX32\_HPB\_CS\_HIGH\_16\_5 15

26

[ 27](adi-max32-hpb_8h.md#af27625302dd49bf2d0930dd5edb74274)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_1 0

[ 28](adi-max32-hpb_8h.md#a56a0721aa887fa6933487b85598d58d9)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_2 1

[ 29](adi-max32-hpb_8h.md#af7e5d91af72daad131d91f16d6ea216d)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_3 2

[ 30](adi-max32-hpb_8h.md#acedb7f7f9094e452d1eed7a39d54c152)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_4 3

[ 31](adi-max32-hpb_8h.md#a2acd664c0989a3dee4a206f54a88a981)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_5 4

[ 32](adi-max32-hpb_8h.md#a92d15100cada582907cff46a726fcf89)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_6 5

[ 33](adi-max32-hpb_8h.md#a2760c84c31f5db2774325e4d5068c0fb)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_7 6

[ 34](adi-max32-hpb_8h.md#ab17e595f863b0cbd823756996c2555e8)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_8 7

[ 35](adi-max32-hpb_8h.md#acf481a3e65bc2bcf267a4ed10c82efd8)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_9 8

[ 36](adi-max32-hpb_8h.md#a4e932f1ff4ed17f40b440bd81cd2ef36)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_10 9

[ 37](adi-max32-hpb_8h.md#a9b987ad8248ba9a4149fa5e2c91e38ad)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_11 10

[ 38](adi-max32-hpb_8h.md#ad88c4841f5bbb3657043562242328133)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_12 11

[ 39](adi-max32-hpb_8h.md#ac21f9af20df18a5c2a67362c2f5b94de)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_13 12

[ 40](adi-max32-hpb_8h.md#aecccb097f343e0adfd3a628894333a28)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_14 13

[ 41](adi-max32-hpb_8h.md#aff1191a58754e64cb694e7814d34f6a3)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_15 14

[ 42](adi-max32-hpb_8h.md#a5ecc2938ad6d46ee9767f5cbf8f01786)#define ADI\_MAX32\_HPB\_CS\_SETUP\_HOLD\_16 15

43

[ 44](adi-max32-hpb_8h.md#a3a967815c515fdb1df5a3b9ef71c4f19)#define ADI\_MAX32\_HPB\_LAT\_5 0x0

[ 45](adi-max32-hpb_8h.md#a0560b2c90f206af78b006cfcb61119b8)#define ADI\_MAX32\_HPB\_LAT\_6 0x1

[ 46](adi-max32-hpb_8h.md#a4b7cc63424ad76ff66c3adcec3918e53)#define ADI\_MAX32\_HPB\_LAT\_3 0xE

[ 47](adi-max32-hpb_8h.md#a8375ffba91c4035beb26cdb7626816b0)#define ADI\_MAX32\_HPB\_LAT\_4 0xF

48

[ 49](adi-max32-hpb_8h.md#a776abc308a0492f4ec393112d7328d78)#define ADI\_MAX32\_HPB\_DEV\_TYPE\_HYPER\_FLASH 0

[ 50](adi-max32-hpb_8h.md#a3f2557ed41214d6bc0f62e4dd61ad569)#define ADI\_MAX32\_HPB\_DEV\_TYPE\_XCCELA\_PSRAM 1

[ 51](adi-max32-hpb_8h.md#a888831adc568e5c1e83b88410c1f276a)#define ADI\_MAX32\_HPB\_DEV\_TYPE\_HYPER\_RAM 2

52

53#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_ADI\_MAX32\_HPB\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-controller](dir_35d961eb615f3ea19ec1fece6b4faa4b.md)
- [adi-max32-hpb.h](adi-max32-hpb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
