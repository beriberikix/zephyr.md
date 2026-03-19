---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/charger_8h_source.html
original_path: doxygen/html/charger_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 86](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72) [CHARGER\_PROP\_DISCHARGE\_CURRENT\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72),

[ 91](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0) [CHARGER\_PROP\_SYSTEM\_VOLTAGE\_NOTIFICATION\_UV](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0),

[ 97](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b) [CHARGER\_PROP\_STATUS\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b),

[ 103](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7) [CHARGER\_PROP\_ONLINE\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7),

[ 105](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732) [CHARGER\_PROP\_COMMON\_COUNT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732),

[ 110](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3) [CHARGER\_PROP\_CUSTOM\_BEGIN](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3) = [CHARGER\_PROP\_COMMON\_COUNT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732) + 1,

[ 112](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e) [CHARGER\_PROP\_MAX](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e) = [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602),

113};

114

[ 121](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635);

122

[ 126](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19)enum [charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) {

[ 128](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3) [CHARGER\_ONLINE\_OFFLINE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3) = 0,

[ 130](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6) [CHARGER\_ONLINE\_FIXED](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6),

[ 132](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e) [CHARGER\_ONLINE\_PROGRAMMABLE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e),

133};

134

[ 138](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7)enum [charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) {

[ 140](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5) [CHARGER\_STATUS\_UNKNOWN](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5) = 0,

[ 142](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad) [CHARGER\_STATUS\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad),

[ 144](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e) [CHARGER\_STATUS\_DISCHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e),

[ 146](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658) [CHARGER\_STATUS\_NOT\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658),

[ 148](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf) [CHARGER\_STATUS\_FULL](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf),

149};

150

[ 154](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803)enum [charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803) {

[ 156](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4) [CHARGER\_CHARGE\_TYPE\_UNKNOWN](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4) = 0,

[ 158](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17) [CHARGER\_CHARGE\_TYPE\_NONE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17),

[ 163](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8) [CHARGER\_CHARGE\_TYPE\_TRICKLE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8),

[ 165](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711) [CHARGER\_CHARGE\_TYPE\_FAST](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711),

[ 167](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6) [CHARGER\_CHARGE\_TYPE\_STANDARD](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6),

168 /\*

169 \* Charging is being dynamically adjusted by the charger device

170 \*/

[ 171](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2) [CHARGER\_CHARGE\_TYPE\_ADAPTIVE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2),

172 /\*

173 \* Charging is occurring at a reduced charge rate to preserve

174 \* battery health

175 \*/

[ 176](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f) [CHARGER\_CHARGE\_TYPE\_LONGLIFE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f),

177 /\*

178 \* The charger device is being bypassed and the power conversion

179 \* is being handled externally, typically by a "smart" wall adaptor

180 \*/

[ 181](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8) [CHARGER\_CHARGE\_TYPE\_BYPASS](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8),

182};

183

[ 189](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412)enum [charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412) {

[ 191](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad) [CHARGER\_HEALTH\_UNKNOWN](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad) = 0,

[ 193](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538) [CHARGER\_HEALTH\_GOOD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538),

[ 195](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b) [CHARGER\_HEALTH\_OVERHEAT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b),

[ 197](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459) [CHARGER\_HEALTH\_OVERVOLTAGE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459),

[ 202](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa) [CHARGER\_HEALTH\_UNSPEC\_FAILURE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa),

[ 204](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967) [CHARGER\_HEALTH\_COLD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967),

[ 206](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce) [CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce),

[ 208](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82) [CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82),

[ 210](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1) [CHARGER\_HEALTH\_CALIBRATION\_REQUIRED](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1),

[ 212](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f) [CHARGER\_HEALTH\_WARM](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f),

[ 214](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3) [CHARGER\_HEALTH\_COOL](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3),

[ 216](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1) [CHARGER\_HEALTH\_HOT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1),

[ 218](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b) [CHARGER\_HEALTH\_NO\_BATTERY](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b),

219};

220

