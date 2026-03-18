---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rat_8h_source.html
original_path: doxygen/html/rat_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rat.h

[Go to the documentation of this file.](rat_8h.md)

1/\*

2 \* Copyright (c) 2023 Texas Instruments Incorporated

3 \* Copyright (c) 2023 L Lakshmanan

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_RAT\_H\_

9#define ZEPHYR\_INCLUDE\_RAT\_H\_

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

15#include <[stdint.h](stdint_8h.md)>

16

[ 17](rat_8h.md#a6fbe67ecd2ee230303753783d8d4d51b)#define ADDR\_TRANSLATE\_MAX\_REGIONS (16u)

[ 18](rat_8h.md#ac29ba66726ab4ddf65f06ec9ebafdaf9)#define RAT\_CTRL(base\_addr, i) (base\_addr + 0x20 + 0x10 \* (i))

[ 19](rat_8h.md#a4dd3fc4f79f31651f7f13ff0150048cb)#define RAT\_BASE(base\_addr, i) (base\_addr + 0x24 + 0x10 \* (i))

[ 20](rat_8h.md#a8e1b0d98277bc23e55e588b0c14aff81)#define RAT\_TRANS\_L(base\_addr, i) (base\_addr + 0x28 + 0x10 \* (i))

[ 21](rat_8h.md#ae8a0ae682e7618fc081fc2ede237265f)#define RAT\_TRANS\_H(base\_addr, i) (base\_addr + 0x2C + 0x10 \* (i))

[ 22](rat_8h.md#a2a9d73f6745d1fa2343d739fc9c1f94d)#define RAT\_CTRL\_W(enable, size) (((enable & 0x1) << 31u) | (size & 0x3F))

23

[ 27](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881e)enum [address\_trans\_region\_size](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881e) {

[ 28](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f58d582cd0c756345d5006804405df3) [address\_trans\_region\_size\_1](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f58d582cd0c756345d5006804405df3) = 0x0,

[ 29](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea04dbfa2d52dfefb293092f9e11a23113) [address\_trans\_region\_size\_2](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea04dbfa2d52dfefb293092f9e11a23113),

[ 30](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead08d9d6124c8069651e7fa624fa9271a) [address\_trans\_region\_size\_4](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead08d9d6124c8069651e7fa624fa9271a),

[ 31](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead2486648f0256c8fafffc92d8d9008ae) [address\_trans\_region\_size\_8](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead2486648f0256c8fafffc92d8d9008ae),

[ 32](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea5700badf7a90fb967dd354ac0fc11164) [address\_trans\_region\_size\_16](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea5700badf7a90fb967dd354ac0fc11164),

[ 33](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea175247673aabe51988328e3baf4d7f2c) [address\_trans\_region\_size\_32](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea175247673aabe51988328e3baf4d7f2c),

[ 34](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f7389ecd49b7263e9c33613b32ff6a5) [address\_trans\_region\_size\_64](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f7389ecd49b7263e9c33613b32ff6a5),

[ 35](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea4b17e36f5f39f920c78e684df121abef) [address\_trans\_region\_size\_128](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea4b17e36f5f39f920c78e684df121abef),

[ 36](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eaf97a04aae5b62d1bf686dadf7fe5323b) [address\_trans\_region\_size\_256](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eaf97a04aae5b62d1bf686dadf7fe5323b),

[ 37](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea32eb15028196cf30411c597e8815e3f0) [address\_trans\_region\_size\_512](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea32eb15028196cf30411c597e8815e3f0),

[ 38](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea040a8134c953aecc21244a345df155df) [address\_trans\_region\_size\_1K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea040a8134c953aecc21244a345df155df),

[ 39](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eae6615e1cd2c34edb18b09d84cd8f2d63) [address\_trans\_region\_size\_2K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eae6615e1cd2c34edb18b09d84cd8f2d63),

[ 40](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea83dd8600901fe070cab760e1b16c9252) [address\_trans\_region\_size\_4K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea83dd8600901fe070cab760e1b16c9252),

[ 41](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea1a5c0ad9be70669316c2f3b0bf5f2b12) [address\_trans\_region\_size\_8K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea1a5c0ad9be70669316c2f3b0bf5f2b12),

[ 42](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea072693f3fe262f442ff8036fe9d762d8) [address\_trans\_region\_size\_16K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea072693f3fe262f442ff8036fe9d762d8),

[ 43](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eadd5defe08d296c7236eb9651a79b82a4) [address\_trans\_region\_size\_32K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eadd5defe08d296c7236eb9651a79b82a4),

[ 44](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eac866cbba7ad7848f22a6b023e983188f) [address\_trans\_region\_size\_64K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eac866cbba7ad7848f22a6b023e983188f),

[ 45](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8950584e532d0e7d5dfe84d9df9df555) [address\_trans\_region\_size\_128K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8950584e532d0e7d5dfe84d9df9df555),

[ 46](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea564588b427d38b1137e73a47748f2c8a) [address\_trans\_region\_size\_256K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea564588b427d38b1137e73a47748f2c8a),

[ 47](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eac4940c1e11068d9c74878b209a09acaa) [address\_trans\_region\_size\_512K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eac4940c1e11068d9c74878b209a09acaa),

[ 48](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea051f8ca6c90e483782a79baa69c24d5a) [address\_trans\_region\_size\_1M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea051f8ca6c90e483782a79baa69c24d5a),

[ 49](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea5807a3fe19aba5a9ecfe472200a3fe79) [address\_trans\_region\_size\_2M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea5807a3fe19aba5a9ecfe472200a3fe79),

[ 50](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea602aefd08974ed3b66687205f32cc2af) [address\_trans\_region\_size\_4M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea602aefd08974ed3b66687205f32cc2af),

[ 51](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea81426462fbe9681a39a6e3d172ab6f22) [address\_trans\_region\_size\_8M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea81426462fbe9681a39a6e3d172ab6f22),

[ 52](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eadcdcbcc90bfdd2f718bacf063d5efbf1) [address\_trans\_region\_size\_16M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eadcdcbcc90bfdd2f718bacf063d5efbf1),

[ 53](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea7b851d6026a73d2ed29ae928a858a054) [address\_trans\_region\_size\_32M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea7b851d6026a73d2ed29ae928a858a054),

[ 54](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eabb0fb07483fd4c7da7a7a93484aebb55) [address\_trans\_region\_size\_64M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eabb0fb07483fd4c7da7a7a93484aebb55),

[ 55](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eaa1fb7f23f29fa23f03435cecdcce95c2) [address\_trans\_region\_size\_128M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eaa1fb7f23f29fa23f03435cecdcce95c2),

[ 56](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea11b12b2dc0d87f01571a85e4d4d2b925) [address\_trans\_region\_size\_256M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea11b12b2dc0d87f01571a85e4d4d2b925),

[ 57](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea279d93a8260daf631aa0199469af0b53) [address\_trans\_region\_size\_512M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea279d93a8260daf631aa0199469af0b53),

[ 58](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eab293b5d29ef308e02c7920235c7f848c) [address\_trans\_region\_size\_1G](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eab293b5d29ef308e02c7920235c7f848c),

[ 59](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead7490f34d6aa5b45f1704ce985645fc1) [address\_trans\_region\_size\_2G](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead7490f34d6aa5b45f1704ce985645fc1),

[ 60](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea1b125b2f8bab78b4d2a504cebed559c2) [address\_trans\_region\_size\_4G](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea1b125b2f8bab78b4d2a504cebed559c2)

61};

62

[ 66](structaddress__trans__region__config.md)struct [address\_trans\_region\_config](structaddress__trans__region__config.md) {

[ 67](structaddress__trans__region__config.md#ab5ad2baec37c5949f099ff9e32016cc5) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [system\_addr](structaddress__trans__region__config.md#ab5ad2baec37c5949f099ff9e32016cc5);

[ 68](structaddress__trans__region__config.md#ae58869e0b4be0e52d9a39d4a29733843) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [local\_addr](structaddress__trans__region__config.md#ae58869e0b4be0e52d9a39d4a29733843);

[ 69](structaddress__trans__region__config.md#a0cae76338ca84e5de894f2def9272ddd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structaddress__trans__region__config.md#a0cae76338ca84e5de894f2def9272ddd);

70};

71

[ 75](structaddress__trans__params.md)struct [address\_trans\_params](structaddress__trans__params.md) {

[ 76](structaddress__trans__params.md#a1ea9c3785d02e9f5124786c3da7dc4e7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_regions](structaddress__trans__params.md#a1ea9c3785d02e9f5124786c3da7dc4e7);

[ 77](structaddress__trans__params.md#a9bcd9e881f8acff531f100ad06ab8e2d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rat\_base\_addr](structaddress__trans__params.md#a9bcd9e881f8acff531f100ad06ab8e2d);

[ 78](structaddress__trans__params.md#a28afbd17772097ab9aabcbc654e364e0) struct [address\_trans\_region\_config](structaddress__trans__region__config.md) \*[region\_config](structaddress__trans__params.md#a28afbd17772097ab9aabcbc654e364e0);

79};

80

[ 81](rat_8h.md#a3df25e5ff3b79d701d6ce979ab3f1b65)void [sys\_mm\_drv\_ti\_rat\_init](rat_8h.md#a3df25e5ff3b79d701d6ce979ab3f1b65)(void \*region\_config, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rat\_base\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) translate\_regions);

82

83#ifdef \_\_cplusplus

84}

85#endif

86

87#endif /\* ZEPHYR\_INCLUDE\_RAT\_H\_ \*/

[sys\_mm\_drv\_ti\_rat\_init](rat_8h.md#a3df25e5ff3b79d701d6ce979ab3f1b65)

void sys\_mm\_drv\_ti\_rat\_init(void \*region\_config, uint64\_t rat\_base\_addr, uint8\_t translate\_regions)

[address\_trans\_region\_size](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881e)

address\_trans\_region\_size

Enum's to represent different possible region size for the address translate module.

**Definition** rat.h:27

[address\_trans\_region\_size\_1K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea040a8134c953aecc21244a345df155df)

@ address\_trans\_region\_size\_1K

**Definition** rat.h:38

[address\_trans\_region\_size\_2](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea04dbfa2d52dfefb293092f9e11a23113)

@ address\_trans\_region\_size\_2

**Definition** rat.h:29

[address\_trans\_region\_size\_1M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea051f8ca6c90e483782a79baa69c24d5a)

@ address\_trans\_region\_size\_1M

**Definition** rat.h:48

[address\_trans\_region\_size\_16K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea072693f3fe262f442ff8036fe9d762d8)

@ address\_trans\_region\_size\_16K

**Definition** rat.h:42

[address\_trans\_region\_size\_256M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea11b12b2dc0d87f01571a85e4d4d2b925)

@ address\_trans\_region\_size\_256M

**Definition** rat.h:56

[address\_trans\_region\_size\_32](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea175247673aabe51988328e3baf4d7f2c)

@ address\_trans\_region\_size\_32

**Definition** rat.h:33

[address\_trans\_region\_size\_8K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea1a5c0ad9be70669316c2f3b0bf5f2b12)

@ address\_trans\_region\_size\_8K

**Definition** rat.h:41

[address\_trans\_region\_size\_4G](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea1b125b2f8bab78b4d2a504cebed559c2)

@ address\_trans\_region\_size\_4G

**Definition** rat.h:60

[address\_trans\_region\_size\_512M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea279d93a8260daf631aa0199469af0b53)

@ address\_trans\_region\_size\_512M

**Definition** rat.h:57

[address\_trans\_region\_size\_512](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea32eb15028196cf30411c597e8815e3f0)

@ address\_trans\_region\_size\_512

**Definition** rat.h:37

[address\_trans\_region\_size\_128](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea4b17e36f5f39f920c78e684df121abef)

@ address\_trans\_region\_size\_128

**Definition** rat.h:35

[address\_trans\_region\_size\_256K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea564588b427d38b1137e73a47748f2c8a)

@ address\_trans\_region\_size\_256K

**Definition** rat.h:46

[address\_trans\_region\_size\_16](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea5700badf7a90fb967dd354ac0fc11164)

@ address\_trans\_region\_size\_16

**Definition** rat.h:32

[address\_trans\_region\_size\_2M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea5807a3fe19aba5a9ecfe472200a3fe79)

@ address\_trans\_region\_size\_2M

**Definition** rat.h:49

[address\_trans\_region\_size\_4M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea602aefd08974ed3b66687205f32cc2af)

@ address\_trans\_region\_size\_4M

**Definition** rat.h:50

[address\_trans\_region\_size\_32M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea7b851d6026a73d2ed29ae928a858a054)

@ address\_trans\_region\_size\_32M

**Definition** rat.h:53

[address\_trans\_region\_size\_8M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea81426462fbe9681a39a6e3d172ab6f22)

@ address\_trans\_region\_size\_8M

**Definition** rat.h:51

[address\_trans\_region\_size\_4K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea83dd8600901fe070cab760e1b16c9252)

@ address\_trans\_region\_size\_4K

**Definition** rat.h:40

[address\_trans\_region\_size\_128K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8950584e532d0e7d5dfe84d9df9df555)

@ address\_trans\_region\_size\_128K

**Definition** rat.h:45

[address\_trans\_region\_size\_1](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f58d582cd0c756345d5006804405df3)

@ address\_trans\_region\_size\_1

**Definition** rat.h:28

[address\_trans\_region\_size\_64](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f7389ecd49b7263e9c33613b32ff6a5)

@ address\_trans\_region\_size\_64

**Definition** rat.h:34

[address\_trans\_region\_size\_128M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eaa1fb7f23f29fa23f03435cecdcce95c2)

@ address\_trans\_region\_size\_128M

**Definition** rat.h:55

[address\_trans\_region\_size\_1G](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eab293b5d29ef308e02c7920235c7f848c)

@ address\_trans\_region\_size\_1G

**Definition** rat.h:58

[address\_trans\_region\_size\_64M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eabb0fb07483fd4c7da7a7a93484aebb55)

@ address\_trans\_region\_size\_64M

**Definition** rat.h:54

[address\_trans\_region\_size\_512K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eac4940c1e11068d9c74878b209a09acaa)

@ address\_trans\_region\_size\_512K

**Definition** rat.h:47

[address\_trans\_region\_size\_64K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eac866cbba7ad7848f22a6b023e983188f)

@ address\_trans\_region\_size\_64K

**Definition** rat.h:44

[address\_trans\_region\_size\_4](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead08d9d6124c8069651e7fa624fa9271a)

@ address\_trans\_region\_size\_4

**Definition** rat.h:30

[address\_trans\_region\_size\_8](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead2486648f0256c8fafffc92d8d9008ae)

@ address\_trans\_region\_size\_8

**Definition** rat.h:31

[address\_trans\_region\_size\_2G](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881ead7490f34d6aa5b45f1704ce985645fc1)

@ address\_trans\_region\_size\_2G

**Definition** rat.h:59

[address\_trans\_region\_size\_16M](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eadcdcbcc90bfdd2f718bacf063d5efbf1)

@ address\_trans\_region\_size\_16M

**Definition** rat.h:52

[address\_trans\_region\_size\_32K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eadd5defe08d296c7236eb9651a79b82a4)

@ address\_trans\_region\_size\_32K

**Definition** rat.h:43

[address\_trans\_region\_size\_2K](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eae6615e1cd2c34edb18b09d84cd8f2d63)

@ address\_trans\_region\_size\_2K

**Definition** rat.h:39

[address\_trans\_region\_size\_256](rat_8h.md#add39d351d9d3b5e5e0b1ed6a7dd0881eaf97a04aae5b62d1bf686dadf7fe5323b)

@ address\_trans\_region\_size\_256

**Definition** rat.h:36

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[address\_trans\_params](structaddress__trans__params.md)

Parameters for address\_trans\_init.

**Definition** rat.h:75

[address\_trans\_params::num\_regions](structaddress__trans__params.md#a1ea9c3785d02e9f5124786c3da7dc4e7)

uint32\_t num\_regions

**Definition** rat.h:76

[address\_trans\_params::region\_config](structaddress__trans__params.md#a28afbd17772097ab9aabcbc654e364e0)

struct address\_trans\_region\_config \* region\_config

**Definition** rat.h:78

[address\_trans\_params::rat\_base\_addr](structaddress__trans__params.md#a9bcd9e881f8acff531f100ad06ab8e2d)

uint32\_t rat\_base\_addr

**Definition** rat.h:77

[address\_trans\_region\_config](structaddress__trans__region__config.md)

Region config structure.

**Definition** rat.h:66

[address\_trans\_region\_config::size](structaddress__trans__region__config.md#a0cae76338ca84e5de894f2def9272ddd)

uint32\_t size

**Definition** rat.h:69

[address\_trans\_region\_config::system\_addr](structaddress__trans__region__config.md#ab5ad2baec37c5949f099ff9e32016cc5)

uint64\_t system\_addr

**Definition** rat.h:67

[address\_trans\_region\_config::local\_addr](structaddress__trans__region__config.md#ae58869e0b4be0e52d9a39d4a29733843)

uint32\_t local\_addr

**Definition** rat.h:68

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mm](dir_464cfbc388e9245b11da9b89dd2be842.md)
- [rat.h](rat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
