---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lsm6dso_8h_source.html
original_path: doxygen/html/lsm6dso_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lsm6dso.h

[Go to the documentation of this file.](lsm6dso_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSO\_H\_

8

9/\* Accel power-modes \*/

[ 10](lsm6dso_8h.md#aa62e5d2a5529d005f4d622ecdf97f8f0)#define LSM6DSO\_DT\_XL\_HP\_MODE 0

[ 11](lsm6dso_8h.md#a031783c6119db7de6138f368c65c0e49)#define LSM6DSO\_DT\_XL\_LP\_NORMAL\_MODE 1

[ 12](lsm6dso_8h.md#ae1fc1b3317d8dac484cc8f094ff453c6)#define LSM6DSO\_DT\_XL\_ULP\_MODE 2

13

14/\* Gyro power-modes \*/

[ 15](lsm6dso_8h.md#ac6810407924f44016f0f27c44aca22de)#define LSM6DSO\_DT\_GY\_HP\_MODE 0

[ 16](lsm6dso_8h.md#aae6bf6b52db6321cba323a06af6afe4c)#define LSM6DSO\_DT\_GY\_NORMAL\_MODE 1

17

18/\* Accel range \*/

[ 19](lsm6dso_8h.md#a4b6fd691c9843fdce021c027a6c1d38f)#define LSM6DSO\_DT\_FS\_2G 0

[ 20](lsm6dso_8h.md#aab163b8d605a6433aff9af2c4fb31764)#define LSM6DSO\_DT\_FS\_16G 1

[ 21](lsm6dso_8h.md#ac6b3e663efb2aa9340480a0a955b97d7)#define LSM6DSO\_DT\_FS\_4G 2

[ 22](lsm6dso_8h.md#ad2f86d00fa1665c011296fa27b4a235c)#define LSM6DSO\_DT\_FS\_8G 3

23

24/\* Gyro range \*/

[ 25](lsm6dso_8h.md#a3754f6339351a7d1be2b98fab8b88102)#define LSM6DSO\_DT\_FS\_250DPS 0

[ 26](lsm6dso_8h.md#ae427e045d161c9f90eff4c6e5dee4efe)#define LSM6DSO\_DT\_FS\_125DPS 1

[ 27](lsm6dso_8h.md#a0edc66177f1cb810257fe8e3460586a4)#define LSM6DSO\_DT\_FS\_500DPS 2

[ 28](lsm6dso_8h.md#a862e3383ea2a6db7fea154fe7b5e5f58)#define LSM6DSO\_DT\_FS\_1000DPS 4

[ 29](lsm6dso_8h.md#a5f007e2d998b5eda7c5fd08145665e4e)#define LSM6DSO\_DT\_FS\_2000DPS 6

30

31/\* Accel and Gyro Data rates \*/

[ 32](lsm6dso_8h.md#a8969b4f07c618f652bf4b15de9d0b5f7)#define LSM6DSO\_DT\_ODR\_OFF 0x0

[ 33](lsm6dso_8h.md#a9f0952fa1854848632b30b59e8145f08)#define LSM6DSO\_DT\_ODR\_12Hz5 0x1

[ 34](lsm6dso_8h.md#ab8cc4ee8854e45071720c6e97cb9a133)#define LSM6DSO\_DT\_ODR\_26H 0x2

[ 35](lsm6dso_8h.md#ab172e908c0810d7a57cad2ccd70626b1)#define LSM6DSO\_DT\_ODR\_52Hz 0x3

[ 36](lsm6dso_8h.md#a59b98b9f338fd9cf2d568b14ac5a5410)#define LSM6DSO\_DT\_ODR\_104Hz 0x4

[ 37](lsm6dso_8h.md#af57d5e0ecb4fba8230d4a69390a4857c)#define LSM6DSO\_DT\_ODR\_208Hz 0x5

[ 38](lsm6dso_8h.md#aeb374d527698dc50af30a2469957da6f)#define LSM6DSO\_DT\_ODR\_417Hz 0x6

[ 39](lsm6dso_8h.md#a2cb2a2d726eee22c6e5457700a966c9a)#define LSM6DSO\_DT\_ODR\_833Hz 0x7

[ 40](lsm6dso_8h.md#a41f7e1ee6c74cd37b707382ccda3474b)#define LSM6DSO\_DT\_ODR\_1667Hz 0x8

[ 41](lsm6dso_8h.md#ab66ab364d747f4b95f68c596effeb143)#define LSM6DSO\_DT\_ODR\_3333Hz 0x9

[ 42](lsm6dso_8h.md#a73b782f5504622e185d60d635397620a)#define LSM6DSO\_DT\_ODR\_6667Hz 0xa

[ 43](lsm6dso_8h.md#a14963a4bd7e78ba44eb33da3eaa950af)#define LSM6DSO\_DT\_ODR\_1Hz6 0xb

44

45#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LSM6DSO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm6dso.h](lsm6dso_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
