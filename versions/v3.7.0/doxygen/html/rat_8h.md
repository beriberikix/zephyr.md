---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rat_8h.html
original_path: doxygen/html/rat_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rat.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](rat_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [address\_trans\_region\_config](structaddress__trans__region__config.md) |
|  | Region config structure. [More...](structaddress__trans__region__config.md#details) |
| struct | [address\_trans\_params](structaddress__trans__params.md) |
|  | Parameters for address\_trans\_init. [More...](structaddress__trans__params.md#details) |

| Macros | |
| --- | --- |
| #define | [ADDR\_TRANSLATE\_MAX\_REGIONS](#a6fbe67ecd2ee230303753783d8d4d51b)   (16u) |
| #define | [RAT\_CTRL](#ac29ba66726ab4ddf65f06ec9ebafdaf9)(base\_addr, i) |
| #define | [RAT\_BASE](#a4dd3fc4f79f31651f7f13ff0150048cb)(base\_addr, i) |
| #define | [RAT\_TRANS\_L](#a8e1b0d98277bc23e55e588b0c14aff81)(base\_addr, i) |
| #define | [RAT\_TRANS\_H](#ae8a0ae682e7618fc081fc2ede237265f)(base\_addr, i) |
| #define | [RAT\_CTRL\_W](#a2a9d73f6745d1fa2343d739fc9c1f94d)(enable, size) |

| Enumerations | |
| --- | --- |
| enum | [address\_trans\_region\_size](#add39d351d9d3b5e5e0b1ed6a7dd0881e) {     [address\_trans\_region\_size\_1](#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f58d582cd0c756345d5006804405df3) = 0x0 , [address\_trans\_region\_size\_2](#add39d351d9d3b5e5e0b1ed6a7dd0881ea04dbfa2d52dfefb293092f9e11a23113) , [address\_trans\_region\_size\_4](#add39d351d9d3b5e5e0b1ed6a7dd0881ead08d9d6124c8069651e7fa624fa9271a) , [address\_trans\_region\_size\_8](#add39d351d9d3b5e5e0b1ed6a7dd0881ead2486648f0256c8fafffc92d8d9008ae) ,     [address\_trans\_region\_size\_16](#add39d351d9d3b5e5e0b1ed6a7dd0881ea5700badf7a90fb967dd354ac0fc11164) , [address\_trans\_region\_size\_32](#add39d351d9d3b5e5e0b1ed6a7dd0881ea175247673aabe51988328e3baf4d7f2c) , [address\_trans\_region\_size\_64](#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f7389ecd49b7263e9c33613b32ff6a5) , [address\_trans\_region\_size\_128](#add39d351d9d3b5e5e0b1ed6a7dd0881ea4b17e36f5f39f920c78e684df121abef) ,     [address\_trans\_region\_size\_256](#add39d351d9d3b5e5e0b1ed6a7dd0881eaf97a04aae5b62d1bf686dadf7fe5323b) , [address\_trans\_region\_size\_512](#add39d351d9d3b5e5e0b1ed6a7dd0881ea32eb15028196cf30411c597e8815e3f0) , [address\_trans\_region\_size\_1K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea040a8134c953aecc21244a345df155df) , [address\_trans\_region\_size\_2K](#add39d351d9d3b5e5e0b1ed6a7dd0881eae6615e1cd2c34edb18b09d84cd8f2d63) ,     [address\_trans\_region\_size\_4K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea83dd8600901fe070cab760e1b16c9252) , [address\_trans\_region\_size\_8K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea1a5c0ad9be70669316c2f3b0bf5f2b12) , [address\_trans\_region\_size\_16K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea072693f3fe262f442ff8036fe9d762d8) , [address\_trans\_region\_size\_32K](#add39d351d9d3b5e5e0b1ed6a7dd0881eadd5defe08d296c7236eb9651a79b82a4) ,     [address\_trans\_region\_size\_64K](#add39d351d9d3b5e5e0b1ed6a7dd0881eac866cbba7ad7848f22a6b023e983188f) , [address\_trans\_region\_size\_128K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea8950584e532d0e7d5dfe84d9df9df555) , [address\_trans\_region\_size\_256K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea564588b427d38b1137e73a47748f2c8a) , [address\_trans\_region\_size\_512K](#add39d351d9d3b5e5e0b1ed6a7dd0881eac4940c1e11068d9c74878b209a09acaa) ,     [address\_trans\_region\_size\_1M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea051f8ca6c90e483782a79baa69c24d5a) , [address\_trans\_region\_size\_2M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea5807a3fe19aba5a9ecfe472200a3fe79) , [address\_trans\_region\_size\_4M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea602aefd08974ed3b66687205f32cc2af) , [address\_trans\_region\_size\_8M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea81426462fbe9681a39a6e3d172ab6f22) ,     [address\_trans\_region\_size\_16M](#add39d351d9d3b5e5e0b1ed6a7dd0881eadcdcbcc90bfdd2f718bacf063d5efbf1) , [address\_trans\_region\_size\_32M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea7b851d6026a73d2ed29ae928a858a054) , [address\_trans\_region\_size\_64M](#add39d351d9d3b5e5e0b1ed6a7dd0881eabb0fb07483fd4c7da7a7a93484aebb55) , [address\_trans\_region\_size\_128M](#add39d351d9d3b5e5e0b1ed6a7dd0881eaa1fb7f23f29fa23f03435cecdcce95c2) ,     [address\_trans\_region\_size\_256M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea11b12b2dc0d87f01571a85e4d4d2b925) , [address\_trans\_region\_size\_512M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea279d93a8260daf631aa0199469af0b53) , [address\_trans\_region\_size\_1G](#add39d351d9d3b5e5e0b1ed6a7dd0881eab293b5d29ef308e02c7920235c7f848c) , [address\_trans\_region\_size\_2G](#add39d351d9d3b5e5e0b1ed6a7dd0881ead7490f34d6aa5b45f1704ce985645fc1) ,     [address\_trans\_region\_size\_4G](#add39d351d9d3b5e5e0b1ed6a7dd0881ea1b125b2f8bab78b4d2a504cebed559c2)   } |
|  | Enum's to represent different possible region size for the address translate module. [More...](#add39d351d9d3b5e5e0b1ed6a7dd0881e) |

| Functions | |
| --- | --- |
| void | [sys\_mm\_drv\_ti\_rat\_init](#a3df25e5ff3b79d701d6ce979ab3f1b65) (void \*region\_config, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rat\_base\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) translate\_regions) |

## Macro Definition Documentation

## [◆ ](#a6fbe67ecd2ee230303753783d8d4d51b)ADDR\_TRANSLATE\_MAX\_REGIONS

| #define ADDR\_TRANSLATE\_MAX\_REGIONS   (16u) |
| --- |

## [◆ ](#a4dd3fc4f79f31651f7f13ff0150048cb)RAT\_BASE

| #define RAT\_BASE | ( |  | *base\_addr*, |
| --- | --- | --- | --- |
|  |  |  | *i* ) |

**Value:**

(base\_addr + 0x24 + 0x10 \* (i))

## [◆ ](#ac29ba66726ab4ddf65f06ec9ebafdaf9)RAT\_CTRL

| #define RAT\_CTRL | ( |  | *base\_addr*, |
| --- | --- | --- | --- |
|  |  |  | *i* ) |

**Value:**

(base\_addr + 0x20 + 0x10 \* (i))

## [◆ ](#a2a9d73f6745d1fa2343d739fc9c1f94d)RAT\_CTRL\_W

| #define RAT\_CTRL\_W | ( |  | *enable*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

**Value:**

(((enable & 0x1) << 31u) | (size & 0x3F))

## [◆ ](#ae8a0ae682e7618fc081fc2ede237265f)RAT\_TRANS\_H

| #define RAT\_TRANS\_H | ( |  | *base\_addr*, |
| --- | --- | --- | --- |
|  |  |  | *i* ) |

**Value:**

(base\_addr + 0x2C + 0x10 \* (i))

## [◆ ](#a8e1b0d98277bc23e55e588b0c14aff81)RAT\_TRANS\_L

| #define RAT\_TRANS\_L | ( |  | *base\_addr*, |
| --- | --- | --- | --- |
|  |  |  | *i* ) |

**Value:**

(base\_addr + 0x28 + 0x10 \* (i))

## Enumeration Type Documentation

## [◆ ](#add39d351d9d3b5e5e0b1ed6a7dd0881e)address\_trans\_region\_size

| enum [address\_trans\_region\_size](#add39d351d9d3b5e5e0b1ed6a7dd0881e) |
| --- |

Enum's to represent different possible region size for the address translate module.

| Enumerator | |
| --- | --- |
| address\_trans\_region\_size\_1 |  |
| address\_trans\_region\_size\_2 |  |
| address\_trans\_region\_size\_4 |  |
| address\_trans\_region\_size\_8 |  |
| address\_trans\_region\_size\_16 |  |
| address\_trans\_region\_size\_32 |  |
| address\_trans\_region\_size\_64 |  |
| address\_trans\_region\_size\_128 |  |
| address\_trans\_region\_size\_256 |  |
| address\_trans\_region\_size\_512 |  |
| address\_trans\_region\_size\_1K |  |
| address\_trans\_region\_size\_2K |  |
| address\_trans\_region\_size\_4K |  |
| address\_trans\_region\_size\_8K |  |
| address\_trans\_region\_size\_16K |  |
| address\_trans\_region\_size\_32K |  |
| address\_trans\_region\_size\_64K |  |
| address\_trans\_region\_size\_128K |  |
| address\_trans\_region\_size\_256K |  |
| address\_trans\_region\_size\_512K |  |
| address\_trans\_region\_size\_1M |  |
| address\_trans\_region\_size\_2M |  |
| address\_trans\_region\_size\_4M |  |
| address\_trans\_region\_size\_8M |  |
| address\_trans\_region\_size\_16M |  |
| address\_trans\_region\_size\_32M |  |
| address\_trans\_region\_size\_64M |  |
| address\_trans\_region\_size\_128M |  |
| address\_trans\_region\_size\_256M |  |
| address\_trans\_region\_size\_512M |  |
| address\_trans\_region\_size\_1G |  |
| address\_trans\_region\_size\_2G |  |
| address\_trans\_region\_size\_4G |  |

## Function Documentation

## [◆ ](#a3df25e5ff3b79d701d6ce979ab3f1b65)sys\_mm\_drv\_ti\_rat\_init()

| void sys\_mm\_drv\_ti\_rat\_init | ( | void \* | *region\_config*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *rat\_base\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *translate\_regions* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mm](dir_464cfbc388e9245b11da9b89dd2be842.md)
- [rat.h](rat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
