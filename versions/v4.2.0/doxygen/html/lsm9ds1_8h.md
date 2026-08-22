---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/lsm9ds1_8h.html
original_path: doxygen/html/lsm9ds1_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lsm9ds1.h File Reference

[Go to the source code of this file.](lsm9ds1_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LSM9DS1\_DT\_FS\_2G](#aa0f17393c9ff976e0ee0c110ecc72473)   0 |
| #define | [LSM9DS1\_DT\_FS\_16G](#a2db5ff66fa97b7b4bb5915843b1bb6f6)   1 |
| #define | [LSM9DS1\_DT\_FS\_4G](#a7535ca239218a5e9356c6246b938caaf)   2 |
| #define | [LSM9DS1\_DT\_FS\_8G](#a6afa3768fd367db78b1e3f7deac5508e)   3 |
| #define | [LSM9DS1\_DT\_FS\_245DPS](#a088dba4db0ddde1687db351ed03b1538)   0 |
| #define | [LSM9DS1\_DT\_FS\_500DPS](#a8e32311fa33f06c0003d41fac83d4121)   1 |
| #define | [LSM9DS1\_DT\_FS\_2000DPS](#aa6a1e7e28d197dd28b2e13a40a521015)   3 |
| #define | [LSM9DS1\_IMU\_OFF](#ab7f0150bb6481d55f759f64f7c502edf)   0x00 |
| #define | [LSM9DS1\_GY\_OFF\_XL\_10Hz](#ae897ff93c37f7254c016349cfc48466e)   0x10 |
| #define | [LSM9DS1\_GY\_OFF\_XL\_50Hz](#a055b320d6158932562f10ef2d2b96a97)   0x20 |
| #define | [LSM9DS1\_GY\_OFF\_XL\_119Hz](#a4d7b97ebeba2cb8007372755021a5de8)   0x30 |
| #define | [LSM9DS1\_GY\_OFF\_XL\_238Hz](#aa9db97ee52368cabd1c3ccd7cbd3f1a4)   0x40 |
| #define | [LSM9DS1\_GY\_OFF\_XL\_476Hz](#ad3318f2c48533b3822d7c6fafe224373)   0x50 |
| #define | [LSM9DS1\_GY\_OFF\_XL\_952Hz](#a086c4d1c8287d40be3437f05f3227db7)   0x60 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_14Hz9](#a393366ba14c5db7ed1a5ff95a85adae7)   0x01 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_59Hz5](#aff981b33a86e8d93268ec9e144c1e761)   0x02 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_119Hz](#afe2f271b51a0ea6cf5ce29f03f761054)   0x03 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_238Hz](#aa9d2c6c89ef7bb5d1d543b8bcc39b392)   0x04 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_476Hz](#af7af84f2ee96d01fe3f031e5b09217ff)   0x05 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_952Hz](#abcb55995e6b3de4aa23dc804b88eb409)   0x06 |
| #define | [LSM9DS1\_IMU\_14Hz9](#af65ec4dc4c5075282380da389b68a77b)   0x11 |
| #define | [LSM9DS1\_IMU\_59Hz5](#a571432113f63d003e7c3e242b6509093)   0x22 |
| #define | [LSM9DS1\_IMU\_119Hz](#a71e8c41d54062e315ecd72f933160208)   0x33 |
| #define | [LSM9DS1\_IMU\_238Hz](#a3a8b6d1a000a7d4e1fdb6bcc0a70243d)   0x44 |
| #define | [LSM9DS1\_IMU\_476Hz](#a5a09b132476058df9906e58d0755386c)   0x55 |
| #define | [LSM9DS1\_IMU\_952Hz](#a5fe83cf26a6024edeb2ff759ee20d3c8)   0x66 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_14Hz9\_LP](#a6bbd0b822cc47491d6048f7d71478c9b)   0x81 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_59Hz5\_LP](#aca3c0f2e322a39f56fa9a5fa70497df6)   0x82 |
| #define | [LSM9DS1\_XL\_OFF\_GY\_119Hz\_LP](#a98e7b9e3924622147f73be90f00bd1ba)   0x83 |
| #define | [LSM9DS1\_IMU\_14Hz9\_LP](#a61e50f3183b7541a81fe2907752f7375)   0x91 |
| #define | [LSM9DS1\_IMU\_59Hz5\_LP](#a5b991524e1cec97295c9a1bfdcf31708)   0xA2 |
| #define | [LSM9DS1\_IMU\_119Hz\_LP](#a20088ff32a83f6a368d36ae138629452)   0xB3 |
| #define | [LSM9DS1\_DT\_FS\_4Ga](#aa268b28f8b86b3cef6a82e38609160c9)   0 |
| #define | [LSM9DS1\_DT\_FS\_8Ga](#a3106e0cabbb21625faf2af9ae8250262)   1 |
| #define | [LSM9DS1\_DT\_FS\_12Ga](#a539af8febdf954010ef673afe2c5ee73)   2 |
| #define | [LSM9DS1\_DT\_FS\_16Ga](#acf7c7ab63f7255bac3bebc1f4dc007f3)   3 |
| #define | [LSM9DS1\_MAG\_POWER\_DOWN](#a7963c9a3003168a8a52dce50054bc96f)   0xC0 |
| #define | [LSM9DS1\_MAG\_LP\_0Hz625](#a002a92d8c6cf9ba80d80033e972645ef)   0x00 |
| #define | [LSM9DS1\_MAG\_LP\_1Hz25](#a13f527ae76cb0677f94968496d530a13)   0x01 |
| #define | [LSM9DS1\_MAG\_LP\_2Hz5](#a758b8866ffcd4c654ab457e1f0521d09)   0x02 |
| #define | [LSM9DS1\_MAG\_LP\_5Hz](#a30dcf54cd4be8c55dac82932ad7a37b2)   0x03 |
| #define | [LSM9DS1\_MAG\_LP\_10Hz](#a9ef4b743a50dfd2b1d5db86bc6495644)   0x04 |
| #define | [LSM9DS1\_MAG\_LP\_20Hz](#a4e575f4fb5326777f50531556d1353a3)   0x05 |
| #define | [LSM9DS1\_MAG\_LP\_40Hz](#a0b4eaacf63176e5231f137ab0ce56d99)   0x06 |
| #define | [LSM9DS1\_MAG\_LP\_80Hz](#a724fade6479c4f729dec15448df15e97)   0x07 |
| #define | [LSM9DS1\_MAG\_MP\_0Hz625](#a6d6e2f72b0dc4aa6bcd5d15842f65e7f)   0x10 |
| #define | [LSM9DS1\_MAG\_MP\_1Hz25](#aafe3cfba4bc8cbc7e74e3410aefaea17)   0x11 |
| #define | [LSM9DS1\_MAG\_MP\_2Hz5](#a106068e9984c230a9044b5c1dca25fa5)   0x12 |
| #define | [LSM9DS1\_MAG\_MP\_5Hz](#a6ba7628e2ee8564d8fab308eb2a3eef4)   0x13 |
| #define | [LSM9DS1\_MAG\_MP\_10Hz](#aab920f8d82ff7795dc155482d5c25814)   0x14 |
| #define | [LSM9DS1\_MAG\_MP\_20Hz](#a2fefcffec0ca84714c22930bf571cb59)   0x15 |
| #define | [LSM9DS1\_MAG\_MP\_40Hz](#a64d18383987182bf4bf1e53f2b453eac)   0x16 |
| #define | [LSM9DS1\_MAG\_MP\_80Hz](#a3471c091bd2aa1e74806ecb346d6596f)   0x17 |
| #define | [LSM9DS1\_MAG\_HP\_0Hz625](#a8a2acdcf03dbf680d4a426ce40c8febd)   0x20 |
| #define | [LSM9DS1\_MAG\_HP\_1Hz25](#a45dd09f8821be6c22c566b849fdc8809)   0x21 |
| #define | [LSM9DS1\_MAG\_HP\_2Hz5](#a453c9c2cd3c8c3cb06269ca4dd9618d5)   0x22 |
| #define | [LSM9DS1\_MAG\_HP\_5Hz](#afcaa83b806529e561a6aa56c43e11fbf)   0x23 |
| #define | [LSM9DS1\_MAG\_HP\_10Hz](#af1b8bbaf138fb569f9940d9ce463ed8d)   0x24 |
| #define | [LSM9DS1\_MAG\_HP\_20Hz](#a8a36029449d53745c049809e21277694)   0x25 |
| #define | [LSM9DS1\_MAG\_HP\_40Hz](#a31edee3a33e9a0b80b750db1c65e8b1b)   0x26 |
| #define | [LSM9DS1\_MAG\_HP\_80Hz](#a932221535b82f140d9d27c671b3a1dea)   0x27 |
| #define | [LSM9DS1\_MAG\_UHP\_0Hz625](#a32701c13ef1b3a1f0f7729559494a05e)   0x30 |
| #define | [LSM9DS1\_MAG\_UHP\_1Hz25](#a5fe24fb1f5d2a406988ed21a468a2c65)   0x31 |
| #define | [LSM9DS1\_MAG\_UHP\_2Hz5](#a5ee91247f5ac37f1b7039e5f94d812b4)   0x32 |
| #define | [LSM9DS1\_MAG\_UHP\_5Hz](#adec6d523b553139aec1434b4f82f092b)   0x33 |
| #define | [LSM9DS1\_MAG\_UHP\_10Hz](#ae984af176e83d363d81eac84fb3d110c)   0x34 |
| #define | [LSM9DS1\_MAG\_UHP\_20Hz](#a52a1f1cb2ec277d35efc15d69d291d7f)   0x35 |
| #define | [LSM9DS1\_MAG\_UHP\_40Hz](#a4831ab9b2168d875f3031894264a2628)   0x36 |
| #define | [LSM9DS1\_MAG\_UHP\_80Hz](#a2da3adcf32e4a22b8663ee011317c907)   0x37 |
| #define | [LSM9DS1\_MAG\_UHP\_155Hz](#aa0f179e3e3f3c65461e405329d723cec)   0x38 |
| #define | [LSM9DS1\_MAG\_HP\_300Hz](#ae7fb9f552e7a91943291b42e14883cfa)   0x28 |
| #define | [LSM9DS1\_MAG\_MP\_560Hz](#a94294a103d745a8967f28df3a9e0e8d6)   0x18 |
| #define | [LSM9DS1\_MAG\_LP\_1000Hz](#a2347bfea0c970effe93f8cc48bb9e567)   0x08 |
| #define | [LSM9DS1\_MAG\_ONE\_SHOT](#a0f5049091c9bf8123cd6bf110ae95a99)   0x70 |

## Macro Definition Documentation

## [◆ ](#a539af8febdf954010ef673afe2c5ee73)LSM9DS1\_DT\_FS\_12Ga

| #define LSM9DS1\_DT\_FS\_12Ga   2 |
| --- |

## [◆ ](#a2db5ff66fa97b7b4bb5915843b1bb6f6)LSM9DS1\_DT\_FS\_16G

| #define LSM9DS1\_DT\_FS\_16G   1 |
| --- |

## [◆ ](#acf7c7ab63f7255bac3bebc1f4dc007f3)LSM9DS1\_DT\_FS\_16Ga

| #define LSM9DS1\_DT\_FS\_16Ga   3 |
| --- |

## [◆ ](#aa6a1e7e28d197dd28b2e13a40a521015)LSM9DS1\_DT\_FS\_2000DPS

| #define LSM9DS1\_DT\_FS\_2000DPS   3 |
| --- |

## [◆ ](#a088dba4db0ddde1687db351ed03b1538)LSM9DS1\_DT\_FS\_245DPS

| #define LSM9DS1\_DT\_FS\_245DPS   0 |
| --- |

## [◆ ](#aa0f17393c9ff976e0ee0c110ecc72473)LSM9DS1\_DT\_FS\_2G

| #define LSM9DS1\_DT\_FS\_2G   0 |
| --- |

## [◆ ](#a7535ca239218a5e9356c6246b938caaf)LSM9DS1\_DT\_FS\_4G

| #define LSM9DS1\_DT\_FS\_4G   2 |
| --- |

## [◆ ](#aa268b28f8b86b3cef6a82e38609160c9)LSM9DS1\_DT\_FS\_4Ga

| #define LSM9DS1\_DT\_FS\_4Ga   0 |
| --- |

## [◆ ](#a8e32311fa33f06c0003d41fac83d4121)LSM9DS1\_DT\_FS\_500DPS

| #define LSM9DS1\_DT\_FS\_500DPS   1 |
| --- |

## [◆ ](#a6afa3768fd367db78b1e3f7deac5508e)LSM9DS1\_DT\_FS\_8G

| #define LSM9DS1\_DT\_FS\_8G   3 |
| --- |

## [◆ ](#a3106e0cabbb21625faf2af9ae8250262)LSM9DS1\_DT\_FS\_8Ga

| #define LSM9DS1\_DT\_FS\_8Ga   1 |
| --- |

## [◆ ](#ae897ff93c37f7254c016349cfc48466e)LSM9DS1\_GY\_OFF\_XL\_10Hz

| #define LSM9DS1\_GY\_OFF\_XL\_10Hz   0x10 |
| --- |

## [◆ ](#a4d7b97ebeba2cb8007372755021a5de8)LSM9DS1\_GY\_OFF\_XL\_119Hz

| #define LSM9DS1\_GY\_OFF\_XL\_119Hz   0x30 |
| --- |

## [◆ ](#aa9db97ee52368cabd1c3ccd7cbd3f1a4)LSM9DS1\_GY\_OFF\_XL\_238Hz

| #define LSM9DS1\_GY\_OFF\_XL\_238Hz   0x40 |
| --- |

## [◆ ](#ad3318f2c48533b3822d7c6fafe224373)LSM9DS1\_GY\_OFF\_XL\_476Hz

| #define LSM9DS1\_GY\_OFF\_XL\_476Hz   0x50 |
| --- |

## [◆ ](#a055b320d6158932562f10ef2d2b96a97)LSM9DS1\_GY\_OFF\_XL\_50Hz

| #define LSM9DS1\_GY\_OFF\_XL\_50Hz   0x20 |
| --- |

## [◆ ](#a086c4d1c8287d40be3437f05f3227db7)LSM9DS1\_GY\_OFF\_XL\_952Hz

| #define LSM9DS1\_GY\_OFF\_XL\_952Hz   0x60 |
| --- |

## [◆ ](#a71e8c41d54062e315ecd72f933160208)LSM9DS1\_IMU\_119Hz

| #define LSM9DS1\_IMU\_119Hz   0x33 |
| --- |

## [◆ ](#a20088ff32a83f6a368d36ae138629452)LSM9DS1\_IMU\_119Hz\_LP

| #define LSM9DS1\_IMU\_119Hz\_LP   0xB3 |
| --- |

## [◆ ](#af65ec4dc4c5075282380da389b68a77b)LSM9DS1\_IMU\_14Hz9

| #define LSM9DS1\_IMU\_14Hz9   0x11 |
| --- |

## [◆ ](#a61e50f3183b7541a81fe2907752f7375)LSM9DS1\_IMU\_14Hz9\_LP

| #define LSM9DS1\_IMU\_14Hz9\_LP   0x91 |
| --- |

## [◆ ](#a3a8b6d1a000a7d4e1fdb6bcc0a70243d)LSM9DS1\_IMU\_238Hz

| #define LSM9DS1\_IMU\_238Hz   0x44 |
| --- |

## [◆ ](#a5a09b132476058df9906e58d0755386c)LSM9DS1\_IMU\_476Hz

| #define LSM9DS1\_IMU\_476Hz   0x55 |
| --- |

## [◆ ](#a571432113f63d003e7c3e242b6509093)LSM9DS1\_IMU\_59Hz5

| #define LSM9DS1\_IMU\_59Hz5   0x22 |
| --- |

## [◆ ](#a5b991524e1cec97295c9a1bfdcf31708)LSM9DS1\_IMU\_59Hz5\_LP

| #define LSM9DS1\_IMU\_59Hz5\_LP   0xA2 |
| --- |

## [◆ ](#a5fe83cf26a6024edeb2ff759ee20d3c8)LSM9DS1\_IMU\_952Hz

| #define LSM9DS1\_IMU\_952Hz   0x66 |
| --- |

## [◆ ](#ab7f0150bb6481d55f759f64f7c502edf)LSM9DS1\_IMU\_OFF

| #define LSM9DS1\_IMU\_OFF   0x00 |
| --- |

## [◆ ](#a8a2acdcf03dbf680d4a426ce40c8febd)LSM9DS1\_MAG\_HP\_0Hz625

| #define LSM9DS1\_MAG\_HP\_0Hz625   0x20 |
| --- |

## [◆ ](#af1b8bbaf138fb569f9940d9ce463ed8d)LSM9DS1\_MAG\_HP\_10Hz

| #define LSM9DS1\_MAG\_HP\_10Hz   0x24 |
| --- |

## [◆ ](#a45dd09f8821be6c22c566b849fdc8809)LSM9DS1\_MAG\_HP\_1Hz25

| #define LSM9DS1\_MAG\_HP\_1Hz25   0x21 |
| --- |

## [◆ ](#a8a36029449d53745c049809e21277694)LSM9DS1\_MAG\_HP\_20Hz

| #define LSM9DS1\_MAG\_HP\_20Hz   0x25 |
| --- |

## [◆ ](#a453c9c2cd3c8c3cb06269ca4dd9618d5)LSM9DS1\_MAG\_HP\_2Hz5

| #define LSM9DS1\_MAG\_HP\_2Hz5   0x22 |
| --- |

## [◆ ](#ae7fb9f552e7a91943291b42e14883cfa)LSM9DS1\_MAG\_HP\_300Hz

| #define LSM9DS1\_MAG\_HP\_300Hz   0x28 |
| --- |

## [◆ ](#a31edee3a33e9a0b80b750db1c65e8b1b)LSM9DS1\_MAG\_HP\_40Hz

| #define LSM9DS1\_MAG\_HP\_40Hz   0x26 |
| --- |

## [◆ ](#afcaa83b806529e561a6aa56c43e11fbf)LSM9DS1\_MAG\_HP\_5Hz

| #define LSM9DS1\_MAG\_HP\_5Hz   0x23 |
| --- |

## [◆ ](#a932221535b82f140d9d27c671b3a1dea)LSM9DS1\_MAG\_HP\_80Hz

| #define LSM9DS1\_MAG\_HP\_80Hz   0x27 |
| --- |

## [◆ ](#a002a92d8c6cf9ba80d80033e972645ef)LSM9DS1\_MAG\_LP\_0Hz625

| #define LSM9DS1\_MAG\_LP\_0Hz625   0x00 |
| --- |

## [◆ ](#a2347bfea0c970effe93f8cc48bb9e567)LSM9DS1\_MAG\_LP\_1000Hz

| #define LSM9DS1\_MAG\_LP\_1000Hz   0x08 |
| --- |

## [◆ ](#a9ef4b743a50dfd2b1d5db86bc6495644)LSM9DS1\_MAG\_LP\_10Hz

| #define LSM9DS1\_MAG\_LP\_10Hz   0x04 |
| --- |

## [◆ ](#a13f527ae76cb0677f94968496d530a13)LSM9DS1\_MAG\_LP\_1Hz25

| #define LSM9DS1\_MAG\_LP\_1Hz25   0x01 |
| --- |

## [◆ ](#a4e575f4fb5326777f50531556d1353a3)LSM9DS1\_MAG\_LP\_20Hz

| #define LSM9DS1\_MAG\_LP\_20Hz   0x05 |
| --- |

## [◆ ](#a758b8866ffcd4c654ab457e1f0521d09)LSM9DS1\_MAG\_LP\_2Hz5

| #define LSM9DS1\_MAG\_LP\_2Hz5   0x02 |
| --- |

## [◆ ](#a0b4eaacf63176e5231f137ab0ce56d99)LSM9DS1\_MAG\_LP\_40Hz

| #define LSM9DS1\_MAG\_LP\_40Hz   0x06 |
| --- |

## [◆ ](#a30dcf54cd4be8c55dac82932ad7a37b2)LSM9DS1\_MAG\_LP\_5Hz

| #define LSM9DS1\_MAG\_LP\_5Hz   0x03 |
| --- |

## [◆ ](#a724fade6479c4f729dec15448df15e97)LSM9DS1\_MAG\_LP\_80Hz

| #define LSM9DS1\_MAG\_LP\_80Hz   0x07 |
| --- |

## [◆ ](#a6d6e2f72b0dc4aa6bcd5d15842f65e7f)LSM9DS1\_MAG\_MP\_0Hz625

| #define LSM9DS1\_MAG\_MP\_0Hz625   0x10 |
| --- |

## [◆ ](#aab920f8d82ff7795dc155482d5c25814)LSM9DS1\_MAG\_MP\_10Hz

| #define LSM9DS1\_MAG\_MP\_10Hz   0x14 |
| --- |

## [◆ ](#aafe3cfba4bc8cbc7e74e3410aefaea17)LSM9DS1\_MAG\_MP\_1Hz25

| #define LSM9DS1\_MAG\_MP\_1Hz25   0x11 |
| --- |

## [◆ ](#a2fefcffec0ca84714c22930bf571cb59)LSM9DS1\_MAG\_MP\_20Hz

| #define LSM9DS1\_MAG\_MP\_20Hz   0x15 |
| --- |

## [◆ ](#a106068e9984c230a9044b5c1dca25fa5)LSM9DS1\_MAG\_MP\_2Hz5

| #define LSM9DS1\_MAG\_MP\_2Hz5   0x12 |
| --- |

## [◆ ](#a64d18383987182bf4bf1e53f2b453eac)LSM9DS1\_MAG\_MP\_40Hz

| #define LSM9DS1\_MAG\_MP\_40Hz   0x16 |
| --- |

## [◆ ](#a94294a103d745a8967f28df3a9e0e8d6)LSM9DS1\_MAG\_MP\_560Hz

| #define LSM9DS1\_MAG\_MP\_560Hz   0x18 |
| --- |

## [◆ ](#a6ba7628e2ee8564d8fab308eb2a3eef4)LSM9DS1\_MAG\_MP\_5Hz

| #define LSM9DS1\_MAG\_MP\_5Hz   0x13 |
| --- |

## [◆ ](#a3471c091bd2aa1e74806ecb346d6596f)LSM9DS1\_MAG\_MP\_80Hz

| #define LSM9DS1\_MAG\_MP\_80Hz   0x17 |
| --- |

## [◆ ](#a0f5049091c9bf8123cd6bf110ae95a99)LSM9DS1\_MAG\_ONE\_SHOT

| #define LSM9DS1\_MAG\_ONE\_SHOT   0x70 |
| --- |

## [◆ ](#a7963c9a3003168a8a52dce50054bc96f)LSM9DS1\_MAG\_POWER\_DOWN

| #define LSM9DS1\_MAG\_POWER\_DOWN   0xC0 |
| --- |

## [◆ ](#a32701c13ef1b3a1f0f7729559494a05e)LSM9DS1\_MAG\_UHP\_0Hz625

| #define LSM9DS1\_MAG\_UHP\_0Hz625   0x30 |
| --- |

## [◆ ](#ae984af176e83d363d81eac84fb3d110c)LSM9DS1\_MAG\_UHP\_10Hz

| #define LSM9DS1\_MAG\_UHP\_10Hz   0x34 |
| --- |

## [◆ ](#aa0f179e3e3f3c65461e405329d723cec)LSM9DS1\_MAG\_UHP\_155Hz

| #define LSM9DS1\_MAG\_UHP\_155Hz   0x38 |
| --- |

## [◆ ](#a5fe24fb1f5d2a406988ed21a468a2c65)LSM9DS1\_MAG\_UHP\_1Hz25

| #define LSM9DS1\_MAG\_UHP\_1Hz25   0x31 |
| --- |

## [◆ ](#a52a1f1cb2ec277d35efc15d69d291d7f)LSM9DS1\_MAG\_UHP\_20Hz

| #define LSM9DS1\_MAG\_UHP\_20Hz   0x35 |
| --- |

## [◆ ](#a5ee91247f5ac37f1b7039e5f94d812b4)LSM9DS1\_MAG\_UHP\_2Hz5

| #define LSM9DS1\_MAG\_UHP\_2Hz5   0x32 |
| --- |

## [◆ ](#a4831ab9b2168d875f3031894264a2628)LSM9DS1\_MAG\_UHP\_40Hz

| #define LSM9DS1\_MAG\_UHP\_40Hz   0x36 |
| --- |

## [◆ ](#adec6d523b553139aec1434b4f82f092b)LSM9DS1\_MAG\_UHP\_5Hz

| #define LSM9DS1\_MAG\_UHP\_5Hz   0x33 |
| --- |

## [◆ ](#a2da3adcf32e4a22b8663ee011317c907)LSM9DS1\_MAG\_UHP\_80Hz

| #define LSM9DS1\_MAG\_UHP\_80Hz   0x37 |
| --- |

## [◆ ](#afe2f271b51a0ea6cf5ce29f03f761054)LSM9DS1\_XL\_OFF\_GY\_119Hz

| #define LSM9DS1\_XL\_OFF\_GY\_119Hz   0x03 |
| --- |

## [◆ ](#a98e7b9e3924622147f73be90f00bd1ba)LSM9DS1\_XL\_OFF\_GY\_119Hz\_LP

| #define LSM9DS1\_XL\_OFF\_GY\_119Hz\_LP   0x83 |
| --- |

## [◆ ](#a393366ba14c5db7ed1a5ff95a85adae7)LSM9DS1\_XL\_OFF\_GY\_14Hz9

| #define LSM9DS1\_XL\_OFF\_GY\_14Hz9   0x01 |
| --- |

## [◆ ](#a6bbd0b822cc47491d6048f7d71478c9b)LSM9DS1\_XL\_OFF\_GY\_14Hz9\_LP

| #define LSM9DS1\_XL\_OFF\_GY\_14Hz9\_LP   0x81 |
| --- |

## [◆ ](#aa9d2c6c89ef7bb5d1d543b8bcc39b392)LSM9DS1\_XL\_OFF\_GY\_238Hz

| #define LSM9DS1\_XL\_OFF\_GY\_238Hz   0x04 |
| --- |

## [◆ ](#af7af84f2ee96d01fe3f031e5b09217ff)LSM9DS1\_XL\_OFF\_GY\_476Hz

| #define LSM9DS1\_XL\_OFF\_GY\_476Hz   0x05 |
| --- |

## [◆ ](#aff981b33a86e8d93268ec9e144c1e761)LSM9DS1\_XL\_OFF\_GY\_59Hz5

| #define LSM9DS1\_XL\_OFF\_GY\_59Hz5   0x02 |
| --- |

## [◆ ](#aca3c0f2e322a39f56fa9a5fa70497df6)LSM9DS1\_XL\_OFF\_GY\_59Hz5\_LP

| #define LSM9DS1\_XL\_OFF\_GY\_59Hz5\_LP   0x82 |
| --- |

## [◆ ](#abcb55995e6b3de4aa23dc804b88eb409)LSM9DS1\_XL\_OFF\_GY\_952Hz

| #define LSM9DS1\_XL\_OFF\_GY\_952Hz   0x06 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm9ds1.h](lsm9ds1_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
