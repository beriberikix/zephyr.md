---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bap_8h_source.html
original_path: doxygen/html/bap_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bap.h

[Go to the documentation of this file.](bap_8h.md)

1

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_

13

26

27#include <[stdbool.h](stdbool_8h.md)>

28#include <stddef.h>

29#include <[stdint.h](stdint_8h.md)>

30

31#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

32#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

33#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

34#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

35#include <[zephyr/bluetooth/iso.h](iso_8h.md)>

36#include <[zephyr/net\_buf.h](net__buf_8h.md)>

37#include <[zephyr/sys/slist.h](slist_8h.md)>

38#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

39

40#ifdef \_\_cplusplus

41extern "C" {

42#endif

43

[ 45](group__bt__bap.md#ga83cfb2a817e0db6d78c300dc5dea2d8a)#define BT\_BAP\_INVALID\_BROADCAST\_ID 0xFFFFFFFFU

46

[ 55](group__bt__bap.md#ga91adb24c76c0d14757c5eec0146caebb)#define BT\_BAP\_BASS\_VALID\_BIT\_BITFIELD(\_bis\_bitfield) \

56 ((\_bis\_bitfield) == 0U || (\_bis\_bitfield) == BT\_BAP\_BIS\_SYNC\_NO\_PREF || \

57 BT\_ISO\_VALID\_BIS\_BITFIELD(\_bis\_bitfield))

58

[ 70](group__bt__bap.md#ga7bd804c68e67d0b4bfe391d80d33a6c7)#define BT\_BAP\_QOS\_CFG(\_interval, \_framing, \_phy, \_sdu, \_rtn, \_latency, \_pd) \

71 ((struct bt\_bap\_qos\_cfg){ \

72 .interval = \_interval, \

73 .framing = \_framing, \

74 .phy = \_phy, \

75 .sdu = \_sdu, \

76 .rtn = \_rtn, \

77 IF\_ENABLED(UTIL\_OR(IS\_ENABLED(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE), \

78 IS\_ENABLED(CONFIG\_BT\_BAP\_UNICAST)), \

79 (.latency = \_latency,)) \

80 .pd = \_pd, \

81 })

82

[ 84](group__bt__bap.md#ga37a5f9d7198739eef8bde6764da30de9)enum [bt\_bap\_qos\_cfg\_framing](group__bt__bap.md#ga37a5f9d7198739eef8bde6764da30de9) {

[ 86](group__bt__bap.md#gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94) [BT\_BAP\_QOS\_CFG\_FRAMING\_UNFRAMED](group__bt__bap.md#gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94) = 0x00,

[ 88](group__bt__bap.md#gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298) [BT\_BAP\_QOS\_CFG\_FRAMING\_FRAMED](group__bt__bap.md#gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298) = 0x01,

89};

90

92enum {

[ 94](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28) [BT\_BAP\_QOS\_CFG\_1M](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 96](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147) [BT\_BAP\_QOS\_CFG\_2M](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 98](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73) [BT\_BAP\_QOS\_CFG\_CODED](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

99};

100

[ 110](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)#define BT\_BAP\_QOS\_CFG\_UNFRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd) \

111 BT\_BAP\_QOS\_CFG(\_interval, BT\_BAP\_QOS\_CFG\_FRAMING\_UNFRAMED, BT\_BAP\_QOS\_CFG\_2M, \_sdu, \_rtn, \

112 \_latency, \_pd)

113

[ 123](group__bt__bap.md#gaa91c55ca2de3ddf09620948fd4914b14)#define BT\_BAP\_QOS\_CFG\_FRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd) \

124 BT\_BAP\_QOS\_CFG(\_interval, BT\_BAP\_QOS\_CFG\_FRAMING\_FRAMED, BT\_BAP\_QOS\_CFG\_2M, \_sdu, \_rtn, \

125 \_latency, \_pd)

126

[ 128](structbt__bap__qos__cfg.md)struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) {

[ 139](structbt__bap__qos__cfg.md#addf190fac00b2fb99c0d1abf13eb20b3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd](structbt__bap__qos__cfg.md#addf190fac00b2fb99c0d1abf13eb20b3);

140

148 struct {

[ 150](structbt__bap__qos__cfg.md#a60057a7812cdc5b26f839e68dc4603c4) enum [bt\_bap\_qos\_cfg\_framing](group__bt__bap.md#ga37a5f9d7198739eef8bde6764da30de9) [framing](structbt__bap__qos__cfg.md#a60057a7812cdc5b26f839e68dc4603c4);

151

[ 158](structbt__bap__qos__cfg.md#ac50ea51e1645546d8f8faa58c64672ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__bap__qos__cfg.md#ac50ea51e1645546d8f8faa58c64672ce);

159

[ 166](structbt__bap__qos__cfg.md#aaaa4a88499cfd1f90e409fa98891bf2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__bap__qos__cfg.md#aaaa4a88499cfd1f90e409fa98891bf2c);

167

[ 173](structbt__bap__qos__cfg.md#a294709496f7779ee4cb7aa542da8832b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sdu](structbt__bap__qos__cfg.md#a294709496f7779ee4cb7aa542da8832b);

174

175#if defined(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE) || defined(CONFIG\_BT\_BAP\_UNICAST) || \

176 defined(\_\_DOXYGEN\_\_)

[ 182](structbt__bap__qos__cfg.md#a912ee316aa2ddb00ebab7bb78af0f34a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__bap__qos__cfg.md#a912ee316aa2ddb00ebab7bb78af0f34a);

183#endif /\* CONFIG\_BT\_BAP\_BROADCAST\_SOURCE || CONFIG\_BT\_BAP\_UNICAST \*/

184

[ 190](structbt__bap__qos__cfg.md#abf8a1b76cc0735b9aec1962d2ce574ec) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval](structbt__bap__qos__cfg.md#abf8a1b76cc0735b9aec1962d2ce574ec);

191

192#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 204](structbt__bap__qos__cfg.md#acb84f2da73e865e38dcefa92007f01e1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__bap__qos__cfg.md#acb84f2da73e865e38dcefa92007f01e1);

205

[ 211](structbt__bap__qos__cfg.md#a597b81261511ec820caa66bd091ab896) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_number](structbt__bap__qos__cfg.md#a597b81261511ec820caa66bd091ab896);

212

[ 220](structbt__bap__qos__cfg.md#a97094ac8254ff3e97790943a5c71cdf3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__bap__qos__cfg.md#a97094ac8254ff3e97790943a5c71cdf3);

221#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

222 };

223};

224

[ 237](group__bt__bap.md#ga7a3fc7cb21be45276cf50846c076101d)#define BT\_BAP\_QOS\_CFG\_PREF(\_unframed\_supported, \_phy, \_rtn, \_latency, \_pd\_min, \_pd\_max, \

238 \_pref\_pd\_min, \_pref\_pd\_max) \

239 { \

240 .unframed\_supported = \_unframed\_supported, .phy = \_phy, .rtn = \_rtn, \

241 .latency = \_latency, .pd\_min = \_pd\_min, .pd\_max = \_pd\_max, \

242 .pref\_pd\_min = \_pref\_pd\_min, .pref\_pd\_max = \_pref\_pd\_max, \

243 }

244

[ 246](structbt__bap__qos__cfg__pref.md)struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) {

[ 253](structbt__bap__qos__cfg__pref.md#a2a2de382f04a50d26d174dcc7c7a12c1) bool [unframed\_supported](structbt__bap__qos__cfg__pref.md#a2a2de382f04a50d26d174dcc7c7a12c1);

254

[ 261](structbt__bap__qos__cfg__pref.md#a697a67e623d758b76be342a125a369a6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__bap__qos__cfg__pref.md#a697a67e623d758b76be342a125a369a6);

262

[ 268](structbt__bap__qos__cfg__pref.md#a286bfb02d35ca148f263f1fa1ca9e061) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__bap__qos__cfg__pref.md#a286bfb02d35ca148f263f1fa1ca9e061);

269

[ 275](structbt__bap__qos__cfg__pref.md#ac5871b4f58be038eeda483e8d07b9b53) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__bap__qos__cfg__pref.md#ac5871b4f58be038eeda483e8d07b9b53);

276

[ 284](structbt__bap__qos__cfg__pref.md#a3f643768de9d8b0a7a62e403703e0033) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd\_min](structbt__bap__qos__cfg__pref.md#a3f643768de9d8b0a7a62e403703e0033);

285

[ 293](structbt__bap__qos__cfg__pref.md#a666be60856b5b4688d21d7a36b956c29) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd\_max](structbt__bap__qos__cfg__pref.md#a666be60856b5b4688d21d7a36b956c29);

294

[ 301](structbt__bap__qos__cfg__pref.md#a1df8cd4ed27e9099b8b2a069855010aa) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pref\_pd\_min](structbt__bap__qos__cfg__pref.md#a1df8cd4ed27e9099b8b2a069855010aa);

302

[ 310](structbt__bap__qos__cfg__pref.md#ab6475a80b33a9cea69edeaa3093c9070) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pref\_pd\_max](structbt__bap__qos__cfg__pref.md#ab6475a80b33a9cea69edeaa3093c9070);

311};

312

[ 314](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296)enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) {

[ 316](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf) [BT\_BAP\_PA\_STATE\_NOT\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf) = 0x00,

317

[ 319](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb) [BT\_BAP\_PA\_STATE\_INFO\_REQ](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb) = 0x01,

320

[ 322](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc) [BT\_BAP\_PA\_STATE\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc) = 0x02,

323

[ 325](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647) [BT\_BAP\_PA\_STATE\_FAILED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647) = 0x03,

326

[ 328](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d) [BT\_BAP\_PA\_STATE\_NO\_PAST](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d) = 0x04,

329};

330

[ 332](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22)enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) {

[ 334](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4) [BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4) = 0x00,

335

[ 337](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2) [BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2) = 0x01,

338

[ 340](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10) [BT\_BAP\_BIG\_ENC\_STATE\_DEC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10) = 0x02,

341

[ 343](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b) [BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b) = 0x03,

344};

345

[ 347](group__bt__bap.md#ga13e9b6d571a613d689b8ba58bae64ae3)enum [bt\_bap\_bass\_att\_err](group__bt__bap.md#ga13e9b6d571a613d689b8ba58bae64ae3) {

[ 349](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c) [BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c) = 0x80,

350

[ 352](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202) [BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202) = 0x81,

353};

354

[ 356](group__bt__bap.md#ga357079ef00ce6f250e72a37103926c64)#define BT\_BAP\_PA\_INTERVAL\_UNKNOWN 0xFFFF

357

[ 364](group__bt__bap.md#ga799f1417272e9b545c1e30ed4616b988)#define BT\_BAP\_BIS\_SYNC\_NO\_PREF 0xFFFFFFFF

[ 366](group__bt__bap.md#ga2a2e4a06f6e39360458fe2e4d0b66833)#define BT\_BAP\_BIS\_SYNC\_FAILED 0xFFFFFFFF

367

[ 369](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a)enum [bt\_bap\_ep\_state](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a) {

[ 371](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961) [BT\_BAP\_EP\_STATE\_IDLE](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961) = 0x00,

372

[ 374](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688) [BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688) = 0x01,

375

[ 377](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523) [BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523) = 0x02,

378

[ 380](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332) [BT\_BAP\_EP\_STATE\_ENABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332) = 0x03,

381

[ 383](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710) [BT\_BAP\_EP\_STATE\_STREAMING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710) = 0x04,

384

[ 386](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8) [BT\_BAP\_EP\_STATE\_DISABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8) = 0x05,

387

[ 389](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c) [BT\_BAP\_EP\_STATE\_RELEASING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c) = 0x06,

390};

391

[ 398](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1)enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) {

[ 400](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd) [BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd) = 0x00,

[ 402](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d) [BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d) = 0x01,

[ 404](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9) [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9) = 0x02,

[ 406](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa) [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa) = 0x03,

[ 408](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5) [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5) = 0x04,

[ 410](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146) [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146) = 0x05,

[ 412](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a) [BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a) = 0x06,

[ 414](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62) [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62) = 0x07,

[ 416](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) = 0x08,

[ 418](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219) [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219) = 0x09,

[ 420](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7) [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7) = 0x0a,

[ 422](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06) [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06) = 0x0b,

[ 424](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06) [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06) = 0x0c,

[ 426](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb) [BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb) = 0x0d,

[ 428](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a) [BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a) = 0x0e,

429};

430

[ 438](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45)enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) {

[ 440](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd) [BT\_BAP\_ASCS\_REASON\_NONE](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd) = 0x00,

[ 442](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea) [BT\_BAP\_ASCS\_REASON\_CODEC](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea) = 0x01,

[ 444](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0) [BT\_BAP\_ASCS\_REASON\_CODEC\_DATA](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0) = 0x02,

[ 446](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c) [BT\_BAP\_ASCS\_REASON\_INTERVAL](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c) = 0x03,

[ 448](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539) [BT\_BAP\_ASCS\_REASON\_FRAMING](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539) = 0x04,

[ 450](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8) [BT\_BAP\_ASCS\_REASON\_PHY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8) = 0x05,

[ 452](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b) [BT\_BAP\_ASCS\_REASON\_SDU](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b) = 0x06,

[ 454](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf) [BT\_BAP\_ASCS\_REASON\_RTN](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf) = 0x07,

[ 456](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942) [BT\_BAP\_ASCS\_REASON\_LATENCY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942) = 0x08,

[ 458](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557) [BT\_BAP\_ASCS\_REASON\_PD](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557) = 0x09,

[ 460](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c) [BT\_BAP\_ASCS\_REASON\_CIS](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c) = 0x0a,

461};

462

[ 464](structbt__bap__ascs__rsp.md)struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) {

[ 478](structbt__bap__ascs__rsp.md#a8ea364298f7e3e784b7878215db63d91) enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) [code](structbt__bap__ascs__rsp.md#a8ea364298f7e3e784b7878215db63d91);

479

485 union {

[ 501](structbt__bap__ascs__rsp.md#a138532bc40f60547c56d8b108ad44d1e) enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) [reason](structbt__bap__ascs__rsp.md#a138532bc40f60547c56d8b108ad44d1e);

502

[ 511](structbt__bap__ascs__rsp.md#a736f44864015244a8b48a859eff6b902) enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) [metadata\_type](structbt__bap__ascs__rsp.md#a736f44864015244a8b48a859eff6b902);

512 };

513};

514

[ 522](group__bt__bap.md#ga8e5cd46a1428a315119e47c9cbbb9bfd)#define BT\_BAP\_ASCS\_RSP(c, r) (struct bt\_bap\_ascs\_rsp) { .code = c, .reason = r }

523

525struct bt\_bap\_broadcast\_source;

526

528struct bt\_bap\_broadcast\_sink;

529

531struct bt\_bap\_unicast\_group;

532

534struct bt\_bap\_ep;

535

[ 537](structbt__bap__bass__subgroup.md)struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) {

[ 539](structbt__bap__bass__subgroup.md#ac8061995eb73ba30e335e37714396ff5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bis\_sync](structbt__bap__bass__subgroup.md#ac8061995eb73ba30e335e37714396ff5);

540

[ 542](structbt__bap__bass__subgroup.md#ace1c1ff5d2f5cc79838653d468166664) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [metadata\_len](structbt__bap__bass__subgroup.md#ace1c1ff5d2f5cc79838653d468166664);

543

544#if defined(CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE) || defined(\_\_DOXYGEN\_\_)

[ 546](structbt__bap__bass__subgroup.md#a851fda16d0856714ebf4d3970c4d2e4b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [metadata](structbt__bap__bass__subgroup.md#a851fda16d0856714ebf4d3970c4d2e4b)[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE];

547#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE \*/

548};

549

[ 551](structbt__bap__scan__delegator__recv__state.md)struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) {

[ 553](structbt__bap__scan__delegator__recv__state.md#a1755a6332c86aeaf624d3c540037772a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__bap__scan__delegator__recv__state.md#a1755a6332c86aeaf624d3c540037772a);

554

[ 556](structbt__bap__scan__delegator__recv__state.md#a6153ea6bbfe7057c39f6b652a4e6e34e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__bap__scan__delegator__recv__state.md#a6153ea6bbfe7057c39f6b652a4e6e34e);

557

[ 559](structbt__bap__scan__delegator__recv__state.md#aa03e02a1832950e4a53ff2fe803c14a6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__bap__scan__delegator__recv__state.md#aa03e02a1832950e4a53ff2fe803c14a6);

560

[ 562](structbt__bap__scan__delegator__recv__state.md#a30fbad06780fd7bca9aacdf14ecaf4a0) enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) [pa\_sync\_state](structbt__bap__scan__delegator__recv__state.md#a30fbad06780fd7bca9aacdf14ecaf4a0);

563

[ 565](structbt__bap__scan__delegator__recv__state.md#ac770a5ad001f73d3acaf2b36827f9343) enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) [encrypt\_state](structbt__bap__scan__delegator__recv__state.md#ac770a5ad001f73d3acaf2b36827f9343);

566

[ 568](structbt__bap__scan__delegator__recv__state.md#abaa80f30cf2e84ee873d18eaedd4159d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__bap__scan__delegator__recv__state.md#abaa80f30cf2e84ee873d18eaedd4159d);

569

[ 575](structbt__bap__scan__delegator__recv__state.md#a1c268bb7b340c874935f186c0ba2a253) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bad\_code](structbt__bap__scan__delegator__recv__state.md#a1c268bb7b340c874935f186c0ba2a253)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

576

[ 578](structbt__bap__scan__delegator__recv__state.md#aa97765bdbaa43a280645eb62c0035b82) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__scan__delegator__recv__state.md#aa97765bdbaa43a280645eb62c0035b82);

579

[ 585](structbt__bap__scan__delegator__recv__state.md#ae674ccfdc1905f230b0f7a58cc553274) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) [subgroups](structbt__bap__scan__delegator__recv__state.md#ae674ccfdc1905f230b0f7a58cc553274)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS];

586};

587

[ 593](structbt__bap__scan__delegator__cb.md)struct [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md) {

[ 603](structbt__bap__scan__delegator__cb.md#a5d95631d95ae1085071c9b795eca1a8e) void (\*[recv\_state\_updated](structbt__bap__scan__delegator__cb.md#a5d95631d95ae1085071c9b795eca1a8e))(struct bt\_conn \*conn,

604 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state);

605

[ 622](structbt__bap__scan__delegator__cb.md#a0ea55963f92361f35e68eadcf10306b1) int (\*[pa\_sync\_req](structbt__bap__scan__delegator__cb.md#a0ea55963f92361f35e68eadcf10306b1))(struct bt\_conn \*conn,

623 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state,

624 bool past\_avail, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pa\_interval);

625

[ 639](structbt__bap__scan__delegator__cb.md#a5b918538cfe0edaa69155f891981eeae) int (\*[pa\_sync\_term\_req](structbt__bap__scan__delegator__cb.md#a5b918538cfe0edaa69155f891981eeae))(struct bt\_conn \*conn,

640 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state);

641

[ 653](structbt__bap__scan__delegator__cb.md#a78d011c817e60725a0ef14c68bd655cd) void (\*[broadcast\_code](structbt__bap__scan__delegator__cb.md#a78d011c817e60725a0ef14c68bd655cd))(struct bt\_conn \*conn,

654 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state,

655 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__bap__scan__delegator__cb.md#a78d011c817e60725a0ef14c68bd655cd)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)]);

[ 677](structbt__bap__scan__delegator__cb.md#a959112080deec0ab2dcc2c09a6958874) int (\*[bis\_sync\_req](structbt__bap__scan__delegator__cb.md#a959112080deec0ab2dcc2c09a6958874))(struct bt\_conn \*conn,

678 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state,

679 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bis\_sync\_req](structbt__bap__scan__delegator__cb.md#a959112080deec0ab2dcc2c09a6958874)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]);

[ 689](structbt__bap__scan__delegator__cb.md#ae41d499d75123a1b70b778e8e95edcc3) void (\*[scanning\_state](structbt__bap__scan__delegator__cb.md#ae41d499d75123a1b70b778e8e95edcc3))(struct bt\_conn \*conn, bool is\_scanning);

690};

691

[ 693](structbt__bap__ep__info.md)struct [bt\_bap\_ep\_info](structbt__bap__ep__info.md) {

[ 695](structbt__bap__ep__info.md#a07e8878e7e6a8ee059639330ffa78c1c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__bap__ep__info.md#a07e8878e7e6a8ee059639330ffa78c1c);

696

[ 698](structbt__bap__ep__info.md#a650727747d0a093528544c3e16255feb) enum [bt\_bap\_ep\_state](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a) [state](structbt__bap__ep__info.md#a650727747d0a093528544c3e16255feb);

699

[ 701](structbt__bap__ep__info.md#abb0dc6d25744cd734f8fd6ba2bc84b24) enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) [dir](structbt__bap__ep__info.md#abb0dc6d25744cd734f8fd6ba2bc84b24);

702

[ 704](structbt__bap__ep__info.md#a54dd673e21455c85193df844f3aa4083) struct [bt\_iso\_chan](structbt__iso__chan.md) \*[iso\_chan](structbt__bap__ep__info.md#a54dd673e21455c85193df844f3aa4083);

705

[ 707](structbt__bap__ep__info.md#abbad124bf9e40ed530b2a33fefbadc84) bool [can\_send](structbt__bap__ep__info.md#abbad124bf9e40ed530b2a33fefbadc84);

708

[ 710](structbt__bap__ep__info.md#a30698c71f556ca876a1c69bffefac653) bool [can\_recv](structbt__bap__ep__info.md#a30698c71f556ca876a1c69bffefac653);

711

[ 715](structbt__bap__ep__info.md#a819ac77dcf7cb6985e97f290a666ed09) struct bt\_bap\_ep \*[paired\_ep](structbt__bap__ep__info.md#a819ac77dcf7cb6985e97f290a666ed09);

716

[ 718](structbt__bap__ep__info.md#ad5201e9b9623e8ff8e74e1be87ece864) const struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*[qos\_pref](structbt__bap__ep__info.md#ad5201e9b9623e8ff8e74e1be87ece864);

719};

720

[ 730](group__bt__bap.md#gaf15e5ec5bca364f6a3e7a43b1f27da68)int [bt\_bap\_ep\_get\_info](group__bt__bap.md#gaf15e5ec5bca364f6a3e7a43b1f27da68)(const struct bt\_bap\_ep \*ep, struct [bt\_bap\_ep\_info](structbt__bap__ep__info.md) \*info);

731

[ 740](structbt__bap__stream.md)struct [bt\_bap\_stream](structbt__bap__stream.md) {

[ 742](structbt__bap__stream.md#adb95fe7a0b981a46898382ee45fd99df) struct bt\_conn \*[conn](structbt__bap__stream.md#adb95fe7a0b981a46898382ee45fd99df);

743

[ 745](structbt__bap__stream.md#af871d28b2cca8e4deba66997badbeca2) struct bt\_bap\_ep \*[ep](structbt__bap__stream.md#af871d28b2cca8e4deba66997badbeca2);

746

[ 748](structbt__bap__stream.md#a2abf6e4d8cbbdbb6e2ccd705581484ed) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__bap__stream.md#a2abf6e4d8cbbdbb6e2ccd705581484ed);

749

[ 751](structbt__bap__stream.md#a41cfe6496de63d05f86bcab90b9fbbf2) struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*[qos](structbt__bap__stream.md#a41cfe6496de63d05f86bcab90b9fbbf2);

752

[ 754](structbt__bap__stream.md#a46a1f70c1a1fe4696039be14adf3c9b6) struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*[ops](structbt__bap__stream.md#a46a1f70c1a1fe4696039be14adf3c9b6);

755

756#if defined(CONFIG\_BT\_BAP\_UNICAST\_CLIENT) || defined(\_\_DOXYGEN\_\_)

[ 762](structbt__bap__stream.md#af5fdb04fdeb394a0345ece23331445e5) struct bt\_bap\_iso \*[bap\_iso](structbt__bap__stream.md#af5fdb04fdeb394a0345ece23331445e5);

763#endif /\* CONFIG\_BT\_BAP\_UNICAST\_CLIENT \*/

764

[ 766](structbt__bap__stream.md#a17d91a06d581cd4341d035eb76d8e0b2) void \*[group](structbt__bap__stream.md#a17d91a06d581cd4341d035eb76d8e0b2);

767

[ 769](structbt__bap__stream.md#afe81620dd215aebe04ddc9e36dc7d2dd) void \*[user\_data](structbt__bap__stream.md#afe81620dd215aebe04ddc9e36dc7d2dd);

770

771#if defined(CONFIG\_BT\_BAP\_DEBUG\_STREAM\_SEQ\_NUM) || defined(\_\_DOXYGEN\_\_)

773 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_prev\_seq\_num;

774#endif /\* CONFIG\_BT\_BAP\_DEBUG\_STREAM\_SEQ\_NUM \*/

775

777 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

778};

779

[ 781](structbt__bap__stream__ops.md)struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) {

782#if defined(CONFIG\_BT\_BAP\_UNICAST) || defined(\_\_DOXYGEN\_\_)

[ 791](structbt__bap__stream__ops.md#a509a400c622d1684e6ab0d47bc6300ba) void (\*[configured](structbt__bap__stream__ops.md#a509a400c622d1684e6ab0d47bc6300ba))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*pref);

792

[ 801](structbt__bap__stream__ops.md#add541b683a0042bde13749b327b897dd) void (\*[qos\_set](structbt__bap__stream__ops.md#add541b683a0042bde13749b327b897dd))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

802

[ 810](structbt__bap__stream__ops.md#a1c67137b439a87647994530710d9e075) void (\*[enabled](structbt__bap__stream__ops.md#a1c67137b439a87647994530710d9e075))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

811

[ 820](structbt__bap__stream__ops.md#a553777c6b6bdda3e0e8c03f3915404cd) void (\*[metadata\_updated](structbt__bap__stream__ops.md#a553777c6b6bdda3e0e8c03f3915404cd))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

821

[ 829](structbt__bap__stream__ops.md#a3fc784b8a2a7c1a5b19dece3619c130e) void (\*[disabled](structbt__bap__stream__ops.md#a3fc784b8a2a7c1a5b19dece3619c130e))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

830

[ 839](structbt__bap__stream__ops.md#a37876562731d7dbbcd5f5613621b78ca) void (\*[released](structbt__bap__stream__ops.md#a37876562731d7dbbcd5f5613621b78ca))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

840#endif /\* CONFIG\_BT\_BAP\_UNICAST \*/

841

[ 850](structbt__bap__stream__ops.md#a7f595e37d40b94510bf09c1f82b479f3) void (\*[started](structbt__bap__stream__ops.md#a7f595e37d40b94510bf09c1f82b479f3))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

851

[ 860](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5) void (\*[stopped](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

861

862#if defined(CONFIG\_BT\_AUDIO\_RX) || defined(\_\_DOXYGEN\_\_)

[ 874](structbt__bap__stream__ops.md#a09f31dc30de9c880758ec4a1468e59f0) void (\*[recv](structbt__bap__stream__ops.md#a09f31dc30de9c880758ec4a1468e59f0))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_iso\_recv\_info](structbt__iso__recv__info.md) \*info,

875 struct [net\_buf](structnet__buf.md) \*buf);

876#endif /\* CONFIG\_BT\_AUDIO\_RX \*/

877

878#if defined(CONFIG\_BT\_AUDIO\_TX) || defined(\_\_DOXYGEN\_\_)

[ 891](structbt__bap__stream__ops.md#a33b07c51394dea6d632f42aec89a1510) void (\*[sent](structbt__bap__stream__ops.md#a33b07c51394dea6d632f42aec89a1510))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

892#endif /\* CONFIG\_BT\_AUDIO\_TX \*/

893

[ 906](structbt__bap__stream__ops.md#a533d5ea96aa67b9b74b19c55afd43df1) void (\*[connected](structbt__bap__stream__ops.md#a533d5ea96aa67b9b74b19c55afd43df1))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

907

[ 920](structbt__bap__stream__ops.md#a953c7174297f1a27ceed012dced53c5a) void (\*[disconnected](structbt__bap__stream__ops.md#a953c7174297f1a27ceed012dced53c5a))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

921};

922

[ 924](structbt__bap__unicast__server__register__param.md)struct [bt\_bap\_unicast\_server\_register\_param](structbt__bap__unicast__server__register__param.md) {

[ 930](structbt__bap__unicast__server__register__param.md#a88635d5926173f23f411402b5961f783) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [snk\_cnt](structbt__bap__unicast__server__register__param.md#a88635d5926173f23f411402b5961f783);

931

[ 936](structbt__bap__unicast__server__register__param.md#ab4963c035d75404831ec1293c7f40f95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_cnt](structbt__bap__unicast__server__register__param.md#ab4963c035d75404831ec1293c7f40f95);

937};

938

[ 947](group__bt__bap.md#gab29c1e134156dceaa6c67abae9239378)void [bt\_bap\_stream\_cb\_register](group__bt__bap.md#gab29c1e134156dceaa6c67abae9239378)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*ops);

948

[ 962](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402)int [bt\_bap\_stream\_config](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402)(struct bt\_conn \*conn, struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct bt\_bap\_ep \*ep,

963 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

964

[ 978](group__bt__bap.md#gaac84ee7b3ab5578d258848754f752546)int [bt\_bap\_stream\_reconfig](group__bt__bap.md#gaac84ee7b3ab5578d258848754f752546)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

979

[ 992](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d)int [bt\_bap\_stream\_qos](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d)(struct bt\_conn \*conn, struct bt\_bap\_unicast\_group \*[group](structgroup.md));

993

[ 1008](group__bt__bap.md#ga13a859b31b0310ec22339ec7ed0754f8)int [bt\_bap\_stream\_enable](group__bt__bap.md#ga13a859b31b0310ec22339ec7ed0754f8)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

1009

[ 1021](group__bt__bap.md#ga0afe6c927729697e2f984cefcbc7c0f1)int [bt\_bap\_stream\_metadata](group__bt__bap.md#ga0afe6c927729697e2f984cefcbc7c0f1)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

1022

[ 1035](group__bt__bap.md#ga0fd2bb35909fc19e3e9cff068ba9e9aa)int [bt\_bap\_stream\_disable](group__bt__bap.md#ga0fd2bb35909fc19e3e9cff068ba9e9aa)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

1036

[ 1060](group__bt__bap.md#gaa75f2cd2c36fdaef04a62c95bec6e2e3)int [bt\_bap\_stream\_connect](group__bt__bap.md#gaa75f2cd2c36fdaef04a62c95bec6e2e3)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

1061

[ 1084](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae)int [bt\_bap\_stream\_start](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

1085

[ 1109](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b)int [bt\_bap\_stream\_stop](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

1110

[ 1124](group__bt__bap.md#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)int [bt\_bap\_stream\_release](group__bt__bap.md#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream);

1125

[ 1140](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e)int [bt\_bap\_stream\_send](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num);

1141

[ 1158](group__bt__bap.md#gaa0e012446238c916abc84d6c0de89bf3)int [bt\_bap\_stream\_send\_ts](group__bt__bap.md#gaa0e012446238c916abc84d6c0de89bf3)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num,

1159 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

1160

[ 1179](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928)int [bt\_bap\_stream\_get\_tx\_sync](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928)(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info);

1180

1186

[ 1188](structbt__bap__unicast__server__cb.md)struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) {

[ 1207](structbt__bap__unicast__server__cb.md#ad179b35a5a5685edb8f0ac1b791d5271) int (\*[config](structbt__bap__unicast__server__cb.md#ad179b35a5a5685edb8f0ac1b791d5271))(struct bt\_conn \*conn, const struct bt\_bap\_ep \*ep, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

1208 const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, struct [bt\_bap\_stream](structbt__bap__stream.md) \*\*stream,

1209 struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*const pref, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1210

[ 1227](structbt__bap__unicast__server__cb.md#a7bed12780fdf780227d38b61d76d099b) int (\*[reconfig](structbt__bap__unicast__server__cb.md#a7bed12780fdf780227d38b61d76d099b))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

1228 const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1229 struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*const pref, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1230

[ 1244](structbt__bap__unicast__server__cb.md#a2d50b6c328607fc46d85eaf12633f13d) int (\*[qos](structbt__bap__unicast__server__cb.md#a2d50b6c328607fc46d85eaf12633f13d))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*[qos](structbt__bap__unicast__server__cb.md#a2d50b6c328607fc46d85eaf12633f13d),

1245 struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1246

[ 1260](structbt__bap__unicast__server__cb.md#a7424079675204fba02339ddc661b77c5) int (\*[enable](structbt__bap__unicast__server__cb.md#a7424079675204fba02339ddc661b77c5))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len,

1261 struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1262

[ 1274](structbt__bap__unicast__server__cb.md#a48fb3021507a708a0847a1ebec6075ba) int (\*[start](structbt__bap__unicast__server__cb.md#a48fb3021507a708a0847a1ebec6075ba))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1275

[ 1289](structbt__bap__unicast__server__cb.md#a5fe98295e41c426a12ab4a7875b665c8) int (\*[metadata](structbt__bap__unicast__server__cb.md#a5fe98295e41c426a12ab4a7875b665c8))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len,

1290 struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1291

[ 1303](structbt__bap__unicast__server__cb.md#a22f1af95f055bce79e3810b9682024cf) int (\*[disable](structbt__bap__unicast__server__cb.md#a22f1af95f055bce79e3810b9682024cf))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1304

[ 1316](structbt__bap__unicast__server__cb.md#a932296643929403c11512ff4ee7f7879) int (\*[stop](structbt__bap__unicast__server__cb.md#a932296643929403c11512ff4ee7f7879))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1317

[ 1330](structbt__bap__unicast__server__cb.md#a9f5169f0bcdb3a6560f0767ec117b3c6) int (\*[release](structbt__bap__unicast__server__cb.md#a9f5169f0bcdb3a6560f0767ec117b3c6))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp);

1331};

1332

[ 1343](group__bt__bap__unicast__server.md#gab3ea6014854e6290f058c87e866c3191)int [bt\_bap\_unicast\_server\_register](group__bt__bap__unicast__server.md#gab3ea6014854e6290f058c87e866c3191)(const struct [bt\_bap\_unicast\_server\_register\_param](structbt__bap__unicast__server__register__param.md) \*param);

1344

[ 1359](group__bt__bap__unicast__server.md#ga6ef3b9e877ffdc04cc48fda6713a0209)int [bt\_bap\_unicast\_server\_unregister](group__bt__bap__unicast__server.md#ga6ef3b9e877ffdc04cc48fda6713a0209)(void);

1360

[ 1373](group__bt__bap__unicast__server.md#ga7669133936bc13f7ab38817db9ce69c0)int [bt\_bap\_unicast\_server\_register\_cb](group__bt__bap__unicast__server.md#ga7669133936bc13f7ab38817db9ce69c0)(const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \*cb);

1374

[ 1388](group__bt__bap__unicast__server.md#gadf984f12bdeadcfc814dc2fc770cb7bf)int [bt\_bap\_unicast\_server\_unregister\_cb](group__bt__bap__unicast__server.md#gadf984f12bdeadcfc814dc2fc770cb7bf)(const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \*cb);

1389

[ 1397](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1)typedef void (\*[bt\_bap\_ep\_func\_t](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1))(struct bt\_bap\_ep \*ep, void \*user\_data);

1398

[ 1406](group__bt__bap__unicast__server.md#ga4614a504d47cf732b09d4f22302d3239)void [bt\_bap\_unicast\_server\_foreach\_ep](group__bt__bap__unicast__server.md#ga4614a504d47cf732b09d4f22302d3239)(struct bt\_conn \*conn, [bt\_bap\_ep\_func\_t](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1) func, void \*user\_data);

1407

[ 1418](group__bt__bap__unicast__server.md#ga6e71c34a21091f222d3478f4fad95319)int [bt\_bap\_unicast\_server\_config\_ase](group__bt__bap__unicast__server.md#ga6e71c34a21091f222d3478f4fad95319)(struct bt\_conn \*conn, struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream,

1419 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1420 const struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*qos\_pref);

1421 /\* End of group bt\_bap\_unicast\_server \*/

1423

1429

[ 1431](structbt__bap__unicast__group__stream__param.md)struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) {

[ 1433](structbt__bap__unicast__group__stream__param.md#acfa192fed73b27fb194881f0021fcb35) struct [bt\_bap\_stream](structbt__bap__stream.md) \*[stream](structbt__bap__unicast__group__stream__param.md#acfa192fed73b27fb194881f0021fcb35);

1434

[ 1436](structbt__bap__unicast__group__stream__param.md#a35ba371c7e1050589ab8abe75cbb605d) struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*[qos](structbt__bap__unicast__group__stream__param.md#a35ba371c7e1050589ab8abe75cbb605d);

1437};

1438

[ 1445](structbt__bap__unicast__group__stream__pair__param.md)struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) {

[ 1447](structbt__bap__unicast__group__stream__pair__param.md#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d) struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) \*[rx\_param](structbt__bap__unicast__group__stream__pair__param.md#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d);

1448

[ 1450](structbt__bap__unicast__group__stream__pair__param.md#ae73a11aab16a60806d1a941306c1822a) struct [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) \*[tx\_param](structbt__bap__unicast__group__stream__pair__param.md#ae73a11aab16a60806d1a941306c1822a);

1451};

1452

[ 1454](structbt__bap__unicast__group__param.md)struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) {

[ 1456](structbt__bap__unicast__group__param.md#a9cd09b720fa9a31364878ba205b3b58c) size\_t [params\_count](structbt__bap__unicast__group__param.md#a9cd09b720fa9a31364878ba205b3b58c);

1457

[ 1459](structbt__bap__unicast__group__param.md#aefae7dfccdaed2bc3f59ca63689d4f2e) struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) \*[params](structbt__bap__unicast__group__param.md#aefae7dfccdaed2bc3f59ca63689d4f2e);

1460

[ 1468](structbt__bap__unicast__group__param.md#a6829c82346ca70772a4ab0dc93fbb88f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__bap__unicast__group__param.md#a6829c82346ca70772a4ab0dc93fbb88f);

1469

1470#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 1479](structbt__bap__unicast__group__param.md#a7980c8e5c66a11507701ce2679b461ed) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_to\_p\_ft](structbt__bap__unicast__group__param.md#a7980c8e5c66a11507701ce2679b461ed);

1480

[ 1489](structbt__bap__unicast__group__param.md#a72e2c6dbeb7b7778f92af5cab2474a7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_to\_c\_ft](structbt__bap__unicast__group__param.md#a72e2c6dbeb7b7778f92af5cab2474a7e);

1490

[ 1498](structbt__bap__unicast__group__param.md#a278797713b97a6520247b01caa2938b9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__bap__unicast__group__param.md#a278797713b97a6520247b01caa2938b9);

1499#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

1500};

1501

[ 1515](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21)int [bt\_bap\_unicast\_group\_create](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21)(struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \*param,

1516 struct bt\_bap\_unicast\_group \*\*unicast\_group);

1517

[ 1533](group__bt__bap__unicast__client.md#gacd684504c8127ff4f8d038cc06718e5e)int [bt\_bap\_unicast\_group\_reconfig](group__bt__bap__unicast__client.md#gacd684504c8127ff4f8d038cc06718e5e)(struct bt\_bap\_unicast\_group \*unicast\_group,

1534 const struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \*param);

1535

[ 1555](group__bt__bap__unicast__client.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6)int [bt\_bap\_unicast\_group\_add\_streams](group__bt__bap__unicast__client.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6)(struct bt\_bap\_unicast\_group \*unicast\_group,

1556 struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) params[],

1557 size\_t num\_param);

1558

[ 1569](group__bt__bap__unicast__client.md#ga34dbdce6133f8366df453ec937fb47d2)int [bt\_bap\_unicast\_group\_delete](group__bt__bap__unicast__client.md#ga34dbdce6133f8366df453ec937fb47d2)(struct bt\_bap\_unicast\_group \*unicast\_group);

1570

[ 1572](structbt__bap__unicast__client__cb.md)struct [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) {

[ 1585](structbt__bap__unicast__client__cb.md#a64546cd17ac346dcb4bbfad5bd9f9616) void (\*[location](structbt__bap__unicast__client__cb.md#a64546cd17ac346dcb4bbfad5bd9f9616))(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) loc);

1586

[ 1599](structbt__bap__unicast__client__cb.md#ac49c3b8283552213623608498a7befd2) void (\*[available\_contexts](structbt__bap__unicast__client__cb.md#ac49c3b8283552213623608498a7befd2))(struct bt\_conn \*conn, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) snk\_ctx,

1600 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) src\_ctx);

1601

[ 1611](structbt__bap__unicast__client__cb.md#ae5c31f2540eb39c5b8272b5ae1e867fd) void (\*[config](structbt__bap__unicast__client__cb.md#ae5c31f2540eb39c5b8272b5ae1e867fd))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1612 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1613

[ 1626](structbt__bap__unicast__client__cb.md#a23b82e9f4174bcc2130d6f4570990180) void (\*[qos](structbt__bap__unicast__client__cb.md#a23b82e9f4174bcc2130d6f4570990180))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1627 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1628

[ 1639](structbt__bap__unicast__client__cb.md#a15dd1277b37dcd96a545bb6d450c2f9d) void (\*[enable](structbt__bap__unicast__client__cb.md#a15dd1277b37dcd96a545bb6d450c2f9d))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1640 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1641

[ 1654](structbt__bap__unicast__client__cb.md#a5c2d9ec444699ae5c75736115aab0b71) void (\*[start](structbt__bap__unicast__client__cb.md#a5c2d9ec444699ae5c75736115aab0b71))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1655 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1656

[ 1669](structbt__bap__unicast__client__cb.md#abf8ec1b630220172887e3d3d4c550992) void (\*[stop](structbt__bap__unicast__client__cb.md#abf8ec1b630220172887e3d3d4c550992))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1670 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1671

[ 1682](structbt__bap__unicast__client__cb.md#a47f86af7675fcf6ac86fad578437afa9) void (\*[disable](structbt__bap__unicast__client__cb.md#a47f86af7675fcf6ac86fad578437afa9))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1683 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1684

[ 1695](structbt__bap__unicast__client__cb.md#a7b5fcba437b1532dbac796a48fee2f6a) void (\*[metadata](structbt__bap__unicast__client__cb.md#a7b5fcba437b1532dbac796a48fee2f6a))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1696 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1697

[ 1708](structbt__bap__unicast__client__cb.md#a7dc1f2486bdabf37b85d0b347563e314) void (\*[release](structbt__bap__unicast__client__cb.md#a7dc1f2486bdabf37b85d0b347563e314))(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code,

1709 enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason);

1710

[ 1725](structbt__bap__unicast__client__cb.md#a3c55f4e23607b1e655b5f520d691bf33) void (\*[pac\_record](structbt__bap__unicast__client__cb.md#a3c55f4e23607b1e655b5f520d691bf33))(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

1726 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1727

[ 1739](structbt__bap__unicast__client__cb.md#ae473ecc92b5c02a29742d0ba0c51ef4a) void (\*[endpoint](structbt__bap__unicast__client__cb.md#ae473ecc92b5c02a29742d0ba0c51ef4a))(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct bt\_bap\_ep \*ep);

1740

[ 1753](structbt__bap__unicast__client__cb.md#a1f2f7476506b6b798c1f26371217956e) void (\*[discover](structbt__bap__unicast__client__cb.md#a1f2f7476506b6b798c1f26371217956e))(struct bt\_conn \*conn, int err, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir);

1754

1757 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

1759};

1760

[ 1773](group__bt__bap__unicast__client.md#gade70f04ae1a828b43b3b44fa8933f674)int [bt\_bap\_unicast\_client\_register\_cb](group__bt__bap__unicast__client.md#gade70f04ae1a828b43b3b44fa8933f674)(struct [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) \*cb);

1774

[ 1784](group__bt__bap__unicast__client.md#gacef9c88f66762e8de19303d20dafa0bb)int [bt\_bap\_unicast\_client\_discover](group__bt__bap__unicast__client.md#gacef9c88f66762e8de19303d20dafa0bb)(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir);

1785 /\* End of group bt\_bap\_unicast\_client \*/

1793

1795struct bt\_bap\_base\_subgroup;

1797struct bt\_bap\_base;

1798

[ 1800](structbt__bap__base__codec__id.md)struct [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) {

[ 1802](structbt__bap__base__codec__id.md#a9031aaf6a3f6e0acf68f1bfaed39b819) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__bap__base__codec__id.md#a9031aaf6a3f6e0acf68f1bfaed39b819);

[ 1804](structbt__bap__base__codec__id.md#a0aadd7e53f72efd8c0e33dd9a8eca177) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__bap__base__codec__id.md#a0aadd7e53f72efd8c0e33dd9a8eca177);

[ 1806](structbt__bap__base__codec__id.md#a49802819cc3129a993320b95472f2262) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__bap__base__codec__id.md#a49802819cc3129a993320b95472f2262);

1807};

1808

[ 1810](structbt__bap__base__subgroup__bis.md)struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) {

[ 1812](structbt__bap__base__subgroup__bis.md#ad0f5dff3150c36b1625f1f6f206d41d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structbt__bap__base__subgroup__bis.md#ad0f5dff3150c36b1625f1f6f206d41d2);

[ 1814](structbt__bap__base__subgroup__bis.md#ac4132c798c04c0f93c944dc91891221e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__bap__base__subgroup__bis.md#ac4132c798c04c0f93c944dc91891221e);

[ 1816](structbt__bap__base__subgroup__bis.md#aa53f22b29e447822e8bb36d9245bfc77) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__bap__base__subgroup__bis.md#aa53f22b29e447822e8bb36d9245bfc77);

1817};

1818

[ 1827](group__bt__bap__broadcast.md#ga29423a39d76ad16f0586d82a23c07ba7)const struct bt\_bap\_base \*[bt\_bap\_base\_get\_base\_from\_ad](group__bt__bap__broadcast.md#ga29423a39d76ad16f0586d82a23c07ba7)(const struct [bt\_data](structbt__data.md) \*ad);

1828

[ 1837](group__bt__bap__broadcast.md#ga539f92b71ec34f0551ef6240d83b972e)int [bt\_bap\_base\_get\_size](group__bt__bap__broadcast.md#ga539f92b71ec34f0551ef6240d83b972e)(const struct bt\_bap\_base \*base);

1838

[ 1847](group__bt__bap__broadcast.md#gaf91f45bcf7df2f368c5abeb116b65dd0)int [bt\_bap\_base\_get\_pres\_delay](group__bt__bap__broadcast.md#gaf91f45bcf7df2f368c5abeb116b65dd0)(const struct bt\_bap\_base \*base);

1848

[ 1857](group__bt__bap__broadcast.md#gadcae0230168564da1ee8b3c577ce27d7)int [bt\_bap\_base\_get\_subgroup\_count](group__bt__bap__broadcast.md#gadcae0230168564da1ee8b3c577ce27d7)(const struct bt\_bap\_base \*base);

1858

[ 1868](group__bt__bap__broadcast.md#ga6deab5a8b7a16ddf0c3685d4003694e1)int [bt\_bap\_base\_get\_bis\_indexes](group__bt__bap__broadcast.md#ga6deab5a8b7a16ddf0c3685d4003694e1)(const struct bt\_bap\_base \*base, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bis\_indexes);

1869

[ 1881](group__bt__bap__broadcast.md#ga5e6e0b758409cbdde93c0f648ef5e5e8)int [bt\_bap\_base\_foreach\_subgroup](group__bt__bap__broadcast.md#ga5e6e0b758409cbdde93c0f648ef5e5e8)(const struct bt\_bap\_base \*base,

1882 bool (\*func)(const struct bt\_bap\_base\_subgroup \*subgroup,

1883 void \*user\_data),

1884 void \*user\_data);

1885

[ 1895](group__bt__bap__broadcast.md#gae75e05a002dee8336eb066ae8231ea0c)int [bt\_bap\_base\_get\_subgroup\_codec\_id](group__bt__bap__broadcast.md#gae75e05a002dee8336eb066ae8231ea0c)(const struct bt\_bap\_base\_subgroup \*subgroup,

1896 struct [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) \*codec\_id);

1897

[ 1907](group__bt__bap__broadcast.md#ga10e2e32dc2802ba55d55c77148331f6a)int [bt\_bap\_base\_get\_subgroup\_codec\_data](group__bt__bap__broadcast.md#ga10e2e32dc2802ba55d55c77148331f6a)(const struct bt\_bap\_base\_subgroup \*subgroup,

1908 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1909

[ 1919](group__bt__bap__broadcast.md#gafb9d9544f38c7ad2613fff1679eb1f0c)int [bt\_bap\_base\_get\_subgroup\_codec\_meta](group__bt__bap__broadcast.md#gafb9d9544f38c7ad2613fff1679eb1f0c)(const struct bt\_bap\_base\_subgroup \*subgroup,

1920 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*meta);

1921

[ 1932](group__bt__bap__broadcast.md#ga920e3409f1978b803bcf6bc8d05ac8f6)int [bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg](group__bt__bap__broadcast.md#ga920e3409f1978b803bcf6bc8d05ac8f6)(const struct bt\_bap\_base\_subgroup \*subgroup,

1933 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1934

[ 1943](group__bt__bap__broadcast.md#ga051e1f8aa2faf3ba7a973356138fd2d3)int [bt\_bap\_base\_get\_subgroup\_bis\_count](group__bt__bap__broadcast.md#ga051e1f8aa2faf3ba7a973356138fd2d3)(const struct bt\_bap\_base\_subgroup \*subgroup);

1944

[ 1954](group__bt__bap__broadcast.md#ga37df3bf1e18d2d8e9388541217b2e366)int [bt\_bap\_base\_subgroup\_get\_bis\_indexes](group__bt__bap__broadcast.md#ga37df3bf1e18d2d8e9388541217b2e366)(const struct bt\_bap\_base\_subgroup \*subgroup,

1955 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bis\_indexes);

1956

[ 1968](group__bt__bap__broadcast.md#ga4f85ee43984cb2f3139b41da7b9b1aee)int [bt\_bap\_base\_subgroup\_foreach\_bis](group__bt__bap__broadcast.md#ga4f85ee43984cb2f3139b41da7b9b1aee)(const struct bt\_bap\_base\_subgroup \*subgroup,

1969 bool (\*func)(const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis,

1970 void \*user\_data),

1971 void \*user\_data);

1972

[ 1986](group__bt__bap__broadcast.md#gaa5cb191df7807ea87f1fba1871ca8ebe)int [bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg](group__bt__bap__broadcast.md#gaa5cb191df7807ea87f1fba1871ca8ebe)(const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis,

1987 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1988 /\* End of group bt\_bap\_broadcast \*/

1990

1997

[ 1999](structbt__bap__broadcast__source__stream__param.md)struct [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md) {

[ 2001](structbt__bap__broadcast__source__stream__param.md#a9c92fb50b62d963e01b1506b790fb5e1) struct [bt\_bap\_stream](structbt__bap__stream.md) \*[stream](structbt__bap__broadcast__source__stream__param.md#a9c92fb50b62d963e01b1506b790fb5e1);

2002

2003#if CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0 || defined(\_\_DOXYGEN\_\_)

[ 2009](structbt__bap__broadcast__source__stream__param.md#ac79a76ad748673ca4bd52c597cd073df) size\_t [data\_len](structbt__bap__broadcast__source__stream__param.md#ac79a76ad748673ca4bd52c597cd073df);

2010

[ 2012](structbt__bap__broadcast__source__stream__param.md#a5604297eafad95ae4e6a6c33a91b7e33) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__bap__broadcast__source__stream__param.md#a5604297eafad95ae4e6a6c33a91b7e33);

2013#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0 \*/

2014};

2015

[ 2017](structbt__bap__broadcast__source__subgroup__param.md)struct [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md) {

[ 2019](structbt__bap__broadcast__source__subgroup__param.md#a701d9480ffae2351149de6b962095d32) size\_t [params\_count](structbt__bap__broadcast__source__subgroup__param.md#a701d9480ffae2351149de6b962095d32);

2020

[ 2022](structbt__bap__broadcast__source__subgroup__param.md#a9719e89d8979f9502023e0032814c477) struct [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md) \*[params](structbt__bap__broadcast__source__subgroup__param.md#a9719e89d8979f9502023e0032814c477);

2023

[ 2025](structbt__bap__broadcast__source__subgroup__param.md#a1986239ea2ed5204d8f46a6500d5900d) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__bap__broadcast__source__subgroup__param.md#a1986239ea2ed5204d8f46a6500d5900d);

2026};

2027

[ 2029](structbt__bap__broadcast__source__param.md)struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) {

[ 2031](structbt__bap__broadcast__source__param.md#a5e155c3b92b4f9de3c9e6efa377097e3) size\_t [params\_count](structbt__bap__broadcast__source__param.md#a5e155c3b92b4f9de3c9e6efa377097e3);

2032

[ 2034](structbt__bap__broadcast__source__param.md#a6291842b49a55f6b2767dc95c9e874f3) struct [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md) \*[params](structbt__bap__broadcast__source__param.md#a6291842b49a55f6b2767dc95c9e874f3);

2035

[ 2037](structbt__bap__broadcast__source__param.md#ad62b77786a6996990d03d313331f2eb5) struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*[qos](structbt__bap__broadcast__source__param.md#ad62b77786a6996990d03d313331f2eb5);

2038

[ 2046](structbt__bap__broadcast__source__param.md#a493fa57a80e21a288854b2e3e1df775a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__bap__broadcast__source__param.md#a493fa57a80e21a288854b2e3e1df775a);

2047

[ 2049](structbt__bap__broadcast__source__param.md#a7552bf9a4ff5441b13669effe23abb8c) bool [encryption](structbt__bap__broadcast__source__param.md#a7552bf9a4ff5441b13669effe23abb8c);

2050

[ 2061](structbt__bap__broadcast__source__param.md#a6a05b6448f55cf5f52f90e44d83146dc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__bap__broadcast__source__param.md#a6a05b6448f55cf5f52f90e44d83146dc)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

2062

2063#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 2071](structbt__bap__broadcast__source__param.md#aab1799ab671500b02c1ab0e023ac43f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__bap__broadcast__source__param.md#aab1799ab671500b02c1ab0e023ac43f7);

2072

[ 2080](structbt__bap__broadcast__source__param.md#a50c29b5a2bcae162c0bbda32102a30cc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__bap__broadcast__source__param.md#a50c29b5a2bcae162c0bbda32102a30cc);

2081

[ 2089](structbt__bap__broadcast__source__param.md#a11b03e3d63ca2e116e743d9efde920be) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__bap__broadcast__source__param.md#a11b03e3d63ca2e116e743d9efde920be);

2090#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

2091};

2092

[ 2109](group__bt__bap__broadcast__source.md#gacdebfc435eebd47cf9cd05099a5f78e0)int [bt\_bap\_broadcast\_source\_create](group__bt__bap__broadcast__source.md#gacdebfc435eebd47cf9cd05099a5f78e0)(struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \*param,

2110 struct bt\_bap\_broadcast\_source \*\*source);

2111

[ 2131](group__bt__bap__broadcast__source.md#gabecaa9db7be5cb03ed997ba478878d40)int [bt\_bap\_broadcast\_source\_reconfig](group__bt__bap__broadcast__source.md#gabecaa9db7be5cb03ed997ba478878d40)(struct bt\_bap\_broadcast\_source \*source,

2132 struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \*param);

2133

[ 2146](group__bt__bap__broadcast__source.md#gaff2cfdadbff3ebe1e2efb660dee56f02)int [bt\_bap\_broadcast\_source\_update\_metadata](group__bt__bap__broadcast__source.md#gaff2cfdadbff3ebe1e2efb660dee56f02)(struct bt\_bap\_broadcast\_source \*source,

2147 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

2148

[ 2160](group__bt__bap__broadcast__source.md#gac4640f5207599d51c1a63ff47f3c1d5a)int [bt\_bap\_broadcast\_source\_start](group__bt__bap__broadcast__source.md#gac4640f5207599d51c1a63ff47f3c1d5a)(struct bt\_bap\_broadcast\_source \*source,

2161 struct bt\_le\_ext\_adv \*adv);

2162

[ 2173](group__bt__bap__broadcast__source.md#ga36a885581eec5cab8b3f652db19b9aba)int [bt\_bap\_broadcast\_source\_stop](group__bt__bap__broadcast__source.md#ga36a885581eec5cab8b3f652db19b9aba)(struct bt\_bap\_broadcast\_source \*source);

2174

[ 2185](group__bt__bap__broadcast__source.md#ga12e0a4856115a8eb297fe2d1fc130155)int [bt\_bap\_broadcast\_source\_delete](group__bt__bap__broadcast__source.md#ga12e0a4856115a8eb297fe2d1fc130155)(struct bt\_bap\_broadcast\_source \*source);

2186

[ 2201](group__bt__bap__broadcast__source.md#gafe07e4c6962858500fcf66415a173be8)int [bt\_bap\_broadcast\_source\_get\_base](group__bt__bap__broadcast__source.md#gafe07e4c6962858500fcf66415a173be8)(struct bt\_bap\_broadcast\_source \*source,

2202 struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf);

2203 /\* End of bt\_bap\_broadcast\_source \*/

2205

2212

[ 2214](structbt__bap__broadcast__sink__cb.md)struct [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) {

[ 2225](structbt__bap__broadcast__sink__cb.md#a1adf2124ec9a16c3c68774194febd0fc) void (\*[base\_recv](structbt__bap__broadcast__sink__cb.md#a1adf2124ec9a16c3c68774194febd0fc))(struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_bap\_base \*base,

2226 size\_t base\_size);

2227

[ 2240](structbt__bap__broadcast__sink__cb.md#a23390a63acbcf831a177a550d1012047) void (\*[syncable](structbt__bap__broadcast__sink__cb.md#a23390a63acbcf831a177a550d1012047))(struct bt\_bap\_broadcast\_sink \*sink, const struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) \*biginfo);

2241

2243 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

2244};

2245

[ 2258](group__bt__bap__broadcast__sink.md#ga1b83ead634d990e954f233d0208c5a85)int [bt\_bap\_broadcast\_sink\_register\_cb](group__bt__bap__broadcast__sink.md#ga1b83ead634d990e954f233d0208c5a85)(struct [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) \*cb);

2259

[ 2278](group__bt__bap__broadcast__sink.md#ga0637d1957db70ad39e0608ed07e75166)int [bt\_bap\_broadcast\_sink\_create](group__bt__bap__broadcast__sink.md#ga0637d1957db70ad39e0608ed07e75166)(struct bt\_le\_per\_adv\_sync \*pa\_sync, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) broadcast\_id,

2279 struct bt\_bap\_broadcast\_sink \*\*sink);

2280

[ 2300](group__bt__bap__broadcast__sink.md#gacadebb5ce8aab5f5b8f1ff7e0fa57805)int [bt\_bap\_broadcast\_sink\_sync](group__bt__bap__broadcast__sink.md#gacadebb5ce8aab5f5b8f1ff7e0fa57805)(struct bt\_bap\_broadcast\_sink \*sink, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) indexes\_bitfield,

2301 struct [bt\_bap\_stream](structbt__bap__stream.md) \*streams[],

2302 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)]);

2303

[ 2314](group__bt__bap__broadcast__sink.md#ga1020b21bfb4195aeb5823197145b1fe9)int [bt\_bap\_broadcast\_sink\_stop](group__bt__bap__broadcast__sink.md#ga1020b21bfb4195aeb5823197145b1fe9)(struct bt\_bap\_broadcast\_sink \*sink);

2315

[ 2327](group__bt__bap__broadcast__sink.md#ga8b9d6cb409a3671654e053475ada3fda)int [bt\_bap\_broadcast\_sink\_delete](group__bt__bap__broadcast__sink.md#ga8b9d6cb409a3671654e053475ada3fda)(struct bt\_bap\_broadcast\_sink \*sink);

2328 /\* End of group bt\_bap\_broadcast\_sink \*/

2330

[ 2344](group__bt__bap.md#ga7632ab444dbf99387871f7d0c90b11ba)int [bt\_bap\_scan\_delegator\_register](group__bt__bap.md#ga7632ab444dbf99387871f7d0c90b11ba)(struct [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md) \*cb);

2345

[ 2354](group__bt__bap.md#ga6f52e58767303ded16cb6289f094895a)int [bt\_bap\_scan\_delegator\_unregister](group__bt__bap.md#ga6f52e58767303ded16cb6289f094895a)(void);

2355

[ 2369](group__bt__bap.md#ga381c1f3b386ecbdfd570eb125882161e)int [bt\_bap\_scan\_delegator\_set\_pa\_state](group__bt__bap.md#ga381c1f3b386ecbdfd570eb125882161e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id,

2370 enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) pa\_state);

2371

[ 2380](group__bt__bap.md#ga7cce7e53264294abec4421364afffdbe)int [bt\_bap\_scan\_delegator\_set\_bis\_sync\_state](group__bt__bap.md#ga7cce7e53264294abec4421364afffdbe)(

2381 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id,

2382 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bis\_synced[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]);

2383

[ 2385](structbt__bap__scan__delegator__add__src__param.md)struct [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) {

[ 2387](structbt__bap__scan__delegator__add__src__param.md#a751106648b8f040747b5ffb804932798) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__bap__scan__delegator__add__src__param.md#a751106648b8f040747b5ffb804932798);

2388

[ 2390](structbt__bap__scan__delegator__add__src__param.md#a80817dd3bc046d76baabd62e470ad797) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__bap__scan__delegator__add__src__param.md#a80817dd3bc046d76baabd62e470ad797);

2391

[ 2393](structbt__bap__scan__delegator__add__src__param.md#a502d263982995c99559714f07d74443f) enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) [encrypt\_state](structbt__bap__scan__delegator__add__src__param.md#a502d263982995c99559714f07d74443f);

2394

[ 2396](structbt__bap__scan__delegator__add__src__param.md#a8e8eda4139e460800c6195b4c5f246e2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__bap__scan__delegator__add__src__param.md#a8e8eda4139e460800c6195b4c5f246e2);

2397

[ 2399](structbt__bap__scan__delegator__add__src__param.md#a12bed26ffdc9d4683a5fcdf512a194eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__scan__delegator__add__src__param.md#a12bed26ffdc9d4683a5fcdf512a194eb);

2400

[ 2402](structbt__bap__scan__delegator__add__src__param.md#a9153dbdef5b507ef14e73a188cb00ae1) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) [subgroups](structbt__bap__scan__delegator__add__src__param.md#a9153dbdef5b507ef14e73a188cb00ae1)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS];

2403};

2404

[ 2418](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0)int [bt\_bap\_scan\_delegator\_add\_src](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0)(const struct [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) \*param);

2419

[ 2421](structbt__bap__scan__delegator__mod__src__param.md)struct [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) {

[ 2423](structbt__bap__scan__delegator__mod__src__param.md#ae387a2c0613545ae3acd372780f738bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__bap__scan__delegator__mod__src__param.md#ae387a2c0613545ae3acd372780f738bb);

2424

[ 2426](structbt__bap__scan__delegator__mod__src__param.md#aecc8b74632dcb2b17b9a358e00c75d31) enum [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) [encrypt\_state](structbt__bap__scan__delegator__mod__src__param.md#aecc8b74632dcb2b17b9a358e00c75d31);

2427

[ 2429](structbt__bap__scan__delegator__mod__src__param.md#a11b4c6d787bd2c828e565282daf5cf2f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__bap__scan__delegator__mod__src__param.md#a11b4c6d787bd2c828e565282daf5cf2f);

2430

[ 2432](structbt__bap__scan__delegator__mod__src__param.md#aa8dcd7983005ffd23779db6b6ccfb752) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__scan__delegator__mod__src__param.md#aa8dcd7983005ffd23779db6b6ccfb752);

2433

[ 2440](structbt__bap__scan__delegator__mod__src__param.md#a14ffee52751dd152b1a8cc0822d1702f) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) [subgroups](structbt__bap__scan__delegator__mod__src__param.md#a14ffee52751dd152b1a8cc0822d1702f)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS];

2441};

2442

[ 2456](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a)int [bt\_bap\_scan\_delegator\_mod\_src](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a)(const struct [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) \*param);

2457

[ 2471](group__bt__bap.md#ga6c240f1cdb33945197700e4fe106ef2c)int [bt\_bap\_scan\_delegator\_rem\_src](group__bt__bap.md#ga6c240f1cdb33945197700e4fe106ef2c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id);

2472

[ 2483](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824))(

2484 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, void \*user\_data);

2485

[ 2492](group__bt__bap.md#gab6f1a12699a9437c6575c70df33d5be0)void [bt\_bap\_scan\_delegator\_foreach\_state](group__bt__bap.md#gab6f1a12699a9437c6575c70df33d5be0)([bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824) func,

2493 void \*user\_data);

2494

[ 2503](group__bt__bap.md#gabec9fd0a2966e1811fd4770855050510)const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*[bt\_bap\_scan\_delegator\_find\_state](group__bt__bap.md#gabec9fd0a2966e1811fd4770855050510)(

2504 [bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824) func, void \*user\_data);

2505

2506/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* CLIENT API \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

2507

[ 2514](group__bt__bap.md#ga496c8a2f599d997a7e6e033bda5f0c36)typedef void (\*[bt\_bap\_broadcast\_assistant\_write\_cb](group__bt__bap.md#ga496c8a2f599d997a7e6e033bda5f0c36))(struct bt\_conn \*conn,

2515 int err);

2516

[ 2522](structbt__bap__broadcast__assistant__cb.md)struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) {

[ 2532](structbt__bap__broadcast__assistant__cb.md#a01ad0a89db9041670f6a68d6f1680988) void (\*[discover](structbt__bap__broadcast__assistant__cb.md#a01ad0a89db9041670f6a68d6f1680988))(struct bt\_conn \*conn, int err,

2533 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_state\_count);

2534

[ 2544](structbt__bap__broadcast__assistant__cb.md#ab88d98b1e742ccd36aac69069ebf3f61) void (\*[scan](structbt__bap__broadcast__assistant__cb.md#ab88d98b1e742ccd36aac69069ebf3f61))(const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info,

2545 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) broadcast\_id);

2546

[ 2556](structbt__bap__broadcast__assistant__cb.md#a629ff4299b8ae5bcbddf28338caddfd0) void (\*[recv\_state](structbt__bap__broadcast__assistant__cb.md#a629ff4299b8ae5bcbddf28338caddfd0))(struct bt\_conn \*conn, int err,

2557 const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

2558

[ 2565](structbt__bap__broadcast__assistant__cb.md#af3fb53d95cdc7ba202657e4c54e0b2b8) void (\*[recv\_state\_removed](structbt__bap__broadcast__assistant__cb.md#af3fb53d95cdc7ba202657e4c54e0b2b8))(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id);

2566

[ 2573](structbt__bap__broadcast__assistant__cb.md#ad2bdfcc0147a751910d82232a77e34f8) void (\*[scan\_start](structbt__bap__broadcast__assistant__cb.md#ad2bdfcc0147a751910d82232a77e34f8))(struct bt\_conn \*conn, int err);

2574

[ 2581](structbt__bap__broadcast__assistant__cb.md#a80296a38e664aabff7ec27e007c59e95) void (\*[scan\_stop](structbt__bap__broadcast__assistant__cb.md#a80296a38e664aabff7ec27e007c59e95))(struct bt\_conn \*conn, int err);

2582

[ 2589](structbt__bap__broadcast__assistant__cb.md#ad909b9e6e3c35be10a29ee5a4b7213fb) void (\*[add\_src](structbt__bap__broadcast__assistant__cb.md#ad909b9e6e3c35be10a29ee5a4b7213fb))(struct bt\_conn \*conn, int err);

2590

[ 2597](structbt__bap__broadcast__assistant__cb.md#ab24e3ecb9764ca833524b787126b8c2c) void (\*[mod\_src](structbt__bap__broadcast__assistant__cb.md#ab24e3ecb9764ca833524b787126b8c2c))(struct bt\_conn \*conn, int err);

2598

[ 2605](structbt__bap__broadcast__assistant__cb.md#a09de9cb86dad76b485ff52257a0c68dc) void (\*[broadcast\_code](structbt__bap__broadcast__assistant__cb.md#a09de9cb86dad76b485ff52257a0c68dc))(struct bt\_conn \*conn, int err);

2606

[ 2613](structbt__bap__broadcast__assistant__cb.md#af0cf259088cd793152390b21813a9481) void (\*[rem\_src](structbt__bap__broadcast__assistant__cb.md#af0cf259088cd793152390b21813a9481))(struct bt\_conn \*conn, int err);

2614

2616 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

2617};

2618

[ 2634](group__bt__bap.md#gab59c5ebc4fef28da34d8a54b1244c33b)int [bt\_bap\_broadcast\_assistant\_discover](group__bt__bap.md#gab59c5ebc4fef28da34d8a54b1244c33b)(struct bt\_conn \*conn);

2635

[ 2660](group__bt__bap.md#ga98ac067e66d263aa41fc6f8df6bb9126)int [bt\_bap\_broadcast\_assistant\_scan\_start](group__bt__bap.md#ga98ac067e66d263aa41fc6f8df6bb9126)(struct bt\_conn \*conn,

2661 bool start\_scan);

2662

[ 2676](group__bt__bap.md#ga76cae35df980b78a10551811050b2760)int [bt\_bap\_broadcast\_assistant\_scan\_stop](group__bt__bap.md#ga76cae35df980b78a10551811050b2760)(struct bt\_conn \*conn);

2677

[ 2687](group__bt__bap.md#gabab24c44e9833029965475ad7b149e6e)int [bt\_bap\_broadcast\_assistant\_register\_cb](group__bt__bap.md#gabab24c44e9833029965475ad7b149e6e)(struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \*cb);

2688

[ 2698](group__bt__bap.md#ga679cdeb6e555bfc9ce20f38e493000ee)int [bt\_bap\_broadcast\_assistant\_unregister\_cb](group__bt__bap.md#ga679cdeb6e555bfc9ce20f38e493000ee)(struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \*cb);

2699

2700

[ 2702](structbt__bap__broadcast__assistant__add__src__param.md)struct [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) {

[ 2704](structbt__bap__broadcast__assistant__add__src__param.md#a2b04d75ca9a740a7d819eae1bcc5cba7) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__bap__broadcast__assistant__add__src__param.md#a2b04d75ca9a740a7d819eae1bcc5cba7);

2705

[ 2707](structbt__bap__broadcast__assistant__add__src__param.md#a390cd8d887cd256ee74b39b9b516cac4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__bap__broadcast__assistant__add__src__param.md#a390cd8d887cd256ee74b39b9b516cac4);

2708

[ 2710](structbt__bap__broadcast__assistant__add__src__param.md#ad9af814e8a232230d4ee97c459f47747) bool [pa\_sync](structbt__bap__broadcast__assistant__add__src__param.md#ad9af814e8a232230d4ee97c459f47747);

2711

[ 2713](structbt__bap__broadcast__assistant__add__src__param.md#ae50b6b5a3f2c92f01e7070c605b37dde) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__bap__broadcast__assistant__add__src__param.md#ae50b6b5a3f2c92f01e7070c605b37dde);

2714

[ 2720](structbt__bap__broadcast__assistant__add__src__param.md#acaecbbf7b3c96fe5ca53f90e92fa1e5e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pa\_interval](structbt__bap__broadcast__assistant__add__src__param.md#acaecbbf7b3c96fe5ca53f90e92fa1e5e);

2721

[ 2723](structbt__bap__broadcast__assistant__add__src__param.md#a17b67d65b6840c3d4480027b7deb31a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__broadcast__assistant__add__src__param.md#a17b67d65b6840c3d4480027b7deb31a5);

2724

[ 2730](structbt__bap__broadcast__assistant__add__src__param.md#ab8423e5cce4a6c9ac142221d2e816763) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) \*[subgroups](structbt__bap__broadcast__assistant__add__src__param.md#ab8423e5cce4a6c9ac142221d2e816763);

2731};

2732

[ 2746](group__bt__bap.md#gac93cb4cab33d0b937e752bc0b71cad9e)int [bt\_bap\_broadcast\_assistant\_add\_src](group__bt__bap.md#gac93cb4cab33d0b937e752bc0b71cad9e)(

2747 struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) \*param);

2748

[ 2750](structbt__bap__broadcast__assistant__mod__src__param.md)struct [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) {

[ 2752](structbt__bap__broadcast__assistant__mod__src__param.md#a5bc7c0a491872d655296bbb979402a62) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__bap__broadcast__assistant__mod__src__param.md#a5bc7c0a491872d655296bbb979402a62);

2753

[ 2755](structbt__bap__broadcast__assistant__mod__src__param.md#a794bb68c8a73edfe3d44dbe9a0bf2830) bool [pa\_sync](structbt__bap__broadcast__assistant__mod__src__param.md#a794bb68c8a73edfe3d44dbe9a0bf2830);

2756

[ 2762](structbt__bap__broadcast__assistant__mod__src__param.md#aebaa104384dcbec7bb952a27f3acc24d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pa\_interval](structbt__bap__broadcast__assistant__mod__src__param.md#aebaa104384dcbec7bb952a27f3acc24d);

2763

[ 2765](structbt__bap__broadcast__assistant__mod__src__param.md#a42b12c6d9f5c622433c9c1f0c72726c1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subgroups](structbt__bap__broadcast__assistant__mod__src__param.md#a42b12c6d9f5c622433c9c1f0c72726c1);

2766

[ 2768](structbt__bap__broadcast__assistant__mod__src__param.md#a2383ec98b14054e0bc66bb4a0ae7b8b6) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) \*[subgroups](structbt__bap__broadcast__assistant__mod__src__param.md#a2383ec98b14054e0bc66bb4a0ae7b8b6);

2769};

2770

[ 2784](group__bt__bap.md#gaa9c292a7dcb470926d8d7d4be699a0c7)int [bt\_bap\_broadcast\_assistant\_mod\_src](group__bt__bap.md#gaa9c292a7dcb470926d8d7d4be699a0c7)(

2785 struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) \*param);

2786

[ 2801](group__bt__bap.md#gabcec07689c13a996bcb9d2d417347dbb)int [bt\_bap\_broadcast\_assistant\_set\_broadcast\_code](group__bt__bap.md#gabcec07689c13a996bcb9d2d417347dbb)(

2802 struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id,

2803 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)]);

2804

[ 2818](group__bt__bap.md#ga09785690db551677a043fcaa2fdb7f29)int [bt\_bap\_broadcast\_assistant\_rem\_src](group__bt__bap.md#ga09785690db551677a043fcaa2fdb7f29)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id);

2819

[ 2834](group__bt__bap.md#ga94fce2b4346b1026d53e0b860ca7fbf2)int [bt\_bap\_broadcast\_assistant\_read\_recv\_state](group__bt__bap.md#ga94fce2b4346b1026d53e0b860ca7fbf2)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx);

2835 /\* end of bt\_bap \*/

2837

2838#ifdef \_\_cplusplus

2839}

2840#endif

2841

2842#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)

bt\_audio\_dir

Audio direction from the perspective of the BAP Unicast Server / BAP Broadcast Sink.

**Definition** audio.h:796

[bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)

bt\_audio\_location

Location values for BT Audio.

**Definition** audio.h:590

[bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)

bt\_audio\_metadata\_type

Codec metadata type IDs.

**Definition** audio.h:432

[bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)

bt\_audio\_context

Audio Context Type for Generic Audio.

**Definition** audio.h:303

[bt\_bap\_broadcast\_sink\_create](group__bt__bap__broadcast__sink.md#ga0637d1957db70ad39e0608ed07e75166)

int bt\_bap\_broadcast\_sink\_create(struct bt\_le\_per\_adv\_sync \*pa\_sync, uint32\_t broadcast\_id, struct bt\_bap\_broadcast\_sink \*\*sink)

Create a Broadcast Sink from a periodic advertising sync.

[bt\_bap\_broadcast\_sink\_stop](group__bt__bap__broadcast__sink.md#ga1020b21bfb4195aeb5823197145b1fe9)

int bt\_bap\_broadcast\_sink\_stop(struct bt\_bap\_broadcast\_sink \*sink)

Stop audio broadcast sink.

[bt\_bap\_broadcast\_sink\_register\_cb](group__bt__bap__broadcast__sink.md#ga1b83ead634d990e954f233d0208c5a85)

int bt\_bap\_broadcast\_sink\_register\_cb(struct bt\_bap\_broadcast\_sink\_cb \*cb)

Register Broadcast sink callbacks.

[bt\_bap\_broadcast\_sink\_delete](group__bt__bap__broadcast__sink.md#ga8b9d6cb409a3671654e053475ada3fda)

int bt\_bap\_broadcast\_sink\_delete(struct bt\_bap\_broadcast\_sink \*sink)

Release a broadcast sink.

[bt\_bap\_broadcast\_sink\_sync](group__bt__bap__broadcast__sink.md#gacadebb5ce8aab5f5b8f1ff7e0fa57805)

int bt\_bap\_broadcast\_sink\_sync(struct bt\_bap\_broadcast\_sink \*sink, uint32\_t indexes\_bitfield, struct bt\_bap\_stream \*streams[], const uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE])

Sync to a broadcaster's audio.

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

[bt\_bap\_base\_subgroup\_get\_bis\_indexes](group__bt__bap__broadcast.md#ga37df3bf1e18d2d8e9388541217b2e366)

int bt\_bap\_base\_subgroup\_get\_bis\_indexes(const struct bt\_bap\_base\_subgroup \*subgroup, uint32\_t \*bis\_indexes)

Get all BIS indexes of a subgroup.

[bt\_bap\_base\_subgroup\_foreach\_bis](group__bt__bap__broadcast.md#ga4f85ee43984cb2f3139b41da7b9b1aee)

int bt\_bap\_base\_subgroup\_foreach\_bis(const struct bt\_bap\_base\_subgroup \*subgroup, bool(\*func)(const struct bt\_bap\_base\_subgroup\_bis \*bis, void \*user\_data), void \*user\_data)

Iterate on all BIS in the subgroup.

[bt\_bap\_base\_get\_size](group__bt__bap__broadcast.md#ga539f92b71ec34f0551ef6240d83b972e)

int bt\_bap\_base\_get\_size(const struct bt\_bap\_base \*base)

Get the size of a BASE.

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

Create unicast group.

[bt\_bap\_unicast\_group\_reconfig](group__bt__bap__unicast__client.md#gacd684504c8127ff4f8d038cc06718e5e)

int bt\_bap\_unicast\_group\_reconfig(struct bt\_bap\_unicast\_group \*unicast\_group, const struct bt\_bap\_unicast\_group\_param \*param)

Reconfigure unicast group.

[bt\_bap\_unicast\_client\_discover](group__bt__bap__unicast__client.md#gacef9c88f66762e8de19303d20dafa0bb)

int bt\_bap\_unicast\_client\_discover(struct bt\_conn \*conn, enum bt\_audio\_dir dir)

Discover remote capabilities and endpoints.

[bt\_bap\_unicast\_client\_register\_cb](group__bt__bap__unicast__client.md#gade70f04ae1a828b43b3b44fa8933f674)

int bt\_bap\_unicast\_client\_register\_cb(struct bt\_bap\_unicast\_client\_cb \*cb)

Register unicast client callbacks.

[bt\_bap\_unicast\_server\_foreach\_ep](group__bt__bap__unicast__server.md#ga4614a504d47cf732b09d4f22302d3239)

void bt\_bap\_unicast\_server\_foreach\_ep(struct bt\_conn \*conn, bt\_bap\_ep\_func\_t func, void \*user\_data)

Iterate through all endpoints of the given connection.

[bt\_bap\_unicast\_server\_config\_ase](group__bt__bap__unicast__server.md#ga6e71c34a21091f222d3478f4fad95319)

int bt\_bap\_unicast\_server\_config\_ase(struct bt\_conn \*conn, struct bt\_bap\_stream \*stream, struct bt\_audio\_codec\_cfg \*codec\_cfg, const struct bt\_bap\_qos\_cfg\_pref \*qos\_pref)

Initialize and configure a new ASE.

[bt\_bap\_unicast\_server\_unregister](group__bt__bap__unicast__server.md#ga6ef3b9e877ffdc04cc48fda6713a0209)

int bt\_bap\_unicast\_server\_unregister(void)

Unregister the Unicast Server.

[bt\_bap\_unicast\_server\_register\_cb](group__bt__bap__unicast__server.md#ga7669133936bc13f7ab38817db9ce69c0)

int bt\_bap\_unicast\_server\_register\_cb(const struct bt\_bap\_unicast\_server\_cb \*cb)

Register unicast server callbacks.

[bt\_bap\_unicast\_server\_register](group__bt__bap__unicast__server.md#gab3ea6014854e6290f058c87e866c3191)

int bt\_bap\_unicast\_server\_register(const struct bt\_bap\_unicast\_server\_register\_param \*param)

Register the Unicast Server.

[bt\_bap\_ep\_func\_t](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1)

void(\* bt\_bap\_ep\_func\_t)(struct bt\_bap\_ep \*ep, void \*user\_data)

The callback function called for each endpoint.

**Definition** bap.h:1397

[bt\_bap\_unicast\_server\_unregister\_cb](group__bt__bap__unicast__server.md#gadf984f12bdeadcfc814dc2fc770cb7bf)

int bt\_bap\_unicast\_server\_unregister\_cb(const struct bt\_bap\_unicast\_server\_cb \*cb)

Unregister unicast server callbacks.

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

**Definition** bap.h:347

[bt\_bap\_stream\_config](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402)

int bt\_bap\_stream\_config(struct bt\_conn \*conn, struct bt\_bap\_stream \*stream, struct bt\_bap\_ep \*ep, struct bt\_audio\_codec\_cfg \*codec\_cfg)

Configure Audio Stream.

[bt\_bap\_qos\_cfg\_framing](group__bt__bap.md#ga37a5f9d7198739eef8bde6764da30de9)

bt\_bap\_qos\_cfg\_framing

QoS Framing.

**Definition** bap.h:84

[bt\_bap\_scan\_delegator\_set\_pa\_state](group__bt__bap.md#ga381c1f3b386ecbdfd570eb125882161e)

int bt\_bap\_scan\_delegator\_set\_pa\_state(uint8\_t src\_id, enum bt\_bap\_pa\_state pa\_state)

Set the periodic advertising sync state to syncing.

[bt\_bap\_stream\_get\_tx\_sync](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928)

int bt\_bap\_stream\_get\_tx\_sync(struct bt\_bap\_stream \*stream, struct bt\_iso\_tx\_info \*info)

Get ISO transmission timing info for a Basic Audio Profile stream.

[bt\_bap\_broadcast\_assistant\_write\_cb](group__bt__bap.md#ga496c8a2f599d997a7e6e033bda5f0c36)

void(\* bt\_bap\_broadcast\_assistant\_write\_cb)(struct bt\_conn \*conn, int err)

Callback function for writes.

**Definition** bap.h:2514

[bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22)

bt\_bap\_big\_enc\_state

Broadcast Isochronous Group encryption state reported by the Scan Delegator.

**Definition** bap.h:332

[bt\_bap\_stream\_send](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e)

int bt\_bap\_stream\_send(struct bt\_bap\_stream \*stream, struct net\_buf \*buf, uint16\_t seq\_num)

Send data to Audio stream without timestamp.

[bt\_bap\_broadcast\_assistant\_unregister\_cb](group__bt__bap.md#ga679cdeb6e555bfc9ce20f38e493000ee)

int bt\_bap\_broadcast\_assistant\_unregister\_cb(struct bt\_bap\_broadcast\_assistant\_cb \*cb)

Unregisters the callbacks used by the Broadcast Audio Scan Service client.

[bt\_bap\_scan\_delegator\_rem\_src](group__bt__bap.md#ga6c240f1cdb33945197700e4fe106ef2c)

int bt\_bap\_scan\_delegator\_rem\_src(uint8\_t src\_id)

Remove a receive state source.

[bt\_bap\_scan\_delegator\_add\_src](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0)

int bt\_bap\_scan\_delegator\_add\_src(const struct bt\_bap\_scan\_delegator\_add\_src\_param \*param)

Add a receive state source locally.

[bt\_bap\_scan\_delegator\_unregister](group__bt__bap.md#ga6f52e58767303ded16cb6289f094895a)

int bt\_bap\_scan\_delegator\_unregister(void)

unregister the Basic Audio Profile Scan Delegator and BASS.

[bt\_bap\_scan\_delegator\_register](group__bt__bap.md#ga7632ab444dbf99387871f7d0c90b11ba)

int bt\_bap\_scan\_delegator\_register(struct bt\_bap\_scan\_delegator\_cb \*cb)

Register the Basic Audio Profile Scan Delegator and BASS.

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

**Definition** bap.h:438

[bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1)

bt\_bap\_ascs\_rsp\_code

Response Status Code.

**Definition** bap.h:398

[bt\_bap\_stream\_send\_ts](group__bt__bap.md#gaa0e012446238c916abc84d6c0de89bf3)

int bt\_bap\_stream\_send\_ts(struct bt\_bap\_stream \*stream, struct net\_buf \*buf, uint16\_t seq\_num, uint32\_t ts)

Send data to Audio stream with timestamp.

[bt\_bap\_stream\_connect](group__bt__bap.md#gaa75f2cd2c36fdaef04a62c95bec6e2e3)

int bt\_bap\_stream\_connect(struct bt\_bap\_stream \*stream)

Connect unicast audio stream.

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

[bt\_bap\_broadcast\_assistant\_register\_cb](group__bt__bap.md#gabab24c44e9833029965475ad7b149e6e)

int bt\_bap\_broadcast\_assistant\_register\_cb(struct bt\_bap\_broadcast\_assistant\_cb \*cb)

Registers the callbacks used by Broadcast Audio Scan Service client.

[bt\_bap\_broadcast\_assistant\_set\_broadcast\_code](group__bt__bap.md#gabcec07689c13a996bcb9d2d417347dbb)

int bt\_bap\_broadcast\_assistant\_set\_broadcast\_code(struct bt\_conn \*conn, uint8\_t src\_id, const uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE])

Set a broadcast code to the specified receive state.

[bt\_bap\_scan\_delegator\_find\_state](group__bt__bap.md#gabec9fd0a2966e1811fd4770855050510)

const struct bt\_bap\_scan\_delegator\_recv\_state \* bt\_bap\_scan\_delegator\_find\_state(bt\_bap\_scan\_delegator\_state\_func\_t func, void \*user\_data)

Find and return a receive state based on a compare function.

[bt\_bap\_scan\_delegator\_mod\_src](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a)

int bt\_bap\_scan\_delegator\_mod\_src(const struct bt\_bap\_scan\_delegator\_mod\_src\_param \*param)

Add a receive state source locally.

[bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296)

bt\_bap\_pa\_state

Periodic advertising state reported by the Scan Delegator.

**Definition** bap.h:314

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

**Definition** bap.h:369

[bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824)

bool(\* bt\_bap\_scan\_delegator\_state\_func\_t)(const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state, void \*user\_data)

Callback function for Scan Delegator receive state search functions.

**Definition** bap.h:2483

[BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c)

@ BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED

Opcode not supported.

**Definition** bap.h:349

[BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202)

@ BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID

Invalid source ID supplied.

**Definition** bap.h:352

[BT\_BAP\_QOS\_CFG\_FRAMING\_FRAMED](group__bt__bap.md#gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298)

@ BT\_BAP\_QOS\_CFG\_FRAMING\_FRAMED

Packets are always framed.

**Definition** bap.h:88

[BT\_BAP\_QOS\_CFG\_FRAMING\_UNFRAMED](group__bt__bap.md#gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94)

@ BT\_BAP\_QOS\_CFG\_FRAMING\_UNFRAMED

Packets may be framed or unframed.

**Definition** bap.h:86

[BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2)

@ BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ

The Broadcast Isochronous Group broadcast code requested.

**Definition** bap.h:337

[BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4)

@ BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC

The Broadcast Isochronous Group not encrypted.

**Definition** bap.h:334

[BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b)

@ BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE

The Broadcast Isochronous Group bad broadcast code.

**Definition** bap.h:343

[BT\_BAP\_BIG\_ENC\_STATE\_DEC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10)

@ BT\_BAP\_BIG\_ENC\_STATE\_DEC

The Broadcast Isochronous Group decrypted.

**Definition** bap.h:340

[BT\_BAP\_QOS\_CFG\_CODED](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73)

@ BT\_BAP\_QOS\_CFG\_CODED

LE Coded PHY.

**Definition** bap.h:98

[BT\_BAP\_QOS\_CFG\_2M](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147)

@ BT\_BAP\_QOS\_CFG\_2M

LE 2M PHY.

**Definition** bap.h:96

[BT\_BAP\_QOS\_CFG\_1M](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28)

@ BT\_BAP\_QOS\_CFG\_1M

LE 1M PHY.

**Definition** bap.h:94

[BT\_BAP\_ASCS\_REASON\_NONE](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd)

@ BT\_BAP\_ASCS\_REASON\_NONE

No reason.

**Definition** bap.h:440

[BT\_BAP\_ASCS\_REASON\_PD](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557)

@ BT\_BAP\_ASCS\_REASON\_PD

Presendation delay.

**Definition** bap.h:458

[BT\_BAP\_ASCS\_REASON\_FRAMING](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539)

@ BT\_BAP\_ASCS\_REASON\_FRAMING

Framing.

**Definition** bap.h:448

[BT\_BAP\_ASCS\_REASON\_CODEC\_DATA](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0)

@ BT\_BAP\_ASCS\_REASON\_CODEC\_DATA

Codec configuration.

**Definition** bap.h:444

[BT\_BAP\_ASCS\_REASON\_SDU](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b)

@ BT\_BAP\_ASCS\_REASON\_SDU

Maximum SDU size.

**Definition** bap.h:452

[BT\_BAP\_ASCS\_REASON\_CODEC](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea)

@ BT\_BAP\_ASCS\_REASON\_CODEC

Codec ID.

**Definition** bap.h:442

[BT\_BAP\_ASCS\_REASON\_PHY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8)

@ BT\_BAP\_ASCS\_REASON\_PHY

PHY.

**Definition** bap.h:450

[BT\_BAP\_ASCS\_REASON\_LATENCY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942)

@ BT\_BAP\_ASCS\_REASON\_LATENCY

Max transport latency.

**Definition** bap.h:456

[BT\_BAP\_ASCS\_REASON\_CIS](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c)

@ BT\_BAP\_ASCS\_REASON\_CIS

Invalid CIS mapping.

**Definition** bap.h:460

[BT\_BAP\_ASCS\_REASON\_RTN](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf)

@ BT\_BAP\_ASCS\_REASON\_RTN

RTN.

**Definition** bap.h:454

[BT\_BAP\_ASCS\_REASON\_INTERVAL](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c)

@ BT\_BAP\_ASCS\_REASON\_INTERVAL

SDU interval.

**Definition** bap.h:446

[BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5)

@ BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE

Invalid ASE state.

**Definition** bap.h:408

[BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06)

@ BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID

Invalid metadata.

**Definition** bap.h:424

[BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d)

@ BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED

Server did not support operation by client.

**Definition** bap.h:402

[BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62)

@ BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED

Configuration parameters not supported by server.

**Definition** bap.h:414

[BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa)

@ BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE

Invalid ASE ID.

**Definition** bap.h:406

[BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146)

@ BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR

Invalid operation for direction.

**Definition** bap.h:410

[BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219)

@ BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID

Invalid Configuration parameters.

**Definition** bap.h:418

[BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a)

@ BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED

Capabilities not supported by server.

**Definition** bap.h:412

[BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb)

@ BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM

Server has insufficient resources.

**Definition** bap.h:426

[BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06)

@ BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED

Metadata rejected by server.

**Definition** bap.h:422

[BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a)

@ BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED

Unspecified error.

**Definition** bap.h:428

[BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9)

@ BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH

Server rejected due to invalid operation length.

**Definition** bap.h:404

[BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7)

@ BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED

Unsupported metadata.

**Definition** bap.h:420

[BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd)

@ BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS

Server completed operation successfully.

**Definition** bap.h:400

[BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21)

@ BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED

Configuration parameters rejected by server.

**Definition** bap.h:416

[BT\_BAP\_PA\_STATE\_NOT\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf)

@ BT\_BAP\_PA\_STATE\_NOT\_SYNCED

The periodic advertising has not been synchronized.

**Definition** bap.h:316

[BT\_BAP\_PA\_STATE\_FAILED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647)

@ BT\_BAP\_PA\_STATE\_FAILED

Failed to synchronized to periodic advertising.

**Definition** bap.h:325

[BT\_BAP\_PA\_STATE\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc)

@ BT\_BAP\_PA\_STATE\_SYNCED

Synchronized to periodic advertising.

**Definition** bap.h:322

[BT\_BAP\_PA\_STATE\_INFO\_REQ](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb)

@ BT\_BAP\_PA\_STATE\_INFO\_REQ

Waiting for SyncInfo from Broadcast Assistant.

**Definition** bap.h:319

[BT\_BAP\_PA\_STATE\_NO\_PAST](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d)

@ BT\_BAP\_PA\_STATE\_NO\_PAST

No periodic advertising sync transfer receiver from Broadcast Assistant.

**Definition** bap.h:328

[BT\_BAP\_EP\_STATE\_ENABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332)

@ BT\_BAP\_EP\_STATE\_ENABLING

Audio Stream Endpoint Enabling state.

**Definition** bap.h:380

[BT\_BAP\_EP\_STATE\_IDLE](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961)

@ BT\_BAP\_EP\_STATE\_IDLE

Audio Stream Endpoint Idle state.

**Definition** bap.h:371

[BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688)

@ BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED

Audio Stream Endpoint Codec Configured state.

**Definition** bap.h:374

[BT\_BAP\_EP\_STATE\_RELEASING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c)

@ BT\_BAP\_EP\_STATE\_RELEASING

Audio Stream Endpoint Streaming state.

**Definition** bap.h:389

[BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523)

@ BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED

Audio Stream Endpoint QoS Configured state.

**Definition** bap.h:377

[BT\_BAP\_EP\_STATE\_DISABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8)

@ BT\_BAP\_EP\_STATE\_DISABLING

Audio Stream Endpoint Disabling state.

**Definition** bap.h:386

[BT\_BAP\_EP\_STATE\_STREAMING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710)

@ BT\_BAP\_EP\_STATE\_STREAMING

Audio Stream Endpoint Streaming state.

**Definition** bap.h:383

[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)

#define BT\_ISO\_BROADCAST\_CODE\_SIZE

Broadcast code size.

**Definition** iso.h:129

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[iso.h](iso_8h.md)

Bluetooth ISO handling.

[net\_buf.h](net__buf_8h.md)

Buffer management.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

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

**Definition** audio.h:684

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:718

[bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md)

Structure storing values of fields of ASE Control Point notification.

**Definition** bap.h:464

[bt\_bap\_ascs\_rsp::reason](structbt__bap__ascs__rsp.md#a138532bc40f60547c56d8b108ad44d1e)

enum bt\_bap\_ascs\_reason reason

Response reason.

**Definition** bap.h:501

[bt\_bap\_ascs\_rsp::metadata\_type](structbt__bap__ascs__rsp.md#a736f44864015244a8b48a859eff6b902)

enum bt\_audio\_metadata\_type metadata\_type

Response metadata type.

**Definition** bap.h:511

[bt\_bap\_ascs\_rsp::code](structbt__bap__ascs__rsp.md#a8ea364298f7e3e784b7878215db63d91)

enum bt\_bap\_ascs\_rsp\_code code

Value of the Response Code field.

**Definition** bap.h:478

[bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md)

Codec ID structure for a Broadcast Audio Source Endpoint (BASE).

**Definition** bap.h:1800

[bt\_bap\_base\_codec\_id::cid](structbt__bap__base__codec__id.md#a0aadd7e53f72efd8c0e33dd9a8eca177)

uint16\_t cid

Codec Company ID.

**Definition** bap.h:1804

[bt\_bap\_base\_codec\_id::vid](structbt__bap__base__codec__id.md#a49802819cc3129a993320b95472f2262)

uint16\_t vid

Codec Company Vendor ID.

**Definition** bap.h:1806

[bt\_bap\_base\_codec\_id::id](structbt__bap__base__codec__id.md#a9031aaf6a3f6e0acf68f1bfaed39b819)

uint8\_t id

Codec ID.

**Definition** bap.h:1802

[bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md)

BIS structure for each BIS in a Broadcast Audio Source Endpoint (BASE) subgroup.

**Definition** bap.h:1810

[bt\_bap\_base\_subgroup\_bis::data](structbt__bap__base__subgroup__bis.md#aa53f22b29e447822e8bb36d9245bfc77)

uint8\_t \* data

Codec Specific Data.

**Definition** bap.h:1816

[bt\_bap\_base\_subgroup\_bis::data\_len](structbt__bap__base__subgroup__bis.md#ac4132c798c04c0f93c944dc91891221e)

uint8\_t data\_len

Codec Specific Data length.

**Definition** bap.h:1814

[bt\_bap\_base\_subgroup\_bis::index](structbt__bap__base__subgroup__bis.md#ad0f5dff3150c36b1625f1f6f206d41d2)

uint8\_t index

Unique index of the BIS.

**Definition** bap.h:1812

[bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md)

Struct to hold subgroup specific information for the receive state.

**Definition** bap.h:537

[bt\_bap\_bass\_subgroup::metadata](structbt__bap__bass__subgroup.md#a851fda16d0856714ebf4d3970c4d2e4b)

uint8\_t metadata[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE]

The metadata.

**Definition** bap.h:546

[bt\_bap\_bass\_subgroup::bis\_sync](structbt__bap__bass__subgroup.md#ac8061995eb73ba30e335e37714396ff5)

uint32\_t bis\_sync

BIS synced bitfield.

**Definition** bap.h:539

[bt\_bap\_bass\_subgroup::metadata\_len](structbt__bap__bass__subgroup.md#ace1c1ff5d2f5cc79838653d468166664)

uint8\_t metadata\_len

Length of the metadata.

**Definition** bap.h:542

[bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md)

Parameters for adding a source to a Broadcast Audio Scan Service server.

**Definition** bap.h:2702

[bt\_bap\_broadcast\_assistant\_add\_src\_param::num\_subgroups](structbt__bap__broadcast__assistant__add__src__param.md#a17b67d65b6840c3d4480027b7deb31a5)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:2723

[bt\_bap\_broadcast\_assistant\_add\_src\_param::addr](structbt__bap__broadcast__assistant__add__src__param.md#a2b04d75ca9a740a7d819eae1bcc5cba7)

bt\_addr\_le\_t addr

Address of the advertiser.

**Definition** bap.h:2704

[bt\_bap\_broadcast\_assistant\_add\_src\_param::adv\_sid](structbt__bap__broadcast__assistant__add__src__param.md#a390cd8d887cd256ee74b39b9b516cac4)

uint8\_t adv\_sid

SID of the advertising set.

**Definition** bap.h:2707

[bt\_bap\_broadcast\_assistant\_add\_src\_param::subgroups](structbt__bap__broadcast__assistant__add__src__param.md#ab8423e5cce4a6c9ac142221d2e816763)

struct bt\_bap\_bass\_subgroup \* subgroups

Pointer to array of subgroups.

**Definition** bap.h:2730

[bt\_bap\_broadcast\_assistant\_add\_src\_param::pa\_interval](structbt__bap__broadcast__assistant__add__src__param.md#acaecbbf7b3c96fe5ca53f90e92fa1e5e)

uint16\_t pa\_interval

Periodic advertising interval in milliseconds.

**Definition** bap.h:2720

[bt\_bap\_broadcast\_assistant\_add\_src\_param::pa\_sync](structbt__bap__broadcast__assistant__add__src__param.md#ad9af814e8a232230d4ee97c459f47747)

bool pa\_sync

Whether to sync to periodic advertisements.

**Definition** bap.h:2710

[bt\_bap\_broadcast\_assistant\_add\_src\_param::broadcast\_id](structbt__bap__broadcast__assistant__add__src__param.md#ae50b6b5a3f2c92f01e7070c605b37dde)

uint32\_t broadcast\_id

24-bit broadcast ID

**Definition** bap.h:2713

[bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md)

Struct to hold the Basic Audio Profile Broadcast Assistant callbacks.

**Definition** bap.h:2522

[bt\_bap\_broadcast\_assistant\_cb::discover](structbt__bap__broadcast__assistant__cb.md#a01ad0a89db9041670f6a68d6f1680988)

void(\* discover)(struct bt\_conn \*conn, int err, uint8\_t recv\_state\_count)

Callback function for bt\_bap\_broadcast\_assistant\_discover.

**Definition** bap.h:2532

[bt\_bap\_broadcast\_assistant\_cb::broadcast\_code](structbt__bap__broadcast__assistant__cb.md#a09de9cb86dad76b485ff52257a0c68dc)

void(\* broadcast\_code)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_set\_broadcast\_code().

**Definition** bap.h:2605

[bt\_bap\_broadcast\_assistant\_cb::recv\_state](structbt__bap__broadcast__assistant__cb.md#a629ff4299b8ae5bcbddf28338caddfd0)

void(\* recv\_state)(struct bt\_conn \*conn, int err, const struct bt\_bap\_scan\_delegator\_recv\_state \*state)

Callback function for when a receive state is read or updated.

**Definition** bap.h:2556

[bt\_bap\_broadcast\_assistant\_cb::scan\_stop](structbt__bap__broadcast__assistant__cb.md#a80296a38e664aabff7ec27e007c59e95)

void(\* scan\_stop)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_scan\_stop().

**Definition** bap.h:2581

[bt\_bap\_broadcast\_assistant\_cb::mod\_src](structbt__bap__broadcast__assistant__cb.md#ab24e3ecb9764ca833524b787126b8c2c)

void(\* mod\_src)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_mod\_src().

**Definition** bap.h:2597

[bt\_bap\_broadcast\_assistant\_cb::scan](structbt__bap__broadcast__assistant__cb.md#ab88d98b1e742ccd36aac69069ebf3f61)

void(\* scan)(const struct bt\_le\_scan\_recv\_info \*info, uint32\_t broadcast\_id)

Callback function for Broadcast Audio Scan Service client scan results.

**Definition** bap.h:2544

[bt\_bap\_broadcast\_assistant\_cb::scan\_start](structbt__bap__broadcast__assistant__cb.md#ad2bdfcc0147a751910d82232a77e34f8)

void(\* scan\_start)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_scan\_start().

**Definition** bap.h:2573

[bt\_bap\_broadcast\_assistant\_cb::add\_src](structbt__bap__broadcast__assistant__cb.md#ad909b9e6e3c35be10a29ee5a4b7213fb)

void(\* add\_src)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_add\_src().

**Definition** bap.h:2589

[bt\_bap\_broadcast\_assistant\_cb::rem\_src](structbt__bap__broadcast__assistant__cb.md#af0cf259088cd793152390b21813a9481)

void(\* rem\_src)(struct bt\_conn \*conn, int err)

Callback function for bt\_bap\_broadcast\_assistant\_rem\_src().

**Definition** bap.h:2613

[bt\_bap\_broadcast\_assistant\_cb::recv\_state\_removed](structbt__bap__broadcast__assistant__cb.md#af3fb53d95cdc7ba202657e4c54e0b2b8)

void(\* recv\_state\_removed)(struct bt\_conn \*conn, uint8\_t src\_id)

Callback function for when a receive state is removed.

**Definition** bap.h:2565

[bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md)

Parameters for modifying a source.

**Definition** bap.h:2750

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::subgroups](structbt__bap__broadcast__assistant__mod__src__param.md#a2383ec98b14054e0bc66bb4a0ae7b8b6)

struct bt\_bap\_bass\_subgroup \* subgroups

Pointer to array of subgroups.

**Definition** bap.h:2768

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::num\_subgroups](structbt__bap__broadcast__assistant__mod__src__param.md#a42b12c6d9f5c622433c9c1f0c72726c1)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:2765

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::src\_id](structbt__bap__broadcast__assistant__mod__src__param.md#a5bc7c0a491872d655296bbb979402a62)

uint8\_t src\_id

Source ID of the receive state.

**Definition** bap.h:2752

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::pa\_sync](structbt__bap__broadcast__assistant__mod__src__param.md#a794bb68c8a73edfe3d44dbe9a0bf2830)

bool pa\_sync

Whether to sync to periodic advertisements.

**Definition** bap.h:2755

[bt\_bap\_broadcast\_assistant\_mod\_src\_param::pa\_interval](structbt__bap__broadcast__assistant__mod__src__param.md#aebaa104384dcbec7bb952a27f3acc24d)

uint16\_t pa\_interval

Periodic advertising interval.

**Definition** bap.h:2762

[bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md)

Broadcast Audio Sink callback structure.

**Definition** bap.h:2214

[bt\_bap\_broadcast\_sink\_cb::base\_recv](structbt__bap__broadcast__sink__cb.md#a1adf2124ec9a16c3c68774194febd0fc)

void(\* base\_recv)(struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_bap\_base \*base, size\_t base\_size)

Broadcast Audio Source Endpoint (BASE) received.

**Definition** bap.h:2225

[bt\_bap\_broadcast\_sink\_cb::syncable](structbt__bap__broadcast__sink__cb.md#a23390a63acbcf831a177a550d1012047)

void(\* syncable)(struct bt\_bap\_broadcast\_sink \*sink, const struct bt\_iso\_biginfo \*biginfo)

Broadcast sink is syncable.

**Definition** bap.h:2240

[bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md)

Broadcast Source create parameters.

**Definition** bap.h:2029

[bt\_bap\_broadcast\_source\_param::iso\_interval](structbt__bap__broadcast__source__param.md#a11b03e3d63ca2e116e743d9efde920be)

uint16\_t iso\_interval

ISO interval.

**Definition** bap.h:2089

[bt\_bap\_broadcast\_source\_param::packing](structbt__bap__broadcast__source__param.md#a493fa57a80e21a288854b2e3e1df775a)

uint8\_t packing

Broadcast Source packing mode.

**Definition** bap.h:2046

[bt\_bap\_broadcast\_source\_param::pto](structbt__bap__broadcast__source__param.md#a50c29b5a2bcae162c0bbda32102a30cc)

uint8\_t pto

Pre-transmission offset.

**Definition** bap.h:2080

[bt\_bap\_broadcast\_source\_param::params\_count](structbt__bap__broadcast__source__param.md#a5e155c3b92b4f9de3c9e6efa377097e3)

size\_t params\_count

The number of parameters in subgroup\_params.

**Definition** bap.h:2031

[bt\_bap\_broadcast\_source\_param::params](structbt__bap__broadcast__source__param.md#a6291842b49a55f6b2767dc95c9e874f3)

struct bt\_bap\_broadcast\_source\_subgroup\_param \* params

Array of stream parameters.

**Definition** bap.h:2034

[bt\_bap\_broadcast\_source\_param::broadcast\_code](structbt__bap__broadcast__source__param.md#a6a05b6448f55cf5f52f90e44d83146dc)

uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]

Broadcast code.

**Definition** bap.h:2061

[bt\_bap\_broadcast\_source\_param::encryption](structbt__bap__broadcast__source__param.md#a7552bf9a4ff5441b13669effe23abb8c)

bool encryption

Whether or not to encrypt the streams.

**Definition** bap.h:2049

[bt\_bap\_broadcast\_source\_param::irc](structbt__bap__broadcast__source__param.md#aab1799ab671500b02c1ab0e023ac43f7)

uint8\_t irc

Immediate Repetition Count.

**Definition** bap.h:2071

[bt\_bap\_broadcast\_source\_param::qos](structbt__bap__broadcast__source__param.md#ad62b77786a6996990d03d313331f2eb5)

struct bt\_bap\_qos\_cfg \* qos

Quality of Service configuration.

**Definition** bap.h:2037

[bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md)

Broadcast Source stream parameters.

**Definition** bap.h:1999

[bt\_bap\_broadcast\_source\_stream\_param::data](structbt__bap__broadcast__source__stream__param.md#a5604297eafad95ae4e6a6c33a91b7e33)

uint8\_t \* data

BIS Codec Specific Configuration.

**Definition** bap.h:2012

[bt\_bap\_broadcast\_source\_stream\_param::stream](structbt__bap__broadcast__source__stream__param.md#a9c92fb50b62d963e01b1506b790fb5e1)

struct bt\_bap\_stream \* stream

Audio stream.

**Definition** bap.h:2001

[bt\_bap\_broadcast\_source\_stream\_param::data\_len](structbt__bap__broadcast__source__stream__param.md#ac79a76ad748673ca4bd52c597cd073df)

size\_t data\_len

The number of elements in the data array.

**Definition** bap.h:2009

[bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md)

Broadcast Source subgroup parameters.

**Definition** bap.h:2017

[bt\_bap\_broadcast\_source\_subgroup\_param::codec\_cfg](structbt__bap__broadcast__source__subgroup__param.md#a1986239ea2ed5204d8f46a6500d5900d)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Subgroup Codec configuration.

**Definition** bap.h:2025

[bt\_bap\_broadcast\_source\_subgroup\_param::params\_count](structbt__bap__broadcast__source__subgroup__param.md#a701d9480ffae2351149de6b962095d32)

size\_t params\_count

The number of parameters in stream\_params.

**Definition** bap.h:2019

[bt\_bap\_broadcast\_source\_subgroup\_param::params](structbt__bap__broadcast__source__subgroup__param.md#a9719e89d8979f9502023e0032814c477)

struct bt\_bap\_broadcast\_source\_stream\_param \* params

Array of stream parameters.

**Definition** bap.h:2022

[bt\_bap\_ep\_info](structbt__bap__ep__info.md)

Structure holding information of audio stream endpoint.

**Definition** bap.h:693

[bt\_bap\_ep\_info::id](structbt__bap__ep__info.md#a07e8878e7e6a8ee059639330ffa78c1c)

uint8\_t id

The ID of the endpoint.

**Definition** bap.h:695

[bt\_bap\_ep\_info::can\_recv](structbt__bap__ep__info.md#a30698c71f556ca876a1c69bffefac653)

bool can\_recv

True if the stream associated with the endpoint is able to receive data.

**Definition** bap.h:710

[bt\_bap\_ep\_info::iso\_chan](structbt__bap__ep__info.md#a54dd673e21455c85193df844f3aa4083)

struct bt\_iso\_chan \* iso\_chan

The isochronous channel associated with the endpoint.

**Definition** bap.h:704

[bt\_bap\_ep\_info::state](structbt__bap__ep__info.md#a650727747d0a093528544c3e16255feb)

enum bt\_bap\_ep\_state state

The state of the endpoint.

**Definition** bap.h:698

[bt\_bap\_ep\_info::paired\_ep](structbt__bap__ep__info.md#a819ac77dcf7cb6985e97f290a666ed09)

struct bt\_bap\_ep \* paired\_ep

Pointer to paired endpoint if the endpoint is part of a bidirectional CIS, otherwise NULL.

**Definition** bap.h:715

[bt\_bap\_ep\_info::dir](structbt__bap__ep__info.md#abb0dc6d25744cd734f8fd6ba2bc84b24)

enum bt\_audio\_dir dir

Capabilities type.

**Definition** bap.h:701

[bt\_bap\_ep\_info::can\_send](structbt__bap__ep__info.md#abbad124bf9e40ed530b2a33fefbadc84)

bool can\_send

True if the stream associated with the endpoint is able to send data.

**Definition** bap.h:707

[bt\_bap\_ep\_info::qos\_pref](structbt__bap__ep__info.md#ad5201e9b9623e8ff8e74e1be87ece864)

const struct bt\_bap\_qos\_cfg\_pref \* qos\_pref

Pointer to the preferred QoS settings associated with the endpoint.

**Definition** bap.h:718

[bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md)

Audio Stream Quality of Service Preference structure.

**Definition** bap.h:246

[bt\_bap\_qos\_cfg\_pref::pref\_pd\_min](structbt__bap__qos__cfg__pref.md#a1df8cd4ed27e9099b8b2a069855010aa)

uint32\_t pref\_pd\_min

Preferred minimum Presentation Delay in microseconds.

**Definition** bap.h:301

[bt\_bap\_qos\_cfg\_pref::rtn](structbt__bap__qos__cfg__pref.md#a286bfb02d35ca148f263f1fa1ca9e061)

uint8\_t rtn

Preferred Retransmission Number.

**Definition** bap.h:268

[bt\_bap\_qos\_cfg\_pref::unframed\_supported](structbt__bap__qos__cfg__pref.md#a2a2de382f04a50d26d174dcc7c7a12c1)

bool unframed\_supported

Unframed PDUs supported.

**Definition** bap.h:253

[bt\_bap\_qos\_cfg\_pref::pd\_min](structbt__bap__qos__cfg__pref.md#a3f643768de9d8b0a7a62e403703e0033)

uint32\_t pd\_min

Minimum Presentation Delay in microseconds.

**Definition** bap.h:284

[bt\_bap\_qos\_cfg\_pref::pd\_max](structbt__bap__qos__cfg__pref.md#a666be60856b5b4688d21d7a36b956c29)

uint32\_t pd\_max

Maximum Presentation Delay in microseconds.

**Definition** bap.h:293

[bt\_bap\_qos\_cfg\_pref::phy](structbt__bap__qos__cfg__pref.md#a697a67e623d758b76be342a125a369a6)

uint8\_t phy

Preferred PHY bitfield.

**Definition** bap.h:261

[bt\_bap\_qos\_cfg\_pref::pref\_pd\_max](structbt__bap__qos__cfg__pref.md#ab6475a80b33a9cea69edeaa3093c9070)

uint32\_t pref\_pd\_max

Preferred maximum Presentation Delay in microseconds.

**Definition** bap.h:310

[bt\_bap\_qos\_cfg\_pref::latency](structbt__bap__qos__cfg__pref.md#ac5871b4f58be038eeda483e8d07b9b53)

uint16\_t latency

Preferred Transport Latency.

**Definition** bap.h:275

[bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md)

QoS configuration structure.

**Definition** bap.h:128

[bt\_bap\_qos\_cfg::sdu](structbt__bap__qos__cfg.md#a294709496f7779ee4cb7aa542da8832b)

uint16\_t sdu

Maximum SDU size.

**Definition** bap.h:173

[bt\_bap\_qos\_cfg::burst\_number](structbt__bap__qos__cfg.md#a597b81261511ec820caa66bd091ab896)

uint8\_t burst\_number

Burst number.

**Definition** bap.h:211

[bt\_bap\_qos\_cfg::framing](structbt__bap__qos__cfg.md#a60057a7812cdc5b26f839e68dc4603c4)

enum bt\_bap\_qos\_cfg\_framing framing

QoS Framing.

**Definition** bap.h:150

[bt\_bap\_qos\_cfg::latency](structbt__bap__qos__cfg.md#a912ee316aa2ddb00ebab7bb78af0f34a)

uint16\_t latency

Maximum Transport Latency.

**Definition** bap.h:182

[bt\_bap\_qos\_cfg::num\_subevents](structbt__bap__qos__cfg.md#a97094ac8254ff3e97790943a5c71cdf3)

uint8\_t num\_subevents

Number of subevents.

**Definition** bap.h:220

[bt\_bap\_qos\_cfg::rtn](structbt__bap__qos__cfg.md#aaaa4a88499cfd1f90e409fa98891bf2c)

uint8\_t rtn

Retransmission Number.

**Definition** bap.h:166

[bt\_bap\_qos\_cfg::interval](structbt__bap__qos__cfg.md#abf8a1b76cc0735b9aec1962d2ce574ec)

uint32\_t interval

SDU Interval.

**Definition** bap.h:190

[bt\_bap\_qos\_cfg::phy](structbt__bap__qos__cfg.md#ac50ea51e1645546d8f8faa58c64672ce)

uint8\_t phy

PHY.

**Definition** bap.h:158

[bt\_bap\_qos\_cfg::max\_pdu](structbt__bap__qos__cfg.md#acb84f2da73e865e38dcefa92007f01e1)

uint16\_t max\_pdu

Maximum PDU size.

**Definition** bap.h:204

[bt\_bap\_qos\_cfg::pd](structbt__bap__qos__cfg.md#addf190fac00b2fb99c0d1abf13eb20b3)

uint32\_t pd

Presentation Delay in microseconds.

**Definition** bap.h:139

[bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md)

Parameters for bt\_bap\_scan\_delegator\_add\_src().

**Definition** bap.h:2385

[bt\_bap\_scan\_delegator\_add\_src\_param::num\_subgroups](structbt__bap__scan__delegator__add__src__param.md#a12bed26ffdc9d4683a5fcdf512a194eb)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:2399

[bt\_bap\_scan\_delegator\_add\_src\_param::encrypt\_state](structbt__bap__scan__delegator__add__src__param.md#a502d263982995c99559714f07d74443f)

enum bt\_bap\_big\_enc\_state encrypt\_state

The broadcast isochronous group encryption state.

**Definition** bap.h:2393

[bt\_bap\_scan\_delegator\_add\_src\_param::addr](structbt__bap__scan__delegator__add__src__param.md#a751106648b8f040747b5ffb804932798)

bt\_addr\_le\_t addr

Periodic Advertiser Address.

**Definition** bap.h:2387

[bt\_bap\_scan\_delegator\_add\_src\_param::sid](structbt__bap__scan__delegator__add__src__param.md#a80817dd3bc046d76baabd62e470ad797)

uint8\_t sid

Advertiser SID.

**Definition** bap.h:2390

[bt\_bap\_scan\_delegator\_add\_src\_param::broadcast\_id](structbt__bap__scan__delegator__add__src__param.md#a8e8eda4139e460800c6195b4c5f246e2)

uint32\_t broadcast\_id

The 24-bit broadcast ID.

**Definition** bap.h:2396

[bt\_bap\_scan\_delegator\_add\_src\_param::subgroups](structbt__bap__scan__delegator__add__src__param.md#a9153dbdef5b507ef14e73a188cb00ae1)

struct bt\_bap\_bass\_subgroup subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]

Subgroup specific information.

**Definition** bap.h:2402

[bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md)

Struct to hold the Basic Audio Profile Scan Delegator callbacks.

**Definition** bap.h:593

[bt\_bap\_scan\_delegator\_cb::pa\_sync\_req](structbt__bap__scan__delegator__cb.md#a0ea55963f92361f35e68eadcf10306b1)

int(\* pa\_sync\_req)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state, bool past\_avail, uint16\_t pa\_interval)

Periodic advertising sync request.

**Definition** bap.h:622

[bt\_bap\_scan\_delegator\_cb::pa\_sync\_term\_req](structbt__bap__scan__delegator__cb.md#a5b918538cfe0edaa69155f891981eeae)

int(\* pa\_sync\_term\_req)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state)

Periodic advertising sync termination request.

**Definition** bap.h:639

[bt\_bap\_scan\_delegator\_cb::recv\_state\_updated](structbt__bap__scan__delegator__cb.md#a5d95631d95ae1085071c9b795eca1a8e)

void(\* recv\_state\_updated)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state)

Receive state updated.

**Definition** bap.h:603

[bt\_bap\_scan\_delegator\_cb::broadcast\_code](structbt__bap__scan__delegator__cb.md#a78d011c817e60725a0ef14c68bd655cd)

void(\* broadcast\_code)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state, const uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE])

Broadcast code received.

**Definition** bap.h:653

[bt\_bap\_scan\_delegator\_cb::bis\_sync\_req](structbt__bap__scan__delegator__cb.md#a959112080deec0ab2dcc2c09a6958874)

int(\* bis\_sync\_req)(struct bt\_conn \*conn, const struct bt\_bap\_scan\_delegator\_recv\_state \*recv\_state, const uint32\_t bis\_sync\_req[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS])

Broadcast Isochronous Stream synchronize request.

**Definition** bap.h:677

[bt\_bap\_scan\_delegator\_cb::scanning\_state](structbt__bap__scan__delegator__cb.md#ae41d499d75123a1b70b778e8e95edcc3)

void(\* scanning\_state)(struct bt\_conn \*conn, bool is\_scanning)

Broadcast Assistant scanning state callback.

**Definition** bap.h:689

[bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md)

Parameters for bt\_bap\_scan\_delegator\_mod\_src().

**Definition** bap.h:2421

[bt\_bap\_scan\_delegator\_mod\_src\_param::broadcast\_id](structbt__bap__scan__delegator__mod__src__param.md#a11b4c6d787bd2c828e565282daf5cf2f)

uint32\_t broadcast\_id

The 24-bit broadcast ID.

**Definition** bap.h:2429

[bt\_bap\_scan\_delegator\_mod\_src\_param::subgroups](structbt__bap__scan__delegator__mod__src__param.md#a14ffee52751dd152b1a8cc0822d1702f)

struct bt\_bap\_bass\_subgroup subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]

Subgroup specific information.

**Definition** bap.h:2440

[bt\_bap\_scan\_delegator\_mod\_src\_param::num\_subgroups](structbt__bap__scan__delegator__mod__src__param.md#aa8dcd7983005ffd23779db6b6ccfb752)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:2432

[bt\_bap\_scan\_delegator\_mod\_src\_param::src\_id](structbt__bap__scan__delegator__mod__src__param.md#ae387a2c0613545ae3acd372780f738bb)

uint8\_t src\_id

The periodic adverting sync.

**Definition** bap.h:2423

[bt\_bap\_scan\_delegator\_mod\_src\_param::encrypt\_state](structbt__bap__scan__delegator__mod__src__param.md#aecc8b74632dcb2b17b9a358e00c75d31)

enum bt\_bap\_big\_enc\_state encrypt\_state

The broadcast isochronous group encryption state.

**Definition** bap.h:2426

[bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md)

Represents the Broadcast Audio Scan Service receive state.

**Definition** bap.h:551

[bt\_bap\_scan\_delegator\_recv\_state::src\_id](structbt__bap__scan__delegator__recv__state.md#a1755a6332c86aeaf624d3c540037772a)

uint8\_t src\_id

The source ID.

**Definition** bap.h:553

[bt\_bap\_scan\_delegator\_recv\_state::bad\_code](structbt__bap__scan__delegator__recv__state.md#a1c268bb7b340c874935f186c0ba2a253)

uint8\_t bad\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]

The bad broadcast code.

**Definition** bap.h:575

[bt\_bap\_scan\_delegator\_recv\_state::pa\_sync\_state](structbt__bap__scan__delegator__recv__state.md#a30fbad06780fd7bca9aacdf14ecaf4a0)

enum bt\_bap\_pa\_state pa\_sync\_state

The periodic adverting sync state.

**Definition** bap.h:562

[bt\_bap\_scan\_delegator\_recv\_state::addr](structbt__bap__scan__delegator__recv__state.md#a6153ea6bbfe7057c39f6b652a4e6e34e)

bt\_addr\_le\_t addr

The Bluetooth address.

**Definition** bap.h:556

[bt\_bap\_scan\_delegator\_recv\_state::adv\_sid](structbt__bap__scan__delegator__recv__state.md#aa03e02a1832950e4a53ff2fe803c14a6)

uint8\_t adv\_sid

The advertising set ID.

**Definition** bap.h:559

[bt\_bap\_scan\_delegator\_recv\_state::num\_subgroups](structbt__bap__scan__delegator__recv__state.md#aa97765bdbaa43a280645eb62c0035b82)

uint8\_t num\_subgroups

Number of subgroups.

**Definition** bap.h:578

[bt\_bap\_scan\_delegator\_recv\_state::broadcast\_id](structbt__bap__scan__delegator__recv__state.md#abaa80f30cf2e84ee873d18eaedd4159d)

uint32\_t broadcast\_id

The 24-bit broadcast ID.

**Definition** bap.h:568

[bt\_bap\_scan\_delegator\_recv\_state::encrypt\_state](structbt__bap__scan__delegator__recv__state.md#ac770a5ad001f73d3acaf2b36827f9343)

enum bt\_bap\_big\_enc\_state encrypt\_state

The broadcast isochronous group encryption state.

**Definition** bap.h:565

[bt\_bap\_scan\_delegator\_recv\_state::subgroups](structbt__bap__scan__delegator__recv__state.md#ae674ccfdc1905f230b0f7a58cc553274)

struct bt\_bap\_bass\_subgroup subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]

Subgroup specific information.

**Definition** bap.h:585

[bt\_bap\_stream\_ops](structbt__bap__stream__ops.md)

Stream operation.

**Definition** bap.h:781

[bt\_bap\_stream\_ops::recv](structbt__bap__stream__ops.md#a09f31dc30de9c880758ec4a1468e59f0)

void(\* recv)(struct bt\_bap\_stream \*stream, const struct bt\_iso\_recv\_info \*info, struct net\_buf \*buf)

Stream audio HCI receive callback.

**Definition** bap.h:874

[bt\_bap\_stream\_ops::enabled](structbt__bap__stream__ops.md#a1c67137b439a87647994530710d9e075)

void(\* enabled)(struct bt\_bap\_stream \*stream)

Stream enabled callback.

**Definition** bap.h:810

[bt\_bap\_stream\_ops::sent](structbt__bap__stream__ops.md#a33b07c51394dea6d632f42aec89a1510)

void(\* sent)(struct bt\_bap\_stream \*stream)

Stream audio HCI sent callback.

**Definition** bap.h:891

[bt\_bap\_stream\_ops::released](structbt__bap__stream__ops.md#a37876562731d7dbbcd5f5613621b78ca)

void(\* released)(struct bt\_bap\_stream \*stream)

Stream released callback.

**Definition** bap.h:839

[bt\_bap\_stream\_ops::disabled](structbt__bap__stream__ops.md#a3fc784b8a2a7c1a5b19dece3619c130e)

void(\* disabled)(struct bt\_bap\_stream \*stream)

Stream disabled callback.

**Definition** bap.h:829

[bt\_bap\_stream\_ops::configured](structbt__bap__stream__ops.md#a509a400c622d1684e6ab0d47bc6300ba)

void(\* configured)(struct bt\_bap\_stream \*stream, const struct bt\_bap\_qos\_cfg\_pref \*pref)

Stream configured callback.

**Definition** bap.h:791

[bt\_bap\_stream\_ops::connected](structbt__bap__stream__ops.md#a533d5ea96aa67b9b74b19c55afd43df1)

void(\* connected)(struct bt\_bap\_stream \*stream)

Isochronous channel connected callback.

**Definition** bap.h:906

[bt\_bap\_stream\_ops::metadata\_updated](structbt__bap__stream__ops.md#a553777c6b6bdda3e0e8c03f3915404cd)

void(\* metadata\_updated)(struct bt\_bap\_stream \*stream)

Stream metadata updated callback.

**Definition** bap.h:820

[bt\_bap\_stream\_ops::started](structbt__bap__stream__ops.md#a7f595e37d40b94510bf09c1f82b479f3)

void(\* started)(struct bt\_bap\_stream \*stream)

Stream started callback.

**Definition** bap.h:850

[bt\_bap\_stream\_ops::disconnected](structbt__bap__stream__ops.md#a953c7174297f1a27ceed012dced53c5a)

void(\* disconnected)(struct bt\_bap\_stream \*stream, uint8\_t reason)

Isochronous channel disconnected callback.

**Definition** bap.h:920

[bt\_bap\_stream\_ops::stopped](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5)

void(\* stopped)(struct bt\_bap\_stream \*stream, uint8\_t reason)

Stream stopped callback.

**Definition** bap.h:860

[bt\_bap\_stream\_ops::qos\_set](structbt__bap__stream__ops.md#add541b683a0042bde13749b327b897dd)

void(\* qos\_set)(struct bt\_bap\_stream \*stream)

Stream QoS set callback.

**Definition** bap.h:801

[bt\_bap\_stream](structbt__bap__stream.md)

Basic Audio Profile stream structure.

**Definition** bap.h:740

[bt\_bap\_stream::group](structbt__bap__stream.md#a17d91a06d581cd4341d035eb76d8e0b2)

void \* group

**Definition** bap.h:766

[bt\_bap\_stream::codec\_cfg](structbt__bap__stream.md#a2abf6e4d8cbbdbb6e2ccd705581484ed)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Codec Configuration.

**Definition** bap.h:748

[bt\_bap\_stream::qos](structbt__bap__stream.md#a41cfe6496de63d05f86bcab90b9fbbf2)

struct bt\_bap\_qos\_cfg \* qos

QoS Configuration.

**Definition** bap.h:751

[bt\_bap\_stream::ops](structbt__bap__stream.md#a46a1f70c1a1fe4696039be14adf3c9b6)

struct bt\_bap\_stream\_ops \* ops

Audio stream operations.

**Definition** bap.h:754

[bt\_bap\_stream::conn](structbt__bap__stream.md#adb95fe7a0b981a46898382ee45fd99df)

struct bt\_conn \* conn

Connection reference.

**Definition** bap.h:742

[bt\_bap\_stream::bap\_iso](structbt__bap__stream.md#af5fdb04fdeb394a0345ece23331445e5)

struct bt\_bap\_iso \* bap\_iso

**Definition** bap.h:762

[bt\_bap\_stream::ep](structbt__bap__stream.md#af871d28b2cca8e4deba66997badbeca2)

struct bt\_bap\_ep \* ep

Endpoint reference.

**Definition** bap.h:745

[bt\_bap\_stream::user\_data](structbt__bap__stream.md#afe81620dd215aebe04ddc9e36dc7d2dd)

void \* user\_data

Stream user data.

**Definition** bap.h:769

[bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md)

Unicast Client callback structure.

**Definition** bap.h:1572

[bt\_bap\_unicast\_client\_cb::enable](structbt__bap__unicast__client__cb.md#a15dd1277b37dcd96a545bb6d450c2f9d)

void(\* enable)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_enable().

**Definition** bap.h:1639

[bt\_bap\_unicast\_client\_cb::discover](structbt__bap__unicast__client__cb.md#a1f2f7476506b6b798c1f26371217956e)

void(\* discover)(struct bt\_conn \*conn, int err, enum bt\_audio\_dir dir)

BAP discovery callback function.

**Definition** bap.h:1753

[bt\_bap\_unicast\_client\_cb::qos](structbt__bap__unicast__client__cb.md#a23b82e9f4174bcc2130d6f4570990180)

void(\* qos)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_qos().

**Definition** bap.h:1626

[bt\_bap\_unicast\_client\_cb::pac\_record](structbt__bap__unicast__client__cb.md#a3c55f4e23607b1e655b5f520d691bf33)

void(\* pac\_record)(struct bt\_conn \*conn, enum bt\_audio\_dir dir, const struct bt\_audio\_codec\_cap \*codec\_cap)

Remote Published Audio Capability (PAC) record discovered.

**Definition** bap.h:1725

[bt\_bap\_unicast\_client\_cb::disable](structbt__bap__unicast__client__cb.md#a47f86af7675fcf6ac86fad578437afa9)

void(\* disable)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_disable().

**Definition** bap.h:1682

[bt\_bap\_unicast\_client\_cb::start](structbt__bap__unicast__client__cb.md#a5c2d9ec444699ae5c75736115aab0b71)

void(\* start)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_start().

**Definition** bap.h:1654

[bt\_bap\_unicast\_client\_cb::location](structbt__bap__unicast__client__cb.md#a64546cd17ac346dcb4bbfad5bd9f9616)

void(\* location)(struct bt\_conn \*conn, enum bt\_audio\_dir dir, enum bt\_audio\_location loc)

Remote Unicast Server Audio Locations.

**Definition** bap.h:1585

[bt\_bap\_unicast\_client\_cb::metadata](structbt__bap__unicast__client__cb.md#a7b5fcba437b1532dbac796a48fee2f6a)

void(\* metadata)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_metadata().

**Definition** bap.h:1695

[bt\_bap\_unicast\_client\_cb::release](structbt__bap__unicast__client__cb.md#a7dc1f2486bdabf37b85d0b347563e314)

void(\* release)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_release().

**Definition** bap.h:1708

[bt\_bap\_unicast\_client\_cb::stop](structbt__bap__unicast__client__cb.md#abf8ec1b630220172887e3d3d4c550992)

void(\* stop)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_stop().

**Definition** bap.h:1669

[bt\_bap\_unicast\_client\_cb::available\_contexts](structbt__bap__unicast__client__cb.md#ac49c3b8283552213623608498a7befd2)

void(\* available\_contexts)(struct bt\_conn \*conn, enum bt\_audio\_context snk\_ctx, enum bt\_audio\_context src\_ctx)

Remote Unicast Server Available Contexts.

**Definition** bap.h:1599

[bt\_bap\_unicast\_client\_cb::endpoint](structbt__bap__unicast__client__cb.md#ae473ecc92b5c02a29742d0ba0c51ef4a)

void(\* endpoint)(struct bt\_conn \*conn, enum bt\_audio\_dir dir, struct bt\_bap\_ep \*ep)

Remote Audio Stream Endpoint (ASE) discovered.

**Definition** bap.h:1739

[bt\_bap\_unicast\_client\_cb::config](structbt__bap__unicast__client__cb.md#ae5c31f2540eb39c5b8272b5ae1e867fd)

void(\* config)(struct bt\_bap\_stream \*stream, enum bt\_bap\_ascs\_rsp\_code rsp\_code, enum bt\_bap\_ascs\_reason reason)

Callback function for bt\_bap\_stream\_config() and bt\_bap\_stream\_reconfig().

**Definition** bap.h:1611

[bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md)

Parameters for the creating unicast groups with bt\_bap\_unicast\_group\_create().

**Definition** bap.h:1454

[bt\_bap\_unicast\_group\_param::iso\_interval](structbt__bap__unicast__group__param.md#a278797713b97a6520247b01caa2938b9)

uint16\_t iso\_interval

ISO interval.

**Definition** bap.h:1498

[bt\_bap\_unicast\_group\_param::packing](structbt__bap__unicast__group__param.md#a6829c82346ca70772a4ab0dc93fbb88f)

uint8\_t packing

Unicast Group packing mode.

**Definition** bap.h:1468

[bt\_bap\_unicast\_group\_param::p\_to\_c\_ft](structbt__bap__unicast__group__param.md#a72e2c6dbeb7b7778f92af5cab2474a7e)

uint8\_t p\_to\_c\_ft

Peripheral to Central flush timeout.

**Definition** bap.h:1489

[bt\_bap\_unicast\_group\_param::c\_to\_p\_ft](structbt__bap__unicast__group__param.md#a7980c8e5c66a11507701ce2679b461ed)

uint8\_t c\_to\_p\_ft

Central to Peripheral flush timeout.

**Definition** bap.h:1479

[bt\_bap\_unicast\_group\_param::params\_count](structbt__bap__unicast__group__param.md#a9cd09b720fa9a31364878ba205b3b58c)

size\_t params\_count

The number of parameters in params.

**Definition** bap.h:1456

[bt\_bap\_unicast\_group\_param::params](structbt__bap__unicast__group__param.md#aefae7dfccdaed2bc3f59ca63689d4f2e)

struct bt\_bap\_unicast\_group\_stream\_pair\_param \* params

Array of stream parameters.

**Definition** bap.h:1459

[bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md)

Parameter struct for the unicast group functions.

**Definition** bap.h:1445

[bt\_bap\_unicast\_group\_stream\_pair\_param::rx\_param](structbt__bap__unicast__group__stream__pair__param.md#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d)

struct bt\_bap\_unicast\_group\_stream\_param \* rx\_param

Pointer to a receiving stream parameters.

**Definition** bap.h:1447

[bt\_bap\_unicast\_group\_stream\_pair\_param::tx\_param](structbt__bap__unicast__group__stream__pair__param.md#ae73a11aab16a60806d1a941306c1822a)

struct bt\_bap\_unicast\_group\_stream\_param \* tx\_param

Pointer to a transmitting stream parameters.

**Definition** bap.h:1450

[bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md)

Parameter struct for each stream in the unicast group.

**Definition** bap.h:1431

[bt\_bap\_unicast\_group\_stream\_param::qos](structbt__bap__unicast__group__stream__param.md#a35ba371c7e1050589ab8abe75cbb605d)

struct bt\_bap\_qos\_cfg \* qos

The QoS settings for the stream object.

**Definition** bap.h:1436

[bt\_bap\_unicast\_group\_stream\_param::stream](structbt__bap__unicast__group__stream__param.md#acfa192fed73b27fb194881f0021fcb35)

struct bt\_bap\_stream \* stream

Pointer to a stream object.

**Definition** bap.h:1433

[bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md)

Unicast Server callback structure.

**Definition** bap.h:1188

[bt\_bap\_unicast\_server\_cb::disable](structbt__bap__unicast__server__cb.md#a22f1af95f055bce79e3810b9682024cf)

int(\* disable)(struct bt\_bap\_stream \*stream, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Disable request callback.

**Definition** bap.h:1303

[bt\_bap\_unicast\_server\_cb::qos](structbt__bap__unicast__server__cb.md#a2d50b6c328607fc46d85eaf12633f13d)

int(\* qos)(struct bt\_bap\_stream \*stream, const struct bt\_bap\_qos\_cfg \*qos, struct bt\_bap\_ascs\_rsp \*rsp)

Stream QoS request callback.

**Definition** bap.h:1244

[bt\_bap\_unicast\_server\_cb::start](structbt__bap__unicast__server__cb.md#a48fb3021507a708a0847a1ebec6075ba)

int(\* start)(struct bt\_bap\_stream \*stream, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Start request callback.

**Definition** bap.h:1274

[bt\_bap\_unicast\_server\_cb::metadata](structbt__bap__unicast__server__cb.md#a5fe98295e41c426a12ab4a7875b665c8)

int(\* metadata)(struct bt\_bap\_stream \*stream, const uint8\_t meta[], size\_t meta\_len, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Metadata update request callback.

**Definition** bap.h:1289

[bt\_bap\_unicast\_server\_cb::enable](structbt__bap__unicast__server__cb.md#a7424079675204fba02339ddc661b77c5)

int(\* enable)(struct bt\_bap\_stream \*stream, const uint8\_t meta[], size\_t meta\_len, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Enable request callback.

**Definition** bap.h:1260

[bt\_bap\_unicast\_server\_cb::reconfig](structbt__bap__unicast__server__cb.md#a7bed12780fdf780227d38b61d76d099b)

int(\* reconfig)(struct bt\_bap\_stream \*stream, enum bt\_audio\_dir dir, const struct bt\_audio\_codec\_cfg \*codec\_cfg, struct bt\_bap\_qos\_cfg\_pref \*const pref, struct bt\_bap\_ascs\_rsp \*rsp)

Stream reconfig request callback.

**Definition** bap.h:1227

[bt\_bap\_unicast\_server\_cb::stop](structbt__bap__unicast__server__cb.md#a932296643929403c11512ff4ee7f7879)

int(\* stop)(struct bt\_bap\_stream \*stream, struct bt\_bap\_ascs\_rsp \*rsp)

Stream Stop callback.

**Definition** bap.h:1316

[bt\_bap\_unicast\_server\_cb::release](structbt__bap__unicast__server__cb.md#a9f5169f0bcdb3a6560f0767ec117b3c6)

int(\* release)(struct bt\_bap\_stream \*stream, struct bt\_bap\_ascs\_rsp \*rsp)

Stream release callback.

**Definition** bap.h:1330

[bt\_bap\_unicast\_server\_cb::config](structbt__bap__unicast__server__cb.md#ad179b35a5a5685edb8f0ac1b791d5271)

int(\* config)(struct bt\_conn \*conn, const struct bt\_bap\_ep \*ep, enum bt\_audio\_dir dir, const struct bt\_audio\_codec\_cfg \*codec\_cfg, struct bt\_bap\_stream \*\*stream, struct bt\_bap\_qos\_cfg\_pref \*const pref, struct bt\_bap\_ascs\_rsp \*rsp)

Endpoint config request callback.

**Definition** bap.h:1207

[bt\_bap\_unicast\_server\_register\_param](structbt__bap__unicast__server__register__param.md)

Structure for registering Unicast Server.

**Definition** bap.h:924

[bt\_bap\_unicast\_server\_register\_param::snk\_cnt](structbt__bap__unicast__server__register__param.md#a88635d5926173f23f411402b5961f783)

uint8\_t snk\_cnt

Sink Count to register.

**Definition** bap.h:930

[bt\_bap\_unicast\_server\_register\_param::src\_cnt](structbt__bap__unicast__server__register__param.md#ab4963c035d75404831ec1293c7f40f95)

uint8\_t src\_cnt

Source Count to register.

**Definition** bap.h:936

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:456

[bt\_iso\_biginfo](structbt__iso__biginfo.md)

Broadcast Isochronous Group (BIG) information.

**Definition** iso.h:621

[bt\_iso\_chan](structbt__iso__chan.md)

ISO Channel structure.

**Definition** iso.h:180

[bt\_iso\_recv\_info](structbt__iso__recv__info.md)

ISO Meta Data structure for received ISO packets.

**Definition** iso.h:330

[bt\_iso\_tx\_info](structbt__iso__tx__info.md)

ISO Meta Data structure for transmitted ISO packets.

**Definition** iso.h:346

[bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md)

LE advertisement and scan response packet information.

**Definition** bluetooth.h:2206

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [bap.h](bap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
