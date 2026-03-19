---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lsm6dso16is_8h_source.html
original_path: doxygen/html/lsm6dso16is_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lsm6dso16is.h

[Go to the documentation of this file.](lsm6dso16is_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSO16IS\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSO16IS\_H\_

8

9/\* Accel range \*/

[ 10](lsm6dso16is_8h.md#aef962f51d056b682499253d924efbebd)#define LSM6DSO16IS\_DT\_FS\_2G 0

[ 11](lsm6dso16is_8h.md#aa5a35dd0a780ef6bcc9e10d3649da6ea)#define LSM6DSO16IS\_DT\_FS\_16G 1

[ 12](lsm6dso16is_8h.md#a4c001f612eeda1cbf4f90fc8b5d152de)#define LSM6DSO16IS\_DT\_FS\_4G 2

[ 13](lsm6dso16is_8h.md#aaf35c79b724086e52bf23e770672dbfb)#define LSM6DSO16IS\_DT\_FS\_8G 3

14

15/\* Gyro range \*/

[ 16](lsm6dso16is_8h.md#a1d0a9442346bae3d5b5a36ad1c3489e8)#define LSM6DSO16IS\_DT\_FS\_250DPS 0x0

[ 17](lsm6dso16is_8h.md#aceffc85cca61d470130c161db5c96e07)#define LSM6DSO16IS\_DT\_FS\_500DPS 0x1

[ 18](lsm6dso16is_8h.md#a69b6df4545ebb41822bafaca1b874d17)#define LSM6DSO16IS\_DT\_FS\_1000DPS 0x2

[ 19](lsm6dso16is_8h.md#ac902aeef5746301643bbfd8cdaa4de58)#define LSM6DSO16IS\_DT\_FS\_2000DPS 0x3

[ 20](lsm6dso16is_8h.md#ada2187a79f7a1760cd51b9013db3116b)#define LSM6DSO16IS\_DT\_FS\_125DPS 0x10

21

22/\* Accel and Gyro Data rates \*/

[ 23](lsm6dso16is_8h.md#a4ba627f0619a454d6ef51cd96bd16899)#define LSM6DSO16IS\_DT\_ODR\_OFF 0x0

[ 24](lsm6dso16is_8h.md#ab8f3e866915d67db14c2542b0e0daf7a)#define LSM6DSO16IS\_DT\_ODR\_12Hz5\_HP 0x1

[ 25](lsm6dso16is_8h.md#a0b207e36eccb0cd6925c892825b92b20)#define LSM6DSO16IS\_DT\_ODR\_26H\_HP 0x2

[ 26](lsm6dso16is_8h.md#af65d338ed7037873e8eeed06f13de32e)#define LSM6DSO16IS\_DT\_ODR\_52Hz\_HP 0x3

[ 27](lsm6dso16is_8h.md#a9fc5dae1a461c33532eb9886408f826d)#define LSM6DSO16IS\_DT\_ODR\_104Hz\_HP 0x4

[ 28](lsm6dso16is_8h.md#abf26a667b036d12df116892b61da4c21)#define LSM6DSO16IS\_DT\_ODR\_208Hz\_HP 0x5

[ 29](lsm6dso16is_8h.md#a3369d95d744f89867ec3bfc72657eabf)#define LSM6DSO16IS\_DT\_ODR\_416Hz\_HP 0x6

[ 30](lsm6dso16is_8h.md#a4e8db7ad45aae2970ed6b5128054180a)#define LSM6DSO16IS\_DT\_ODR\_833Hz\_HP 0x7

[ 31](lsm6dso16is_8h.md#ad25ff38e64749fc911d1981283546cd0)#define LSM6DSO16IS\_DT\_ODR\_1667Hz\_HP 0x8

[ 32](lsm6dso16is_8h.md#a81004a456887572b9df7140e0e85b33c)#define LSM6DSO16IS\_DT\_ODR\_3333Hz\_HP 0x9

[ 33](lsm6dso16is_8h.md#af7c0b12cf6995c790a91d513a2046bd8)#define LSM6DSO16IS\_DT\_ODR\_6667Hz\_HP 0xa

[ 34](lsm6dso16is_8h.md#a03f8cf22c6e912aa10767c316fb7e2a3)#define LSM6DSO16IS\_DT\_ODR\_12Hz5\_LP 0x11

[ 35](lsm6dso16is_8h.md#a752fea530e4977f942cd802299b8f04e)#define LSM6DSO16IS\_DT\_ODR\_26H\_LP 0x12

[ 36](lsm6dso16is_8h.md#aaa1feb747d3f4156194ad712b6790210)#define LSM6DSO16IS\_DT\_ODR\_52Hz\_LP 0x13

[ 37](lsm6dso16is_8h.md#a2e827035678f213fc3dcc31f8c439eea)#define LSM6DSO16IS\_DT\_ODR\_104Hz\_LP 0x14

[ 38](lsm6dso16is_8h.md#a5b875ba646a4a94cba706f275e056fb8)#define LSM6DSO16IS\_DT\_ODR\_208Hz\_LP 0x15

[ 39](lsm6dso16is_8h.md#aa5c131c9bc27d864c19a7eaf3f815a0f)#define LSM6DSO16IS\_DT\_ODR\_416Hz\_LP 0x16

[ 40](lsm6dso16is_8h.md#a1402fda052ab8395909a3c825045fc73)#define LSM6DSO16IS\_DT\_ODR\_833Hz\_LP 0x17

[ 41](lsm6dso16is_8h.md#a6460d76877bad9037e704c262f703c1d)#define LSM6DSO16IS\_DT\_ODR\_1667Hz\_LP 0x18

[ 42](lsm6dso16is_8h.md#af34646135c7fa8351ae55395e4d30b1c)#define LSM6DSO16IS\_DT\_ODR\_3333Hz\_LP 0x19

[ 43](lsm6dso16is_8h.md#a36bdc86bb5f3a64db2120340bbd52587)#define LSM6DSO16IS\_DT\_ODR\_6667Hz\_LP 0x1a

[ 44](lsm6dso16is_8h.md#ab6e4b5abb44d1a0da80b9ce0f8a48169)#define LSM6DSO16IS\_DT\_ODR\_1Hz6\_LP 0x1b

45

46#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSO16IS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm6dso16is.h](lsm6dso16is_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
