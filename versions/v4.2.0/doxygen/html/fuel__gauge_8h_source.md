---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/fuel__gauge_8h_source.html
original_path: doxygen/html/fuel__gauge_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fuel\_gauge.h

[Go to the documentation of this file.](fuel__gauge_8h.md)

1/\*

2 \* Copyright 2022 Google LLC

3 \* Copyright 2023 Microsoft Corporation

4 \* Copyright (c) 2025 Philipp Steiner <philipp.steiner1987@gmail.com>

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_BATTERY\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_BATTERY\_H\_

11

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif /\* \_\_cplusplus \*/

24

25#include <[errno.h](errno_8h.md)>

26#include <[stdbool.h](stdbool_8h.md)>

27#include <stddef.h>

28#include <[stdint.h](stdint_8h.md)>

29

30#include <[zephyr/device.h](device_8h.md)>

31

[ 32](group__fuel__gauge__interface.md#gae49908857800bdd010d59895cfad9171)enum [fuel\_gauge\_prop\_type](group__fuel__gauge__interface.md#gae49908857800bdd010d59895cfad9171) {

[ 40](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396) [FUEL\_GAUGE\_AVG\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396) = 0,

41

[ 43](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad431ab05b79f942dd500ce84980cf81f) [FUEL\_GAUGE\_BATTERY\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad431ab05b79f942dd500ce84980cf81f),

[ 45](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354) [FUEL\_GAUGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354),

[ 47](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f) [FUEL\_GAUGE\_CHARGE\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f),

[ 49](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984) [FUEL\_GAUGE\_CYCLE\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984),

[ 51](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d) [FUEL\_GAUGE\_CONNECT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d),

[ 53](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c) [FUEL\_GAUGE\_FLAGS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c),

[ 55](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9) [FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9),

[ 57](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b) [FUEL\_GAUGE\_PRESENT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b),

[ 59](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4) [FUEL\_GAUGE\_REMAINING\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4),

[ 61](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd) [FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd),

[ 63](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399) [FUEL\_GAUGE\_RUNTIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399),

[ 65](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd) [FUEL\_GAUGE\_SBS\_MFR\_ACCESS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd),

[ 67](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee) [FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee),

[ 69](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b) [FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b),

[ 71](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009) [FUEL\_GAUGE\_TEMPERATURE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009),

[ 73](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71) [FUEL\_GAUGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71),

[ 75](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae) [FUEL\_GAUGE\_SBS\_MODE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae),

[ 77](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e) [FUEL\_GAUGE\_CHARGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e),

[ 79](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920) [FUEL\_GAUGE\_CHARGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920),

[ 81](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40) [FUEL\_GAUGE\_STATUS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40),

[ 83](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67) [FUEL\_GAUGE\_DESIGN\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67),

[ 85](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf) [FUEL\_GAUGE\_DESIGN\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf),

[ 87](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58) [FUEL\_GAUGE\_SBS\_ATRATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58),

[ 89](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70) [FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70),

[ 91](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0) [FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0),

[ 93](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec) [FUEL\_GAUGE\_SBS\_ATRATE\_OK](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec),

[ 95](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2) [FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2),

[ 97](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a) [FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a),

[ 99](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8) [FUEL\_GAUGE\_MANUFACTURER\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8),

[ 101](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10) [FUEL\_GAUGE\_DEVICE\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10),

[ 103](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9) [FUEL\_GAUGE\_DEVICE\_CHEMISTRY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9),

[ 105](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21) [FUEL\_GAUGE\_CURRENT\_DIRECTION](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21),

[ 107](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae) [FUEL\_GAUGE\_STATE\_OF\_CHARGE\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae),

[ 109](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7) [FUEL\_GAUGE\_LOW\_VOLTAGE\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7),

110

[ 112](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815) [FUEL\_GAUGE\_COMMON\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815),

[ 117](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584) [FUEL\_GAUGE\_CUSTOM\_BEGIN](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584),

118

[ 120](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81) [FUEL\_GAUGE\_PROP\_MAX](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81) = [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602),

121};

122

[ 123](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806);

124

