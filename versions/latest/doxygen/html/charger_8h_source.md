---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/charger_8h_source.html
original_path: doxygen/html/charger_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

charger.h

[Go to the documentation of this file.](charger_8h.md)

1/\*

2 \* Copyright 2023 Cirrus Logic, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CHARGER\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_CHARGER\_H\_

14

21

22#include <[stdbool.h](stdbool_8h.md)>

23#include <stddef.h>

24#include <[stdint.h](stdint_8h.md)>

25

26#include <[zephyr/device.h](device_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif /\* \_\_cplusplus \*/

31

[ 35](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7)enum [charger\_property](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7) {

[ 38](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526) [CHARGER\_PROP\_ONLINE](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526) = 0,

[ 41](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b) [CHARGER\_PROP\_PRESENT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b),

[ 44](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6) [CHARGER\_PROP\_STATUS](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6),

[ 47](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95) [CHARGER\_PROP\_CHARGE\_TYPE](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95),

[ 50](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654) [CHARGER\_PROP\_HEALTH](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654),

[ 52](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306) [CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306),

[ 54](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9) [CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9),

[ 56](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc) [CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc),

[ 58](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf) [CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf),

[ 65](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085) [CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085),

[ 72](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0) [CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0),

[ 79](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe) [CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe),

[ 81](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732) [CHARGER\_PROP\_COMMON\_COUNT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732),

[ 86](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3) [CHARGER\_PROP\_CUSTOM\_BEGIN](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3) = [CHARGER\_PROP\_COMMON\_COUNT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732) + 1,

[ 88](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e) [CHARGER\_PROP\_MAX](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e) = [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602),

89};

90

[ 97](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635);

98

[ 102](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19)enum [charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) {

[ 104](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3) [CHARGER\_ONLINE\_OFFLINE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3) = 0,

[ 106](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6) [CHARGER\_ONLINE\_FIXED](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6),

[ 108](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e) [CHARGER\_ONLINE\_PROGRAMMABLE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e),

109};

110

[ 114](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7)enum [charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) {

[ 116](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5) [CHARGER\_STATUS\_UNKNOWN](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5) = 0,

[ 118](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad) [CHARGER\_STATUS\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad),

[ 120](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e) [CHARGER\_STATUS\_DISCHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e),

[ 122](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658) [CHARGER\_STATUS\_NOT\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658),

[ 124](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf) [CHARGER\_STATUS\_FULL](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf),

125};

126

[ 130](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803)enum [charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803) {

[ 132](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4) [CHARGER\_CHARGE\_TYPE\_UNKNOWN](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4) = 0,

[ 134](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17) [CHARGER\_CHARGE\_TYPE\_NONE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17),

[ 139](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8) [CHARGER\_CHARGE\_TYPE\_TRICKLE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8),

[ 141](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711) [CHARGER\_CHARGE\_TYPE\_FAST](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711),

[ 143](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6) [CHARGER\_CHARGE\_TYPE\_STANDARD](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6),

144 /\*

145 \* Charging is being dynamically adjusted by the charger device

146 \*/

[ 147](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2) [CHARGER\_CHARGE\_TYPE\_ADAPTIVE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2),

148 /\*

149 \* Charging is occurring at a reduced charge rate to preserve

150 \* battery health

151 \*/

[ 152](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f) [CHARGER\_CHARGE\_TYPE\_LONGLIFE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f),

153 /\*

154 \* The charger device is being bypassed and the power conversion

155 \* is being handled externally, typically by a "smart" wall adaptor

156 \*/

[ 157](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8) [CHARGER\_CHARGE\_TYPE\_BYPASS](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8),

158};

159

