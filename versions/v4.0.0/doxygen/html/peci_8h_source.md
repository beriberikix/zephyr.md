---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/peci_8h_source.html
original_path: doxygen/html/peci_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

peci.h

[Go to the documentation of this file.](peci_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PECI\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_PECI\_H\_

14

23

24#include <[errno.h](errno_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <stddef.h>

27#include <[zephyr/device.h](device_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 36](group__peci__interface.md#ga76ad37d4317b48311cf23cf516549544)enum [peci\_error\_code](group__peci__interface.md#ga76ad37d4317b48311cf23cf516549544) {

[ 37](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f) [PECI\_GENERAL\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f) = 0x8000,

[ 38](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41) [PECI\_UNDERFLOW\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41) = 0x8002,

[ 39](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2) [PECI\_OVERFLOW\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2) = 0x8003,

40};

41

[ 45](group__peci__interface.md#gacd243f64973f7bdcc8c999dc14ed2bd6)enum [peci\_command\_code](group__peci__interface.md#gacd243f64973f7bdcc8c999dc14ed2bd6) {

[ 46](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d) [PECI\_CMD\_PING](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d) = 0x00,

[ 47](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf) [PECI\_CMD\_GET\_TEMP0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf) = 0x01,

[ 48](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c) [PECI\_CMD\_GET\_TEMP1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c) = 0x02,

[ 49](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d) [PECI\_CMD\_RD\_PCI\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d) = 0x61,

[ 50](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa) [PECI\_CMD\_RD\_PCI\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa) = 0x62,

[ 51](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc) [PECI\_CMD\_WR\_PCI\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc) = 0x65,

[ 52](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12) [PECI\_CMD\_WR\_PCI\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12) = 0x66,

[ 53](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523) [PECI\_CMD\_RD\_PKG\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523) = 0xA1,

[ 54](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed) [PECI\_CMD\_RD\_PKG\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed) = 0xA,

[ 55](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55) [PECI\_CMD\_WR\_PKG\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55) = 0xA5,

[ 56](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95) [PECI\_CMD\_WR\_PKG\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95) = 0xA6,

[ 57](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10) [PECI\_CMD\_RD\_IAMSR0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10) = 0xB1,

[ 58](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53) [PECI\_CMD\_RD\_IAMSR1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53) = 0xB2,

[ 59](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2) [PECI\_CMD\_WR\_IAMSR0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2) = 0xB5,

[ 60](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3) [PECI\_CMD\_WR\_IAMSR1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3) = 0xB6,

[ 61](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5) [PECI\_CMD\_RD\_PCI\_CFG\_LOCAL0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5) = 0xE1,

[ 62](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c) [PECI\_CMD\_RD\_PCI\_CFG\_LOCAL1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c) = 0xE2,

[ 63](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158) [PECI\_CMD\_WR\_PCI\_CFG\_LOCAL0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158) = 0xE5,

[ 64](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd) [PECI\_CMD\_WR\_PCI\_CFG\_LOCAL1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd) = 0xE6,

[ 65](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8) [PECI\_CMD\_GET\_DIB](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8) = 0xF7,

66};

67