[ 224](group__charger__interface.md#ga2e7d7f15725db4d502bc3f46476a310d)enum [charger\_notification\_severity](group__charger__interface.md#ga2e7d7f15725db4d502bc3f46476a310d) {

[ 226](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b) [CHARGER\_SEVERITY\_PEAK](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b) = 0,

[ 228](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8) [CHARGER\_SEVERITY\_CRITICAL](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8),

[ 230](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885) [CHARGER\_SEVERITY\_WARNING](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885),

231};

232

[ 236](structcharger__current__notifier.md)struct [charger\_current\_notifier](structcharger__current__notifier.md) {

[ 238](structcharger__current__notifier.md#a22c26477263e5abedb200de36a29d9de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [severity](structcharger__current__notifier.md#a22c26477263e5abedb200de36a29d9de);

[ 240](structcharger__current__notifier.md#acb54706bf47f55e197e799393b9eb87e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [current\_ua](structcharger__current__notifier.md#acb54706bf47f55e197e799393b9eb87e);

[ 242](structcharger__current__notifier.md#a4998999ef893d18fa64b86ec4fd9ad94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [duration\_us](structcharger__current__notifier.md#a4998999ef893d18fa64b86ec4fd9ad94);

243};

244

[ 250](group__charger__interface.md#ga7666697bde91b66829113efe151d1cb2)typedef void (\*[charger\_status\_notifier\_t](group__charger__interface.md#ga7666697bde91b66829113efe151d1cb2))(enum [charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) status);

251

[ 257](group__charger__interface.md#gab29c2fafc53988555d72974199f25475)typedef void (\*[charger\_online\_notifier\_t](group__charger__interface.md#gab29c2fafc53988555d72974199f25475))(enum [charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) online);

258

[ 263](unioncharger__propval.md)union [charger\_propval](unioncharger__propval.md) {

264 /\* Fields have the format: \*/

265 /\* CHARGER\_PROPERTY\_FIELD \*/

266 /\* type property\_field; \*/

267

[ 269](unioncharger__propval.md#a8589124e6152b70b649788a8b94461ab) enum [charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) [online](unioncharger__propval.md#a8589124e6152b70b649788a8b94461ab);

[ 271](unioncharger__propval.md#ab0eec508b90d205a1662fd6c69638764) bool [present](unioncharger__propval.md#ab0eec508b90d205a1662fd6c69638764);

[ 273](unioncharger__propval.md#a7f4976d72d4a7d48385ceb9f18c510b5) enum [charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) [status](unioncharger__propval.md#a7f4976d72d4a7d48385ceb9f18c510b5);

[ 275](unioncharger__propval.md#ac1a594de2b1c10d28b6a81dd66f1a6ba) enum [charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803) [charge\_type](unioncharger__propval.md#ac1a594de2b1c10d28b6a81dd66f1a6ba);

[ 277](unioncharger__propval.md#abd990f67423424da60856f4b6e8824a3) enum [charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412) [health](unioncharger__propval.md#abd990f67423424da60856f4b6e8824a3);

[ 279](unioncharger__propval.md#af4e383bb797432033050937740ce0ac3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [const\_charge\_current\_ua](unioncharger__propval.md#af4e383bb797432033050937740ce0ac3);

[ 281](unioncharger__propval.md#a24a97e16505fa336bd3a68743d05936b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [precharge\_current\_ua](unioncharger__propval.md#a24a97e16505fa336bd3a68743d05936b);

[ 283](unioncharger__propval.md#a89d0c93d68650cefe29e891f4db928f4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [charge\_term\_current\_ua](unioncharger__propval.md#a89d0c93d68650cefe29e891f4db928f4);

[ 285](unioncharger__propval.md#a733bae9ce0bf7e902f8af307f94a356c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [const\_charge\_voltage\_uv](unioncharger__propval.md#a733bae9ce0bf7e902f8af307f94a356c);

[ 287](unioncharger__propval.md#ae51670de8fa560f0c7610452db029bc2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [input\_current\_regulation\_current\_ua](unioncharger__propval.md#ae51670de8fa560f0c7610452db029bc2);

[ 289](unioncharger__propval.md#afbe7b5fe1e421fb97b37d71ce14dc51a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [input\_voltage\_regulation\_voltage\_uv](unioncharger__propval.md#afbe7b5fe1e421fb97b37d71ce14dc51a);

[ 291](unioncharger__propval.md#a0ad956ab4d0b306f94cce2aa81283a35) struct [charger\_current\_notifier](structcharger__current__notifier.md) [input\_current\_notification](unioncharger__propval.md#a0ad956ab4d0b306f94cce2aa81283a35);

[ 293](unioncharger__propval.md#af256e63ca94f7809da101ad1c33c8e7a) struct [charger\_current\_notifier](structcharger__current__notifier.md) [discharge\_current\_notification](unioncharger__propval.md#af256e63ca94f7809da101ad1c33c8e7a);

[ 295](unioncharger__propval.md#a541d1bf0b3e32d7aaeb6a2f4f443c5dc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [system\_voltage\_notification](unioncharger__propval.md#a541d1bf0b3e32d7aaeb6a2f4f443c5dc);

[ 297](unioncharger__propval.md#ad77547e88ec465d2e37526751008f634) [charger\_status\_notifier\_t](group__charger__interface.md#ga7666697bde91b66829113efe151d1cb2) [status\_notification](unioncharger__propval.md#ad77547e88ec465d2e37526751008f634);

[ 299](unioncharger__propval.md#ab9f40a6083ff2361ea4d161226cd77ad) [charger\_online\_notifier\_t](group__charger__interface.md#gab29c2fafc53988555d72974199f25475) [online\_notification](unioncharger__propval.md#ab9f40a6083ff2361ea4d161226cd77ad);

300};

301

[ 308](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b)typedef int (\*[charger\_get\_property\_t](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b))(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

309 union [charger\_propval](unioncharger__propval.md) \*val);

310

[ 317](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6)typedef int (\*[charger\_set\_property\_t](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6))(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

318 const union [charger\_propval](unioncharger__propval.md) \*val);

319

[ 326](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd)typedef int (\*[charger\_charge\_enable\_t](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd))(const struct [device](structdevice.md) \*dev, const bool enable);

327

[ 333](structcharger__driver__api.md)\_\_subsystem struct [charger\_driver\_api](structcharger__driver__api.md) {

[ 334](structcharger__driver__api.md#a945bfc62b0572da09480e97a6a819269) [charger\_get\_property\_t](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b) [get\_property](structcharger__driver__api.md#a945bfc62b0572da09480e97a6a819269);

[ 335](structcharger__driver__api.md#a7a7942d11841d9ec02ff57f46323a3a3) [charger\_set\_property\_t](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6) [set\_property](structcharger__driver__api.md#a7a7942d11841d9ec02ff57f46323a3a3);

[ 336](structcharger__driver__api.md#a41ea553c8bb6a24915d73a00129ee67d) [charger\_charge\_enable\_t](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd) [charge\_enable](structcharger__driver__api.md#a41ea553c8bb6a24915d73a00129ee67d);

337};

338

[ 349](group__charger__interface.md#ga00e5b61d517c93d7d3c863b14b07b738)\_\_syscall int [charger\_get\_prop](group__charger__interface.md#ga00e5b61d517c93d7d3c863b14b07b738)(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

350 union [charger\_propval](unioncharger__propval.md) \*val);

351

352static inline int z\_impl\_charger\_get\_prop(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

353 union [charger\_propval](unioncharger__propval.md) \*val)

354{

355 const struct [charger\_driver\_api](structcharger__driver__api.md) \*api = (const struct [charger\_driver\_api](structcharger__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

356

357 return api->get\_property(dev, prop, val);

358}

359

[ 370](group__charger__interface.md#ga0036e3f5924585457a99a2e444ef5aab)\_\_syscall int [charger\_set\_prop](group__charger__interface.md#ga0036e3f5924585457a99a2e444ef5aab)(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

371 const union [charger\_propval](unioncharger__propval.md) \*val);

372

373static inline int z\_impl\_charger\_set\_prop(const struct [device](structdevice.md) \*dev, const [charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635) prop,

374 const union [charger\_propval](unioncharger__propval.md) \*val)

375{

376 const struct [charger\_driver\_api](structcharger__driver__api.md) \*api = (const struct [charger\_driver\_api](structcharger__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

377

378 return api->set\_property(dev, prop, val);

379}

380

[ 391](group__charger__interface.md#gace1ea9841574d75d314db078df5a0b3a)\_\_syscall int [charger\_charge\_enable](group__charger__interface.md#gace1ea9841574d75d314db078df5a0b3a)(const struct [device](structdevice.md) \*dev, const bool enable);

392

393static inline int z\_impl\_charger\_charge\_enable(const struct [device](structdevice.md) \*dev, const bool enable)

394{

395 const struct [charger\_driver\_api](structcharger__driver__api.md) \*api = (const struct [charger\_driver\_api](structcharger__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

396

397 return api->charge\_enable(dev, enable);

398}

399

403

404#ifdef \_\_cplusplus

405}

406#endif /\* \_\_cplusplus \*/

407

408#include <zephyr/syscalls/charger.h>

409

410#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CHARGER\_H\_ \*/

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

**Definition** charger.h:224

[charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7)

charger\_status

Charging states.

**Definition** charger.h:138

[charger\_prop\_t](group__charger__interface.md#ga4ce808890de2d01cdb75feddbf275635)

uint16\_t charger\_prop\_t

A charger property's identifier.

**Definition** charger.h:121

[charger\_set\_property\_t](group__charger__interface.md#ga6556781abf0e81eee431c88cb894a8e6)

int(\* charger\_set\_property\_t)(const struct device \*dev, const charger\_prop\_t prop, const union charger\_propval \*val)

Callback API for setting a charger property.

**Definition** charger.h:317

[charger\_property](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7)

charger\_property

Runtime Dynamic Battery Parameters.

**Definition** charger.h:35

[charger\_status\_notifier\_t](group__charger__interface.md#ga7666697bde91b66829113efe151d1cb2)

void(\* charger\_status\_notifier\_t)(enum charger\_status status)

The charger status change callback to notify the system.

**Definition** charger.h:250

[charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412)

charger\_health

Charger health conditions.

**Definition** charger.h:189

[charger\_online\_notifier\_t](group__charger__interface.md#gab29c2fafc53988555d72974199f25475)

void(\* charger\_online\_notifier\_t)(enum charger\_online online)

The charger online change callback to notify the system.

**Definition** charger.h:257

[charger\_charge\_enable](group__charger__interface.md#gace1ea9841574d75d314db078df5a0b3a)

int charger\_charge\_enable(const struct device \*dev, const bool enable)

Enable or disable a charge cycle.

[charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19)

charger\_online

External supply states.

**Definition** charger.h:126

[charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803)

charger\_charge\_type

Charge algorithm types.

**Definition** charger.h:154

[charger\_charge\_enable\_t](group__charger__interface.md#gaf035c2972693a8763fd08b7db8c9c0bd)

int(\* charger\_charge\_enable\_t)(const struct device \*dev, const bool enable)

Callback API enabling or disabling a charge cycle.

**Definition** charger.h:326

[charger\_get\_property\_t](group__charger__interface.md#gafb7488129e0a6c086d3ff0ffadb6c82b)

int(\* charger\_get\_property\_t)(const struct device \*dev, const charger\_prop\_t prop, union charger\_propval \*val)

Callback API for getting a charger property.

**Definition** charger.h:308

[CHARGER\_SEVERITY\_WARNING](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da347972f338fe70920f72c85dcdd1f885)

@ CHARGER\_SEVERITY\_WARNING

Base severity level.

**Definition** charger.h:230

[CHARGER\_SEVERITY\_PEAK](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da667f21cc72028772d09228424f75b40b)

@ CHARGER\_SEVERITY\_PEAK

Most severe level, typically triggered instantaneously.

**Definition** charger.h:226

[CHARGER\_SEVERITY\_CRITICAL](group__charger__interface.md#gga2e7d7f15725db4d502bc3f46476a310da6bb0e1059a26d31380094530da94e3e8)

@ CHARGER\_SEVERITY\_CRITICAL

More severe than the warning level, less severe than peak.

**Definition** charger.h:228

[CHARGER\_STATUS\_FULL](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a2f550ea27e63b2eab78cc673d3e692cf)

@ CHARGER\_STATUS\_FULL

The battery is full and the charging device will not attempt charging.

**Definition** charger.h:148

[CHARGER\_STATUS\_NOT\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7a445d1979c2541ead57ddaa89dc57c658)

@ CHARGER\_STATUS\_NOT\_CHARGING

Charging device is not charging a battery.

**Definition** charger.h:146

[CHARGER\_STATUS\_DISCHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad06083516280a41fec5f8cc649ff499e)

@ CHARGER\_STATUS\_DISCHARGING

Charging device is not able to charge a battery.

**Definition** charger.h:144

[CHARGER\_STATUS\_UNKNOWN](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad474b06c524aea24b1ecb2e7d6621fa5)

@ CHARGER\_STATUS\_UNKNOWN

Charging device state is unknown.

**Definition** charger.h:140

[CHARGER\_STATUS\_CHARGING](group__charger__interface.md#gga4a3c46bc0916082d15e665f7665c89d7ad95370e7cd6dc5d72e73d741b41cb8ad)

@ CHARGER\_STATUS\_CHARGING

Charging device is charging a battery.

**Definition** charger.h:142

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

**Definition** charger.h:110

[CHARGER\_PROP\_HEALTH](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a2cc8bc744a98284e6c96a6ffb30ec654)

@ CHARGER\_PROP\_HEALTH

Represents the health of the charger.

**Definition** charger.h:50

[CHARGER\_PROP\_ONLINE\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a389920359b8866af70b164d68820d4b7)

@ CHARGER\_PROP\_ONLINE\_NOTIFICATION

Configuration to issue a notification to the system based on the charger online change.

**Definition** charger.h:103

[CHARGER\_PROP\_COMMON\_COUNT](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3c6d858ad83fa0aeca39ce33817f3732)

@ CHARGER\_PROP\_COMMON\_COUNT

Reserved to demark end of common charger properties.

**Definition** charger.h:105

[CHARGER\_PROP\_DISCHARGE\_CURRENT\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a3d3e3190b016a9c31ed5c82e2ade0b72)

@ CHARGER\_PROP\_DISCHARGE\_CURRENT\_NOTIFICATION

Configuration to issue a notification to the system based on the battery discharge current level and ...

**Definition** charger.h:86

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

[CHARGER\_PROP\_STATUS\_NOTIFICATION](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a9340eb6fb5b80370148a43366b753d9b)

@ CHARGER\_PROP\_STATUS\_NOTIFICATION

Configuration to issue a notification to the system based on the charger status change.

**Definition** charger.h:97

[CHARGER\_PROP\_MAX](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7a97342ebdadce27894e82dc57ed54724e)

@ CHARGER\_PROP\_MAX

Reserved to demark end of valid enum properties.

**Definition** charger.h:112

[CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aa8d97a1db907ccd40a7b5d917c0a9ab9)

@ CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA

Configuration of current sink used for conditioning in µA.

**Definition** charger.h:54

[CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7ac60d2e9945e8f1eaf0e824b778a377fc)

@ CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA

Configuration of charge termination target in µA.

**Definition** charger.h:56

[CHARGER\_PROP\_SYSTEM\_VOLTAGE\_NOTIFICATION\_UV](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7ace0a0e6cbc0ccaf166ff0df7e1b275c0)

@ CHARGER\_PROP\_SYSTEM\_VOLTAGE\_NOTIFICATION\_UV

Configuration of the falling system voltage threshold where a notification is issued to the system,...

**Definition** charger.h:91

[CHARGER\_PROP\_CHARGE\_TYPE](group__charger__interface.md#gga6eb3b4cc76e4f1e34732b7853eb860b7aff40a23cd65dcab5b3118fd9da3aaf95)

@ CHARGER\_PROP\_CHARGE\_TYPE

Represents the charging algo type of the charger.

**Definition** charger.h:47

[CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a17ccf9a3e7878c11e6a34bf5a4e38a82)

@ CHARGER\_HEALTH\_SAFETY\_TIMER\_EXPIRE

The charger device's safety timer has expired.

**Definition** charger.h:208

[CHARGER\_HEALTH\_CALIBRATION\_REQUIRED](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a1936cf89fd8e7286831a91dc218c25f1)

@ CHARGER\_HEALTH\_CALIBRATION\_REQUIRED

The charger device requires calibration.

**Definition** charger.h:210

[CHARGER\_HEALTH\_WARM](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a206b491bf7e7efc60b9a41d69a2d305f)

@ CHARGER\_HEALTH\_WARM

The battery temperature is in the "warm" range.

**Definition** charger.h:212

[CHARGER\_HEALTH\_UNKNOWN](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a21f2873586a920885d411e8dd02786ad)

@ CHARGER\_HEALTH\_UNKNOWN

Charger health condition is unknown.

**Definition** charger.h:191

[CHARGER\_HEALTH\_COLD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a24b2e80a03d4d06a267f3264edd64967)

@ CHARGER\_HEALTH\_COLD

The battery temperature is below the "cold" threshold.

**Definition** charger.h:204

[CHARGER\_HEALTH\_NO\_BATTERY](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a50dabeb87f23ca712b5c78f0e5a4c60b)

@ CHARGER\_HEALTH\_NO\_BATTERY

The charger device does not detect a battery.

**Definition** charger.h:218

[CHARGER\_HEALTH\_UNSPEC\_FAILURE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7651b0b32b8472caa8545278bef4e8fa)

@ CHARGER\_HEALTH\_UNSPEC\_FAILURE

The battery or charger device is experiencing an unspecified failure.

**Definition** charger.h:202

[CHARGER\_HEALTH\_GOOD](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412a7fe49d6d81fc76c70ab979eece42d538)

@ CHARGER\_HEALTH\_GOOD

Charger health condition is good.

**Definition** charger.h:193

[CHARGER\_HEALTH\_HOT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aa3cd6b3e3e2ccfde03ba49912a2efcf1)

@ CHARGER\_HEALTH\_HOT

The battery temperature is below the "hot" threshold.

**Definition** charger.h:216

[CHARGER\_HEALTH\_COOL](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412aad346d9b4b43998367facd491bc0ecd3)

@ CHARGER\_HEALTH\_COOL

The battery temperature is in the "cool" range.

**Definition** charger.h:214

[CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412ab9c81803fd5a1dd6a843765304e592ce)

@ CHARGER\_HEALTH\_WATCHDOG\_TIMER\_EXPIRE

The charger device's watchdog timer has expired.

**Definition** charger.h:206

[CHARGER\_HEALTH\_OVERVOLTAGE](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affbc931d777af7a03233d0dbed364459)

@ CHARGER\_HEALTH\_OVERVOLTAGE

The battery voltage has exceeded its overvoltage threshold.

**Definition** charger.h:197

[CHARGER\_HEALTH\_OVERHEAT](group__charger__interface.md#ggaab33241d3b85ab0770be9b1bd17e4412affd0237aed52d704e51f18a4d57f3b3b)

@ CHARGER\_HEALTH\_OVERHEAT

The charger device is overheated.

**Definition** charger.h:195

[CHARGER\_ONLINE\_FIXED](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a119679acb9bcc173831003dfa309f5a6)

@ CHARGER\_ONLINE\_FIXED

External supply is present and of fixed output.

**Definition** charger.h:130

[CHARGER\_ONLINE\_PROGRAMMABLE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a2b51eb24ac1047c99f8079beb261503e)

@ CHARGER\_ONLINE\_PROGRAMMABLE

External supply is present and of programmable output.

**Definition** charger.h:132

[CHARGER\_ONLINE\_OFFLINE](group__charger__interface.md#ggad95d2b1aaf18ac3a1c536f2d40317c19a50004df0b037325d33d21427a847a5b3)

@ CHARGER\_ONLINE\_OFFLINE

External supply not present.

**Definition** charger.h:128

[CHARGER\_CHARGE\_TYPE\_STANDARD](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a004c6c71a3a9943e151ed4fa49746ee6)

@ CHARGER\_CHARGE\_TYPE\_STANDARD

Charging is occurring at a moderate charge rate.

**Definition** charger.h:167

[CHARGER\_CHARGE\_TYPE\_NONE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803a71e7c6a73193c0ce1ba0467d93b72f17)

@ CHARGER\_CHARGE\_TYPE\_NONE

Charging is not occurring.

**Definition** charger.h:158

[CHARGER\_CHARGE\_TYPE\_ADAPTIVE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aa5a6d6cc9767fb0b19d13070c108ccc2)

@ CHARGER\_CHARGE\_TYPE\_ADAPTIVE

**Definition** charger.h:171

[CHARGER\_CHARGE\_TYPE\_UNKNOWN](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803aab6c7ea7d961c131bc91f91a9fa7cce4)

@ CHARGER\_CHARGE\_TYPE\_UNKNOWN

Charge type is unknown.

**Definition** charger.h:156

[CHARGER\_CHARGE\_TYPE\_BYPASS](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803abe42aac55841886e2a69b94018918ee8)

@ CHARGER\_CHARGE\_TYPE\_BYPASS

**Definition** charger.h:181

[CHARGER\_CHARGE\_TYPE\_LONGLIFE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acaa4a3c513188cd9dba71c98639bd31f)

@ CHARGER\_CHARGE\_TYPE\_LONGLIFE

**Definition** charger.h:176

[CHARGER\_CHARGE\_TYPE\_TRICKLE](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803acc5367f61f10e6574ec01d090598cbf8)

@ CHARGER\_CHARGE\_TYPE\_TRICKLE

Charging is occurring at the slowest desired charge rate, typically for battery detection or precondi...

**Definition** charger.h:163

[CHARGER\_CHARGE\_TYPE\_FAST](group__charger__interface.md#ggaee833a379a8674621d2fdf9b57d1f803ae2b5fc2d034a037c9eee5afca2c5a711)

@ CHARGER\_CHARGE\_TYPE\_FAST

Charging is occurring at the fastest desired charge rate.

**Definition** charger.h:165

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

**Definition** charger.h:236

[charger\_current\_notifier::severity](structcharger__current__notifier.md#a22c26477263e5abedb200de36a29d9de)

uint8\_t severity

The severity of the notification where CHARGER\_SEVERITY\_PEAK is the most severe.

**Definition** charger.h:238

[charger\_current\_notifier::duration\_us](structcharger__current__notifier.md#a4998999ef893d18fa64b86ec4fd9ad94)

uint32\_t duration\_us

The duration of excess current before notifying the system.

**Definition** charger.h:242

[charger\_current\_notifier::current\_ua](structcharger__current__notifier.md#acb54706bf47f55e197e799393b9eb87e)

uint32\_t current\_ua

The current threshold to be exceeded.

**Definition** charger.h:240

[charger\_driver\_api](structcharger__driver__api.md)

Charging device API.

**Definition** charger.h:333

[charger\_driver\_api::charge\_enable](structcharger__driver__api.md#a41ea553c8bb6a24915d73a00129ee67d)

charger\_charge\_enable\_t charge\_enable

**Definition** charger.h:336

[charger\_driver\_api::set\_property](structcharger__driver__api.md#a7a7942d11841d9ec02ff57f46323a3a3)

charger\_set\_property\_t set\_property

**Definition** charger.h:335

[charger\_driver\_api::get\_property](structcharger__driver__api.md#a945bfc62b0572da09480e97a6a819269)

charger\_get\_property\_t get\_property

**Definition** charger.h:334

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[charger\_propval](unioncharger__propval.md)

container for a charger\_property value

**Definition** charger.h:263

[charger\_propval::input\_current\_notification](unioncharger__propval.md#a0ad956ab4d0b306f94cce2aa81283a35)

struct charger\_current\_notifier input\_current\_notification

CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION.

**Definition** charger.h:291

[charger\_propval::precharge\_current\_ua](unioncharger__propval.md#a24a97e16505fa336bd3a68743d05936b)

uint32\_t precharge\_current\_ua

CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA.

**Definition** charger.h:281

[charger\_propval::system\_voltage\_notification](unioncharger__propval.md#a541d1bf0b3e32d7aaeb6a2f4f443c5dc)

uint32\_t system\_voltage\_notification

CHARGER\_PROP\_SYSTEM\_VOLTAGE\_NOTIFICATION\_UV.

**Definition** charger.h:295

[charger\_propval::const\_charge\_voltage\_uv](unioncharger__propval.md#a733bae9ce0bf7e902f8af307f94a356c)

uint32\_t const\_charge\_voltage\_uv

CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV.

**Definition** charger.h:285

[charger\_propval::status](unioncharger__propval.md#a7f4976d72d4a7d48385ceb9f18c510b5)

enum charger\_status status

CHARGER\_PROP\_STATUS.

**Definition** charger.h:273

[charger\_propval::online](unioncharger__propval.md#a8589124e6152b70b649788a8b94461ab)

enum charger\_online online

CHARGER\_PROP\_ONLINE.

**Definition** charger.h:269

[charger\_propval::charge\_term\_current\_ua](unioncharger__propval.md#a89d0c93d68650cefe29e891f4db928f4)

uint32\_t charge\_term\_current\_ua

CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA.

**Definition** charger.h:283

[charger\_propval::present](unioncharger__propval.md#ab0eec508b90d205a1662fd6c69638764)

bool present

CHARGER\_PROP\_PRESENT.

**Definition** charger.h:271

[charger\_propval::online\_notification](unioncharger__propval.md#ab9f40a6083ff2361ea4d161226cd77ad)

charger\_online\_notifier\_t online\_notification

CHARGER\_PROP\_ONLINE\_NOTIFICATION.

**Definition** charger.h:299

[charger\_propval::health](unioncharger__propval.md#abd990f67423424da60856f4b6e8824a3)

enum charger\_health health

CHARGER\_PROP\_HEALTH.

**Definition** charger.h:277

[charger\_propval::charge\_type](unioncharger__propval.md#ac1a594de2b1c10d28b6a81dd66f1a6ba)

enum charger\_charge\_type charge\_type

CHARGER\_PROP\_CHARGE\_TYPE.

**Definition** charger.h:275

[charger\_propval::status\_notification](unioncharger__propval.md#ad77547e88ec465d2e37526751008f634)

charger\_status\_notifier\_t status\_notification

CHARGER\_PROP\_STATUS\_NOTIFICATION.

**Definition** charger.h:297

[charger\_propval::input\_current\_regulation\_current\_ua](unioncharger__propval.md#ae51670de8fa560f0c7610452db029bc2)

uint32\_t input\_current\_regulation\_current\_ua

CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA.

**Definition** charger.h:287

[charger\_propval::discharge\_current\_notification](unioncharger__propval.md#af256e63ca94f7809da101ad1c33c8e7a)

struct charger\_current\_notifier discharge\_current\_notification

CHARGER\_PROP\_DISCHARGE\_CURRENT\_NOTIFICATION.

**Definition** charger.h:293

[charger\_propval::const\_charge\_current\_ua](unioncharger__propval.md#af4e383bb797432033050937740ce0ac3)

uint32\_t const\_charge\_current\_ua

CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA.

**Definition** charger.h:279

[charger\_propval::input\_voltage\_regulation\_voltage\_uv](unioncharger__propval.md#afbe7b5fe1e421fb97b37d71ce14dc51a)

uint32\_t input\_voltage\_regulation\_voltage\_uv

CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV.

**Definition** charger.h:289

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [charger.h](charger_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
