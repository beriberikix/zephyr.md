---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/hfp__ag_8h_source.html
original_path: doxygen/html/hfp__ag_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hfp\_ag.h

[Go to the documentation of this file.](hfp__ag_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \* Copyright 2023-2024 NXP

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_AG\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_AG\_H\_

13

20

21#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27/\* HFP AG Indicators \*/

[ 28](group__bt__hfp__ag.md#ga37640efdcc737bfa0390df889a62f810)enum [bt\_hfp\_ag\_indicator](group__bt__hfp__ag.md#ga37640efdcc737bfa0390df889a62f810) {

[ 29](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234) [BT\_HFP\_AG\_SERVICE\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234) = 0, /\* Service availability indicator \*/

[ 30](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d) [BT\_HFP\_AG\_CALL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d) = 1, /\* call status indicator \*/

[ 31](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5) [BT\_HFP\_AG\_CALL\_SETUP\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5) = 2, /\* Call set up status indicator \*/

[ 32](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b) [BT\_HFP\_AG\_CALL\_HELD\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b) = 3, /\* Call hold status indicator \*/

[ 33](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493) [BT\_HFP\_AG\_SIGNAL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493) = 4, /\* Signal strength indicator \*/

[ 34](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863) [BT\_HFP\_AG\_ROAM\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863) = 5, /\* Roaming status indicator \*/

[ 35](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609) [BT\_HFP\_AG\_BATTERY\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609) = 6, /\* Battery change indicator \*/

[ 36](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36) [BT\_HFP\_AG\_IND\_MAX](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36) /\* Indicator MAX value \*/

37};

38

39/\* HFP CODEC \*/

[ 40](group__bt__hfp__ag.md#gada6266f825879f39147c5d889e4192c9)#define BT\_HFP\_AG\_CODEC\_CVSD 0x01

[ 41](group__bt__hfp__ag.md#ga3591201c7310288ea2e01e2f77a0c0d3)#define BT\_HFP\_AG\_CODEC\_MSBC 0x02

[ 42](group__bt__hfp__ag.md#ga8a833c4b11dc9e8fd08a73a2af418d83)#define BT\_HFP\_AG\_CODEC\_LC3\_SWB 0x03

43

44struct bt\_hfp\_ag;

45struct bt\_hfp\_ag\_call;

46

[ 71](group__bt__hfp__ag.md#ga8e9b485f7ea0b9e16d96f578cdc587c3)typedef int (\*[bt\_hfp\_ag\_query\_subscriber\_func\_t](group__bt__hfp__ag.md#ga8e9b485f7ea0b9e16d96f578cdc587c3))(struct bt\_hfp\_ag \*ag, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

72 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) service);

73

74/\* HF indicators \*/

[ 75](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403)enum [hfp\_ag\_hf\_indicators](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403) {

[ 76](group__bt__hfp__ag.md#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f) [HFP\_AG\_ENHANCED\_SAFETY\_IND](group__bt__hfp__ag.md#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f) = 1, /\* Enhanced Safety \*/

[ 77](group__bt__hfp__ag.md#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1) [HFP\_AG\_BATTERY\_LEVEL\_IND](group__bt__hfp__ag.md#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1) = 2, /\* Remaining level of Battery \*/

78};

79

80/\* The status of the call \*/

[ 81](group__bt__hfp__ag.md#gad2220b4a470cb3d537cf09492847568e)enum \_\_packed [bt\_hfp\_ag\_call\_status](group__bt__hfp__ag.md#gad2220b4a470cb3d537cf09492847568e) {

[ 82](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658) [BT\_HFP\_AG\_CALL\_STATUS\_ACTIVE](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658) = 0, /\* Call is active \*/

[ 83](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2) [BT\_HFP\_AG\_CALL\_STATUS\_HELD](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2) = 1, /\* Call is on hold \*/

[ 84](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963) [BT\_HFP\_AG\_CALL\_STATUS\_DIALING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963) = 2, /\* Outgoing call is being dialed \*/

[ 85](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae) [BT\_HFP\_AG\_CALL\_STATUS\_ALERTING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae) = 3, /\* Outgoing call is being alerted \*/

[ 86](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8) [BT\_HFP\_AG\_CALL\_STATUS\_INCOMING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8) = 4, /\* Incoming call is came \*/

[ 87](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2) [BT\_HFP\_AG\_CALL\_STATUS\_WAITING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2) = 5, /\* Incoming call is waiting \*/

[ 88](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542) [BT\_HFP\_AG\_CALL\_STATUS\_INCOMING\_HELD](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542) = 6 /\* Call held by Response and Hold \*/

89};

90

91/\* The direction of the call \*/

[ 92](group__bt__hfp__ag.md#ga019020ee2ed73c218f7dadf8371bf9a6)enum \_\_packed [bt\_hfp\_ag\_call\_dir](group__bt__hfp__ag.md#ga019020ee2ed73c218f7dadf8371bf9a6) {

[ 93](group__bt__hfp__ag.md#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37) [BT\_HFP\_AG\_CALL\_DIR\_OUTGOING](group__bt__hfp__ag.md#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37) = 0, /\* It is a outgoing call \*/

[ 94](group__bt__hfp__ag.md#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55) [BT\_HFP\_AG\_CALL\_DIR\_INCOMING](group__bt__hfp__ag.md#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55) = 1, /\* It is a incoming call \*/

95};

96

[ 104](structbt__hfp__ag__ongoing__call.md)struct [bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md) {

[ 105](structbt__hfp__ag__ongoing__call.md#a1e5800a9c0f37539d0505d3223a35e2f) char [number](structbt__hfp__ag__ongoing__call.md#a1e5800a9c0f37539d0505d3223a35e2f)[CONFIG\_BT\_HFP\_AG\_PHONE\_NUMBER\_MAX\_LEN + 1];

[ 106](structbt__hfp__ag__ongoing__call.md#a26a77093f5aace7dd2d5693f4cb82189) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hfp__ag__ongoing__call.md#a26a77093f5aace7dd2d5693f4cb82189);

[ 107](structbt__hfp__ag__ongoing__call.md#a506610c17544daf8a0238a2c4d285526) enum [bt\_hfp\_ag\_call\_dir](group__bt__hfp__ag.md#ga019020ee2ed73c218f7dadf8371bf9a6) [dir](structbt__hfp__ag__ongoing__call.md#a506610c17544daf8a0238a2c4d285526);

[ 108](structbt__hfp__ag__ongoing__call.md#ac865f464436c3e73561fa8f6fcf09947) enum [bt\_hfp\_ag\_call\_status](group__bt__hfp__ag.md#gad2220b4a470cb3d537cf09492847568e) [status](structbt__hfp__ag__ongoing__call.md#ac865f464436c3e73561fa8f6fcf09947);

109};

110

[ 112](structbt__hfp__ag__cb.md)struct [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) {

[ 121](structbt__hfp__ag__cb.md#ab9506172c5b23bf97b5d59ddaddd7282) void (\*[connected](structbt__hfp__ag__cb.md#ab9506172c5b23bf97b5d59ddaddd7282))(struct bt\_conn \*conn, struct bt\_hfp\_ag \*ag);

[ 130](structbt__hfp__ag__cb.md#af9c53ab021dbbf1017d71895581960c4) void (\*[disconnected](structbt__hfp__ag__cb.md#af9c53ab021dbbf1017d71895581960c4))(struct bt\_hfp\_ag \*ag);

[ 139](structbt__hfp__ag__cb.md#aac2b1ff4d80361e0e5eea2481027b4cf) void (\*[sco\_connected](structbt__hfp__ag__cb.md#aac2b1ff4d80361e0e5eea2481027b4cf))(struct bt\_hfp\_ag \*ag, struct bt\_conn \*sco\_conn);

[ 148](structbt__hfp__ag__cb.md#a95600361e59a516f220a314e920c5858) void (\*[sco\_disconnected](structbt__hfp__ag__cb.md#a95600361e59a516f220a314e920c5858))(struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

149

[ 168](structbt__hfp__ag__cb.md#ac3771d39b8f1982514bbb23fc7773468) int (\*[get\_ongoing\_call](structbt__hfp__ag__cb.md#ac3771d39b8f1982514bbb23fc7773468))(struct bt\_hfp\_ag \*ag);

169

[ 182](structbt__hfp__ag__cb.md#af335450c5e63139485fa5a131814d650) int (\*[memory\_dial](structbt__hfp__ag__cb.md#af335450c5e63139485fa5a131814d650))(struct bt\_hfp\_ag \*ag, const char \*location, char \*\*number);

183

[ 198](structbt__hfp__ag__cb.md#a98c497e706ed5fcfe6fd308741893e91) int (\*[number\_call](structbt__hfp__ag__cb.md#a98c497e706ed5fcfe6fd308741893e91))(struct bt\_hfp\_ag \*ag, const char \*number);

199

[ 209](structbt__hfp__ag__cb.md#a8946de63ef24bbbc69e285abe2d141c1) void (\*[outgoing](structbt__hfp__ag__cb.md#a8946de63ef24bbbc69e285abe2d141c1))(struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_call \*call, const char \*number);

210

[ 220](structbt__hfp__ag__cb.md#aa0a4ab5aad6557a786ccf2f6861b932c) void (\*[incoming](structbt__hfp__ag__cb.md#aa0a4ab5aad6557a786ccf2f6861b932c))(struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_call \*call, const char \*number);

221

[ 229](structbt__hfp__ag__cb.md#a5b9f1c48e15a74b052678c491a592a5f) void (\*[incoming\_held](structbt__hfp__ag__cb.md#a5b9f1c48e15a74b052678c491a592a5f))(struct bt\_hfp\_ag\_call \*call);

230

[ 239](structbt__hfp__ag__cb.md#a0b8967f487d64556851420b2f4e059fe) void (\*[ringing](structbt__hfp__ag__cb.md#a0b8967f487d64556851420b2f4e059fe))(struct bt\_hfp\_ag\_call \*call, bool in\_band);

240

[ 248](structbt__hfp__ag__cb.md#a7da69bf1f5b85130ce2656c4915ba6d8) void (\*[accept](structbt__hfp__ag__cb.md#a7da69bf1f5b85130ce2656c4915ba6d8))(struct bt\_hfp\_ag\_call \*call);

249

[ 257](structbt__hfp__ag__cb.md#abe78441b0f01acd72713c7658f4e0274) void (\*[held](structbt__hfp__ag__cb.md#abe78441b0f01acd72713c7658f4e0274))(struct bt\_hfp\_ag\_call \*call);

258

[ 266](structbt__hfp__ag__cb.md#a9d6b978f82de6ded48881a87eb90aebb) void (\*[retrieve](structbt__hfp__ag__cb.md#a9d6b978f82de6ded48881a87eb90aebb))(struct bt\_hfp\_ag\_call \*call);

267

[ 275](structbt__hfp__ag__cb.md#abe1b5d71279c2e3292b3b90043d75224) void (\*[reject](structbt__hfp__ag__cb.md#abe1b5d71279c2e3292b3b90043d75224))(struct bt\_hfp\_ag\_call \*call);

276

[ 284](structbt__hfp__ag__cb.md#adf9960da8a3f4c38f7fcd60501522462) void (\*[terminate](structbt__hfp__ag__cb.md#adf9960da8a3f4c38f7fcd60501522462))(struct bt\_hfp\_ag\_call \*call);

285

[ 293](structbt__hfp__ag__cb.md#a2f15172060cc5d225894be5c8311610b) void (\*[codec](structbt__hfp__ag__cb.md#a2f15172060cc5d225894be5c8311610b))(struct bt\_hfp\_ag \*ag, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ids);

294

[ 303](structbt__hfp__ag__cb.md#a82abcad15f921fb0c99cc705e139aac1) void (\*[codec\_negotiate](structbt__hfp__ag__cb.md#a82abcad15f921fb0c99cc705e139aac1))(struct bt\_hfp\_ag \*ag, int err);

304

[ 320](structbt__hfp__ag__cb.md#a390377048e8623889515f2c6b6be0874) void (\*[audio\_connect\_req](structbt__hfp__ag__cb.md#a390377048e8623889515f2c6b6be0874))(struct bt\_hfp\_ag \*ag);

321

[ 330](structbt__hfp__ag__cb.md#aaad37582866c420ee41c3f730de16eb4) void (\*[vgm](structbt__hfp__ag__cb.md#aaad37582866c420ee41c3f730de16eb4))(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain);

331

[ 340](structbt__hfp__ag__cb.md#a38adb040dee9abd794f952322bf3d615) void (\*[vgs](structbt__hfp__ag__cb.md#a38adb040dee9abd794f952322bf3d615))(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain);

341

[ 352](structbt__hfp__ag__cb.md#ac3c09ffe392e167dd5aae82e740b5050) void (\*[ecnr\_turn\_off](structbt__hfp__ag__cb.md#ac3c09ffe392e167dd5aae82e740b5050))(struct bt\_hfp\_ag \*ag);

353

[ 369](structbt__hfp__ag__cb.md#ac06c1ddfa5cdc4ecb81a838e32299c8a) void (\*[explicit\_call\_transfer](structbt__hfp__ag__cb.md#ac06c1ddfa5cdc4ecb81a838e32299c8a))(struct bt\_hfp\_ag \*ag);

370

[ 387](structbt__hfp__ag__cb.md#a16c528018a2e9e97320df885c049454f) void (\*[voice\_recognition](structbt__hfp__ag__cb.md#a16c528018a2e9e97320df885c049454f))(struct bt\_hfp\_ag \*ag, bool activate);

388

[ 405](structbt__hfp__ag__cb.md#ad9925958c87b164113f607bd680ce2c3) void (\*[ready\_to\_accept\_audio](structbt__hfp__ag__cb.md#ad9925958c87b164113f607bd680ce2c3))(struct bt\_hfp\_ag \*ag);

406

[ 423](structbt__hfp__ag__cb.md#aecc8cdaf372d93f9cb531604f9b82d65) int (\*[request\_phone\_number](structbt__hfp__ag__cb.md#aecc8cdaf372d93f9cb531604f9b82d65))(struct bt\_hfp\_ag \*ag, char \*\*number);

424

[ 436](structbt__hfp__ag__cb.md#ad690d69c9786c69ad85e005e778b316c) void (\*[transmit\_dtmf\_code](structbt__hfp__ag__cb.md#ad690d69c9786c69ad85e005e778b316c))(struct bt\_hfp\_ag \*ag, char code);

437

[ 448](structbt__hfp__ag__cb.md#a976016f32e462daf38cd6d24ba18ff3d) int (\*[subscriber\_number](structbt__hfp__ag__cb.md#a976016f32e462daf38cd6d24ba18ff3d))(struct bt\_hfp\_ag \*ag, [bt\_hfp\_ag\_query\_subscriber\_func\_t](group__bt__hfp__ag.md#ga8e9b485f7ea0b9e16d96f578cdc587c3) func);

449

[ 461](structbt__hfp__ag__cb.md#a965d39254b75668f968d9a2bb5cffeba) void (\*[hf\_indicator\_value](structbt__hfp__ag__cb.md#a965d39254b75668f968d9a2bb5cffeba))(struct bt\_hfp\_ag \*ag, enum [hfp\_ag\_hf\_indicators](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403) indicator,

462 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

463};

464

[ 474](group__bt__hfp__ag.md#ga379ec1c540195549fc59417d8d1ce7e5)int [bt\_hfp\_ag\_register](group__bt__hfp__ag.md#ga379ec1c540195549fc59417d8d1ce7e5)(struct [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) \*cb);

475

[ 486](group__bt__hfp__ag.md#ga5b602810558268396f0cb64adcb0d014)int [bt\_hfp\_ag\_connect](group__bt__hfp__ag.md#ga5b602810558268396f0cb64adcb0d014)(struct bt\_conn \*conn, struct bt\_hfp\_ag \*\*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

487

[ 496](group__bt__hfp__ag.md#gadf0b4aef701cf0986ea9599ad79d451a)int [bt\_hfp\_ag\_disconnect](group__bt__hfp__ag.md#gadf0b4aef701cf0986ea9599ad79d451a)(struct bt\_hfp\_ag \*ag);

497

[ 507](group__bt__hfp__ag.md#ga443cd2928686f222d61f06c7477ea793)int [bt\_hfp\_ag\_remote\_incoming](group__bt__hfp__ag.md#ga443cd2928686f222d61f06c7477ea793)(struct bt\_hfp\_ag \*ag, const char \*number);

508

[ 517](group__bt__hfp__ag.md#gab288d6e6b45a24b706328da58ca43a3b)int [bt\_hfp\_ag\_hold\_incoming](group__bt__hfp__ag.md#gab288d6e6b45a24b706328da58ca43a3b)(struct bt\_hfp\_ag\_call \*call);

518

[ 527](group__bt__hfp__ag.md#ga195daffc37f1a3f210ba52dae1a9c4c2)int [bt\_hfp\_ag\_reject](group__bt__hfp__ag.md#ga195daffc37f1a3f210ba52dae1a9c4c2)(struct bt\_hfp\_ag\_call \*call);

528

[ 537](group__bt__hfp__ag.md#ga351e1b78b8c19c3971554fabb331e5c6)int [bt\_hfp\_ag\_accept](group__bt__hfp__ag.md#ga351e1b78b8c19c3971554fabb331e5c6)(struct bt\_hfp\_ag\_call \*call);

538

[ 547](group__bt__hfp__ag.md#ga2f2e85a6076930ed87bc0727c75209a9)int [bt\_hfp\_ag\_terminate](group__bt__hfp__ag.md#ga2f2e85a6076930ed87bc0727c75209a9)(struct bt\_hfp\_ag\_call \*call);

548

[ 557](group__bt__hfp__ag.md#ga405fcf8e03bac39bd5b0e7bf2766045f)int [bt\_hfp\_ag\_retrieve](group__bt__hfp__ag.md#ga405fcf8e03bac39bd5b0e7bf2766045f)(struct bt\_hfp\_ag\_call \*call);

558

[ 567](group__bt__hfp__ag.md#ga4bbcec3ed5394e965aa7404dc968b94d)int [bt\_hfp\_ag\_hold](group__bt__hfp__ag.md#ga4bbcec3ed5394e965aa7404dc968b94d)(struct bt\_hfp\_ag\_call \*call);

568

[ 578](group__bt__hfp__ag.md#ga580328104cf990c6f9e0a64642c16ebd)int [bt\_hfp\_ag\_outgoing](group__bt__hfp__ag.md#ga580328104cf990c6f9e0a64642c16ebd)(struct bt\_hfp\_ag \*ag, const char \*number);

579

[ 588](group__bt__hfp__ag.md#ga0a12a56baa25e2aea101a387fcccb88e)int [bt\_hfp\_ag\_remote\_ringing](group__bt__hfp__ag.md#ga0a12a56baa25e2aea101a387fcccb88e)(struct bt\_hfp\_ag\_call \*call);

589

[ 598](group__bt__hfp__ag.md#gacb1b361e6b0a441102f7ccd641eb3e6b)int [bt\_hfp\_ag\_remote\_reject](group__bt__hfp__ag.md#gacb1b361e6b0a441102f7ccd641eb3e6b)(struct bt\_hfp\_ag\_call \*call);

599

[ 608](group__bt__hfp__ag.md#ga018d8ed8912f9dcef8c5fa37ac2bd889)int [bt\_hfp\_ag\_remote\_accept](group__bt__hfp__ag.md#ga018d8ed8912f9dcef8c5fa37ac2bd889)(struct bt\_hfp\_ag\_call \*call);

609

[ 618](group__bt__hfp__ag.md#ga525085c7c75e412ca43ba8b23cbc0c3d)int [bt\_hfp\_ag\_remote\_terminate](group__bt__hfp__ag.md#ga525085c7c75e412ca43ba8b23cbc0c3d)(struct bt\_hfp\_ag\_call \*call);

619

[ 631](group__bt__hfp__ag.md#ga5e249248a52d7c95c9d3f3f852bf2314)int [bt\_hfp\_ag\_explicit\_call\_transfer](group__bt__hfp__ag.md#ga5e249248a52d7c95c9d3f3f852bf2314)(struct bt\_hfp\_ag \*ag);

632

[ 642](group__bt__hfp__ag.md#ga53778bd332c95fa4357d254f5ef125a2)int [bt\_hfp\_ag\_vgm](group__bt__hfp__ag.md#ga53778bd332c95fa4357d254f5ef125a2)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vgm);

643

[ 653](group__bt__hfp__ag.md#gabdad8c764c91e133598584d741ed9d4b)int [bt\_hfp\_ag\_vgs](group__bt__hfp__ag.md#gabdad8c764c91e133598584d741ed9d4b)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vgs);

654

[ 668](group__bt__hfp__ag.md#gaaf066dce38c028254b6c1880bcebaa13)int [bt\_hfp\_ag\_set\_operator](group__bt__hfp__ag.md#gaaf066dce38c028254b6c1880bcebaa13)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, char \*name);

669

[ 690](group__bt__hfp__ag.md#ga542a1754a16e32a9b2651f1230aa7066)int [bt\_hfp\_ag\_audio\_connect](group__bt__hfp__ag.md#ga542a1754a16e32a9b2651f1230aa7066)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id);

691

[ 701](group__bt__hfp__ag.md#ga881ea4d3cc732fb5d804df203dde7746)int [bt\_hfp\_ag\_inband\_ringtone](group__bt__hfp__ag.md#ga881ea4d3cc732fb5d804df203dde7746)(struct bt\_hfp\_ag \*ag, bool inband);

702

[ 714](group__bt__hfp__ag.md#ga28682fc5d8cfee9c0adece68bcb94c3f)int [bt\_hfp\_ag\_voice\_recognition](group__bt__hfp__ag.md#ga28682fc5d8cfee9c0adece68bcb94c3f)(struct bt\_hfp\_ag \*ag, bool activate);

715

[ 733](group__bt__hfp__ag.md#ga3668f3997afe9ab678f9eb2e6faf324d)int [bt\_hfp\_ag\_vre\_state](group__bt__hfp__ag.md#ga3668f3997afe9ab678f9eb2e6faf324d)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

734

[ 775](group__bt__hfp__ag.md#ga4e71364283448c7c5d3306c111aa167d)int [bt\_hfp\_ag\_vre\_textual\_representation](group__bt__hfp__ag.md#ga4e71364283448c7c5d3306c111aa167d)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const char \*id,

776 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) operation, const char \*text);

777

[ 787](group__bt__hfp__ag.md#ga20ef1240e0ff72d914405b259cc3164f)int [bt\_hfp\_ag\_signal\_strength](group__bt__hfp__ag.md#ga20ef1240e0ff72d914405b259cc3164f)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) strength);

788

[ 798](group__bt__hfp__ag.md#ga0f8b2e463aefbf74b26ac4f27033486c)int [bt\_hfp\_ag\_roaming\_status](group__bt__hfp__ag.md#ga0f8b2e463aefbf74b26ac4f27033486c)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

799

[ 809](group__bt__hfp__ag.md#ga4da632e9775051df6a5b5010fd3806df)int [bt\_hfp\_ag\_battery\_level](group__bt__hfp__ag.md#ga4da632e9775051df6a5b5010fd3806df)(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

810

[ 820](group__bt__hfp__ag.md#gaf838e54046c380931f23a59919ccfa5b)int [bt\_hfp\_ag\_service\_availability](group__bt__hfp__ag.md#gaf838e54046c380931f23a59919ccfa5b)(struct bt\_hfp\_ag \*ag, bool available);

821

[ 843](group__bt__hfp__ag.md#gaacc2df6144e1a33b13635855fe74f1f1)int [bt\_hfp\_ag\_hf\_indicator](group__bt__hfp__ag.md#gaacc2df6144e1a33b13635855fe74f1f1)(struct bt\_hfp\_ag \*ag, enum [hfp\_ag\_hf\_indicators](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403) indicator, bool enable);

844

[ 855](group__bt__hfp__ag.md#ga5614bf3f1de11959a0364f458523e06e)int [bt\_hfp\_ag\_ongoing\_calls](group__bt__hfp__ag.md#ga5614bf3f1de11959a0364f458523e06e)(struct bt\_hfp\_ag \*ag, struct [bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md) \*calls,

856 size\_t count);

857

858#ifdef \_\_cplusplus

859}

860#endif

861

865

866#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_HF\_H\_ \*/

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_hfp\_ag\_remote\_accept](group__bt__hfp__ag.md#ga018d8ed8912f9dcef8c5fa37ac2bd889)

int bt\_hfp\_ag\_remote\_accept(struct bt\_hfp\_ag\_call \*call)

Notify HFP Unit that the remote accepts the call.

[bt\_hfp\_ag\_call\_dir](group__bt__hfp__ag.md#ga019020ee2ed73c218f7dadf8371bf9a6)

bt\_hfp\_ag\_call\_dir

**Definition** hfp\_ag.h:92

[hfp\_ag\_hf\_indicators](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403)

hfp\_ag\_hf\_indicators

**Definition** hfp\_ag.h:75

[bt\_hfp\_ag\_remote\_ringing](group__bt__hfp__ag.md#ga0a12a56baa25e2aea101a387fcccb88e)

int bt\_hfp\_ag\_remote\_ringing(struct bt\_hfp\_ag\_call \*call)

Notify HFP Unit that the remote starts ringing.

[bt\_hfp\_ag\_roaming\_status](group__bt__hfp__ag.md#ga0f8b2e463aefbf74b26ac4f27033486c)

int bt\_hfp\_ag\_roaming\_status(struct bt\_hfp\_ag \*ag, uint8\_t status)

Set roaming status.

[bt\_hfp\_ag\_reject](group__bt__hfp__ag.md#ga195daffc37f1a3f210ba52dae1a9c4c2)

int bt\_hfp\_ag\_reject(struct bt\_hfp\_ag\_call \*call)

Reject the incoming call.

[bt\_hfp\_ag\_signal\_strength](group__bt__hfp__ag.md#ga20ef1240e0ff72d914405b259cc3164f)

int bt\_hfp\_ag\_signal\_strength(struct bt\_hfp\_ag \*ag, uint8\_t strength)

Set signal strength.

[bt\_hfp\_ag\_voice\_recognition](group__bt__hfp__ag.md#ga28682fc5d8cfee9c0adece68bcb94c3f)

int bt\_hfp\_ag\_voice\_recognition(struct bt\_hfp\_ag \*ag, bool activate)

Enable/disable the voice recognition function.

[bt\_hfp\_ag\_terminate](group__bt__hfp__ag.md#ga2f2e85a6076930ed87bc0727c75209a9)

int bt\_hfp\_ag\_terminate(struct bt\_hfp\_ag\_call \*call)

Terminate the active/hold call.

[bt\_hfp\_ag\_accept](group__bt__hfp__ag.md#ga351e1b78b8c19c3971554fabb331e5c6)

int bt\_hfp\_ag\_accept(struct bt\_hfp\_ag\_call \*call)

Accept the incoming call.

[bt\_hfp\_ag\_vre\_state](group__bt__hfp__ag.md#ga3668f3997afe9ab678f9eb2e6faf324d)

int bt\_hfp\_ag\_vre\_state(struct bt\_hfp\_ag \*ag, uint8\_t state)

set voice recognition engine state

[bt\_hfp\_ag\_indicator](group__bt__hfp__ag.md#ga37640efdcc737bfa0390df889a62f810)

bt\_hfp\_ag\_indicator

**Definition** hfp\_ag.h:28

[bt\_hfp\_ag\_register](group__bt__hfp__ag.md#ga379ec1c540195549fc59417d8d1ce7e5)

int bt\_hfp\_ag\_register(struct bt\_hfp\_ag\_cb \*cb)

Register HFP AG profile.

[bt\_hfp\_ag\_retrieve](group__bt__hfp__ag.md#ga405fcf8e03bac39bd5b0e7bf2766045f)

int bt\_hfp\_ag\_retrieve(struct bt\_hfp\_ag\_call \*call)

Retrieve the held call.

[bt\_hfp\_ag\_remote\_incoming](group__bt__hfp__ag.md#ga443cd2928686f222d61f06c7477ea793)

int bt\_hfp\_ag\_remote\_incoming(struct bt\_hfp\_ag \*ag, const char \*number)

Notify HFP Unit of an incoming call.

[bt\_hfp\_ag\_hold](group__bt__hfp__ag.md#ga4bbcec3ed5394e965aa7404dc968b94d)

int bt\_hfp\_ag\_hold(struct bt\_hfp\_ag\_call \*call)

Hold the active call.

[bt\_hfp\_ag\_battery\_level](group__bt__hfp__ag.md#ga4da632e9775051df6a5b5010fd3806df)

int bt\_hfp\_ag\_battery\_level(struct bt\_hfp\_ag \*ag, uint8\_t level)

Set battery level.

[bt\_hfp\_ag\_vre\_textual\_representation](group__bt__hfp__ag.md#ga4e71364283448c7c5d3306c111aa167d)

int bt\_hfp\_ag\_vre\_textual\_representation(struct bt\_hfp\_ag \*ag, uint8\_t state, const char \*id, uint8\_t type, uint8\_t operation, const char \*text)

set voice recognition engine state and textual representation

[bt\_hfp\_ag\_remote\_terminate](group__bt__hfp__ag.md#ga525085c7c75e412ca43ba8b23cbc0c3d)

int bt\_hfp\_ag\_remote\_terminate(struct bt\_hfp\_ag\_call \*call)

Notify HFP Unit that the remote terminates the active/hold call.

[bt\_hfp\_ag\_vgm](group__bt__hfp__ag.md#ga53778bd332c95fa4357d254f5ef125a2)

int bt\_hfp\_ag\_vgm(struct bt\_hfp\_ag \*ag, uint8\_t vgm)

Set the HF microphone gain.

[bt\_hfp\_ag\_audio\_connect](group__bt__hfp__ag.md#ga542a1754a16e32a9b2651f1230aa7066)

int bt\_hfp\_ag\_audio\_connect(struct bt\_hfp\_ag \*ag, uint8\_t id)

Create audio connection.

[bt\_hfp\_ag\_ongoing\_calls](group__bt__hfp__ag.md#ga5614bf3f1de11959a0364f458523e06e)

int bt\_hfp\_ag\_ongoing\_calls(struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_ongoing\_call \*calls, size\_t count)

Set the ongoing calls.

[bt\_hfp\_ag\_outgoing](group__bt__hfp__ag.md#ga580328104cf990c6f9e0a64642c16ebd)

int bt\_hfp\_ag\_outgoing(struct bt\_hfp\_ag \*ag, const char \*number)

Dial a call.

[bt\_hfp\_ag\_connect](group__bt__hfp__ag.md#ga5b602810558268396f0cb64adcb0d014)

int bt\_hfp\_ag\_connect(struct bt\_conn \*conn, struct bt\_hfp\_ag \*\*ag, uint8\_t channel)

Create the hfp ag session.

[bt\_hfp\_ag\_explicit\_call\_transfer](group__bt__hfp__ag.md#ga5e249248a52d7c95c9d3f3f852bf2314)

int bt\_hfp\_ag\_explicit\_call\_transfer(struct bt\_hfp\_ag \*ag)

explicit call transfer

[bt\_hfp\_ag\_inband\_ringtone](group__bt__hfp__ag.md#ga881ea4d3cc732fb5d804df203dde7746)

int bt\_hfp\_ag\_inband\_ringtone(struct bt\_hfp\_ag \*ag, bool inband)

Set In-Band Ring Tone.

[bt\_hfp\_ag\_query\_subscriber\_func\_t](group__bt__hfp__ag.md#ga8e9b485f7ea0b9e16d96f578cdc587c3)

int(\* bt\_hfp\_ag\_query\_subscriber\_func\_t)(struct bt\_hfp\_ag \*ag, char \*number, uint8\_t type, uint8\_t service)

Query subscriber number callback function.

**Definition** hfp\_ag.h:71

[bt\_hfp\_ag\_hf\_indicator](group__bt__hfp__ag.md#gaacc2df6144e1a33b13635855fe74f1f1)

int bt\_hfp\_ag\_hf\_indicator(struct bt\_hfp\_ag \*ag, enum hfp\_ag\_hf\_indicators indicator, bool enable)

Activate/deactivate HF indicator.

[bt\_hfp\_ag\_set\_operator](group__bt__hfp__ag.md#gaaf066dce38c028254b6c1880bcebaa13)

int bt\_hfp\_ag\_set\_operator(struct bt\_hfp\_ag \*ag, uint8\_t mode, char \*name)

Set currently network operator.

[bt\_hfp\_ag\_hold\_incoming](group__bt__hfp__ag.md#gab288d6e6b45a24b706328da58ca43a3b)

int bt\_hfp\_ag\_hold\_incoming(struct bt\_hfp\_ag\_call \*call)

Put the incoming call on hold.

[bt\_hfp\_ag\_vgs](group__bt__hfp__ag.md#gabdad8c764c91e133598584d741ed9d4b)

int bt\_hfp\_ag\_vgs(struct bt\_hfp\_ag \*ag, uint8\_t vgs)

Set the HF speaker gain.

[bt\_hfp\_ag\_remote\_reject](group__bt__hfp__ag.md#gacb1b361e6b0a441102f7ccd641eb3e6b)

int bt\_hfp\_ag\_remote\_reject(struct bt\_hfp\_ag\_call \*call)

Notify HFP Unit that the remote rejects the call.

[bt\_hfp\_ag\_call\_status](group__bt__hfp__ag.md#gad2220b4a470cb3d537cf09492847568e)

bt\_hfp\_ag\_call\_status

**Definition** hfp\_ag.h:81

[bt\_hfp\_ag\_disconnect](group__bt__hfp__ag.md#gadf0b4aef701cf0986ea9599ad79d451a)

int bt\_hfp\_ag\_disconnect(struct bt\_hfp\_ag \*ag)

Disconnect the hfp ag session.

[bt\_hfp\_ag\_service\_availability](group__bt__hfp__ag.md#gaf838e54046c380931f23a59919ccfa5b)

int bt\_hfp\_ag\_service\_availability(struct bt\_hfp\_ag \*ag, bool available)

Set service availability.

[BT\_HFP\_AG\_CALL\_DIR\_INCOMING](group__bt__hfp__ag.md#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55)

@ BT\_HFP\_AG\_CALL\_DIR\_INCOMING

**Definition** hfp\_ag.h:94

[BT\_HFP\_AG\_CALL\_DIR\_OUTGOING](group__bt__hfp__ag.md#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37)

@ BT\_HFP\_AG\_CALL\_DIR\_OUTGOING

**Definition** hfp\_ag.h:93

[HFP\_AG\_BATTERY\_LEVEL\_IND](group__bt__hfp__ag.md#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1)

@ HFP\_AG\_BATTERY\_LEVEL\_IND

**Definition** hfp\_ag.h:77

[HFP\_AG\_ENHANCED\_SAFETY\_IND](group__bt__hfp__ag.md#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f)

@ HFP\_AG\_ENHANCED\_SAFETY\_IND

**Definition** hfp\_ag.h:76

[BT\_HFP\_AG\_SERVICE\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234)

@ BT\_HFP\_AG\_SERVICE\_IND

**Definition** hfp\_ag.h:29

[BT\_HFP\_AG\_CALL\_SETUP\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5)

@ BT\_HFP\_AG\_CALL\_SETUP\_IND

**Definition** hfp\_ag.h:31

[BT\_HFP\_AG\_CALL\_HELD\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b)

@ BT\_HFP\_AG\_CALL\_HELD\_IND

**Definition** hfp\_ag.h:32

[BT\_HFP\_AG\_SIGNAL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493)

@ BT\_HFP\_AG\_SIGNAL\_IND

**Definition** hfp\_ag.h:33

[BT\_HFP\_AG\_BATTERY\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609)

@ BT\_HFP\_AG\_BATTERY\_IND

**Definition** hfp\_ag.h:35

[BT\_HFP\_AG\_CALL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d)

@ BT\_HFP\_AG\_CALL\_IND

**Definition** hfp\_ag.h:30

[BT\_HFP\_AG\_ROAM\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863)

@ BT\_HFP\_AG\_ROAM\_IND

**Definition** hfp\_ag.h:34

[BT\_HFP\_AG\_IND\_MAX](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)

@ BT\_HFP\_AG\_IND\_MAX

**Definition** hfp\_ag.h:36

[BT\_HFP\_AG\_CALL\_STATUS\_DIALING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963)

@ BT\_HFP\_AG\_CALL\_STATUS\_DIALING

**Definition** hfp\_ag.h:84

[BT\_HFP\_AG\_CALL\_STATUS\_INCOMING\_HELD](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542)

@ BT\_HFP\_AG\_CALL\_STATUS\_INCOMING\_HELD

**Definition** hfp\_ag.h:88

[BT\_HFP\_AG\_CALL\_STATUS\_ALERTING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae)

@ BT\_HFP\_AG\_CALL\_STATUS\_ALERTING

**Definition** hfp\_ag.h:85

[BT\_HFP\_AG\_CALL\_STATUS\_ACTIVE](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658)

@ BT\_HFP\_AG\_CALL\_STATUS\_ACTIVE

**Definition** hfp\_ag.h:82

[BT\_HFP\_AG\_CALL\_STATUS\_INCOMING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8)

@ BT\_HFP\_AG\_CALL\_STATUS\_INCOMING

**Definition** hfp\_ag.h:86

[BT\_HFP\_AG\_CALL\_STATUS\_WAITING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2)

@ BT\_HFP\_AG\_CALL\_STATUS\_WAITING

**Definition** hfp\_ag.h:87

[BT\_HFP\_AG\_CALL\_STATUS\_HELD](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2)

@ BT\_HFP\_AG\_CALL\_STATUS\_HELD

**Definition** hfp\_ag.h:83

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md)

HFP profile AG application callback.

**Definition** hfp\_ag.h:112

[bt\_hfp\_ag\_cb::ringing](structbt__hfp__ag__cb.md#a0b8967f487d64556851420b2f4e059fe)

void(\* ringing)(struct bt\_hfp\_ag\_call \*call, bool in\_band)

HF ringing Callback.

**Definition** hfp\_ag.h:239

[bt\_hfp\_ag\_cb::voice\_recognition](structbt__hfp__ag__cb.md#a16c528018a2e9e97320df885c049454f)

void(\* voice\_recognition)(struct bt\_hfp\_ag \*ag, bool activate)

Voice recognition activation/deactivation callback.

**Definition** hfp\_ag.h:387

[bt\_hfp\_ag\_cb::codec](structbt__hfp__ag__cb.md#a2f15172060cc5d225894be5c8311610b)

void(\* codec)(struct bt\_hfp\_ag \*ag, uint32\_t ids)

Supported codec Ids callback.

**Definition** hfp\_ag.h:293

[bt\_hfp\_ag\_cb::vgs](structbt__hfp__ag__cb.md#a38adb040dee9abd794f952322bf3d615)

void(\* vgs)(struct bt\_hfp\_ag \*ag, uint8\_t gain)

HF VGS setting callback.

**Definition** hfp\_ag.h:340

[bt\_hfp\_ag\_cb::audio\_connect\_req](structbt__hfp__ag__cb.md#a390377048e8623889515f2c6b6be0874)

void(\* audio\_connect\_req)(struct bt\_hfp\_ag \*ag)

Audio connection request callback.

**Definition** hfp\_ag.h:320

[bt\_hfp\_ag\_cb::incoming\_held](structbt__hfp__ag__cb.md#a5b9f1c48e15a74b052678c491a592a5f)

void(\* incoming\_held)(struct bt\_hfp\_ag\_call \*call)

HF incoming call is held Callback.

**Definition** hfp\_ag.h:229

[bt\_hfp\_ag\_cb::accept](structbt__hfp__ag__cb.md#a7da69bf1f5b85130ce2656c4915ba6d8)

void(\* accept)(struct bt\_hfp\_ag\_call \*call)

HF call accept Callback.

**Definition** hfp\_ag.h:248

[bt\_hfp\_ag\_cb::codec\_negotiate](structbt__hfp__ag__cb.md#a82abcad15f921fb0c99cc705e139aac1)

void(\* codec\_negotiate)(struct bt\_hfp\_ag \*ag, int err)

Codec negotiate callback.

**Definition** hfp\_ag.h:303

[bt\_hfp\_ag\_cb::outgoing](structbt__hfp__ag__cb.md#a8946de63ef24bbbc69e285abe2d141c1)

void(\* outgoing)(struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_call \*call, const char \*number)

HF outgoing Callback.

**Definition** hfp\_ag.h:209

[bt\_hfp\_ag\_cb::sco\_disconnected](structbt__hfp__ag__cb.md#a95600361e59a516f220a314e920c5858)

void(\* sco\_disconnected)(struct bt\_conn \*sco\_conn, uint8\_t reason)

HF SCO/eSCO disconnected Callback.

**Definition** hfp\_ag.h:148

[bt\_hfp\_ag\_cb::hf\_indicator\_value](structbt__hfp__ag__cb.md#a965d39254b75668f968d9a2bb5cffeba)

void(\* hf\_indicator\_value)(struct bt\_hfp\_ag \*ag, enum hfp\_ag\_hf\_indicators indicator, uint32\_t value)

HF indicator value callback.

**Definition** hfp\_ag.h:461

[bt\_hfp\_ag\_cb::subscriber\_number](structbt__hfp__ag__cb.md#a976016f32e462daf38cd6d24ba18ff3d)

int(\* subscriber\_number)(struct bt\_hfp\_ag \*ag, bt\_hfp\_ag\_query\_subscriber\_func\_t func)

Get subscriber number callback.

**Definition** hfp\_ag.h:448

[bt\_hfp\_ag\_cb::number\_call](structbt__hfp__ag__cb.md#a98c497e706ed5fcfe6fd308741893e91)

int(\* number\_call)(struct bt\_hfp\_ag \*ag, const char \*number)

HF phone number calling request Callback.

**Definition** hfp\_ag.h:198

[bt\_hfp\_ag\_cb::retrieve](structbt__hfp__ag__cb.md#a9d6b978f82de6ded48881a87eb90aebb)

void(\* retrieve)(struct bt\_hfp\_ag\_call \*call)

HF call retrieve Callback.

**Definition** hfp\_ag.h:266

[bt\_hfp\_ag\_cb::incoming](structbt__hfp__ag__cb.md#aa0a4ab5aad6557a786ccf2f6861b932c)

void(\* incoming)(struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_call \*call, const char \*number)

HF incoming Callback.

**Definition** hfp\_ag.h:220

[bt\_hfp\_ag\_cb::vgm](structbt__hfp__ag__cb.md#aaad37582866c420ee41c3f730de16eb4)

void(\* vgm)(struct bt\_hfp\_ag \*ag, uint8\_t gain)

HF VGM setting callback.

**Definition** hfp\_ag.h:330

[bt\_hfp\_ag\_cb::sco\_connected](structbt__hfp__ag__cb.md#aac2b1ff4d80361e0e5eea2481027b4cf)

void(\* sco\_connected)(struct bt\_hfp\_ag \*ag, struct bt\_conn \*sco\_conn)

HF SCO/eSCO connected Callback.

**Definition** hfp\_ag.h:139

[bt\_hfp\_ag\_cb::connected](structbt__hfp__ag__cb.md#ab9506172c5b23bf97b5d59ddaddd7282)

void(\* connected)(struct bt\_conn \*conn, struct bt\_hfp\_ag \*ag)

HF AG connected callback to application.

**Definition** hfp\_ag.h:121

[bt\_hfp\_ag\_cb::reject](structbt__hfp__ag__cb.md#abe1b5d71279c2e3292b3b90043d75224)

void(\* reject)(struct bt\_hfp\_ag\_call \*call)

HF call reject Callback.

**Definition** hfp\_ag.h:275

[bt\_hfp\_ag\_cb::held](structbt__hfp__ag__cb.md#abe78441b0f01acd72713c7658f4e0274)

void(\* held)(struct bt\_hfp\_ag\_call \*call)

HF call held Callback.

**Definition** hfp\_ag.h:257

[bt\_hfp\_ag\_cb::explicit\_call\_transfer](structbt__hfp__ag__cb.md#ac06c1ddfa5cdc4ecb81a838e32299c8a)

void(\* explicit\_call\_transfer)(struct bt\_hfp\_ag \*ag)

HF explicit call transfer callback.

**Definition** hfp\_ag.h:369

[bt\_hfp\_ag\_cb::get\_ongoing\_call](structbt__hfp__ag__cb.md#ac3771d39b8f1982514bbb23fc7773468)

int(\* get\_ongoing\_call)(struct bt\_hfp\_ag \*ag)

Get ongoing call information Callback.

**Definition** hfp\_ag.h:168

[bt\_hfp\_ag\_cb::ecnr\_turn\_off](structbt__hfp__ag__cb.md#ac3c09ffe392e167dd5aae82e740b5050)

void(\* ecnr\_turn\_off)(struct bt\_hfp\_ag \*ag)

HF ECNR turns off callback.

**Definition** hfp\_ag.h:352

[bt\_hfp\_ag\_cb::transmit\_dtmf\_code](structbt__hfp__ag__cb.md#ad690d69c9786c69ad85e005e778b316c)

void(\* transmit\_dtmf\_code)(struct bt\_hfp\_ag \*ag, char code)

Transmit a DTMF Code callback.

**Definition** hfp\_ag.h:436

[bt\_hfp\_ag\_cb::ready\_to\_accept\_audio](structbt__hfp__ag__cb.md#ad9925958c87b164113f607bd680ce2c3)

void(\* ready\_to\_accept\_audio)(struct bt\_hfp\_ag \*ag)

Ready to accept audio callback.

**Definition** hfp\_ag.h:405

[bt\_hfp\_ag\_cb::terminate](structbt__hfp__ag__cb.md#adf9960da8a3f4c38f7fcd60501522462)

void(\* terminate)(struct bt\_hfp\_ag\_call \*call)

HF call terminate Callback.

**Definition** hfp\_ag.h:284

[bt\_hfp\_ag\_cb::request\_phone\_number](structbt__hfp__ag__cb.md#aecc8cdaf372d93f9cb531604f9b82d65)

int(\* request\_phone\_number)(struct bt\_hfp\_ag \*ag, char \*\*number)

Request phone number callback.

**Definition** hfp\_ag.h:423

[bt\_hfp\_ag\_cb::memory\_dial](structbt__hfp__ag__cb.md#af335450c5e63139485fa5a131814d650)

int(\* memory\_dial)(struct bt\_hfp\_ag \*ag, const char \*location, char \*\*number)

HF memory dialing request Callback.

**Definition** hfp\_ag.h:182

[bt\_hfp\_ag\_cb::disconnected](structbt__hfp__ag__cb.md#af9c53ab021dbbf1017d71895581960c4)

void(\* disconnected)(struct bt\_hfp\_ag \*ag)

HF disconnected callback to application.

**Definition** hfp\_ag.h:130

[bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md)

The ongoing call.

**Definition** hfp\_ag.h:104

[bt\_hfp\_ag\_ongoing\_call::number](structbt__hfp__ag__ongoing__call.md#a1e5800a9c0f37539d0505d3223a35e2f)

char number[CONFIG\_BT\_HFP\_AG\_PHONE\_NUMBER\_MAX\_LEN+1]

**Definition** hfp\_ag.h:105

[bt\_hfp\_ag\_ongoing\_call::type](structbt__hfp__ag__ongoing__call.md#a26a77093f5aace7dd2d5693f4cb82189)

uint8\_t type

**Definition** hfp\_ag.h:106

[bt\_hfp\_ag\_ongoing\_call::dir](structbt__hfp__ag__ongoing__call.md#a506610c17544daf8a0238a2c4d285526)

enum bt\_hfp\_ag\_call\_dir dir

**Definition** hfp\_ag.h:107

[bt\_hfp\_ag\_ongoing\_call::status](structbt__hfp__ag__ongoing__call.md#ac865f464436c3e73561fa8f6fcf09947)

enum bt\_hfp\_ag\_call\_status status

**Definition** hfp\_ag.h:108

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [hfp\_ag.h](hfp__ag_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
