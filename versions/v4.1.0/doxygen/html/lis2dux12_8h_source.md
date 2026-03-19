---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lis2dux12_8h_source.html
original_path: doxygen/html/lis2dux12_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2dux12.h

[Go to the documentation of this file.](lis2dux12_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_LIS2DUX12\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_LIS2DUX12\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

11/\* Operating Mode \*/

[ 12](lis2dux12_8h.md#a2319e5357a3b3933e46e0e445d8bb868)#define LIS2DUX12\_OPER\_MODE\_POWER\_DOWN 0

[ 13](lis2dux12_8h.md#a03d276c97b5ee65f80ce301f78d8d620)#define LIS2DUX12\_OPER\_MODE\_LOW\_POWER 1

[ 14](lis2dux12_8h.md#aee9aa425da279bd1f39a34954f76ec4d)#define LIS2DUX12\_OPER\_MODE\_HIGH\_RESOLUTION 2

[ 15](lis2dux12_8h.md#a91f64cdb166b4e3ef48d72f754c23f62)#define LIS2DUX12\_OPER\_MODE\_HIGH\_FREQUENCY 3

16

17/\* Data rate \*/

[ 18](lis2dux12_8h.md#a94ab30f7ef8aec193a84188ccf63a21d)#define LIS2DUX12\_DT\_ODR\_OFF 0

[ 19](lis2dux12_8h.md#ae8f5f4224653c75ba0343d13d0588910)#define LIS2DUX12\_DT\_ODR\_1Hz\_ULP 1 /\* available in ultra-low power mode \*/

[ 20](lis2dux12_8h.md#a4a85ef36d5836a6c216a36272c645cfb)#define LIS2DUX12\_DT\_ODR\_3Hz\_ULP 2 /\* available in ultra-low power mode \*/

[ 21](lis2dux12_8h.md#af649bb985c44d6631e6fd1a0a91fbf85)#define LIS2DUX12\_DT\_ODR\_25Hz\_ULP 3 /\* available in ultra-low power mode \*/

[ 22](lis2dux12_8h.md#a7c83ff001a3ff25aaab5cbac32a56df0)#define LIS2DUX12\_DT\_ODR\_6Hz 4 /\* available in LP and HP mode \*/

[ 23](lis2dux12_8h.md#a01ab37065a2bb53366adc7740af37d62)#define LIS2DUX12\_DT\_ODR\_12Hz5 5 /\* available in LP and HP mode \*/

[ 24](lis2dux12_8h.md#a1daa6448cea439025041b74f5dc3e58f)#define LIS2DUX12\_DT\_ODR\_25Hz 6 /\* available in LP and HP mode \*/

[ 25](lis2dux12_8h.md#aea1f056b715ed59a38ddb4c8aac48804)#define LIS2DUX12\_DT\_ODR\_50Hz 7 /\* available in LP and HP mode \*/

[ 26](lis2dux12_8h.md#a3b40a334bea0de6546b783ab65e9f4dd)#define LIS2DUX12\_DT\_ODR\_100Hz 8 /\* available in LP and HP mode \*/

[ 27](lis2dux12_8h.md#a230b18cdf50c202d1bced583914332e1)#define LIS2DUX12\_DT\_ODR\_200Hz 9 /\* available in LP and HP mode \*/

[ 28](lis2dux12_8h.md#ae3dc67b51572e8f0c5d5ec3394d5d750)#define LIS2DUX12\_DT\_ODR\_400Hz 10 /\* available in LP and HP mode \*/

[ 29](lis2dux12_8h.md#a6a8105006b18fe6632fbce06c77bed52)#define LIS2DUX12\_DT\_ODR\_800Hz 11 /\* available in LP and HP mode \*/

[ 30](lis2dux12_8h.md#a68214dc2825057ef3fa3e87a7ae1fcc1)#define LIS2DUX12\_DT\_ODR\_END 12

31

32/\* Accelerometer Full-scale \*/

[ 33](lis2dux12_8h.md#a9793fcda818ea10e61e844a3b94cda62)#define LIS2DUX12\_DT\_FS\_2G 0 /\* 2g (0.061 mg/LSB) \*/

[ 34](lis2dux12_8h.md#ab50eb77d0d2bac9eb493ec0490f2b4f7)#define LIS2DUX12\_DT\_FS\_4G 1 /\* 4g (0.122 mg/LSB) \*/

[ 35](lis2dux12_8h.md#ad0119b9353cec4ff57ad4e6fe1c7c055)#define LIS2DUX12\_DT\_FS\_8G 2 /\* 8g (0.244 mg/LSB) \*/

[ 36](lis2dux12_8h.md#a6e29f5351f4eebe482648629024af77e)#define LIS2DUX12\_DT\_FS\_16G 3 /\* 16g (0.488 mg/LSB) \*/

37

38#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_LIS2DUX12\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2dux12.h](lis2dux12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
