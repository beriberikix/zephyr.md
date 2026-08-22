---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/lsm9ds1_8h_source.html
original_path: doxygen/html/lsm9ds1_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

46/\* magnetometer \*/

47

[ 48](lsm9ds1_8h.md#aa268b28f8b86b3cef6a82e38609160c9)#define LSM9DS1\_DT\_FS\_4Ga 0

[ 49](lsm9ds1_8h.md#a3106e0cabbb21625faf2af9ae8250262)#define LSM9DS1\_DT\_FS\_8Ga 1

[ 50](lsm9ds1_8h.md#a539af8febdf954010ef673afe2c5ee73)#define LSM9DS1\_DT\_FS\_12Ga 2

[ 51](lsm9ds1_8h.md#acf7c7ab63f7255bac3bebc1f4dc007f3)#define LSM9DS1\_DT\_FS\_16Ga 3

52

[ 53](lsm9ds1_8h.md#a7963c9a3003168a8a52dce50054bc96f)#define LSM9DS1\_MAG\_POWER\_DOWN 0xC0

[ 54](lsm9ds1_8h.md#a002a92d8c6cf9ba80d80033e972645ef)#define LSM9DS1\_MAG\_LP\_0Hz625 0x00

[ 55](lsm9ds1_8h.md#a13f527ae76cb0677f94968496d530a13)#define LSM9DS1\_MAG\_LP\_1Hz25 0x01

[ 56](lsm9ds1_8h.md#a758b8866ffcd4c654ab457e1f0521d09)#define LSM9DS1\_MAG\_LP\_2Hz5 0x02

[ 57](lsm9ds1_8h.md#a30dcf54cd4be8c55dac82932ad7a37b2)#define LSM9DS1\_MAG\_LP\_5Hz 0x03

[ 58](lsm9ds1_8h.md#a9ef4b743a50dfd2b1d5db86bc6495644)#define LSM9DS1\_MAG\_LP\_10Hz 0x04

[ 59](lsm9ds1_8h.md#a4e575f4fb5326777f50531556d1353a3)#define LSM9DS1\_MAG\_LP\_20Hz 0x05

[ 60](lsm9ds1_8h.md#a0b4eaacf63176e5231f137ab0ce56d99)#define LSM9DS1\_MAG\_LP\_40Hz 0x06

[ 61](lsm9ds1_8h.md#a724fade6479c4f729dec15448df15e97)#define LSM9DS1\_MAG\_LP\_80Hz 0x07

[ 62](lsm9ds1_8h.md#a6d6e2f72b0dc4aa6bcd5d15842f65e7f)#define LSM9DS1\_MAG\_MP\_0Hz625 0x10

[ 63](lsm9ds1_8h.md#aafe3cfba4bc8cbc7e74e3410aefaea17)#define LSM9DS1\_MAG\_MP\_1Hz25 0x11

[ 64](lsm9ds1_8h.md#a106068e9984c230a9044b5c1dca25fa5)#define LSM9DS1\_MAG\_MP\_2Hz5 0x12

[ 65](lsm9ds1_8h.md#a6ba7628e2ee8564d8fab308eb2a3eef4)#define LSM9DS1\_MAG\_MP\_5Hz 0x13

[ 66](lsm9ds1_8h.md#aab920f8d82ff7795dc155482d5c25814)#define LSM9DS1\_MAG\_MP\_10Hz 0x14

[ 67](lsm9ds1_8h.md#a2fefcffec0ca84714c22930bf571cb59)#define LSM9DS1\_MAG\_MP\_20Hz 0x15

[ 68](lsm9ds1_8h.md#a64d18383987182bf4bf1e53f2b453eac)#define LSM9DS1\_MAG\_MP\_40Hz 0x16

[ 69](lsm9ds1_8h.md#a3471c091bd2aa1e74806ecb346d6596f)#define LSM9DS1\_MAG\_MP\_80Hz 0x17

[ 70](lsm9ds1_8h.md#a8a2acdcf03dbf680d4a426ce40c8febd)#define LSM9DS1\_MAG\_HP\_0Hz625 0x20

[ 71](lsm9ds1_8h.md#a45dd09f8821be6c22c566b849fdc8809)#define LSM9DS1\_MAG\_HP\_1Hz25 0x21

[ 72](lsm9ds1_8h.md#a453c9c2cd3c8c3cb06269ca4dd9618d5)#define LSM9DS1\_MAG\_HP\_2Hz5 0x22

[ 73](lsm9ds1_8h.md#afcaa83b806529e561a6aa56c43e11fbf)#define LSM9DS1\_MAG\_HP\_5Hz 0x23

[ 74](lsm9ds1_8h.md#af1b8bbaf138fb569f9940d9ce463ed8d)#define LSM9DS1\_MAG\_HP\_10Hz 0x24

[ 75](lsm9ds1_8h.md#a8a36029449d53745c049809e21277694)#define LSM9DS1\_MAG\_HP\_20Hz 0x25

[ 76](lsm9ds1_8h.md#a31edee3a33e9a0b80b750db1c65e8b1b)#define LSM9DS1\_MAG\_HP\_40Hz 0x26

[ 77](lsm9ds1_8h.md#a932221535b82f140d9d27c671b3a1dea)#define LSM9DS1\_MAG\_HP\_80Hz 0x27

[ 78](lsm9ds1_8h.md#a32701c13ef1b3a1f0f7729559494a05e)#define LSM9DS1\_MAG\_UHP\_0Hz625 0x30

[ 79](lsm9ds1_8h.md#a5fe24fb1f5d2a406988ed21a468a2c65)#define LSM9DS1\_MAG\_UHP\_1Hz25 0x31

[ 80](lsm9ds1_8h.md#a5ee91247f5ac37f1b7039e5f94d812b4)#define LSM9DS1\_MAG\_UHP\_2Hz5 0x32

[ 81](lsm9ds1_8h.md#adec6d523b553139aec1434b4f82f092b)#define LSM9DS1\_MAG\_UHP\_5Hz 0x33

[ 82](lsm9ds1_8h.md#ae984af176e83d363d81eac84fb3d110c)#define LSM9DS1\_MAG\_UHP\_10Hz 0x34

[ 83](lsm9ds1_8h.md#a52a1f1cb2ec277d35efc15d69d291d7f)#define LSM9DS1\_MAG\_UHP\_20Hz 0x35

[ 84](lsm9ds1_8h.md#a4831ab9b2168d875f3031894264a2628)#define LSM9DS1\_MAG\_UHP\_40Hz 0x36

[ 85](lsm9ds1_8h.md#a2da3adcf32e4a22b8663ee011317c907)#define LSM9DS1\_MAG\_UHP\_80Hz 0x37

[ 86](lsm9ds1_8h.md#aa0f179e3e3f3c65461e405329d723cec)#define LSM9DS1\_MAG\_UHP\_155Hz 0x38

[ 87](lsm9ds1_8h.md#ae7fb9f552e7a91943291b42e14883cfa)#define LSM9DS1\_MAG\_HP\_300Hz 0x28

[ 88](lsm9ds1_8h.md#a94294a103d745a8967f28df3a9e0e8d6)#define LSM9DS1\_MAG\_MP\_560Hz 0x18

[ 89](lsm9ds1_8h.md#a2347bfea0c970effe93f8cc48bb9e567)#define LSM9DS1\_MAG\_LP\_1000Hz 0x08

[ 90](lsm9ds1_8h.md#a0f5049091c9bf8123cd6bf110ae95a99)#define LSM9DS1\_MAG\_ONE\_SHOT 0x70

91

92#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM9DS1\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm9ds1.h](lsm9ds1_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
