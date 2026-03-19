---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/access_8h_source.html
original_path: doxygen/html/access_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

access.h

[Go to the documentation of this file.](access_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_ACCESS\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_ACCESS\_H\_

12

13#include <[zephyr/sys/util.h](sys_2util_8h.md)>

14#include <[zephyr/settings/settings.h](settings_8h.md)>

15#include <[zephyr/bluetooth/mesh/msg.h](msg_8h.md)>

16

17/\* Internal macros used to initialize array members \*/

[ 18](access_8h.md#abe51f11257cf1bbb236e899e7a23acbc)#define BT\_MESH\_KEY\_UNUSED\_ELT\_(IDX, \_) BT\_MESH\_KEY\_UNUSED

[ 19](access_8h.md#a421f6ac3aa620d77033a98f3d059e3ce)#define BT\_MESH\_ADDR\_UNASSIGNED\_ELT\_(IDX, \_) BT\_MESH\_ADDR\_UNASSIGNED

[ 20](access_8h.md#aa5b0403118f5fd434e2ca9c298aee1fd)#define BT\_MESH\_UUID\_UNASSIGNED\_ELT\_(IDX, \_) NULL

[ 21](access_8h.md#a575258fd6073a81b8037b6127f6b975a)#define BT\_MESH\_MODEL\_KEYS\_UNUSED(\_keys) \

22 { LISTIFY(\_keys, BT\_MESH\_KEY\_UNUSED\_ELT\_, (,)) }

[ 23](access_8h.md#a6023b10a0b89e067d68e8393155a2945)#define BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED(\_grps) \

24 { LISTIFY(\_grps, BT\_MESH\_ADDR\_UNASSIGNED\_ELT\_, (,)) }

25#if CONFIG\_BT\_MESH\_LABEL\_COUNT > 0

26#define BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED() \

27 .uuids = (const uint8\_t \*[]){ LISTIFY(CONFIG\_BT\_MESH\_LABEL\_COUNT, \

28 BT\_MESH\_UUID\_UNASSIGNED\_ELT\_, (,)) },

29#else

[ 30](access_8h.md#abf60c1897454c0cbfa034bc4a3c92843)#define BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED()

31#endif

32

[ 33](access_8h.md#ad28c5301ea6cf93f3bf2a672043cae4e)#define BT\_MESH\_MODEL\_RUNTIME\_INIT(\_user\_data) \

34 .rt = &(struct bt\_mesh\_model\_rt\_ctx){ .user\_data = (\_user\_data) },

35

42

43#ifdef \_\_cplusplus

44extern "C" {

45#endif

46

[ 51](group__bt__mesh__access.md#ga6d11790af686e6d48f08c6f1cd65317c)#define BT\_MESH\_ADDR\_UNASSIGNED 0x0000

[ 52](group__bt__mesh__access.md#ga27aafd100b6ccc1de060a75370184620)#define BT\_MESH\_ADDR\_ALL\_NODES 0xffff

[ 53](group__bt__mesh__access.md#ga5ee81d48846de9c9c966ffe0b90ff011)#define BT\_MESH\_ADDR\_RELAYS 0xfffe

[ 54](group__bt__mesh__access.md#ga5d44892368bb7c1ecd205a81e66bd6f7)#define BT\_MESH\_ADDR\_FRIENDS 0xfffd

[ 55](group__bt__mesh__access.md#ga30d4975d25c2c120da1cbfadf29c098f)#define BT\_MESH\_ADDR\_PROXIES 0xfffc

[ 56](group__bt__mesh__access.md#gabf77d8365ddc278838fa450826e43243)#define BT\_MESH\_ADDR\_DFW\_NODES 0xfffb

[ 57](group__bt__mesh__access.md#gafd70174e5072dbbfed31156f152aeaa1)#define BT\_MESH\_ADDR\_IP\_NODES 0xfffa

[ 58](group__bt__mesh__access.md#ga1055381438e55e953dec2e6d592ab103)#define BT\_MESH\_ADDR\_IP\_BR\_ROUTERS 0xfff9

62

[ 67](group__bt__mesh__access.md#gace23095bac3705c2f2afab749e48c02d)#define BT\_MESH\_KEY\_UNUSED 0xffff

[ 68](group__bt__mesh__access.md#ga7718cce0713be98a08420c7eab1b40ee)#define BT\_MESH\_KEY\_ANY 0xffff

[ 69](group__bt__mesh__access.md#gabd37f17f3f5c3bc399ad3699df282675)#define BT\_MESH\_KEY\_DEV 0xfffe

[ 70](group__bt__mesh__access.md#ga9c64b38f2a6879f4750e3e1828e8ab7a)#define BT\_MESH\_KEY\_DEV\_LOCAL BT\_MESH\_KEY\_DEV

[ 71](group__bt__mesh__access.md#gaaa6ffb62df5d6d55c831d4d9860fc7eb)#define BT\_MESH\_KEY\_DEV\_REMOTE 0xfffd

[ 72](group__bt__mesh__access.md#gace0a526534e31e8067daf283407533fd)#define BT\_MESH\_KEY\_DEV\_ANY 0xfffc

76

[ 80](group__bt__mesh__access.md#ga1a4694cccf834d71f0abe2a0283cb9a8)#define BT\_MESH\_ADDR\_IS\_UNICAST(addr) ((addr) && (addr) < 0x8000)

[ 84](group__bt__mesh__access.md#gab50cc8dca6f7ffd5420ef4fb38fbe224)#define BT\_MESH\_ADDR\_IS\_GROUP(addr) ((addr) >= 0xc000 && (addr) < 0xff00)

[ 88](group__bt__mesh__access.md#gaff5ff58937924a1e6297aa1b20efc30f)#define BT\_MESH\_ADDR\_IS\_FIXED\_GROUP(addr) ((addr) >= 0xff00 && (addr) < 0xffff)

[ 92](group__bt__mesh__access.md#ga623eb2da2c880eec2107f36402ba6621)#define BT\_MESH\_ADDR\_IS\_VIRTUAL(addr) ((addr) >= 0x8000 && (addr) < 0xc000)

[ 96](group__bt__mesh__access.md#ga98ba7663259ca43cd5a38c7a9e16516d)#define BT\_MESH\_ADDR\_IS\_RFU(addr) ((addr) >= 0xff00 && (addr) <= 0xfff8)

97

[ 101](group__bt__mesh__access.md#gac4aafa0bdd24fb51d515a62e83917936)#define BT\_MESH\_IS\_DEV\_KEY(key) (key == BT\_MESH\_KEY\_DEV\_LOCAL || \

102 key == BT\_MESH\_KEY\_DEV\_REMOTE)

103

[ 105](group__bt__mesh__access.md#gaa620c32d1dce8e4b691b7f4270016506)#define BT\_MESH\_APP\_SEG\_SDU\_MAX 12

106

[ 108](group__bt__mesh__access.md#ga64eb6a94b1db9899c4f5bbf4cc88cd9f)#define BT\_MESH\_APP\_UNSEG\_SDU\_MAX 15

109

111#if defined(CONFIG\_BT\_MESH\_RX\_SEG\_MAX)

112#define BT\_MESH\_RX\_SEG\_MAX CONFIG\_BT\_MESH\_RX\_SEG\_MAX

113#else

[ 114](group__bt__mesh__access.md#ga18756e939ec3b312eef5c3dc9fd70270)#define BT\_MESH\_RX\_SEG\_MAX 0

115#endif

116

118#if defined(CONFIG\_BT\_MESH\_TX\_SEG\_MAX)

119#define BT\_MESH\_TX\_SEG\_MAX CONFIG\_BT\_MESH\_TX\_SEG\_MAX

120#else

[ 121](group__bt__mesh__access.md#ga1b2a3610ac370266578abce195e65fa2)#define BT\_MESH\_TX\_SEG\_MAX 0

122#endif

123

[ 125](group__bt__mesh__access.md#ga86d7386603ecd89952b6d540ea4243c2)#define BT\_MESH\_TX\_SDU\_MAX MAX((BT\_MESH\_TX\_SEG\_MAX \* \

126 BT\_MESH\_APP\_SEG\_SDU\_MAX), \

127 BT\_MESH\_APP\_UNSEG\_SDU\_MAX)

128

[ 130](group__bt__mesh__access.md#ga36f299f2fc13892b5a7d871dad1ec9ce)#define BT\_MESH\_RX\_SDU\_MAX MAX((BT\_MESH\_RX\_SEG\_MAX \* \

131 BT\_MESH\_APP\_SEG\_SDU\_MAX), \

132 BT\_MESH\_APP\_UNSEG\_SDU\_MAX)

133

[ 143](group__bt__mesh__access.md#ga321a5091dabd4ec4beb5396db6cabf44)#define BT\_MESH\_ELEM(\_loc, \_mods, \_vnd\_mods) \

144{ \

145 .rt = &(struct bt\_mesh\_elem\_rt\_ctx) { 0 }, \

146 .loc = (\_loc), \

147 .model\_count = ARRAY\_SIZE(\_mods), \

148 .vnd\_model\_count = ARRAY\_SIZE(\_vnd\_mods), \

149 .models = (\_mods), \

150 .vnd\_models = (\_vnd\_mods), \

151}

152

[ 154](structbt__mesh__elem.md)struct [bt\_mesh\_elem](structbt__mesh__elem.md) {

[ 156](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md) struct [bt\_mesh\_elem\_rt\_ctx](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md) {

[ 158](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md#a659279b38f1f3e015ebc648901577038) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md#a659279b38f1f3e015ebc648901577038);

[ 159](structbt__mesh__elem.md#a2090fa7827eb6a7b8bd1adfb831439cb) } \* const [rt](structbt__mesh__elem.md#a2090fa7827eb6a7b8bd1adfb831439cb);

160

[ 162](structbt__mesh__elem.md#a5f4c8ded34cf56c7f60189584e8e5b46) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [loc](structbt__mesh__elem.md#a5f4c8ded34cf56c7f60189584e8e5b46);

[ 164](structbt__mesh__elem.md#a648273e844ff9fa71578372e764ca8cf) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [model\_count](structbt__mesh__elem.md#a648273e844ff9fa71578372e764ca8cf);

[ 166](structbt__mesh__elem.md#aea56fd98c9aecfb9de3772ad3f14b25e) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vnd\_model\_count](structbt__mesh__elem.md#aea56fd98c9aecfb9de3772ad3f14b25e);

167

[ 169](structbt__mesh__elem.md#a57fefe57d9425d6666495d1f72a3f132) const struct [bt\_mesh\_model](structbt__mesh__model.md) \* const [models](structbt__mesh__elem.md#a57fefe57d9425d6666495d1f72a3f132);

[ 171](structbt__mesh__elem.md#a81d4fc1c41e2944bf7f6e71b00e19a0f) const struct [bt\_mesh\_model](structbt__mesh__model.md) \* const [vnd\_models](structbt__mesh__elem.md#a81d4fc1c41e2944bf7f6e71b00e19a0f);

172};

173

[ 179](group__bt__mesh__access.md#ga004d8d1be55b2aec56abbeeca1d118d8)#define BT\_MESH\_MODEL\_ID\_CFG\_SRV 0x0000

[ 181](group__bt__mesh__access.md#ga3f8442dcd1a110ea0d0023f50057139f)#define BT\_MESH\_MODEL\_ID\_CFG\_CLI 0x0001

[ 183](group__bt__mesh__access.md#ga6416216348d7186f91175ca50bb8c903)#define BT\_MESH\_MODEL\_ID\_HEALTH\_SRV 0x0002

[ 185](group__bt__mesh__access.md#gab58b85b7a77feeb579973177c12bb446)#define BT\_MESH\_MODEL\_ID\_HEALTH\_CLI 0x0003

[ 187](group__bt__mesh__access.md#ga9c7d1c5dfb87a5ce50c08747af47414f)#define BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV 0x0004

[ 189](group__bt__mesh__access.md#gaf373eb4d8af5d6bee76a821bd4d5e48c)#define BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI 0x0005

[ 191](group__bt__mesh__access.md#ga599d00e9d63ade6ed1a6803579c1e16e)#define BT\_MESH\_MODEL\_ID\_BRG\_CFG\_SRV 0x0008

[ 193](group__bt__mesh__access.md#ga9c776b4befd21c15f4867d906f631257)#define BT\_MESH\_MODEL\_ID\_BRG\_CFG\_CLI 0x0009

[ 195](group__bt__mesh__access.md#gacca0e355982935cfbde46a06b09a7bec)#define BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV 0x000a

[ 197](group__bt__mesh__access.md#gab3b21cbee4e11319a6e0ba3b02b24a91)#define BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI 0x000b

[ 199](group__bt__mesh__access.md#ga1e9d8be1d2e65d2977aea0306b015258)#define BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV 0x000e

[ 201](group__bt__mesh__access.md#gaf214eb7eef3530919432b62ff9b353c3)#define BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI 0x000f

[ 203](group__bt__mesh__access.md#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)#define BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV 0x0010

[ 205](group__bt__mesh__access.md#gabac62a77e7d2d7677af21c33c8629187)#define BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI 0x0011

[ 207](group__bt__mesh__access.md#gaec3abd6a0bd7b07a71fe5ed6a7a6931a)#define BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_SRV 0x0012

[ 209](group__bt__mesh__access.md#ga729d67e4183457932e4c837d65abd842)#define BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI 0x0013

[ 211](group__bt__mesh__access.md#ga165bc198dadaa0d534ec82eb8192ebc0)#define BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_SRV 0x0014

[ 213](group__bt__mesh__access.md#ga6e747dd364bcfaa368e37c5f01afd530)#define BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI 0x0015

[ 215](group__bt__mesh__access.md#gaddc0bd645180a57cb9cd36745b84f7a1)#define BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV 0x000c

[ 217](group__bt__mesh__access.md#gadd36546fb2cb6d1c731f7ae7674af6a7)#define BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI 0x000d

221

[ 227](group__bt__mesh__access.md#ga83e1ed5398d513cfeb900e41655aa4d8)#define BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_SRV 0x1000

[ 229](group__bt__mesh__access.md#ga4f0eee2569b518a5e4250f5b7b294fed)#define BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_CLI 0x1001

[ 231](group__bt__mesh__access.md#ga7f10a8332b1406c3ad628b9679e1d7cb)#define BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_SRV 0x1002

[ 233](group__bt__mesh__access.md#ga462c578845a17b20cdb3e008f74f93a6)#define BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_CLI 0x1003

[ 235](group__bt__mesh__access.md#ga004d5ec0870d47a8d37182e5b0c089a5)#define BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_SRV 0x1004

[ 237](group__bt__mesh__access.md#gafa1c6a7d857fe13a139ce2242b4e62f5)#define BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_CLI 0x1005

[ 239](group__bt__mesh__access.md#ga09ac731fff09146ec68557f00e8294e0)#define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SRV 0x1006

[ 241](group__bt__mesh__access.md#ga2a6dad18792ba7f1d81d6c9a1c65f90a)#define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SETUP\_SRV 0x1007

[ 243](group__bt__mesh__access.md#ga9f6544f7b87f39d0792ea2de13cd45f1)#define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_CLI 0x1008

[ 245](group__bt__mesh__access.md#gadd30afe63f89e9c1778e56f722fd82f9)#define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SRV 0x1009

[ 247](group__bt__mesh__access.md#ga1ff6ec64ce3a86d1cfd00fc98e89c0a5)#define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SETUP\_SRV 0x100a

[ 249](group__bt__mesh__access.md#ga8420454c35afc12c62ede55942f3b6d3)#define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_CLI 0x100b

[ 251](group__bt__mesh__access.md#gacf891135f54fb1fbb62beb812235619e)#define BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_SRV 0x100c

[ 253](group__bt__mesh__access.md#ga34bb3d4839e9685ec55f8285aac9a79f)#define BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_CLI 0x100d

[ 255](group__bt__mesh__access.md#gad516f513c5c942fbfee65b85332b105e)#define BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SRV 0x100e

[ 257](group__bt__mesh__access.md#ga240d1ed34b7341627773cce862f85620)#define BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SETUPSRV 0x100f

[ 259](group__bt__mesh__access.md#ga8fa01ddb1f4de4d61500bb650243390d)#define BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_CLI 0x1010

[ 261](group__bt__mesh__access.md#ga3cc6862e9c72f9282055c5cda2343c89)#define BT\_MESH\_MODEL\_ID\_GEN\_ADMIN\_PROP\_SRV 0x1011

[ 263](group__bt__mesh__access.md#ga32e09ddfebd2e8b22da9a3102e116aae)#define BT\_MESH\_MODEL\_ID\_GEN\_MANUFACTURER\_PROP\_SRV 0x1012

[ 265](group__bt__mesh__access.md#ga4b7b6a4b47e87de94ccf11ef1abd64b9)#define BT\_MESH\_MODEL\_ID\_GEN\_USER\_PROP\_SRV 0x1013

[ 267](group__bt__mesh__access.md#ga20906658018ef26114d8a6656c258f62)#define BT\_MESH\_MODEL\_ID\_GEN\_CLIENT\_PROP\_SRV 0x1014

[ 269](group__bt__mesh__access.md#ga69455e5b1e6def3d909c4bb6e0dee9ae)#define BT\_MESH\_MODEL\_ID\_GEN\_PROP\_CLI 0x1015

[ 271](group__bt__mesh__access.md#ga3e0dcb14f46f6076e5b1b114b977f630)#define BT\_MESH\_MODEL\_ID\_SENSOR\_SRV 0x1100

[ 273](group__bt__mesh__access.md#gad10780bfc1c16866fa28de750e56bec3)#define BT\_MESH\_MODEL\_ID\_SENSOR\_SETUP\_SRV 0x1101

[ 275](group__bt__mesh__access.md#ga8f1e4ff66d388627dbe91b2f8d4ed358)#define BT\_MESH\_MODEL\_ID\_SENSOR\_CLI 0x1102

[ 277](group__bt__mesh__access.md#ga93fbf1c661a75d70fdbd2a599353eb94)#define BT\_MESH\_MODEL\_ID\_TIME\_SRV 0x1200

[ 279](group__bt__mesh__access.md#ga2725121dc8c2c21c0ee469fe4348f45f)#define BT\_MESH\_MODEL\_ID\_TIME\_SETUP\_SRV 0x1201

[ 281](group__bt__mesh__access.md#ga500df90af7989794c5d72e760e5e65c6)#define BT\_MESH\_MODEL\_ID\_TIME\_CLI 0x1202

[ 283](group__bt__mesh__access.md#gaaa5554e3d48ae101596476e6bd6caf67)#define BT\_MESH\_MODEL\_ID\_SCENE\_SRV 0x1203

[ 285](group__bt__mesh__access.md#gaa3b08fc8788684abb960fa3516726264)#define BT\_MESH\_MODEL\_ID\_SCENE\_SETUP\_SRV 0x1204

[ 287](group__bt__mesh__access.md#gad60472aa004a8a913aeb63ef62c45857)#define BT\_MESH\_MODEL\_ID\_SCENE\_CLI 0x1205

[ 289](group__bt__mesh__access.md#ga82b723752e240f22b9bcc8dc3dd10eb9)#define BT\_MESH\_MODEL\_ID\_SCHEDULER\_SRV 0x1206

[ 291](group__bt__mesh__access.md#ga3dbec5a3b82cb25a142c4bc851e3fe0e)#define BT\_MESH\_MODEL\_ID\_SCHEDULER\_SETUP\_SRV 0x1207

[ 293](group__bt__mesh__access.md#gac743b26cf7e746b16302c25e8cd56221)#define BT\_MESH\_MODEL\_ID\_SCHEDULER\_CLI 0x1208

[ 295](group__bt__mesh__access.md#ga16df49e84e84d0ae4a6ab5d5f3f1b2b6)#define BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SRV 0x1300

[ 297](group__bt__mesh__access.md#gadb93b2ed2256a5c9c3f66237841b1bf5)#define BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SETUP\_SRV 0x1301

[ 299](group__bt__mesh__access.md#ga960055723dec7b3b366efa7c49cafc2e)#define BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_CLI 0x1302

[ 301](group__bt__mesh__access.md#gaa9a211341c5b3283b9b0e0842adef053)#define BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SRV 0x1303

[ 303](group__bt__mesh__access.md#ga28ac69b2dbeec70bae4bd3c0381e9e93)#define BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SETUP\_SRV 0x1304

[ 305](group__bt__mesh__access.md#ga58fc8d99b746b0061177ac5d95341da1)#define BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_CLI 0x1305

[ 307](group__bt__mesh__access.md#gafcb1f1ea20bb78b78a9ead4bfdbe3e47)#define BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_TEMP\_SRV 0x1306

[ 309](group__bt__mesh__access.md#gaa0ddc753a226060d014dcd368feab17e)#define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SRV 0x1307

[ 311](group__bt__mesh__access.md#ga574d3ba3f629bdbffc8f15db931a263a)#define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SETUP\_SRV 0x1308

[ 313](group__bt__mesh__access.md#ga2d111a352322be8e33ba0cba0feb3f0c)#define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_CLI 0x1309

[ 315](group__bt__mesh__access.md#ga865952346db9336a255c71bcb5f09774)#define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_HUE\_SRV 0x130a

[ 317](group__bt__mesh__access.md#gae55004e70670a8711e18e9c9b3428720)#define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SAT\_SRV 0x130b

[ 319](group__bt__mesh__access.md#ga29e1a90f166d88b6773d9b7ccf08e1c7)#define BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SRV 0x130c

[ 321](group__bt__mesh__access.md#ga4addae460d6b3c0a914198695b3e31ea)#define BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SETUP\_SRV 0x130d

[ 323](group__bt__mesh__access.md#ga0ca4d9997e6016b5c27f42549d42a99d)#define BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_CLI 0x130e

[ 325](group__bt__mesh__access.md#ga789412252034939539ba45e4bf21e3e2)#define BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SRV 0x130f

[ 327](group__bt__mesh__access.md#ga436358740bb64d845aa4d849d462a12e)#define BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SETUPSRV 0x1310

[ 329](group__bt__mesh__access.md#gaadd48b07e1eb53df24df40b7ea412e90)#define BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_CLI 0x1311

333

[ 339](group__bt__mesh__access.md#gae85d4cf7aad4e94582c24f79d6f60904)#define BT\_MESH\_MODEL\_ID\_BLOB\_SRV 0x1400

[ 341](group__bt__mesh__access.md#ga17e2e59a1344e623fe9fec6e27b7f22e)#define BT\_MESH\_MODEL\_ID\_BLOB\_CLI 0x1401

345

[ 351](group__bt__mesh__access.md#ga0215c2c8cd16ab6536ea243864f9604e)#define BT\_MESH\_MODEL\_ID\_DFU\_SRV 0x1402

[ 353](group__bt__mesh__access.md#gaf477a37238ec577000a646af40862ee1)#define BT\_MESH\_MODEL\_ID\_DFU\_CLI 0x1403

[ 355](group__bt__mesh__access.md#gaf4309dea32d05274f8f3a6ea45faba38)#define BT\_MESH\_MODEL\_ID\_DFD\_SRV 0x1404

[ 357](group__bt__mesh__access.md#ga87d3b5cc207dc3b51e85c9594bb98cad)#define BT\_MESH\_MODEL\_ID\_DFD\_CLI 0x1405

361

[ 363](structbt__mesh__model__op.md)struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) {

[ 365](structbt__mesh__model__op.md#a09c18a889e08bc708b9dc623f8177e39) const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [opcode](structbt__mesh__model__op.md#a09c18a889e08bc708b9dc623f8177e39);

366

[ 373](structbt__mesh__model__op.md#a25445fe2e937a321942c312bd675e486) const [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [len](structbt__mesh__model__op.md#a25445fe2e937a321942c312bd675e486);

374

[ 384](structbt__mesh__model__op.md#a4a5de7a12f2f8743048aafc81af0cece) int (\*const [func](structbt__mesh__model__op.md#a4a5de7a12f2f8743048aafc81af0cece))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model,

385 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

386 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

387};

388

[ 389](group__bt__mesh__access.md#ga00915cfdff7dc0646f24d6b06e124d0d)#define BT\_MESH\_MODEL\_OP\_1(b0) (b0)

[ 390](group__bt__mesh__access.md#gaa52a40ef5972c4f34cf5ff5a10e21289)#define BT\_MESH\_MODEL\_OP\_2(b0, b1) (((b0) << 8) | (b1))

[ 391](group__bt__mesh__access.md#ga72d1d19701be52f5eac6af475f9b19a9)#define BT\_MESH\_MODEL\_OP\_3(b0, cid) ((((b0) << 16) | 0xc00000) | (cid))

392

[ 394](group__bt__mesh__access.md#ga637e1be0298dc681414645867b28b59f)#define BT\_MESH\_LEN\_EXACT(len) (-len)

[ 396](group__bt__mesh__access.md#ga691ed9b3ab3ddaceda0f81c4a715ab3a)#define BT\_MESH\_LEN\_MIN(len) (len)

397

[ 399](group__bt__mesh__access.md#gaf2c164506c601214c85d451747176827)#define BT\_MESH\_MODEL\_OP\_END { 0, 0, NULL }

400

401#if !defined(\_\_cplusplus) || defined(\_\_DOXYGEN\_\_)

[ 408](group__bt__mesh__access.md#gae6d55e0a27bb7c448affd312a2e11656)#define BT\_MESH\_MODEL\_NO\_OPS ((struct bt\_mesh\_model\_op []) \

409 { BT\_MESH\_MODEL\_OP\_END })

410

[ 417](group__bt__mesh__access.md#gab0ad2aab95d49e5b60fe8dafd69132a4)#define BT\_MESH\_MODEL\_NONE ((const struct bt\_mesh\_model []){})

418

[ 436](group__bt__mesh__access.md#ga925da443eb15a4c1980d48a69388dc2c)#define BT\_MESH\_MODEL\_CNT\_CB(\_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb) \

437{ \

438 .id = (\_id), \

439 BT\_MESH\_MODEL\_RUNTIME\_INIT(\_user\_data) \

440 .pub = \_pub, \

441 .keys = (uint16\_t []) BT\_MESH\_MODEL\_KEYS\_UNUSED(\_keys), \

442 .keys\_cnt = \_keys, \

443 .groups = (uint16\_t []) BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED(\_grps), \

444 .groups\_cnt = \_grps, \

445 BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED() \

446 .op = \_op, \

447 .cb = \_cb, \

448}

449

[ 468](group__bt__mesh__access.md#ga32733dccd9329aa938dc0bd21cf9beae)#define BT\_MESH\_MODEL\_CNT\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb) \

469{ \

470 .vnd.company = (\_company), \

471 .vnd.id = (\_id), \

472 BT\_MESH\_MODEL\_RUNTIME\_INIT(\_user\_data) \

473 .op = \_op, \

474 .pub = \_pub, \

475 .keys = (uint16\_t []) BT\_MESH\_MODEL\_KEYS\_UNUSED(\_keys), \

476 .keys\_cnt = \_keys, \

477 .groups = (uint16\_t []) BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED(\_grps), \

478 .groups\_cnt = \_grps, \

479 BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED() \

480 .cb = \_cb, \

481}

482

[ 495](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb) \

496 BT\_MESH\_MODEL\_CNT\_CB(\_id, \_op, \_pub, \_user\_data, \

497 CONFIG\_BT\_MESH\_MODEL\_KEY\_COUNT, \

498 CONFIG\_BT\_MESH\_MODEL\_GROUP\_COUNT, \_cb)

499

500

516#if defined(CONFIG\_BT\_MESH\_LARGE\_COMP\_DATA\_SRV)

517#define BT\_MESH\_MODEL\_METADATA\_CB(\_id, \_op, \_pub, \_user\_data, \_cb, \_metadata) \

518{ \

519 .id = (\_id), \

520 BT\_MESH\_MODEL\_RUNTIME\_INIT(\_user\_data) \

521 .pub = \_pub, \

522 .keys = (uint16\_t []) BT\_MESH\_MODEL\_KEYS\_UNUSED(CONFIG\_BT\_MESH\_MODEL\_KEY\_COUNT), \

523 .keys\_cnt = CONFIG\_BT\_MESH\_MODEL\_KEY\_COUNT, \

524 .groups = (uint16\_t []) BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED(CONFIG\_BT\_MESH\_MODEL\_GROUP\_COUNT), \

525 .groups\_cnt = CONFIG\_BT\_MESH\_MODEL\_GROUP\_COUNT, \

526 BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED() \

527 .op = \_op, \

528 .cb = \_cb, \

529 .metadata = \_metadata, \

530}

531#else

[ 532](group__bt__mesh__access.md#ga40204b4ccaa819a487de168bcf66c98f)#define BT\_MESH\_MODEL\_METADATA\_CB(\_id, \_op, \_pub, \_user\_data, \_cb, \_metadata) \

533 BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

534#endif

535

[ 550](group__bt__mesh__access.md#gabe79d914990ba2721f5bb7081910e512)#define BT\_MESH\_MODEL\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_cb) \

551 BT\_MESH\_MODEL\_CNT\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \

552 CONFIG\_BT\_MESH\_MODEL\_KEY\_COUNT, \

553 CONFIG\_BT\_MESH\_MODEL\_GROUP\_COUNT, \_cb)

554

571#if defined(CONFIG\_BT\_MESH\_LARGE\_COMP\_DATA\_SRV)

572#define BT\_MESH\_MODEL\_VND\_METADATA\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_cb, \_metadata) \

573{ \

574 .vnd.company = (\_company), \

575 .vnd.id = (\_id), \

576 BT\_MESH\_MODEL\_RUNTIME\_INIT(\_user\_data) \

577 .op = \_op, \

578 .pub = \_pub, \

579 .keys = (uint16\_t []) BT\_MESH\_MODEL\_KEYS\_UNUSED(CONFIG\_BT\_MESH\_MODEL\_KEY\_COUNT), \

580 .keys\_cnt = CONFIG\_BT\_MESH\_MODEL\_KEY\_COUNT, \

581 .groups = (uint16\_t []) BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED(CONFIG\_BT\_MESH\_MODEL\_GROUP\_COUNT), \

582 .groups\_cnt = CONFIG\_BT\_MESH\_MODEL\_GROUP\_COUNT, \

583 BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED() \

584 .cb = \_cb, \

585 .metadata = \_metadata, \

586}

587#else

[ 588](group__bt__mesh__access.md#gac62334962dcbe3a75a03ce5744b326d8)#define BT\_MESH\_MODEL\_VND\_METADATA\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_cb, \_metadata) \

589 BT\_MESH\_MODEL\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_cb)

590#endif

[ 602](group__bt__mesh__access.md#gae694f5ac7ef9f0de37aaba846443586f)#define BT\_MESH\_MODEL(\_id, \_op, \_pub, \_user\_data) \

603 BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, NULL)

604

[ 617](group__bt__mesh__access.md#ga3759c8c88db48be662bf2511ff514edd)#define BT\_MESH\_MODEL\_VND(\_company, \_id, \_op, \_pub, \_user\_data) \

618 BT\_MESH\_MODEL\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, NULL)

619#endif /\* !defined(\_\_cplusplus) || defined(\_\_DOXYGEN\_\_) \*/

620

[ 631](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9)#define BT\_MESH\_TRANSMIT(count, int\_ms) ((uint8\_t)((count) | (((int\_ms / 10) - 1) << 3)))

632

[ 640](group__bt__mesh__access.md#ga62fda0d731241efbaa4827e4eb9d1795)#define BT\_MESH\_TRANSMIT\_COUNT(transmit) (((transmit) & (uint8\_t)BIT\_MASK(3)))

641

[ 649](group__bt__mesh__access.md#ga2aa21171c5677d23ad0c472291639417)#define BT\_MESH\_TRANSMIT\_INT(transmit) ((((transmit) >> 3) + 1) \* 10)

650

[ 661](group__bt__mesh__access.md#ga19208dea7bab9f31c2c793ef6201dd91)#define BT\_MESH\_PUB\_TRANSMIT(count, int\_ms) BT\_MESH\_TRANSMIT(count, \

662 (int\_ms) / 5)

663

[ 671](group__bt__mesh__access.md#ga13986422dda5edce4f5fb1ce387093e3)#define BT\_MESH\_PUB\_TRANSMIT\_COUNT(transmit) BT\_MESH\_TRANSMIT\_COUNT(transmit)

672

[ 680](group__bt__mesh__access.md#gaac954956dd3913dd7ad2b93a2566afd9)#define BT\_MESH\_PUB\_TRANSMIT\_INT(transmit) ((((transmit) >> 3) + 1) \* 50)

681

[ 690](group__bt__mesh__access.md#ga230538bb39ac3d6c8c0327d1fad77e69)#define BT\_MESH\_PUB\_MSG\_TOTAL(pub) (BT\_MESH\_PUB\_TRANSMIT\_COUNT((pub)->retransmit) + 1)

691

[ 701](group__bt__mesh__access.md#ga115ee29aba3c3e985aa11d6692ca0d83)#define BT\_MESH\_PUB\_MSG\_NUM(pub) (BT\_MESH\_PUB\_TRANSMIT\_COUNT((pub)->retransmit) + 1 - (pub)->count)

702

[ 708](structbt__mesh__model__pub.md)struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) {

[ 710](structbt__mesh__model__pub.md#aa5026299082b3013740c7e36c01f91f5) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](structbt__mesh__model__pub.md#aa5026299082b3013740c7e36c01f91f5);

711

[ 712](structbt__mesh__model__pub.md#a408c9185168b962f7e7314f9a429fe8c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__model__pub.md#a408c9185168b962f7e7314f9a429fe8c);

[ 713](structbt__mesh__model__pub.md#abea9c2085c9d2e1e2fc71f03dd323ee7) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[uuid](structbt__mesh__model__pub.md#abea9c2085c9d2e1e2fc71f03dd323ee7);

[ 714](structbt__mesh__model__pub.md#a0ad1809fe74930c9b36b32516a8d146f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [key](structbt__mesh__model__pub.md#a0ad1809fe74930c9b36b32516a8d146f):12,

[ 715](structbt__mesh__model__pub.md#a3617adb0c1192419bdac2ad0f37199ac) [cred](structbt__mesh__model__pub.md#a3617adb0c1192419bdac2ad0f37199ac):1,

[ 716](structbt__mesh__model__pub.md#ab704aedcfd06d374615ef18c6ecc84a9) [send\_rel](structbt__mesh__model__pub.md#ab704aedcfd06d374615ef18c6ecc84a9):1,

[ 717](structbt__mesh__model__pub.md#abdbdc3bbc5d4ac5a5d606b55bb2d50ee) [fast\_period](structbt__mesh__model__pub.md#abdbdc3bbc5d4ac5a5d606b55bb2d50ee):1,

[ 718](structbt__mesh__model__pub.md#a16c13e46c012ab836acd02b8fe5f05e3) [retr\_update](structbt__mesh__model__pub.md#a16c13e46c012ab836acd02b8fe5f05e3):1;

719

[ 720](structbt__mesh__model__pub.md#a820b713aaa1e0c33a4a59c80f805e854) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__model__pub.md#a820b713aaa1e0c33a4a59c80f805e854);

[ 721](structbt__mesh__model__pub.md#a3d93d44ff85243dc94e7b4d36cde5b97) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retransmit](structbt__mesh__model__pub.md#a3d93d44ff85243dc94e7b4d36cde5b97);

[ 722](structbt__mesh__model__pub.md#ae550510e9ca45f8c9fd9802e4e7e0f3d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [period](structbt__mesh__model__pub.md#ae550510e9ca45f8c9fd9802e4e7e0f3d);

[ 723](structbt__mesh__model__pub.md#a4f2ce8727ffb44f564d1dc0615ebcadf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [period\_div](structbt__mesh__model__pub.md#a4f2ce8727ffb44f564d1dc0615ebcadf):4,

[ 724](structbt__mesh__model__pub.md#a4e211c851bf91a9b43f035d435e9c93c) [count](structbt__mesh__model__pub.md#a4e211c851bf91a9b43f035d435e9c93c):4;

725

[ 726](structbt__mesh__model__pub.md#a23a865dbd2dce5c1af074097864611e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [delayable](structbt__mesh__model__pub.md#a23a865dbd2dce5c1af074097864611e9):1;

727

[ 728](structbt__mesh__model__pub.md#ab6e00714ea899eb32873d10b0908d278) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [period\_start](structbt__mesh__model__pub.md#ab6e00714ea899eb32873d10b0908d278);

729

[ 737](structbt__mesh__model__pub.md#a5f5639c01d3704ec3d527c418d35f827) struct [net\_buf\_simple](structnet__buf__simple.md) \*[msg](structbt__mesh__model__pub.md#a5f5639c01d3704ec3d527c418d35f827);

738

[ 757](structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080) int (\*[update](structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](structbt__mesh__model__pub.md#aa5026299082b3013740c7e36c01f91f5));

758

[ 760](structbt__mesh__model__pub.md#af3771432d13805710e94f013332e8214) struct [k\_work\_delayable](structk__work__delayable.md) [timer](structbt__mesh__model__pub.md#af3771432d13805710e94f013332e8214);

761};

762

[ 770](group__bt__mesh__access.md#ga8334ff2da1f0dc3ab2fc914059c33622)#define BT\_MESH\_MODEL\_PUB\_DEFINE(\_name, \_update, \_msg\_len) \

771 NET\_BUF\_SIMPLE\_DEFINE\_STATIC(bt\_mesh\_pub\_msg\_##\_name, \_msg\_len); \

772 static struct bt\_mesh\_model\_pub \_name = { \

773 .msg = &bt\_mesh\_pub\_msg\_##\_name, \

774 .update = \_update, \

775 }

776

[ 782](structbt__mesh__models__metadata__entry.md)struct [bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md) {

783 /\* Length of the metadata \*/

[ 784](structbt__mesh__models__metadata__entry.md#a39959b1f46e1b21eb78dbe3293f29149) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__mesh__models__metadata__entry.md#a39959b1f46e1b21eb78dbe3293f29149);

785

786 /\* ID of the metadata \*/

[ 787](structbt__mesh__models__metadata__entry.md#ae343d6ca709e1aceafc25d64cdf3916d) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structbt__mesh__models__metadata__entry.md#ae343d6ca709e1aceafc25d64cdf3916d);

788

789 /\* Pointer to raw data \*/

[ 790](structbt__mesh__models__metadata__entry.md#adb5aaf010cae636c0b60a88f38d36fac) const void \* const [data](structbt__mesh__models__metadata__entry.md#adb5aaf010cae636c0b60a88f38d36fac);

791};

792

[ 801](group__bt__mesh__access.md#gaa2587adac719c50c311ae41c548b853c)#define BT\_MESH\_MODELS\_METADATA\_ENTRY(\_len, \_id, \_data) \

802 { \

803 .len = (\_len), .id = \_id, .data = \_data, \

804 }

805

[ 807](group__bt__mesh__access.md#ga56b518123ab47cb3ae4a249f471ae556)#define BT\_MESH\_MODELS\_METADATA\_NONE NULL

808

[ 810](group__bt__mesh__access.md#gaab5fe51071f6e54debd9136ac6a70a49)#define BT\_MESH\_MODELS\_METADATA\_END { 0, 0, NULL }

811

[ 813](structbt__mesh__model__cb.md)struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) {

[ 827](structbt__mesh__model__cb.md#a21fc24829c6933a035b0f0be1a1f58e5) int (\*const [settings\_set](structbt__mesh__model__cb.md#a21fc24829c6933a035b0f0be1a1f58e5))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model,

828 const char \*name, size\_t len\_rd,

829 [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg);

830

[ 843](structbt__mesh__model__cb.md#a8333420fb9d1d98799ae03ba3b23bfe4) int (\*const [start](structbt__mesh__model__cb.md#a8333420fb9d1d98799ae03ba3b23bfe4))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model);

844

[ 857](structbt__mesh__model__cb.md#a1688a2c6d7b3b17ba49a0975b6f4f68e) int (\*const [init](structbt__mesh__model__cb.md#a1688a2c6d7b3b17ba49a0975b6f4f68e))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model);

858

[ 869](structbt__mesh__model__cb.md#a3a7ad466120085c55bcffacb15c78518) void (\*const [reset](structbt__mesh__model__cb.md#a3a7ad466120085c55bcffacb15c78518))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model);

870

[ 879](structbt__mesh__model__cb.md#ae28f875dffc7f5f2ce99abe590369f43) void (\*const [pending\_store](structbt__mesh__model__cb.md#ae28f875dffc7f5f2ce99abe590369f43))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model);

880};

881

[ 883](structbt__mesh__mod__id__vnd.md)struct [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md) {

[ 885](structbt__mesh__mod__id__vnd.md#a187a919337c92f54eaba6f932c7a3670) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [company](structbt__mesh__mod__id__vnd.md#a187a919337c92f54eaba6f932c7a3670);

[ 887](structbt__mesh__mod__id__vnd.md#a1a299852544a5e6fa3c34ac5ffd883d8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structbt__mesh__mod__id__vnd.md#a1a299852544a5e6fa3c34ac5ffd883d8);

888};

889

[ 891](structbt__mesh__model.md)struct [bt\_mesh\_model](structbt__mesh__model.md) {

892 union {

[ 894](structbt__mesh__model.md#a848ccf09f7b75ff8a48acb6c8088cf2a) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structbt__mesh__model.md#a848ccf09f7b75ff8a48acb6c8088cf2a);

[ 896](structbt__mesh__model.md#a3372deccde1a5ab26d9204c97339596e) const struct [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md) [vnd](structbt__mesh__model.md#a3372deccde1a5ab26d9204c97339596e);

897 };

898

899 /\* Model runtime information \*/

[ 900](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md) struct [bt\_mesh\_model\_rt\_ctx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md) {

[ 901](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#aca9b558516b929a0b88d8171027e7c71) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [elem\_idx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#aca9b558516b929a0b88d8171027e7c71); /\* Belongs to Nth element \*/

[ 902](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a79351fd25ad2ebd1f08ef1748d21dabd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mod\_idx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a79351fd25ad2ebd1f08ef1748d21dabd); /\* Is the Nth model in the element \*/

[ 903](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#ab584da43197ad7afe8c9ae807ce69f7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#ab584da43197ad7afe8c9ae807ce69f7e); /\* Model flags for internal bookkeeping \*/

904

905#ifdef CONFIG\_BT\_MESH\_MODEL\_EXTENSIONS

906 /\* Pointer to the next model in a model extension list. \*/

[ 907](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a434ae02cff38c614ef340a3c17f30e9b) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[next](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a434ae02cff38c614ef340a3c17f30e9b);

908#endif

[ 910](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a718d3be40e7be83a196634054d18d568) void \*[user\_data](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a718d3be40e7be83a196634054d18d568);

[ 911](structbt__mesh__model.md#a3980e6f8100151cb3339792821fa7858) } \* const [rt](structbt__mesh__model.md#a3980e6f8100151cb3339792821fa7858);

912

[ 914](structbt__mesh__model.md#af4a1b5e837b3a1266c7f61ee21020c0b) struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) \* const [pub](structbt__mesh__model.md#af4a1b5e837b3a1266c7f61ee21020c0b);

915

[ 917](structbt__mesh__model.md#a63595a0559ca70ca76c996f0b71c7983) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* const [keys](structbt__mesh__model.md#a63595a0559ca70ca76c996f0b71c7983);

[ 918](structbt__mesh__model.md#a79b8fd44ced901c3478f0e04d7dadfcd) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [keys\_cnt](structbt__mesh__model.md#a79b8fd44ced901c3478f0e04d7dadfcd);

919

[ 921](structbt__mesh__model.md#a460ab46730afa4f74e4066f787864b0b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* const [groups](structbt__mesh__model.md#a460ab46730afa4f74e4066f787864b0b);

[ 922](structbt__mesh__model.md#adf3e3f0dab9838cc76361949b237bb9e) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [groups\_cnt](structbt__mesh__model.md#adf3e3f0dab9838cc76361949b237bb9e);

923

924#if (CONFIG\_BT\_MESH\_LABEL\_COUNT > 0) || defined(\_\_DOXYGEN\_\_)

[ 926](structbt__mesh__model.md#a274c811c22b764908599127b128ce584) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* const [uuids](structbt__mesh__model.md#a274c811c22b764908599127b128ce584);

927#endif

928

[ 930](structbt__mesh__model.md#a4acc656c737cf79161414984312100b6) const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \* const [op](structbt__mesh__model.md#a4acc656c737cf79161414984312100b6);

931

[ 933](structbt__mesh__model.md#a67a91d64051e055b79f5d9166ab12660) const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \* const [cb](structbt__mesh__model.md#a67a91d64051e055b79f5d9166ab12660);

934

935#if defined(CONFIG\_BT\_MESH\_LARGE\_COMP\_DATA\_SRV) || defined(\_\_DOXYGEN\_\_)

936 /\* Pointer to the array of model metadata entries. \*/

[ 937](structbt__mesh__model.md#af5b948709773e5388c30d457ec2a9559) const struct [bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md) \* const [metadata](structbt__mesh__model.md#af5b948709773e5388c30d457ec2a9559);

938#endif

939};

940

[ 942](structbt__mesh__send__cb.md)struct [bt\_mesh\_send\_cb](structbt__mesh__send__cb.md) {

[ 949](structbt__mesh__send__cb.md#a2f84ef4cb2d28729cd98b844a3d25f55) void (\*[start](structbt__mesh__send__cb.md#a2f84ef4cb2d28729cd98b844a3d25f55))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration, int err, void \*cb\_data);

[ 955](structbt__mesh__send__cb.md#aa169dbec8c96fd41a35616c009604685) void (\*[end](structbt__mesh__send__cb.md#aa169dbec8c96fd41a35616c009604685))(int err, void \*cb\_data);

956};

957

958

[ 960](group__bt__mesh__access.md#ga16516272b42420263b1c47c3ea16c0c8)#define BT\_MESH\_TTL\_DEFAULT 0xff

961

[ 963](group__bt__mesh__access.md#ga071e85e929589d31bf876e2e09cf2f19)#define BT\_MESH\_TTL\_MAX 0x7f

964

[ 975](group__bt__mesh__access.md#ga7cac052ef76f4b37a95343329b078e77)int [bt\_mesh\_model\_send](group__bt__mesh__access.md#ga7cac052ef76f4b37a95343329b078e77)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model,

976 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

977 struct [net\_buf\_simple](structnet__buf__simple.md) \*msg,

978 const struct [bt\_mesh\_send\_cb](structbt__mesh__send__cb.md) \*cb,

979 void \*cb\_data);

980

[ 994](group__bt__mesh__access.md#ga06644f8a5fa43351328d3f3403dbad03)int [bt\_mesh\_model\_publish](group__bt__mesh__access.md#ga06644f8a5fa43351328d3f3403dbad03)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model);

995

[ 1004](group__bt__mesh__access.md#ga1b961d45f8b7c231c698ca229115e434)static inline bool [bt\_mesh\_model\_pub\_is\_retransmission](group__bt__mesh__access.md#ga1b961d45f8b7c231c698ca229115e434)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model)

1005{

1006 return model->[pub](structbt__mesh__model.md#af4a1b5e837b3a1266c7f61ee21020c0b)->[count](structbt__mesh__model__pub.md#a4e211c851bf91a9b43f035d435e9c93c) != [BT\_MESH\_PUB\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga13986422dda5edce4f5fb1ce387093e3)(model->[pub](structbt__mesh__model.md#af4a1b5e837b3a1266c7f61ee21020c0b)->[retransmit](structbt__mesh__model__pub.md#a3d93d44ff85243dc94e7b4d36cde5b97));

1007}

1008

[ 1015](group__bt__mesh__access.md#ga8edba04af103fb11994d4d3e558ec4fb)const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*[bt\_mesh\_model\_elem](group__bt__mesh__access.md#ga8edba04af103fb11994d4d3e558ec4fb)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod);

1016

[ 1025](group__bt__mesh__access.md#gaf0510f9511d72f1d4fd07f865753a50a)const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[bt\_mesh\_model\_find](group__bt__mesh__access.md#gaf0510f9511d72f1d4fd07f865753a50a)(const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem,

1026 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

1027

[ 1037](group__bt__mesh__access.md#gadfb473db4b23902a192e12d322ff1fd2)const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[bt\_mesh\_model\_find\_vnd](group__bt__mesh__access.md#gadfb473db4b23902a192e12d322ff1fd2)(const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem,

1038 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

1039

[ 1046](group__bt__mesh__access.md#gaa8694fdab3f514d8051dad1cc7362ac9)static inline bool [bt\_mesh\_model\_in\_primary](group__bt__mesh__access.md#gaa8694fdab3f514d8051dad1cc7362ac9)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod)

1047{

1048 return (mod->[rt](structbt__mesh__model.md#a3980e6f8100151cb3339792821fa7858)->[elem\_idx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#aca9b558516b929a0b88d8171027e7c71) == 0);

1049}

1050

[ 1062](group__bt__mesh__access.md#gadff0895c5c34928d778fa615512b3d85)int [bt\_mesh\_model\_data\_store](group__bt__mesh__access.md#gadff0895c5c34928d778fa615512b3d85)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod, bool [vnd](structbt__mesh__model.md#a3372deccde1a5ab26d9204c97339596e),

1063 const char \*name, const void \*data,

1064 size\_t data\_len);

1065

[ 1077](group__bt__mesh__access.md#ga762896dd2e806b5be061b220d53ce4db)void [bt\_mesh\_model\_data\_store\_schedule](group__bt__mesh__access.md#ga762896dd2e806b5be061b220d53ce4db)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod);

1078

[ 1102](group__bt__mesh__access.md#gaf6356f715c8968151b8d539f2dd1880c)int [bt\_mesh\_model\_extend](group__bt__mesh__access.md#gaf6356f715c8968151b8d539f2dd1880c)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*extending\_mod,

1103 const struct [bt\_mesh\_model](structbt__mesh__model.md) \*base\_mod);

1104

1124

[ 1125](group__bt__mesh__access.md#ga03ce9f6f9ccf734ea72beede09288923)int [bt\_mesh\_model\_correspond](group__bt__mesh__access.md#ga03ce9f6f9ccf734ea72beede09288923)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*corresponding\_mod,

1126 const struct [bt\_mesh\_model](structbt__mesh__model.md) \*base\_mod);

1127

[ 1134](group__bt__mesh__access.md#ga10603a5846210a397f306b227ce10c2e)bool [bt\_mesh\_model\_is\_extended](group__bt__mesh__access.md#ga10603a5846210a397f306b227ce10c2e)(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model);

1135

[ 1143](group__bt__mesh__access.md#ga8575f680e77d86d6c85cac27985b9f3c)int [bt\_mesh\_comp\_change\_prepare](group__bt__mesh__access.md#ga8575f680e77d86d6c85cac27985b9f3c)(void);

1144

[ 1152](group__bt__mesh__access.md#ga26ac86bdd32d27e0091735d98670687a)int [bt\_mesh\_models\_metadata\_change\_prepare](group__bt__mesh__access.md#ga26ac86bdd32d27e0091735d98670687a)(void);

1153

[ 1155](structbt__mesh__comp.md)struct [bt\_mesh\_comp](structbt__mesh__comp.md) {

[ 1156](structbt__mesh__comp.md#a648f695898305ef9e6f4f9db42dd8cf9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__mesh__comp.md#a648f695898305ef9e6f4f9db42dd8cf9);

[ 1157](structbt__mesh__comp.md#a54031f4c3683a7209e8f7441c5875788) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pid](structbt__mesh__comp.md#a54031f4c3683a7209e8f7441c5875788);

[ 1158](structbt__mesh__comp.md#a7e4351e81e4e04bb9681e76d384f2fa5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__mesh__comp.md#a7e4351e81e4e04bb9681e76d384f2fa5);

1159

[ 1160](structbt__mesh__comp.md#aff69499c7ac2c1ba643c946c75aa21ce) size\_t [elem\_count](structbt__mesh__comp.md#aff69499c7ac2c1ba643c946c75aa21ce);

[ 1161](structbt__mesh__comp.md#ad3da0629db1cb423260aa202cab7f062) const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*[elem](structbt__mesh__comp.md#ad3da0629db1cb423260aa202cab7f062);

1162};

1163

[ 1165](structbt__mesh__comp2__record.md)struct [bt\_mesh\_comp2\_record](structbt__mesh__comp2__record.md) {

[ 1167](structbt__mesh__comp2__record.md#a19ce94025c1c8079ca2789bbcd09b00e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structbt__mesh__comp2__record.md#a19ce94025c1c8079ca2789bbcd09b00e);

1169 struct {

[ 1171](structbt__mesh__comp2__record.md#a5f25c33170c77375f6492ad3cc0feaac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [x](structbt__mesh__comp2__record.md#a5f25c33170c77375f6492ad3cc0feaac);

[ 1173](structbt__mesh__comp2__record.md#a4970a0757c34ab97697c69728b564df6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [y](structbt__mesh__comp2__record.md#a4970a0757c34ab97697c69728b564df6);

[ 1175](structbt__mesh__comp2__record.md#ac3cabce01490191f145234f386b9b119) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [z](structbt__mesh__comp2__record.md#ac3cabce01490191f145234f386b9b119);

[ 1176](structbt__mesh__comp2__record.md#a26370a5dc68af03424c0f2f4fecd0181) } [version](structbt__mesh__comp2__record.md#a26370a5dc68af03424c0f2f4fecd0181);

[ 1178](structbt__mesh__comp2__record.md#ad13066e9d6d32e8e2eab64881249eb7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [elem\_offset\_cnt](structbt__mesh__comp2__record.md#ad13066e9d6d32e8e2eab64881249eb7e);

[ 1180](structbt__mesh__comp2__record.md#a6f81d99a62252cd26d87ca4fb289bdf9) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[elem\_offset](structbt__mesh__comp2__record.md#a6f81d99a62252cd26d87ca4fb289bdf9);

[ 1182](structbt__mesh__comp2__record.md#abdc488e846233fa05f0fc48f4081576e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data\_len](structbt__mesh__comp2__record.md#abdc488e846233fa05f0fc48f4081576e);

[ 1184](structbt__mesh__comp2__record.md#acd5f5770a6606ad00fa0815e4866ec4e) const void \*[data](structbt__mesh__comp2__record.md#acd5f5770a6606ad00fa0815e4866ec4e);

1185};

1186

[ 1188](structbt__mesh__comp2.md)struct [bt\_mesh\_comp2](structbt__mesh__comp2.md) {

[ 1190](structbt__mesh__comp2.md#a9f3425cd64cc487e9a49b85bb0f2159b) size\_t [record\_cnt](structbt__mesh__comp2.md#a9f3425cd64cc487e9a49b85bb0f2159b);

[ 1192](structbt__mesh__comp2.md#adf022ca0738626832d566fd6a5a1d889) const struct [bt\_mesh\_comp2\_record](structbt__mesh__comp2__record.md) \*[record](structbt__mesh__comp2.md#adf022ca0738626832d566fd6a5a1d889);

1193};

1194

[ 1207](group__bt__mesh__access.md#ga8445c550a47dba16e3fa6fea36d6d9fc)int [bt\_mesh\_comp2\_register](group__bt__mesh__access.md#ga8445c550a47dba16e3fa6fea36d6d9fc)(const struct [bt\_mesh\_comp2](structbt__mesh__comp2.md) \*comp2);

1208

1209#ifdef \_\_cplusplus

1210}

1211#endif

1212

1216

1217#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_ACCESS\_H\_ \*/

[bt\_mesh\_model\_correspond](group__bt__mesh__access.md#ga03ce9f6f9ccf734ea72beede09288923)

int bt\_mesh\_model\_correspond(const struct bt\_mesh\_model \*corresponding\_mod, const struct bt\_mesh\_model \*base\_mod)

Let a model correspond to another.

[bt\_mesh\_model\_publish](group__bt__mesh__access.md#ga06644f8a5fa43351328d3f3403dbad03)

int bt\_mesh\_model\_publish(const struct bt\_mesh\_model \*model)

Send a model publication message.

[bt\_mesh\_model\_is\_extended](group__bt__mesh__access.md#ga10603a5846210a397f306b227ce10c2e)

bool bt\_mesh\_model\_is\_extended(const struct bt\_mesh\_model \*model)

Check if model is extended by another model.

[BT\_MESH\_PUB\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga13986422dda5edce4f5fb1ce387093e3)

#define BT\_MESH\_PUB\_TRANSMIT\_COUNT(transmit)

Decode Publish Retransmit count from a given value.

**Definition** access.h:671

[bt\_mesh\_model\_pub\_is\_retransmission](group__bt__mesh__access.md#ga1b961d45f8b7c231c698ca229115e434)

static bool bt\_mesh\_model\_pub\_is\_retransmission(const struct bt\_mesh\_model \*model)

Check if a message is being retransmitted.

**Definition** access.h:1004

[bt\_mesh\_models\_metadata\_change\_prepare](group__bt__mesh__access.md#ga26ac86bdd32d27e0091735d98670687a)

int bt\_mesh\_models\_metadata\_change\_prepare(void)

Indicate that the metadata will change on next bootup.

[bt\_mesh\_model\_data\_store\_schedule](group__bt__mesh__access.md#ga762896dd2e806b5be061b220d53ce4db)

void bt\_mesh\_model\_data\_store\_schedule(const struct bt\_mesh\_model \*mod)

Schedule the model's user data store in persistent storage.

[bt\_mesh\_model\_send](group__bt__mesh__access.md#ga7cac052ef76f4b37a95343329b078e77)

int bt\_mesh\_model\_send(const struct bt\_mesh\_model \*model, struct bt\_mesh\_msg\_ctx \*ctx, struct net\_buf\_simple \*msg, const struct bt\_mesh\_send\_cb \*cb, void \*cb\_data)

Send an Access Layer message.

[bt\_mesh\_comp2\_register](group__bt__mesh__access.md#ga8445c550a47dba16e3fa6fea36d6d9fc)

int bt\_mesh\_comp2\_register(const struct bt\_mesh\_comp2 \*comp2)

Register composition data page 2 of the device.

[bt\_mesh\_comp\_change\_prepare](group__bt__mesh__access.md#ga8575f680e77d86d6c85cac27985b9f3c)

int bt\_mesh\_comp\_change\_prepare(void)

Indicate that the composition data will change on next bootup.

[bt\_mesh\_model\_elem](group__bt__mesh__access.md#ga8edba04af103fb11994d4d3e558ec4fb)

const struct bt\_mesh\_elem \* bt\_mesh\_model\_elem(const struct bt\_mesh\_model \*mod)

Get the element that a model belongs to.

[bt\_mesh\_model\_in\_primary](group__bt__mesh__access.md#gaa8694fdab3f514d8051dad1cc7362ac9)

static bool bt\_mesh\_model\_in\_primary(const struct bt\_mesh\_model \*mod)

Get whether the model is in the primary element of the device.

**Definition** access.h:1046

[bt\_mesh\_model\_find\_vnd](group__bt__mesh__access.md#gadfb473db4b23902a192e12d322ff1fd2)

const struct bt\_mesh\_model \* bt\_mesh\_model\_find\_vnd(const struct bt\_mesh\_elem \*elem, uint16\_t company, uint16\_t id)

Find a vendor model.

[bt\_mesh\_model\_data\_store](group__bt__mesh__access.md#gadff0895c5c34928d778fa615512b3d85)

int bt\_mesh\_model\_data\_store(const struct bt\_mesh\_model \*mod, bool vnd, const char \*name, const void \*data, size\_t data\_len)

Immediately store the model's user data in persistent storage.

[bt\_mesh\_model\_find](group__bt__mesh__access.md#gaf0510f9511d72f1d4fd07f865753a50a)

const struct bt\_mesh\_model \* bt\_mesh\_model\_find(const struct bt\_mesh\_elem \*elem, uint16\_t id)

Find a SIG model.

[bt\_mesh\_model\_extend](group__bt__mesh__access.md#gaf6356f715c8968151b8d539f2dd1880c)

int bt\_mesh\_model\_extend(const struct bt\_mesh\_model \*extending\_mod, const struct bt\_mesh\_model \*base\_mod)

Let a model extend another.

[settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04)

ssize\_t(\* settings\_read\_cb)(void \*cb\_arg, void \*data, size\_t len)

Function used to read the data from the settings storage in h\_set handler implementations.

**Definition** settings.h:61

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[msg.h](msg_8h.md)

Message APIs.

[settings.h](settings_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_comp2\_record](structbt__mesh__comp2__record.md)

Composition data page 2 record.

**Definition** access.h:1165

[bt\_mesh\_comp2\_record::id](structbt__mesh__comp2__record.md#a19ce94025c1c8079ca2789bbcd09b00e)

uint16\_t id

Mesh profile ID.

**Definition** access.h:1167

[bt\_mesh\_comp2\_record::version](structbt__mesh__comp2__record.md#a26370a5dc68af03424c0f2f4fecd0181)

struct bt\_mesh\_comp2\_record::@315261044123040067132243322322175125334172045074 version

Mesh Profile Version.

[bt\_mesh\_comp2\_record::y](structbt__mesh__comp2__record.md#a4970a0757c34ab97697c69728b564df6)

uint8\_t y

Minor version.

**Definition** access.h:1173

[bt\_mesh\_comp2\_record::x](structbt__mesh__comp2__record.md#a5f25c33170c77375f6492ad3cc0feaac)

uint8\_t x

Major version.

**Definition** access.h:1171

[bt\_mesh\_comp2\_record::elem\_offset](structbt__mesh__comp2__record.md#a6f81d99a62252cd26d87ca4fb289bdf9)

const uint8\_t \* elem\_offset

Element offset list.

**Definition** access.h:1180

[bt\_mesh\_comp2\_record::data\_len](structbt__mesh__comp2__record.md#abdc488e846233fa05f0fc48f4081576e)

uint16\_t data\_len

Length of additional data.

**Definition** access.h:1182

[bt\_mesh\_comp2\_record::z](structbt__mesh__comp2__record.md#ac3cabce01490191f145234f386b9b119)

uint8\_t z

Z version.

**Definition** access.h:1175

[bt\_mesh\_comp2\_record::data](structbt__mesh__comp2__record.md#acd5f5770a6606ad00fa0815e4866ec4e)

const void \* data

Additional data.

**Definition** access.h:1184

[bt\_mesh\_comp2\_record::elem\_offset\_cnt](structbt__mesh__comp2__record.md#ad13066e9d6d32e8e2eab64881249eb7e)

uint8\_t elem\_offset\_cnt

Element offset count.

**Definition** access.h:1178

[bt\_mesh\_comp2](structbt__mesh__comp2.md)

Node Composition data page 2.

**Definition** access.h:1188

[bt\_mesh\_comp2::record\_cnt](structbt__mesh__comp2.md#a9f3425cd64cc487e9a49b85bb0f2159b)

size\_t record\_cnt

The number of Mesh Profile records on a device.

**Definition** access.h:1190

[bt\_mesh\_comp2::record](structbt__mesh__comp2.md#adf022ca0738626832d566fd6a5a1d889)

const struct bt\_mesh\_comp2\_record \* record

List of records.

**Definition** access.h:1192

[bt\_mesh\_comp](structbt__mesh__comp.md)

Node Composition.

**Definition** access.h:1155

[bt\_mesh\_comp::pid](structbt__mesh__comp.md#a54031f4c3683a7209e8f7441c5875788)

uint16\_t pid

Product ID.

**Definition** access.h:1157

[bt\_mesh\_comp::cid](structbt__mesh__comp.md#a648f695898305ef9e6f4f9db42dd8cf9)

uint16\_t cid

Company ID.

**Definition** access.h:1156

[bt\_mesh\_comp::vid](structbt__mesh__comp.md#a7e4351e81e4e04bb9681e76d384f2fa5)

uint16\_t vid

Version ID.

**Definition** access.h:1158

[bt\_mesh\_comp::elem](structbt__mesh__comp.md#ad3da0629db1cb423260aa202cab7f062)

const struct bt\_mesh\_elem \* elem

List of elements.

**Definition** access.h:1161

[bt\_mesh\_comp::elem\_count](structbt__mesh__comp.md#aff69499c7ac2c1ba643c946c75aa21ce)

size\_t elem\_count

The number of elements in this device.

**Definition** access.h:1160

[bt\_mesh\_elem::bt\_mesh\_elem\_rt\_ctx](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md)

Mesh Element runtime information.

**Definition** access.h:156

[bt\_mesh\_elem::bt\_mesh\_elem\_rt\_ctx::addr](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md#a659279b38f1f3e015ebc648901577038)

uint16\_t addr

Unicast Address.

**Definition** access.h:158

[bt\_mesh\_elem](structbt__mesh__elem.md)

Abstraction that describes a Mesh Element.

**Definition** access.h:154

[bt\_mesh\_elem::rt](structbt__mesh__elem.md#a2090fa7827eb6a7b8bd1adfb831439cb)

struct bt\_mesh\_elem::bt\_mesh\_elem\_rt\_ctx rt

[bt\_mesh\_elem::models](structbt__mesh__elem.md#a57fefe57d9425d6666495d1f72a3f132)

const struct bt\_mesh\_model \*const models

The list of SIG models in this element.

**Definition** access.h:169

[bt\_mesh\_elem::loc](structbt__mesh__elem.md#a5f4c8ded34cf56c7f60189584e8e5b46)

const uint16\_t loc

Location Descriptor (GATT Bluetooth Namespace Descriptors).

**Definition** access.h:162

[bt\_mesh\_elem::model\_count](structbt__mesh__elem.md#a648273e844ff9fa71578372e764ca8cf)

const uint8\_t model\_count

The number of SIG models in this element.

**Definition** access.h:164

[bt\_mesh\_elem::vnd\_models](structbt__mesh__elem.md#a81d4fc1c41e2944bf7f6e71b00e19a0f)

const struct bt\_mesh\_model \*const vnd\_models

The list of vendor models in this element.

**Definition** access.h:171

[bt\_mesh\_elem::vnd\_model\_count](structbt__mesh__elem.md#aea56fd98c9aecfb9de3772ad3f14b25e)

const uint8\_t vnd\_model\_count

The number of vendor models in this element.

**Definition** access.h:166

[bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md)

Vendor model ID.

**Definition** access.h:883

[bt\_mesh\_mod\_id\_vnd::company](structbt__mesh__mod__id__vnd.md#a187a919337c92f54eaba6f932c7a3670)

uint16\_t company

Vendor's company ID.

**Definition** access.h:885

[bt\_mesh\_mod\_id\_vnd::id](structbt__mesh__mod__id__vnd.md#a1a299852544a5e6fa3c34ac5ffd883d8)

uint16\_t id

Model ID.

**Definition** access.h:887

[bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md)

**Definition** access.h:900

[bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx::next](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a434ae02cff38c614ef340a3c17f30e9b)

const struct bt\_mesh\_model \* next

**Definition** access.h:907

[bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx::user\_data](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a718d3be40e7be83a196634054d18d568)

void \* user\_data

Model-specific user data.

**Definition** access.h:910

[bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx::mod\_idx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#a79351fd25ad2ebd1f08ef1748d21dabd)

uint8\_t mod\_idx

**Definition** access.h:902

[bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx::flags](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#ab584da43197ad7afe8c9ae807ce69f7e)

uint16\_t flags

**Definition** access.h:903

[bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx::elem\_idx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md#aca9b558516b929a0b88d8171027e7c71)

uint8\_t elem\_idx

**Definition** access.h:901

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_cb::init](structbt__mesh__model__cb.md#a1688a2c6d7b3b17ba49a0975b6f4f68e)

int(\*const init)(const struct bt\_mesh\_model \*model)

Model init callback.

**Definition** access.h:857

[bt\_mesh\_model\_cb::settings\_set](structbt__mesh__model__cb.md#a21fc24829c6933a035b0f0be1a1f58e5)

int(\*const settings\_set)(const struct bt\_mesh\_model \*model, const char \*name, size\_t len\_rd, settings\_read\_cb read\_cb, void \*cb\_arg)

Set value handler of user data tied to the model.

**Definition** access.h:827

[bt\_mesh\_model\_cb::reset](structbt__mesh__model__cb.md#a3a7ad466120085c55bcffacb15c78518)

void(\*const reset)(const struct bt\_mesh\_model \*model)

Model reset callback.

**Definition** access.h:869

[bt\_mesh\_model\_cb::start](structbt__mesh__model__cb.md#a8333420fb9d1d98799ae03ba3b23bfe4)

int(\*const start)(const struct bt\_mesh\_model \*model)

Callback called when the mesh is started.

**Definition** access.h:843

[bt\_mesh\_model\_cb::pending\_store](structbt__mesh__model__cb.md#ae28f875dffc7f5f2ce99abe590369f43)

void(\*const pending\_store)(const struct bt\_mesh\_model \*model)

Callback used to store pending model's user data.

**Definition** access.h:879

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

[bt\_mesh\_model\_op::opcode](structbt__mesh__model__op.md#a09c18a889e08bc708b9dc623f8177e39)

const uint32\_t opcode

OpCode encoded using the BT\_MESH\_MODEL\_OP\_\* macros.

**Definition** access.h:365

[bt\_mesh\_model\_op::len](structbt__mesh__model__op.md#a25445fe2e937a321942c312bd675e486)

const ssize\_t len

Message length.

**Definition** access.h:373

[bt\_mesh\_model\_op::func](structbt__mesh__model__op.md#a4a5de7a12f2f8743048aafc81af0cece)

int(\*const func)(const struct bt\_mesh\_model \*model, struct bt\_mesh\_msg\_ctx \*ctx, struct net\_buf\_simple \*buf)

Handler function for this opcode.

**Definition** access.h:384

[bt\_mesh\_model\_pub](structbt__mesh__model__pub.md)

Model publication context.

**Definition** access.h:708

[bt\_mesh\_model\_pub::update](structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080)

int(\* update)(const struct bt\_mesh\_model \*mod)

Callback for updating the publication buffer.

**Definition** access.h:757

[bt\_mesh\_model\_pub::key](structbt__mesh__model__pub.md#a0ad1809fe74930c9b36b32516a8d146f)

uint16\_t key

Publish AppKey Index.

**Definition** access.h:714

[bt\_mesh\_model\_pub::retr\_update](structbt__mesh__model__pub.md#a16c13e46c012ab836acd02b8fe5f05e3)

uint16\_t retr\_update

Call update callback on every retransmission.

**Definition** access.h:718

[bt\_mesh\_model\_pub::delayable](structbt__mesh__model__pub.md#a23a865dbd2dce5c1af074097864611e9)

uint8\_t delayable

Use random delay for publishing.

**Definition** access.h:726

[bt\_mesh\_model\_pub::cred](structbt__mesh__model__pub.md#a3617adb0c1192419bdac2ad0f37199ac)

uint16\_t cred

Friendship Credentials Flag.

**Definition** access.h:715

[bt\_mesh\_model\_pub::retransmit](structbt__mesh__model__pub.md#a3d93d44ff85243dc94e7b4d36cde5b97)

uint8\_t retransmit

Retransmit Count & Interval Steps.

**Definition** access.h:721

[bt\_mesh\_model\_pub::addr](structbt__mesh__model__pub.md#a408c9185168b962f7e7314f9a429fe8c)

uint16\_t addr

Publish Address.

**Definition** access.h:712

[bt\_mesh\_model\_pub::count](structbt__mesh__model__pub.md#a4e211c851bf91a9b43f035d435e9c93c)

uint8\_t count

Transmissions left.

**Definition** access.h:724

[bt\_mesh\_model\_pub::period\_div](structbt__mesh__model__pub.md#a4f2ce8727ffb44f564d1dc0615ebcadf)

uint8\_t period\_div

Divisor for the Period.

**Definition** access.h:723

[bt\_mesh\_model\_pub::msg](structbt__mesh__model__pub.md#a5f5639c01d3704ec3d527c418d35f827)

struct net\_buf\_simple \* msg

Publication buffer, containing the publication message.

**Definition** access.h:737

[bt\_mesh\_model\_pub::ttl](structbt__mesh__model__pub.md#a820b713aaa1e0c33a4a59c80f805e854)

uint8\_t ttl

Publish Time to Live.

**Definition** access.h:720

[bt\_mesh\_model\_pub::mod](structbt__mesh__model__pub.md#aa5026299082b3013740c7e36c01f91f5)

const struct bt\_mesh\_model \* mod

The model the context belongs to.

**Definition** access.h:710

[bt\_mesh\_model\_pub::period\_start](structbt__mesh__model__pub.md#ab6e00714ea899eb32873d10b0908d278)

uint32\_t period\_start

Start of the current period.

**Definition** access.h:728

[bt\_mesh\_model\_pub::send\_rel](structbt__mesh__model__pub.md#ab704aedcfd06d374615ef18c6ecc84a9)

uint16\_t send\_rel

Force reliable sending (segment acks).

**Definition** access.h:716

[bt\_mesh\_model\_pub::fast\_period](structbt__mesh__model__pub.md#abdbdc3bbc5d4ac5a5d606b55bb2d50ee)

uint16\_t fast\_period

Use FastPeriodDivisor.

**Definition** access.h:717

[bt\_mesh\_model\_pub::uuid](structbt__mesh__model__pub.md#abea9c2085c9d2e1e2fc71f03dd323ee7)

const uint8\_t \* uuid

Label UUID if Publish Address is Virtual Address.

**Definition** access.h:713

[bt\_mesh\_model\_pub::period](structbt__mesh__model__pub.md#ae550510e9ca45f8c9fd9802e4e7e0f3d)

uint8\_t period

Publish Period.

**Definition** access.h:722

[bt\_mesh\_model\_pub::timer](structbt__mesh__model__pub.md#af3771432d13805710e94f013332e8214)

struct k\_work\_delayable timer

Publish Period Timer.

**Definition** access.h:760

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:891

[bt\_mesh\_model::uuids](structbt__mesh__model.md#a274c811c22b764908599127b128ce584)

const uint8\_t \*\*const uuids

List of Label UUIDs the model is subscribed to.

**Definition** access.h:926

[bt\_mesh\_model::vnd](structbt__mesh__model.md#a3372deccde1a5ab26d9204c97339596e)

const struct bt\_mesh\_mod\_id\_vnd vnd

Vendor model ID.

**Definition** access.h:896

[bt\_mesh\_model::rt](structbt__mesh__model.md#a3980e6f8100151cb3339792821fa7858)

struct bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx rt

[bt\_mesh\_model::groups](structbt__mesh__model.md#a460ab46730afa4f74e4066f787864b0b)

uint16\_t \*const groups

Subscription List (group or virtual addresses).

**Definition** access.h:921

[bt\_mesh\_model::op](structbt__mesh__model.md#a4acc656c737cf79161414984312100b6)

const struct bt\_mesh\_model\_op \*const op

Opcode handler list.

**Definition** access.h:930

[bt\_mesh\_model::keys](structbt__mesh__model.md#a63595a0559ca70ca76c996f0b71c7983)

uint16\_t \*const keys

AppKey List.

**Definition** access.h:917

[bt\_mesh\_model::cb](structbt__mesh__model.md#a67a91d64051e055b79f5d9166ab12660)

const struct bt\_mesh\_model\_cb \*const cb

Model callback structure.

**Definition** access.h:933

[bt\_mesh\_model::keys\_cnt](structbt__mesh__model.md#a79b8fd44ced901c3478f0e04d7dadfcd)

const uint16\_t keys\_cnt

**Definition** access.h:918

[bt\_mesh\_model::id](structbt__mesh__model.md#a848ccf09f7b75ff8a48acb6c8088cf2a)

const uint16\_t id

SIG model ID.

**Definition** access.h:894

[bt\_mesh\_model::groups\_cnt](structbt__mesh__model.md#adf3e3f0dab9838cc76361949b237bb9e)

const uint16\_t groups\_cnt

**Definition** access.h:922

[bt\_mesh\_model::pub](structbt__mesh__model.md#af4a1b5e837b3a1266c7f61ee21020c0b)

struct bt\_mesh\_model\_pub \*const pub

Model Publication.

**Definition** access.h:914

[bt\_mesh\_model::metadata](structbt__mesh__model.md#af5b948709773e5388c30d457ec2a9559)

const struct bt\_mesh\_models\_metadata\_entry \*const metadata

**Definition** access.h:937

[bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md)

Models Metadata Entry struct.

**Definition** access.h:782

[bt\_mesh\_models\_metadata\_entry::len](structbt__mesh__models__metadata__entry.md#a39959b1f46e1b21eb78dbe3293f29149)

const uint16\_t len

**Definition** access.h:784

[bt\_mesh\_models\_metadata\_entry::data](structbt__mesh__models__metadata__entry.md#adb5aaf010cae636c0b60a88f38d36fac)

const void \*const data

**Definition** access.h:790

[bt\_mesh\_models\_metadata\_entry::id](structbt__mesh__models__metadata__entry.md#ae343d6ca709e1aceafc25d64cdf3916d)

const uint16\_t id

**Definition** access.h:787

[bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md)

Message sending context.

**Definition** msg.h:76

[bt\_mesh\_send\_cb](structbt__mesh__send__cb.md)

Callback structure for monitoring model message sending.

**Definition** access.h:942

[bt\_mesh\_send\_cb::start](structbt__mesh__send__cb.md#a2f84ef4cb2d28729cd98b844a3d25f55)

void(\* start)(uint16\_t duration, int err, void \*cb\_data)

Handler called at the start of the transmission.

**Definition** access.h:949

[bt\_mesh\_send\_cb::end](structbt__mesh__send__cb.md#aa169dbec8c96fd41a35616c009604685)

void(\* end)(int err, void \*cb\_data)

Handler called at the end of the transmission.

**Definition** access.h:955

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4034

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [access.h](access_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
