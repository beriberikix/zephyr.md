---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bap_8h_source.html
original_path: doxygen/html/bap_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bap.h

[Go to the documentation of this file.](bap_8h.md)

1

9

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_

12

19

20#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

21#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

22

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 29](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296)enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) {

[ 31](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf) [BT\_BAP\_PA\_STATE\_NOT\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf) = 0x00,

32

[ 34](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb) [BT\_BAP\_PA\_STATE\_INFO\_REQ](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb) = 0x01,

35

[ 37](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc) [BT\_BAP\_PA\_STATE\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc) = 0x02,

38

[ 40](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647) [BT\_BAP\_PA\_STATE\_FAILED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647) = 0x03,

41

[ 43](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d) [BT\_BAP\_PA\_STATE\_NO\_PAST](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d) = 0x04,

44};

45

[ 47](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22)enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) {

[ 49](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4) [BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4) = 0x00,

50

[ 52](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2) [BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2) = 0x01,

53

[ 55](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10) [BT\_BAP\_BIG\_ENC\_STATE\_DEC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10) = 0x02,

56

[ 58](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b) [BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b) = 0x03,

59};

60

[ 62](group__bt__bap.md#ga13e9b6d571a613d689b8ba58bae64ae3)enum [bt\_bap\_bass\_att\_err](group__bt__bap.md#ga13e9b6d571a613d689b8ba58bae64ae3) {

[ 64](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c) [BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c) = 0x80,

65

[ 67](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202) [BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202) = 0x81,

68};

69

[ 71](group__bt__bap.md#ga357079ef00ce6f250e72a37103926c64)#define BT\_BAP\_PA\_INTERVAL\_UNKNOWN 0xFFFF

72

[ 78](group__bt__bap.md#ga799f1417272e9b545c1e30ed4616b988)#define BT\_BAP\_BIS\_SYNC\_NO\_PREF 0xFFFFFFFF

79

[ 81](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a)enum [bt\_bap\_ep\_state](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a) {

[ 83](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961) [BT\_BAP\_EP\_STATE\_IDLE](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961) = 0x00,

84

[ 86](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688) [BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688) = 0x01,

87

[ 89](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523) [BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523) = 0x02,

90

[ 92](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332) [BT\_BAP\_EP\_STATE\_ENABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332) = 0x03,

93

[ 95](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710) [BT\_BAP\_EP\_STATE\_STREAMING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710) = 0x04,

96

[ 98](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8) [BT\_BAP\_EP\_STATE\_DISABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8) = 0x05,

99

[ 101](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c) [BT\_BAP\_EP\_STATE\_RELEASING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c) = 0x06,

102};

103

[ 110](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1)enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) {

[ 112](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd) [BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd) = 0x00,

[ 114](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d) [BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d) = 0x01,

[ 116](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9) [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9) = 0x02,

[ 118](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa) [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa) = 0x03,

[ 120](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5) [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5) = 0x04,

[ 122](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146) [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146) = 0x05,

[ 124](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a) [BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a) = 0x06,

[ 126](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62) [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62) = 0x07,

[ 128](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) = 0x08,

[ 130](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219) [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219) = 0x09,

[ 132](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7) [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7) = 0x0a,

[ 134](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06) [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06) = 0x0b,

[ 136](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06) [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06) = 0x0c,

[ 138](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb) [BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb) = 0x0d,

[ 140](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a) [BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a) = 0x0e,

141};

142

[ 150](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45)enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) {

[ 152](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd) [BT\_BAP\_ASCS\_REASON\_NONE](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd) = 0x00,

[ 154](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea) [BT\_BAP\_ASCS\_REASON\_CODEC](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea) = 0x01,

[ 156](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0) [BT\_BAP\_ASCS\_REASON\_CODEC\_DATA](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0) = 0x02,

[ 158](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c) [BT\_BAP\_ASCS\_REASON\_INTERVAL](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c) = 0x03,

[ 160](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539) [BT\_BAP\_ASCS\_REASON\_FRAMING](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539) = 0x04,

[ 162](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8) [BT\_BAP\_ASCS\_REASON\_PHY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8) = 0x05,

[ 164](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b) [BT\_BAP\_ASCS\_REASON\_SDU](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b) = 0x06,

[ 166](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf) [BT\_BAP\_ASCS\_REASON\_RTN](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf) = 0x07,

[ 168](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942) [BT\_BAP\_ASCS\_REASON\_LATENCY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942) = 0x08,

[ 170](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557) [BT\_BAP\_ASCS\_REASON\_PD](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557) = 0x09,

[ 172](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c) [BT\_BAP\_ASCS\_REASON\_CIS](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c) = 0x0a,

173};

174

