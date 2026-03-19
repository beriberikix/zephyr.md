---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bmp581__user_8h_source.html
original_path: doxygen/html/bmp581__user_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bmp581\_user.h

[Go to the documentation of this file.](bmp581__user_8h.md)

1/\*

2 \* Copyright (c) 2022 Badgerd Technologies B.V.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \* Driver is developed to be used with Zephyr. And it only supports i2c interface.

7 \*

8 \* Author: Talha Can Havadar <havadartalha@gmail.com>

9 \*

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BMP581\_USER\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BMP581\_USER\_H\_

14

15#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

16

[ 17](bmp581__user_8h.md#ac6d7556e6fa16e07512a92e86f85df88)#define BMP5\_SEA\_LEVEL\_PRESSURE\_PA 101325

18

19/\* ODR settings \*/

[ 20](bmp581__user_8h.md#a89faf45a4f0a750495eb60005fe00dbf)#define BMP5\_ODR\_240\_HZ 0x00

[ 21](bmp581__user_8h.md#a8e9b8c29bd9660dcc1f6709d3cfcd5e3)#define BMP5\_ODR\_218\_5\_HZ 0x01

[ 22](bmp581__user_8h.md#ac7ca04b5215289e4f193d45cc044d599)#define BMP5\_ODR\_199\_1\_HZ 0x02

[ 23](bmp581__user_8h.md#a3d543b06bea45a25e4f9b881b9da239b)#define BMP5\_ODR\_179\_2\_HZ 0x03

[ 24](bmp581__user_8h.md#a032889481699ea7d2fa97490326099f5)#define BMP5\_ODR\_160\_HZ 0x04

[ 25](bmp581__user_8h.md#a3f2bbfc335b62c474f1e6071d22f222f)#define BMP5\_ODR\_149\_3\_HZ 0x05

[ 26](bmp581__user_8h.md#a05ab36e9ce0fd1d2c5d91d0256318cf2)#define BMP5\_ODR\_140\_HZ 0x06

[ 27](bmp581__user_8h.md#a9e63a12359ee6558c3b07da5a9df6a20)#define BMP5\_ODR\_129\_8\_HZ 0x07

[ 28](bmp581__user_8h.md#a98838acc2b3fd352f4d3833c5cf7f79e)#define BMP5\_ODR\_120\_HZ 0x08

[ 29](bmp581__user_8h.md#a3edc36e9e1bdf619aef24de48affea45)#define BMP5\_ODR\_110\_1\_HZ 0x09

[ 30](bmp581__user_8h.md#a7f403705e7b523f2a3688376a06ebd0b)#define BMP5\_ODR\_100\_2\_HZ 0x0A

[ 31](bmp581__user_8h.md#ae83cd45460b6d7234478ac0ecdc3c7ee)#define BMP5\_ODR\_89\_6\_HZ 0x0B

[ 32](bmp581__user_8h.md#af63d26c2145ce6cf6fa59f284dc628d5)#define BMP5\_ODR\_80\_HZ 0x0C

[ 33](bmp581__user_8h.md#a4a5d9ae784ed454d9328744baf46080a)#define BMP5\_ODR\_70\_HZ 0x0D

[ 34](bmp581__user_8h.md#ac0469a051ed6d0f59c6686c85b8e1f4c)#define BMP5\_ODR\_60\_HZ 0x0E

[ 35](bmp581__user_8h.md#a74bb202e0555729a8b9098a144e598fa)#define BMP5\_ODR\_50\_HZ 0x0F

[ 36](bmp581__user_8h.md#a92827fe8ec3acc4ce16a752c13b2ea54)#define BMP5\_ODR\_45\_HZ 0x10

[ 37](bmp581__user_8h.md#ab146e4e14d42d99a2f658c2d05b25b06)#define BMP5\_ODR\_40\_HZ 0x11

[ 38](bmp581__user_8h.md#a8755f64f4785137e46635564c343ee01)#define BMP5\_ODR\_35\_HZ 0x12

[ 39](bmp581__user_8h.md#a4235324ff2140539bd9f175e44bb6b5e)#define BMP5\_ODR\_30\_HZ 0x13

[ 40](bmp581__user_8h.md#ae56b323a929971f9d66538244a9145b0)#define BMP5\_ODR\_25\_HZ 0x14

[ 41](bmp581__user_8h.md#ad84abc3ec7e567f52cf71214c3d880a4)#define BMP5\_ODR\_20\_HZ 0x15

[ 42](bmp581__user_8h.md#a5243ee609c018ba9ffa6682d9da9a9f7)#define BMP5\_ODR\_15\_HZ 0x16

[ 43](bmp581__user_8h.md#a2949cee1435229d9480773b0bc15ce79)#define BMP5\_ODR\_10\_HZ 0x17

[ 44](bmp581__user_8h.md#a4a8339ab9586d1615bec332ca2a2fd1b)#define BMP5\_ODR\_05\_HZ 0x18

[ 45](bmp581__user_8h.md#a9680646ceb42c557deb9f96510b541ba)#define BMP5\_ODR\_04\_HZ 0x19

[ 46](bmp581__user_8h.md#a4740357d04ef977a42860cd974e48418)#define BMP5\_ODR\_03\_HZ 0x1A

[ 47](bmp581__user_8h.md#adac8a3103dcd2d430c99aeda0d4c74ee)#define BMP5\_ODR\_02\_HZ 0x1B

[ 48](bmp581__user_8h.md#a4e680bb7a1dc04eb880a35c4316ca0f6)#define BMP5\_ODR\_01\_HZ 0x1C

[ 49](bmp581__user_8h.md#a8b36eb7b8f7b1b69a30d8b6e7d9c3916)#define BMP5\_ODR\_0\_5\_HZ 0x1D

[ 50](bmp581__user_8h.md#a70b3bbe281bb922fed76107e045946e7)#define BMP5\_ODR\_0\_250\_HZ 0x1E

[ 51](bmp581__user_8h.md#a495c984829a594550179e96b6c08ebc0)#define BMP5\_ODR\_0\_125\_HZ 0x1F

52

53/\* Oversampling for temperature and pressure \*/

[ 54](bmp581__user_8h.md#a12c3f441da334e280172e826452807b5)#define BMP5\_OVERSAMPLING\_1X 0x00

[ 55](bmp581__user_8h.md#ae04d4a049fa453901b93b7cd095f17ad)#define BMP5\_OVERSAMPLING\_2X 0x01

[ 56](bmp581__user_8h.md#af71a1a77eee2e57b627e200f060020f5)#define BMP5\_OVERSAMPLING\_4X 0x02

[ 57](bmp581__user_8h.md#ac6bad9c3800816fc28fb6aa7b34f7dae)#define BMP5\_OVERSAMPLING\_8X 0x03

[ 58](bmp581__user_8h.md#a4ba17c469da46a5dc519106807a3e7ab)#define BMP5\_OVERSAMPLING\_16X 0x04

[ 59](bmp581__user_8h.md#abce66cefc09f8209997eaef8d717b303)#define BMP5\_OVERSAMPLING\_32X 0x05

[ 60](bmp581__user_8h.md#a905256e59723dd54a3f7fc885bf2ee3a)#define BMP5\_OVERSAMPLING\_64X 0x06

[ 61](bmp581__user_8h.md#a28bf4f590a88d76a4c7aeafe69db459d)#define BMP5\_OVERSAMPLING\_128X 0x07

62

63/\* IIR filter for temperature and pressure \*/

[ 64](bmp581__user_8h.md#a75900213c0e1ef6250d5ae4afba78261)#define BMP5\_IIR\_FILTER\_BYPASS 0x00

[ 65](bmp581__user_8h.md#acef274a2a1bb65fa9c39c0a306e12b4d)#define BMP5\_IIR\_FILTER\_COEFF\_1 0x01

[ 66](bmp581__user_8h.md#acc37a0a23b2fb4586168bdc4e93c3b45)#define BMP5\_IIR\_FILTER\_COEFF\_3 0x02

[ 67](bmp581__user_8h.md#a7e0f68554716f0f968314d5e489fb429)#define BMP5\_IIR\_FILTER\_COEFF\_7 0x03

[ 68](bmp581__user_8h.md#a2972f3271c35c7b45e5c470e3e6b336b)#define BMP5\_IIR\_FILTER\_COEFF\_15 0x04

[ 69](bmp581__user_8h.md#ab4509b34b7803ee4b25d128e737f5103)#define BMP5\_IIR\_FILTER\_COEFF\_31 0x05

[ 70](bmp581__user_8h.md#a31be0ad7bf5c293c09f51bf51495b56e)#define BMP5\_IIR\_FILTER\_COEFF\_63 0x06

[ 71](bmp581__user_8h.md#a95d709c7b56b5f7bd6eb2e2c3aecb878)#define BMP5\_IIR\_FILTER\_COEFF\_127 0x07

72

73/\* Custom ATTR values \*/

74

75/\* This is used to enable IIR config,

76 \* keep in mind that disabling IIR back in runtime is not

77 \* supported yet

78 \*/

[ 79](bmp581__user_8h.md#a57c276018d0ac606684751e19784457e)#define BMP5\_ATTR\_IIR\_CONFIG (SENSOR\_ATTR\_PRIV\_START + 1u)

[ 80](bmp581__user_8h.md#a4f6e56a0a4f9fd984d3993cf819281d8)#define BMP5\_ATTR\_POWER\_MODE (SENSOR\_ATTR\_PRIV\_START + 2u)

81

[ 82](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dc)enum [bmp5\_powermode](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dc) {

[ 84](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca8f50ab92ba9607eaeed772ddbe92a15f) [BMP5\_POWERMODE\_STANDBY](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca8f50ab92ba9607eaeed772ddbe92a15f),

[ 86](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dcabb75d9c71965843c27724d956ffd1f8c) [BMP5\_POWERMODE\_NORMAL](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dcabb75d9c71965843c27724d956ffd1f8c),

[ 88](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dcaf57d41b2953f1986618de43ac1315b96) [BMP5\_POWERMODE\_FORCED](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dcaf57d41b2953f1986618de43ac1315b96),

[ 90](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca14a304e989e6c079c9b6d668b4fd3e57) [BMP5\_POWERMODE\_CONTINUOUS](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca14a304e989e6c079c9b6d668b4fd3e57),

[ 92](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca3904b0e3e14b2cad554436ba96fe4bf1) [BMP5\_POWERMODE\_DEEP\_STANDBY](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca3904b0e3e14b2cad554436ba96fe4bf1)

93};

94

95#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BMP581\_USER\_H\_ \*/

[bmp5\_powermode](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dc)

bmp5\_powermode

**Definition** bmp581\_user.h:82

[BMP5\_POWERMODE\_CONTINUOUS](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca14a304e989e6c079c9b6d668b4fd3e57)

@ BMP5\_POWERMODE\_CONTINUOUS

Continuous powermode.

**Definition** bmp581\_user.h:90

[BMP5\_POWERMODE\_DEEP\_STANDBY](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca3904b0e3e14b2cad554436ba96fe4bf1)

@ BMP5\_POWERMODE\_DEEP\_STANDBY

Deep standby powermode.

**Definition** bmp581\_user.h:92

[BMP5\_POWERMODE\_STANDBY](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dca8f50ab92ba9607eaeed772ddbe92a15f)

@ BMP5\_POWERMODE\_STANDBY

Standby powermode.

**Definition** bmp581\_user.h:84

[BMP5\_POWERMODE\_NORMAL](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dcabb75d9c71965843c27724d956ffd1f8c)

@ BMP5\_POWERMODE\_NORMAL

Normal powermode.

**Definition** bmp581\_user.h:86

[BMP5\_POWERMODE\_FORCED](bmp581__user_8h.md#aca06546e057d7295ca4f6ed4298247dcaf57d41b2953f1986618de43ac1315b96)

@ BMP5\_POWERMODE\_FORCED

Forced powermode.

**Definition** bmp581\_user.h:88

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [bmp581\_user.h](bmp581__user_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
