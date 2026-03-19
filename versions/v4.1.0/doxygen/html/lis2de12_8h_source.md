---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lis2de12_8h_source.html
original_path: doxygen/html/lis2de12_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2de12.h

[Go to the documentation of this file.](lis2de12_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DE12\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DE12\_H\_

8

9/\* Accel range \*/

[ 10](lis2de12_8h.md#a4d98a2437d4189112bf8de962a6427c5)#define LIS2DE12\_DT\_FS\_2G 0

[ 11](lis2de12_8h.md#a28ea756e9426fef814d34e8f8e416373)#define LIS2DE12\_DT\_FS\_4G 1

[ 12](lis2de12_8h.md#a9e527343fd8f40e87698ab4f2095a09c)#define LIS2DE12\_DT\_FS\_8G 2

[ 13](lis2de12_8h.md#a5a79ea2d22261f2cbff1a920165c3614)#define LIS2DE12\_DT\_FS\_16G 3

14

15/\* Accel rates \*/

[ 16](lis2de12_8h.md#a6fbd76dfbed77dbb642f6174e41b4933)#define LIS2DE12\_DT\_ODR\_OFF 0x00 /\* Power-Down \*/

[ 17](lis2de12_8h.md#aeb564c25b94d793c58cb0c54ce04acf5)#define LIS2DE12\_DT\_ODR\_AT\_1Hz 0x01 /\* 1Hz (normal) \*/

[ 18](lis2de12_8h.md#ad0a75e097c965995ed8e46cf93585cf6)#define LIS2DE12\_DT\_ODR\_AT\_10Hz 0x02 /\* 10Hz (normal) \*/

[ 19](lis2de12_8h.md#ab5e906715ed2c45f4794a9d069d56921)#define LIS2DE12\_DT\_ODR\_AT\_25Hz 0x03 /\* 25Hz (normal) \*/

[ 20](lis2de12_8h.md#aa751bddcce56dba2fe8209bd919692ef)#define LIS2DE12\_DT\_ODR\_AT\_50Hz 0x04 /\* 50Hz (normal) \*/

[ 21](lis2de12_8h.md#ab0d6486440d1a759bf86311237803814)#define LIS2DE12\_DT\_ODR\_AT\_100Hz 0x05 /\* 100Hz (normal) \*/

[ 22](lis2de12_8h.md#abb6ab746392ec390affcff0b63208fcd)#define LIS2DE12\_DT\_ODR\_AT\_200Hz 0x06 /\* 200Hz (normal) \*/

[ 23](lis2de12_8h.md#a02142274ee4945c67385ff49b322ad66)#define LIS2DE12\_DT\_ODR\_AT\_400Hz 0x07 /\* 400Hz (normal) \*/

[ 24](lis2de12_8h.md#aa14ef617b90cb5f8453eab1837eeb5d7)#define LIS2DE12\_DT\_ODR\_AT\_1kHz620 0x08 /\* 1KHz620 (normal) \*/

[ 25](lis2de12_8h.md#a817a85c45d4dfb94933715f2b1492ca2)#define LIS2DE12\_DT\_ODR\_AT\_5kHz376 0x09 /\* 5KHz376 (normal) \*/

26

27#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_LIS2DE12\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2de12.h](lis2de12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