[ 165](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412)enum [charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412) {

[ 167](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad) [CHARGER\_HEALTH\_UNKNOWN](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad) = 0,

[ 169](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538) [CHARGER\_HEALTH\_GOOD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538),

[ 171](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b) [CHARGER\_HEALTH\_OVERHEAT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b),

[ 173](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459) [CHARGER\_HEALTH\_OVERVOLTAGE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459),

[ 178](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa) [CHARGER\_HEALTH\_UNSPEC\_FAILURE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa),

[ 180](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967) [CHARGER\_HEALTH\_COLD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967),

[ 182](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce) [CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce),

[ 184](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82) [CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82),

[ 186](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1) [CHARGER\_HEALTH\_CALIBRATION\_REQUIRED](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1),

[ 188](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f) [CHARGER\_HEALTH\_WARM](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f),

[ 190](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3) [CHARGER\_HEALTH\_COOL](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3),

[ 192](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1) [CHARGER\_HEALTH\_HOT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1),

[ 194](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b) [CHARGER\_HEALTH\_NO\_BATTERY](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b),

195};

196

[ 200](group__charger__interface.md#ga2e7d7f15725db4d502bc3f46476a310d)enum [charger\_notification\_severity](group__charger__interface.md#ga2e7d7f15725db4d502bc3f46476a310d) {

[ 202](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b) [CHARGER\_SEVERITY\_PEAK](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b) = 0,

[ 204](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8) [CHARGER\_SEVERITY\_CRITICAL](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8),

[ 206](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885) [CHARGER\_SEVERITY\_WARNING](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885),

207};

208

