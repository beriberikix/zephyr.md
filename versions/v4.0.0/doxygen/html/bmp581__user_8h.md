---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bmp581__user_8h.html
original_path: doxygen/html/bmp581__user_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bmp581\_user.h File Reference

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](bmp581__user_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BMP5\_SEA\_LEVEL\_PRESSURE\_PA](#ac6d7556e6fa16e07512a92e86f85df88)   101325 |
| #define | [BMP5\_ODR\_240\_HZ](#a89faf45a4f0a750495eb60005fe00dbf)   0x00 |
| #define | [BMP5\_ODR\_218\_5\_HZ](#a8e9b8c29bd9660dcc1f6709d3cfcd5e3)   0x01 |
| #define | [BMP5\_ODR\_199\_1\_HZ](#ac7ca04b5215289e4f193d45cc044d599)   0x02 |
| #define | [BMP5\_ODR\_179\_2\_HZ](#a3d543b06bea45a25e4f9b881b9da239b)   0x03 |
| #define | [BMP5\_ODR\_160\_HZ](#a032889481699ea7d2fa97490326099f5)   0x04 |
| #define | [BMP5\_ODR\_149\_3\_HZ](#a3f2bbfc335b62c474f1e6071d22f222f)   0x05 |
| #define | [BMP5\_ODR\_140\_HZ](#a05ab36e9ce0fd1d2c5d91d0256318cf2)   0x06 |
| #define | [BMP5\_ODR\_129\_8\_HZ](#a9e63a12359ee6558c3b07da5a9df6a20)   0x07 |
| #define | [BMP5\_ODR\_120\_HZ](#a98838acc2b3fd352f4d3833c5cf7f79e)   0x08 |
| #define | [BMP5\_ODR\_110\_1\_HZ](#a3edc36e9e1bdf619aef24de48affea45)   0x09 |
| #define | [BMP5\_ODR\_100\_2\_HZ](#a7f403705e7b523f2a3688376a06ebd0b)   0x0A |
| #define | [BMP5\_ODR\_89\_6\_HZ](#ae83cd45460b6d7234478ac0ecdc3c7ee)   0x0B |
| #define | [BMP5\_ODR\_80\_HZ](#af63d26c2145ce6cf6fa59f284dc628d5)   0x0C |
| #define | [BMP5\_ODR\_70\_HZ](#a4a5d9ae784ed454d9328744baf46080a)   0x0D |
| #define | [BMP5\_ODR\_60\_HZ](#ac0469a051ed6d0f59c6686c85b8e1f4c)   0x0E |
| #define | [BMP5\_ODR\_50\_HZ](#a74bb202e0555729a8b9098a144e598fa)   0x0F |
| #define | [BMP5\_ODR\_45\_HZ](#a92827fe8ec3acc4ce16a752c13b2ea54)   0x10 |
| #define | [BMP5\_ODR\_40\_HZ](#ab146e4e14d42d99a2f658c2d05b25b06)   0x11 |
| #define | [BMP5\_ODR\_35\_HZ](#a8755f64f4785137e46635564c343ee01)   0x12 |
| #define | [BMP5\_ODR\_30\_HZ](#a4235324ff2140539bd9f175e44bb6b5e)   0x13 |
| #define | [BMP5\_ODR\_25\_HZ](#ae56b323a929971f9d66538244a9145b0)   0x14 |
| #define | [BMP5\_ODR\_20\_HZ](#ad84abc3ec7e567f52cf71214c3d880a4)   0x15 |
| #define | [BMP5\_ODR\_15\_HZ](#a5243ee609c018ba9ffa6682d9da9a9f7)   0x16 |
| #define | [BMP5\_ODR\_10\_HZ](#a2949cee1435229d9480773b0bc15ce79)   0x17 |
| #define | [BMP5\_ODR\_05\_HZ](#a4a8339ab9586d1615bec332ca2a2fd1b)   0x18 |
| #define | [BMP5\_ODR\_04\_HZ](#a9680646ceb42c557deb9f96510b541ba)   0x19 |
| #define | [BMP5\_ODR\_03\_HZ](#a4740357d04ef977a42860cd974e48418)   0x1A |
| #define | [BMP5\_ODR\_02\_HZ](#adac8a3103dcd2d430c99aeda0d4c74ee)   0x1B |
| #define | [BMP5\_ODR\_01\_HZ](#a4e680bb7a1dc04eb880a35c4316ca0f6)   0x1C |
| #define | [BMP5\_ODR\_0\_5\_HZ](#a8b36eb7b8f7b1b69a30d8b6e7d9c3916)   0x1D |
| #define | [BMP5\_ODR\_0\_250\_HZ](#a70b3bbe281bb922fed76107e045946e7)   0x1E |
| #define | [BMP5\_ODR\_0\_125\_HZ](#a495c984829a594550179e96b6c08ebc0)   0x1F |
| #define | [BMP5\_OVERSAMPLING\_1X](#a12c3f441da334e280172e826452807b5)   0x00 |
| #define | [BMP5\_OVERSAMPLING\_2X](#ae04d4a049fa453901b93b7cd095f17ad)   0x01 |
| #define | [BMP5\_OVERSAMPLING\_4X](#af71a1a77eee2e57b627e200f060020f5)   0x02 |
| #define | [BMP5\_OVERSAMPLING\_8X](#ac6bad9c3800816fc28fb6aa7b34f7dae)   0x03 |
| #define | [BMP5\_OVERSAMPLING\_16X](#a4ba17c469da46a5dc519106807a3e7ab)   0x04 |
| #define | [BMP5\_OVERSAMPLING\_32X](#abce66cefc09f8209997eaef8d717b303)   0x05 |
| #define | [BMP5\_OVERSAMPLING\_64X](#a905256e59723dd54a3f7fc885bf2ee3a)   0x06 |
| #define | [BMP5\_OVERSAMPLING\_128X](#a28bf4f590a88d76a4c7aeafe69db459d)   0x07 |
| #define | [BMP5\_IIR\_FILTER\_BYPASS](#a75900213c0e1ef6250d5ae4afba78261)   0x00 |
| #define | [BMP5\_IIR\_FILTER\_COEFF\_1](#acef274a2a1bb65fa9c39c0a306e12b4d)   0x01 |
| #define | [BMP5\_IIR\_FILTER\_COEFF\_3](#acc37a0a23b2fb4586168bdc4e93c3b45)   0x02 |
| #define | [BMP5\_IIR\_FILTER\_COEFF\_7](#a7e0f68554716f0f968314d5e489fb429)   0x03 |
| #define | [BMP5\_IIR\_FILTER\_COEFF\_15](#a2972f3271c35c7b45e5c470e3e6b336b)   0x04 |
| #define | [BMP5\_IIR\_FILTER\_COEFF\_31](#ab4509b34b7803ee4b25d128e737f5103)   0x05 |
| #define | [BMP5\_IIR\_FILTER\_COEFF\_63](#a31be0ad7bf5c293c09f51bf51495b56e)   0x06 |
| #define | [BMP5\_IIR\_FILTER\_COEFF\_127](#a95d709c7b56b5f7bd6eb2e2c3aecb878)   0x07 |
| #define | [BMP5\_ATTR\_IIR\_CONFIG](#a57c276018d0ac606684751e19784457e)   ([SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) + 1u) |
| #define | [BMP5\_ATTR\_POWER\_MODE](#a4f6e56a0a4f9fd984d3993cf819281d8)   ([SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) + 2u) |

| Enumerations | |
| --- | --- |
| enum | [bmp5\_powermode](#aca06546e057d7295ca4f6ed4298247dc) {     [BMP5\_POWERMODE\_STANDBY](#aca06546e057d7295ca4f6ed4298247dca8f50ab92ba9607eaeed772ddbe92a15f) , [BMP5\_POWERMODE\_NORMAL](#aca06546e057d7295ca4f6ed4298247dcabb75d9c71965843c27724d956ffd1f8c) , [BMP5\_POWERMODE\_FORCED](#aca06546e057d7295ca4f6ed4298247dcaf57d41b2953f1986618de43ac1315b96) , [BMP5\_POWERMODE\_CONTINUOUS](#aca06546e057d7295ca4f6ed4298247dca14a304e989e6c079c9b6d668b4fd3e57) ,     [BMP5\_POWERMODE\_DEEP\_STANDBY](#aca06546e057d7295ca4f6ed4298247dca3904b0e3e14b2cad554436ba96fe4bf1)   } |

## Macro Definition Documentation

## [◆ ](#a57c276018d0ac606684751e19784457e)BMP5\_ATTR\_IIR\_CONFIG

| #define BMP5\_ATTR\_IIR\_CONFIG   ([SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) + 1u) |
| --- |

## [◆ ](#a4f6e56a0a4f9fd984d3993cf819281d8)BMP5\_ATTR\_POWER\_MODE

| #define BMP5\_ATTR\_POWER\_MODE   ([SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) + 2u) |
| --- |

## [◆ ](#a75900213c0e1ef6250d5ae4afba78261)BMP5\_IIR\_FILTER\_BYPASS

| #define BMP5\_IIR\_FILTER\_BYPASS   0x00 |
| --- |

## [◆ ](#acef274a2a1bb65fa9c39c0a306e12b4d)BMP5\_IIR\_FILTER\_COEFF\_1

| #define BMP5\_IIR\_FILTER\_COEFF\_1   0x01 |
| --- |

## [◆ ](#a95d709c7b56b5f7bd6eb2e2c3aecb878)BMP5\_IIR\_FILTER\_COEFF\_127

| #define BMP5\_IIR\_FILTER\_COEFF\_127   0x07 |
| --- |

## [◆ ](#a2972f3271c35c7b45e5c470e3e6b336b)BMP5\_IIR\_FILTER\_COEFF\_15

| #define BMP5\_IIR\_FILTER\_COEFF\_15   0x04 |
| --- |

## [◆ ](#acc37a0a23b2fb4586168bdc4e93c3b45)BMP5\_IIR\_FILTER\_COEFF\_3

| #define BMP5\_IIR\_FILTER\_COEFF\_3   0x02 |
| --- |

## [◆ ](#ab4509b34b7803ee4b25d128e737f5103)BMP5\_IIR\_FILTER\_COEFF\_31

| #define BMP5\_IIR\_FILTER\_COEFF\_31   0x05 |
| --- |

## [◆ ](#a31be0ad7bf5c293c09f51bf51495b56e)BMP5\_IIR\_FILTER\_COEFF\_63

| #define BMP5\_IIR\_FILTER\_COEFF\_63   0x06 |
| --- |

## [◆ ](#a7e0f68554716f0f968314d5e489fb429)BMP5\_IIR\_FILTER\_COEFF\_7

| #define BMP5\_IIR\_FILTER\_COEFF\_7   0x03 |
| --- |

## [◆ ](#a4e680bb7a1dc04eb880a35c4316ca0f6)BMP5\_ODR\_01\_HZ

| #define BMP5\_ODR\_01\_HZ   0x1C |
| --- |

## [◆ ](#adac8a3103dcd2d430c99aeda0d4c74ee)BMP5\_ODR\_02\_HZ

| #define BMP5\_ODR\_02\_HZ   0x1B |
| --- |

## [◆ ](#a4740357d04ef977a42860cd974e48418)BMP5\_ODR\_03\_HZ

| #define BMP5\_ODR\_03\_HZ   0x1A |
| --- |

## [◆ ](#a9680646ceb42c557deb9f96510b541ba)BMP5\_ODR\_04\_HZ

| #define BMP5\_ODR\_04\_HZ   0x19 |
| --- |

## [◆ ](#a4a8339ab9586d1615bec332ca2a2fd1b)BMP5\_ODR\_05\_HZ

| #define BMP5\_ODR\_05\_HZ   0x18 |
| --- |

## [◆ ](#a495c984829a594550179e96b6c08ebc0)BMP5\_ODR\_0\_125\_HZ

| #define BMP5\_ODR\_0\_125\_HZ   0x1F |
| --- |

## [◆ ](#a70b3bbe281bb922fed76107e045946e7)BMP5\_ODR\_0\_250\_HZ

| #define BMP5\_ODR\_0\_250\_HZ   0x1E |
| --- |

## [◆ ](#a8b36eb7b8f7b1b69a30d8b6e7d9c3916)BMP5\_ODR\_0\_5\_HZ

| #define BMP5\_ODR\_0\_5\_HZ   0x1D |
| --- |

## [◆ ](#a7f403705e7b523f2a3688376a06ebd0b)BMP5\_ODR\_100\_2\_HZ

| #define BMP5\_ODR\_100\_2\_HZ   0x0A |
| --- |

## [◆ ](#a2949cee1435229d9480773b0bc15ce79)BMP5\_ODR\_10\_HZ

| #define BMP5\_ODR\_10\_HZ   0x17 |
| --- |

## [◆ ](#a3edc36e9e1bdf619aef24de48affea45)BMP5\_ODR\_110\_1\_HZ

| #define BMP5\_ODR\_110\_1\_HZ   0x09 |
| --- |

## [◆ ](#a98838acc2b3fd352f4d3833c5cf7f79e)BMP5\_ODR\_120\_HZ

| #define BMP5\_ODR\_120\_HZ   0x08 |
| --- |

## [◆ ](#a9e63a12359ee6558c3b07da5a9df6a20)BMP5\_ODR\_129\_8\_HZ

| #define BMP5\_ODR\_129\_8\_HZ   0x07 |
| --- |

## [◆ ](#a05ab36e9ce0fd1d2c5d91d0256318cf2)BMP5\_ODR\_140\_HZ

| #define BMP5\_ODR\_140\_HZ   0x06 |
| --- |

## [◆ ](#a3f2bbfc335b62c474f1e6071d22f222f)BMP5\_ODR\_149\_3\_HZ

| #define BMP5\_ODR\_149\_3\_HZ   0x05 |
| --- |

## [◆ ](#a5243ee609c018ba9ffa6682d9da9a9f7)BMP5\_ODR\_15\_HZ

| #define BMP5\_ODR\_15\_HZ   0x16 |
| --- |

## [◆ ](#a032889481699ea7d2fa97490326099f5)BMP5\_ODR\_160\_HZ

| #define BMP5\_ODR\_160\_HZ   0x04 |
| --- |

## [◆ ](#a3d543b06bea45a25e4f9b881b9da239b)BMP5\_ODR\_179\_2\_HZ

| #define BMP5\_ODR\_179\_2\_HZ   0x03 |
| --- |

## [◆ ](#ac7ca04b5215289e4f193d45cc044d599)BMP5\_ODR\_199\_1\_HZ

| #define BMP5\_ODR\_199\_1\_HZ   0x02 |
| --- |

## [◆ ](#ad84abc3ec7e567f52cf71214c3d880a4)BMP5\_ODR\_20\_HZ

| #define BMP5\_ODR\_20\_HZ   0x15 |
| --- |

## [◆ ](#a8e9b8c29bd9660dcc1f6709d3cfcd5e3)BMP5\_ODR\_218\_5\_HZ

| #define BMP5\_ODR\_218\_5\_HZ   0x01 |
| --- |

## [◆ ](#a89faf45a4f0a750495eb60005fe00dbf)BMP5\_ODR\_240\_HZ

| #define BMP5\_ODR\_240\_HZ   0x00 |
| --- |

## [◆ ](#ae56b323a929971f9d66538244a9145b0)BMP5\_ODR\_25\_HZ

| #define BMP5\_ODR\_25\_HZ   0x14 |
| --- |

## [◆ ](#a4235324ff2140539bd9f175e44bb6b5e)BMP5\_ODR\_30\_HZ

| #define BMP5\_ODR\_30\_HZ   0x13 |
| --- |

## [◆ ](#a8755f64f4785137e46635564c343ee01)BMP5\_ODR\_35\_HZ

| #define BMP5\_ODR\_35\_HZ   0x12 |
| --- |

## [◆ ](#ab146e4e14d42d99a2f658c2d05b25b06)BMP5\_ODR\_40\_HZ

| #define BMP5\_ODR\_40\_HZ   0x11 |
| --- |

## [◆ ](#a92827fe8ec3acc4ce16a752c13b2ea54)BMP5\_ODR\_45\_HZ

| #define BMP5\_ODR\_45\_HZ   0x10 |
| --- |

## [◆ ](#a74bb202e0555729a8b9098a144e598fa)BMP5\_ODR\_50\_HZ

| #define BMP5\_ODR\_50\_HZ   0x0F |
| --- |

## [◆ ](#ac0469a051ed6d0f59c6686c85b8e1f4c)BMP5\_ODR\_60\_HZ

| #define BMP5\_ODR\_60\_HZ   0x0E |
| --- |

## [◆ ](#a4a5d9ae784ed454d9328744baf46080a)BMP5\_ODR\_70\_HZ

| #define BMP5\_ODR\_70\_HZ   0x0D |
| --- |

## [◆ ](#af63d26c2145ce6cf6fa59f284dc628d5)BMP5\_ODR\_80\_HZ

| #define BMP5\_ODR\_80\_HZ   0x0C |
| --- |

## [◆ ](#ae83cd45460b6d7234478ac0ecdc3c7ee)BMP5\_ODR\_89\_6\_HZ

| #define BMP5\_ODR\_89\_6\_HZ   0x0B |
| --- |

## [◆ ](#a28bf4f590a88d76a4c7aeafe69db459d)BMP5\_OVERSAMPLING\_128X

| #define BMP5\_OVERSAMPLING\_128X   0x07 |
| --- |

## [◆ ](#a4ba17c469da46a5dc519106807a3e7ab)BMP5\_OVERSAMPLING\_16X

| #define BMP5\_OVERSAMPLING\_16X   0x04 |
| --- |

## [◆ ](#a12c3f441da334e280172e826452807b5)BMP5\_OVERSAMPLING\_1X

| #define BMP5\_OVERSAMPLING\_1X   0x00 |
| --- |

## [◆ ](#ae04d4a049fa453901b93b7cd095f17ad)BMP5\_OVERSAMPLING\_2X

| #define BMP5\_OVERSAMPLING\_2X   0x01 |
| --- |

## [◆ ](#abce66cefc09f8209997eaef8d717b303)BMP5\_OVERSAMPLING\_32X

| #define BMP5\_OVERSAMPLING\_32X   0x05 |
| --- |

## [◆ ](#af71a1a77eee2e57b627e200f060020f5)BMP5\_OVERSAMPLING\_4X

| #define BMP5\_OVERSAMPLING\_4X   0x02 |
| --- |

## [◆ ](#a905256e59723dd54a3f7fc885bf2ee3a)BMP5\_OVERSAMPLING\_64X

| #define BMP5\_OVERSAMPLING\_64X   0x06 |
| --- |

## [◆ ](#ac6bad9c3800816fc28fb6aa7b34f7dae)BMP5\_OVERSAMPLING\_8X

| #define BMP5\_OVERSAMPLING\_8X   0x03 |
| --- |

## [◆ ](#ac6d7556e6fa16e07512a92e86f85df88)BMP5\_SEA\_LEVEL\_PRESSURE\_PA

| #define BMP5\_SEA\_LEVEL\_PRESSURE\_PA   101325 |
| --- |

## Enumeration Type Documentation

## [◆ ](#aca06546e057d7295ca4f6ed4298247dc)bmp5\_powermode

| enum [bmp5\_powermode](#aca06546e057d7295ca4f6ed4298247dc) |
| --- |

| Enumerator | |
| --- | --- |
| BMP5\_POWERMODE\_STANDBY | Standby powermode. |
| BMP5\_POWERMODE\_NORMAL | Normal powermode. |
| BMP5\_POWERMODE\_FORCED | Forced powermode. |
| BMP5\_POWERMODE\_CONTINUOUS | Continuous powermode. |
| BMP5\_POWERMODE\_DEEP\_STANDBY | Deep standby powermode. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [bmp581\_user.h](bmp581__user_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
