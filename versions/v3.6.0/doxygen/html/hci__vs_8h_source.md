---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hci__vs_8h_source.html
original_path: doxygen/html/hci__vs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_vs.h

[Go to the documentation of this file.](hci__vs_8h.md)

1/\* hci\_vs.h - Bluetooth Host Control Interface Vendor Specific definitions \*/

2

3/\*

4 \* Copyright (c) 2017-2018 Nordic Semiconductor ASA

5 \* Copyright (c) 2015-2016 Intel Corporation

6 \*

7 \* SPDX-License-Identifier: Apache-2.0

8 \*/

9#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_VS\_H\_

10#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_VS\_H\_

11

12#include <[stdint.h](stdint_8h.md)>

13

14#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 20](hci__vs_8h.md#a98cda5172947a82dfee334a5db41b0bb)#define BT\_VS\_CMD\_BIT\_VERSION 0

[ 21](hci__vs_8h.md#a2eec9eff49fc0d8f4e4f746dd7498478)#define BT\_VS\_CMD\_BIT\_SUP\_CMD 1

[ 22](hci__vs_8h.md#a418e0fd9c322671c1124835752b25678)#define BT\_VS\_CMD\_BIT\_SUP\_FEAT 2

[ 23](hci__vs_8h.md#ab1b627847e323e94949b53665e47f20f)#define BT\_VS\_CMD\_BIT\_SET\_EVT\_MASK 3

[ 24](hci__vs_8h.md#a020ca307df4c66bcd4c4f6da42d22e40)#define BT\_VS\_CMD\_BIT\_RESET 4

[ 25](hci__vs_8h.md#ac8fa0f7e3d5b802f1797c77d988bc172)#define BT\_VS\_CMD\_BIT\_WRITE\_BDADDR 5

[ 26](hci__vs_8h.md#ad57ee37a93208d3127e5ba36933b0d36)#define BT\_VS\_CMD\_BIT\_SET\_TRACE\_ENABLE 6

[ 27](hci__vs_8h.md#aaae2460cf69b0ad51aedf57c72d42103)#define BT\_VS\_CMD\_BIT\_READ\_BUILD\_INFO 7

[ 28](hci__vs_8h.md#a27e19ec90e057244db7f632887a46ec1)#define BT\_VS\_CMD\_BIT\_READ\_STATIC\_ADDRS 8

[ 29](hci__vs_8h.md#aa8b39f4ac968cf0cdb18073de1aa1ad5)#define BT\_VS\_CMD\_BIT\_READ\_KEY\_ROOTS 9

[ 30](hci__vs_8h.md#a96cee049fdf09d1e22aa2204a080c956)#define BT\_VS\_CMD\_BIT\_READ\_CHIP\_TEMP 10

[ 31](hci__vs_8h.md#a072226e7bfd637f71a03971e18d795e5)#define BT\_VS\_CMD\_BIT\_READ\_HOST\_STACK\_CMD 11

[ 32](hci__vs_8h.md#ac16322768bdd4688b2cefb4ea7b8c26f)#define BT\_VS\_CMD\_BIT\_SET\_SCAN\_REP\_ENABLE 12

[ 33](hci__vs_8h.md#a3f720e278e3aeefd11e9682d683e448b)#define BT\_VS\_CMD\_BIT\_WRITE\_TX\_POWER 13

[ 34](hci__vs_8h.md#a9af8f8bde7f33db3f32aa2aa5bda4012)#define BT\_VS\_CMD\_BIT\_READ\_TX\_POWER 14

35

[ 36](hci__vs_8h.md#a6f43e26c34622d9b9b2cf0a6ba53a393)#define BT\_VS\_CMD\_SUP\_FEAT(cmd) BT\_LE\_FEAT\_TEST(cmd, \

37 BT\_VS\_CMD\_BIT\_SUP\_FEAT)

[ 38](hci__vs_8h.md#af5ef90c96d5798cef8ad32f8d6094d53)#define BT\_VS\_CMD\_READ\_STATIC\_ADDRS(cmd) BT\_LE\_FEAT\_TEST(cmd, \

39 BT\_VS\_CMD\_BIT\_READ\_STATIC\_ADDRS)

[ 40](hci__vs_8h.md#aa81a670c17714854306b0044e9fb6392)#define BT\_VS\_CMD\_READ\_KEY\_ROOTS(cmd) BT\_LE\_FEAT\_TEST(cmd, \

41 BT\_VS\_CMD\_BIT\_READ\_KEY\_ROOTS)

42

[ 43](hci__vs_8h.md#a35bf58cbe551d8e3e56fa687828a5ee7)#define BT\_HCI\_VS\_HW\_PLAT\_INTEL 0x0001

[ 44](hci__vs_8h.md#a533362f9e60a77ce5c787d26241a2200)#define BT\_HCI\_VS\_HW\_PLAT\_NORDIC 0x0002

[ 45](hci__vs_8h.md#a0813745772dc53d5eb8d78ca016e0b3c)#define BT\_HCI\_VS\_HW\_PLAT\_NXP 0x0003

46

[ 47](hci__vs_8h.md#aef40f22484598bcd15885f1cf27a3a7e)#define BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF51X 0x0001

[ 48](hci__vs_8h.md#a990c9b5feb8fa1756d2270127a8909f9)#define BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF52X 0x0002

[ 49](hci__vs_8h.md#a040e6267e8b8cd77db9668f018d9cc83)#define BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF53X 0x0003

50

[ 51](hci__vs_8h.md#ac7e92cbb6a56d20b641be9304372a457)#define BT\_HCI\_VS\_FW\_VAR\_STANDARD\_CTLR 0x0001

[ 52](hci__vs_8h.md#aa41b3f0e21f47343262aca3648c1f02d)#define BT\_HCI\_VS\_FW\_VAR\_VS\_CTLR 0x0002

[ 53](hci__vs_8h.md#a6514cac9da9792697b18a2bf7906aaae)#define BT\_HCI\_VS\_FW\_VAR\_FW\_LOADER 0x0003

[ 54](hci__vs_8h.md#a551e878d9131dfc94f9a2ac304661e87)#define BT\_HCI\_VS\_FW\_VAR\_RESCUE\_IMG 0x0004

[ 55](hci__vs_8h.md#a7877a1d36a2370abd622eef05cf25795)#define BT\_HCI\_OP\_VS\_READ\_VERSION\_INFO BT\_OP(BT\_OGF\_VS, 0x0001)

[ 56](structbt__hci__rp__vs__read__version__info.md)struct [bt\_hci\_rp\_vs\_read\_version\_info](structbt__hci__rp__vs__read__version__info.md) {

[ 57](structbt__hci__rp__vs__read__version__info.md#a7cdff04c26d2f5864a07fc0a7c31a89a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__version__info.md#a7cdff04c26d2f5864a07fc0a7c31a89a);

[ 58](structbt__hci__rp__vs__read__version__info.md#a7e69f89d5562205f780dc05128b5d46a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [hw\_platform](structbt__hci__rp__vs__read__version__info.md#a7e69f89d5562205f780dc05128b5d46a);

[ 59](structbt__hci__rp__vs__read__version__info.md#abd4ea8df7b338e48490ceafae1b8e6be) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [hw\_variant](structbt__hci__rp__vs__read__version__info.md#abd4ea8df7b338e48490ceafae1b8e6be);

[ 60](structbt__hci__rp__vs__read__version__info.md#a24ad5440e85d2e91c0495a3b06ac7469) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fw\_variant](structbt__hci__rp__vs__read__version__info.md#a24ad5440e85d2e91c0495a3b06ac7469);

[ 61](structbt__hci__rp__vs__read__version__info.md#a147b0b73db111465549196ed67ca60d6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fw\_version](structbt__hci__rp__vs__read__version__info.md#a147b0b73db111465549196ed67ca60d6);

[ 62](structbt__hci__rp__vs__read__version__info.md#a47b4d799df9aeca67f6136264e13ef16) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fw\_revision](structbt__hci__rp__vs__read__version__info.md#a47b4d799df9aeca67f6136264e13ef16);

[ 63](structbt__hci__rp__vs__read__version__info.md#a43fc428c7ea444be2100e970b444f51a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fw\_build](structbt__hci__rp__vs__read__version__info.md#a43fc428c7ea444be2100e970b444f51a);

64} \_\_packed;

65

[ 66](hci__vs_8h.md#aeb5ac33d62cbd0c1db44a387fe99520c)#define BT\_HCI\_OP\_VS\_READ\_SUPPORTED\_COMMANDS BT\_OP(BT\_OGF\_VS, 0x0002)

[ 67](structbt__hci__rp__vs__read__supported__commands.md)struct [bt\_hci\_rp\_vs\_read\_supported\_commands](structbt__hci__rp__vs__read__supported__commands.md) {

[ 68](structbt__hci__rp__vs__read__supported__commands.md#afe9e5d1647b0cea192fa281367dc6c85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__supported__commands.md#afe9e5d1647b0cea192fa281367dc6c85);

[ 69](structbt__hci__rp__vs__read__supported__commands.md#a699129590cb1f5a3418d8e0eab3868e4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [commands](structbt__hci__rp__vs__read__supported__commands.md#a699129590cb1f5a3418d8e0eab3868e4)[64];

70} \_\_packed;

71

[ 72](hci__vs_8h.md#a77537f2ac77e6f4b25b840726899bb8d)#define BT\_HCI\_OP\_VS\_READ\_SUPPORTED\_FEATURES BT\_OP(BT\_OGF\_VS, 0x0003)

[ 73](structbt__hci__rp__vs__read__supported__features.md)struct [bt\_hci\_rp\_vs\_read\_supported\_features](structbt__hci__rp__vs__read__supported__features.md) {

[ 74](structbt__hci__rp__vs__read__supported__features.md#a40468d71ba659d8ef593d82aca0bc583) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__supported__features.md#a40468d71ba659d8ef593d82aca0bc583);

[ 75](structbt__hci__rp__vs__read__supported__features.md#a0459b49e864d3069d4ba818ef2ed59ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__hci__rp__vs__read__supported__features.md#a0459b49e864d3069d4ba818ef2ed59ca)[8];

76} \_\_packed;

77

[ 78](hci__vs_8h.md#a3d99ba16d2510f12c9b8a7fd7cd6e5e9)#define BT\_HCI\_OP\_VS\_SET\_EVENT\_MASK BT\_OP(BT\_OGF\_VS, 0x0004)

[ 79](structbt__hci__cp__vs__set__event__mask.md)struct [bt\_hci\_cp\_vs\_set\_event\_mask](structbt__hci__cp__vs__set__event__mask.md) {

[ 80](structbt__hci__cp__vs__set__event__mask.md#ad5883adb065f04e923ff64093c78949a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [event\_mask](structbt__hci__cp__vs__set__event__mask.md#ad5883adb065f04e923ff64093c78949a)[8];

81} \_\_packed;

82

[ 83](hci__vs_8h.md#a2c47a3d7d4b69e33b5caf5e69ae80abf)#define BT\_HCI\_VS\_RESET\_SOFT 0x00

[ 84](hci__vs_8h.md#a50933b6556620154780af3c54ee987a5)#define BT\_HCI\_VS\_RESET\_HARD 0x01

[ 85](hci__vs_8h.md#ad3e609f9713edcc0fd5a23fa6042df6d)#define BT\_HCI\_OP\_VS\_RESET BT\_OP(BT\_OGF\_VS, 0x0005)

[ 86](structbt__hci__cp__vs__reset.md)struct [bt\_hci\_cp\_vs\_reset](structbt__hci__cp__vs__reset.md) {

[ 87](structbt__hci__cp__vs__reset.md#aa3a47f4d2a593a9c756893ec28e49a00) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__cp__vs__reset.md#aa3a47f4d2a593a9c756893ec28e49a00);

88} \_\_packed;

89

[ 90](hci__vs_8h.md#a81e2e5d7a5c4def4b86ab7074551c5bf)#define BT\_HCI\_OP\_VS\_WRITE\_BD\_ADDR BT\_OP(BT\_OGF\_VS, 0x0006)

[ 91](structbt__hci__cp__vs__write__bd__addr.md)struct [bt\_hci\_cp\_vs\_write\_bd\_addr](structbt__hci__cp__vs__write__bd__addr.md) {

[ 92](structbt__hci__cp__vs__write__bd__addr.md#af54e126fff610467dd730902893b6cd2) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__cp__vs__write__bd__addr.md#af54e126fff610467dd730902893b6cd2);

93} \_\_packed;

94

[ 95](hci__vs_8h.md#afd977fec9cc90cc3e3f304dbb181fac4)#define BT\_HCI\_VS\_TRACE\_DISABLED 0x00

[ 96](hci__vs_8h.md#a22c18b5e3fc458394ef9d20595ff5019)#define BT\_HCI\_VS\_TRACE\_ENABLED 0x01

97

[ 98](hci__vs_8h.md#a3851c5deb79a1530e448a8cfa0eed2ed)#define BT\_HCI\_VS\_TRACE\_HCI\_EVTS 0x00

[ 99](hci__vs_8h.md#a72f7e148fe28d21381870f57b30b87e1)#define BT\_HCI\_VS\_TRACE\_VDC 0x01

[ 100](hci__vs_8h.md#a285f127f83f4c241372aa7258b4cad70)#define BT\_HCI\_OP\_VS\_SET\_TRACE\_ENABLE BT\_OP(BT\_OGF\_VS, 0x0007)

[ 101](structbt__hci__cp__vs__set__trace__enable.md)struct [bt\_hci\_cp\_vs\_set\_trace\_enable](structbt__hci__cp__vs__set__trace__enable.md) {

[ 102](structbt__hci__cp__vs__set__trace__enable.md#a5676627500b6c5aff5986c53a0ba13a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__vs__set__trace__enable.md#a5676627500b6c5aff5986c53a0ba13a7);

[ 103](structbt__hci__cp__vs__set__trace__enable.md#a18c3c81f13599a12903b12e350703dc5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__cp__vs__set__trace__enable.md#a18c3c81f13599a12903b12e350703dc5);

104} \_\_packed;

105

[ 106](hci__vs_8h.md#a6a4f182f0aeeb80e59474f785adda864)#define BT\_HCI\_OP\_VS\_READ\_BUILD\_INFO BT\_OP(BT\_OGF\_VS, 0x0008)

[ 107](structbt__hci__rp__vs__read__build__info.md)struct [bt\_hci\_rp\_vs\_read\_build\_info](structbt__hci__rp__vs__read__build__info.md) {

[ 108](structbt__hci__rp__vs__read__build__info.md#acdebc0d6f8d713075c6e5e69cf136ea3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__build__info.md#acdebc0d6f8d713075c6e5e69cf136ea3);

[ 109](structbt__hci__rp__vs__read__build__info.md#aba2aaa3916221768412eed39cc85ab5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [info](structbt__hci__rp__vs__read__build__info.md#aba2aaa3916221768412eed39cc85ab5f)[0];

110} \_\_packed;

111

[ 112](structbt__hci__vs__static__addr.md)struct [bt\_hci\_vs\_static\_addr](structbt__hci__vs__static__addr.md) {

[ 113](structbt__hci__vs__static__addr.md#aa9b61e3f589465c68a4b6356c9de8b66) [bt\_addr\_t](structbt__addr__t.md) [bdaddr](structbt__hci__vs__static__addr.md#aa9b61e3f589465c68a4b6356c9de8b66);

[ 114](structbt__hci__vs__static__addr.md#afef2fbf31b7d5101ee48e51476c81698) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ir](structbt__hci__vs__static__addr.md#afef2fbf31b7d5101ee48e51476c81698)[16];

115} \_\_packed;

116

[ 117](hci__vs_8h.md#a0306297daa39e9b73c0953b56ac0fb16)#define BT\_HCI\_OP\_VS\_READ\_STATIC\_ADDRS BT\_OP(BT\_OGF\_VS, 0x0009)

[ 118](structbt__hci__rp__vs__read__static__addrs.md)struct [bt\_hci\_rp\_vs\_read\_static\_addrs](structbt__hci__rp__vs__read__static__addrs.md) {

[ 119](structbt__hci__rp__vs__read__static__addrs.md#af3ddb349e82e7a5edcb86300c8d8a548) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__static__addrs.md#af3ddb349e82e7a5edcb86300c8d8a548);

[ 120](structbt__hci__rp__vs__read__static__addrs.md#a482a0984602d4d59ef9572d4e1053a99) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_addrs](structbt__hci__rp__vs__read__static__addrs.md#a482a0984602d4d59ef9572d4e1053a99);

[ 121](structbt__hci__rp__vs__read__static__addrs.md#af8175d96852a67ebcfa4da5019e618e9) struct [bt\_hci\_vs\_static\_addr](structbt__hci__vs__static__addr.md) [a](structbt__hci__rp__vs__read__static__addrs.md#af8175d96852a67ebcfa4da5019e618e9)[0];

122} \_\_packed;

123

[ 124](hci__vs_8h.md#a11cb133e491f6ed0e796f2cb6cd07731)#define BT\_HCI\_OP\_VS\_READ\_KEY\_HIERARCHY\_ROOTS BT\_OP(BT\_OGF\_VS, 0x000a)

[ 125](structbt__hci__rp__vs__read__key__hierarchy__roots.md)struct [bt\_hci\_rp\_vs\_read\_key\_hierarchy\_roots](structbt__hci__rp__vs__read__key__hierarchy__roots.md) {

[ 126](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a3ab9afeea4cc59853ef5a2f04ee39405) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a3ab9afeea4cc59853ef5a2f04ee39405);

[ 127](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a5ce7b3ba72b129191d8a7d73f9978682) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ir](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a5ce7b3ba72b129191d8a7d73f9978682)[16];

[ 128](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a62c6df2ac691c06f481189fb61b0f99c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [er](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a62c6df2ac691c06f481189fb61b0f99c)[16];

129} \_\_packed;

130

[ 131](hci__vs_8h.md#aabf7e4c3ac3b35f22787ad9a448b8220)#define BT\_HCI\_OP\_VS\_READ\_CHIP\_TEMP BT\_OP(BT\_OGF\_VS, 0x000b)

[ 132](structbt__hci__rp__vs__read__chip__temp.md)struct [bt\_hci\_rp\_vs\_read\_chip\_temp](structbt__hci__rp__vs__read__chip__temp.md) {

[ 133](structbt__hci__rp__vs__read__chip__temp.md#a324034b28a6526e195de576432f8ed32) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__chip__temp.md#a324034b28a6526e195de576432f8ed32);

[ 134](structbt__hci__rp__vs__read__chip__temp.md#a2487c86e1975f69f307e70624abf9519) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [temps](structbt__hci__rp__vs__read__chip__temp.md#a2487c86e1975f69f307e70624abf9519);

135} \_\_packed;

136

[ 137](structbt__hci__vs__cmd.md)struct [bt\_hci\_vs\_cmd](structbt__hci__vs__cmd.md) {

[ 138](structbt__hci__vs__cmd.md#a640c7523215b676dd8922d95c136cc4b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vendor\_id](structbt__hci__vs__cmd.md#a640c7523215b676dd8922d95c136cc4b);

[ 139](structbt__hci__vs__cmd.md#a1ca54af74a178506b954fe8e43a04895) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [opcode\_base](structbt__hci__vs__cmd.md#a1ca54af74a178506b954fe8e43a04895);

140} \_\_packed;

141

[ 142](hci__vs_8h.md#a8f9f21d0b193bfdd1e4d1a98b4a96f04)#define BT\_HCI\_VS\_VID\_ANDROID 0x0001

[ 143](hci__vs_8h.md#ab028da372f594f1e698335c3f083bd7f)#define BT\_HCI\_VS\_VID\_MICROSOFT 0x0002

[ 144](hci__vs_8h.md#a33eb32eabc404d0a73a0b75523210778)#define BT\_HCI\_OP\_VS\_READ\_HOST\_STACK\_CMDS BT\_OP(BT\_OGF\_VS, 0x000c)

[ 145](structbt__hci__rp__vs__read__host__stack__cmds.md)struct [bt\_hci\_rp\_vs\_read\_host\_stack\_cmds](structbt__hci__rp__vs__read__host__stack__cmds.md) {

[ 146](structbt__hci__rp__vs__read__host__stack__cmds.md#a374e54391bcb72b5cde885cb04269e9a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__host__stack__cmds.md#a374e54391bcb72b5cde885cb04269e9a);

[ 147](structbt__hci__rp__vs__read__host__stack__cmds.md#ac11d1ed48e49f9ce1d31709be76aed95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_cmds](structbt__hci__rp__vs__read__host__stack__cmds.md#ac11d1ed48e49f9ce1d31709be76aed95);

[ 148](structbt__hci__rp__vs__read__host__stack__cmds.md#a27b591f7784aaec063afc37105c00880) struct [bt\_hci\_vs\_cmd](structbt__hci__vs__cmd.md) [c](structbt__hci__rp__vs__read__host__stack__cmds.md#a27b591f7784aaec063afc37105c00880)[0];

149} \_\_packed;

150

[ 151](hci__vs_8h.md#a4025336d067b79bead25b45de0ed33cf)#define BT\_HCI\_VS\_SCAN\_REQ\_REPORTS\_DISABLED 0x00

[ 152](hci__vs_8h.md#a7be2294229731b3a004788a739d6f616)#define BT\_HCI\_VS\_SCAN\_REQ\_REPORTS\_ENABLED 0x01

[ 153](hci__vs_8h.md#ac1e36447ba26e70b4a95073e200cc549)#define BT\_HCI\_OP\_VS\_SET\_SCAN\_REQ\_REPORTS BT\_OP(BT\_OGF\_VS, 0x000d)

[ 154](structbt__hci__cp__vs__set__scan__req__reports.md)struct [bt\_hci\_cp\_vs\_set\_scan\_req\_reports](structbt__hci__cp__vs__set__scan__req__reports.md) {

[ 155](structbt__hci__cp__vs__set__scan__req__reports.md#ac99b6b1fee39a2330c6d0c214c737fd3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__vs__set__scan__req__reports.md#ac99b6b1fee39a2330c6d0c214c737fd3);

156} \_\_packed;

157

[ 158](hci__vs_8h.md#a1f0308641bb308088c49ca241d1293a8)#define BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_ADV 0x00

[ 159](hci__vs_8h.md#a36e1663258f24c7f5ea8235efcb8b1f6)#define BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_SCAN 0x01

[ 160](hci__vs_8h.md#a9ae772dcf1042953552a44c41d41f3e9)#define BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_CONN 0x02

[ 161](hci__vs_8h.md#a17d4ed99163918297a67a4c00de38728)#define BT\_HCI\_VS\_LL\_TX\_POWER\_LEVEL\_NO\_PREF 0x7F

[ 162](hci__vs_8h.md#a29b5fda3541bfd8d69db72e46688d180)#define BT\_HCI\_OP\_VS\_WRITE\_TX\_POWER\_LEVEL BT\_OP(BT\_OGF\_VS, 0x000e)

[ 163](structbt__hci__cp__vs__write__tx__power__level.md)struct [bt\_hci\_cp\_vs\_write\_tx\_power\_level](structbt__hci__cp__vs__write__tx__power__level.md) {

[ 164](structbt__hci__cp__vs__write__tx__power__level.md#a27e1b402a9a1a8850f551a18651e914e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle\_type](structbt__hci__cp__vs__write__tx__power__level.md#a27e1b402a9a1a8850f551a18651e914e);

[ 165](structbt__hci__cp__vs__write__tx__power__level.md#adff511831f183e031d9c61781d337b9d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__vs__write__tx__power__level.md#adff511831f183e031d9c61781d337b9d);

[ 166](structbt__hci__cp__vs__write__tx__power__level.md#abd7f6c92c1463ec35cfd552ffce50b53) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__hci__cp__vs__write__tx__power__level.md#abd7f6c92c1463ec35cfd552ffce50b53);

167} \_\_packed;

168

[ 169](structbt__hci__rp__vs__write__tx__power__level.md)struct [bt\_hci\_rp\_vs\_write\_tx\_power\_level](structbt__hci__rp__vs__write__tx__power__level.md) {

[ 170](structbt__hci__rp__vs__write__tx__power__level.md#a2d462d79165a3fbc98a3a24c6d6ad8fa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__write__tx__power__level.md#a2d462d79165a3fbc98a3a24c6d6ad8fa);

[ 171](structbt__hci__rp__vs__write__tx__power__level.md#a0ba154d288f23fb5d859d620a9205a68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle\_type](structbt__hci__rp__vs__write__tx__power__level.md#a0ba154d288f23fb5d859d620a9205a68);

[ 172](structbt__hci__rp__vs__write__tx__power__level.md#ac7c2eb75ec96f79d67c0a7b3ce851e14) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__vs__write__tx__power__level.md#ac7c2eb75ec96f79d67c0a7b3ce851e14);

[ 173](structbt__hci__rp__vs__write__tx__power__level.md#a6a8c6103c609f2c05cfb46476e23d58e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [selected\_tx\_power](structbt__hci__rp__vs__write__tx__power__level.md#a6a8c6103c609f2c05cfb46476e23d58e);

174} \_\_packed;

175

[ 176](hci__vs_8h.md#ad18fb75b6b25758cec63ea30ada16394)#define BT\_HCI\_OP\_VS\_READ\_TX\_POWER\_LEVEL BT\_OP(BT\_OGF\_VS, 0x000f)

[ 177](structbt__hci__cp__vs__read__tx__power__level.md)struct [bt\_hci\_cp\_vs\_read\_tx\_power\_level](structbt__hci__cp__vs__read__tx__power__level.md) {

[ 178](structbt__hci__cp__vs__read__tx__power__level.md#a776450ea2132fab77b9350ae46d3a1b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle\_type](structbt__hci__cp__vs__read__tx__power__level.md#a776450ea2132fab77b9350ae46d3a1b5);

[ 179](structbt__hci__cp__vs__read__tx__power__level.md#a2bb528f003b22b88eec0d7389c84034f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__vs__read__tx__power__level.md#a2bb528f003b22b88eec0d7389c84034f);

180} \_\_packed;

181

[ 182](structbt__hci__rp__vs__read__tx__power__level.md)struct [bt\_hci\_rp\_vs\_read\_tx\_power\_level](structbt__hci__rp__vs__read__tx__power__level.md) {

[ 183](structbt__hci__rp__vs__read__tx__power__level.md#ae5011313891d5ac4eaf0383e125bf786) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__tx__power__level.md#ae5011313891d5ac4eaf0383e125bf786);

[ 184](structbt__hci__rp__vs__read__tx__power__level.md#a86f8e314571df0dfbc0995fb14108650) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [handle\_type](structbt__hci__rp__vs__read__tx__power__level.md#a86f8e314571df0dfbc0995fb14108650);

[ 185](structbt__hci__rp__vs__read__tx__power__level.md#ae2755a4ba68c73c5bb97f58400d8b16d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__rp__vs__read__tx__power__level.md#ae2755a4ba68c73c5bb97f58400d8b16d);

[ 186](structbt__hci__rp__vs__read__tx__power__level.md#ae1e1ee5319283a725c1eb1ab3ad13481) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power\_level](structbt__hci__rp__vs__read__tx__power__level.md#ae1e1ee5319283a725c1eb1ab3ad13481);

187} \_\_packed;

188

[ 189](hci__vs_8h.md#ae51d60b72e66a4eae8e5d608e0ab339b)#define BT\_HCI\_OP\_VS\_READ\_USB\_TRANSPORT\_MODE BT\_OP(BT\_OGF\_VS, 0x0010)

190

[ 191](structbt__hci__rp__vs__read__usb__transport__mode.md)struct [bt\_hci\_rp\_vs\_read\_usb\_transport\_mode](structbt__hci__rp__vs__read__usb__transport__mode.md) {

[ 192](structbt__hci__rp__vs__read__usb__transport__mode.md#a7fdfe43b633c153fd9e7cf1f470b435f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__vs__read__usb__transport__mode.md#a7fdfe43b633c153fd9e7cf1f470b435f);

[ 193](structbt__hci__rp__vs__read__usb__transport__mode.md#a25070132401d9b3d3dcd3f325f66da64) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_supported\_modes](structbt__hci__rp__vs__read__usb__transport__mode.md#a25070132401d9b3d3dcd3f325f66da64);

[ 194](structbt__hci__rp__vs__read__usb__transport__mode.md#aec8f1c7acd972d00b8f1070ed444b155) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [supported\_mode](structbt__hci__rp__vs__read__usb__transport__mode.md#aec8f1c7acd972d00b8f1070ed444b155)[0];

195} \_\_packed;

196

[ 197](hci__vs_8h.md#a86badb7e68535ef6d741e03c63811578)#define BT\_HCI\_VS\_USB\_H2\_MODE 0x00

[ 198](hci__vs_8h.md#a758ccb4c0f666df106f550af15025e02)#define BT\_HCI\_VS\_USB\_H4\_MODE 0x01

199

[ 200](hci__vs_8h.md#adcf0e45c997c88301a5f4ba9240eb071)#define BT\_HCI\_OP\_VS\_SET\_USB\_TRANSPORT\_MODE BT\_OP(BT\_OGF\_VS, 0x0011)

201

[ 202](structbt__hci__cp__vs__set__usb__transport__mode.md)struct [bt\_hci\_cp\_vs\_set\_usb\_transport\_mode](structbt__hci__cp__vs__set__usb__transport__mode.md) {

[ 203](structbt__hci__cp__vs__set__usb__transport__mode.md#a651867bbfbc6ff642fbc294488259b4e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__hci__cp__vs__set__usb__transport__mode.md#a651867bbfbc6ff642fbc294488259b4e);

204} \_\_packed;

205

[ 206](hci__vs_8h.md#a6c499204a11f76fe28cc88df665f4af0)#define BT\_HCI\_OP\_VS\_SET\_MIN\_NUM\_USED\_CHANS BT\_OP(BT\_OGF\_VS, 0x0012)

207

[ 208](structbt__hci__cp__vs__set__min__num__used__chans.md)struct [bt\_hci\_cp\_vs\_set\_min\_num\_used\_chans](structbt__hci__cp__vs__set__min__num__used__chans.md) {

[ 209](structbt__hci__cp__vs__set__min__num__used__chans.md#aae4d29392f389a20f9be86870defc954) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [handle](structbt__hci__cp__vs__set__min__num__used__chans.md#aae4d29392f389a20f9be86870defc954);

[ 210](structbt__hci__cp__vs__set__min__num__used__chans.md#a8cfa13723348bb43c19ceaa56fad2b1c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phys](structbt__hci__cp__vs__set__min__num__used__chans.md#a8cfa13723348bb43c19ceaa56fad2b1c);

[ 211](structbt__hci__cp__vs__set__min__num__used__chans.md#a68262baddf6b7d2d42d61ad4c2690567) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_used\_chans](structbt__hci__cp__vs__set__min__num__used__chans.md#a68262baddf6b7d2d42d61ad4c2690567);

212} \_\_packed;

213

214/\* Events \*/

215

[ 216](structbt__hci__evt__vs.md)struct [bt\_hci\_evt\_vs](structbt__hci__evt__vs.md) {

[ 217](structbt__hci__evt__vs.md#aadf6dd6172922d32a4a40be003f09876) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__evt__vs.md#aadf6dd6172922d32a4a40be003f09876);

218} \_\_packed;

219

[ 220](hci__vs_8h.md#a32cd953a56ecfc3eb62b71a8d626c93d)#define BT\_HCI\_EVT\_VS\_FATAL\_ERROR 0x02

221

[ 222](hci__vs_8h.md#a20356ed318eead6aab20ef19b6d7c0df)#define BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_STACK\_FRAME 0x01

[ 223](hci__vs_8h.md#ae9900729ac120c6fb68314b1e0984516)#define BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_CTRL\_ASSERT 0x02

[ 224](hci__vs_8h.md#a7ed9dbedd215a7ed4b040b6486d49b98)#define BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_TRACE 0x03

[ 225](structbt__hci__vs__fata__error__cpu__data__cortex__m.md)struct [bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m](structbt__hci__vs__fata__error__cpu__data__cortex__m.md) {

[ 226](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#add43bedce9999e88f10cb98f3bbb69ab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [a1](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#add43bedce9999e88f10cb98f3bbb69ab);

[ 227](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a7c177a75e51c86faf289d37bff84683c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [a2](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a7c177a75e51c86faf289d37bff84683c);

[ 228](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a3d5e6e7be359a3964ed49051253c428f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [a3](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a3d5e6e7be359a3964ed49051253c428f);

[ 229](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a2cbd9ac477601f457ea7a1d757aeaf30) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [a4](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a2cbd9ac477601f457ea7a1d757aeaf30);

[ 230](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a02a8928cf7754bef640e74d41d72f345) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ip](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a02a8928cf7754bef640e74d41d72f345);

[ 231](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#aa146cf7122eaf4b1d0de328dc05081de) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lr](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#aa146cf7122eaf4b1d0de328dc05081de);

[ 232](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a472c058324fa9349a23586c99d786d32) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [xpsr](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a472c058324fa9349a23586c99d786d32);

233} \_\_packed;

[ 234](hci__vs_8h.md#a36a880f6a4f53465f38f70387b52b006)#define BT\_HCI\_EVT\_VS\_ERROR\_CPU\_TYPE\_CORTEX\_M 0x01

[ 235](structbt__hci__vs__fatal__error__stack__frame.md)struct [bt\_hci\_vs\_fatal\_error\_stack\_frame](structbt__hci__vs__fatal__error__stack__frame.md) {

[ 236](structbt__hci__vs__fatal__error__stack__frame.md#ac2f93a05158d4c170848ee4afdfe1bd1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reason](structbt__hci__vs__fatal__error__stack__frame.md#ac2f93a05158d4c170848ee4afdfe1bd1);

[ 237](structbt__hci__vs__fatal__error__stack__frame.md#a1530d501d5fd5dade63219e16ddd5d85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cpu\_type](structbt__hci__vs__fatal__error__stack__frame.md#a1530d501d5fd5dade63219e16ddd5d85);

[ 238](structbt__hci__vs__fatal__error__stack__frame.md#a89e4ede59af9b37fcaeee00ea028f930) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cpu\_data](structbt__hci__vs__fatal__error__stack__frame.md#a89e4ede59af9b37fcaeee00ea028f930)[0];

239} \_\_packed;

240

[ 241](structbt__hci__evt__vs__fatal__error__trace__data.md)struct [bt\_hci\_evt\_vs\_fatal\_error\_trace\_data](structbt__hci__evt__vs__fatal__error__trace__data.md) {

[ 242](structbt__hci__evt__vs__fatal__error__trace__data.md#a467d2de2a3b26ddef8c412957abfd820) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pc](structbt__hci__evt__vs__fatal__error__trace__data.md#a467d2de2a3b26ddef8c412957abfd820);

[ 243](structbt__hci__evt__vs__fatal__error__trace__data.md#ae1efc729b0c079fa922dcfffab6cdfa6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [err\_info](structbt__hci__evt__vs__fatal__error__trace__data.md#ae1efc729b0c079fa922dcfffab6cdfa6)[0];

244} \_\_packed;

245

[ 246](structbt__hci__evt__vs__fatal__error.md)struct [bt\_hci\_evt\_vs\_fatal\_error](structbt__hci__evt__vs__fatal__error.md) {

[ 247](structbt__hci__evt__vs__fatal__error.md#a15e84185f74e84e1f9ccd83dc4fa2798) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__evt__vs__fatal__error.md#a15e84185f74e84e1f9ccd83dc4fa2798);

[ 248](structbt__hci__evt__vs__fatal__error.md#aefd553e85eedb6e205da39916c5553aa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__vs__fatal__error.md#aefd553e85eedb6e205da39916c5553aa)[0];

249} \_\_packed;

250

[ 251](hci__vs_8h.md#aa56a360e3cdf72fc87216685179edd41)#define BT\_HCI\_VS\_TRACE\_LMP\_TX 0x01

[ 252](hci__vs_8h.md#aa27a4038be1c6e9cfb756e78d9b07df9)#define BT\_HCI\_VS\_TRACE\_LMP\_RX 0x02

[ 253](hci__vs_8h.md#a4a212cd52bdd9343bdab8d27ae5d650e)#define BT\_HCI\_VS\_TRACE\_LLCP\_TX 0x03

[ 254](hci__vs_8h.md#a2c69ab6f964ed5cd95419a9771363b64)#define BT\_HCI\_VS\_TRACE\_LLCP\_RX 0x04

[ 255](hci__vs_8h.md#affed427819b721735e31fbcc52f40b5f)#define BT\_HCI\_VS\_TRACE\_LE\_CONN\_IND 0x05

[ 256](hci__vs_8h.md#a43dd9ebf0a175aa0bc244f99df278344)#define BT\_HCI\_EVT\_VS\_TRACE\_INFO 0x03

[ 257](structbt__hci__evt__vs__trace__info.md)struct [bt\_hci\_evt\_vs\_trace\_info](structbt__hci__evt__vs__trace__info.md) {

[ 258](structbt__hci__evt__vs__trace__info.md#af563e07c5364df229eb767e545c8aaa2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hci__evt__vs__trace__info.md#af563e07c5364df229eb767e545c8aaa2);

[ 259](structbt__hci__evt__vs__trace__info.md#ae524df8cc722cda0fa86127a6b8e56da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__vs__trace__info.md#ae524df8cc722cda0fa86127a6b8e56da)[0];

260} \_\_packed;

261

[ 262](hci__vs_8h.md#ac4fae4567bb2ba2866ed24ccfc328f63)#define BT\_HCI\_EVT\_VS\_SCAN\_REQ\_RX 0x04

[ 263](structbt__hci__evt__vs__scan__req__rx.md)struct [bt\_hci\_evt\_vs\_scan\_req\_rx](structbt__hci__evt__vs__scan__req__rx.md) {

[ 264](structbt__hci__evt__vs__scan__req__rx.md#a56613220a50bc50a771f432b7e617d5b) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__vs__scan__req__rx.md#a56613220a50bc50a771f432b7e617d5b);

[ 265](structbt__hci__evt__vs__scan__req__rx.md#acbfa7ec0a3ab1f94f53598a9d8242aba) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__vs__scan__req__rx.md#acbfa7ec0a3ab1f94f53598a9d8242aba);

266} \_\_packed;

267

[ 268](structbt__hci__le__iq__sample16.md)struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) {

[ 269](structbt__hci__le__iq__sample16.md#ace47fd665d57f7ad7eb0a04ec8e54a47) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [i](structbt__hci__le__iq__sample16.md#ace47fd665d57f7ad7eb0a04ec8e54a47);

[ 270](structbt__hci__le__iq__sample16.md#aa317d2a9f451eeecb35ff05044ea6dc3) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [q](structbt__hci__le__iq__sample16.md#aa317d2a9f451eeecb35ff05044ea6dc3);

271} \_\_packed;

272

[ 273](hci__vs_8h.md#a8b0ced9392cbf33794100794f964d53f)#define BT\_HCI\_EVT\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT 0x5

[ 274](hci__vs_8h.md#a71d87ba67638aca600ebbe615a0d4122)#define BT\_HCI\_VS\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE 0x8000

[ 275](structbt__hci__evt__vs__le__connectionless__iq__report.md)struct [bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report](structbt__hci__evt__vs__le__connectionless__iq__report.md) {

[ 276](structbt__hci__evt__vs__le__connectionless__iq__report.md#a9c199121ac475d635fc51289e8eba979) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_handle](structbt__hci__evt__vs__le__connectionless__iq__report.md#a9c199121ac475d635fc51289e8eba979);

[ 277](structbt__hci__evt__vs__le__connectionless__iq__report.md#ad15beccc7c2207565678ebef72346158) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chan\_idx](structbt__hci__evt__vs__le__connectionless__iq__report.md#ad15beccc7c2207565678ebef72346158);

[ 278](structbt__hci__evt__vs__le__connectionless__iq__report.md#a9b7eb8a5cf363c3aec96b49853056dc7) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rssi](structbt__hci__evt__vs__le__connectionless__iq__report.md#a9b7eb8a5cf363c3aec96b49853056dc7);

[ 279](structbt__hci__evt__vs__le__connectionless__iq__report.md#a5fcd776dce904763c5cc6fab9a1373f4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rssi\_ant\_id](structbt__hci__evt__vs__le__connectionless__iq__report.md#a5fcd776dce904763c5cc6fab9a1373f4);

[ 280](structbt__hci__evt__vs__le__connectionless__iq__report.md#a808a2a134104c69073af253a3c4dd1bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__vs__le__connectionless__iq__report.md#a808a2a134104c69073af253a3c4dd1bd);

[ 281](structbt__hci__evt__vs__le__connectionless__iq__report.md#ac0b077d7b5e2b7c5ce61b3060913cad5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__evt__vs__le__connectionless__iq__report.md#ac0b077d7b5e2b7c5ce61b3060913cad5);

[ 282](structbt__hci__evt__vs__le__connectionless__iq__report.md#af5b27c1504ce4ff8afe23c28a9ac423f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_status](structbt__hci__evt__vs__le__connectionless__iq__report.md#af5b27c1504ce4ff8afe23c28a9ac423f);

[ 283](structbt__hci__evt__vs__le__connectionless__iq__report.md#ab6911af90d85c565615c437715d9c7eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [per\_evt\_counter](structbt__hci__evt__vs__le__connectionless__iq__report.md#ab6911af90d85c565615c437715d9c7eb);

[ 284](structbt__hci__evt__vs__le__connectionless__iq__report.md#a2698510deb6bd8943bf57104f96673db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sample\_count](structbt__hci__evt__vs__le__connectionless__iq__report.md#a2698510deb6bd8943bf57104f96673db);

[ 285](structbt__hci__evt__vs__le__connectionless__iq__report.md#a17c9d19883c9d8e34f300fbff614b475) struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) [sample](structbt__hci__evt__vs__le__connectionless__iq__report.md#a17c9d19883c9d8e34f300fbff614b475)[0];

286} \_\_packed;

287

[ 288](hci__vs_8h.md#a6066be0390be7f611e0e3f4bfab030df)#define BT\_HCI\_EVT\_VS\_LE\_CONNECTION\_IQ\_REPORT 0x6

[ 289](structbt__hci__evt__vs__le__connection__iq__report.md)struct [bt\_hci\_evt\_vs\_le\_connection\_iq\_report](structbt__hci__evt__vs__le__connection__iq__report.md) {

[ 290](structbt__hci__evt__vs__le__connection__iq__report.md#a941d0e025334a0c041cc7a59b69f0af3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_handle](structbt__hci__evt__vs__le__connection__iq__report.md#a941d0e025334a0c041cc7a59b69f0af3);

[ 291](structbt__hci__evt__vs__le__connection__iq__report.md#a959c7e2b910aec90f8b186550cb7f4d8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_phy](structbt__hci__evt__vs__le__connection__iq__report.md#a959c7e2b910aec90f8b186550cb7f4d8);

[ 292](structbt__hci__evt__vs__le__connection__iq__report.md#af634fa464d4ca435ea935ae58db86cfa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_chan\_idx](structbt__hci__evt__vs__le__connection__iq__report.md#af634fa464d4ca435ea935ae58db86cfa);

[ 293](structbt__hci__evt__vs__le__connection__iq__report.md#a87d4a6ebd1cc172816f3fe786c22f058) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [rssi](structbt__hci__evt__vs__le__connection__iq__report.md#a87d4a6ebd1cc172816f3fe786c22f058);

[ 294](structbt__hci__evt__vs__le__connection__iq__report.md#a55a290121f661f155684d37fa0df77d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rssi\_ant\_id](structbt__hci__evt__vs__le__connection__iq__report.md#a55a290121f661f155684d37fa0df77d2);

[ 295](structbt__hci__evt__vs__le__connection__iq__report.md#ad714bb1f2292764eba9c506bcc72bccd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__hci__evt__vs__le__connection__iq__report.md#ad714bb1f2292764eba9c506bcc72bccd);

[ 296](structbt__hci__evt__vs__le__connection__iq__report.md#a71227b896453143a6a4ad11b7e985a16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_durations](structbt__hci__evt__vs__le__connection__iq__report.md#a71227b896453143a6a4ad11b7e985a16);

[ 297](structbt__hci__evt__vs__le__connection__iq__report.md#aa2a9c3589bf8e152627a79c17102ec7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packet\_status](structbt__hci__evt__vs__le__connection__iq__report.md#aa2a9c3589bf8e152627a79c17102ec7c);

[ 298](structbt__hci__evt__vs__le__connection__iq__report.md#aaa29121a6b7fc8f9a76e6b83f6b80f4d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [conn\_evt\_counter](structbt__hci__evt__vs__le__connection__iq__report.md#aaa29121a6b7fc8f9a76e6b83f6b80f4d);

[ 299](structbt__hci__evt__vs__le__connection__iq__report.md#ab96606229994abe966f03c65d57e5568) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sample\_count](structbt__hci__evt__vs__le__connection__iq__report.md#ab96606229994abe966f03c65d57e5568);

[ 300](structbt__hci__evt__vs__le__connection__iq__report.md#abb2b6e915f8de6ad2013a79d0b4ee288) struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) [sample](structbt__hci__evt__vs__le__connection__iq__report.md#abb2b6e915f8de6ad2013a79d0b4ee288)[0];

301} \_\_packed;

302

303/\* Event mask bits \*/

304

[ 305](hci__vs_8h.md#a365da8f1041d55948caa4bf60ea349bd)#define BT\_EVT\_MASK\_VS\_FATAL\_ERROR BT\_EVT\_BIT(1)

[ 306](hci__vs_8h.md#aae4f865bf37b8933de070e16ea3047ec)#define BT\_EVT\_MASK\_VS\_TRACE\_INFO BT\_EVT\_BIT(2)

[ 307](hci__vs_8h.md#a9b4fcdd0de4197b3eb1ac65602e30408)#define BT\_EVT\_MASK\_VS\_SCAN\_REQ\_RX BT\_EVT\_BIT(3)

[ 308](hci__vs_8h.md#a74d2cf07f64f35318ec4ba24fd570dff)#define BT\_EVT\_MASK\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT BT\_EVT\_BIT(4)

[ 309](hci__vs_8h.md#a3971e9541300e12abb4ff36679d9b1f1)#define BT\_EVT\_MASK\_VS\_LE\_CONNECTION\_IQ\_REPORT BT\_EVT\_BIT(5)

310

[ 311](hci__vs_8h.md#a2f8e8f0070bde0e62019c71cc343fbe6)#define DEFAULT\_VS\_EVT\_MASK \

312 BT\_EVT\_MASK\_VS\_FATAL\_ERROR | BT\_EVT\_MASK\_VS\_TRACE\_INFO | BT\_EVT\_MASK\_VS\_SCAN\_REQ\_RX | \

313 BT\_EVT\_MASK\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT | \

314 BT\_EVT\_MASK\_VS\_LE\_CONNECTION\_IQ\_REPORT

315

316/\* Mesh HCI commands \*/

[ 317](hci__vs_8h.md#aeb5fdec34a0dfbf5d56a1aa42ba53318)#define BT\_HCI\_MESH\_REVISION 0x01

318

[ 319](hci__vs_8h.md#ad03814f2ae0c377234c5a340388b6ad1)#define BT\_HCI\_OP\_VS\_MESH BT\_OP(BT\_OGF\_VS, 0x0042)

[ 320](hci__vs_8h.md#a4817a57b69eda704a5a85198aa734792)#define BT\_HCI\_MESH\_EVT\_PREFIX 0xF0

321

[ 322](structbt__hci__cp__mesh.md)struct [bt\_hci\_cp\_mesh](structbt__hci__cp__mesh.md) {

[ 323](structbt__hci__cp__mesh.md#af29f0e2fd21f226143e0908c43c72a0f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structbt__hci__cp__mesh.md#af29f0e2fd21f226143e0908c43c72a0f);

324} \_\_packed;

325

[ 326](hci__vs_8h.md#af4cbb4f987c728312a0d00bea62db1c6)#define BT\_HCI\_OC\_MESH\_GET\_OPTS 0x00

[ 327](structbt__hci__rp__mesh__get__opts.md)struct [bt\_hci\_rp\_mesh\_get\_opts](structbt__hci__rp__mesh__get__opts.md) {

[ 328](structbt__hci__rp__mesh__get__opts.md#a6bc6ec02023723b280cb643bd19a6178) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__mesh__get__opts.md#a6bc6ec02023723b280cb643bd19a6178);

[ 329](structbt__hci__rp__mesh__get__opts.md#a50276763a447e1942b28ef33401c3a54) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structbt__hci__rp__mesh__get__opts.md#a50276763a447e1942b28ef33401c3a54);

[ 330](structbt__hci__rp__mesh__get__opts.md#abcc86aae5c91a0b551d6b7686c807349) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [revision](structbt__hci__rp__mesh__get__opts.md#abcc86aae5c91a0b551d6b7686c807349);

[ 331](structbt__hci__rp__mesh__get__opts.md#a06de566ae223d750a4d367575ca2a8a0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch\_map](structbt__hci__rp__mesh__get__opts.md#a06de566ae223d750a4d367575ca2a8a0);

[ 332](structbt__hci__rp__mesh__get__opts.md#aa000cd8242e6122d11dae17c726cf15a) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [min\_tx\_power](structbt__hci__rp__mesh__get__opts.md#aa000cd8242e6122d11dae17c726cf15a);

[ 333](structbt__hci__rp__mesh__get__opts.md#aeb49bfa06dc5b7200392c363ed6d67b0) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_tx\_power](structbt__hci__rp__mesh__get__opts.md#aeb49bfa06dc5b7200392c363ed6d67b0);

[ 334](structbt__hci__rp__mesh__get__opts.md#a9088d94213a80dfe7f3fb78188f24e05) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_scan\_filter](structbt__hci__rp__mesh__get__opts.md#a9088d94213a80dfe7f3fb78188f24e05);

[ 335](structbt__hci__rp__mesh__get__opts.md#a41b1c570c26ee911bd5f9b005492cb95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_filter\_pattern](structbt__hci__rp__mesh__get__opts.md#a41b1c570c26ee911bd5f9b005492cb95);

[ 336](structbt__hci__rp__mesh__get__opts.md#a1fbb06dca694411d58af86dee7a547fc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_adv\_slot](structbt__hci__rp__mesh__get__opts.md#a1fbb06dca694411d58af86dee7a547fc);

[ 337](structbt__hci__rp__mesh__get__opts.md#a5464a608f37c74f1d43e83d8877e405e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_tx\_window](structbt__hci__rp__mesh__get__opts.md#a5464a608f37c74f1d43e83d8877e405e);

[ 338](structbt__hci__rp__mesh__get__opts.md#af607a95cd367be6950a3185c2df2aca8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt\_prefix\_len](structbt__hci__rp__mesh__get__opts.md#af607a95cd367be6950a3185c2df2aca8);

[ 339](structbt__hci__rp__mesh__get__opts.md#af2f158774100ab0ca1537e69b3918eaa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evt\_prefix](structbt__hci__rp__mesh__get__opts.md#af2f158774100ab0ca1537e69b3918eaa);

340} \_\_packed;

341

[ 342](hci__vs_8h.md#aa31c2257092c0fdce4865ad5af1031ad)#define BT\_HCI\_MESH\_PATTERN\_LEN\_MAX 0x0f

343

[ 344](hci__vs_8h.md#af22f7e03d43595b10ebb6b2cfbe26540)#define BT\_HCI\_OC\_MESH\_SET\_SCAN\_FILTER 0x01

[ 345](structbt__hci__mesh__pattern.md)struct [bt\_hci\_mesh\_pattern](structbt__hci__mesh__pattern.md) {

[ 346](structbt__hci__mesh__pattern.md#a2ab9eac21c74a03416007f5b7d0f5bc4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pattern\_len](structbt__hci__mesh__pattern.md#a2ab9eac21c74a03416007f5b7d0f5bc4);

[ 347](structbt__hci__mesh__pattern.md#a78e52a2890db71c501885f575bc80de4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pattern](structbt__hci__mesh__pattern.md#a78e52a2890db71c501885f575bc80de4)[0];

348} \_\_packed;

349

[ 350](structbt__hci__cp__mesh__set__scan__filter.md)struct [bt\_hci\_cp\_mesh\_set\_scan\_filter](structbt__hci__cp__mesh__set__scan__filter.md) {

[ 351](structbt__hci__cp__mesh__set__scan__filter.md#aa1e74c7f4dc39cf2ad0c130bf8dafa72) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_filter](structbt__hci__cp__mesh__set__scan__filter.md#aa1e74c7f4dc39cf2ad0c130bf8dafa72);

[ 352](structbt__hci__cp__mesh__set__scan__filter.md#a41737323ab5723ce781f77f5752915e3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_dup](structbt__hci__cp__mesh__set__scan__filter.md#a41737323ab5723ce781f77f5752915e3);

[ 353](structbt__hci__cp__mesh__set__scan__filter.md#a3f99242946f3a5a8322a8333d9c58b30) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_patterns](structbt__hci__cp__mesh__set__scan__filter.md#a3f99242946f3a5a8322a8333d9c58b30);

[ 354](structbt__hci__cp__mesh__set__scan__filter.md#a4e72bcfac1beec704d860034abcf22c0) struct [bt\_hci\_mesh\_pattern](structbt__hci__mesh__pattern.md) [patterns](structbt__hci__cp__mesh__set__scan__filter.md#a4e72bcfac1beec704d860034abcf22c0)[0];

355} \_\_packed;

[ 356](structbt__hci__rp__mesh__set__scan__filter.md)struct [bt\_hci\_rp\_mesh\_set\_scan\_filter](structbt__hci__rp__mesh__set__scan__filter.md) {

[ 357](structbt__hci__rp__mesh__set__scan__filter.md#a2c832868fd092e235171a8e963c3eaf9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__mesh__set__scan__filter.md#a2c832868fd092e235171a8e963c3eaf9);

[ 358](structbt__hci__rp__mesh__set__scan__filter.md#a029223e5cfca25fc8b0565211734125e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structbt__hci__rp__mesh__set__scan__filter.md#a029223e5cfca25fc8b0565211734125e);

[ 359](structbt__hci__rp__mesh__set__scan__filter.md#afad78bfd78bb399cdeba73ccd10a66fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_filter](structbt__hci__rp__mesh__set__scan__filter.md#afad78bfd78bb399cdeba73ccd10a66fe);

360} \_\_packed;

361

[ 362](hci__vs_8h.md#ac73a04914ed07491fde6d463d111a9e2)#define BT\_HCI\_OC\_MESH\_ADVERTISE 0x02

[ 363](structbt__hci__cp__mesh__advertise.md)struct [bt\_hci\_cp\_mesh\_advertise](structbt__hci__cp__mesh__advertise.md) {

[ 364](structbt__hci__cp__mesh__advertise.md#a7ec17216955ac784cd213b11038c3521) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_slot](structbt__hci__cp__mesh__advertise.md#a7ec17216955ac784cd213b11038c3521);

[ 365](structbt__hci__cp__mesh__advertise.md#a6b6248069fa1e7eaf6825c52e38c3e78) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__mesh__advertise.md#a6b6248069fa1e7eaf6825c52e38c3e78);

[ 366](structbt__hci__cp__mesh__advertise.md#a0b22a8e1109db932f86bb7312dfeca9e) [bt\_addr\_t](structbt__addr__t.md) [random\_addr](structbt__hci__cp__mesh__advertise.md#a0b22a8e1109db932f86bb7312dfeca9e);

[ 367](structbt__hci__cp__mesh__advertise.md#a9ed6d2b96d9aa417ccd996e650bb00fa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch\_map](structbt__hci__cp__mesh__advertise.md#a9ed6d2b96d9aa417ccd996e650bb00fa);

[ 368](structbt__hci__cp__mesh__advertise.md#af1482ed0255e35d7a2016017dab8713a) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__cp__mesh__advertise.md#af1482ed0255e35d7a2016017dab8713a);

[ 369](structbt__hci__cp__mesh__advertise.md#a6ac4b4dad0ce54e69afd2b8e1f6cdf4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_tx\_delay](structbt__hci__cp__mesh__advertise.md#a6ac4b4dad0ce54e69afd2b8e1f6cdf4f);

[ 370](structbt__hci__cp__mesh__advertise.md#a3cf773db54448d5f7b3da652a798c712) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_tx\_delay](structbt__hci__cp__mesh__advertise.md#a3cf773db54448d5f7b3da652a798c712);

[ 371](structbt__hci__cp__mesh__advertise.md#a5ea37039c817d58d13feb98d5658cbf1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retx\_count](structbt__hci__cp__mesh__advertise.md#a5ea37039c817d58d13feb98d5658cbf1);

[ 372](structbt__hci__cp__mesh__advertise.md#a46242ef61b79723e5136373fa534a292) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retx\_interval](structbt__hci__cp__mesh__advertise.md#a46242ef61b79723e5136373fa534a292);

[ 373](structbt__hci__cp__mesh__advertise.md#a278c21295c73947d7b0971a6ac043d62) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_delay](structbt__hci__cp__mesh__advertise.md#a278c21295c73947d7b0971a6ac043d62);

[ 374](structbt__hci__cp__mesh__advertise.md#ab1b873984143301808f23824074e4df8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [scan\_duration](structbt__hci__cp__mesh__advertise.md#ab1b873984143301808f23824074e4df8);

[ 375](structbt__hci__cp__mesh__advertise.md#a0b190fcabae8555e65a251b37ab5b232) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_filter](structbt__hci__cp__mesh__advertise.md#a0b190fcabae8555e65a251b37ab5b232);

[ 376](structbt__hci__cp__mesh__advertise.md#a67aef4d217cb6b5762b4f823c8f234df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__hci__cp__mesh__advertise.md#a67aef4d217cb6b5762b4f823c8f234df);

[ 377](structbt__hci__cp__mesh__advertise.md#ad2af78fa8d14f1334b52f659f3497b4e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__mesh__advertise.md#ad2af78fa8d14f1334b52f659f3497b4e)[31];

378} \_\_packed;

[ 379](structbt__hci__rp__mesh__advertise.md)struct [bt\_hci\_rp\_mesh\_advertise](structbt__hci__rp__mesh__advertise.md) {

[ 380](structbt__hci__rp__mesh__advertise.md#a1514ae798eb501a0fcb02a48d222d62e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__mesh__advertise.md#a1514ae798eb501a0fcb02a48d222d62e);

[ 381](structbt__hci__rp__mesh__advertise.md#aa5a8760133b1f1554797f91a9c4cd8e3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structbt__hci__rp__mesh__advertise.md#aa5a8760133b1f1554797f91a9c4cd8e3);

[ 382](structbt__hci__rp__mesh__advertise.md#a0b88358de3223b528cdd424db25f05a0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_slot](structbt__hci__rp__mesh__advertise.md#a0b88358de3223b528cdd424db25f05a0);

383} \_\_packed;

384

[ 385](hci__vs_8h.md#a9f894b55f3db9df8bb2f710eb736ef1a)#define BT\_HCI\_OC\_MESH\_ADVERTISE\_TIMED 0x03

[ 386](structbt__hci__cp__mesh__advertise__timed.md)struct [bt\_hci\_cp\_mesh\_advertise\_timed](structbt__hci__cp__mesh__advertise__timed.md) {

[ 387](structbt__hci__cp__mesh__advertise__timed.md#a92f0163ec0854296ab76e49741d45196) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_slot](structbt__hci__cp__mesh__advertise__timed.md#a92f0163ec0854296ab76e49741d45196);

[ 388](structbt__hci__cp__mesh__advertise__timed.md#ae395b4a53ff9e7af8885b9583562022a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [own\_addr\_type](structbt__hci__cp__mesh__advertise__timed.md#ae395b4a53ff9e7af8885b9583562022a);

[ 389](structbt__hci__cp__mesh__advertise__timed.md#ada4348480db5f95acaad86bfa2ddbc7e) [bt\_addr\_t](structbt__addr__t.md) [random\_addr](structbt__hci__cp__mesh__advertise__timed.md#ada4348480db5f95acaad86bfa2ddbc7e);

[ 390](structbt__hci__cp__mesh__advertise__timed.md#aa5bf4322faa354cc6de0c707502b4ed0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch\_map](structbt__hci__cp__mesh__advertise__timed.md#aa5bf4322faa354cc6de0c707502b4ed0);

[ 391](structbt__hci__cp__mesh__advertise__timed.md#aae34dd11723383b5559dc102c59213c2) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__hci__cp__mesh__advertise__timed.md#aae34dd11723383b5559dc102c59213c2);

[ 392](structbt__hci__cp__mesh__advertise__timed.md#adfb3acf9ea540d8405c5979115053b15) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retx\_count](structbt__hci__cp__mesh__advertise__timed.md#adfb3acf9ea540d8405c5979115053b15);

[ 393](structbt__hci__cp__mesh__advertise__timed.md#a6718fd6031b2351eb033333a7302a21b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retx\_interval](structbt__hci__cp__mesh__advertise__timed.md#a6718fd6031b2351eb033333a7302a21b);

[ 394](structbt__hci__cp__mesh__advertise__timed.md#a85a7e965b8004cac3a4bc0107844c69b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [instant](structbt__hci__cp__mesh__advertise__timed.md#a85a7e965b8004cac3a4bc0107844c69b);

[ 395](structbt__hci__cp__mesh__advertise__timed.md#aee05619f0ed3b79f3bce5676c1f3aa8a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_delay](structbt__hci__cp__mesh__advertise__timed.md#aee05619f0ed3b79f3bce5676c1f3aa8a);

[ 396](structbt__hci__cp__mesh__advertise__timed.md#a1a5a5964eeff05fa232543756d234759) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_window](structbt__hci__cp__mesh__advertise__timed.md#a1a5a5964eeff05fa232543756d234759);

[ 397](structbt__hci__cp__mesh__advertise__timed.md#a78ecf7aa6ebf0739a585fed2a8710301) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__hci__cp__mesh__advertise__timed.md#a78ecf7aa6ebf0739a585fed2a8710301);

[ 398](structbt__hci__cp__mesh__advertise__timed.md#ac097c1ee537d9a480ae16205eafc7105) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__cp__mesh__advertise__timed.md#ac097c1ee537d9a480ae16205eafc7105)[31];

399} \_\_packed;

[ 400](structbt__hci__rp__mesh__advertise__timed.md)struct [bt\_hci\_rp\_mesh\_advertise\_timed](structbt__hci__rp__mesh__advertise__timed.md) {

[ 401](structbt__hci__rp__mesh__advertise__timed.md#a84554f3b501a48373e9f58875e6a46be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__mesh__advertise__timed.md#a84554f3b501a48373e9f58875e6a46be);

[ 402](structbt__hci__rp__mesh__advertise__timed.md#a15527bfd94e49f654b15fc188aa7c83a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structbt__hci__rp__mesh__advertise__timed.md#a15527bfd94e49f654b15fc188aa7c83a);

[ 403](structbt__hci__rp__mesh__advertise__timed.md#a17b39cd87b8392ef1ac7d721a55f6fab) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_slot](structbt__hci__rp__mesh__advertise__timed.md#a17b39cd87b8392ef1ac7d721a55f6fab);

404} \_\_packed;

405

[ 406](hci__vs_8h.md#a02491eb40b1874b4fdfb9eac5c3520c0)#define BT\_HCI\_OC\_MESH\_ADVERTISE\_CANCEL 0x04

[ 407](structbt__hci__cp__mesh__advertise__cancel.md)struct [bt\_hci\_cp\_mesh\_advertise\_cancel](structbt__hci__cp__mesh__advertise__cancel.md) {

[ 408](structbt__hci__cp__mesh__advertise__cancel.md#acd1409f2299c6bbddffd62d5e10e6e7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_slot](structbt__hci__cp__mesh__advertise__cancel.md#acd1409f2299c6bbddffd62d5e10e6e7c);

409} \_\_packed;

[ 410](structbt__hci__rp__mesh__advertise__cancel.md)struct [bt\_hci\_rp\_mesh\_advertise\_cancel](structbt__hci__rp__mesh__advertise__cancel.md) {

[ 411](structbt__hci__rp__mesh__advertise__cancel.md#ac8a13ab9c91a88859803dcf9f80658af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__mesh__advertise__cancel.md#ac8a13ab9c91a88859803dcf9f80658af);

[ 412](structbt__hci__rp__mesh__advertise__cancel.md#abcc6cd11403b34f04ff4e128628d7484) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structbt__hci__rp__mesh__advertise__cancel.md#abcc6cd11403b34f04ff4e128628d7484);

[ 413](structbt__hci__rp__mesh__advertise__cancel.md#afd121f3bb6d3453e7ec0bd9b895a3ccb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_slot](structbt__hci__rp__mesh__advertise__cancel.md#afd121f3bb6d3453e7ec0bd9b895a3ccb);

414} \_\_packed;

415

[ 416](hci__vs_8h.md#a4225e58654df90330fe007a8e99f4bdb)#define BT\_HCI\_OC\_MESH\_SET\_SCANNING 0x05

[ 417](structbt__hci__cp__mesh__set__scanning.md)struct [bt\_hci\_cp\_mesh\_set\_scanning](structbt__hci__cp__mesh__set__scanning.md) {

[ 418](structbt__hci__cp__mesh__set__scanning.md#aed23ad3e51e459bbc86945576a8113ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enable](structbt__hci__cp__mesh__set__scanning.md#aed23ad3e51e459bbc86945576a8113ef);

[ 419](structbt__hci__cp__mesh__set__scanning.md#a2b27e80def9b437c16de186d5371e140) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ch\_map](structbt__hci__cp__mesh__set__scanning.md#a2b27e80def9b437c16de186d5371e140);

[ 420](structbt__hci__cp__mesh__set__scanning.md#ac7cf268f484a575268fc6aa0f1b44cce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scan\_filter](structbt__hci__cp__mesh__set__scanning.md#ac7cf268f484a575268fc6aa0f1b44cce);

421} \_\_packed;

[ 422](structbt__hci__rp__mesh__set__scanning.md)struct [bt\_hci\_rp\_mesh\_set\_scanning](structbt__hci__rp__mesh__set__scanning.md) {

[ 423](structbt__hci__rp__mesh__set__scanning.md#afef848e9b6ad1e264d9e7ccc12391da6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__hci__rp__mesh__set__scanning.md#afef848e9b6ad1e264d9e7ccc12391da6);

[ 424](structbt__hci__rp__mesh__set__scanning.md#a88bee72d8dfb306d5f52b40789c6e0f1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structbt__hci__rp__mesh__set__scanning.md#a88bee72d8dfb306d5f52b40789c6e0f1);

425} \_\_packed;

426

427/\* Events \*/

[ 428](structbt__hci__evt__mesh.md)struct [bt\_hci\_evt\_mesh](structbt__hci__evt__mesh.md) {

[ 429](structbt__hci__evt__mesh.md#aaa8104b855bba787c69851ae7872a03e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prefix](structbt__hci__evt__mesh.md#aaa8104b855bba787c69851ae7872a03e);

[ 430](structbt__hci__evt__mesh.md#ac0186d74e355c90c866dda51605b85ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__hci__evt__mesh.md#ac0186d74e355c90c866dda51605b85ac);

431} \_\_packed;

432

[ 433](hci__vs_8h.md#af6e0159b30b73f3bbe8f5df7cdad8ef6)#define BT\_HCI\_EVT\_MESH\_ADV\_COMPLETE 0x00

[ 434](structbt__hci__evt__mesh__adv__complete.md)struct [bt\_hci\_evt\_mesh\_adv\_complete](structbt__hci__evt__mesh__adv__complete.md) {

[ 435](structbt__hci__evt__mesh__adv__complete.md#a2c9240a7fa61dad2c7a29b1ad4e555b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_slot](structbt__hci__evt__mesh__adv__complete.md#a2c9240a7fa61dad2c7a29b1ad4e555b1);

436} \_\_packed;

437

[ 438](hci__vs_8h.md#a77e3ea0a8f95449a11e4119c30313fe9)#define BT\_HCI\_EVT\_MESH\_SCANNING\_REPORT 0x01

[ 439](structbt__hci__evt__mesh__scan__report.md)struct [bt\_hci\_evt\_mesh\_scan\_report](structbt__hci__evt__mesh__scan__report.md) {

[ 440](structbt__hci__evt__mesh__scan__report.md#a20d5ffe0df68bee1205a5ee1a5abd6b2) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__hci__evt__mesh__scan__report.md#a20d5ffe0df68bee1205a5ee1a5abd6b2);

[ 441](structbt__hci__evt__mesh__scan__report.md#a3d283dd74c33b01fffb42bd4560c6e47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [chan](structbt__hci__evt__mesh__scan__report.md#a3d283dd74c33b01fffb42bd4560c6e47);

[ 442](structbt__hci__evt__mesh__scan__report.md#af8fb2e61dfe3a3860bf68af0ee8626e6) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__hci__evt__mesh__scan__report.md#af8fb2e61dfe3a3860bf68af0ee8626e6);

[ 443](structbt__hci__evt__mesh__scan__report.md#aa62526739d11d0fa2614e0822f3d70a7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [instant](structbt__hci__evt__mesh__scan__report.md#aa62526739d11d0fa2614e0822f3d70a7);

[ 444](structbt__hci__evt__mesh__scan__report.md#a281d2c97835fb2f42c6fb322a26d8899) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__hci__evt__mesh__scan__report.md#a281d2c97835fb2f42c6fb322a26d8899);

[ 445](structbt__hci__evt__mesh__scan__report.md#a573ad980305fb7c10b731a1867c97d1b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__hci__evt__mesh__scan__report.md#a573ad980305fb7c10b731a1867c97d1b)[0];

446} \_\_packed;

[ 447](structbt__hci__evt__mesh__scanning__report.md)struct [bt\_hci\_evt\_mesh\_scanning\_report](structbt__hci__evt__mesh__scanning__report.md) {

[ 448](structbt__hci__evt__mesh__scanning__report.md#a5daf719f2f5ec6e47f7a93d47d5c2b17) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_reports](structbt__hci__evt__mesh__scanning__report.md#a5daf719f2f5ec6e47f7a93d47d5c2b17);

[ 449](structbt__hci__evt__mesh__scanning__report.md#aa63b838e431b358bf1a3495998dfd952) struct [bt\_hci\_evt\_mesh\_scan\_report](structbt__hci__evt__mesh__scan__report.md) [reports](structbt__hci__evt__mesh__scanning__report.md#aa63b838e431b358bf1a3495998dfd952)[0];

450} \_\_packed;

451

[ 452](hci__vs_8h.md#ac8531e112ccb56279dd7f1cc3cdf339a)struct [net\_buf](structnet__buf.md) \*[hci\_vs\_err\_stack\_frame](hci__vs_8h.md#ac8531e112ccb56279dd7f1cc3cdf339a)(unsigned int reason, const z\_arch\_esf\_t \*esf);

[ 453](hci__vs_8h.md#a9a91c493cc947492d5a172a15abe9a4e)struct [net\_buf](structnet__buf.md) \*[hci\_vs\_err\_trace](hci__vs_8h.md#a9a91c493cc947492d5a172a15abe9a4e)(const char \*file, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) line, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pc);

[ 454](hci__vs_8h.md#afc9ea0e4f2260bf59336f2c66532d9b1)struct [net\_buf](structnet__buf.md) \*[hci\_vs\_err\_assert](hci__vs_8h.md#afc9ea0e4f2260bf59336f2c66532d9b1)(const char \*file, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) line);

455

456#ifdef \_\_cplusplus

457}

458#endif

459

460#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_VS\_H\_ \*/

[hci.h](hci_8h.md)

[hci\_vs\_err\_trace](hci__vs_8h.md#a9a91c493cc947492d5a172a15abe9a4e)

struct net\_buf \* hci\_vs\_err\_trace(const char \*file, uint32\_t line, uint64\_t pc)

[hci\_vs\_err\_stack\_frame](hci__vs_8h.md#ac8531e112ccb56279dd7f1cc3cdf339a)

struct net\_buf \* hci\_vs\_err\_stack\_frame(unsigned int reason, const z\_arch\_esf\_t \*esf)

[hci\_vs\_err\_assert](hci__vs_8h.md#afc9ea0e4f2260bf59336f2c66532d9b1)

struct net\_buf \* hci\_vs\_err\_assert(const char \*file, uint32\_t line)

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

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_addr\_t](structbt__addr__t.md)

Bluetooth Device Address.

**Definition** addr.h:40

[bt\_hci\_cp\_mesh\_advertise\_cancel](structbt__hci__cp__mesh__advertise__cancel.md)

**Definition** hci\_vs.h:407

[bt\_hci\_cp\_mesh\_advertise\_cancel::adv\_slot](structbt__hci__cp__mesh__advertise__cancel.md#acd1409f2299c6bbddffd62d5e10e6e7c)

uint8\_t adv\_slot

**Definition** hci\_vs.h:408

[bt\_hci\_cp\_mesh\_advertise\_timed](structbt__hci__cp__mesh__advertise__timed.md)

**Definition** hci\_vs.h:386

[bt\_hci\_cp\_mesh\_advertise\_timed::tx\_window](structbt__hci__cp__mesh__advertise__timed.md#a1a5a5964eeff05fa232543756d234759)

uint16\_t tx\_window

**Definition** hci\_vs.h:396

[bt\_hci\_cp\_mesh\_advertise\_timed::retx\_interval](structbt__hci__cp__mesh__advertise__timed.md#a6718fd6031b2351eb033333a7302a21b)

uint8\_t retx\_interval

**Definition** hci\_vs.h:393

[bt\_hci\_cp\_mesh\_advertise\_timed::data\_len](structbt__hci__cp__mesh__advertise__timed.md#a78ecf7aa6ebf0739a585fed2a8710301)

uint8\_t data\_len

**Definition** hci\_vs.h:397

[bt\_hci\_cp\_mesh\_advertise\_timed::instant](structbt__hci__cp__mesh__advertise__timed.md#a85a7e965b8004cac3a4bc0107844c69b)

uint32\_t instant

**Definition** hci\_vs.h:394

[bt\_hci\_cp\_mesh\_advertise\_timed::adv\_slot](structbt__hci__cp__mesh__advertise__timed.md#a92f0163ec0854296ab76e49741d45196)

uint8\_t adv\_slot

**Definition** hci\_vs.h:387

[bt\_hci\_cp\_mesh\_advertise\_timed::ch\_map](structbt__hci__cp__mesh__advertise__timed.md#aa5bf4322faa354cc6de0c707502b4ed0)

uint8\_t ch\_map

**Definition** hci\_vs.h:390

[bt\_hci\_cp\_mesh\_advertise\_timed::tx\_power](structbt__hci__cp__mesh__advertise__timed.md#aae34dd11723383b5559dc102c59213c2)

int8\_t tx\_power

**Definition** hci\_vs.h:391

[bt\_hci\_cp\_mesh\_advertise\_timed::data](structbt__hci__cp__mesh__advertise__timed.md#ac097c1ee537d9a480ae16205eafc7105)

uint8\_t data[31]

**Definition** hci\_vs.h:398

[bt\_hci\_cp\_mesh\_advertise\_timed::random\_addr](structbt__hci__cp__mesh__advertise__timed.md#ada4348480db5f95acaad86bfa2ddbc7e)

bt\_addr\_t random\_addr

**Definition** hci\_vs.h:389

[bt\_hci\_cp\_mesh\_advertise\_timed::retx\_count](structbt__hci__cp__mesh__advertise__timed.md#adfb3acf9ea540d8405c5979115053b15)

uint8\_t retx\_count

**Definition** hci\_vs.h:392

[bt\_hci\_cp\_mesh\_advertise\_timed::own\_addr\_type](structbt__hci__cp__mesh__advertise__timed.md#ae395b4a53ff9e7af8885b9583562022a)

uint8\_t own\_addr\_type

**Definition** hci\_vs.h:388

[bt\_hci\_cp\_mesh\_advertise\_timed::tx\_delay](structbt__hci__cp__mesh__advertise__timed.md#aee05619f0ed3b79f3bce5676c1f3aa8a)

uint16\_t tx\_delay

**Definition** hci\_vs.h:395

[bt\_hci\_cp\_mesh\_advertise](structbt__hci__cp__mesh__advertise.md)

**Definition** hci\_vs.h:363

[bt\_hci\_cp\_mesh\_advertise::scan\_filter](structbt__hci__cp__mesh__advertise.md#a0b190fcabae8555e65a251b37ab5b232)

uint8\_t scan\_filter

**Definition** hci\_vs.h:375

[bt\_hci\_cp\_mesh\_advertise::random\_addr](structbt__hci__cp__mesh__advertise.md#a0b22a8e1109db932f86bb7312dfeca9e)

bt\_addr\_t random\_addr

**Definition** hci\_vs.h:366

[bt\_hci\_cp\_mesh\_advertise::scan\_delay](structbt__hci__cp__mesh__advertise.md#a278c21295c73947d7b0971a6ac043d62)

uint8\_t scan\_delay

**Definition** hci\_vs.h:373

[bt\_hci\_cp\_mesh\_advertise::max\_tx\_delay](structbt__hci__cp__mesh__advertise.md#a3cf773db54448d5f7b3da652a798c712)

uint8\_t max\_tx\_delay

**Definition** hci\_vs.h:370

[bt\_hci\_cp\_mesh\_advertise::retx\_interval](structbt__hci__cp__mesh__advertise.md#a46242ef61b79723e5136373fa534a292)

uint8\_t retx\_interval

**Definition** hci\_vs.h:372

[bt\_hci\_cp\_mesh\_advertise::retx\_count](structbt__hci__cp__mesh__advertise.md#a5ea37039c817d58d13feb98d5658cbf1)

uint8\_t retx\_count

**Definition** hci\_vs.h:371

[bt\_hci\_cp\_mesh\_advertise::data\_len](structbt__hci__cp__mesh__advertise.md#a67aef4d217cb6b5762b4f823c8f234df)

uint8\_t data\_len

**Definition** hci\_vs.h:376

[bt\_hci\_cp\_mesh\_advertise::min\_tx\_delay](structbt__hci__cp__mesh__advertise.md#a6ac4b4dad0ce54e69afd2b8e1f6cdf4f)

uint8\_t min\_tx\_delay

**Definition** hci\_vs.h:369

[bt\_hci\_cp\_mesh\_advertise::own\_addr\_type](structbt__hci__cp__mesh__advertise.md#a6b6248069fa1e7eaf6825c52e38c3e78)

uint8\_t own\_addr\_type

**Definition** hci\_vs.h:365

[bt\_hci\_cp\_mesh\_advertise::adv\_slot](structbt__hci__cp__mesh__advertise.md#a7ec17216955ac784cd213b11038c3521)

uint8\_t adv\_slot

**Definition** hci\_vs.h:364

[bt\_hci\_cp\_mesh\_advertise::ch\_map](structbt__hci__cp__mesh__advertise.md#a9ed6d2b96d9aa417ccd996e650bb00fa)

uint8\_t ch\_map

**Definition** hci\_vs.h:367

[bt\_hci\_cp\_mesh\_advertise::scan\_duration](structbt__hci__cp__mesh__advertise.md#ab1b873984143301808f23824074e4df8)

uint16\_t scan\_duration

**Definition** hci\_vs.h:374

[bt\_hci\_cp\_mesh\_advertise::data](structbt__hci__cp__mesh__advertise.md#ad2af78fa8d14f1334b52f659f3497b4e)

uint8\_t data[31]

**Definition** hci\_vs.h:377

[bt\_hci\_cp\_mesh\_advertise::tx\_power](structbt__hci__cp__mesh__advertise.md#af1482ed0255e35d7a2016017dab8713a)

int8\_t tx\_power

**Definition** hci\_vs.h:368

[bt\_hci\_cp\_mesh\_set\_scan\_filter](structbt__hci__cp__mesh__set__scan__filter.md)

**Definition** hci\_vs.h:350

[bt\_hci\_cp\_mesh\_set\_scan\_filter::num\_patterns](structbt__hci__cp__mesh__set__scan__filter.md#a3f99242946f3a5a8322a8333d9c58b30)

uint8\_t num\_patterns

**Definition** hci\_vs.h:353

[bt\_hci\_cp\_mesh\_set\_scan\_filter::filter\_dup](structbt__hci__cp__mesh__set__scan__filter.md#a41737323ab5723ce781f77f5752915e3)

uint8\_t filter\_dup

**Definition** hci\_vs.h:352

[bt\_hci\_cp\_mesh\_set\_scan\_filter::patterns](structbt__hci__cp__mesh__set__scan__filter.md#a4e72bcfac1beec704d860034abcf22c0)

struct bt\_hci\_mesh\_pattern patterns[0]

**Definition** hci\_vs.h:354

[bt\_hci\_cp\_mesh\_set\_scan\_filter::scan\_filter](structbt__hci__cp__mesh__set__scan__filter.md#aa1e74c7f4dc39cf2ad0c130bf8dafa72)

uint8\_t scan\_filter

**Definition** hci\_vs.h:351

[bt\_hci\_cp\_mesh\_set\_scanning](structbt__hci__cp__mesh__set__scanning.md)

**Definition** hci\_vs.h:417

[bt\_hci\_cp\_mesh\_set\_scanning::ch\_map](structbt__hci__cp__mesh__set__scanning.md#a2b27e80def9b437c16de186d5371e140)

uint8\_t ch\_map

**Definition** hci\_vs.h:419

[bt\_hci\_cp\_mesh\_set\_scanning::scan\_filter](structbt__hci__cp__mesh__set__scanning.md#ac7cf268f484a575268fc6aa0f1b44cce)

uint8\_t scan\_filter

**Definition** hci\_vs.h:420

[bt\_hci\_cp\_mesh\_set\_scanning::enable](structbt__hci__cp__mesh__set__scanning.md#aed23ad3e51e459bbc86945576a8113ef)

uint8\_t enable

**Definition** hci\_vs.h:418

[bt\_hci\_cp\_mesh](structbt__hci__cp__mesh.md)

**Definition** hci\_vs.h:322

[bt\_hci\_cp\_mesh::opcode](structbt__hci__cp__mesh.md#af29f0e2fd21f226143e0908c43c72a0f)

uint8\_t opcode

**Definition** hci\_vs.h:323

[bt\_hci\_cp\_vs\_read\_tx\_power\_level](structbt__hci__cp__vs__read__tx__power__level.md)

**Definition** hci\_vs.h:177

[bt\_hci\_cp\_vs\_read\_tx\_power\_level::handle](structbt__hci__cp__vs__read__tx__power__level.md#a2bb528f003b22b88eec0d7389c84034f)

uint16\_t handle

**Definition** hci\_vs.h:179

[bt\_hci\_cp\_vs\_read\_tx\_power\_level::handle\_type](structbt__hci__cp__vs__read__tx__power__level.md#a776450ea2132fab77b9350ae46d3a1b5)

uint8\_t handle\_type

**Definition** hci\_vs.h:178

[bt\_hci\_cp\_vs\_reset](structbt__hci__cp__vs__reset.md)

**Definition** hci\_vs.h:86

[bt\_hci\_cp\_vs\_reset::type](structbt__hci__cp__vs__reset.md#aa3a47f4d2a593a9c756893ec28e49a00)

uint8\_t type

**Definition** hci\_vs.h:87

[bt\_hci\_cp\_vs\_set\_event\_mask](structbt__hci__cp__vs__set__event__mask.md)

**Definition** hci\_vs.h:79

[bt\_hci\_cp\_vs\_set\_event\_mask::event\_mask](structbt__hci__cp__vs__set__event__mask.md#ad5883adb065f04e923ff64093c78949a)

uint8\_t event\_mask[8]

**Definition** hci\_vs.h:80

[bt\_hci\_cp\_vs\_set\_min\_num\_used\_chans](structbt__hci__cp__vs__set__min__num__used__chans.md)

**Definition** hci\_vs.h:208

[bt\_hci\_cp\_vs\_set\_min\_num\_used\_chans::min\_used\_chans](structbt__hci__cp__vs__set__min__num__used__chans.md#a68262baddf6b7d2d42d61ad4c2690567)

uint8\_t min\_used\_chans

**Definition** hci\_vs.h:211

[bt\_hci\_cp\_vs\_set\_min\_num\_used\_chans::phys](structbt__hci__cp__vs__set__min__num__used__chans.md#a8cfa13723348bb43c19ceaa56fad2b1c)

uint8\_t phys

**Definition** hci\_vs.h:210

[bt\_hci\_cp\_vs\_set\_min\_num\_used\_chans::handle](structbt__hci__cp__vs__set__min__num__used__chans.md#aae4d29392f389a20f9be86870defc954)

uint16\_t handle

**Definition** hci\_vs.h:209

[bt\_hci\_cp\_vs\_set\_scan\_req\_reports](structbt__hci__cp__vs__set__scan__req__reports.md)

**Definition** hci\_vs.h:154

[bt\_hci\_cp\_vs\_set\_scan\_req\_reports::enable](structbt__hci__cp__vs__set__scan__req__reports.md#ac99b6b1fee39a2330c6d0c214c737fd3)

uint8\_t enable

**Definition** hci\_vs.h:155

[bt\_hci\_cp\_vs\_set\_trace\_enable](structbt__hci__cp__vs__set__trace__enable.md)

**Definition** hci\_vs.h:101

[bt\_hci\_cp\_vs\_set\_trace\_enable::type](structbt__hci__cp__vs__set__trace__enable.md#a18c3c81f13599a12903b12e350703dc5)

uint8\_t type

**Definition** hci\_vs.h:103

[bt\_hci\_cp\_vs\_set\_trace\_enable::enable](structbt__hci__cp__vs__set__trace__enable.md#a5676627500b6c5aff5986c53a0ba13a7)

uint8\_t enable

**Definition** hci\_vs.h:102

[bt\_hci\_cp\_vs\_set\_usb\_transport\_mode](structbt__hci__cp__vs__set__usb__transport__mode.md)

**Definition** hci\_vs.h:202

[bt\_hci\_cp\_vs\_set\_usb\_transport\_mode::mode](structbt__hci__cp__vs__set__usb__transport__mode.md#a651867bbfbc6ff642fbc294488259b4e)

uint8\_t mode

**Definition** hci\_vs.h:203

[bt\_hci\_cp\_vs\_write\_bd\_addr](structbt__hci__cp__vs__write__bd__addr.md)

**Definition** hci\_vs.h:91

[bt\_hci\_cp\_vs\_write\_bd\_addr::bdaddr](structbt__hci__cp__vs__write__bd__addr.md#af54e126fff610467dd730902893b6cd2)

bt\_addr\_t bdaddr

**Definition** hci\_vs.h:92

[bt\_hci\_cp\_vs\_write\_tx\_power\_level](structbt__hci__cp__vs__write__tx__power__level.md)

**Definition** hci\_vs.h:163

[bt\_hci\_cp\_vs\_write\_tx\_power\_level::handle\_type](structbt__hci__cp__vs__write__tx__power__level.md#a27e1b402a9a1a8850f551a18651e914e)

uint8\_t handle\_type

**Definition** hci\_vs.h:164

[bt\_hci\_cp\_vs\_write\_tx\_power\_level::tx\_power\_level](structbt__hci__cp__vs__write__tx__power__level.md#abd7f6c92c1463ec35cfd552ffce50b53)

int8\_t tx\_power\_level

**Definition** hci\_vs.h:166

[bt\_hci\_cp\_vs\_write\_tx\_power\_level::handle](structbt__hci__cp__vs__write__tx__power__level.md#adff511831f183e031d9c61781d337b9d)

uint16\_t handle

**Definition** hci\_vs.h:165

[bt\_hci\_evt\_mesh\_adv\_complete](structbt__hci__evt__mesh__adv__complete.md)

**Definition** hci\_vs.h:434

[bt\_hci\_evt\_mesh\_adv\_complete::adv\_slot](structbt__hci__evt__mesh__adv__complete.md#a2c9240a7fa61dad2c7a29b1ad4e555b1)

uint8\_t adv\_slot

**Definition** hci\_vs.h:435

[bt\_hci\_evt\_mesh\_scan\_report](structbt__hci__evt__mesh__scan__report.md)

**Definition** hci\_vs.h:439

[bt\_hci\_evt\_mesh\_scan\_report::addr](structbt__hci__evt__mesh__scan__report.md#a20d5ffe0df68bee1205a5ee1a5abd6b2)

bt\_addr\_le\_t addr

**Definition** hci\_vs.h:440

[bt\_hci\_evt\_mesh\_scan\_report::data\_len](structbt__hci__evt__mesh__scan__report.md#a281d2c97835fb2f42c6fb322a26d8899)

uint8\_t data\_len

**Definition** hci\_vs.h:444

[bt\_hci\_evt\_mesh\_scan\_report::chan](structbt__hci__evt__mesh__scan__report.md#a3d283dd74c33b01fffb42bd4560c6e47)

uint8\_t chan

**Definition** hci\_vs.h:441

[bt\_hci\_evt\_mesh\_scan\_report::data](structbt__hci__evt__mesh__scan__report.md#a573ad980305fb7c10b731a1867c97d1b)

uint8\_t data[0]

**Definition** hci\_vs.h:445

[bt\_hci\_evt\_mesh\_scan\_report::instant](structbt__hci__evt__mesh__scan__report.md#aa62526739d11d0fa2614e0822f3d70a7)

uint32\_t instant

**Definition** hci\_vs.h:443

[bt\_hci\_evt\_mesh\_scan\_report::rssi](structbt__hci__evt__mesh__scan__report.md#af8fb2e61dfe3a3860bf68af0ee8626e6)

int8\_t rssi

**Definition** hci\_vs.h:442

[bt\_hci\_evt\_mesh\_scanning\_report](structbt__hci__evt__mesh__scanning__report.md)

**Definition** hci\_vs.h:447

[bt\_hci\_evt\_mesh\_scanning\_report::num\_reports](structbt__hci__evt__mesh__scanning__report.md#a5daf719f2f5ec6e47f7a93d47d5c2b17)

uint8\_t num\_reports

**Definition** hci\_vs.h:448

[bt\_hci\_evt\_mesh\_scanning\_report::reports](structbt__hci__evt__mesh__scanning__report.md#aa63b838e431b358bf1a3495998dfd952)

struct bt\_hci\_evt\_mesh\_scan\_report reports[0]

**Definition** hci\_vs.h:449

[bt\_hci\_evt\_mesh](structbt__hci__evt__mesh.md)

**Definition** hci\_vs.h:428

[bt\_hci\_evt\_mesh::prefix](structbt__hci__evt__mesh.md#aaa8104b855bba787c69851ae7872a03e)

uint8\_t prefix

**Definition** hci\_vs.h:429

[bt\_hci\_evt\_mesh::subevent](structbt__hci__evt__mesh.md#ac0186d74e355c90c866dda51605b85ac)

uint8\_t subevent

**Definition** hci\_vs.h:430

[bt\_hci\_evt\_vs\_fatal\_error\_trace\_data](structbt__hci__evt__vs__fatal__error__trace__data.md)

**Definition** hci\_vs.h:241

[bt\_hci\_evt\_vs\_fatal\_error\_trace\_data::pc](structbt__hci__evt__vs__fatal__error__trace__data.md#a467d2de2a3b26ddef8c412957abfd820)

uint64\_t pc

**Definition** hci\_vs.h:242

[bt\_hci\_evt\_vs\_fatal\_error\_trace\_data::err\_info](structbt__hci__evt__vs__fatal__error__trace__data.md#ae1efc729b0c079fa922dcfffab6cdfa6)

uint8\_t err\_info[0]

**Definition** hci\_vs.h:243

[bt\_hci\_evt\_vs\_fatal\_error](structbt__hci__evt__vs__fatal__error.md)

**Definition** hci\_vs.h:246

[bt\_hci\_evt\_vs\_fatal\_error::type](structbt__hci__evt__vs__fatal__error.md#a15e84185f74e84e1f9ccd83dc4fa2798)

uint8\_t type

**Definition** hci\_vs.h:247

[bt\_hci\_evt\_vs\_fatal\_error::data](structbt__hci__evt__vs__fatal__error.md#aefd553e85eedb6e205da39916c5553aa)

uint8\_t data[0]

**Definition** hci\_vs.h:248

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report](structbt__hci__evt__vs__le__connection__iq__report.md)

**Definition** hci\_vs.h:289

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::rssi\_ant\_id](structbt__hci__evt__vs__le__connection__iq__report.md#a55a290121f661f155684d37fa0df77d2)

uint8\_t rssi\_ant\_id

**Definition** hci\_vs.h:294

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::slot\_durations](structbt__hci__evt__vs__le__connection__iq__report.md#a71227b896453143a6a4ad11b7e985a16)

uint8\_t slot\_durations

**Definition** hci\_vs.h:296

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::rssi](structbt__hci__evt__vs__le__connection__iq__report.md#a87d4a6ebd1cc172816f3fe786c22f058)

int16\_t rssi

**Definition** hci\_vs.h:293

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::conn\_handle](structbt__hci__evt__vs__le__connection__iq__report.md#a941d0e025334a0c041cc7a59b69f0af3)

uint16\_t conn\_handle

**Definition** hci\_vs.h:290

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::rx\_phy](structbt__hci__evt__vs__le__connection__iq__report.md#a959c7e2b910aec90f8b186550cb7f4d8)

uint8\_t rx\_phy

**Definition** hci\_vs.h:291

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::packet\_status](structbt__hci__evt__vs__le__connection__iq__report.md#aa2a9c3589bf8e152627a79c17102ec7c)

uint8\_t packet\_status

**Definition** hci\_vs.h:297

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::conn\_evt\_counter](structbt__hci__evt__vs__le__connection__iq__report.md#aaa29121a6b7fc8f9a76e6b83f6b80f4d)

uint16\_t conn\_evt\_counter

**Definition** hci\_vs.h:298

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::sample\_count](structbt__hci__evt__vs__le__connection__iq__report.md#ab96606229994abe966f03c65d57e5568)

uint8\_t sample\_count

**Definition** hci\_vs.h:299

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::sample](structbt__hci__evt__vs__le__connection__iq__report.md#abb2b6e915f8de6ad2013a79d0b4ee288)

struct bt\_hci\_le\_iq\_sample16 sample[0]

**Definition** hci\_vs.h:300

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::cte\_type](structbt__hci__evt__vs__le__connection__iq__report.md#ad714bb1f2292764eba9c506bcc72bccd)

uint8\_t cte\_type

**Definition** hci\_vs.h:295

[bt\_hci\_evt\_vs\_le\_connection\_iq\_report::data\_chan\_idx](structbt__hci__evt__vs__le__connection__iq__report.md#af634fa464d4ca435ea935ae58db86cfa)

uint8\_t data\_chan\_idx

**Definition** hci\_vs.h:292

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report](structbt__hci__evt__vs__le__connectionless__iq__report.md)

**Definition** hci\_vs.h:275

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::sample](structbt__hci__evt__vs__le__connectionless__iq__report.md#a17c9d19883c9d8e34f300fbff614b475)

struct bt\_hci\_le\_iq\_sample16 sample[0]

**Definition** hci\_vs.h:285

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::sample\_count](structbt__hci__evt__vs__le__connectionless__iq__report.md#a2698510deb6bd8943bf57104f96673db)

uint8\_t sample\_count

**Definition** hci\_vs.h:284

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::rssi\_ant\_id](structbt__hci__evt__vs__le__connectionless__iq__report.md#a5fcd776dce904763c5cc6fab9a1373f4)

uint8\_t rssi\_ant\_id

**Definition** hci\_vs.h:279

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::cte\_type](structbt__hci__evt__vs__le__connectionless__iq__report.md#a808a2a134104c69073af253a3c4dd1bd)

uint8\_t cte\_type

**Definition** hci\_vs.h:280

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::rssi](structbt__hci__evt__vs__le__connectionless__iq__report.md#a9b7eb8a5cf363c3aec96b49853056dc7)

int16\_t rssi

**Definition** hci\_vs.h:278

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::sync\_handle](structbt__hci__evt__vs__le__connectionless__iq__report.md#a9c199121ac475d635fc51289e8eba979)

uint16\_t sync\_handle

**Definition** hci\_vs.h:276

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::per\_evt\_counter](structbt__hci__evt__vs__le__connectionless__iq__report.md#ab6911af90d85c565615c437715d9c7eb)

uint16\_t per\_evt\_counter

**Definition** hci\_vs.h:283

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::slot\_durations](structbt__hci__evt__vs__le__connectionless__iq__report.md#ac0b077d7b5e2b7c5ce61b3060913cad5)

uint8\_t slot\_durations

**Definition** hci\_vs.h:281

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::chan\_idx](structbt__hci__evt__vs__le__connectionless__iq__report.md#ad15beccc7c2207565678ebef72346158)

uint8\_t chan\_idx

**Definition** hci\_vs.h:277

[bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::packet\_status](structbt__hci__evt__vs__le__connectionless__iq__report.md#af5b27c1504ce4ff8afe23c28a9ac423f)

uint8\_t packet\_status

**Definition** hci\_vs.h:282

[bt\_hci\_evt\_vs\_scan\_req\_rx](structbt__hci__evt__vs__scan__req__rx.md)

**Definition** hci\_vs.h:263

[bt\_hci\_evt\_vs\_scan\_req\_rx::addr](structbt__hci__evt__vs__scan__req__rx.md#a56613220a50bc50a771f432b7e617d5b)

bt\_addr\_le\_t addr

**Definition** hci\_vs.h:264

[bt\_hci\_evt\_vs\_scan\_req\_rx::rssi](structbt__hci__evt__vs__scan__req__rx.md#acbfa7ec0a3ab1f94f53598a9d8242aba)

int8\_t rssi

**Definition** hci\_vs.h:265

[bt\_hci\_evt\_vs\_trace\_info](structbt__hci__evt__vs__trace__info.md)

**Definition** hci\_vs.h:257

[bt\_hci\_evt\_vs\_trace\_info::data](structbt__hci__evt__vs__trace__info.md#ae524df8cc722cda0fa86127a6b8e56da)

uint8\_t data[0]

**Definition** hci\_vs.h:259

[bt\_hci\_evt\_vs\_trace\_info::type](structbt__hci__evt__vs__trace__info.md#af563e07c5364df229eb767e545c8aaa2)

uint8\_t type

**Definition** hci\_vs.h:258

[bt\_hci\_evt\_vs](structbt__hci__evt__vs.md)

**Definition** hci\_vs.h:216

[bt\_hci\_evt\_vs::subevent](structbt__hci__evt__vs.md#aadf6dd6172922d32a4a40be003f09876)

uint8\_t subevent

**Definition** hci\_vs.h:217

[bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md)

**Definition** hci\_vs.h:268

[bt\_hci\_le\_iq\_sample16::q](structbt__hci__le__iq__sample16.md#aa317d2a9f451eeecb35ff05044ea6dc3)

int16\_t q

**Definition** hci\_vs.h:270

[bt\_hci\_le\_iq\_sample16::i](structbt__hci__le__iq__sample16.md#ace47fd665d57f7ad7eb0a04ec8e54a47)

int16\_t i

**Definition** hci\_vs.h:269

[bt\_hci\_mesh\_pattern](structbt__hci__mesh__pattern.md)

**Definition** hci\_vs.h:345

[bt\_hci\_mesh\_pattern::pattern\_len](structbt__hci__mesh__pattern.md#a2ab9eac21c74a03416007f5b7d0f5bc4)

uint8\_t pattern\_len

**Definition** hci\_vs.h:346

[bt\_hci\_mesh\_pattern::pattern](structbt__hci__mesh__pattern.md#a78e52a2890db71c501885f575bc80de4)

uint8\_t pattern[0]

**Definition** hci\_vs.h:347

[bt\_hci\_rp\_mesh\_advertise\_cancel](structbt__hci__rp__mesh__advertise__cancel.md)

**Definition** hci\_vs.h:410

[bt\_hci\_rp\_mesh\_advertise\_cancel::opcode](structbt__hci__rp__mesh__advertise__cancel.md#abcc6cd11403b34f04ff4e128628d7484)

uint8\_t opcode

**Definition** hci\_vs.h:412

[bt\_hci\_rp\_mesh\_advertise\_cancel::status](structbt__hci__rp__mesh__advertise__cancel.md#ac8a13ab9c91a88859803dcf9f80658af)

uint8\_t status

**Definition** hci\_vs.h:411

[bt\_hci\_rp\_mesh\_advertise\_cancel::adv\_slot](structbt__hci__rp__mesh__advertise__cancel.md#afd121f3bb6d3453e7ec0bd9b895a3ccb)

uint8\_t adv\_slot

**Definition** hci\_vs.h:413

[bt\_hci\_rp\_mesh\_advertise\_timed](structbt__hci__rp__mesh__advertise__timed.md)

**Definition** hci\_vs.h:400

[bt\_hci\_rp\_mesh\_advertise\_timed::opcode](structbt__hci__rp__mesh__advertise__timed.md#a15527bfd94e49f654b15fc188aa7c83a)

uint8\_t opcode

**Definition** hci\_vs.h:402

[bt\_hci\_rp\_mesh\_advertise\_timed::adv\_slot](structbt__hci__rp__mesh__advertise__timed.md#a17b39cd87b8392ef1ac7d721a55f6fab)

uint8\_t adv\_slot

**Definition** hci\_vs.h:403

[bt\_hci\_rp\_mesh\_advertise\_timed::status](structbt__hci__rp__mesh__advertise__timed.md#a84554f3b501a48373e9f58875e6a46be)

uint8\_t status

**Definition** hci\_vs.h:401

[bt\_hci\_rp\_mesh\_advertise](structbt__hci__rp__mesh__advertise.md)

**Definition** hci\_vs.h:379

[bt\_hci\_rp\_mesh\_advertise::adv\_slot](structbt__hci__rp__mesh__advertise.md#a0b88358de3223b528cdd424db25f05a0)

uint8\_t adv\_slot

**Definition** hci\_vs.h:382

[bt\_hci\_rp\_mesh\_advertise::status](structbt__hci__rp__mesh__advertise.md#a1514ae798eb501a0fcb02a48d222d62e)

uint8\_t status

**Definition** hci\_vs.h:380

[bt\_hci\_rp\_mesh\_advertise::opcode](structbt__hci__rp__mesh__advertise.md#aa5a8760133b1f1554797f91a9c4cd8e3)

uint8\_t opcode

**Definition** hci\_vs.h:381

[bt\_hci\_rp\_mesh\_get\_opts](structbt__hci__rp__mesh__get__opts.md)

**Definition** hci\_vs.h:327

[bt\_hci\_rp\_mesh\_get\_opts::ch\_map](structbt__hci__rp__mesh__get__opts.md#a06de566ae223d750a4d367575ca2a8a0)

uint8\_t ch\_map

**Definition** hci\_vs.h:331

[bt\_hci\_rp\_mesh\_get\_opts::max\_adv\_slot](structbt__hci__rp__mesh__get__opts.md#a1fbb06dca694411d58af86dee7a547fc)

uint8\_t max\_adv\_slot

**Definition** hci\_vs.h:336

[bt\_hci\_rp\_mesh\_get\_opts::max\_filter\_pattern](structbt__hci__rp__mesh__get__opts.md#a41b1c570c26ee911bd5f9b005492cb95)

uint8\_t max\_filter\_pattern

**Definition** hci\_vs.h:335

[bt\_hci\_rp\_mesh\_get\_opts::opcode](structbt__hci__rp__mesh__get__opts.md#a50276763a447e1942b28ef33401c3a54)

uint8\_t opcode

**Definition** hci\_vs.h:329

[bt\_hci\_rp\_mesh\_get\_opts::max\_tx\_window](structbt__hci__rp__mesh__get__opts.md#a5464a608f37c74f1d43e83d8877e405e)

uint8\_t max\_tx\_window

**Definition** hci\_vs.h:337

[bt\_hci\_rp\_mesh\_get\_opts::status](structbt__hci__rp__mesh__get__opts.md#a6bc6ec02023723b280cb643bd19a6178)

uint8\_t status

**Definition** hci\_vs.h:328

[bt\_hci\_rp\_mesh\_get\_opts::max\_scan\_filter](structbt__hci__rp__mesh__get__opts.md#a9088d94213a80dfe7f3fb78188f24e05)

uint8\_t max\_scan\_filter

**Definition** hci\_vs.h:334

[bt\_hci\_rp\_mesh\_get\_opts::min\_tx\_power](structbt__hci__rp__mesh__get__opts.md#aa000cd8242e6122d11dae17c726cf15a)

int8\_t min\_tx\_power

**Definition** hci\_vs.h:332

[bt\_hci\_rp\_mesh\_get\_opts::revision](structbt__hci__rp__mesh__get__opts.md#abcc86aae5c91a0b551d6b7686c807349)

uint8\_t revision

**Definition** hci\_vs.h:330

[bt\_hci\_rp\_mesh\_get\_opts::max\_tx\_power](structbt__hci__rp__mesh__get__opts.md#aeb49bfa06dc5b7200392c363ed6d67b0)

int8\_t max\_tx\_power

**Definition** hci\_vs.h:333

[bt\_hci\_rp\_mesh\_get\_opts::evt\_prefix](structbt__hci__rp__mesh__get__opts.md#af2f158774100ab0ca1537e69b3918eaa)

uint8\_t evt\_prefix

**Definition** hci\_vs.h:339

[bt\_hci\_rp\_mesh\_get\_opts::evt\_prefix\_len](structbt__hci__rp__mesh__get__opts.md#af607a95cd367be6950a3185c2df2aca8)

uint8\_t evt\_prefix\_len

**Definition** hci\_vs.h:338

[bt\_hci\_rp\_mesh\_set\_scan\_filter](structbt__hci__rp__mesh__set__scan__filter.md)

**Definition** hci\_vs.h:356

[bt\_hci\_rp\_mesh\_set\_scan\_filter::opcode](structbt__hci__rp__mesh__set__scan__filter.md#a029223e5cfca25fc8b0565211734125e)

uint8\_t opcode

**Definition** hci\_vs.h:358

[bt\_hci\_rp\_mesh\_set\_scan\_filter::status](structbt__hci__rp__mesh__set__scan__filter.md#a2c832868fd092e235171a8e963c3eaf9)

uint8\_t status

**Definition** hci\_vs.h:357

[bt\_hci\_rp\_mesh\_set\_scan\_filter::scan\_filter](structbt__hci__rp__mesh__set__scan__filter.md#afad78bfd78bb399cdeba73ccd10a66fe)

uint8\_t scan\_filter

**Definition** hci\_vs.h:359

[bt\_hci\_rp\_mesh\_set\_scanning](structbt__hci__rp__mesh__set__scanning.md)

**Definition** hci\_vs.h:422

[bt\_hci\_rp\_mesh\_set\_scanning::opcode](structbt__hci__rp__mesh__set__scanning.md#a88bee72d8dfb306d5f52b40789c6e0f1)

uint8\_t opcode

**Definition** hci\_vs.h:424

[bt\_hci\_rp\_mesh\_set\_scanning::status](structbt__hci__rp__mesh__set__scanning.md#afef848e9b6ad1e264d9e7ccc12391da6)

uint8\_t status

**Definition** hci\_vs.h:423

[bt\_hci\_rp\_vs\_read\_build\_info](structbt__hci__rp__vs__read__build__info.md)

**Definition** hci\_vs.h:107

[bt\_hci\_rp\_vs\_read\_build\_info::info](structbt__hci__rp__vs__read__build__info.md#aba2aaa3916221768412eed39cc85ab5f)

uint8\_t info[0]

**Definition** hci\_vs.h:109

[bt\_hci\_rp\_vs\_read\_build\_info::status](structbt__hci__rp__vs__read__build__info.md#acdebc0d6f8d713075c6e5e69cf136ea3)

uint8\_t status

**Definition** hci\_vs.h:108

[bt\_hci\_rp\_vs\_read\_chip\_temp](structbt__hci__rp__vs__read__chip__temp.md)

**Definition** hci\_vs.h:132

[bt\_hci\_rp\_vs\_read\_chip\_temp::temps](structbt__hci__rp__vs__read__chip__temp.md#a2487c86e1975f69f307e70624abf9519)

int8\_t temps

**Definition** hci\_vs.h:134

[bt\_hci\_rp\_vs\_read\_chip\_temp::status](structbt__hci__rp__vs__read__chip__temp.md#a324034b28a6526e195de576432f8ed32)

uint8\_t status

**Definition** hci\_vs.h:133

[bt\_hci\_rp\_vs\_read\_host\_stack\_cmds](structbt__hci__rp__vs__read__host__stack__cmds.md)

**Definition** hci\_vs.h:145

[bt\_hci\_rp\_vs\_read\_host\_stack\_cmds::c](structbt__hci__rp__vs__read__host__stack__cmds.md#a27b591f7784aaec063afc37105c00880)

struct bt\_hci\_vs\_cmd c[0]

**Definition** hci\_vs.h:148

[bt\_hci\_rp\_vs\_read\_host\_stack\_cmds::status](structbt__hci__rp__vs__read__host__stack__cmds.md#a374e54391bcb72b5cde885cb04269e9a)

uint8\_t status

**Definition** hci\_vs.h:146

[bt\_hci\_rp\_vs\_read\_host\_stack\_cmds::num\_cmds](structbt__hci__rp__vs__read__host__stack__cmds.md#ac11d1ed48e49f9ce1d31709be76aed95)

uint8\_t num\_cmds

**Definition** hci\_vs.h:147

[bt\_hci\_rp\_vs\_read\_key\_hierarchy\_roots](structbt__hci__rp__vs__read__key__hierarchy__roots.md)

**Definition** hci\_vs.h:125

[bt\_hci\_rp\_vs\_read\_key\_hierarchy\_roots::status](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a3ab9afeea4cc59853ef5a2f04ee39405)

uint8\_t status

**Definition** hci\_vs.h:126

[bt\_hci\_rp\_vs\_read\_key\_hierarchy\_roots::ir](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a5ce7b3ba72b129191d8a7d73f9978682)

uint8\_t ir[16]

**Definition** hci\_vs.h:127

[bt\_hci\_rp\_vs\_read\_key\_hierarchy\_roots::er](structbt__hci__rp__vs__read__key__hierarchy__roots.md#a62c6df2ac691c06f481189fb61b0f99c)

uint8\_t er[16]

**Definition** hci\_vs.h:128

[bt\_hci\_rp\_vs\_read\_static\_addrs](structbt__hci__rp__vs__read__static__addrs.md)

**Definition** hci\_vs.h:118

[bt\_hci\_rp\_vs\_read\_static\_addrs::num\_addrs](structbt__hci__rp__vs__read__static__addrs.md#a482a0984602d4d59ef9572d4e1053a99)

uint8\_t num\_addrs

**Definition** hci\_vs.h:120

[bt\_hci\_rp\_vs\_read\_static\_addrs::status](structbt__hci__rp__vs__read__static__addrs.md#af3ddb349e82e7a5edcb86300c8d8a548)

uint8\_t status

**Definition** hci\_vs.h:119

[bt\_hci\_rp\_vs\_read\_static\_addrs::a](structbt__hci__rp__vs__read__static__addrs.md#af8175d96852a67ebcfa4da5019e618e9)

struct bt\_hci\_vs\_static\_addr a[0]

**Definition** hci\_vs.h:121

[bt\_hci\_rp\_vs\_read\_supported\_commands](structbt__hci__rp__vs__read__supported__commands.md)

**Definition** hci\_vs.h:67

[bt\_hci\_rp\_vs\_read\_supported\_commands::commands](structbt__hci__rp__vs__read__supported__commands.md#a699129590cb1f5a3418d8e0eab3868e4)

uint8\_t commands[64]

**Definition** hci\_vs.h:69

[bt\_hci\_rp\_vs\_read\_supported\_commands::status](structbt__hci__rp__vs__read__supported__commands.md#afe9e5d1647b0cea192fa281367dc6c85)

uint8\_t status

**Definition** hci\_vs.h:68

[bt\_hci\_rp\_vs\_read\_supported\_features](structbt__hci__rp__vs__read__supported__features.md)

**Definition** hci\_vs.h:73

[bt\_hci\_rp\_vs\_read\_supported\_features::features](structbt__hci__rp__vs__read__supported__features.md#a0459b49e864d3069d4ba818ef2ed59ca)

uint8\_t features[8]

**Definition** hci\_vs.h:75

[bt\_hci\_rp\_vs\_read\_supported\_features::status](structbt__hci__rp__vs__read__supported__features.md#a40468d71ba659d8ef593d82aca0bc583)

uint8\_t status

**Definition** hci\_vs.h:74

[bt\_hci\_rp\_vs\_read\_tx\_power\_level](structbt__hci__rp__vs__read__tx__power__level.md)

**Definition** hci\_vs.h:182

[bt\_hci\_rp\_vs\_read\_tx\_power\_level::handle\_type](structbt__hci__rp__vs__read__tx__power__level.md#a86f8e314571df0dfbc0995fb14108650)

uint8\_t handle\_type

**Definition** hci\_vs.h:184

[bt\_hci\_rp\_vs\_read\_tx\_power\_level::tx\_power\_level](structbt__hci__rp__vs__read__tx__power__level.md#ae1e1ee5319283a725c1eb1ab3ad13481)

int8\_t tx\_power\_level

**Definition** hci\_vs.h:186

[bt\_hci\_rp\_vs\_read\_tx\_power\_level::handle](structbt__hci__rp__vs__read__tx__power__level.md#ae2755a4ba68c73c5bb97f58400d8b16d)

uint16\_t handle

**Definition** hci\_vs.h:185

[bt\_hci\_rp\_vs\_read\_tx\_power\_level::status](structbt__hci__rp__vs__read__tx__power__level.md#ae5011313891d5ac4eaf0383e125bf786)

uint8\_t status

**Definition** hci\_vs.h:183

[bt\_hci\_rp\_vs\_read\_usb\_transport\_mode](structbt__hci__rp__vs__read__usb__transport__mode.md)

**Definition** hci\_vs.h:191

[bt\_hci\_rp\_vs\_read\_usb\_transport\_mode::num\_supported\_modes](structbt__hci__rp__vs__read__usb__transport__mode.md#a25070132401d9b3d3dcd3f325f66da64)

uint8\_t num\_supported\_modes

**Definition** hci\_vs.h:193

[bt\_hci\_rp\_vs\_read\_usb\_transport\_mode::status](structbt__hci__rp__vs__read__usb__transport__mode.md#a7fdfe43b633c153fd9e7cf1f470b435f)

uint8\_t status

**Definition** hci\_vs.h:192

[bt\_hci\_rp\_vs\_read\_usb\_transport\_mode::supported\_mode](structbt__hci__rp__vs__read__usb__transport__mode.md#aec8f1c7acd972d00b8f1070ed444b155)

uint8\_t supported\_mode[0]

**Definition** hci\_vs.h:194

[bt\_hci\_rp\_vs\_read\_version\_info](structbt__hci__rp__vs__read__version__info.md)

**Definition** hci\_vs.h:56

[bt\_hci\_rp\_vs\_read\_version\_info::fw\_version](structbt__hci__rp__vs__read__version__info.md#a147b0b73db111465549196ed67ca60d6)

uint8\_t fw\_version

**Definition** hci\_vs.h:61

[bt\_hci\_rp\_vs\_read\_version\_info::fw\_variant](structbt__hci__rp__vs__read__version__info.md#a24ad5440e85d2e91c0495a3b06ac7469)

uint8\_t fw\_variant

**Definition** hci\_vs.h:60

[bt\_hci\_rp\_vs\_read\_version\_info::fw\_build](structbt__hci__rp__vs__read__version__info.md#a43fc428c7ea444be2100e970b444f51a)

uint32\_t fw\_build

**Definition** hci\_vs.h:63

[bt\_hci\_rp\_vs\_read\_version\_info::fw\_revision](structbt__hci__rp__vs__read__version__info.md#a47b4d799df9aeca67f6136264e13ef16)

uint16\_t fw\_revision

**Definition** hci\_vs.h:62

[bt\_hci\_rp\_vs\_read\_version\_info::status](structbt__hci__rp__vs__read__version__info.md#a7cdff04c26d2f5864a07fc0a7c31a89a)

uint8\_t status

**Definition** hci\_vs.h:57

[bt\_hci\_rp\_vs\_read\_version\_info::hw\_platform](structbt__hci__rp__vs__read__version__info.md#a7e69f89d5562205f780dc05128b5d46a)

uint16\_t hw\_platform

**Definition** hci\_vs.h:58

[bt\_hci\_rp\_vs\_read\_version\_info::hw\_variant](structbt__hci__rp__vs__read__version__info.md#abd4ea8df7b338e48490ceafae1b8e6be)

uint16\_t hw\_variant

**Definition** hci\_vs.h:59

[bt\_hci\_rp\_vs\_write\_tx\_power\_level](structbt__hci__rp__vs__write__tx__power__level.md)

**Definition** hci\_vs.h:169

[bt\_hci\_rp\_vs\_write\_tx\_power\_level::handle\_type](structbt__hci__rp__vs__write__tx__power__level.md#a0ba154d288f23fb5d859d620a9205a68)

uint8\_t handle\_type

**Definition** hci\_vs.h:171

[bt\_hci\_rp\_vs\_write\_tx\_power\_level::status](structbt__hci__rp__vs__write__tx__power__level.md#a2d462d79165a3fbc98a3a24c6d6ad8fa)

uint8\_t status

**Definition** hci\_vs.h:170

[bt\_hci\_rp\_vs\_write\_tx\_power\_level::selected\_tx\_power](structbt__hci__rp__vs__write__tx__power__level.md#a6a8c6103c609f2c05cfb46476e23d58e)

int8\_t selected\_tx\_power

**Definition** hci\_vs.h:173

[bt\_hci\_rp\_vs\_write\_tx\_power\_level::handle](structbt__hci__rp__vs__write__tx__power__level.md#ac7c2eb75ec96f79d67c0a7b3ce851e14)

uint16\_t handle

**Definition** hci\_vs.h:172

[bt\_hci\_vs\_cmd](structbt__hci__vs__cmd.md)

**Definition** hci\_vs.h:137

[bt\_hci\_vs\_cmd::opcode\_base](structbt__hci__vs__cmd.md#a1ca54af74a178506b954fe8e43a04895)

uint16\_t opcode\_base

**Definition** hci\_vs.h:139

[bt\_hci\_vs\_cmd::vendor\_id](structbt__hci__vs__cmd.md#a640c7523215b676dd8922d95c136cc4b)

uint16\_t vendor\_id

**Definition** hci\_vs.h:138

[bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m](structbt__hci__vs__fata__error__cpu__data__cortex__m.md)

**Definition** hci\_vs.h:225

[bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m::ip](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a02a8928cf7754bef640e74d41d72f345)

uint32\_t ip

**Definition** hci\_vs.h:230

[bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m::a4](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a2cbd9ac477601f457ea7a1d757aeaf30)

uint32\_t a4

**Definition** hci\_vs.h:229

[bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m::a3](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a3d5e6e7be359a3964ed49051253c428f)

uint32\_t a3

**Definition** hci\_vs.h:228

[bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m::xpsr](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a472c058324fa9349a23586c99d786d32)

uint32\_t xpsr

**Definition** hci\_vs.h:232

[bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m::a2](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#a7c177a75e51c86faf289d37bff84683c)

uint32\_t a2

**Definition** hci\_vs.h:227

[bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m::lr](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#aa146cf7122eaf4b1d0de328dc05081de)

uint32\_t lr

**Definition** hci\_vs.h:231

[bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m::a1](structbt__hci__vs__fata__error__cpu__data__cortex__m.md#add43bedce9999e88f10cb98f3bbb69ab)

uint32\_t a1

**Definition** hci\_vs.h:226

[bt\_hci\_vs\_fatal\_error\_stack\_frame](structbt__hci__vs__fatal__error__stack__frame.md)

**Definition** hci\_vs.h:235

[bt\_hci\_vs\_fatal\_error\_stack\_frame::cpu\_type](structbt__hci__vs__fatal__error__stack__frame.md#a1530d501d5fd5dade63219e16ddd5d85)

uint8\_t cpu\_type

**Definition** hci\_vs.h:237

[bt\_hci\_vs\_fatal\_error\_stack\_frame::cpu\_data](structbt__hci__vs__fatal__error__stack__frame.md#a89e4ede59af9b37fcaeee00ea028f930)

uint8\_t cpu\_data[0]

**Definition** hci\_vs.h:238

[bt\_hci\_vs\_fatal\_error\_stack\_frame::reason](structbt__hci__vs__fatal__error__stack__frame.md#ac2f93a05158d4c170848ee4afdfe1bd1)

uint32\_t reason

**Definition** hci\_vs.h:236

[bt\_hci\_vs\_static\_addr](structbt__hci__vs__static__addr.md)

**Definition** hci\_vs.h:112

[bt\_hci\_vs\_static\_addr::bdaddr](structbt__hci__vs__static__addr.md#aa9b61e3f589465c68a4b6356c9de8b66)

bt\_addr\_t bdaddr

**Definition** hci\_vs.h:113

[bt\_hci\_vs\_static\_addr::ir](structbt__hci__vs__static__addr.md#afef2fbf31b7d5101ee48e51476c81698)

uint8\_t ir[16]

**Definition** hci\_vs.h:114

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_vs.h](hci__vs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