[ 176](structbt__bap__ascs__rsp.md)struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) {

[ 190](structbt__bap__ascs__rsp.md#a8ea364298f7e3e784b7878215db63d91) enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) [code](structbt__bap__ascs__rsp.md#a8ea364298f7e3e784b7878215db63d91);

191

197 union {

[ 213](structbt__bap__ascs__rsp.md#a138532bc40f60547c56d8b108ad44d1e) enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) [reason](structbt__bap__ascs__rsp.md#a138532bc40f60547c56d8b108ad44d1e);

214

[ 223](structbt__bap__ascs__rsp.md#a736f44864015244a8b48a859eff6b902) enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) [metadata\_type](structbt__bap__ascs__rsp.md#a736f44864015244a8b48a859eff6b902);

224 };

225};

226

[ 234](group__bt__bap.md#ga8e5cd46a1428a315119e47c9cbbb9bfd)#define BT\_BAP\_ASCS\_RSP(c, r) (struct bt\_bap\_ascs\_rsp) { .code = c, .reason = r }

235

237struct bt\_bap\_broadcast\_source;

238

240struct bt\_bap\_broadcast\_sink;

241

243struct bt\_bap\_unicast\_group;

244

246struct bt\_bap\_ep;

247

[ 249](structbt__bap__bass__subgroup.md)struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) {

[ 251](structbt__bap__bass__subgroup.md#ac8061995eb73ba30e335e37714396ff5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bis\_sync](structbt__bap__bass__subgroup.md#ac8061995eb73ba30e335e37714396ff5);

252

[ 254](structbt__bap__bass__subgroup.md#ace1c1ff5d2f5cc79838653d468166664) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [metadata\_len](structbt__bap__bass__subgroup.md#ace1c1ff5d2f5cc79838653d468166664);

255

256#if defined(CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE)

258 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) metadata[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE];

259#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE \*/

260};

261

[ 263](structbt__bap__scan__delegator__recv__state.md)struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) {

[ 265](structbt__bap__scan__delegator__recv__state.md#a1755a6332c86aeaf624d3c540037772a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__bap__scan__delegator__recv__state.md#a1755a6332c86aeaf624d3c540037772a);

266

[ 268](structbt__bap__scan__delegator__recv__state.md#a6153ea6bbfe7057c39f6b652a4e6e34e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__bap__scan__delegator__recv__state.md#a6153ea6bbfe7057c39f6b652a4e6e34e);

269

[ 271](structbt__bap__scan__delegator__recv__state.md#aa03e02a1832950e4a53ff2fe803c14a6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__bap__scan__delegator__recv__state.md#aa03e02a1832950e4a53ff2fe803c14a6);

272

[ 274](structbt__bap__scan__delegator__recv__state.md#a30fbad06780fd7bca9aacdf14ecaf4a0) enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) [pa\_sync\_state](structbt__bap__scan__delegator__recv__state.md#a30fbad06780fd7bca9aacdf14ecaf4a0);

275

[ 277](structbt__bap__scan__delegator__recv__state.md#ac770a5ad001f73d3acaf2b36827f9343) enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) [encrypt\_state](structbt__bap__scan__delegator__recv__state.md#ac770a5ad001f73d3acaf2b36827f9343);

278

[ 280](structbt__bap__scan__delegator__recv__state.md#abaa80f30cf2e84ee873d18eaedd4159d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__bap__scan__delegator__recv__state.md#abaa80f30cf2e84ee873d18eaedd4159d);

281

[ 286](structbt__bap__scan__delegator__recv__state.md#a3fb5ae9266643182798ef056d1569821) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bad\_code](structbt__bap__scan__delegator__recv__state.md#a3fb5ae9266643182798ef056d1569821)[[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)];

287

[ 289](structbt__bap__scan__delegator__recv__state.md#aa97765bdbaa43a280645eb62c0035b82) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__scan__delegator__recv__state.md#aa97765bdbaa43a280645eb62c0035b82);

290

[ 292](structbt__bap__scan__delegator__recv__state.md#ae674ccfdc1905f230b0f7a58cc553274) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) [subgroups](structbt__bap__scan__delegator__recv__state.md#ae674ccfdc1905f230b0f7a58cc553274)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS];

293};

294

[ 295](structbt__bap__scan__delegator__cb.md)struct [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md) {

[ 305](structbt__bap__scan__delegator__cb.md#a5d95631d95ae1085071c9b795eca1a8e) void (\*[recv\_state\_updated](structbt__bap__scan__delegator__cb.md#a5d95631d95ae1085071c9b795eca1a8e))(struct bt\_conn \*conn,

306 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state);

307

[ 329](structbt__bap__scan__delegator__cb.md#a0ea55963f92361f35e68eadcf10306b1) int (\*[pa\_sync\_req](structbt__bap__scan__delegator__cb.md#a0ea55963f92361f35e68eadcf10306b1))(struct bt\_conn \*conn,

330 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state,

331 bool past\_avail, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pa\_interval);

332

[ 346](structbt__bap__scan__delegator__cb.md#a5b918538cfe0edaa69155f891981eeae) int (\*[pa\_sync\_term\_req](structbt__bap__scan__delegator__cb.md#a5b918538cfe0edaa69155f891981eeae))(struct bt\_conn \*conn,

347 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state);

348

[ 360](structbt__bap__scan__delegator__cb.md#a8b0efda7e68164189b52f73abac025b8) void (\*[broadcast\_code](structbt__bap__scan__delegator__cb.md#a8b0efda7e68164189b52f73abac025b8))(struct bt\_conn \*conn,

361 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state,

362 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__bap__scan__delegator__cb.md#a8b0efda7e68164189b52f73abac025b8)[[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)]);

[ 384](structbt__bap__scan__delegator__cb.md#a959112080deec0ab2dcc2c09a6958874) int (\*[bis\_sync\_req](structbt__bap__scan__delegator__cb.md#a959112080deec0ab2dcc2c09a6958874))(struct bt\_conn \*conn,

385 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state,

386 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bis\_sync\_req](structbt__bap__scan__delegator__cb.md#a959112080deec0ab2dcc2c09a6958874)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]);

387};

388

[ 390](structbt__bap__ep__info.md)struct [bt\_bap\_ep\_info](structbt__bap__ep__info.md) {

[ 392](structbt__bap__ep__info.md#a07e8878e7e6a8ee059639330ffa78c1c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__bap__ep__info.md#a07e8878e7e6a8ee059639330ffa78c1c);

393

[ 395](structbt__bap__ep__info.md#a650727747d0a093528544c3e16255feb) enum [bt\_bap\_ep\_state](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a) [state](structbt__bap__ep__info.md#a650727747d0a093528544c3e16255feb);

396

[ 398](structbt__bap__ep__info.md#abb0dc6d25744cd734f8fd6ba2bc84b24) enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) [dir](structbt__bap__ep__info.md#abb0dc6d25744cd734f8fd6ba2bc84b24);

399

[ 401](structbt__bap__ep__info.md#abbad124bf9e40ed530b2a33fefbadc84) bool [can\_send](structbt__bap__ep__info.md#abbad124bf9e40ed530b2a33fefbadc84);

402

[ 406](structbt__bap__ep__info.md#a819ac77dcf7cb6985e97f290a666ed09) struct bt\_bap\_ep \*[paired\_ep](structbt__bap__ep__info.md#a819ac77dcf7cb6985e97f290a666ed09);

407};

408

[ 417](group__bt__bap.md#gaf15e5ec5bca364f6a3e7a43b1f27da68)int [bt\_bap\_ep\_get\_info](group__bt__bap.md#gaf15e5ec5bca364f6a3e7a43b1f27da68)(const struct bt\_bap\_ep \*ep, struct [bt\_bap\_ep\_info](structbt__bap__ep__info.md) \*info);

418

[ 427](structbt__bap__stream.md)struct [bt\_bap\_stream](structbt__bap__stream.md) {

[ 429](structbt__bap__stream.md#adb95fe7a0b981a46898382ee45fd99df) struct bt\_conn \*[conn](structbt__bap__stream.md#adb95fe7a0b981a46898382ee45fd99df);

430

[ 432](structbt__bap__stream.md#af871d28b2cca8e4deba66997badbeca2) struct bt\_bap\_ep \*[ep](structbt__bap__stream.md#af871d28b2cca8e4deba66997badbeca2);

433

[ 435](structbt__bap__stream.md#a2abf6e4d8cbbdbb6e2ccd705581484ed) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__bap__stream.md#a2abf6e4d8cbbdbb6e2ccd705581484ed);

436

[ 438](structbt__bap__stream.md#a854ff3dec732d17821fb304667e0518e) struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \*[qos](structbt__bap__stream.md#a854ff3dec732d17821fb304667e0518e);

439

[ 441](structbt__bap__stream.md#a46a1f70c1a1fe4696039be14adf3c9b6) struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*[ops](structbt__bap__stream.md#a46a1f70c1a1fe4696039be14adf3c9b6);

442

443#if defined(CONFIG\_BT\_BAP\_UNICAST\_CLIENT)

449 struct bt\_bap\_iso \*bap\_iso;

450#endif /\* CONFIG\_BT\_BAP\_UNICAST\_CLIENT \*/

451

[ 453](structbt__bap__stream.md#a17d91a06d581cd4341d035eb76d8e0b2) void \*[group](structbt__bap__stream.md#a17d91a06d581cd4341d035eb76d8e0b2);

454

[ 456](structbt__bap__stream.md#afe81620dd215aebe04ddc9e36dc7d2dd) void \*[user\_data](structbt__bap__stream.md#afe81620dd215aebe04ddc9e36dc7d2dd);

457

458#if defined(CONFIG\_BT\_BAP\_DEBUG\_STREAM\_SEQ\_NUM)

459 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_prev\_seq\_num;

460#endif /\* CONFIG\_BT\_BAP\_DEBUG\_STREAM\_SEQ\_NUM \*/

461

462 /\* Internally used list node \*/

463 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

464};

465

[ 467](structbt__bap__stream__ops.md)struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) {

468#if defined(CONFIG\_BT\_BAP\_UNICAST)

477 void (\*configured)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream,

478 const struct [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) \*pref);

479

488 void (\*qos\_set)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

489

497 void (\*enabled)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

498

507 void (\*metadata\_updated)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

508

516 void (\*disabled)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

517

526 void (\*released)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

527#endif /\* CONFIG\_BT\_BAP\_UNICAST \*/

528

[ 537](structbt__bap__stream__ops.md#a7f595e37d40b94510bf09c1f82b479f3) void (\*[started](structbt__bap__stream__ops.md#a7f595e37d40b94510bf09c1f82b479f3))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

538

[ 547](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5) void (\*[stopped](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

548

549#if defined(CONFIG\_BT\_AUDIO\_RX)

561 void (\*[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_iso\_recv\_info](structbt__iso__recv__info.md) \*info,

562 struct [net\_buf](structnet__buf.md) \*buf);

563#endif /\* CONFIG\_BT\_AUDIO\_RX \*/

564

565#if defined(CONFIG\_BT\_AUDIO\_TX)

578 void (\*sent)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

579#endif /\* CONFIG\_BT\_AUDIO\_TX \*/

580

[ 593](structbt__bap__stream__ops.md#a533d5ea96aa67b9b74b19c55afd43df1) void (\*[connected](structbt__bap__stream__ops.md#a533d5ea96aa67b9b74b19c55afd43df1))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

594

[ 607](structbt__bap__stream__ops.md#a953c7174297f1a27ceed012dced53c5a) void (\*[disconnected](structbt__bap__stream__ops.md#a953c7174297f1a27ceed012dced53c5a))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

608};

609

[ 618](group__bt__bap.md#gab29c1e134156dceaa6c67abae9239378)void [bt\_bap\_stream\_cb\_register](group__bt__bap.md#gab29c1e134156dceaa6c67abae9239378)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*[ops](structbt__bap__stream.md#a46a1f70c1a1fe4696039be14adf3c9b6));

619

[ 633](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402)int [bt\_bap\_stream\_config](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402)(struct bt\_conn \*[conn](structbt__bap__stream.md#adb95fe7a0b981a46898382ee45fd99df), struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct bt\_bap\_ep \*[ep](structbt__bap__stream.md#af871d28b2cca8e4deba66997badbeca2),

634 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__bap__stream.md#a2abf6e4d8cbbdbb6e2ccd705581484ed));

635

[ 649](group__bt__bap.md#gaac84ee7b3ab5578d258848754f752546)int [bt\_bap\_stream\_reconfig](group__bt__bap.md#gaac84ee7b3ab5578d258848754f752546)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__bap__stream.md#a2abf6e4d8cbbdbb6e2ccd705581484ed));

650

[ 663](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d)int [bt\_bap\_stream\_qos](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d)(struct bt\_conn \*[conn](structbt__bap__stream.md#adb95fe7a0b981a46898382ee45fd99df), struct bt\_bap\_unicast\_group \*[group](structbt__bap__stream.md#a17d91a06d581cd4341d035eb76d8e0b2));

664

[ 679](group__bt__bap.md#ga13a859b31b0310ec22339ec7ed0754f8)int [bt\_bap\_stream\_enable](group__bt__bap.md#ga13a859b31b0310ec22339ec7ed0754f8)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

680

[ 692](group__bt__bap.md#ga0afe6c927729697e2f984cefcbc7c0f1)int [bt\_bap\_stream\_metadata](group__bt__bap.md#ga0afe6c927729697e2f984cefcbc7c0f1)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

693

[ 706](group__bt__bap.md#ga0fd2bb35909fc19e3e9cff068ba9e9aa)int [bt\_bap\_stream\_disable](group__bt__bap.md#ga0fd2bb35909fc19e3e9cff068ba9e9aa)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

707

[ 732](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae)int [bt\_bap\_stream\_start](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

733

[ 747](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b)int [bt\_bap\_stream\_stop](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

748

[ 762](group__bt__bap.md#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)int [bt\_bap\_stream\_release](group__bt__bap.md#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

763

[ 778](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e)int [bt\_bap\_stream\_send](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num);

779

[ 796](group__bt__bap.md#gaa0e012446238c916abc84d6c0de89bf3)int [bt\_bap\_stream\_send\_ts](group__bt__bap.md#gaa0e012446238c916abc84d6c0de89bf3)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num,

797 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

798

[ 817](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928)int [bt\_bap\_stream\_get\_tx\_sync](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info);

818

824

[ 826](structbt__bap__unicast__server__cb.md)struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) {

[ 845](structbt__bap__unicast__server__cb.md#ada4b8b6a9371291a29068dcab05c17b2) int (\*[config](structbt__bap__unicast__server__cb.md#ada4b8b6a9371291a29068dcab05c17b2))(struct bt\_conn \*conn, const struct bt\_bap\_ep \*ep, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

846 const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, struct [bt\_bap\_stream](structbt__bap__stream.md) \*\*stream,

847 struct [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) \*const pref, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

848

[ 865](structbt__bap__unicast__server__cb.md#a0bafd8a52b3ae0b111c9a2e371d9cc62) int (\*[reconfig](structbt__bap__unicast__server__cb.md#a0bafd8a52b3ae0b111c9a2e371d9cc62))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

866 const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

867 struct [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) \*const pref, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

868

[ 882](structbt__bap__unicast__server__cb.md#a851c6095e29ccc057d211d45a9a60a66) int (\*[qos](structbt__bap__unicast__server__cb.md#a851c6095e29ccc057d211d45a9a60a66))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \*[qos](structbt__bap__unicast__server__cb.md#a851c6095e29ccc057d211d45a9a60a66),

883 struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

884

[ 898](structbt__bap__unicast__server__cb.md#a7424079675204fba02339ddc661b77c5) int (\*[enable](structbt__bap__unicast__server__cb.md#a7424079675204fba02339ddc661b77c5))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len,

899 struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

900

[ 912](structbt__bap__unicast__server__cb.md#a48fb3021507a708a0847a1ebec6075ba) int (\*[start](structbt__bap__unicast__server__cb.md#a48fb3021507a708a0847a1ebec6075ba))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

913

[ 927](structbt__bap__unicast__server__cb.md#a5fe98295e41c426a12ab4a7875b665c8) int (\*[metadata](structbt__bap__unicast__server__cb.md#a5fe98295e41c426a12ab4a7875b665c8))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len,

928 struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

929

[ 941](structbt__bap__unicast__server__cb.md#a22f1af95f055bce79e3810b9682024cf) int (\*[disable](structbt__bap__unicast__server__cb.md#a22f1af95f055bce79e3810b9682024cf))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

942

[ 954](structbt__bap__unicast__server__cb.md#a932296643929403c11512ff4ee7f7879) int (\*[stop](structbt__bap__unicast__server__cb.md#a932296643929403c11512ff4ee7f7879))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

955

[ 968](structbt__bap__unicast__server__cb.md#a9f5169f0bcdb3a6560f0767ec117b3c6) int (\*[release](structbt__bap__unicast__server__cb.md#a9f5169f0bcdb3a6560f0767ec117b3c6))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

969};

970

[ 981](group__bt__bap__unicast__server.md#ga7669133936bc13f7ab38817db9ce69c0)int [bt\_bap\_unicast\_server\_register\_cb](group__bt__bap__unicast__server.md#ga7669133936bc13f7ab38817db9ce69c0)(const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \*cb);

982

[ 993](group__bt__bap__unicast__server.md#gadf984f12bdeadcfc814dc2fc770cb7bf)int [bt\_bap\_unicast\_server\_unregister\_cb](group__bt__bap__unicast__server.md#gadf984f12bdeadcfc814dc2fc770cb7bf)(const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \*cb);

994

[ 1002](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1)typedef void (\*[bt\_bap\_ep\_func\_t](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1))(struct bt\_bap\_ep \*ep, void \*user\_data);

1003

[ 1011](group__bt__bap__unicast__server.md#ga4614a504d47cf732b09d4f22302d3239)void [bt\_bap\_unicast\_server\_foreach\_ep](group__bt__bap__unicast__server.md#ga4614a504d47cf732b09d4f22302d3239)(struct bt\_conn \*conn, [bt\_bap\_ep\_func\_t](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1) func, void \*user\_data);

1012

[ 1023](group__bt__bap__unicast__server.md#gaf0f06f2536d1e108691fba87b234a7f4)int [bt\_bap\_unicast\_server\_config\_ase](group__bt__bap__unicast__server.md#gaf0f06f2536d1e108691fba87b234a7f4)(struct bt\_conn \*conn, struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream,

1024 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1025 const struct [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) \*qos\_pref);

1026 /\* End of group bt\_bap\_unicast\_server \*/

1028

1034

[ 1036](structbt__bap__unicast__group__stream__param.md)struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) {

[ 1038](structbt__bap__unicast__group__stream__param.md#acfa192fed73b27fb194881f0021fcb35) struct [bt\_bap\_stream](structbt__bap__stream.md) \*[stream](structbt__bap__unicast__group__stream__param.md#acfa192fed73b27fb194881f0021fcb35);

1039

[ 1041](structbt__bap__unicast__group__stream__param.md#a570776d2b689a76884331a0bc00e50ec) struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \*[qos](structbt__bap__unicast__group__stream__param.md#a570776d2b689a76884331a0bc00e50ec);

1042};

1043

[ 1049](structbt__bap__unicast__group__stream__pair__param.md)struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) {

[ 1051](structbt__bap__unicast__group__stream__pair__param.md#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d) struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) \*[rx\_param](structbt__bap__unicast__group__stream__pair__param.md#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d);

1052

[ 1054](structbt__bap__unicast__group__stream__pair__param.md#ae73a11aab16a60806d1a941306c1822a) struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) \*[tx\_param](structbt__bap__unicast__group__stream__pair__param.md#ae73a11aab16a60806d1a941306c1822a);

1055};

1056

[ 1057](structbt__bap__unicast__group__param.md)struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) {

[ 1059](structbt__bap__unicast__group__param.md#a9cd09b720fa9a31364878ba205b3b58c) size\_t [params\_count](structbt__bap__unicast__group__param.md#a9cd09b720fa9a31364878ba205b3b58c);

1060

[ 1062](structbt__bap__unicast__group__param.md#aefae7dfccdaed2bc3f59ca63689d4f2e) struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) \*[params](structbt__bap__unicast__group__param.md#aefae7dfccdaed2bc3f59ca63689d4f2e);

1063

[ 1070](structbt__bap__unicast__group__param.md#a6829c82346ca70772a4ab0dc93fbb88f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__bap__unicast__group__param.md#a6829c82346ca70772a4ab0dc93fbb88f);

1071

1072#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS)

1080 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) c\_to\_p\_ft;

1081

1089 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) p\_to\_c\_ft;

1090

1098 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) iso\_interval;

1099#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

1100};

1101

[ 1113](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21)int [bt\_bap\_unicast\_group\_create](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21)(struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \*param,

1114 struct bt\_bap\_unicast\_group \*\*unicast\_group);

1115

[ 1135](group__bt__bap__unicast__client.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6)int [bt\_bap\_unicast\_group\_add\_streams](group__bt__bap__unicast__client.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6)(struct bt\_bap\_unicast\_group \*unicast\_group,

1136 struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) params[],

1137 size\_t num\_param);

1138

[ 1149](group__bt__bap__unicast__client.md#ga34dbdce6133f8366df453ec937fb47d2)int [bt\_bap\_unicast\_group\_delete](group__bt__bap__unicast__client.md#ga34dbdce6133f8366df453ec937fb47d2)(struct bt\_bap\_unicast\_group \*unicast\_group);

1150

[ 1152](structbt__bap__unicast__client__cb.md)struct [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) {

[ 1165](structbt__bap__unicast__client__cb.md#a64546cd17ac346dcb4bbfad5bd9f9616) void (\*[location](structbt__bap__unicast__client__cb.md#a64546cd17ac346dcb4bbfad5bd9f9616))(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) loc);

1166

[ 1179](structbt__bap__unicast__client__cb.md#ac49c3b8283552213623608498a7befd2) void (\*[available\_contexts](structbt__bap__unicast__client__cb.md#ac49c3b8283552213623608498a7befd2))(struct bt\_conn \*conn, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) snk\_ctx,

1180 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) src\_ctx);

1181

[ 1191](structbt__bap__unicast__client__cb.md#ae5c31f2540eb39c5b8272b5ae1e867fd) void (\*[config](structbt__bap__unicast__client__cb.md#ae5c31f2540eb39c5b8272b5ae1e867fd))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1192 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1193

[ 1206](structbt__bap__unicast__client__cb.md#a23b82e9f4174bcc2130d6f4570990180) void (\*[qos](structbt__bap__unicast__client__cb.md#a23b82e9f4174bcc2130d6f4570990180))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1207 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1208

[ 1219](structbt__bap__unicast__client__cb.md#a15dd1277b37dcd96a545bb6d450c2f9d) void (\*[enable](structbt__bap__unicast__client__cb.md#a15dd1277b37dcd96a545bb6d450c2f9d))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1220 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1221

[ 1234](structbt__bap__unicast__client__cb.md#a5c2d9ec444699ae5c75736115aab0b71) void (\*[start](structbt__bap__unicast__client__cb.md#a5c2d9ec444699ae5c75736115aab0b71))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1235 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1236

[ 1249](structbt__bap__unicast__client__cb.md#abf8ec1b630220172887e3d3d4c550992) void (\*[stop](structbt__bap__unicast__client__cb.md#abf8ec1b630220172887e3d3d4c550992))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1250 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1251

[ 1262](structbt__bap__unicast__client__cb.md#a47f86af7675fcf6ac86fad578437afa9) void (\*[disable](structbt__bap__unicast__client__cb.md#a47f86af7675fcf6ac86fad578437afa9))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1263 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1264

[ 1275](structbt__bap__unicast__client__cb.md#a7b5fcba437b1532dbac796a48fee2f6a) void (\*[metadata](structbt__bap__unicast__client__cb.md#a7b5fcba437b1532dbac796a48fee2f6a))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1276 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1277

[ 1288](structbt__bap__unicast__client__cb.md#a7dc1f2486bdabf37b85d0b347563e314) void (\*[release](structbt__bap__unicast__client__cb.md#a7dc1f2486bdabf37b85d0b347563e314))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1289 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1290

[ 1305](structbt__bap__unicast__client__cb.md#a3c55f4e23607b1e655b5f520d691bf33) void (\*[pac\_record](structbt__bap__unicast__client__cb.md#a3c55f4e23607b1e655b5f520d691bf33))(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

1306 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1307

[ 1319](structbt__bap__unicast__client__cb.md#ae473ecc92b5c02a29742d0ba0c51ef4a) void (\*[endpoint](structbt__bap__unicast__client__cb.md#ae473ecc92b5c02a29742d0ba0c51ef4a))(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct bt\_bap\_ep \*ep);

1320

[ 1333](structbt__bap__unicast__client__cb.md#a1f2f7476506b6b798c1f26371217956e) void (\*[discover](structbt__bap__unicast__client__cb.md#a1f2f7476506b6b798c1f26371217956e))(struct bt\_conn \*conn, int err, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir);

1334};

1335

[ 1346](group__bt__bap__unicast__client.md#gae598c65d7c5d419ee941d7cf33601a64)int [bt\_bap\_unicast\_client\_register\_cb](group__bt__bap__unicast__client.md#gae598c65d7c5d419ee941d7cf33601a64)(const struct [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) \*cb);

1347

[ 1357](group__bt__bap__unicast__client.md#gacef9c88f66762e8de19303d20dafa0bb)int [bt\_bap\_unicast\_client\_discover](group__bt__bap__unicast__client.md#gacef9c88f66762e8de19303d20dafa0bb)(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir);

1358 /\* End of group bt\_bap\_unicast\_client \*/

1366

1368struct bt\_bap\_base\_subgroup;

1370struct bt\_bap\_base;

1371

[ 1373](structbt__bap__base__codec__id.md)struct [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) {

[ 1375](structbt__bap__base__codec__id.md#a9031aaf6a3f6e0acf68f1bfaed39b819) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__bap__base__codec__id.md#a9031aaf6a3f6e0acf68f1bfaed39b819);

[ 1377](structbt__bap__base__codec__id.md#a0aadd7e53f72efd8c0e33dd9a8eca177) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__bap__base__codec__id.md#a0aadd7e53f72efd8c0e33dd9a8eca177);

[ 1379](structbt__bap__base__codec__id.md#a49802819cc3129a993320b95472f2262) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__bap__base__codec__id.md#a49802819cc3129a993320b95472f2262);

1380};

1381

[ 1383](structbt__bap__base__subgroup__bis.md)struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) {

1384 /\* Unique index of the BIS \*/

[ 1385](structbt__bap__base__subgroup__bis.md#ad0f5dff3150c36b1625f1f6f206d41d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structbt__bap__base__subgroup__bis.md#ad0f5dff3150c36b1625f1f6f206d41d2);

[ 1387](structbt__bap__base__subgroup__bis.md#ac4132c798c04c0f93c944dc91891221e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__bap__base__subgroup__bis.md#ac4132c798c04c0f93c944dc91891221e);

[ 1389](structbt__bap__base__subgroup__bis.md#aa53f22b29e447822e8bb36d9245bfc77) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__bap__base__subgroup__bis.md#aa53f22b29e447822e8bb36d9245bfc77);

1390};

1391

[ 1400](group__bt__bap__broadcast.md#ga29423a39d76ad16f0586d82a23c07ba7)const struct bt\_bap\_base \*[bt\_bap\_base\_get\_base\_from\_ad](group__bt__bap__broadcast.md#ga29423a39d76ad16f0586d82a23c07ba7)(const struct [bt\_data](structbt__data.md) \*ad);

1401

[ 1410](group__bt__bap__broadcast.md#gaf91f45bcf7df2f368c5abeb116b65dd0)int [bt\_bap\_base\_get\_pres\_delay](group__bt__bap__broadcast.md#gaf91f45bcf7df2f368c5abeb116b65dd0)(const struct bt\_bap\_base \*base);

1411

[ 1420](group__bt__bap__broadcast.md#gadcae0230168564da1ee8b3c577ce27d7)int [bt\_bap\_base\_get\_subgroup\_count](group__bt__bap__broadcast.md#gadcae0230168564da1ee8b3c577ce27d7)(const struct bt\_bap\_base \*base);

1421

[ 1431](group__bt__bap__broadcast.md#ga6deab5a8b7a16ddf0c3685d4003694e1)int [bt\_bap\_base\_get\_bis\_indexes](group__bt__bap__broadcast.md#ga6deab5a8b7a16ddf0c3685d4003694e1)(const struct bt\_bap\_base \*base, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bis\_indexes);

1432

[ 1444](group__bt__bap__broadcast.md#ga5e6e0b758409cbdde93c0f648ef5e5e8)int [bt\_bap\_base\_foreach\_subgroup](group__bt__bap__broadcast.md#ga5e6e0b758409cbdde93c0f648ef5e5e8)(const struct bt\_bap\_base \*base,

1445 bool (\*func)(const struct bt\_bap\_base\_subgroup \*subgroup,

1446 void \*user\_data),

1447 void \*user\_data);

1448

[ 1458](group__bt__bap__broadcast.md#gae75e05a002dee8336eb066ae8231ea0c)int [bt\_bap\_base\_get\_subgroup\_codec\_id](group__bt__bap__broadcast.md#gae75e05a002dee8336eb066ae8231ea0c)(const struct bt\_bap\_base\_subgroup \*subgroup,

1459 struct [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) \*codec\_id);

1460

[ 1470](group__bt__bap__broadcast.md#ga10e2e32dc2802ba55d55c77148331f6a)int [bt\_bap\_base\_get\_subgroup\_codec\_data](group__bt__bap__broadcast.md#ga10e2e32dc2802ba55d55c77148331f6a)(const struct bt\_bap\_base\_subgroup \*subgroup,

1471 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1472

[ 1482](group__bt__bap__broadcast.md#gafb9d9544f38c7ad2613fff1679eb1f0c)int [bt\_bap\_base\_get\_subgroup\_codec\_meta](group__bt__bap__broadcast.md#gafb9d9544f38c7ad2613fff1679eb1f0c)(const struct bt\_bap\_base\_subgroup \*subgroup,

1483 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*meta);

1484

[ 1495](group__bt__bap__broadcast.md#ga920e3409f1978b803bcf6bc8d05ac8f6)int [bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg](group__bt__bap__broadcast.md#ga920e3409f1978b803bcf6bc8d05ac8f6)(const struct bt\_bap\_base\_subgroup \*subgroup,

1496 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1497

[ 1506](group__bt__bap__broadcast.md#ga051e1f8aa2faf3ba7a973356138fd2d3)int [bt\_bap\_base\_get\_subgroup\_bis\_count](group__bt__bap__broadcast.md#ga051e1f8aa2faf3ba7a973356138fd2d3)(const struct bt\_bap\_base\_subgroup \*subgroup);

1507

[ 1519](group__bt__bap__broadcast.md#ga4f85ee43984cb2f3139b41da7b9b1aee)int [bt\_bap\_base\_subgroup\_foreach\_bis](group__bt__bap__broadcast.md#ga4f85ee43984cb2f3139b41da7b9b1aee)(const struct bt\_bap\_base\_subgroup \*subgroup,

1520 bool (\*func)(const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis,

1521 void \*user\_data),

1522 void \*user\_data);

1523

[ 1537](group__bt__bap__broadcast.md#gaa5cb191df7807ea87f1fba1871ca8ebe)int [bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg](group__bt__bap__broadcast.md#gaa5cb191df7807ea87f1fba1871ca8ebe)(const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis,

1538 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1539 /\* End of group bt\_bap\_broadcast \*/

1541

1548

[ 1550](structbt__bap__broadcast__source__stream__param.md)struct [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md) {

[ 1552](structbt__bap__broadcast__source__stream__param.md#a9c92fb50b62d963e01b1506b790fb5e1) struct [bt\_bap\_stream](structbt__bap__stream.md) \*[stream](structbt__bap__broadcast__source__stream__param.md#a9c92fb50b62d963e01b1506b790fb5e1);

1553

1554#if CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0

1560 size\_t data\_len;

1561

1563 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data;

1564#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0 \*/

1565};

1566

[ 1568](structbt__bap__broadcast__source__subgroup__param.md)struct [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md) {

[ 1570](structbt__bap__broadcast__source__subgroup__param.md#a701d9480ffae2351149de6b962095d32) size\_t [params\_count](structbt__bap__broadcast__source__subgroup__param.md#a701d9480ffae2351149de6b962095d32);

1571

[ 1573](structbt__bap__broadcast__source__subgroup__param.md#a9719e89d8979f9502023e0032814c477) struct [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md) \*[params](structbt__bap__broadcast__source__subgroup__param.md#a9719e89d8979f9502023e0032814c477);

1574

[ 1576](structbt__bap__broadcast__source__subgroup__param.md#a1986239ea2ed5204d8f46a6500d5900d) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__bap__broadcast__source__subgroup__param.md#a1986239ea2ed5204d8f46a6500d5900d);

1577};

1578

[ 1580](structbt__bap__broadcast__source__param.md)struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) {

[ 1582](structbt__bap__broadcast__source__param.md#a5e155c3b92b4f9de3c9e6efa377097e3) size\_t [params\_count](structbt__bap__broadcast__source__param.md#a5e155c3b92b4f9de3c9e6efa377097e3);

1583

[ 1585](structbt__bap__broadcast__source__param.md#a6291842b49a55f6b2767dc95c9e874f3) struct [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md) \*[params](structbt__bap__broadcast__source__param.md#a6291842b49a55f6b2767dc95c9e874f3);

1586

[ 1588](structbt__bap__broadcast__source__param.md#af969b5aacd4743bae608a7f54c0556e9) struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \*[qos](structbt__bap__broadcast__source__param.md#af969b5aacd4743bae608a7f54c0556e9);

1589

[ 1597](structbt__bap__broadcast__source__param.md#a493fa57a80e21a288854b2e3e1df775a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__bap__broadcast__source__param.md#a493fa57a80e21a288854b2e3e1df775a);

1598

[ 1600](structbt__bap__broadcast__source__param.md#a7552bf9a4ff5441b13669effe23abb8c) bool [encryption](structbt__bap__broadcast__source__param.md#a7552bf9a4ff5441b13669effe23abb8c);

1601

[ 1612](structbt__bap__broadcast__source__param.md#acc096d55aaeb419a356ab5c023928df6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__bap__broadcast__source__param.md#acc096d55aaeb419a356ab5c023928df6)[[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)];

1613

1614#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS)

1622 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irc;

1623

1630 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pto;

1631

1639 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) iso\_interval;

1640#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

1641};

1642

[ 1659](group__bt__bap__broadcast__source.md#gacdebfc435eebd47cf9cd05099a5f78e0)int [bt\_bap\_broadcast\_source\_create](group__bt__bap__broadcast__source.md#gacdebfc435eebd47cf9cd05099a5f78e0)(struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \*param,

1660 struct bt\_bap\_broadcast\_source \*\*source);

1661

[ 1681](group__bt__bap__broadcast__source.md#gabecaa9db7be5cb03ed997ba478878d40)int [bt\_bap\_broadcast\_source\_reconfig](group__bt__bap__broadcast__source.md#gabecaa9db7be5cb03ed997ba478878d40)(struct bt\_bap\_broadcast\_source \*source,

1682 struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \*param);

1683

[ 1696](group__bt__bap__broadcast__source.md#gaff2cfdadbff3ebe1e2efb660dee56f02)int [bt\_bap\_broadcast\_source\_update\_metadata](group__bt__bap__broadcast__source.md#gaff2cfdadbff3ebe1e2efb660dee56f02)(struct bt\_bap\_broadcast\_source \*source,

1697 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

1698

[ 1710](group__bt__bap__broadcast__source.md#gac4640f5207599d51c1a63ff47f3c1d5a)int [bt\_bap\_broadcast\_source\_start](group__bt__bap__broadcast__source.md#gac4640f5207599d51c1a63ff47f3c1d5a)(struct bt\_bap\_broadcast\_source \*source,

1711 struct bt\_le\_ext\_adv \*adv);

1712

[ 1723](group__bt__bap__broadcast__source.md#ga36a885581eec5cab8b3f652db19b9aba)int [bt\_bap\_broadcast\_source\_stop](group__bt__bap__broadcast__source.md#ga36a885581eec5cab8b3f652db19b9aba)(struct bt\_bap\_broadcast\_source \*source);

1724

[ 1735](group__bt__bap__broadcast__source.md#ga12e0a4856115a8eb297fe2d1fc130155)int [bt\_bap\_broadcast\_source\_delete](group__bt__bap__broadcast__source.md#ga12e0a4856115a8eb297fe2d1fc130155)(struct bt\_bap\_broadcast\_source \*source);

1736

[ 1750](group__bt__bap__broadcast__source.md#ga118bc35af0b1db024e7aada5da65b796)int [bt\_bap\_broadcast\_source\_get\_id](group__bt__bap__broadcast__source.md#ga118bc35af0b1db024e7aada5da65b796)(struct bt\_bap\_broadcast\_source \*source,

1751 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const broadcast\_id);

1752

[ 1767](group__bt__bap__broadcast__source.md#gafe07e4c6962858500fcf66415a173be8)int [bt\_bap\_broadcast\_source\_get\_base](group__bt__bap__broadcast__source.md#gafe07e4c6962858500fcf66415a173be8)(struct bt\_bap\_broadcast\_source \*source,

1768 struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf);

1769 /\* End of bt\_bap\_broadcast\_source \*/

1771

1778

[ 1780](structbt__bap__broadcast__sink__cb.md)struct [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) {

[ 1790](structbt__bap__broadcast__sink__cb.md#a1adf2124ec9a16c3c68774194febd0fc) void (\*[base\_recv](structbt__bap__broadcast__sink__cb.md#a1adf2124ec9a16c3c68774194febd0fc))(struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_bap\_base \*base,

1791 size\_t base\_size);

1792

[ 1804](structbt__bap__broadcast__sink__cb.md#ac2c8389a8e68e5b4afe735f623dc36ec) void (\*[syncable](structbt__bap__broadcast__sink__cb.md#ac2c8389a8e68e5b4afe735f623dc36ec))(struct bt\_bap\_broadcast\_sink \*sink, bool encrypted);

1805

1806 /\* Internally used list node \*/

1807 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

1808};

1809

[ 1814](group__bt__bap__broadcast__sink.md#ga1b83ead634d990e954f233d0208c5a85)int [bt\_bap\_broadcast\_sink\_register\_cb](group__bt__bap__broadcast__sink.md#ga1b83ead634d990e954f233d0208c5a85)(struct [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) \*cb);

1815

[ 1834](group__bt__bap__broadcast__sink.md#ga0637d1957db70ad39e0608ed07e75166)int [bt\_bap\_broadcast\_sink\_create](group__bt__bap__broadcast__sink.md#ga0637d1957db70ad39e0608ed07e75166)(struct bt\_le\_per\_adv\_sync \*pa\_sync, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) broadcast\_id,

1835 struct bt\_bap\_broadcast\_sink \*\*sink);

1836

[ 1855](group__bt__bap__broadcast__sink.md#ga3485ef8527928209274ae0b5351b72b3)int [bt\_bap\_broadcast\_sink\_sync](group__bt__bap__broadcast__sink.md#ga3485ef8527928209274ae0b5351b72b3)(struct bt\_bap\_broadcast\_sink \*sink, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) indexes\_bitfield,

1856 struct [bt\_bap\_stream](structbt__bap__stream.md) \*streams[], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[16]);

1857

[ 1867](group__bt__bap__broadcast__sink.md#ga1020b21bfb4195aeb5823197145b1fe9)int [bt\_bap\_broadcast\_sink\_stop](group__bt__bap__broadcast__sink.md#ga1020b21bfb4195aeb5823197145b1fe9)(struct bt\_bap\_broadcast\_sink \*sink);

1868

[ 1879](group__bt__bap__broadcast__sink.md#ga8b9d6cb409a3671654e053475ada3fda)int [bt\_bap\_broadcast\_sink\_delete](group__bt__bap__broadcast__sink.md#ga8b9d6cb409a3671654e053475ada3fda)(struct bt\_bap\_broadcast\_sink \*sink);

1880 /\* End of group bt\_bap\_broadcast\_sink \*/

1882

[ 1888](group__bt__bap.md#ga5841f00a46c8b32bc8253d70dc05f104)void [bt\_bap\_scan\_delegator\_register\_cb](group__bt__bap.md#ga5841f00a46c8b32bc8253d70dc05f104)(struct [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md) \*cb);

1889

[ 1903](group__bt__bap.md#ga381c1f3b386ecbdfd570eb125882161e)int [bt\_bap\_scan\_delegator\_set\_pa\_state](group__bt__bap.md#ga381c1f3b386ecbdfd570eb125882161e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id,

1904 enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) pa\_state);

1905

[ 1914](group__bt__bap.md#ga7cce7e53264294abec4421364afffdbe)int [bt\_bap\_scan\_delegator\_set\_bis\_sync\_state](group__bt__bap.md#ga7cce7e53264294abec4421364afffdbe)(

1915 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id,

1916 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bis\_synced[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]);

1917

[ 1918](structbt__bap__scan__delegator__add__src__param.md)struct [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) {

[ 1920](structbt__bap__scan__delegator__add__src__param.md#a7e2ae6194fe7878e6f8d4967f005c7aa) struct bt\_le\_per\_adv\_sync \*[pa\_sync](structbt__bap__scan__delegator__add__src__param.md#a7e2ae6194fe7878e6f8d4967f005c7aa);

1921

[ 1923](structbt__bap__scan__delegator__add__src__param.md#a502d263982995c99559714f07d74443f) enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) [encrypt\_state](structbt__bap__scan__delegator__add__src__param.md#a502d263982995c99559714f07d74443f);

1924

[ 1926](structbt__bap__scan__delegator__add__src__param.md#a8e8eda4139e460800c6195b4c5f246e2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__bap__scan__delegator__add__src__param.md#a8e8eda4139e460800c6195b4c5f246e2);

1927

[ 1929](structbt__bap__scan__delegator__add__src__param.md#a12bed26ffdc9d4683a5fcdf512a194eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__scan__delegator__add__src__param.md#a12bed26ffdc9d4683a5fcdf512a194eb);

1930

[ 1932](structbt__bap__scan__delegator__add__src__param.md#a9153dbdef5b507ef14e73a188cb00ae1) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) [subgroups](structbt__bap__scan__delegator__add__src__param.md#a9153dbdef5b507ef14e73a188cb00ae1)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS];

1933};

1934

[ 1948](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0)int [bt\_bap\_scan\_delegator\_add\_src](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0)(const struct [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) \*param);

1949

[ 1950](structbt__bap__scan__delegator__mod__src__param.md)struct [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) {

[ 1952](structbt__bap__scan__delegator__mod__src__param.md#ae387a2c0613545ae3acd372780f738bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__bap__scan__delegator__mod__src__param.md#ae387a2c0613545ae3acd372780f738bb);

1953

[ 1955](structbt__bap__scan__delegator__mod__src__param.md#aecc8b74632dcb2b17b9a358e00c75d31) enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) [encrypt\_state](structbt__bap__scan__delegator__mod__src__param.md#aecc8b74632dcb2b17b9a358e00c75d31);

1956

[ 1958](structbt__bap__scan__delegator__mod__src__param.md#a11b4c6d787bd2c828e565282daf5cf2f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__bap__scan__delegator__mod__src__param.md#a11b4c6d787bd2c828e565282daf5cf2f);

1959

[ 1961](structbt__bap__scan__delegator__mod__src__param.md#aa8dcd7983005ffd23779db6b6ccfb752) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__scan__delegator__mod__src__param.md#aa8dcd7983005ffd23779db6b6ccfb752);

1962

[ 1969](structbt__bap__scan__delegator__mod__src__param.md#a14ffee52751dd152b1a8cc0822d1702f) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) [subgroups](structbt__bap__scan__delegator__mod__src__param.md#a14ffee52751dd152b1a8cc0822d1702f)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS];

1970};

1971

[ 1985](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a)int [bt\_bap\_scan\_delegator\_mod\_src](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a)(const struct [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) \*param);

1986

[ 2000](group__bt__bap.md#ga6c240f1cdb33945197700e4fe106ef2c)int [bt\_bap\_scan\_delegator\_rem\_src](group__bt__bap.md#ga6c240f1cdb33945197700e4fe106ef2c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id);

2001

[ 2012](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824))(

2013 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, void \*user\_data);

2014

[ 2020](group__bt__bap.md#gab6f1a12699a9437c6575c70df33d5be0)void [bt\_bap\_scan\_delegator\_foreach\_state](group__bt__bap.md#gab6f1a12699a9437c6575c70df33d5be0)([bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824) func,

2021 void \*user\_data);

2022

[ 2030](group__bt__bap.md#gabec9fd0a2966e1811fd4770855050510)const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*[bt\_bap\_scan\_delegator\_find\_state](group__bt__bap.md#gabec9fd0a2966e1811fd4770855050510)(

2031 [bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824) func, void \*user\_data);

2032

2033/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* CLIENT API \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

2034

[ 2041](group__bt__bap.md#ga496c8a2f599d997a7e6e033bda5f0c36)typedef void (\*[bt\_bap\_broadcast\_assistant\_write\_cb](group__bt__bap.md#ga496c8a2f599d997a7e6e033bda5f0c36))(struct bt\_conn \*conn,

2042 int err);

2043

[ 2044](structbt__bap__broadcast__assistant__cb.md)struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) {

[ 2054](structbt__bap__broadcast__assistant__cb.md#a01ad0a89db9041670f6a68d6f1680988) void (\*[discover](structbt__bap__broadcast__assistant__cb.md#a01ad0a89db9041670f6a68d6f1680988))(struct bt\_conn \*conn, int err,

2055 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_state\_count);

2056

[ 2066](structbt__bap__broadcast__assistant__cb.md#ab88d98b1e742ccd36aac69069ebf3f61) void (\*[scan](structbt__bap__broadcast__assistant__cb.md#ab88d98b1e742ccd36aac69069ebf3f61))(const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info,

2067 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) broadcast\_id);

2068

[ 2078](structbt__bap__broadcast__assistant__cb.md#a629ff4299b8ae5bcbddf28338caddfd0) void (\*[recv\_state](structbt__bap__broadcast__assistant__cb.md#a629ff4299b8ae5bcbddf28338caddfd0))(struct bt\_conn \*conn, int err,

2079 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

2080

[ 2088](structbt__bap__broadcast__assistant__cb.md#ab0f09236e236d8456fcdee36b5871bfc) void (\*[recv\_state\_removed](structbt__bap__broadcast__assistant__cb.md#ab0f09236e236d8456fcdee36b5871bfc))(struct bt\_conn \*conn, int err,

2089 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id);

2090

[ 2097](structbt__bap__broadcast__assistant__cb.md#ad2bdfcc0147a751910d82232a77e34f8) void (\*[scan\_start](structbt__bap__broadcast__assistant__cb.md#ad2bdfcc0147a751910d82232a77e34f8))(struct bt\_conn \*conn, int err);

2098

[ 2105](structbt__bap__broadcast__assistant__cb.md#a80296a38e664aabff7ec27e007c59e95) void (\*[scan\_stop](structbt__bap__broadcast__assistant__cb.md#a80296a38e664aabff7ec27e007c59e95))(struct bt\_conn \*conn, int err);

2106

[ 2113](structbt__bap__broadcast__assistant__cb.md#ad909b9e6e3c35be10a29ee5a4b7213fb) void (\*[add\_src](structbt__bap__broadcast__assistant__cb.md#ad909b9e6e3c35be10a29ee5a4b7213fb))(struct bt\_conn \*conn, int err);

2114

[ 2121](structbt__bap__broadcast__assistant__cb.md#ab24e3ecb9764ca833524b787126b8c2c) void (\*[mod\_src](structbt__bap__broadcast__assistant__cb.md#ab24e3ecb9764ca833524b787126b8c2c))(struct bt\_conn \*conn, int err);

2122

[ 2129](structbt__bap__broadcast__assistant__cb.md#a09de9cb86dad76b485ff52257a0c68dc) void (\*[broadcast\_code](structbt__bap__broadcast__assistant__cb.md#a09de9cb86dad76b485ff52257a0c68dc))(struct bt\_conn \*conn, int err);

2130

[ 2137](structbt__bap__broadcast__assistant__cb.md#af0cf259088cd793152390b21813a9481) void (\*[rem\_src](structbt__bap__broadcast__assistant__cb.md#af0cf259088cd793152390b21813a9481))(struct bt\_conn \*conn, int err);

2138};

2139

[ 2149](group__bt__bap.md#gab59c5ebc4fef28da34d8a54b1244c33b)int [bt\_bap\_broadcast\_assistant\_discover](group__bt__bap.md#gab59c5ebc4fef28da34d8a54b1244c33b)(struct bt\_conn \*conn);

2150

[ 2168](group__bt__bap.md#ga98ac067e66d263aa41fc6f8df6bb9126)int [bt\_bap\_broadcast\_assistant\_scan\_start](group__bt__bap.md#ga98ac067e66d263aa41fc6f8df6bb9126)(struct bt\_conn \*conn,

2169 bool start\_scan);

2170

[ 2177](group__bt__bap.md#ga76cae35df980b78a10551811050b2760)int [bt\_bap\_broadcast\_assistant\_scan\_stop](group__bt__bap.md#ga76cae35df980b78a10551811050b2760)(struct bt\_conn \*conn);

2178

[ 2182](group__bt__bap.md#gafe741eb3ba1054ed81de71aafd5c03d8)void [bt\_bap\_broadcast\_assistant\_register\_cb](group__bt__bap.md#gafe741eb3ba1054ed81de71aafd5c03d8)(struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \*cb);

2183

[ 2185](structbt__bap__broadcast__assistant__add__src__param.md)struct [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) {

[ 2187](structbt__bap__broadcast__assistant__add__src__param.md#a2b04d75ca9a740a7d819eae1bcc5cba7) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__bap__broadcast__assistant__add__src__param.md#a2b04d75ca9a740a7d819eae1bcc5cba7);

2188

[ 2190](structbt__bap__broadcast__assistant__add__src__param.md#a390cd8d887cd256ee74b39b9b516cac4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__bap__broadcast__assistant__add__src__param.md#a390cd8d887cd256ee74b39b9b516cac4);

2191

[ 2193](structbt__bap__broadcast__assistant__add__src__param.md#ad9af814e8a232230d4ee97c459f47747) bool [pa\_sync](structbt__bap__broadcast__assistant__add__src__param.md#ad9af814e8a232230d4ee97c459f47747);

2194

[ 2196](structbt__bap__broadcast__assistant__add__src__param.md#ae50b6b5a3f2c92f01e7070c605b37dde) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__bap__broadcast__assistant__add__src__param.md#ae50b6b5a3f2c92f01e7070c605b37dde);

2197

[ 2203](structbt__bap__broadcast__assistant__add__src__param.md#acaecbbf7b3c96fe5ca53f90e92fa1e5e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pa\_interval](structbt__bap__broadcast__assistant__add__src__param.md#acaecbbf7b3c96fe5ca53f90e92fa1e5e);

2204

[ 2206](structbt__bap__broadcast__assistant__add__src__param.md#a17b67d65b6840c3d4480027b7deb31a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__broadcast__assistant__add__src__param.md#a17b67d65b6840c3d4480027b7deb31a5);

2207

[ 2209](structbt__bap__broadcast__assistant__add__src__param.md#ab8423e5cce4a6c9ac142221d2e816763) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) \*[subgroups](structbt__bap__broadcast__assistant__add__src__param.md#ab8423e5cce4a6c9ac142221d2e816763);

2210};

2211

[ 2220](group__bt__bap.md#gac93cb4cab33d0b937e752bc0b71cad9e)int [bt\_bap\_broadcast\_assistant\_add\_src](group__bt__bap.md#gac93cb4cab33d0b937e752bc0b71cad9e)(

2221 struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) \*param);

2222

[ 2224](structbt__bap__broadcast__assistant__mod__src__param.md)struct [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) {

[ 2226](structbt__bap__broadcast__assistant__mod__src__param.md#a5bc7c0a491872d655296bbb979402a62) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__bap__broadcast__assistant__mod__src__param.md#a5bc7c0a491872d655296bbb979402a62);

2227

[ 2229](structbt__bap__broadcast__assistant__mod__src__param.md#a794bb68c8a73edfe3d44dbe9a0bf2830) bool [pa\_sync](structbt__bap__broadcast__assistant__mod__src__param.md#a794bb68c8a73edfe3d44dbe9a0bf2830);

2230

[ 2236](structbt__bap__broadcast__assistant__mod__src__param.md#aebaa104384dcbec7bb952a27f3acc24d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pa\_interval](structbt__bap__broadcast__assistant__mod__src__param.md#aebaa104384dcbec7bb952a27f3acc24d);

2237

[ 2239](structbt__bap__broadcast__assistant__mod__src__param.md#a42b12c6d9f5c622433c9c1f0c72726c1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__broadcast__assistant__mod__src__param.md#a42b12c6d9f5c622433c9c1f0c72726c1);

2240

[ 2242](structbt__bap__broadcast__assistant__mod__src__param.md#a2383ec98b14054e0bc66bb4a0ae7b8b6) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) \*[subgroups](structbt__bap__broadcast__assistant__mod__src__param.md#a2383ec98b14054e0bc66bb4a0ae7b8b6);

2243};

2244

[ 2252](group__bt__bap.md#gaa9c292a7dcb470926d8d7d4be699a0c7)int [bt\_bap\_broadcast\_assistant\_mod\_src](group__bt__bap.md#gaa9c292a7dcb470926d8d7d4be699a0c7)(

2253 struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) \*param);

2254

[ 2263](group__bt__bap.md#ga0105535992cf66e55ab2587648fb571f)int [bt\_bap\_broadcast\_assistant\_set\_broadcast\_code](group__bt__bap.md#ga0105535992cf66e55ab2587648fb571f)(

2264 struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id,

2265 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)]);

2266

[ 2274](group__bt__bap.md#ga09785690db551677a043fcaa2fdb7f29)int [bt\_bap\_broadcast\_assistant\_rem\_src](group__bt__bap.md#ga09785690db551677a043fcaa2fdb7f29)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id);

2275

[ 2284](group__bt__bap.md#ga94fce2b4346b1026d53e0b860ca7fbf2)int [bt\_bap\_broadcast\_assistant\_read\_recv\_state](group__bt__bap.md#ga94fce2b4346b1026d53e0b860ca7fbf2)(struct bt\_conn \*conn,

2285 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx);

2286 /\* end of bt\_bap \*/

2288

2289#ifdef \_\_cplusplus

2290}

2291#endif

2292

2293#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_ \*/

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:888

[bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)

bt\_audio\_dir

Audio Capability type.

**Definition** audio.h:635

[bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)

bt\_audio\_location

Location values for BT Audio.

**Definition** audio.h:485

[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)

#define BT\_AUDIO\_BROADCAST\_CODE\_SIZE

**Definition** audio.h:42

[bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)

bt\_audio\_metadata\_type

Codec metadata type IDs.

**Definition** audio.h:350

[bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)

bt\_audio\_context

Audio Context Type for Generic Audio.

**Definition** audio.h:282

[bt\_bap\_broadcast\_sink\_create](group__bt__bap__broadcast__sink.md#ga0637d1957db70ad39e0608ed07e75166)

int bt\_bap\_broadcast\_sink\_create(struct bt\_le\_per\_adv\_sync \*pa\_sync, uint32\_t broadcast\_id, struct bt\_bap\_broadcast\_sink \*\*sink)

Create a Broadcast Sink from a periodic advertising sync.

[bt\_bap\_broadcast\_sink\_stop](group__bt__bap__broadcast__sink.md#ga1020b21bfb4195aeb5823197145b1fe9)

int bt\_bap\_broadcast\_sink\_stop(struct bt\_bap\_broadcast\_sink \*sink)

Stop audio broadcast sink.

[bt\_bap\_broadcast\_sink\_register\_cb](group__bt__bap__broadcast__sink.md#ga1b83ead634d990e954f233d0208c5a85)

int bt\_bap\_broadcast\_sink\_register\_cb(struct bt\_bap\_broadcast\_sink\_cb \*cb)

Register Broadcast sink callbacks \*.

[bt\_bap\_broadcast\_sink\_sync](group__bt__bap__broadcast__sink.md#ga3485ef8527928209274ae0b5351b72b3)

int bt\_bap\_broadcast\_sink\_sync(struct bt\_bap\_broadcast\_sink \*sink, uint32\_t indexes\_bitfield, struct bt\_bap\_stream \*streams[], const uint8\_t broadcast\_code[16])

Sync to a broadcaster's audio.

[bt\_bap\_broadcast\_sink\_delete](group__bt__bap__broadcast__sink.md#ga8b9d6cb409a3671654e053475ada3fda)

int bt\_bap\_broadcast\_sink\_delete(struct bt\_bap\_broadcast\_sink \*sink)

Release a broadcast sink.

[bt\_bap\_broadcast\_source\_get\_id](group__bt__bap__broadcast__source.md#ga118bc35af0b1db024e7aada5da65b796)

int bt\_bap\_broadcast\_source\_get\_id(struct bt\_bap\_broadcast\_source \*source, uint32\_t \*const broadcast\_id)

Get the broadcast ID of a broadcast source.

[bt\_bap\_broadcast\_source\_delete](group__bt__bap__broadcast__source.md#ga12e0a4856115a8eb297fe2d1fc130155)

int bt\_bap\_broadcast\_source\_delete(struct bt\_bap\_broadcast\_source \*source)

Delete audio broadcast source.

[bt\_bap\_broadcast\_source\_stop](group__bt__bap__broadcast__source.md#ga36a885581eec5cab8b3f652db19b9aba)

int bt\_bap\_broadcast\_source\_stop(struct bt\_bap\_broadcast\_source \*source)

Stop audio broadcast source.

[bt\_bap\_broadcast\_source\_reconfig](group__bt__bap__broadcast__source.md#gabecaa9db7be5cb03ed997ba478878d40)

int bt\_bap\_broadcast\_source\_reconfig(struct bt\_bap\_broadcast\_source \*source, struct bt\_bap\_broadcast\_source\_param \*param)

Reconfigure audio broadcast source.

[bt\_bap\_broadcast\_source\_start](group__bt__bap__broadcast__source.md#gac4640f5207599d51c1a63ff47f3c1d5a)

int bt\_bap\_broadcast\_source\_start(struct bt\_bap\_broadcast\_source \*source, struct bt\_le\_ext\_adv \*adv)

Start audio broadcast source.

[bt\_bap\_broadcast\_source\_create](group__bt__bap__broadcast__source.md#gacdebfc435eebd47cf9cd05099a5f78e0)

int bt\_bap\_broadcast\_source\_create(struct bt\_bap\_broadcast\_source\_param \*param, struct bt\_bap\_broadcast\_source \*\*source)

Create audio broadcast source.

[bt\_bap\_broadcast\_source\_get\_base](group__bt__bap__broadcast__source.md#gafe07e4c6962858500fcf66415a173be8)

int bt\_bap\_broadcast\_source\_get\_base(struct bt\_bap\_broadcast\_source \*source, struct net\_buf\_simple \*base\_buf)

Get the Broadcast Audio Stream Endpoint of a broadcast source.

[bt\_bap\_broadcast\_source\_update\_metadata](group__bt__bap__broadcast__source.md#gaff2cfdadbff3ebe1e2efb660dee56f02)

int bt\_bap\_broadcast\_source\_update\_metadata(struct bt\_bap\_broadcast\_source \*source, const uint8\_t meta[], size\_t meta\_len)

Modify the metadata of an audio broadcast source.

[bt\_bap\_base\_get\_subgroup\_bis\_count](group__bt__bap__broadcast.md#ga051e1f8aa2faf3ba7a973356138fd2d3)

int bt\_bap\_base\_get\_subgroup\_bis\_count(const struct bt\_bap\_base\_subgroup \*subgroup)

Get the BIS count of a subgroup.

[bt\_bap\_base\_get\_subgroup\_codec\_data](group__bt__bap__broadcast.md#ga10e2e32dc2802ba55d55c77148331f6a)

int bt\_bap\_base\_get\_subgroup\_codec\_data(const struct bt\_bap\_base\_subgroup \*subgroup, uint8\_t \*\*data)

Get the codec configuration data of a subgroup.

[bt\_bap\_base\_get\_base\_from\_ad](group__bt__bap__broadcast.md#ga29423a39d76ad16f0586d82a23c07ba7)

const struct bt\_bap\_base \* bt\_bap\_base\_get\_base\_from\_ad(const struct bt\_data \*ad)

Generate a pointer to a BASE from periodic advertising data.

[bt\_bap\_base\_subgroup\_foreach\_bis](group__bt__bap__broadcast.md#ga4f85ee43984cb2f3139b41da7b9b1aee)

int bt\_bap\_base\_subgroup\_foreach\_bis(const struct bt\_bap\_base\_subgroup \*subgroup, bool(\*func)(const struct bt\_bap\_base\_subgroup\_bis \*bis, void \*user\_data), void \*user\_data)

Iterate on all BIS in the subgroup.

[bt\_bap\_base\_foreach\_subgroup](group__bt__bap__broadcast.md#ga5e6e0b758409cbdde93c0f648ef5e5e8)

int bt\_bap\_base\_foreach\_subgroup(const struct bt\_bap\_base \*base, bool(\*func)(const struct bt\_bap\_base\_subgroup \*subgroup, void \*user\_data), void \*user\_data)

Iterate on all subgroups in the BASE.

[bt\_bap\_base\_get\_bis\_indexes](group__bt__bap__broadcast.md#ga6deab5a8b7a16ddf0c3685d4003694e1)

int bt\_bap\_base\_get\_bis\_indexes(const struct bt\_bap\_base \*base, uint32\_t \*bis\_indexes)

Get all BIS indexes of a BASE.

[bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg](group__bt__bap__broadcast.md#ga920e3409f1978b803bcf6bc8d05ac8f6)

int bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg(const struct bt\_bap\_base\_subgroup \*subgroup, struct bt\_audio\_codec\_cfg \*codec\_cfg)

Store subgroup codec data in a Codec config parsing APIs.

[bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg](group__bt__bap__broadcast.md#gaa5cb191df7807ea87f1fba1871ca8ebe)

int bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg(const struct bt\_bap\_base\_subgroup\_bis \*bis, struct bt\_audio\_codec\_cfg \*codec\_cfg)

Store BIS codec configuration data in a Codec config parsing APIs.

[bt\_bap\_base\_get\_subgroup\_count](group__bt__bap__broadcast.md#gadcae0230168564da1ee8b3c577ce27d7)

int bt\_bap\_base\_get\_subgroup\_count(const struct bt\_bap\_base \*base)

Get the subgroup count of a BASE.

[bt\_bap\_base\_get\_subgroup\_codec\_id](group__bt__bap__broadcast.md#gae75e05a002dee8336eb066ae8231ea0c)

int bt\_bap\_base\_get\_subgroup\_codec\_id(const struct bt\_bap\_base\_subgroup \*subgroup, struct bt\_bap\_base\_codec\_id \*codec\_id)

Get the codec ID of a subgroup.

[bt\_bap\_base\_get\_pres\_delay](group__bt__bap__broadcast.md#gaf91f45bcf7df2f368c5abeb116b65dd0)

int bt\_bap\_base\_get\_pres\_delay(const struct bt\_bap\_base \*base)

Get the presentation delay value of a BASE.

[bt\_bap\_base\_get\_subgroup\_codec\_meta](group__bt__bap__broadcast.md#gafb9d9544f38c7ad2613fff1679eb1f0c)

int bt\_bap\_base\_get\_subgroup\_codec\_meta(const struct bt\_bap\_base\_subgroup \*subgroup, uint8\_t \*\*meta)

Get the codec metadata of a subgroup.

[bt\_bap\_unicast\_group\_delete](group__bt__bap__unicast__client.md#ga34dbdce6133f8366df453ec937fb47d2)

int bt\_bap\_unicast\_group\_delete(struct bt\_bap\_unicast\_group \*unicast\_group)

Delete audio unicast group.

[bt\_bap\_unicast\_group\_add\_streams](group__bt__bap__unicast__client.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6)

int bt\_bap\_unicast\_group\_add\_streams(struct bt\_bap\_unicast\_group \*unicast\_group, struct bt\_bap\_unicast\_group\_stream\_pair\_param params[], size\_t num\_param)

Add streams to a unicast group as a unicast client.

[bt\_bap\_unicast\_group\_create](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21)

int bt\_bap\_unicast\_group\_create(struct bt\_bap\_unicast\_group\_param \*param, struct bt\_bap\_unicast\_group \*\*unicast\_group)

Create audio unicast group.

[bt\_bap\_unicast\_client\_discover](group__bt__bap__unicast__client.md#gacef9c88f66762e8de19303d20dafa0bb)

int bt\_bap\_unicast\_client\_discover(struct bt\_conn \*conn, enum bt\_audio\_dir dir)

Discover remote capabilities and endpoints.

[bt\_bap\_unicast\_client\_register\_cb](group__bt__bap__unicast__client.md#gae598c65d7c5d419ee941d7cf33601a64)

int bt\_bap\_unicast\_client\_register\_cb(const struct bt\_bap\_unicast\_client\_cb \*cb)

Register unicast client callbacks.

[bt\_bap\_unicast\_server\_foreach\_ep](group__bt__bap__unicast__server.md#ga4614a504d47cf732b09d4f22302d3239)

void bt\_bap\_unicast\_server\_foreach\_ep(struct bt\_conn \*conn, bt\_bap\_ep\_func\_t func, void \*user\_data)

Iterate through all endpoints of the given connection.

[bt\_bap\_unicast\_server\_register\_cb](group__bt__bap__unicast__server.md#ga7669133936bc13f7ab38817db9ce69c0)

int bt\_bap\_unicast\_server\_register\_cb(const struct bt\_bap\_unicast\_server\_cb \*cb)

Register unicast server callbacks.

[bt\_bap\_ep\_func\_t](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1)

void(\* bt\_bap\_ep\_func\_t)(struct bt\_bap\_ep \*ep, void \*user\_data)

The callback function called for each endpoint.

**Definition** bap.h:1002

[bt\_bap\_unicast\_server\_unregister\_cb](group__bt__bap__unicast__server.md#gadf984f12bdeadcfc814dc2fc770cb7bf)

int bt\_bap\_unicast\_server\_unregister\_cb(const struct bt\_bap\_unicast\_server\_cb \*cb)

Unregister unicast server callbacks.

[bt\_bap\_unicast\_server\_config\_ase](group__bt__bap__unicast__server.md#gaf0f06f2536d1e108691fba87b234a7f4)

int bt\_bap\_unicast\_server\_config\_ase(struct bt\_conn \*conn, struct bt\_bap\_stream \*stream, struct bt\_audio\_codec\_cfg \*codec\_cfg, const struct bt\_audio\_codec\_qos\_pref \*qos\_pref)

Initialize and configure a new ASE.

[bt\_bap\_broadcast\_assistant\_set\_broadcast\_code](group__bt__bap.md#ga0105535992cf66e55ab2587648fb571f)

int bt\_bap\_broadcast\_assistant\_set\_broadcast\_code(struct bt\_conn \*conn, uint8\_t src\_id, const uint8\_t broadcast\_code[16])

Set a broadcast code to the specified receive state.

[bt\_bap\_broadcast\_assistant\_rem\_src](group__bt__bap.md#ga09785690db551677a043fcaa2fdb7f29)

int bt\_bap\_broadcast\_assistant\_rem\_src(struct bt\_conn \*conn, uint8\_t src\_id)

Remove a source from the server.

[bt\_bap\_stream\_metadata](group__bt__bap.md#ga0afe6c927729697e2f984cefcbc7c0f1)

int bt\_bap\_stream\_metadata(struct bt\_bap\_stream \*stream, const uint8\_t meta[], size\_t meta\_len)

Change Audio Stream Metadata.

[bt\_bap\_stream\_disable](group__bt__bap.md#ga0fd2bb35909fc19e3e9cff068ba9e9aa)

int bt\_bap\_stream\_disable(struct bt\_bap\_stream \*stream)

Disable Audio Stream.

[bt\_bap\_stream\_enable](group__bt__bap.md#ga13a859b31b0310ec22339ec7ed0754f8)

int bt\_bap\_stream\_enable(struct bt\_bap\_stream \*stream, const uint8\_t meta[], size\_t meta\_len)

Enable Audio Stream.

[bt\_bap\_bass\_att\_err](group__bt__bap.md#ga13e9b6d571a613d689b8ba58bae64ae3)

bt\_bap\_bass\_att\_err

Broadcast Audio Scan Service (BASS) specific ATT error codes.

**Definition** bap.h:62

[bt\_bap\_stream\_config](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402)

int bt\_bap\_stream\_config(struct bt\_conn \*conn, struct bt\_bap\_stream \*stream, struct bt\_bap\_ep \*ep, struct bt\_audio\_codec\_cfg \*codec\_cfg)

Configure Audio Stream.

[bt\_bap\_scan\_delegator\_set\_pa\_state](group__bt__bap.md#ga381c1f3b386ecbdfd570eb125882161e)

int bt\_bap\_scan\_delegator\_set\_pa\_state(uint8\_t src\_id, enum bt\_bap\_pa\_state pa\_state)

Set the periodic advertising sync state to syncing.

[bt\_bap\_stream\_get\_tx\_sync](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928)

int bt\_bap\_stream\_get\_tx\_sync(struct bt\_bap\_stream \*stream, struct bt\_iso\_tx\_info \*info)

Get ISO transmission timing info for a Basic Audio Profile stream.

[bt\_bap\_broadcast\_assistant\_write\_cb](group__bt__bap.md#ga496c8a2f599d997a7e6e033bda5f0c36)

void(\* bt\_bap\_broadcast\_assistant\_write\_cb)(struct bt\_conn \*conn, int err)

Callback function for writes.

**Definition** bap.h:2041

[bt\_bap\_scan\_delegator\_register\_cb](group__bt__bap.md#ga5841f00a46c8b32bc8253d70dc05f104)

void bt\_bap\_scan\_delegator\_register\_cb(struct bt\_bap\_scan\_delegator\_cb \*cb)

Register the callbacks for the Basic Audio Profile Scan Delegator.

[bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22)

bt\_bap\_big\_enc\_state

Broadcast Isochronous Group encryption state reported by the Scan Delegator.

**Definition** bap.h:47

[bt\_bap\_stream\_send](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e)

int bt\_bap\_stream\_send(struct bt\_bap\_stream \*stream, struct net\_buf \*buf, uint16\_t seq\_num)

Send data to Audio stream without timestamp.

[bt\_bap\_scan\_delegator\_rem\_src](group__bt__bap.md#ga6c240f1cdb33945197700e4fe106ef2c)

int bt\_bap\_scan\_delegator\_rem\_src(uint8\_t src\_id)

Remove a receive state source.

[bt\_bap\_scan\_delegator\_add\_src](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0)

int bt\_bap\_scan\_delegator\_add\_src(const struct bt\_bap\_scan\_delegator\_add\_src\_param \*param)

Add a receive state source locally.

[bt\_bap\_broadcast\_assistant\_scan\_stop](group__bt__bap.md#ga76cae35df980b78a10551811050b2760)

int bt\_bap\_broadcast\_assistant\_scan\_stop(struct bt\_conn \*conn)

Stop remote scanning for BISes for a server.

[bt\_bap\_scan\_delegator\_set\_bis\_sync\_state](group__bt__bap.md#ga7cce7e53264294abec4421364afffdbe)

int bt\_bap\_scan\_delegator\_set\_bis\_sync\_state(uint8\_t src\_id, uint32\_t bis\_synced[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS])

Set the sync state of a receive state in the server.

[bt\_bap\_stream\_start](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae)

int bt\_bap\_stream\_start(struct bt\_bap\_stream \*stream)

Start Audio Stream.

[bt\_bap\_broadcast\_assistant\_read\_recv\_state](group__bt__bap.md#ga94fce2b4346b1026d53e0b860ca7fbf2)

int bt\_bap\_broadcast\_assistant\_read\_recv\_state(struct bt\_conn \*conn, uint8\_t idx)

Read the specified receive state from the server.

[bt\_bap\_broadcast\_assistant\_scan\_start](group__bt__bap.md#ga98ac067e66d263aa41fc6f8df6bb9126)

int bt\_bap\_broadcast\_assistant\_scan\_start(struct bt\_conn \*conn, bool start\_scan)

Scan start for BISes for a remote server.

[bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45)

bt\_bap\_ascs\_reason

Response Reasons.

**Definition** bap.h:150

[bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1)

bt\_bap\_ascs\_rsp\_code

Response Status Code.

**Definition** bap.h:110

[bt\_bap\_stream\_send\_ts](group__bt__bap.md#gaa0e012446238c916abc84d6c0de89bf3)

int bt\_bap\_stream\_send\_ts(struct bt\_bap\_stream \*stream, struct net\_buf \*buf, uint16\_t seq\_num, uint32\_t ts)

Send data to Audio stream with timestamp.

[bt\_bap\_broadcast\_assistant\_mod\_src](group__bt__bap.md#gaa9c292a7dcb470926d8d7d4be699a0c7)

int bt\_bap\_broadcast\_assistant\_mod\_src(struct bt\_conn \*conn, const struct bt\_bap\_broadcast\_assistant\_mod\_src\_param \*param)

Modify a source on the server.

[bt\_bap\_stream\_reconfig](group__bt__bap.md#gaac84ee7b3ab5578d258848754f752546)

int bt\_bap\_stream\_reconfig(struct bt\_bap\_stream \*stream, struct bt\_audio\_codec\_cfg \*codec\_cfg)

Reconfigure Audio Stream.

[bt\_bap\_stream\_release](group__bt__bap.md#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)

int bt\_bap\_stream\_release(struct bt\_bap\_stream \*stream)

Release Audio Stream.

[bt\_bap\_stream\_cb\_register](group__bt__bap.md#gab29c1e134156dceaa6c67abae9239378)

void bt\_bap\_stream\_cb\_register(struct bt\_bap\_stream \*stream, struct bt\_bap\_stream\_ops \*ops)

Register Audio callbacks for a stream.

[bt\_bap\_broadcast\_assistant\_discover](group__bt__bap.md#gab59c5ebc4fef28da34d8a54b1244c33b)

int bt\_bap\_broadcast\_assistant\_discover(struct bt\_conn \*conn)

Discover Broadcast Audio Scan Service on the server.

[bt\_bap\_scan\_delegator\_foreach\_state](group__bt__bap.md#gab6f1a12699a9437c6575c70df33d5be0)

void bt\_bap\_scan\_delegator\_foreach\_state(bt\_bap\_scan\_delegator\_state\_func\_t func, void \*user\_data)

Iterate through all existing receive states.

[bt\_bap\_scan\_delegator\_find\_state](group__bt__bap.md#gabec9fd0a2966e1811fd4770855050510)

const struct bt\_bap\_scan\_delegator\_recv\_state \* bt\_bap\_scan\_delegator\_find\_state(bt\_bap\_scan\_delegator\_state\_func\_t func, void \*user\_data)

Find and return a receive state based on a compare function.

[bt\_bap\_scan\_delegator\_mod\_src](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a)

int bt\_bap\_scan\_delegator\_mod\_src(const struct bt\_bap\_scan\_delegator\_mod\_src\_param \*param)

Add a receive state source locally.

[bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296)

bt\_bap\_pa\_state

Periodic advertising state reported by the Scan Delegator.

**Definition** bap.h:29

[bt\_bap\_stream\_qos](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d)

int bt\_bap\_stream\_qos(struct bt\_conn \*conn, struct bt\_bap\_unicast\_group \*group)

Configure Audio Stream QoS.

[bt\_bap\_broadcast\_assistant\_add\_src](group__bt__bap.md#gac93cb4cab33d0b937e752bc0b71cad9e)

int bt\_bap\_broadcast\_assistant\_add\_src(struct bt\_conn \*conn, const struct bt\_bap\_broadcast\_assistant\_add\_src\_param \*param)

Add a source on the server.

[bt\_bap\_stream\_stop](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b)

int bt\_bap\_stream\_stop(struct bt\_bap\_stream \*stream)

Stop Audio Stream.

[bt\_bap\_ep\_get\_info](group__bt__bap.md#gaf15e5ec5bca364f6a3e7a43b1f27da68)

int bt\_bap\_ep\_get\_info(const struct bt\_bap\_ep \*ep, struct bt\_bap\_ep\_info \*info)

Return structure holding information of audio stream endpoint.

[bt\_bap\_ep\_state](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a)

bt\_bap\_ep\_state

Endpoint states.

**Definition** bap.h:81

[bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824)

bool(\* bt\_bap\_scan\_delegator\_state\_func\_t)(const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state, void \*user\_data)

Callback function for Scan Delegator receive state search functions.

**Definition** bap.h:2012

[bt\_bap\_broadcast\_assistant\_register\_cb](group__bt__bap.md#gafe741eb3ba1054ed81de71aafd5c03d8)

void bt\_bap\_broadcast\_assistant\_register\_cb(struct bt\_bap\_broadcast\_assistant\_cb \*cb)

Registers the callbacks used by Broadcast Audio Scan Service client.

[BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c)

@ BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED

Opcode not supported.

**Definition** bap.h:64

[BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202)

@ BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID

Invalid source ID supplied.

**Definition** bap.h:67

[BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2)

@ BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ

The Broadcast Isochronous Group broadcast code requested.

**Definition** bap.h:52

[BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4)

@ BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC

The Broadcast Isochronous Group not encrypted.

**Definition** bap.h:49

[BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b)

@ BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE

The Broadcast Isochronous Group bad broadcast code.

**Definition** bap.h:58

[BT\_BAP\_BIG\_ENC\_STATE\_DEC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10)

@ BT\_BAP\_BIG\_ENC\_STATE\_DEC

The Broadcast Isochronous Group decrypted.

**Definition** bap.h:55

[BT\_BAP\_ASCS\_REASON\_NONE](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd)

@ BT\_BAP\_ASCS\_REASON\_NONE

No reason.

**Definition** bap.h:152

[BT\_BAP\_ASCS\_REASON\_PD](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557)

@ BT\_BAP\_ASCS\_REASON\_PD

Presendation delay.

**Definition** bap.h:170

[BT\_BAP\_ASCS\_REASON\_FRAMING](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539)

@ BT\_BAP\_ASCS\_REASON\_FRAMING

Framing.

**Definition** bap.h:160

[BT\_BAP\_ASCS\_REASON\_CODEC\_DATA](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0)

@ BT\_BAP\_ASCS\_REASON\_CODEC\_DATA

Codec configuration.

**Definition** bap.h:156

[BT\_BAP\_ASCS\_REASON\_SDU](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b)

@ BT\_BAP\_ASCS\_REASON\_SDU

Maximum SDU size.

**Definition** bap.h:164

[BT\_BAP\_ASCS\_REASON\_CODEC](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea)

@ BT\_BAP\_ASCS\_REASON\_CODEC

Codec ID.

**Definition** bap.h:154

[BT\_BAP\_ASCS\_REASON\_PHY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8)

@ BT\_BAP\_ASCS\_REASON\_PHY

PHY.

**Definition** bap.h:162

[BT\_BAP\_ASCS\_REASON\_LATENCY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942)

@ BT\_BAP\_ASCS\_REASON\_LATENCY

Max transport latency.

**Definition** bap.h:168

[BT\_BAP\_ASCS\_REASON\_CIS](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c)

@ BT\_BAP\_ASCS\_REASON\_CIS

Invalid CIS mapping.

**Definition** bap.h:172

[BT\_BAP\_ASCS\_REASON\_RTN](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf)

@ BT\_BAP\_ASCS\_REASON\_RTN

RTN.

**Definition** bap.h:166

[BT\_BAP\_ASCS\_REASON\_INTERVAL](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c)

@ BT\_BAP\_ASCS\_REASON\_INTERVAL

SDU interval.

**Definition** bap.h:158

[BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5)

@ BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE

Invalid ASE state.

**Definition** bap.h:120

[BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06)

@ BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID

Invalid metadata.

**Definition** bap.h:136

[BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d)

@ BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED

Server did not support operation by client.

**Definition** bap.h:114

[BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)

@ BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED

Configuration parameters not supported by server.

**Definition** bap.h:126

[BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa)

@ BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE

Invalid ASE ID.

**Definition** bap.h:118

[BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146)

@ BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR

Invalid operation for direction.

**Definition** bap.h:122

[BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219)

@ BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID

Invalid Configuration parameters.

**Definition** bap.h:130

[BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)

@ BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED

Capabilities not supported by server.

**Definition** bap.h:124

[BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)

@ BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM

Server has insufficient resources.

**Definition** bap.h:138

[BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06)

@ BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED

Metadata rejected by server.

**Definition** bap.h:134

[BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a)

@ BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED

Unspecified error.

**Definition** bap.h:140

[BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9)

@ BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH

Server rejected due to invalid operation length.

**Definition** bap.h:116

[BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)

@ BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED

Unsupported metadata.

**Definition** bap.h:132

[BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)

@ BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS

Server completed operation successfully.

**Definition** bap.h:112

[BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21)

@ BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED

Configuration parameters rejected by server.

**Definition** bap.h:128

[BT\_BAP\_PA\_STATE\_NOT\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf)

@ BT\_BAP\_PA\_STATE\_NOT\_SYNCED

The periodic advertising has not been synchronized.

**Definition** bap.h:31

[BT\_BAP\_PA\_STATE\_FAILED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647)

@ BT\_BAP\_PA\_STATE\_FAILED

Failed to synchronized to periodic advertising.

**Definition** bap.h:40

[BT\_BAP\_PA\_STATE\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc)

@ BT\_BAP\_PA\_STATE\_SYNCED

Synchronized to periodic advertising.

**Definition** bap.h:37

[BT\_BAP\_PA\_STATE\_INFO\_REQ](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb)

@ BT\_BAP\_PA\_STATE\_INFO\_REQ

Waiting for SyncInfo from Broadcast Assistant.

**Definition** bap.h:34

[BT\_BAP\_PA\_STATE\_NO\_PAST](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d)

@ BT\_BAP\_PA\_STATE\_NO\_PAST

No periodic advertising sync transfer receiver from Broadcast Assistant.

**Definition** bap.h:43

[BT\_BAP\_EP\_STATE\_ENABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332)

@ BT\_BAP\_EP\_STATE\_ENABLING

Audio Stream Endpoint Enabling state.

**Definition** bap.h:92

[BT\_BAP\_EP\_STATE\_IDLE](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961)

@ BT\_BAP\_EP\_STATE\_IDLE

Audio Stream Endpoint Idle state.

**Definition** bap.h:83

[BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688)

@ BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED

Audio Stream Endpoint Codec Configured state.

**Definition** bap.h:86

[BT\_BAP\_EP\_STATE\_RELEASING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c)

@ BT\_BAP\_EP\_STATE\_RELEASING

Audio Stream Endpoint Streaming state.

**Definition** bap.h:101

[BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523)

@ BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED

Audio Stream Endpoint QoS Configured state.

**Definition** bap.h:89

[BT\_BAP\_EP\_STATE\_DISABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8)

@ BT\_BAP\_EP\_STATE\_DISABLING

Audio Stream Endpoint Disabling state.

**Definition** bap.h:98

[BT\_BAP\_EP\_STATE\_STREAMING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710)

@ BT\_BAP\_EP\_STATE\_STREAMING

Audio Stream Endpoint Streaming state.

**Definition** bap.h:95

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_audio\_codec\_cap](structbt__audio__codec__cap.md)

Codec capability structure.

**Definition** audio.h:550

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:584

[bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md)

Audio Stream Quality of Service Preference structure.

**Definition** audio.h:785

[bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)

Codec QoS structure.

**Definition** audio.h:702

[bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md)

Structure storing values of fields of ASE Control Point notification.

**Definition** bap.h:176

[bt\_bap\_ascs\_rsp::reason](structbt__bap__ascs__rsp.md#a138532bc40f60547c56d8b108ad44d1e)

enum bt\_bap\_ascs\_reason reason

Response reason.

**Definition** bap.h:213

[bt\_bap\_ascs\_rsp::metadata\_type](structbt__bap__ascs__rsp.md#a736f44864015244a8b48a859eff6b902)

enum bt\_audio\_metadata\_type metadata\_type

Response metadata type.

**Definition** bap.h:223

[bt\_bap\_ascs\_rsp::code](structbt__bap__ascs__rsp.md#a8ea364298f7e3e784b7878215db63d91)

enum bt\_bap\_ascs\_rsp\_code code

Value of the Response Code field.

**Definition** bap.h:190

[bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md)

Codec ID structure for a Broadcast Audio Source Endpoint (BASE).

**Definition** bap.h:1373

[bt\_bap\_base\_codec\_id::cid](structbt__bap__base__codec__id.md#a0aadd7e53f72efd8c0e33dd9a8eca177)

uint16\_t cid

Codec Company ID.

**Definition** bap.h:1377

[bt\_bap\_base\_codec\_id::vid](structbt__bap__base__codec__id.md#a49802819cc3129a993320b95472f2262)

uint16\_t vid

Codec Company Vendor ID.

**Definition** bap.h:1379

[bt\_bap\_base\_codec\_id::id](structbt__bap__base__codec__id.md#a9031aaf6a3f6e0acf68f1bfaed39b819)

uint8\_t id

Codec ID.

**Definition** bap.h:1375

[bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md)

BIS structure for each BIS in a Broadcast Audio Source Endpoint (BASE) subgroup.

**Definition** bap.h:1383

[bt\_bap\_base\_subgroup\_bis::data](structbt__bap__base__subgroup__bis.md#aa53f22b29e447822e8bb36d9245bfc77)

uint8\_t \* data

Codec Specific Data.

**Definition** bap.h:1389

[bt\_bap\_base\_subgroup\_bis::data\_len](structbt__bap__base__subgroup__bis.md#ac4132c798c04c0f93c944dc91891221e)

uint8\_t data\_len

Codec Specific Data length.

**Definition** bap.h:1387

[bt\_bap\_base\_subgroup\_bis::index](structbt__bap__base__subgroup__bis.md#ad0f5dff3150c36b1625f1f6f206d41d2)

uint8\_t index

**Definition** bap.h:1385

[bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md)

Struct to hold subgroup specific information for the receive state.

**Definition** bap.h:249

[bt\_bap\_bass\_subgroup::bis\_sync](structbt__bap__bass__subgroup.md#ac8061995eb73ba30e335e37714396ff5)

uint32\_t bis\_sync

BIS synced bitfield.

**Definition** bap.h:251

[bt\_bap\_bass\_subgroup::metadata\_len](structbt__bap__bass__subgroup.md#ace1c1ff5d2f5cc79838653d468166664)

uint8\_t metadata\_len

Length of the metadata.

**Definition** bap.h:254

[bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md)

Parameters for adding a source to a Broadcast Audio Scan Service server.

**Definition** bap.h:2185

[bt\_bap\_broadcast\_assistant\_add\_src\_param::num\_subgroups](structbt__bap__broadcast__assistant__add__src__param.md#a17b67d65b6840c3d4480027b7deb31a5)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:2206

[bt\_bap\_broadcast\_assistant\_add\_src\_param::addr](structbt__bap__broadcast__assistant__add__src__param.md#a2b04d75ca9a740a7d819eae1bcc5cba7)

bt\_addr\_le\_t addr

Address of the advertiser.

**Definition** bap.h:2187

[bt\_bap\_broadcast\_assistant\_add\_src\_param::adv\_sid](structbt__bap__broadcast__assistant__add__src__param.md#a390cd8d887cd256ee74b39b9b516cac4)

uint8\_t adv\_sid

SID of the advertising set.

**Definition** bap.h:2190

[bt\_bap\_broadcast\_assistant\_add\_src\_param::subgroups](structbt__bap__broadcast__assistant__add__src__param.md#ab8423e5cce4a6c9ac142221d2e816763)

struct bt\_bap\_bass\_subgroup \* subgroups

Pointer to array of subgroups.

**Definition** bap.h:2209

[bt\_bap\_broadcast\_assistant\_add\_src\_param::pa\_interval](structbt__bap__broadcast__assistant__add__src__param.md#acaecbbf7b3c96fe5ca53f90e92fa1e5e)

uint16\_t pa\_interval

Periodic advertising interval in milliseconds.

**Definition** bap.h:2203

[bt\_bap\_broadcast\_assistant\_add\_src\_param::pa\_sync](structbt__bap__broadcast__assistant__add__src__param.md#ad9af814e8a232230d4ee97c459f47747)

bool pa\_sync

Whether to sync to periodic advertisements.

**Definition** bap.h:2193

[bt\_bap\_broadcast\_assistant\_add\_src\_param::broadcast\_id](structbt__bap__broadcast__assistant__add__src__param.md#ae50b6b5a3f2c92f01e7070c605b37dde)

uint32\_t broadcast\_id

24-bit broadcast ID

**Definition** bap.h:2196

[bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md)

**Definition** bap.h:2044

[bt\_bap\_broadcast\_assistant\_cb::discover](structbt__bap__broadcast__assistant__cb.md#a01ad0a89db9041670f6a68d6f1680988)

void(\* discover)(struct bt\_conn \*conn, int err, uint8\_t recv\_state\_count)

Callback function for bt\_bap\_broadcast\_assistant\_discover.

**Definition** bap.h:2054

[bt\_bap\_broadcast\_assistant\_cb::broadcast\_code](structbt__bap__broadcast__assistant__cb.md#a09de9cb86dad76b485ff52257a0c68dc)

void(\* broadcast\_code)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_broadcast\_code().

**Definition** bap.h:2129

[bt\_bap\_broadcast\_assistant\_cb::recv\_state](structbt__bap__broadcast__assistant__cb.md#a629ff4299b8ae5bcbddf28338caddfd0)

void(\* recv\_state)(struct bt\_conn \*conn, int err, const struct bt\_bap\_scan\_delegator\_recv\_state \*state)

Callback function for when a receive state is read or updated.

**Definition** bap.h:2078

[bt\_bap\_broadcast\_assistant\_cb::scan\_stop](structbt__bap__broadcast__assistant__cb.md#a80296a38e664aabff7ec27e007c59e95)

void(\* scan\_stop)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_scan\_stop().

**Definition** bap.h:2105

[bt\_bap\_broadcast\_assistant\_cb::recv\_state\_removed](structbt__bap__broadcast__assistant__cb.md#ab0f09236e236d8456fcdee36b5871bfc)

void(\* recv\_state\_removed)(struct bt\_conn \*conn, int err, uint8\_t src\_id)

Callback function for when a receive state is removed.

**Definition** bap.h:2088

[bt\_bap\_broadcast\_assistant\_cb::mod\_src](structbt__bap__broadcast__assistant__cb.md#ab24e3ecb9764ca833524b787126b8c2c)

void(\* mod\_src)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_mod\_src().

**Definition** bap.h:2121

[bt\_bap\_broadcast\_assistant\_cb::scan](structbt__bap__broadcast__assistant__cb.md#ab88d98b1e742ccd36aac69069ebf3f61)

void(\* scan)(const struct bt\_le\_scan\_recv\_info \*info, uint32\_t broadcast\_id)

Callback function for Broadcast Audio Scan Service client scan results.

**Definition** bap.h:2066

[bt\_bap\_broadcast\_assistant\_cb::scan\_start](structbt__bap__broadcast__assistant__cb.md#ad2bdfcc0147a751910d82232a77e34f8)

void(\* scan\_start)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_scan\_start().

**Definition** bap.h:2097

[bt\_bap\_broadcast\_assistant\_cb::add\_src](structbt__bap__broadcast__assistant__cb.md#ad909b9e6e3c35be10a29ee5a4b7213fb)

void(\* add\_src)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_add\_src().

**Definition** bap.h:2113

[bt\_bap\_broadcast\_assistant\_cb::rem\_src](structbt__bap__broadcast__assistant__cb.md#af0cf259088cd793152390b21813a9481)

void(\* rem\_src)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_rem\_src().

**Definition** bap.h:2137

[bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md)

Parameters for modifying a source.

**Definition** bap.h:2224

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::subgroups](structbt__bap__broadcast__assistant__mod__src__param.md#a2383ec98b14054e0bc66bb4a0ae7b8b6)

struct bt\_bap\_bass\_subgroup \* subgroups

Pointer to array of subgroups.

**Definition** bap.h:2242

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::num\_subgroups](structbt__bap__broadcast__assistant__mod__src__param.md#a42b12c6d9f5c622433c9c1f0c72726c1)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:2239

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::src\_id](structbt__bap__broadcast__assistant__mod__src__param.md#a5bc7c0a491872d655296bbb979402a62)

uint8\_t src\_id

Source ID of the receive state.

**Definition** bap.h:2226

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::pa\_sync](structbt__bap__broadcast__assistant__mod__src__param.md#a794bb68c8a73edfe3d44dbe9a0bf2830)

bool pa\_sync

Whether to sync to periodic advertisements.

**Definition** bap.h:2229

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::pa\_interval](structbt__bap__broadcast__assistant__mod__src__param.md#aebaa104384dcbec7bb952a27f3acc24d)

uint16\_t pa\_interval

Periodic advertising interval.

**Definition** bap.h:2236

[bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md)

Broadcast Audio Sink callback structure.

**Definition** bap.h:1780

[bt\_bap\_broadcast\_sink\_cb::base\_recv](structbt__bap__broadcast__sink__cb.md#a1adf2124ec9a16c3c68774194febd0fc)

void(\* base\_recv)(struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_bap\_base \*base, size\_t base\_size)

Broadcast Audio Source Endpoint (BASE) received.

**Definition** bap.h:1790

[bt\_bap\_broadcast\_sink\_cb::syncable](structbt__bap__broadcast__sink__cb.md#ac2c8389a8e68e5b4afe735f623dc36ec)

void(\* syncable)(struct bt\_bap\_broadcast\_sink \*sink, bool encrypted)

Broadcast sink is syncable.

**Definition** bap.h:1804

[bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md)

Broadcast Source create parameters.

**Definition** bap.h:1580

[bt\_bap\_broadcast\_source\_param::packing](structbt__bap__broadcast__source__param.md#a493fa57a80e21a288854b2e3e1df775a)

uint8\_t packing

Broadcast Source packing mode.

**Definition** bap.h:1597

[bt\_bap\_broadcast\_source\_param::params\_count](structbt__bap__broadcast__source__param.md#a5e155c3b92b4f9de3c9e6efa377097e3)

size\_t params\_count

The number of parameters in subgroup\_params.

**Definition** bap.h:1582

[bt\_bap\_broadcast\_source\_param::params](structbt__bap__broadcast__source__param.md#a6291842b49a55f6b2767dc95c9e874f3)

struct bt\_bap\_broadcast\_source\_subgroup\_param \* params

Array of stream parameters.

**Definition** bap.h:1585

[bt\_bap\_broadcast\_source\_param::encryption](structbt__bap__broadcast__source__param.md#a7552bf9a4ff5441b13669effe23abb8c)

bool encryption

Whether or not to encrypt the streams.

**Definition** bap.h:1600

[bt\_bap\_broadcast\_source\_param::broadcast\_code](structbt__bap__broadcast__source__param.md#acc096d55aaeb419a356ab5c023928df6)

uint8\_t broadcast\_code[16]

Broadcast code.

**Definition** bap.h:1612

[bt\_bap\_broadcast\_source\_param::qos](structbt__bap__broadcast__source__param.md#af969b5aacd4743bae608a7f54c0556e9)

struct bt\_audio\_codec\_qos \* qos

Quality of Service configuration.

**Definition** bap.h:1588

[bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md)

Broadcast Source stream parameters.

**Definition** bap.h:1550

[bt\_bap\_broadcast\_source\_stream\_param::stream](structbt__bap__broadcast__source__stream__param.md#a9c92fb50b62d963e01b1506b790fb5e1)

struct bt\_bap\_stream \* stream

Audio stream.

**Definition** bap.h:1552

[bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md)

Broadcast Source subgroup parameters.

**Definition** bap.h:1568

[bt\_bap\_broadcast\_source\_subgroup\_param::codec\_cfg](structbt__bap__broadcast__source__subgroup__param.md#a1986239ea2ed5204d8f46a6500d5900d)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Subgroup Codec configuration.

**Definition** bap.h:1576

[bt\_bap\_broadcast\_source\_subgroup\_param::params\_count](structbt__bap__broadcast__source__subgroup__param.md#a701d9480ffae2351149de6b962095d32)

size\_t params\_count

The number of parameters in stream\_params.

**Definition** bap.h:1570

[bt\_bap\_broadcast\_source\_subgroup\_param::params](structbt__bap__broadcast__source__subgroup__param.md#a9719e89d8979f9502023e0032814c477)

struct bt\_bap\_broadcast\_source\_stream\_param \* params

Array of stream parameters.

**Definition** bap.h:1573

[bt\_bap\_ep\_info](structbt__bap__ep__info.md)

Structure holding information of audio stream endpoint.

**Definition** bap.h:390

[bt\_bap\_ep\_info::id](structbt__bap__ep__info.md#a07e8878e7e6a8ee059639330ffa78c1c)

uint8\_t id

The ID of the endpoint.

**Definition** bap.h:392

[bt\_bap\_ep\_info::state](structbt__bap__ep__info.md#a650727747d0a093528544c3e16255feb)

enum bt\_bap\_ep\_state state

The state of the endpoint.

**Definition** bap.h:395

[bt\_bap\_ep\_info::paired\_ep](structbt__bap__ep__info.md#a819ac77dcf7cb6985e97f290a666ed09)

struct bt\_bap\_ep \* paired\_ep

Pointer to paired endpoint if the endpoint is part of a bidirectional CIS, otherwise NULL.

**Definition** bap.h:406

[bt\_bap\_ep\_info::dir](structbt__bap__ep__info.md#abb0dc6d25744cd734f8fd6ba2bc84b24)

enum bt\_audio\_dir dir

Capabilities type.

**Definition** bap.h:398

[bt\_bap\_ep\_info::can\_send](structbt__bap__ep__info.md#abbad124bf9e40ed530b2a33fefbadc84)

bool can\_send

True if the stream associated with the endpoint is able to send data.

**Definition** bap.h:401

[bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md)

**Definition** bap.h:1918

[bt\_bap\_scan\_delegator\_add\_src\_param::num\_subgroups](structbt__bap__scan__delegator__add__src__param.md#a12bed26ffdc9d4683a5fcdf512a194eb)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:1929

[bt\_bap\_scan\_delegator\_add\_src\_param::encrypt\_state](structbt__bap__scan__delegator__add__src__param.md#a502d263982995c99559714f07d74443f)

enum bt\_bap\_big\_enc\_state encrypt\_state

The broadcast isochronous group encryption state.

**Definition** bap.h:1923

[bt\_bap\_scan\_delegator\_add\_src\_param::pa\_sync](structbt__bap__scan__delegator__add__src__param.md#a7e2ae6194fe7878e6f8d4967f005c7aa)

struct bt\_le\_per\_adv\_sync \* pa\_sync

The periodic adverting sync.

**Definition** bap.h:1920

[bt\_bap\_scan\_delegator\_add\_src\_param::broadcast\_id](structbt__bap__scan__delegator__add__src__param.md#a8e8eda4139e460800c6195b4c5f246e2)

uint32\_t broadcast\_id

The 24-bit broadcast ID.

**Definition** bap.h:1926

[bt\_bap\_scan\_delegator\_add\_src\_param::subgroups](structbt__bap__scan__delegator__add__src__param.md#a9153dbdef5b507ef14e73a188cb00ae1)

struct bt\_bap\_bass\_subgroup subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]

Subgroup specific information.

**Definition** bap.h:1932

[bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md)

**Definition** bap.h:295

[bt\_bap\_scan\_delegator\_cb::pa\_sync\_req](structbt__bap__scan__delegator__cb.md#a0ea55963f92361f35e68eadcf10306b1)

int(\* pa\_sync\_req)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state, bool past\_avail, uint16\_t pa\_interval)

Periodic advertising sync request.

**Definition** bap.h:329

[bt\_bap\_scan\_delegator\_cb::pa\_sync\_term\_req](structbt__bap__scan__delegator__cb.md#a5b918538cfe0edaa69155f891981eeae)

int(\* pa\_sync\_term\_req)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state)

Periodic advertising sync termination request.

**Definition** bap.h:346

[bt\_bap\_scan\_delegator\_cb::recv\_state\_updated](structbt__bap__scan__delegator__cb.md#a5d95631d95ae1085071c9b795eca1a8e)

void(\* recv\_state\_updated)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state)

Receive state updated.

**Definition** bap.h:305

[bt\_bap\_scan\_delegator\_cb::broadcast\_code](structbt__bap__scan__delegator__cb.md#a8b0efda7e68164189b52f73abac025b8)

void(\* broadcast\_code)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state, const uint8\_t broadcast\_code[16])

Broadcast code received.

**Definition** bap.h:360

[bt\_bap\_scan\_delegator\_cb::bis\_sync\_req](structbt__bap__scan__delegator__cb.md#a959112080deec0ab2dcc2c09a6958874)

int(\* bis\_sync\_req)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state, const uint32\_t bis\_sync\_req[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS])

Broadcast Isochronous Stream synchronize request.

**Definition** bap.h:384

[bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md)

**Definition** bap.h:1950

[bt\_bap\_scan\_delegator\_mod\_src\_param::broadcast\_id](structbt__bap__scan__delegator__mod__src__param.md#a11b4c6d787bd2c828e565282daf5cf2f)

uint32\_t broadcast\_id

The 24-bit broadcast ID.

**Definition** bap.h:1958

[bt\_bap\_scan\_delegator\_mod\_src\_param::subgroups](structbt__bap__scan__delegator__mod__src__param.md#a14ffee52751dd152b1a8cc0822d1702f)

struct bt\_bap\_bass\_subgroup subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]

Subgroup specific information.

**Definition** bap.h:1969

[bt\_bap\_scan\_delegator\_mod\_src\_param::num\_subgroups](structbt__bap__scan__delegator__mod__src__param.md#aa8dcd7983005ffd23779db6b6ccfb752)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:1961

[bt\_bap\_scan\_delegator\_mod\_src\_param::src\_id](structbt__bap__scan__delegator__mod__src__param.md#ae387a2c0613545ae3acd372780f738bb)

uint8\_t src\_id

The periodic adverting sync.

**Definition** bap.h:1952

[bt\_bap\_scan\_delegator\_mod\_src\_param::encrypt\_state](structbt__bap__scan__delegator__mod__src__param.md#aecc8b74632dcb2b17b9a358e00c75d31)

enum bt\_bap\_big\_enc\_state encrypt\_state

The broadcast isochronous group encryption state.

**Definition** bap.h:1955

[bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md)

Represents the Broadcast Audio Scan Service receive state.

**Definition** bap.h:263

[bt\_bap\_scan\_delegator\_recv\_state::src\_id](structbt__bap__scan__delegator__recv__state.md#a1755a6332c86aeaf624d3c540037772a)

uint8\_t src\_id

The source ID.

**Definition** bap.h:265

[bt\_bap\_scan\_delegator\_recv\_state::pa\_sync\_state](structbt__bap__scan__delegator__recv__state.md#a30fbad06780fd7bca9aacdf14ecaf4a0)

enum bt\_bap\_pa\_state pa\_sync\_state

The periodic adverting sync state.

**Definition** bap.h:274

[bt\_bap\_scan\_delegator\_recv\_state::bad\_code](structbt__bap__scan__delegator__recv__state.md#a3fb5ae9266643182798ef056d1569821)

uint8\_t bad\_code[16]

The bad broadcast code.

**Definition** bap.h:286

[bt\_bap\_scan\_delegator\_recv\_state::addr](structbt__bap__scan__delegator__recv__state.md#a6153ea6bbfe7057c39f6b652a4e6e34e)

bt\_addr\_le\_t addr

The Bluetooth address.

**Definition** bap.h:268

[bt\_bap\_scan\_delegator\_recv\_state::adv\_sid](structbt__bap__scan__delegator__recv__state.md#aa03e02a1832950e4a53ff2fe803c14a6)

uint8\_t adv\_sid

The advertising set ID.

**Definition** bap.h:271

[bt\_bap\_scan\_delegator\_recv\_state::num\_subgroups](structbt__bap__scan__delegator__recv__state.md#aa97765bdbaa43a280645eb62c0035b82)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:289

[bt\_bap\_scan\_delegator\_recv\_state::broadcast\_id](structbt__bap__scan__delegator__recv__state.md#abaa80f30cf2e84ee873d18eaedd4159d)

uint32\_t broadcast\_id

The 24-bit broadcast ID.

**Definition** bap.h:280

[bt\_bap\_scan\_delegator\_recv\_state::encrypt\_state](structbt__bap__scan__delegator__recv__state.md#ac770a5ad001f73d3acaf2b36827f9343)

enum bt\_bap\_big\_enc\_state encrypt\_state

The broadcast isochronous group encryption state.

**Definition** bap.h:277

[bt\_bap\_scan\_delegator\_recv\_state::subgroups](structbt__bap__scan__delegator__recv__state.md#ae674ccfdc1905f230b0f7a58cc553274)

struct bt\_bap\_bass\_subgroup subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]

Subgroup specific information.

**Definition** bap.h:292

[bt\_bap\_stream\_ops](structbt__bap__stream__ops.md)

Stream operation.

**Definition** bap.h:467

[bt\_bap\_stream\_ops::connected](structbt__bap__stream__ops.md#a533d5ea96aa67b9b74b19c55afd43df1)

void(\* connected)(struct bt\_bap\_stream \*stream)

Isochronous channel connected callback.

**Definition** bap.h:593

[bt\_bap\_stream\_ops::started](structbt__bap__stream__ops.md#a7f595e37d40b94510bf09c1f82b479f3)

void(\* started)(struct bt\_bap\_stream \*stream)

Stream started callback.

**Definition** bap.h:537

[bt\_bap\_stream\_ops::disconnected](structbt__bap__stream__ops.md#a953c7174297f1a27ceed012dced53c5a)

void(\* disconnected)(struct bt\_bap\_stream \*stream, uint8\_t reason)

Isochronous channel disconnected callback.

**Definition** bap.h:607

[bt\_bap\_stream\_ops::stopped](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5)

void(\* stopped)(struct bt\_bap\_stream \*stream, uint8\_t reason)

Stream stopped callback.

**Definition** bap.h:547

[bt\_bap\_stream](structbt__bap__stream.md)

Basic Audio Profile stream structure.

**Definition** bap.h:427

[bt\_bap\_stream::group](structbt__bap__stream.md#a17d91a06d581cd4341d035eb76d8e0b2)

void \* group

Unicast or Broadcast group - Used internally.

**Definition** bap.h:453

[bt\_bap\_stream::codec\_cfg](structbt__bap__stream.md#a2abf6e4d8cbbdbb6e2ccd705581484ed)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Codec Configuration.

**Definition** bap.h:435

[bt\_bap\_stream::ops](structbt__bap__stream.md#a46a1f70c1a1fe4696039be14adf3c9b6)

struct bt\_bap\_stream\_ops \* ops

Audio stream operations.

**Definition** bap.h:441

[bt\_bap\_stream::qos](structbt__bap__stream.md#a854ff3dec732d17821fb304667e0518e)

struct bt\_audio\_codec\_qos \* qos

QoS Configuration.

**Definition** bap.h:438

[bt\_bap\_stream::conn](structbt__bap__stream.md#adb95fe7a0b981a46898382ee45fd99df)

struct bt\_conn \* conn

Connection reference.

**Definition** bap.h:429

[bt\_bap\_stream::ep](structbt__bap__stream.md#af871d28b2cca8e4deba66997badbeca2)

struct bt\_bap\_ep \* ep

Endpoint reference.

**Definition** bap.h:432

[bt\_bap\_stream::user\_data](structbt__bap__stream.md#afe81620dd215aebe04ddc9e36dc7d2dd)

void \* user\_data

Stream user data.

**Definition** bap.h:456

[bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md)

Unicast Client callback structure.

**Definition** bap.h:1152

[bt\_bap\_unicast\_client\_cb::enable](structbt__bap__unicast__client__cb.md#a15dd1277b37dcd96a545bb6d450c2f9d)

void(\* enable)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_enable().

**Definition** bap.h:1219

[bt\_bap\_unicast\_client\_cb::discover](structbt__bap__unicast__client__cb.md#a1f2f7476506b6b798c1f26371217956e)

void(\* discover)(struct bt\_conn \*conn, int err, enum bt\_audio\_dir dir)

BAP discovery callback function.

**Definition** bap.h:1333

[bt\_bap\_unicast\_client\_cb::qos](structbt__bap__unicast__client__cb.md#a23b82e9f4174bcc2130d6f4570990180)

void(\* qos)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_qos().

**Definition** bap.h:1206

[bt\_bap\_unicast\_client\_cb::pac\_record](structbt__bap__unicast__client__cb.md#a3c55f4e23607b1e655b5f520d691bf33)

void(\* pac\_record)(struct bt\_conn \*conn, enum bt\_audio\_dir dir, const struct bt\_audio\_codec\_cap \*codec\_cap)

Remote Published Audio Capability (PAC) record discovered.

**Definition** bap.h:1305

[bt\_bap\_unicast\_client\_cb::disable](structbt__bap__unicast__client__cb.md#a47f86af7675fcf6ac86fad578437afa9)

void(\* disable)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_disable().

**Definition** bap.h:1262

[bt\_bap\_unicast\_client\_cb::start](structbt__bap__unicast__client__cb.md#a5c2d9ec444699ae5c75736115aab0b71)

void(\* start)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_start().

**Definition** bap.h:1234

[bt\_bap\_unicast\_client\_cb::location](structbt__bap__unicast__client__cb.md#a64546cd17ac346dcb4bbfad5bd9f9616)

void(\* location)(struct bt\_conn \*conn, enum bt\_audio\_dir dir, enum bt\_audio\_location loc)

Remote Unicast Server Audio Locations.

**Definition** bap.h:1165

[bt\_bap\_unicast\_client\_cb::metadata](structbt__bap__unicast__client__cb.md#a7b5fcba437b1532dbac796a48fee2f6a)

void(\* metadata)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_metadata().

**Definition** bap.h:1275

[bt\_bap\_unicast\_client\_cb::release](structbt__bap__unicast__client__cb.md#a7dc1f2486bdabf37b85d0b347563e314)

void(\* release)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_release().

**Definition** bap.h:1288

[bt\_bap\_unicast\_client\_cb::stop](structbt__bap__unicast__client__cb.md#abf8ec1b630220172887e3d3d4c550992)

void(\* stop)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_stop().

**Definition** bap.h:1249

[bt\_bap\_unicast\_client\_cb::available\_contexts](structbt__bap__unicast__client__cb.md#ac49c3b8283552213623608498a7befd2)

void(\* available\_contexts)(struct bt\_conn \*conn, enum bt\_audio\_context snk\_ctx, enum bt\_audio\_context src\_ctx)

Remote Unicast Server Available Contexts.

**Definition** bap.h:1179

[bt\_bap\_unicast\_client\_cb::endpoint](structbt__bap__unicast__client__cb.md#ae473ecc92b5c02a29742d0ba0c51ef4a)

void(\* endpoint)(struct bt\_conn \*conn, enum bt\_audio\_dir dir, struct bt\_bap\_ep \*ep)

Remote Audio Stream Endoint (ASE) discovered.

**Definition** bap.h:1319

[bt\_bap\_unicast\_client\_cb::config](structbt__bap__unicast__client__cb.md#ae5c31f2540eb39c5b8272b5ae1e867fd)

void(\* config)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_config() and bt\_bap\_stream\_reconfig().

**Definition** bap.h:1191

[bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md)

**Definition** bap.h:1057

[bt\_bap\_unicast\_group\_param::packing](structbt__bap__unicast__group__param.md#a6829c82346ca70772a4ab0dc93fbb88f)

uint8\_t packing

Unicast Group packing mode.

**Definition** bap.h:1070

[bt\_bap\_unicast\_group\_param::params\_count](structbt__bap__unicast__group__param.md#a9cd09b720fa9a31364878ba205b3b58c)

size\_t params\_count

The number of parameters in params.

**Definition** bap.h:1059

[bt\_bap\_unicast\_group\_param::params](structbt__bap__unicast__group__param.md#aefae7dfccdaed2bc3f59ca63689d4f2e)

struct bt\_bap\_unicast\_group\_stream\_pair\_param \* params

Array of stream parameters.

**Definition** bap.h:1062

[bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md)

Parameter struct for the unicast group functions.

**Definition** bap.h:1049

[bt\_bap\_unicast\_group\_stream\_pair\_param::rx\_param](structbt__bap__unicast__group__stream__pair__param.md#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d)

struct bt\_bap\_unicast\_group\_stream\_param \* rx\_param

Pointer to a receiving stream parameters.

**Definition** bap.h:1051

[bt\_bap\_unicast\_group\_stream\_pair\_param::tx\_param](structbt__bap__unicast__group__stream__pair__param.md#ae73a11aab16a60806d1a941306c1822a)

struct bt\_bap\_unicast\_group\_stream\_param \* tx\_param

Pointer to a transmiting stream parameters.

**Definition** bap.h:1054

[bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md)

Parameter struct for each stream in the unicast group.

**Definition** bap.h:1036

[bt\_bap\_unicast\_group\_stream\_param::qos](structbt__bap__unicast__group__stream__param.md#a570776d2b689a76884331a0bc00e50ec)

struct bt\_audio\_codec\_qos \* qos

The QoS settings for the stream object.

**Definition** bap.h:1041

[bt\_bap\_unicast\_group\_stream\_param::stream](structbt__bap__unicast__group__stream__param.md#acfa192fed73b27fb194881f0021fcb35)

struct bt\_bap\_stream \* stream

Pointer to a stream object.

**Definition** bap.h:1038

[bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md)

Unicast Server callback structure.

**Definition** bap.h:826

[bt\_bap\_unicast\_server\_cb::reconfig](structbt__bap__unicast__server__cb.md#a0bafd8a52b3ae0b111c9a2e371d9cc62)

int(\* reconfig)(struct bt\_bap\_stream \*stream, enum bt\_audio\_dir dir, const struct bt\_audio\_codec\_cfg \*codec\_cfg, struct bt\_audio\_codec\_qos\_pref \*const pref, struct bt\_bap\_ascs\_rsp \*rsp)

Stream reconfig request callback.

**Definition** bap.h:865

[bt\_bap\_unicast\_server\_cb::disable](structbt__bap__unicast__server__cb.md#a22f1af95f055bce79e3810b9682024cf)

int(\* disable)(struct bt\_bap\_stream \*stream, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Disable request callback.

**Definition** bap.h:941

[bt\_bap\_unicast\_server\_cb::start](structbt__bap__unicast__server__cb.md#a48fb3021507a708a0847a1ebec6075ba)

int(\* start)(struct bt\_bap\_stream \*stream, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Start request callback.

**Definition** bap.h:912

[bt\_bap\_unicast\_server\_cb::metadata](structbt__bap__unicast__server__cb.md#a5fe98295e41c426a12ab4a7875b665c8)

int(\* metadata)(struct bt\_bap\_stream \*stream, const uint8\_t meta[], size\_t meta\_len, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Metadata update request callback.

**Definition** bap.h:927

[bt\_bap\_unicast\_server\_cb::enable](structbt__bap__unicast__server__cb.md#a7424079675204fba02339ddc661b77c5)

int(\* enable)(struct bt\_bap\_stream \*stream, const uint8\_t meta[], size\_t meta\_len, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Enable request callback.

**Definition** bap.h:898

[bt\_bap\_unicast\_server\_cb::qos](structbt__bap__unicast__server__cb.md#a851c6095e29ccc057d211d45a9a60a66)

int(\* qos)(struct bt\_bap\_stream \*stream, const struct bt\_audio\_codec\_qos \*qos, struct bt\_bap\_ascs\_rsp \*rsp)

Stream QoS request callback.

**Definition** bap.h:882

[bt\_bap\_unicast\_server\_cb::stop](structbt__bap__unicast__server__cb.md#a932296643929403c11512ff4ee7f7879)

int(\* stop)(struct bt\_bap\_stream \*stream, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Stop callback.

**Definition** bap.h:954

[bt\_bap\_unicast\_server\_cb::release](structbt__bap__unicast__server__cb.md#a9f5169f0bcdb3a6560f0767ec117b3c6)

int(\* release)(struct bt\_bap\_stream \*stream, struct bt\_bap\_ascs\_rsp \*rsp)

Stream release callback.

**Definition** bap.h:968

[bt\_bap\_unicast\_server\_cb::config](structbt__bap__unicast__server__cb.md#ada4b8b6a9371291a29068dcab05c17b2)

int(\* config)(struct bt\_conn \*conn, const struct bt\_bap\_ep \*ep, enum bt\_audio\_dir dir, const struct bt\_audio\_codec\_cfg \*codec\_cfg, struct bt\_bap\_stream \*\*stream, struct bt\_audio\_codec\_qos\_pref \*const pref, struct bt\_bap\_ascs\_rsp \*rsp)

Endpoint config request callback.

**Definition** bap.h:845

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:439

[bt\_iso\_recv\_info](structbt__iso__recv__info.md)

ISO Meta Data structure for received ISO packets.

**Definition** iso.h:288

[bt\_iso\_tx\_info](structbt__iso__tx__info.md)

ISO Meta Data structure for transmitted ISO packets.

**Definition** iso.h:303

[bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md)

LE advertisement and scan response packet information.

**Definition** bluetooth.h:2016

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [bap.h](bap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