[ 126](unionfuel__gauge__prop__val.md)union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) {

127 /\* Fields have the format: \*/

128 /\* FUEL\_GAUGE\_PROPERTY\_FIELD \*/

129 /\* type property\_field; \*/

130

131 /\* Dynamic Battery Info \*/

[ 133](unionfuel__gauge__prop__val.md#ad96f07db337c038466dd17401c076d38) int [avg\_current](unionfuel__gauge__prop__val.md#ad96f07db337c038466dd17401c076d38);

[ 135](unionfuel__gauge__prop__val.md#ac8e8e74c2b1f2e0c1f4e65eecf5a745a) bool [cutoff](unionfuel__gauge__prop__val.md#ac8e8e74c2b1f2e0c1f4e65eecf5a745a);

[ 137](unionfuel__gauge__prop__val.md#a9bed3247063f069bb92b2902cc5ff468) int [current](unionfuel__gauge__prop__val.md#a9bed3247063f069bb92b2902cc5ff468);

[ 139](unionfuel__gauge__prop__val.md#ac27ae67a315a7204cea6e88962758587) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cycle\_count](unionfuel__gauge__prop__val.md#ac27ae67a315a7204cea6e88962758587);

[ 141](unionfuel__gauge__prop__val.md#a9f4653e270e93280bd6bed6022c135b0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [connect\_state](unionfuel__gauge__prop__val.md#a9f4653e270e93280bd6bed6022c135b0);

[ 143](unionfuel__gauge__prop__val.md#adeb93ed2120e808aac815dcbdf69067f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](unionfuel__gauge__prop__val.md#adeb93ed2120e808aac815dcbdf69067f);

[ 145](unionfuel__gauge__prop__val.md#aa29f7163a1637b6aa8cd6a15dc99d55b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [full\_charge\_capacity](unionfuel__gauge__prop__val.md#aa29f7163a1637b6aa8cd6a15dc99d55b);

[ 147](unionfuel__gauge__prop__val.md#a4916bb50489c5f70335da2f11ed9477e) bool [present\_state](unionfuel__gauge__prop__val.md#a4916bb50489c5f70335da2f11ed9477e);

[ 149](unionfuel__gauge__prop__val.md#adecf57aa90e2b5d483cfd889ec512400) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [remaining\_capacity](unionfuel__gauge__prop__val.md#adecf57aa90e2b5d483cfd889ec512400);

[ 151](unionfuel__gauge__prop__val.md#ae716bdf1346dc7767d98526db6083008) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [runtime\_to\_empty](unionfuel__gauge__prop__val.md#ae716bdf1346dc7767d98526db6083008);

[ 153](unionfuel__gauge__prop__val.md#a2c77e8de7fa40fadfa13dfd4c94df804) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [runtime\_to\_full](unionfuel__gauge__prop__val.md#a2c77e8de7fa40fadfa13dfd4c94df804);

[ 155](unionfuel__gauge__prop__val.md#a957025a2a9fb7709e2bf478f15fd31a0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_mfr\_access\_word](unionfuel__gauge__prop__val.md#a957025a2a9fb7709e2bf478f15fd31a0);

[ 157](unionfuel__gauge__prop__val.md#a33297ff5bf70b510272eddf77ced411e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [absolute\_state\_of\_charge](unionfuel__gauge__prop__val.md#a33297ff5bf70b510272eddf77ced411e);

[ 159](unionfuel__gauge__prop__val.md#a45b20c5118f7ee408d507b94e6cae1dc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [relative\_state\_of\_charge](unionfuel__gauge__prop__val.md#a45b20c5118f7ee408d507b94e6cae1dc);

[ 161](unionfuel__gauge__prop__val.md#a36528b111568bd1c90859e454610fd9f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [temperature](unionfuel__gauge__prop__val.md#a36528b111568bd1c90859e454610fd9f);

[ 163](unionfuel__gauge__prop__val.md#abec5cadefa09e088620a9598dec9c473) int [voltage](unionfuel__gauge__prop__val.md#abec5cadefa09e088620a9598dec9c473);

[ 165](unionfuel__gauge__prop__val.md#a7fc0551e303de56e0eb6bdac1ecaccd0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_mode](unionfuel__gauge__prop__val.md#a7fc0551e303de56e0eb6bdac1ecaccd0);

[ 167](unionfuel__gauge__prop__val.md#a6f74626deef4debbd8dfe6c188984d1b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [chg\_current](unionfuel__gauge__prop__val.md#a6f74626deef4debbd8dfe6c188984d1b);

[ 169](unionfuel__gauge__prop__val.md#a8743f7e7a05919b5469e39527b697e62) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [chg\_voltage](unionfuel__gauge__prop__val.md#a8743f7e7a05919b5469e39527b697e62);

[ 171](unionfuel__gauge__prop__val.md#a65607bb9ba43022c9c566646d4763aac) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fg\_status](unionfuel__gauge__prop__val.md#a65607bb9ba43022c9c566646d4763aac);

[ 173](unionfuel__gauge__prop__val.md#a20aa5736b0ac3c5adda10152660de275) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [design\_cap](unionfuel__gauge__prop__val.md#a20aa5736b0ac3c5adda10152660de275);

[ 175](unionfuel__gauge__prop__val.md#a11626713aef0445ad613a5976401d09e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [design\_volt](unionfuel__gauge__prop__val.md#a11626713aef0445ad613a5976401d09e);

[ 177](unionfuel__gauge__prop__val.md#aa5529fea5cfe765be9b66f5fad96ab2f) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [sbs\_at\_rate](unionfuel__gauge__prop__val.md#aa5529fea5cfe765be9b66f5fad96ab2f);

[ 179](unionfuel__gauge__prop__val.md#aeeeddb48f22b54f90c603d58e9ffa9a5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_at\_rate\_time\_to\_full](unionfuel__gauge__prop__val.md#aeeeddb48f22b54f90c603d58e9ffa9a5);

[ 181](unionfuel__gauge__prop__val.md#a7c8b6f9ee98e5b97ddc85b7e72cea4a8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_at\_rate\_time\_to\_empty](unionfuel__gauge__prop__val.md#a7c8b6f9ee98e5b97ddc85b7e72cea4a8);

[ 183](unionfuel__gauge__prop__val.md#a9b5015878c9a77d9c8330139f94843b7) bool [sbs\_at\_rate\_ok](unionfuel__gauge__prop__val.md#a9b5015878c9a77d9c8330139f94843b7);

[ 185](unionfuel__gauge__prop__val.md#a818ab7faf8f51d4d1a5c5f070d54b997) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_remaining\_capacity\_alarm](unionfuel__gauge__prop__val.md#a818ab7faf8f51d4d1a5c5f070d54b997);

[ 187](unionfuel__gauge__prop__val.md#aa0e46c727bb31acb5d41ce4bc6d5b106) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sbs\_remaining\_time\_alarm](unionfuel__gauge__prop__val.md#aa0e46c727bb31acb5d41ce4bc6d5b106);

[ 189](unionfuel__gauge__prop__val.md#a52b70375d15ed878d62d1390c3144cd8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [current\_direction](unionfuel__gauge__prop__val.md#a52b70375d15ed878d62d1390c3144cd8);

[ 191](unionfuel__gauge__prop__val.md#aa901ef363509234577d73958984862a4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state\_of\_charge\_alarm](unionfuel__gauge__prop__val.md#aa901ef363509234577d73958984862a4);

[ 193](unionfuel__gauge__prop__val.md#aff81db28e93cb70ebea6793e4493915f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [low\_voltage\_alarm](unionfuel__gauge__prop__val.md#aff81db28e93cb70ebea6793e4493915f);

194};

195

[ 199](group__fuel__gauge__interface.md#ga824e00f1d607cdfe2598625f154636f1)#define SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE 20

[ 200](group__fuel__gauge__interface.md#ga41b8379542b9cbd0b3ee9e1bbe4bc599)#define SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE 20

[ 201](group__fuel__gauge__interface.md#gafe9bdc00d856d4cc787265edb7eb0ed2)#define SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE 4

202

[ 203](structsbs__gauge__manufacturer__name.md)struct [sbs\_gauge\_manufacturer\_name](structsbs__gauge__manufacturer__name.md) {

[ 204](structsbs__gauge__manufacturer__name.md#a13a5902df94842f7a69a8028b8708ced) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [manufacturer\_name\_length](structsbs__gauge__manufacturer__name.md#a13a5902df94842f7a69a8028b8708ced);

[ 205](structsbs__gauge__manufacturer__name.md#a40af61fe30263b21e9b9c92383562b0d) char [manufacturer\_name](structsbs__gauge__manufacturer__name.md#a40af61fe30263b21e9b9c92383562b0d)[[SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga824e00f1d607cdfe2598625f154636f1)];

206} \_\_packed;

207

[ 208](structsbs__gauge__device__name.md)struct [sbs\_gauge\_device\_name](structsbs__gauge__device__name.md) {

[ 209](structsbs__gauge__device__name.md#a5e599e923ccbdc7eb89ab6f7e1d3a662) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device\_name\_length](structsbs__gauge__device__name.md#a5e599e923ccbdc7eb89ab6f7e1d3a662);

[ 210](structsbs__gauge__device__name.md#a6699e048a1ca5feb2cadb05169bcfa5f) char [device\_name](structsbs__gauge__device__name.md#a6699e048a1ca5feb2cadb05169bcfa5f)[[SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga41b8379542b9cbd0b3ee9e1bbe4bc599)];

211} \_\_packed;

212

[ 213](structsbs__gauge__device__chemistry.md)struct [sbs\_gauge\_device\_chemistry](structsbs__gauge__device__chemistry.md) {

[ 214](structsbs__gauge__device__chemistry.md#a340cfddcc1ad7a758f75208b38208df4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device\_chemistry\_length](structsbs__gauge__device__chemistry.md#a340cfddcc1ad7a758f75208b38208df4);

[ 215](structsbs__gauge__device__chemistry.md#a2a3990be7618165d88790e53ac7b4e72) char [device\_chemistry](structsbs__gauge__device__chemistry.md#a2a3990be7618165d88790e53ac7b4e72)[[SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE](group__fuel__gauge__interface.md#gafe9bdc00d856d4cc787265edb7eb0ed2)];

216} \_\_packed;

217

[ 224](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568)typedef int (\*[fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568))(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

225 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val);

226

[ 233](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9)typedef int (\*[fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9))(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

234 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val);

235

[ 242](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)typedef int (\*[fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69))(const struct [device](structdevice.md) \*dev,

243 [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop\_type, void \*dst,

244 size\_t dst\_len);

245

[ 252](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7)typedef int (\*[fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7))(const struct [device](structdevice.md) \*dev);

253

254/\* Caching is entirely on the onus of the client \*/

255

[ 256](structfuel__gauge__driver__api.md)\_\_subsystem struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) {

[ 263](structfuel__gauge__driver__api.md#ab729a85c69e561f1ca0aca9f8eb22d91) [fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568) [get\_property](structfuel__gauge__driver__api.md#ab729a85c69e561f1ca0aca9f8eb22d91);

[ 264](structfuel__gauge__driver__api.md#a74815d3bb721452bfd3e35cd1221b223) [fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9) [set\_property](structfuel__gauge__driver__api.md#a74815d3bb721452bfd3e35cd1221b223);

[ 265](structfuel__gauge__driver__api.md#ad12c13461173177d1c81846a85a3f570) [fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69) [get\_buffer\_property](structfuel__gauge__driver__api.md#ad12c13461173177d1c81846a85a3f570);

[ 266](structfuel__gauge__driver__api.md#a406816c19022eea26f0fd61fb21d234c) [fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7) [battery\_cutoff](structfuel__gauge__driver__api.md#a406816c19022eea26f0fd61fb21d234c);

267};

268

[ 278](group__fuel__gauge__interface.md#gab84999beab9a43241992945a3b2d37e1)\_\_syscall int [fuel\_gauge\_get\_prop](group__fuel__gauge__interface.md#gab84999beab9a43241992945a3b2d37e1)(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

279 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val);

280

281static inline int z\_impl\_fuel\_gauge\_get\_prop(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

282 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val)

283{

284 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = (const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

285

286 if (api->get\_property == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

287 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

288 }

289

290 return api->get\_property(dev, prop, val);

291}

292

307

[ 308](group__fuel__gauge__interface.md#gaf8a1fed5f6af9c25a12130c481411603)\_\_syscall int [fuel\_gauge\_get\_props](group__fuel__gauge__interface.md#gaf8a1fed5f6af9c25a12130c481411603)(const struct [device](structdevice.md) \*dev, const [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props,

309 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, size\_t len);

310static inline int z\_impl\_fuel\_gauge\_get\_props(const struct [device](structdevice.md) \*dev,

311 const [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props,

312 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, size\_t len)

313{

314 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = (const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

315

316 for (size\_t i = 0; i < len; i++) {

317 int ret = api->get\_property(dev, props[i], vals + i);

318

319 if (ret) {

320 return ret;

321 }

322 }

323

324 return 0;

325}

326

[ 336](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d)\_\_syscall int [fuel\_gauge\_set\_prop](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d)(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

337 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val);

338

339static inline int z\_impl\_fuel\_gauge\_set\_prop(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop,

340 union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val)

341{

342 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = (const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

343

344 if (api->set\_property == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

345 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

346 }

347

348 return api->set\_property(dev, prop, val);

349}

[ 362](group__fuel__gauge__interface.md#gac8efb10ccb6f510dc92618e218c1df9b)\_\_syscall int [fuel\_gauge\_set\_props](group__fuel__gauge__interface.md#gac8efb10ccb6f510dc92618e218c1df9b)(const struct [device](structdevice.md) \*dev, const [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props,

363 const union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, size\_t len);

364

365static inline int z\_impl\_fuel\_gauge\_set\_props(const struct [device](structdevice.md) \*dev,

366 const [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props,

367 const union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, size\_t len)

368{

369 for (size\_t i = 0; i < len; i++) {

370 int ret = [fuel\_gauge\_set\_prop](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d)(dev, props[i], vals[i]);

371

372 if (ret) {

373 return ret;

374 }

375 }

376

377 return 0;

378}

379

390

[ 391](group__fuel__gauge__interface.md#ga7e6cb77d2d4dd7a0feb25c92d031614c)\_\_syscall int [fuel\_gauge\_get\_buffer\_prop](group__fuel__gauge__interface.md#ga7e6cb77d2d4dd7a0feb25c92d031614c)(const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop\_type,

392 void \*dst, size\_t dst\_len);

393

394static inline int z\_impl\_fuel\_gauge\_get\_buffer\_prop(const struct [device](structdevice.md) \*dev,

395 [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop\_type, void \*dst,

396 size\_t dst\_len)

397{

398 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = (const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

399

400 if (api->get\_buffer\_property == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

401 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

402 }

403

404 return api->get\_buffer\_property(dev, prop\_type, dst, dst\_len);

405}

406

[ 415](group__fuel__gauge__interface.md#ga763a40688dc8fc6a0ba85fdc79178ebc)\_\_syscall int [fuel\_gauge\_battery\_cutoff](group__fuel__gauge__interface.md#ga763a40688dc8fc6a0ba85fdc79178ebc)(const struct [device](structdevice.md) \*dev);

416

417static inline int z\_impl\_fuel\_gauge\_battery\_cutoff(const struct [device](structdevice.md) \*dev)

418{

419 const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*api = (const struct [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

420

421 if (api->battery\_cutoff == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

422 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

423 }

424

425 return api->battery\_cutoff(dev);

426}

427

431

432#ifdef \_\_cplusplus

433}

434#endif /\* \_\_cplusplus \*/

435

436#include <zephyr/syscalls/fuel\_gauge.h>

437

438#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_BATTERY\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga41b8379542b9cbd0b3ee9e1bbe4bc599)

#define SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE

**Definition** fuel\_gauge.h:200

[fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806)

uint16\_t fuel\_gauge\_prop\_t

**Definition** fuel\_gauge.h:123

[fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7)

int(\* fuel\_gauge\_battery\_cutoff\_t)(const struct device \*dev)

Callback API for doing a battery cutoff.

**Definition** fuel\_gauge.h:252

[fuel\_gauge\_battery\_cutoff](group__fuel__gauge__interface.md#ga763a40688dc8fc6a0ba85fdc79178ebc)

int fuel\_gauge\_battery\_cutoff(const struct device \*dev)

Have fuel gauge cutoff its associated battery.

[fuel\_gauge\_get\_buffer\_prop](group__fuel__gauge__interface.md#ga7e6cb77d2d4dd7a0feb25c92d031614c)

int fuel\_gauge\_get\_buffer\_prop(const struct device \*dev, fuel\_gauge\_prop\_t prop\_type, void \*dst, size\_t dst\_len)

Fetch a battery fuel-gauge buffer property.

[SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga824e00f1d607cdfe2598625f154636f1)

#define SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE

Data structures for reading SBS buffer properties.

**Definition** fuel\_gauge.h:199

[fuel\_gauge\_set\_prop](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d)

int fuel\_gauge\_set\_prop(const struct device \*dev, fuel\_gauge\_prop\_t prop, union fuel\_gauge\_prop\_val val)

Set a battery fuel-gauge property.

[fuel\_gauge\_get\_prop](group__fuel__gauge__interface.md#gab84999beab9a43241992945a3b2d37e1)

int fuel\_gauge\_get\_prop(const struct device \*dev, fuel\_gauge\_prop\_t prop, union fuel\_gauge\_prop\_val \*val)

Fetch a battery fuel-gauge property.

[fuel\_gauge\_set\_props](group__fuel__gauge__interface.md#gac8efb10ccb6f510dc92618e218c1df9b)

int fuel\_gauge\_set\_props(const struct device \*dev, const fuel\_gauge\_prop\_t \*props, const union fuel\_gauge\_prop\_val \*vals, size\_t len)

Set a battery fuel-gauge property.

[fuel\_gauge\_prop\_type](group__fuel__gauge__interface.md#gae49908857800bdd010d59895cfad9171)

fuel\_gauge\_prop\_type

**Definition** fuel\_gauge.h:32

[fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9)

int(\* fuel\_gauge\_set\_property\_t)(const struct device \*dev, fuel\_gauge\_prop\_t prop, union fuel\_gauge\_prop\_val val)

Callback API for setting a fuel\_gauge property.

**Definition** fuel\_gauge.h:233

[fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568)

int(\* fuel\_gauge\_get\_property\_t)(const struct device \*dev, fuel\_gauge\_prop\_t prop, union fuel\_gauge\_prop\_val \*val)

Callback API for getting a fuel\_gauge property.

**Definition** fuel\_gauge.h:224

[fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)

int(\* fuel\_gauge\_get\_buffer\_property\_t)(const struct device \*dev, fuel\_gauge\_prop\_t prop\_type, void \*dst, size\_t dst\_len)

Callback API for getting a fuel\_gauge buffer property.

**Definition** fuel\_gauge.h:242

[fuel\_gauge\_get\_props](group__fuel__gauge__interface.md#gaf8a1fed5f6af9c25a12130c481411603)

int fuel\_gauge\_get\_props(const struct device \*dev, const fuel\_gauge\_prop\_t \*props, union fuel\_gauge\_prop\_val \*vals, size\_t len)

Fetch multiple battery fuel-gauge properties.

[SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE](group__fuel__gauge__interface.md#gafe9bdc00d856d4cc787265edb7eb0ed2)

#define SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE

**Definition** fuel\_gauge.h:201

[FUEL\_GAUGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354)

@ FUEL\_GAUGE\_CURRENT

Battery current (uA); negative=discharging.

**Definition** fuel\_gauge.h:45

[FUEL\_GAUGE\_STATUS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40)

@ FUEL\_GAUGE\_STATUS

Alarm, Status and Error codes (flags).

**Definition** fuel\_gauge.h:81

[FUEL\_GAUGE\_SBS\_MFR\_ACCESS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd)

@ FUEL\_GAUGE\_SBS\_MFR\_ACCESS

Retrieve word from SBS1.1 ManufactuerAccess.

**Definition** fuel\_gauge.h:65

[FUEL\_GAUGE\_CONNECT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d)

@ FUEL\_GAUGE\_CONNECT\_STATE

Connect state of battery.

**Definition** fuel\_gauge.h:51

[FUEL\_GAUGE\_FLAGS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c)

@ FUEL\_GAUGE\_FLAGS

General Error/Runtime Flags.

**Definition** fuel\_gauge.h:53

[FUEL\_GAUGE\_CYCLE\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984)

@ FUEL\_GAUGE\_CYCLE\_COUNT

Cycle count in 1/100ths (number of charge/discharge cycles).

**Definition** fuel\_gauge.h:49

[FUEL\_GAUGE\_COMMON\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815)

@ FUEL\_GAUGE\_COMMON\_COUNT

Reserved to demark end of common fuel gauge properties.

**Definition** fuel\_gauge.h:112

[FUEL\_GAUGE\_MANUFACTURER\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8)

@ FUEL\_GAUGE\_MANUFACTURER\_NAME

Manufacturer of pack (1 byte length + 20 bytes data).

**Definition** fuel\_gauge.h:99

[FUEL\_GAUGE\_SBS\_MODE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae)

@ FUEL\_GAUGE\_SBS\_MODE

Battery Mode (flags).

**Definition** fuel\_gauge.h:75

[FUEL\_GAUGE\_SBS\_ATRATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58)

@ FUEL\_GAUGE\_SBS\_ATRATE

AtRate (mA or 10 mW).

**Definition** fuel\_gauge.h:87

[FUEL\_GAUGE\_DESIGN\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf)

@ FUEL\_GAUGE\_DESIGN\_VOLTAGE

Design Voltage (mV).

**Definition** fuel\_gauge.h:85

[FUEL\_GAUGE\_AVG\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396)

@ FUEL\_GAUGE\_AVG\_CURRENT

Runtime Dynamic Battery Parameters.

**Definition** fuel\_gauge.h:40

[FUEL\_GAUGE\_RUNTIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399)

@ FUEL\_GAUGE\_RUNTIME\_TO\_FULL

Remaining time in minutes until battery reaches full charge.

**Definition** fuel\_gauge.h:63

[FUEL\_GAUGE\_CHARGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e)

@ FUEL\_GAUGE\_CHARGE\_CURRENT

Battery desired Max Charging Current (uA).

**Definition** fuel\_gauge.h:77

[FUEL\_GAUGE\_CUSTOM\_BEGIN](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584)

@ FUEL\_GAUGE\_CUSTOM\_BEGIN

Reserved to demark downstream custom properties - use this value as the actual value may change over ...

**Definition** fuel\_gauge.h:117

[FUEL\_GAUGE\_DEVICE\_CHEMISTRY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9)

@ FUEL\_GAUGE\_DEVICE\_CHEMISTRY

Chemistry (1 byte length + 4 bytes data).

**Definition** fuel\_gauge.h:103

[FUEL\_GAUGE\_PROP\_MAX](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81)

@ FUEL\_GAUGE\_PROP\_MAX

Reserved to demark end of valid enum properties.

**Definition** fuel\_gauge.h:120

[FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0)

@ FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY

AtRateTimeToEmpty (minutes).

**Definition** fuel\_gauge.h:91

[FUEL\_GAUGE\_DESIGN\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67)

@ FUEL\_GAUGE\_DESIGN\_CAPACITY

Design Capacity (mAh or 10mWh).

**Definition** fuel\_gauge.h:83

[FUEL\_GAUGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71)

@ FUEL\_GAUGE\_VOLTAGE

Battery voltage (uV).

**Definition** fuel\_gauge.h:73

[FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a)

@ FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM

Remaining Time Alarm (minutes).

**Definition** fuel\_gauge.h:97

[FUEL\_GAUGE\_CHARGE\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f)

@ FUEL\_GAUGE\_CHARGE\_CUTOFF

Whether the battery underlying the fuel-gauge is cut off from charge.

**Definition** fuel\_gauge.h:47

[FUEL\_GAUGE\_CHARGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920)

@ FUEL\_GAUGE\_CHARGE\_VOLTAGE

Battery desired Max Charging Voltage (uV).

**Definition** fuel\_gauge.h:79

[FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee)

@ FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE

Absolute state of charge (percent, 0-100) - expressed as % of design capacity.

**Definition** fuel\_gauge.h:67

[FUEL\_GAUGE\_DEVICE\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10)

@ FUEL\_GAUGE\_DEVICE\_NAME

Name of pack (1 byte length + 20 bytes data).

**Definition** fuel\_gauge.h:101

[FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70)

@ FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL

AtRateTimeToFull (minutes).

**Definition** fuel\_gauge.h:89

[FUEL\_GAUGE\_STATE\_OF\_CHARGE\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae)

@ FUEL\_GAUGE\_STATE\_OF\_CHARGE\_ALARM

Remaining state of charge alarm (percent, 0-100).

**Definition** fuel\_gauge.h:107

[FUEL\_GAUGE\_TEMPERATURE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009)

@ FUEL\_GAUGE\_TEMPERATURE

Temperature in 0.1 K.

**Definition** fuel\_gauge.h:71

[FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9)

@ FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY

Full Charge Capacity in uAh (might change in some implementations to determine wear).

**Definition** fuel\_gauge.h:55

[FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd)

@ FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY

Remaining battery life time in minutes.

**Definition** fuel\_gauge.h:61

[FUEL\_GAUGE\_PRESENT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b)

@ FUEL\_GAUGE\_PRESENT\_STATE

Is the battery physically present.

**Definition** fuel\_gauge.h:57

[FUEL\_GAUGE\_REMAINING\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4)

@ FUEL\_GAUGE\_REMAINING\_CAPACITY

Remaining capacity in uAh.

**Definition** fuel\_gauge.h:59

[FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2)

@ FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM

Remaining Capacity Alarm (mAh or 10mWh).

**Definition** fuel\_gauge.h:95

[FUEL\_GAUGE\_LOW\_VOLTAGE\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7)

@ FUEL\_GAUGE\_LOW\_VOLTAGE\_ALARM

Low Cell Voltage Alarm (uV).

**Definition** fuel\_gauge.h:109

[FUEL\_GAUGE\_BATTERY\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad431ab05b79f942dd500ce84980cf81f)

@ FUEL\_GAUGE\_BATTERY\_CUTOFF

Used to cutoff the battery from the system - useful for storage/shipping of devices.

**Definition** fuel\_gauge.h:43

[FUEL\_GAUGE\_CURRENT\_DIRECTION](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21)

@ FUEL\_GAUGE\_CURRENT\_DIRECTION

Battery current direction (flags).

**Definition** fuel\_gauge.h:105

[FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b)

@ FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE

Relative state of charge (percent, 0-100) - expressed as % of full charge capacity.

**Definition** fuel\_gauge.h:69

[FUEL\_GAUGE\_SBS\_ATRATE\_OK](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec)

@ FUEL\_GAUGE\_SBS\_ATRATE\_OK

AtRateOK (boolean).

**Definition** fuel\_gauge.h:93

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602)

#define UINT16\_MAX

**Definition** stdint.h:28

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md)

**Definition** fuel\_gauge.h:256

[fuel\_gauge\_driver\_api::battery\_cutoff](structfuel__gauge__driver__api.md#a406816c19022eea26f0fd61fb21d234c)

fuel\_gauge\_battery\_cutoff\_t battery\_cutoff

**Definition** fuel\_gauge.h:266

[fuel\_gauge\_driver\_api::set\_property](structfuel__gauge__driver__api.md#a74815d3bb721452bfd3e35cd1221b223)

fuel\_gauge\_set\_property\_t set\_property

**Definition** fuel\_gauge.h:264

[fuel\_gauge\_driver\_api::get\_property](structfuel__gauge__driver__api.md#ab729a85c69e561f1ca0aca9f8eb22d91)

fuel\_gauge\_get\_property\_t get\_property

Note: Historically this API allowed drivers to implement a custom multi-get/set property function,...

**Definition** fuel\_gauge.h:263

[fuel\_gauge\_driver\_api::get\_buffer\_property](structfuel__gauge__driver__api.md#ad12c13461173177d1c81846a85a3f570)

fuel\_gauge\_get\_buffer\_property\_t get\_buffer\_property

**Definition** fuel\_gauge.h:265

[sbs\_gauge\_device\_chemistry](structsbs__gauge__device__chemistry.md)

**Definition** fuel\_gauge.h:213

[sbs\_gauge\_device\_chemistry::device\_chemistry](structsbs__gauge__device__chemistry.md#a2a3990be7618165d88790e53ac7b4e72)

char device\_chemistry[4]

**Definition** fuel\_gauge.h:215

[sbs\_gauge\_device\_chemistry::device\_chemistry\_length](structsbs__gauge__device__chemistry.md#a340cfddcc1ad7a758f75208b38208df4)

uint8\_t device\_chemistry\_length

**Definition** fuel\_gauge.h:214

[sbs\_gauge\_device\_name](structsbs__gauge__device__name.md)

**Definition** fuel\_gauge.h:208

[sbs\_gauge\_device\_name::device\_name\_length](structsbs__gauge__device__name.md#a5e599e923ccbdc7eb89ab6f7e1d3a662)

uint8\_t device\_name\_length

**Definition** fuel\_gauge.h:209

[sbs\_gauge\_device\_name::device\_name](structsbs__gauge__device__name.md#a6699e048a1ca5feb2cadb05169bcfa5f)

char device\_name[20]

**Definition** fuel\_gauge.h:210

[sbs\_gauge\_manufacturer\_name](structsbs__gauge__manufacturer__name.md)

**Definition** fuel\_gauge.h:203

[sbs\_gauge\_manufacturer\_name::manufacturer\_name\_length](structsbs__gauge__manufacturer__name.md#a13a5902df94842f7a69a8028b8708ced)

uint8\_t manufacturer\_name\_length

**Definition** fuel\_gauge.h:204

[sbs\_gauge\_manufacturer\_name::manufacturer\_name](structsbs__gauge__manufacturer__name.md#a40af61fe30263b21e9b9c92383562b0d)

char manufacturer\_name[20]

**Definition** fuel\_gauge.h:205

[fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md)

Property field to value/type union.

**Definition** fuel\_gauge.h:126

[fuel\_gauge\_prop\_val::design\_volt](unionfuel__gauge__prop__val.md#a11626713aef0445ad613a5976401d09e)

uint16\_t design\_volt

FUEL\_GAUGE\_DESIGN\_VOLTAGE.

**Definition** fuel\_gauge.h:175

[fuel\_gauge\_prop\_val::design\_cap](unionfuel__gauge__prop__val.md#a20aa5736b0ac3c5adda10152660de275)

uint16\_t design\_cap

FUEL\_GAUGE\_DESIGN\_CAPACITY.

**Definition** fuel\_gauge.h:173

[fuel\_gauge\_prop\_val::runtime\_to\_full](unionfuel__gauge__prop__val.md#a2c77e8de7fa40fadfa13dfd4c94df804)

uint32\_t runtime\_to\_full

FUEL\_GAUGE\_RUNTIME\_TO\_FULL.

**Definition** fuel\_gauge.h:153

[fuel\_gauge\_prop\_val::absolute\_state\_of\_charge](unionfuel__gauge__prop__val.md#a33297ff5bf70b510272eddf77ced411e)

uint8\_t absolute\_state\_of\_charge

FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE.

**Definition** fuel\_gauge.h:157

[fuel\_gauge\_prop\_val::temperature](unionfuel__gauge__prop__val.md#a36528b111568bd1c90859e454610fd9f)

uint16\_t temperature

FUEL\_GAUGE\_TEMPERATURE.

**Definition** fuel\_gauge.h:161

[fuel\_gauge\_prop\_val::relative\_state\_of\_charge](unionfuel__gauge__prop__val.md#a45b20c5118f7ee408d507b94e6cae1dc)

uint8\_t relative\_state\_of\_charge

FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE.

**Definition** fuel\_gauge.h:159

[fuel\_gauge\_prop\_val::present\_state](unionfuel__gauge__prop__val.md#a4916bb50489c5f70335da2f11ed9477e)

bool present\_state

FUEL\_GAUGE\_PRESENT\_STATE.

**Definition** fuel\_gauge.h:147

[fuel\_gauge\_prop\_val::current\_direction](unionfuel__gauge__prop__val.md#a52b70375d15ed878d62d1390c3144cd8)

uint16\_t current\_direction

FUEL\_GAUGE\_CURRENT\_DIRECTION.

**Definition** fuel\_gauge.h:189

[fuel\_gauge\_prop\_val::fg\_status](unionfuel__gauge__prop__val.md#a65607bb9ba43022c9c566646d4763aac)

uint16\_t fg\_status

FUEL\_GAUGE\_STATUS.

**Definition** fuel\_gauge.h:171

[fuel\_gauge\_prop\_val::chg\_current](unionfuel__gauge__prop__val.md#a6f74626deef4debbd8dfe6c188984d1b)

uint32\_t chg\_current

FUEL\_GAUGE\_CHARGE\_CURRENT.

**Definition** fuel\_gauge.h:167

[fuel\_gauge\_prop\_val::sbs\_at\_rate\_time\_to\_empty](unionfuel__gauge__prop__val.md#a7c8b6f9ee98e5b97ddc85b7e72cea4a8)

uint16\_t sbs\_at\_rate\_time\_to\_empty

FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY.

**Definition** fuel\_gauge.h:181

[fuel\_gauge\_prop\_val::sbs\_mode](unionfuel__gauge__prop__val.md#a7fc0551e303de56e0eb6bdac1ecaccd0)

uint16\_t sbs\_mode

FUEL\_GAUGE\_SBS\_MODE.

**Definition** fuel\_gauge.h:165

[fuel\_gauge\_prop\_val::sbs\_remaining\_capacity\_alarm](unionfuel__gauge__prop__val.md#a818ab7faf8f51d4d1a5c5f070d54b997)

uint16\_t sbs\_remaining\_capacity\_alarm

FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM.

**Definition** fuel\_gauge.h:185

[fuel\_gauge\_prop\_val::chg\_voltage](unionfuel__gauge__prop__val.md#a8743f7e7a05919b5469e39527b697e62)

uint32\_t chg\_voltage

FUEL\_GAUGE\_CHARGE\_VOLTAGE.

**Definition** fuel\_gauge.h:169

[fuel\_gauge\_prop\_val::sbs\_mfr\_access\_word](unionfuel__gauge__prop__val.md#a957025a2a9fb7709e2bf478f15fd31a0)

uint16\_t sbs\_mfr\_access\_word

FUEL\_GAUGE\_SBS\_MFR\_ACCESS.

**Definition** fuel\_gauge.h:155

[fuel\_gauge\_prop\_val::sbs\_at\_rate\_ok](unionfuel__gauge__prop__val.md#a9b5015878c9a77d9c8330139f94843b7)

bool sbs\_at\_rate\_ok

FUEL\_GAUGE\_SBS\_ATRATE\_OK.

**Definition** fuel\_gauge.h:183

[fuel\_gauge\_prop\_val::current](unionfuel__gauge__prop__val.md#a9bed3247063f069bb92b2902cc5ff468)

int current

FUEL\_GAUGE\_CURRENT.

**Definition** fuel\_gauge.h:137

[fuel\_gauge\_prop\_val::connect\_state](unionfuel__gauge__prop__val.md#a9f4653e270e93280bd6bed6022c135b0)

uint32\_t connect\_state

FUEL\_GAUGE\_CONNECT\_STATE.

**Definition** fuel\_gauge.h:141

[fuel\_gauge\_prop\_val::sbs\_remaining\_time\_alarm](unionfuel__gauge__prop__val.md#aa0e46c727bb31acb5d41ce4bc6d5b106)

uint16\_t sbs\_remaining\_time\_alarm

FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM.

**Definition** fuel\_gauge.h:187

[fuel\_gauge\_prop\_val::full\_charge\_capacity](unionfuel__gauge__prop__val.md#aa29f7163a1637b6aa8cd6a15dc99d55b)

uint32\_t full\_charge\_capacity

FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY.

**Definition** fuel\_gauge.h:145

[fuel\_gauge\_prop\_val::sbs\_at\_rate](unionfuel__gauge__prop__val.md#aa5529fea5cfe765be9b66f5fad96ab2f)

int16\_t sbs\_at\_rate

FUEL\_GAUGE\_SBS\_ATRATE.

**Definition** fuel\_gauge.h:177

[fuel\_gauge\_prop\_val::state\_of\_charge\_alarm](unionfuel__gauge__prop__val.md#aa901ef363509234577d73958984862a4)

uint8\_t state\_of\_charge\_alarm

FUEL\_GAUGE\_STATE\_OF\_CHARGE\_ALARM.

**Definition** fuel\_gauge.h:191

[fuel\_gauge\_prop\_val::voltage](unionfuel__gauge__prop__val.md#abec5cadefa09e088620a9598dec9c473)

int voltage

FUEL\_GAUGE\_VOLTAGE.

**Definition** fuel\_gauge.h:163

[fuel\_gauge\_prop\_val::cycle\_count](unionfuel__gauge__prop__val.md#ac27ae67a315a7204cea6e88962758587)

uint32\_t cycle\_count

FUEL\_GAUGE\_CYCLE\_COUNT.

**Definition** fuel\_gauge.h:139

[fuel\_gauge\_prop\_val::cutoff](unionfuel__gauge__prop__val.md#ac8e8e74c2b1f2e0c1f4e65eecf5a745a)

bool cutoff

FUEL\_GAUGE\_CHARGE\_CUTOFF.

**Definition** fuel\_gauge.h:135

[fuel\_gauge\_prop\_val::avg\_current](unionfuel__gauge__prop__val.md#ad96f07db337c038466dd17401c076d38)

int avg\_current

FUEL\_GAUGE\_AVG\_CURRENT.

**Definition** fuel\_gauge.h:133

[fuel\_gauge\_prop\_val::flags](unionfuel__gauge__prop__val.md#adeb93ed2120e808aac815dcbdf69067f)

uint32\_t flags

FUEL\_GAUGE\_FLAGS.

**Definition** fuel\_gauge.h:143

[fuel\_gauge\_prop\_val::remaining\_capacity](unionfuel__gauge__prop__val.md#adecf57aa90e2b5d483cfd889ec512400)

uint32\_t remaining\_capacity

FUEL\_GAUGE\_REMAINING\_CAPACITY.

**Definition** fuel\_gauge.h:149

[fuel\_gauge\_prop\_val::runtime\_to\_empty](unionfuel__gauge__prop__val.md#ae716bdf1346dc7767d98526db6083008)

uint32\_t runtime\_to\_empty

FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY.

**Definition** fuel\_gauge.h:151

[fuel\_gauge\_prop\_val::sbs\_at\_rate\_time\_to\_full](unionfuel__gauge__prop__val.md#aeeeddb48f22b54f90c603d58e9ffa9a5)

uint16\_t sbs\_at\_rate\_time\_to\_full

FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL.

**Definition** fuel\_gauge.h:179

[fuel\_gauge\_prop\_val::low\_voltage\_alarm](unionfuel__gauge__prop__val.md#aff81db28e93cb70ebea6793e4493915f)

uint32\_t low\_voltage\_alarm

FUEL\_GAUGE\_LOW\_VOLTAGE\_ALARM.

**Definition** fuel\_gauge.h:193

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [fuel\_gauge.h](fuel__gauge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
