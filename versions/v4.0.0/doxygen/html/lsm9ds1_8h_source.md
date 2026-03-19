---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lsm9ds1_8h_source.html
original_path: doxygen/html/lsm9ds1_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lsm9ds1.h

[Go to the documentation of this file.](lsm9ds1_8h.md)

1/\*

2 \* Copyright (c) 2024 Bootlin

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM9DS1\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM9DS1\_H\_

9

10/\* Accel range \*/

[ 11](lsm9ds1_8h.md#aa0f17393c9ff976e0ee0c110ecc72473)#define LSM9DS1\_DT\_FS\_2G 0

[ 12](lsm9ds1_8h.md#a2db5ff66fa97b7b4bb5915843b1bb6f6)#define LSM9DS1\_DT\_FS\_16G 1

[ 13](lsm9ds1_8h.md#a7535ca239218a5e9356c6246b938caaf)#define LSM9DS1\_DT\_FS\_4G 2

[ 14](lsm9ds1_8h.md#a6afa3768fd367db78b1e3f7deac5508e)#define LSM9DS1\_DT\_FS\_8G 3

15

[ 16](lsm9ds1_8h.md#a088dba4db0ddde1687db351ed03b1538)#define LSM9DS1\_DT\_FS\_245DPS 0

[ 17](lsm9ds1_8h.md#a8e32311fa33f06c0003d41fac83d4121)#define LSM9DS1\_DT\_FS\_500DPS 1

[ 18](lsm9ds1_8h.md#aa6a1e7e28d197dd28b2e13a40a521015)#define LSM9DS1\_DT\_FS\_2000DPS 3

19

[ 20](lsm9ds1_8h.md#ab7f0150bb6481d55f759f64f7c502edf)#define LSM9DS1\_IMU\_OFF 0x00

[ 21](lsm9ds1_8h.md#ae897ff93c37f7254c016349cfc48466e)#define LSM9DS1\_GY\_OFF\_XL\_10Hz 0x10

[ 22](lsm9ds1_8h.md#a055b320d6158932562f10ef2d2b96a97)#define LSM9DS1\_GY\_OFF\_XL\_50Hz 0x20

[ 23](lsm9ds1_8h.md#a4d7b97ebeba2cb8007372755021a5de8)#define LSM9DS1\_GY\_OFF\_XL\_119Hz 0x30

[ 24](lsm9ds1_8h.md#aa9db97ee52368cabd1c3ccd7cbd3f1a4)#define LSM9DS1\_GY\_OFF\_XL\_238Hz 0x40

[ 25](lsm9ds1_8h.md#ad3318f2c48533b3822d7c6fafe224373)#define LSM9DS1\_GY\_OFF\_XL\_476Hz 0x50

[ 26](lsm9ds1_8h.md#a086c4d1c8287d40be3437f05f3227db7)#define LSM9DS1\_GY\_OFF\_XL\_952Hz 0x60

[ 27](lsm9ds1_8h.md#a393366ba14c5db7ed1a5ff95a85adae7)#define LSM9DS1\_XL\_OFF\_GY\_14Hz9 0x01

[ 28](lsm9ds1_8h.md#aff981b33a86e8d93268ec9e144c1e761)#define LSM9DS1\_XL\_OFF\_GY\_59Hz5 0x02

[ 29](lsm9ds1_8h.md#afe2f271b51a0ea6cf5ce29f03f761054)#define LSM9DS1\_XL\_OFF\_GY\_119Hz 0x03

[ 30](lsm9ds1_8h.md#aa9d2c6c89ef7bb5d1d543b8bcc39b392)#define LSM9DS1\_XL\_OFF\_GY\_238Hz 0x04

[ 31](lsm9ds1_8h.md#af7af84f2ee96d01fe3f031e5b09217ff)#define LSM9DS1\_XL\_OFF\_GY\_476Hz 0x05

[ 32](lsm9ds1_8h.md#abcb55995e6b3de4aa23dc804b88eb409)#define LSM9DS1\_XL\_OFF\_GY\_952Hz 0x06

[ 33](lsm9ds1_8h.md#af65ec4dc4c5075282380da389b68a77b)#define LSM9DS1\_IMU\_14Hz9 0x11

[ 34](lsm9ds1_8h.md#a571432113f63d003e7c3e242b6509093)#define LSM9DS1\_IMU\_59Hz5 0x22

[ 35](lsm9ds1_8h.md#a71e8c41d54062e315ecd72f933160208)#define LSM9DS1\_IMU\_119Hz 0x33

[ 36](lsm9ds1_8h.md#a3a8b6d1a000a7d4e1fdb6bcc0a70243d)#define LSM9DS1\_IMU\_238Hz 0x44

[ 37](lsm9ds1_8h.md#a5a09b132476058df9906e58d0755386c)#define LSM9DS1\_IMU\_476Hz 0x55

[ 38](lsm9ds1_8h.md#a5fe83cf26a6024edeb2ff759ee20d3c8)#define LSM9DS1\_IMU\_952Hz 0x66

[ 39](lsm9ds1_8h.md#a6bbd0b822cc47491d6048f7d71478c9b)#define LSM9DS1\_XL\_OFF\_GY\_14Hz9\_LP 0x81

[ 40](lsm9ds1_8h.md#aca3c0f2e322a39f56fa9a5fa70497df6)#define LSM9DS1\_XL\_OFF\_GY\_59Hz5\_LP 0x82

[ 41](lsm9ds1_8h.md#a98e7b9e3924622147f73be90f00bd1ba)#define LSM9DS1\_XL\_OFF\_GY\_119Hz\_LP 0x83

[ 42](lsm9ds1_8h.md#a61e50f3183b7541a81fe2907752f7375)#define LSM9DS1\_IMU\_14Hz9\_LP 0x91

[ 43](lsm9ds1_8h.md#a5b991524e1cec97295c9a1bfdcf31708)#define LSM9DS1\_IMU\_59Hz5\_LP 0xA2

[ 44](lsm9ds1_8h.md#a20088ff32a83f6a368d36ae138629452)#define LSM9DS1\_IMU\_119Hz\_LP 0xB3

45

46#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM9DS1\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm9ds1.h](lsm9ds1_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
