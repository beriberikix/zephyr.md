---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lsm6dsv16x_8h_source.html
original_path: doxygen/html/lsm6dsv16x_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lsm6dsv16x.h

[Go to the documentation of this file.](lsm6dsv16x_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSV16X\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSV16X\_H\_

8

9/\* Accel range \*/

[ 10](lsm6dsv16x_8h.md#a0062d4a16bf431f8429ae06c1926dd13)#define LSM6DSV16X\_DT\_FS\_2G 0

[ 11](lsm6dsv16x_8h.md#a90b5d8955a2e8d4cfc1741f426433668)#define LSM6DSV16X\_DT\_FS\_4G 1

[ 12](lsm6dsv16x_8h.md#a5416be4ee0699ccf0994c7decfd9637f)#define LSM6DSV16X\_DT\_FS\_8G 2

[ 13](lsm6dsv16x_8h.md#a8106285e2a93c6dfc3b9c704166938e7)#define LSM6DSV16X\_DT\_FS\_16G 3

14

15/\* Gyro range \*/

[ 16](lsm6dsv16x_8h.md#aba0ad1e516dc73ce4f610474db2cf8f0)#define LSM6DSV16X\_DT\_FS\_125DPS 0x0

[ 17](lsm6dsv16x_8h.md#a4b908bb6e1684b69e3023a9b3056461d)#define LSM6DSV16X\_DT\_FS\_250DPS 0x1

[ 18](lsm6dsv16x_8h.md#a02d9fa7e2f077d98c4f6882555f74162)#define LSM6DSV16X\_DT\_FS\_500DPS 0x2

[ 19](lsm6dsv16x_8h.md#a062069e117674a493a3100369c6bae0c)#define LSM6DSV16X\_DT\_FS\_1000DPS 0x3

[ 20](lsm6dsv16x_8h.md#a7568fcc223af82319d884138ff43fcaa)#define LSM6DSV16X\_DT\_FS\_2000DPS 0x4

[ 21](lsm6dsv16x_8h.md#aad0a2d26bab54aff65bcf922db56d5dd)#define LSM6DSV16X\_DT\_FS\_4000DPS 0xc

22

23/\* Accel and Gyro Data rates \*/

[ 24](lsm6dsv16x_8h.md#a0b11f0f939bc10587ca0f8cc1e8da7d0)#define LSM6DSV16X\_DT\_ODR\_OFF 0x0

[ 25](lsm6dsv16x_8h.md#a51ad08e5e99e7da94cb4948f04cb7931)#define LSM6DSV16X\_DT\_ODR\_AT\_1Hz875 0x1

[ 26](lsm6dsv16x_8h.md#a908f07f0e822f1776f0e59166986fb43)#define LSM6DSV16X\_DT\_ODR\_AT\_7Hz5 0x2

[ 27](lsm6dsv16x_8h.md#af25ef10ac9e3183392ea6f3b4c8872ad)#define LSM6DSV16X\_DT\_ODR\_AT\_15Hz 0x3

[ 28](lsm6dsv16x_8h.md#acb735ed313c5813c26206dc0a8c649a0)#define LSM6DSV16X\_DT\_ODR\_AT\_30Hz 0x4

[ 29](lsm6dsv16x_8h.md#ac4763e79340953fdec46a2557cc3a7e9)#define LSM6DSV16X\_DT\_ODR\_AT\_60Hz 0x5

[ 30](lsm6dsv16x_8h.md#a4a8d2eb4eef9d6137b02aab5cf60d9b3)#define LSM6DSV16X\_DT\_ODR\_AT\_120Hz 0x6

[ 31](lsm6dsv16x_8h.md#a6cc44855f1c9ba6a44063c59204ab6e7)#define LSM6DSV16X\_DT\_ODR\_AT\_240Hz 0x7

[ 32](lsm6dsv16x_8h.md#a3814c412b7314efc062a8ed31a95a530)#define LSM6DSV16X\_DT\_ODR\_AT\_480Hz 0x8

[ 33](lsm6dsv16x_8h.md#abd274f980523545640e31b5e8fa373b0)#define LSM6DSV16X\_DT\_ODR\_AT\_960Hz 0x9

[ 34](lsm6dsv16x_8h.md#ae0d6b562ee0cb8523a1a9b974332f74c)#define LSM6DSV16X\_DT\_ODR\_AT\_1920Hz 0xA

[ 35](lsm6dsv16x_8h.md#a349976f99ae8bd144054eb4b6d5601a6)#define LSM6DSV16X\_DT\_ODR\_AT\_3840Hz 0xB

[ 36](lsm6dsv16x_8h.md#a7adb88cac62df5b3e63b9cf647ddfea3)#define LSM6DSV16X\_DT\_ODR\_AT\_7680Hz 0xC

[ 37](lsm6dsv16x_8h.md#af7f63bb894b71c67c933651539f370fa)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_15Hz625 0x13

[ 38](lsm6dsv16x_8h.md#ab3da725c6833f45b7a33afa55cfc40b3)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_31Hz25 0x14

[ 39](lsm6dsv16x_8h.md#ab024dfe5fc460ce2a9001732e21d9f05)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_62Hz5 0x15

[ 40](lsm6dsv16x_8h.md#a23da2ed6467ffb0cd1f2ab9ae9584ec8)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_125Hz 0x16

[ 41](lsm6dsv16x_8h.md#a62eaf6164a041b9280933dc50e3dca89)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_250Hz 0x17

[ 42](lsm6dsv16x_8h.md#a5875eadae47c3b41ee32c6571f5fd7e9)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_500Hz 0x18

[ 43](lsm6dsv16x_8h.md#a37a462e9411d24b07ffa0266baf4b0e8)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_1000Hz 0x19

[ 44](lsm6dsv16x_8h.md#a797db8e4aa3fa0ceae95f9af0a720767)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_2000Hz 0x1A

[ 45](lsm6dsv16x_8h.md#a312e7af10f7387764d4760017c8d19fd)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_4000Hz 0x1B

[ 46](lsm6dsv16x_8h.md#a490ba6a741e42ab2cf6a8260c1481bf7)#define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_8000Hz 0x1C

[ 47](lsm6dsv16x_8h.md#ae9f6bae9e1bec8194d9ce6a42e30f472)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_12Hz5 0x23

[ 48](lsm6dsv16x_8h.md#a3996f051df14448dfa2b91864ee0e951)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_25Hz 0x24

[ 49](lsm6dsv16x_8h.md#a76bee41aedef974a0db131751047db55)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_50Hz 0x25

[ 50](lsm6dsv16x_8h.md#adfc3e88f261d411102538e9e73352b55)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_100Hz 0x26

[ 51](lsm6dsv16x_8h.md#a30137882a4c78ddb51cff91a3775780c)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_200Hz 0x27

[ 52](lsm6dsv16x_8h.md#a2b30fdf564d398b52d8f0ca7ab39ec92)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_400Hz 0x28

[ 53](lsm6dsv16x_8h.md#adc01cf297fde9fa86865c80343107e6c)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_800Hz 0x29

[ 54](lsm6dsv16x_8h.md#ae2f10f581548e9c1b91680f044b70815)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_1600Hz 0x2A

[ 55](lsm6dsv16x_8h.md#a0685e049b46f34e3cff3590827a4cd04)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_3200Hz 0x2B

[ 56](lsm6dsv16x_8h.md#ae52f4d001cefe4730ff81224871821c7)#define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_6400Hz 0x2C

57

58#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSV16X\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm6dsv16x.h](lsm6dsv16x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
