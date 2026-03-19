---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lis2du12_8h_source.html
original_path: doxygen/html/lis2du12_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2du12.h

[Go to the documentation of this file.](lis2du12_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DU12\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DU12\_H\_

8

9/\* Accel range \*/

[ 10](lis2du12_8h.md#a2b42fd439750df2fb03d62a9c657fca1)#define LIS2DU12\_DT\_FS\_2G 0

[ 11](lis2du12_8h.md#a3465e147dab6ce4b85fbdf2709e39613)#define LIS2DU12\_DT\_FS\_4G 1

[ 12](lis2du12_8h.md#af1b1956d5a808fca2dbaab01845bcf5e)#define LIS2DU12\_DT\_FS\_8G 2

[ 13](lis2du12_8h.md#a07253b36548b1ae59171576a8e7e2115)#define LIS2DU12\_DT\_FS\_16G 3

14

15/\* Accel rates \*/

[ 16](lis2du12_8h.md#a3a76a7b040855274d5e8b00ea522654d)#define LIS2DU12\_DT\_ODR\_OFF 0x00 /\* Power-Down \*/

[ 17](lis2du12_8h.md#ac1c54a059fbfb427f975fc0961343e28)#define LIS2DU12\_DT\_ODR\_AT\_1Hz6\_ULP 0x01 /\* 1Hz6 (ultra low power) \*/

[ 18](lis2du12_8h.md#a64606f40cd014eae9d89c929168c5e0f)#define LIS2DU12\_DT\_ODR\_AT\_3Hz\_ULP 0x02 /\* 3Hz (ultra low power) \*/

[ 19](lis2du12_8h.md#ab54ebbbe8991aa268c0dbaae4427fcd8)#define LIS2DU12\_DT\_ODR\_AT\_6Hz\_ULP 0x03 /\* 6Hz (ultra low power) \*/

[ 20](lis2du12_8h.md#af135c2f1fd176eef32ee45ec09010213)#define LIS2DU12\_DT\_ODR\_AT\_6Hz 0x04 /\* 6Hz (normal) \*/

[ 21](lis2du12_8h.md#a421b54616308f44cd796b4553ccbd93d)#define LIS2DU12\_DT\_ODR\_AT\_12Hz 0x05 /\* 12Hz5 (normal) \*/

[ 22](lis2du12_8h.md#ad3aaa0a89d8e90cac5e67a52b63e2c7e)#define LIS2DU12\_DT\_ODR\_AT\_25Hz 0x06 /\* 25Hz (normal) \*/

[ 23](lis2du12_8h.md#ac444fac795f58756c3d5dd469412bba1)#define LIS2DU12\_DT\_ODR\_AT\_50Hz 0x07 /\* 50Hz (normal) \*/

[ 24](lis2du12_8h.md#a2f43a631e26e62246d9b198b48b3c10e)#define LIS2DU12\_DT\_ODR\_AT\_100Hz 0x08 /\* 100Hz (normal) \*/

[ 25](lis2du12_8h.md#a11789548c0055a69e0899dcd8590df07)#define LIS2DU12\_DT\_ODR\_AT\_200Hz 0x09 /\* 200Hz (normal) \*/

[ 26](lis2du12_8h.md#aa728d2f438efffdcd6eb607efa5db714)#define LIS2DU12\_DT\_ODR\_AT\_400Hz 0x0a /\* 400Hz (normal) \*/

[ 27](lis2du12_8h.md#a1ab1a8891428768cbdfedf3f281ff9fb)#define LIS2DU12\_DT\_ODR\_AT\_800Hz 0x0b /\* 800Hz (normal) \*/

[ 28](lis2du12_8h.md#a5b1ec0132ce400ce9207b100a1926687)#define LIS2DU12\_DT\_ODR\_TRIG\_PIN 0x0e /\* Single-shot high latency by INT2 \*/

[ 29](lis2du12_8h.md#af3389a81e1bc4ce6a9965ad6ba828963)#define LIS2DU12\_DT\_ODR\_TRIG\_SW 0x0f /\* Single-shot high latency by IF \*/

30

31#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DU12\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2du12.h](lis2du12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
