---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/lis2dux12_8h_source.html
original_path: doxygen/html/lis2dux12_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

[ 14](lis2dux12_8h.md#ae08239e9d97ce581865d441faf13861b)#define LIS2DUX12\_OPER\_MODE\_HIGH\_PERFORMANCE 2

[ 15](lis2dux12_8h.md#a1a6e9387e8b30d1c6ffcf0f02ca61000)#define LIS2DUX12\_OPER\_MODE\_SINGLE\_SHOT 3

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

38/\* Accelerometer FIFO batching data rate \*/

[ 39](lis2dux12_8h.md#a3d4281053ce07bf0e2871180affd246a)#define LIS2DUX12\_DT\_BDR\_XL\_ODR 0x0

[ 40](lis2dux12_8h.md#a658039a66e163c5950d80eebd1b67f4a)#define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_2 0x1

[ 41](lis2dux12_8h.md#a0b27bbf1af06f586a9f901d8603629b7)#define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_4 0x2

[ 42](lis2dux12_8h.md#adf324739868e1fe7bc4b1128699e2223)#define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_8 0x3

[ 43](lis2dux12_8h.md#a9560e4c28c1d4b50f273aab0c3274274)#define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_16 0x4

[ 44](lis2dux12_8h.md#a03ef61baf524a38730341b3344cdc046)#define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_32 0x5

[ 45](lis2dux12_8h.md#a73e547d7a3fd0436ee3c308d6f7c20f2)#define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_64 0x6

[ 46](lis2dux12_8h.md#afbbb48285a89128d313eeea2b7a1bbb1)#define LIS2DUX12\_DT\_BDR\_XL\_ODR\_OFF 0x7

47

48/\* Accelerometer FIFO timestamp ratio \*/

[ 49](lis2dux12_8h.md#a058e573325b65dde80dd3813984ac38a)#define LIS2DUX12\_DT\_DEC\_TS\_OFF 0x0

[ 50](lis2dux12_8h.md#a7520bcd1eae2b91bf068cdc1f6ae4487)#define LIS2DUX12\_DT\_DEC\_TS\_1 0x1

[ 51](lis2dux12_8h.md#a209de2a2bd10240767aa01c9d2f4d73d)#define LIS2DUX12\_DT\_DEC\_TS\_8 0x2

[ 52](lis2dux12_8h.md#a12c2234e04c51383868576fb82f8cecc)#define LIS2DUX12\_DT\_DEC\_TS\_32 0x3

53

54/\* Accelerometer FIFO tags (aligned with lis2dux12\_fifo\_sensor\_tag\_t) \*/

[ 55](lis2dux12_8h.md#ab0f9df25d43e17fc210c63581a3abc0f)#define LIS2DUXXX\_FIFO\_EMPTY 0x0

[ 56](lis2dux12_8h.md#a26fc2cb8dbefd4995f47b0dd4b7d0652)#define LIS2DUXXX\_XL\_TEMP\_TAG 0x2

[ 57](lis2dux12_8h.md#a6540e92e3d71a254fbb5c6d13e0e707c)#define LIS2DUXXX\_XL\_ONLY\_2X\_TAG 0x3

[ 58](lis2dux12_8h.md#a4eb99cf7057a0688bc7289c3fbb05020)#define LIS2DUXXX\_TIMESTAMP\_TAG 0x4

[ 59](lis2dux12_8h.md#ad2648a4dd63e75dc6ec07fc7f5307ed8)#define LIS2DUXXX\_STEP\_COUNTER\_TAG 0x12

[ 60](lis2dux12_8h.md#ab6e05aec8aec334546ef581b88f85741)#define LIS2DUXXX\_MLC\_RESULT\_TAG 0x1A

[ 61](lis2dux12_8h.md#a9063c5ef1b246d7e859945aaa2832dd3)#define LIS2DUXXX\_MLC\_FILTER\_TAG 0x1B

[ 62](lis2dux12_8h.md#a9ca64efe26ab1956ccffd4a921c0352c)#define LIS2DUXXX\_MLC\_FEATURE 0x1C

[ 63](lis2dux12_8h.md#aa0b27f7c2bca8115c3026482aeaea324)#define LIS2DUXXX\_FSM\_RESULT\_TAG 0x1D

64

65/\* Accelerometer FIFO modes (aligned with lis2dux12\_operation\_t) \*/

[ 66](lis2dux12_8h.md#acc96a742af72f029a4b05ef67f99bb6d)#define LIS2DUXXX\_DT\_BYPASS\_MODE 0x0

[ 67](lis2dux12_8h.md#a64c29d5624aac1eb64d5d38f3aa77f2b)#define LIS2DUXXX\_DT\_FIFO\_MODE 0x1

[ 68](lis2dux12_8h.md#ad0846e36da27873da048c8c44689f59e)#define LIS2DUXXX\_DT\_STREAM\_TO\_FIFO\_MODE 0x3

[ 69](lis2dux12_8h.md#a2d1b9368d9bfcc55b93334fb13208b21)#define LIS2DUXXX\_DT\_BYPASS\_TO\_STREAM\_MODE 0x4

[ 70](lis2dux12_8h.md#a62f6c22b8c4bdeb587a5262a727e4368)#define LIS2DUXXX\_DT\_STREAM\_MODE 0x6

[ 71](lis2dux12_8h.md#a2ad4e4ad6c41d804db6a502f7863726a)#define LIS2DUXXX\_DT\_BYPASS\_TO\_FIFO\_MODE 0x7

[ 72](lis2dux12_8h.md#a952127a0b7199066e7f3f0fa58fa2f95)#define LIS2DUXXX\_DT\_FIFO\_OFF 0x8

73

74/\* Accelerometer registers \*/

[ 75](lis2dux12_8h.md#affa56c1d9471f5afbada2c14261f36a3)#define LIS2DUXXX\_DT\_FIFO\_CTRL 0x15U

[ 76](lis2dux12_8h.md#ac4d1357af5ab51679f04a03a5396f76e)#define LIS2DUXXX\_DT\_STATUS 0x25U

[ 77](lis2dux12_8h.md#aeb7afe0eb54defa45b66a5726d51dec7)#define LIS2DUXXX\_DT\_FIFO\_STATUS1 0x26U

[ 78](lis2dux12_8h.md#a7fd3f10740da5a54fdf18f37c9282f29)#define LIS2DUXXX\_DT\_OUTX\_L 0x28U

[ 79](lis2dux12_8h.md#ad773a65749a20dd28e4e7b37cf8db62d)#define LIS2DUXXX\_DT\_FIFO\_DATA\_OUT\_TAG 0x40U

80

81#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_LIS2DUX12\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2dux12.h](lis2dux12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