[ 212](structcharger__current__notifier.md)struct [charger\_current\_notifier](structcharger__current__notifier.md) {

[ 214](structcharger__current__notifier.md#a22c26477263e5abedb200de36a29d9de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [severity](structcharger__current__notifier.md#a22c26477263e5abedb200de36a29d9de);

[ 216](structcharger__current__notifier.md#acb54706bf47f55e197e799393b9eb87e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [current\_ua](structcharger__current__notifier.md#acb54706bf47f55e197e799393b9eb87e);

[ 218](structcharger__current__notifier.md#a4998999ef893d18fa64b86ec4fd9ad94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [duration\_us](structcharger__current__notifier.md#a4998999ef893d18fa64b86ec4fd9ad94);

219};

220

[ 225](unioncharger__propval.md)union [charger\_propval](unioncharger__propval.md) {

226 /\* Fields have the format: \*/

227 /\* CHARGER\_PROPERTY\_FIELD \*/

228 /\* type property\_field; \*/

229

[ 231](unioncharger__propval.md#a8589124e6152b70b649788a8b94461ab) enum [charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) [online](unioncharger__propval.md#a8589124e6152b70b649788a8b94461ab);

[ 233](unioncharger__propval.md#ab0eec508b90d205a1662fd6c69638764) bool [present](unioncharger__propval.md#ab0eec508b90d205a1662fd6c69638764);

[ 235](unioncharger__propval.md#a7f4976d72d4a7d48385ceb9f18c510b5) enum [charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) [status](unioncharger__propval.md#a7f4976d72d4a7d48385ceb9f18c510b5);

[ 237](unioncharger__propval.md#ac1a594de2b1c10d28b6a81dd66f1a6ba) enum [charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803) [charge\_type](unioncharger__propval.md#ac1a594de2b1c10d28b6a81dd66f1a6ba);

[ 239](unioncharger__propval.md#abd990f67423424da60856f4b6e8824a3) enum [charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412) [health](unioncharger__propval.md#abd990f67423424da60856f4b6e8824a3);

[ 241](unioncharger__propval.md#af4e383bb797432033050937740ce0ac3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [const\_charge\_current\_ua](unioncharger__propval.md#af4e383bb797432033050937740ce0ac3);

[ 243](unioncharger__propval.md#a24a97e16505fa336bd3a68743d05936b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [precharge\_current\_ua](unioncharger__propval.md#a24a97e16505fa336bd3a68743d05936b);

[ 245](unioncharger__propval.md#a89d0c93d68650cefe29e891f4db928f4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [charge\_term\_current\_ua](unioncharger__propval.md#a89d0c93d68650cefe29e891f4db928f4);

[ 247](unioncharger__propval.md#a733bae9ce0bf7e902f8af307f94a356c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [const\_charge\_voltage\_uv](unioncharger__propval.md#a733bae9ce0bf7e902f8af307f94a356c);

[ 249](unioncharger__propval.md#ae51670de8fa560f0c7610452db029bc2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [input\_current\_regulation\_current\_ua](unioncharger__propval.md#ae51670de8fa560f0c7610452db029bc2);

[ 251](unioncharger__propval.md#afbe7b5fe1e421fb97b37d71ce14dc51a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [input\_voltage\_regulation\_voltage\_uv](unioncharger__propval.md#afbe7b5fe1e421fb97b37d71ce14dc51a);

[ 253](unioncharger__propval.md#a0ad956ab4d0b306f94cce2aa81283a35) struct [charger\_current\_notifier](structcharger__current__notifier.md) [input\_current\_notification](unioncharger__propval.md#a0ad956ab4d0b306f94cce2aa81283a35);

254};

255

[ 262](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b)typedef int (\*[charger\_get\_property\_t](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b))(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

263 union [charger\_propval](unioncharger__propval.md) \*val);

264

[ 271](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6)typedef int (\*[charger\_set\_property\_t](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6))(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

272 const union [charger\_propval](unioncharger__propval.md) \*val);

273

[ 280](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd)typedef int (\*[charger\_charge\_enable\_t](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd))(const struct [device](structdevice.md) \*dev, const bool enable);

281

[ 287](structcharger__driver__api.md)\_\_subsystem struct [charger\_driver\_api](structcharger__driver__api.md) {

[ 288](structcharger__driver__api.md#a945bfc62b0572da09480e97a6a819269) [charger\_get\_property\_t](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b) [get\_property](structcharger__driver__api.md#a945bfc62b0572da09480e97a6a819269);

[ 289](structcharger__driver__api.md#a7a7942d11841d9ec02ff57f46323a3a3) [charger\_set\_property\_t](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6) [set\_property](structcharger__driver__api.md#a7a7942d11841d9ec02ff57f46323a3a3);

[ 290](structcharger__driver__api.md#a41ea553c8bb6a24915d73a00129ee67d) [charger\_charge\_enable\_t](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd) [charge\_enable](structcharger__driver__api.md#a41ea553c8bb6a24915d73a00129ee67d);

291};

292

[ 303](group__charger__interface.md#ga00e5b61d517c93d7d3c863b14b07b738)\_\_syscall int [charger\_get\_prop](group__charger__interface.md#ga00e5b61d517c93d7d3c863b14b07b738)(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

304 union [charger\_propval](unioncharger__propval.md) \*val);

305

306static inline int z\_impl\_charger\_get\_prop(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

307 union [charger\_propval](unioncharger__propval.md) \*val)

308{

309 const struct [charger\_driver\_api](structcharger__driver__api.md) \*api = (const struct [charger\_driver\_api](structcharger__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

310

311 return api->get\_property(dev, prop, val);

312}

313

[ 324](group__charger__interface.md#ga0036e3f5924585457a99a2e444ef5aab)\_\_syscall int [charger\_set\_prop](group__charger__interface.md#ga0036e3f5924585457a99a2e444ef5aab)(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

325 const union [charger\_propval](unioncharger__propval.md) \*val);

326

327static inline int z\_impl\_charger\_set\_prop(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

328 const union [charger\_propval](unioncharger__propval.md) \*val)

329{

330 const struct [charger\_driver\_api](structcharger__driver__api.md) \*api = (const struct [charger\_driver\_api](structcharger__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

331

332 return api->set\_property(dev, prop, val);

333}

334

[ 345](group__charger__interface.md#gace1ea9841574d75d314db078df5a0b3a)\_\_syscall int [charger\_charge\_enable](group__charger__interface.md#gace1ea9841574d75d314db078df5a0b3a)(const struct [device](structdevice.md) \*dev, const bool enable);

346

347static inline int z\_impl\_charger\_charge\_enable(const struct [device](structdevice.md) \*dev, const bool enable)

348{

349 const struct [charger\_driver\_api](structcharger__driver__api.md) \*api = (const struct [charger\_driver\_api](structcharger__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

350

351 return api->charge\_enable(dev, enable);

352}

353

357

358#ifdef \_\_cplusplus

359}

360#endif /\* \_\_cplusplus \*/

361

362#include <syscalls/charger.h>

363

364#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CHARGER\_H\_ \*/

[device.h](device_8h.md)

[charger\_set\_prop](group__charger__interface.md#ga0036e3f5924585457a99a2e444ef5aab)

int charger\_set\_prop(const struct device \*dev, const charger\_prop\_t prop, const union charger\_propval \*val)

Set a battery charger property.

[charger\_get\_prop](group__charger__interface.md#ga00e5b61d517c93d7d3c863b14b07b738)

int charger\_get\_prop(const struct device \*dev, const charger\_prop\_t prop, union charger\_propval \*val)

Fetch a battery charger property.

[charger\_notification\_severity](group__charger__interface.md#ga2e7d7f15725db4d502bc3f46476a310d)

charger\_notification\_severity

Charger severity levels for system notifications.

**Definition** charger.h:200

[charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7)

charger\_status

Charging states.

**Definition** charger.h:114

[charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635)

uint16\_t charger\_prop\_t

A charger property's identifier.

**Definition** charger.h:97

[charger\_set\_property\_t](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6)

int(\* charger\_set\_property\_t)(const struct device \*dev, const charger\_prop\_t prop, const union charger\_propval \*val)

Callback API for setting a charger property.

**Definition** charger.h:271

[charger\_property](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7)

charger\_property

Runtime Dynamic Battery Parameters.

**Definition** charger.h:35

[charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412)

charger\_health

Charger health conditions.

**Definition** charger.h:165

[charger\_charge\_enable](group__charger__interface.md#gace1ea9841574d75d314db078df5a0b3a)

int charger\_charge\_enable(const struct device \*dev, const bool enable)

Enable or disable a charge cycle.

[charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19)

charger\_online

External supply states.

**Definition** charger.h:102

[charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803)

charger\_charge\_type

Charge algorithm types.

**Definition** charger.h:130

[charger\_charge\_enable\_t](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd)

int(\* charger\_charge\_enable\_t)(const struct device \*dev, const bool enable)

Callback API enabling or disabling a charge cycle.

**Definition** charger.h:280

[charger\_get\_property\_t](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b)

int(\* charger\_get\_property\_t)(const struct device \*dev, const charger\_prop\_t prop, union charger\_propval \*val)

Callback API for getting a charger property.

**Definition** charger.h:262

[CHARGER\_SEVERITY\_WARNING](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885)

@ CHARGER\_SEVERITY\_WARNING

Base severity level.

**Definition** charger.h:206

[CHARGER\_SEVERITY\_PEAK](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b)

@ CHARGER\_SEVERITY\_PEAK

Most severe level, typically triggered instantaneously.

**Definition** charger.h:202

[CHARGER\_SEVERITY\_CRITICAL](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8)

@ CHARGER\_SEVERITY\_CRITICAL

More severe than the warning level, less severe than peak.

**Definition** charger.h:204

[CHARGER\_STATUS\_FULL](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf)

@ CHARGER\_STATUS\_FULL

The battery is full and the charging device will not attempt charging.

**Definition** charger.h:124

[CHARGER\_STATUS\_NOT\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658)

@ CHARGER\_STATUS\_NOT\_CHARGING

Charging device is not charging a battery.

**Definition** charger.h:122

[CHARGER\_STATUS\_DISCHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e)

@ CHARGER\_STATUS\_DISCHARGING

Charging device is not able to charge a battery.

**Definition** charger.h:120

[CHARGER\_STATUS\_UNKNOWN](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5)

@ CHARGER\_STATUS\_UNKNOWN

Charging device state is unknown.

**Definition** charger.h:116

[CHARGER\_STATUS\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad)

@ CHARGER\_STATUS\_CHARGING

Charging device is charging a battery.

**Definition** charger.h:118

[CHARGER\_PROP\_PRESENT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a0dd5ee0d22cba6440c3f3583582d405b)

@ CHARGER\_PROP\_PRESENT

Reports whether or not a battery is present.

**Definition** charger.h:41

[CHARGER\_PROP\_ONLINE](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a1c8906c0e4e278b84cab7d126cf95526)

@ CHARGER\_PROP\_ONLINE

Indicates if external supply is present for the charger.

**Definition** charger.h:38

[CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a1e60d770a5d8e47118040ace3c6d8ec0)

@ CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV

Configuration of the input voltage regulation target in µV.

**Definition** charger.h:72

[CHARGER\_PROP\_CUSTOM\_BEGIN](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3)

@ CHARGER\_PROP\_CUSTOM\_BEGIN

Reserved to demark downstream custom properties - use this value as the actual value may change over ...

**Definition** charger.h:86

[CHARGER\_PROP\_HEALTH](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654)

@ CHARGER\_PROP\_HEALTH

Represents the health of the charger.

**Definition** charger.h:50

[CHARGER\_PROP\_COMMON\_COUNT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732)

@ CHARGER\_PROP\_COMMON\_COUNT

Reserved to demark end of common charger properties.

**Definition** charger.h:81

[CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a5b4a6c4f1f6abb7a568c7c42dca696bf)

@ CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV

Configuration of charge voltage regulation target in µV.

**Definition** charger.h:58

[CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a703a0e374053a410ec154eac117f9085)

@ CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA

Configuration of the input current regulation target in µA.

**Definition** charger.h:65

[CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a70f2c71cd9d4e0f88ee36886094540fe)

@ CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION

Configuration to issue a notification to the system based on the input current level and timing.

**Definition** charger.h:79

[CHARGER\_PROP\_STATUS](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a73b9f45dd43347016a4dd6e15cd78cf6)

@ CHARGER\_PROP\_STATUS

Represents the charging status of the charger.

**Definition** charger.h:44

[CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a81a18d7286bfcf729402db6990ddc306)

@ CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA

Configuration of current sink used for charging in µA.

**Definition** charger.h:52

[CHARGER\_PROP\_MAX](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e)

@ CHARGER\_PROP\_MAX

Reserved to demark end of valid enum properties.

**Definition** charger.h:88

[CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9)

@ CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA

Configuration of current sink used for conditioning in µA.

**Definition** charger.h:54

[CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc)

@ CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA

Configuration of charge termination target in µA.

**Definition** charger.h:56

[CHARGER\_PROP\_CHARGE\_TYPE](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95)

@ CHARGER\_PROP\_CHARGE\_TYPE

Represents the charging algo type of the charger.

**Definition** charger.h:47

[CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82)

@ CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE

The charger device's safety timer has expired.

**Definition** charger.h:184

[CHARGER\_HEALTH\_CALIBRATION\_REQUIRED](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1)

@ CHARGER\_HEALTH\_CALIBRATION\_REQUIRED

The charger device requires calibration.

**Definition** charger.h:186

[CHARGER\_HEALTH\_WARM](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f)

@ CHARGER\_HEALTH\_WARM

The battery temperature is in the "warm" range.

**Definition** charger.h:188

[CHARGER\_HEALTH\_UNKNOWN](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad)

@ CHARGER\_HEALTH\_UNKNOWN

Charger health condition is unknown.

**Definition** charger.h:167

[CHARGER\_HEALTH\_COLD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967)

@ CHARGER\_HEALTH\_COLD

The battery temperature is below the "cold" threshold.

**Definition** charger.h:180

[CHARGER\_HEALTH\_NO\_BATTERY](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b)

@ CHARGER\_HEALTH\_NO\_BATTERY

The charger device does not detect a battery.

**Definition** charger.h:194

[CHARGER\_HEALTH\_UNSPEC\_FAILURE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa)

@ CHARGER\_HEALTH\_UNSPEC\_FAILURE

The battery or charger device is experiencing an unspecified failure.

**Definition** charger.h:178

[CHARGER\_HEALTH\_GOOD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538)

@ CHARGER\_HEALTH\_GOOD

Charger health condition is good.

**Definition** charger.h:169

[CHARGER\_HEALTH\_HOT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1)

@ CHARGER\_HEALTH\_HOT

The battery temperature is below the "hot" threshold.

**Definition** charger.h:192

[CHARGER\_HEALTH\_COOL](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3)

@ CHARGER\_HEALTH\_COOL

The battery temperature is in the "cool" range.

**Definition** charger.h:190

[CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce)

@ CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE

The charger device's watchdog timer has expired.

**Definition** charger.h:182

[CHARGER\_HEALTH\_OVERVOLTAGE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459)

@ CHARGER\_HEALTH\_OVERVOLTAGE

The battery voltage has exceeded its overvoltage threshold.

**Definition** charger.h:173

[CHARGER\_HEALTH\_OVERHEAT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b)

@ CHARGER\_HEALTH\_OVERHEAT

The charger device is overheated.

**Definition** charger.h:171

[CHARGER\_ONLINE\_FIXED](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6)

@ CHARGER\_ONLINE\_FIXED

External supply is present and of fixed output.

**Definition** charger.h:106

[CHARGER\_ONLINE\_PROGRAMMABLE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e)

@ CHARGER\_ONLINE\_PROGRAMMABLE

External supply is present and of programmable output.

**Definition** charger.h:108

[CHARGER\_ONLINE\_OFFLINE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3)

@ CHARGER\_ONLINE\_OFFLINE

External supply not present.

**Definition** charger.h:104

[CHARGER\_CHARGE\_TYPE\_STANDARD](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6)

@ CHARGER\_CHARGE\_TYPE\_STANDARD

Charging is occurring at a moderate charge rate.

**Definition** charger.h:143

[CHARGER\_CHARGE\_TYPE\_NONE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17)

@ CHARGER\_CHARGE\_TYPE\_NONE

Charging is not occurring.

**Definition** charger.h:134

[CHARGER\_CHARGE\_TYPE\_ADAPTIVE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2)

@ CHARGER\_CHARGE\_TYPE\_ADAPTIVE

**Definition** charger.h:147

[CHARGER\_CHARGE\_TYPE\_UNKNOWN](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4)

@ CHARGER\_CHARGE\_TYPE\_UNKNOWN

Charge type is unknown.

**Definition** charger.h:132

[CHARGER\_CHARGE\_TYPE\_BYPASS](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8)

@ CHARGER\_CHARGE\_TYPE\_BYPASS

**Definition** charger.h:157

[CHARGER\_CHARGE\_TYPE\_LONGLIFE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f)

@ CHARGER\_CHARGE\_TYPE\_LONGLIFE

**Definition** charger.h:152

[CHARGER\_CHARGE\_TYPE\_TRICKLE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8)

@ CHARGER\_CHARGE\_TYPE\_TRICKLE

Charging is occurring at the slowest desired charge rate, typically for battery detection or precondi...

**Definition** charger.h:139

[CHARGER\_CHARGE\_TYPE\_FAST](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711)

@ CHARGER\_CHARGE\_TYPE\_FAST

Charging is occurring at the fastest desired charge rate.

**Definition** charger.h:141

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

[charger\_current\_notifier](structcharger__current__notifier.md)

The input current thresholds for the charger to notify the system.

**Definition** charger.h:212

[charger\_current\_notifier::severity](structcharger__current__notifier.md#a22c26477263e5abedb200de36a29d9de)

uint8\_t severity

The severity of the notification where CHARGER\_SEVERITY\_PEAK is the most severe.

**Definition** charger.h:214

[charger\_current\_notifier::duration\_us](structcharger__current__notifier.md#a4998999ef893d18fa64b86ec4fd9ad94)

uint32\_t duration\_us

The duration of excess current before notifying the system.

**Definition** charger.h:218

[charger\_current\_notifier::current\_ua](structcharger__current__notifier.md#acb54706bf47f55e197e799393b9eb87e)

uint32\_t current\_ua

The current threshold to be exceeded.

**Definition** charger.h:216

[charger\_driver\_api](structcharger__driver__api.md)

Charging device API.

**Definition** charger.h:287

[charger\_driver\_api::charge\_enable](structcharger__driver__api.md#a41ea553c8bb6a24915d73a00129ee67d)

charger\_charge\_enable\_t charge\_enable

**Definition** charger.h:290

[charger\_driver\_api::set\_property](structcharger__driver__api.md#a7a7942d11841d9ec02ff57f46323a3a3)

charger\_set\_property\_t set\_property

**Definition** charger.h:289

[charger\_driver\_api::get\_property](structcharger__driver__api.md#a945bfc62b0572da09480e97a6a819269)

charger\_get\_property\_t get\_property

**Definition** charger.h:288

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[charger\_propval](unioncharger__propval.md)

container for a charger\_property value

**Definition** charger.h:225

[charger\_propval::input\_current\_notification](unioncharger__propval.md#a0ad956ab4d0b306f94cce2aa81283a35)

struct charger\_current\_notifier input\_current\_notification

CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION.

**Definition** charger.h:253

[charger\_propval::precharge\_current\_ua](unioncharger__propval.md#a24a97e16505fa336bd3a68743d05936b)

uint32\_t precharge\_current\_ua

CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA.

**Definition** charger.h:243

[charger\_propval::const\_charge\_voltage\_uv](unioncharger__propval.md#a733bae9ce0bf7e902f8af307f94a356c)

uint32\_t const\_charge\_voltage\_uv

CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV.

**Definition** charger.h:247

[charger\_propval::status](unioncharger__propval.md#a7f4976d72d4a7d48385ceb9f18c510b5)

enum charger\_status status

CHARGER\_PROP\_STATUS.

**Definition** charger.h:235

[charger\_propval::online](unioncharger__propval.md#a8589124e6152b70b649788a8b94461ab)

enum charger\_online online

CHARGER\_PROP\_ONLINE.

**Definition** charger.h:231

[charger\_propval::charge\_term\_current\_ua](unioncharger__propval.md#a89d0c93d68650cefe29e891f4db928f4)

uint32\_t charge\_term\_current\_ua

CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA.

**Definition** charger.h:245

[charger\_propval::present](unioncharger__propval.md#ab0eec508b90d205a1662fd6c69638764)

bool present

CHARGER\_PROP\_PRESENT.

**Definition** charger.h:233

[charger\_propval::health](unioncharger__propval.md#abd990f67423424da60856f4b6e8824a3)

enum charger\_health health

CHARGER\_PROP\_HEALTH.

**Definition** charger.h:239

[charger\_propval::charge\_type](unioncharger__propval.md#ac1a594de2b1c10d28b6a81dd66f1a6ba)

enum charger\_charge\_type charge\_type

CHARGER\_PROP\_CHARGE\_TYPE.

**Definition** charger.h:237

[charger\_propval::input\_current\_regulation\_current\_ua](unioncharger__propval.md#ae51670de8fa560f0c7610452db029bc2)

uint32\_t input\_current\_regulation\_current\_ua

CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA.

**Definition** charger.h:249

[charger\_propval::const\_charge\_current\_ua](unioncharger__propval.md#af4e383bb797432033050937740ce0ac3)

uint32\_t const\_charge\_current\_ua

CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA.

**Definition** charger.h:241

[charger\_propval::input\_voltage\_regulation\_voltage\_uv](unioncharger__propval.md#afbe7b5fe1e421fb97b37d71ce14dc51a)

uint32\_t input\_voltage\_regulation\_voltage\_uv

CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV.

**Definition** charger.h:251

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [charger.h](charger_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