[ 72](group__peci__interface.md#gaaa72e987f7345168055de5dc4e206d05)#define PECI\_CC\_RSP\_SUCCESS (0x40U)

[ 73](group__peci__interface.md#ga797ae69ec374fb64bb89f944f6985c6d)#define PECI\_CC\_RSP\_TIMEOUT (0x80U)

[ 74](group__peci__interface.md#gaac992f1ccc084c3ea5f517cd3fba8271)#define PECI\_CC\_OUT\_OF\_RESOURCES\_TIMEOUT (0x81U)

[ 75](group__peci__interface.md#gaae8cfb17318fa562c45c797c24e69abe)#define PECI\_CC\_RESOURCES\_LOWPWR\_TIMEOUT (0x82U)

[ 76](group__peci__interface.md#gac26eca50fb7dd2b899ae0e820bbb4412)#define PECI\_CC\_ILLEGAL\_REQUEST (0x90U)

78

[ 83](group__peci__interface.md#ga22a92f0547fd1fe30dd413b071f53d22)#define PECI\_PING\_WR\_LEN (0U)

[ 84](group__peci__interface.md#ga28b67489837aa513c987a56cfd2a52ed)#define PECI\_PING\_RD\_LEN (0U)

[ 85](group__peci__interface.md#ga260b7df883f39c44ac77c0504688fcd4)#define PECI\_PING\_LEN (3U)

87

[ 92](group__peci__interface.md#ga326203908d537fd303b865a32100d45b)#define PECI\_GET\_DIB\_WR\_LEN (1U)

[ 93](group__peci__interface.md#gaa3da9245648157eed5d483dd934b3874)#define PECI\_GET\_DIB\_RD\_LEN (8U)

[ 94](group__peci__interface.md#gad7c7732a98738308f4f3f5f4e3cc29ee)#define PECI\_GET\_DIB\_CMD\_LEN (4U)

[ 95](group__peci__interface.md#ga679c229499e6669bdf577dad45b51da2)#define PECI\_GET\_DIB\_DEVINFO (0U)

[ 96](group__peci__interface.md#ga83fab6ba4c3ee0df1997b322bc28d986)#define PECI\_GET\_DIB\_REVNUM (1U)

[ 97](group__peci__interface.md#ga4fad3e307b5eee6de75b2e9d5b7c5252)#define PECI\_GET\_DIB\_DOMAIN\_BIT\_MASK (0x4U)

[ 98](group__peci__interface.md#ga56be056f7286d8633a9dcad3904aadc6)#define PECI\_GET\_DIB\_MAJOR\_REV\_MASK 0xF0

[ 99](group__peci__interface.md#gaaaf4e2450fe327826451899458011669)#define PECI\_GET\_DIB\_MINOR\_REV\_MASK 0x0F

101

[ 106](group__peci__interface.md#ga782d004f484ba89a2a85552b1367f5e3)#define PECI\_GET\_TEMP\_WR\_LEN (1U)

[ 107](group__peci__interface.md#ga8abc4778c30a938b891e45595e1a05bb)#define PECI\_GET\_TEMP\_RD\_LEN (2U)

[ 108](group__peci__interface.md#gac9eb9af198bcad988f756e5bbfa610e6)#define PECI\_GET\_TEMP\_CMD\_LEN (4U)

[ 109](group__peci__interface.md#gac57d46b51397b3f86ab1850e45a14d8d)#define PECI\_GET\_TEMP\_LSB (0U)

[ 110](group__peci__interface.md#gab10cf44c7f53989d0d3eb7646c7a2ebf)#define PECI\_GET\_TEMP\_MSB (1U)

[ 111](group__peci__interface.md#ga0a748818ab3e256a372a1444fbbeb4d2)#define PECI\_GET\_TEMP\_ERR\_MSB (0x80U)

[ 112](group__peci__interface.md#ga5c8b7afaf9e84ffc289551bf65d27888)#define PECI\_GET\_TEMP\_ERR\_LSB\_GENERAL (0x0U)

[ 113](group__peci__interface.md#ga5fc4196ce832e80a9219ab66b6018b40)#define PECI\_GET\_TEMP\_ERR\_LSB\_RES (0x1U)

[ 114](group__peci__interface.md#ga48cdea4c953b8f9f71fc4d38cc9e1b52)#define PECI\_GET\_TEMP\_ERR\_LSB\_TEMP\_LO (0x2U)

[ 115](group__peci__interface.md#ga3d13f32e4aa52df7f5a14bfbe7bef310)#define PECI\_GET\_TEMP\_ERR\_LSB\_TEMP\_HI (0x3U)

117

[ 122](group__peci__interface.md#ga14c5301c855e0fd6d3e6ce2671ca2630)#define PECI\_RD\_PKG\_WR\_LEN (5U)

[ 123](group__peci__interface.md#gae73ca3befdbc95c6ed95fa64deca40f2)#define PECI\_RD\_PKG\_LEN\_BYTE (2U)

[ 124](group__peci__interface.md#ga8b37ea69eb7194fb68162fabcf47abd4)#define PECI\_RD\_PKG\_LEN\_WORD (3U)

[ 125](group__peci__interface.md#ga7ffc8df46be38442238e3a1913d80a43)#define PECI\_RD\_PKG\_LEN\_DWORD (5U)

[ 126](group__peci__interface.md#ga617975c279fa6c25d00c3611388c7c87)#define PECI\_RD\_PKG\_CMD\_LEN (8U)

128

[ 133](group__peci__interface.md#ga3a48be4c578e26e0425281d8dc45b675)#define PECI\_WR\_PKG\_RD\_LEN (1U)

[ 134](group__peci__interface.md#ga25a60618673b02a987049d7bf9e0d177)#define PECI\_WR\_PKG\_LEN\_BYTE (7U)

[ 135](group__peci__interface.md#ga3b3bb82e32dfb47e642485cd90046805)#define PECI\_WR\_PKG\_LEN\_WORD (8U)

[ 136](group__peci__interface.md#gae47cf47f1bacc97b29da8a77754b1856)#define PECI\_WR\_PKG\_LEN\_DWORD (10U)

[ 137](group__peci__interface.md#ga44721cfff04cf37a9dad8e6290efadd8)#define PECI\_WR\_PKG\_CMD\_LEN (9U)

139

[ 144](group__peci__interface.md#ga32a758a9489a4dc40a6f451a33b3873e)#define PECI\_RD\_IAMSR\_WR\_LEN (5U)

[ 145](group__peci__interface.md#gac1a68fb49b86937dbbcea02a6e38678e)#define PECI\_RD\_IAMSR\_LEN\_BYTE (2U)

[ 146](group__peci__interface.md#gad95974df60609e97652d090aaeb15dbd)#define PECI\_RD\_IAMSR\_LEN\_WORD (3U)

[ 147](group__peci__interface.md#gaee3af8380685c9162102439790c43bca)#define PECI\_RD\_IAMSR\_LEN\_DWORD (5U)

[ 148](group__peci__interface.md#ga6075e0aabf13898467ce99bd32234acd)#define PECI\_RD\_IAMSR\_LEN\_QWORD (9U)

[ 149](group__peci__interface.md#gaac4377037fe078d06ba711ffd92ece3a)#define PECI\_RD\_IAMSR\_CMD\_LEN (8U)

151

[ 156](group__peci__interface.md#ga84bac67b2d70a27b029ef58a37b18656)#define PECI\_WR\_IAMSR\_RD\_LEN (1U)

[ 157](group__peci__interface.md#gacff3b7ae6bc7b054a9b14474372a4932)#define PECI\_WR\_IAMSR\_LEN\_BYTE (7U)

[ 158](group__peci__interface.md#ga2a9278a92885a8dc23254ced8e717dee)#define PECI\_WR\_IAMSR\_LEN\_WORD (8U)

[ 159](group__peci__interface.md#ga0fdcb8d4cddc7f8bf778253f17b8d622)#define PECI\_WR\_IAMSR\_LEN\_DWORD (10U)

[ 160](group__peci__interface.md#gaa53d79877fa3a8df479edae01fdb02cc)#define PECI\_WR\_IAMSR\_LEN\_QWORD (14U)

[ 161](group__peci__interface.md#gaf6743aec8256e30c862470d20401c80b)#define PECI\_WR\_IAMSR\_CMD\_LEN (9U)

163

[ 168](group__peci__interface.md#ga28d95625dca7dcd18009b8a9d1af1b40)#define PECI\_RD\_PCICFG\_WR\_LEN (6U)

[ 169](group__peci__interface.md#gae64fc86f4a5dc7ffa4317312eba25ace)#define PECI\_RD\_PCICFG\_LEN\_BYTE (2U)

[ 170](group__peci__interface.md#gaac909c672633eb8aea767eca556e9684)#define PECI\_RD\_PCICFG\_LEN\_WORD (3U)

[ 171](group__peci__interface.md#gaee3c84370914cb27509ea9a91ca5f6b9)#define PECI\_RD\_PCICFG\_LEN\_DWORD (5U)

[ 172](group__peci__interface.md#ga8bec0be2c5762df6a451b322f4652f8a)#define PECI\_RD\_PCICFG\_CMD\_LEN (9U)

174

[ 179](group__peci__interface.md#gac81baf9413648e72cd12c5a0a4afafb1)#define PECI\_WR\_PCICFG\_RD\_LEN (1U)

[ 180](group__peci__interface.md#ga74d1759fc8b25a191af7a50f929b3ccc)#define PECI\_WR\_PCICFG\_LEN\_BYTE (8U)

[ 181](group__peci__interface.md#ga94107bc6d6384cac4a93f2dc31d4ff0a)#define PECI\_WR\_PCICFG\_LEN\_WORD (9U)

[ 182](group__peci__interface.md#gab2ec9a3f5b1cd095c510b8526ecfb788)#define PECI\_WR\_PCICFG\_LEN\_DWORD (11U)

[ 183](group__peci__interface.md#ga431b61c8b4a2e3d12aa681abec3433fa)#define PECI\_WR\_PCICFG\_CMD\_LEN (10U)

185

[ 190](group__peci__interface.md#ga60ba164ab5036ce14dc2f18daf0c264e)#define PECI\_RD\_PCICFGL\_WR\_LEN (5U)

[ 191](group__peci__interface.md#ga712626f9f7ec395fa0781b3a2f7b5cfb)#define PECI\_RD\_PCICFGL\_RD\_LEN\_BYTE (2U)

[ 192](group__peci__interface.md#ga27dfea893aa66268fcb938152cff4974)#define PECI\_RD\_PCICFGL\_RD\_LEN\_WORD (3U)

[ 193](group__peci__interface.md#ga3df08231dc4cec3f8c8706c7a63421d1)#define PECI\_RD\_PCICFGL\_RD\_LEN\_DWORD (5U)

[ 194](group__peci__interface.md#gaf9fd6d6eefe3133aec4e6ee2d682a238)#define PECI\_RD\_PCICFGL\_CMD\_LEN (8U)

196

[ 201](group__peci__interface.md#ga8063cf05f9f26b28219e5fece331717d)#define PECI\_WR\_PCICFGL\_RD\_LEN (1U)

[ 202](group__peci__interface.md#gac3cd61027ba11b6a0304c51616e17be9)#define PECI\_WR\_PCICFGL\_WR\_LEN\_BYTE (7U)

[ 203](group__peci__interface.md#ga240fcf510dc8f3aae66ca45750b6939f)#define PECI\_WR\_PCICFGL\_WR\_LEN\_WORD (8U)

[ 204](group__peci__interface.md#gad33f4be78198ba75fdcde410a5660b39)#define PECI\_WR\_PCICFGL\_WR\_LEN\_DWORD (10U)

[ 205](group__peci__interface.md#gaa9fcd8acb3578585afbbda38b76e40c3)#define PECI\_WR\_PCICFGL\_CMD\_LEN (9U)

207

[ 211](structpeci__buf.md)struct [peci\_buf](structpeci__buf.md) {

[ 215](structpeci__buf.md#aca55975957106666161da358b7f85db6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structpeci__buf.md#aca55975957106666161da358b7f85db6);

[ 223](structpeci__buf.md#a8e3fd0ef3f9141113214b89bb589a5e9) size\_t [len](structpeci__buf.md#a8e3fd0ef3f9141113214b89bb589a5e9);

224};

225

[ 229](structpeci__msg.md)struct [peci\_msg](structpeci__msg.md) {

[ 231](structpeci__msg.md#aa4d6785fc79059dc7e8574010bc29e4c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structpeci__msg.md#aa4d6785fc79059dc7e8574010bc29e4c);

[ 233](structpeci__msg.md#a10b270f4669c85a85c6e8f1bef7671e8) enum [peci\_command\_code](group__peci__interface.md#gacd243f64973f7bdcc8c999dc14ed2bd6) [cmd\_code](structpeci__msg.md#a10b270f4669c85a85c6e8f1bef7671e8);

[ 235](structpeci__msg.md#a22e435e110d261b8ecd5180d118ffd2d) struct [peci\_buf](structpeci__buf.md) [tx\_buffer](structpeci__msg.md#a22e435e110d261b8ecd5180d118ffd2d);

[ 237](structpeci__msg.md#abea62e39ca0ac59fca47c2f08a72f1e8) struct [peci\_buf](structpeci__buf.md) [rx\_buffer](structpeci__msg.md#abea62e39ca0ac59fca47c2f08a72f1e8);

[ 239](structpeci__msg.md#a0449f151c62e672553d7d60480e1b995) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structpeci__msg.md#a0449f151c62e672553d7d60480e1b995);

240};

241

249typedef int (\*peci\_config\_t)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate);

250typedef int (\*peci\_transfer\_t)(const struct [device](structdevice.md) \*dev, struct [peci\_msg](structpeci__msg.md) \*msg);

251typedef int (\*peci\_disable\_t)(const struct [device](structdevice.md) \*dev);

252typedef int (\*peci\_enable\_t)(const struct [device](structdevice.md) \*dev);

253

254\_\_subsystem struct peci\_driver\_api {

255 peci\_config\_t config;

256 peci\_disable\_t disable;

257 peci\_enable\_t enable;

258 peci\_transfer\_t transfer;

259};

260

264

[ 274](group__peci__interface.md#gaa1fee6839b68eed73f0a8d93b3a3ec82)\_\_syscall int [peci\_config](group__peci__interface.md#gaa1fee6839b68eed73f0a8d93b3a3ec82)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate);

275

276static inline int z\_impl\_peci\_config(const struct [device](structdevice.md) \*dev,

277 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate)

278{

279 struct peci\_driver\_api \*api;

280

281 api = (struct peci\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

282 return api->config(dev, bitrate);

283}

284

[ 293](group__peci__interface.md#gaa42e2e015a2c778a9eaf2dc1b697630f)\_\_syscall int [peci\_enable](group__peci__interface.md#gaa42e2e015a2c778a9eaf2dc1b697630f)(const struct [device](structdevice.md) \*dev);

294

295static inline int z\_impl\_peci\_enable(const struct [device](structdevice.md) \*dev)

296{

297 struct peci\_driver\_api \*api;

298

299 api = (struct peci\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

300 return api->enable(dev);

301}

302

[ 311](group__peci__interface.md#gaf197262cd58db5eb7691d1ce816057de)\_\_syscall int [peci\_disable](group__peci__interface.md#gaf197262cd58db5eb7691d1ce816057de)(const struct [device](structdevice.md) \*dev);

312

313static inline int z\_impl\_peci\_disable(const struct [device](structdevice.md) \*dev)

314{

315 struct peci\_driver\_api \*api;

316

317 api = (struct peci\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

318 return api->disable(dev);

319}

320

330

[ 331](group__peci__interface.md#gacf15bdae6483ad3e9498ed984a959687)\_\_syscall int [peci\_transfer](group__peci__interface.md#gacf15bdae6483ad3e9498ed984a959687)(const struct [device](structdevice.md) \*dev, struct [peci\_msg](structpeci__msg.md) \*msg);

332

333static inline int z\_impl\_peci\_transfer(const struct [device](structdevice.md) \*dev,

334 struct [peci\_msg](structpeci__msg.md) \*msg)

335{

336 struct peci\_driver\_api \*api;

337

338 api = (struct peci\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

339 return api->transfer(dev, msg);

340}

341

342

343#ifdef \_\_cplusplus

344}

345#endif

346

350

351#include <zephyr/syscalls/peci.h>

352

353#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PECI\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[peci\_error\_code](group__peci__interface.md#ga76ad37d4317b48311cf23cf516549544)

peci\_error\_code

PECI error codes.

**Definition** peci.h:36

[peci\_config](group__peci__interface.md#gaa1fee6839b68eed73f0a8d93b3a3ec82)

int peci\_config(const struct device \*dev, uint32\_t bitrate)

Configures the PECI interface.

[peci\_enable](group__peci__interface.md#gaa42e2e015a2c778a9eaf2dc1b697630f)

int peci\_enable(const struct device \*dev)

Enable PECI interface.

[peci\_command\_code](group__peci__interface.md#gacd243f64973f7bdcc8c999dc14ed2bd6)

peci\_command\_code

PECI commands.

**Definition** peci.h:45

[peci\_transfer](group__peci__interface.md#gacf15bdae6483ad3e9498ed984a959687)

int peci\_transfer(const struct device \*dev, struct peci\_msg \*msg)

Performs a PECI transaction.

[peci\_disable](group__peci__interface.md#gaf197262cd58db5eb7691d1ce816057de)

int peci\_disable(const struct device \*dev)

Disable PECI interface.

[PECI\_UNDERFLOW\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41)

@ PECI\_UNDERFLOW\_SENSOR\_ERROR

**Definition** peci.h:38

[PECI\_GENERAL\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f)

@ PECI\_GENERAL\_SENSOR\_ERROR

**Definition** peci.h:37

[PECI\_OVERFLOW\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2)

@ PECI\_OVERFLOW\_SENSOR\_ERROR

**Definition** peci.h:39

[PECI\_CMD\_GET\_DIB](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8)

@ PECI\_CMD\_GET\_DIB

**Definition** peci.h:65

[PECI\_CMD\_GET\_TEMP1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c)

@ PECI\_CMD\_GET\_TEMP1

**Definition** peci.h:48

[PECI\_CMD\_RD\_PCI\_CFG\_LOCAL0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5)

@ PECI\_CMD\_RD\_PCI\_CFG\_LOCAL0

**Definition** peci.h:61

[PECI\_CMD\_RD\_PKG\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed)

@ PECI\_CMD\_RD\_PKG\_CFG1

**Definition** peci.h:54

[PECI\_CMD\_WR\_IAMSR0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2)

@ PECI\_CMD\_WR\_IAMSR0

**Definition** peci.h:59

[PECI\_CMD\_WR\_PKG\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95)

@ PECI\_CMD\_WR\_PKG\_CFG1

**Definition** peci.h:56

[PECI\_CMD\_RD\_PKG\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523)

@ PECI\_CMD\_RD\_PKG\_CFG0

**Definition** peci.h:53

[PECI\_CMD\_WR\_PCI\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12)

@ PECI\_CMD\_WR\_PCI\_CFG1

**Definition** peci.h:52

[PECI\_CMD\_RD\_IAMSR1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53)

@ PECI\_CMD\_RD\_IAMSR1

**Definition** peci.h:58

[PECI\_CMD\_RD\_PCI\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa)

@ PECI\_CMD\_RD\_PCI\_CFG1

**Definition** peci.h:50

[PECI\_CMD\_WR\_PCI\_CFG\_LOCAL1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd)

@ PECI\_CMD\_WR\_PCI\_CFG\_LOCAL1

**Definition** peci.h:64

[PECI\_CMD\_RD\_PCI\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d)

@ PECI\_CMD\_RD\_PCI\_CFG0

**Definition** peci.h:49

[PECI\_CMD\_WR\_IAMSR1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3)

@ PECI\_CMD\_WR\_IAMSR1

**Definition** peci.h:60

[PECI\_CMD\_WR\_PKG\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55)

@ PECI\_CMD\_WR\_PKG\_CFG0

**Definition** peci.h:55

[PECI\_CMD\_WR\_PCI\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc)

@ PECI\_CMD\_WR\_PCI\_CFG0

**Definition** peci.h:51

[PECI\_CMD\_RD\_PCI\_CFG\_LOCAL1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c)

@ PECI\_CMD\_RD\_PCI\_CFG\_LOCAL1

**Definition** peci.h:62

[PECI\_CMD\_RD\_IAMSR0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10)

@ PECI\_CMD\_RD\_IAMSR0

**Definition** peci.h:57

[PECI\_CMD\_PING](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d)

@ PECI\_CMD\_PING

**Definition** peci.h:46

[PECI\_CMD\_WR\_PCI\_CFG\_LOCAL0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158)

@ PECI\_CMD\_WR\_PCI\_CFG\_LOCAL0

**Definition** peci.h:63

[PECI\_CMD\_GET\_TEMP0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf)

@ PECI\_CMD\_GET\_TEMP0

**Definition** peci.h:47

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[peci\_buf](structpeci__buf.md)

PECI buffer structure.

**Definition** peci.h:211

[peci\_buf::len](structpeci__buf.md#a8e3fd0ef3f9141113214b89bb589a5e9)

size\_t len

Length of the data buffer expected to be received without considering the frame check sequence byte.

**Definition** peci.h:223

[peci\_buf::buf](structpeci__buf.md#aca55975957106666161da358b7f85db6)

uint8\_t \* buf

Valid pointer on a data buffer, or NULL otherwise.

**Definition** peci.h:215

[peci\_msg](structpeci__msg.md)

PECI transaction packet format.

**Definition** peci.h:229

[peci\_msg::flags](structpeci__msg.md#a0449f151c62e672553d7d60480e1b995)

uint8\_t flags

PECI msg flags.

**Definition** peci.h:239

[peci\_msg::cmd\_code](structpeci__msg.md#a10b270f4669c85a85c6e8f1bef7671e8)

enum peci\_command\_code cmd\_code

Command code.

**Definition** peci.h:233

[peci\_msg::tx\_buffer](structpeci__msg.md#a22e435e110d261b8ecd5180d118ffd2d)

struct peci\_buf tx\_buffer

Pointer to buffer of write data.

**Definition** peci.h:235

[peci\_msg::addr](structpeci__msg.md#aa4d6785fc79059dc7e8574010bc29e4c)

uint8\_t addr

Client address.

**Definition** peci.h:231

[peci\_msg::rx\_buffer](structpeci__msg.md#abea62e39ca0ac59fca47c2f08a72f1e8)

struct peci\_buf rx\_buffer

Pointer to buffer of read data.

**Definition** peci.h:237

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [peci.h](peci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
