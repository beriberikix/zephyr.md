---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mcc_8h_source.html
original_path: doxygen/html/mcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcc.h

[Go to the documentation of this file.](mcc_8h.md)

1

5

6/\*

7 \* Copyright (c) 2019 - 2024 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCC\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCC\_

14

28

29#include <[stdint.h](stdint_8h.md)>

30#include <[stdbool.h](stdbool_8h.md)>

31

32#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

33#include <[zephyr/net\_buf.h](net__buf_8h.md)>

34#include <[zephyr/bluetooth/audio/media\_proxy.h](media__proxy_8h.md)>

35

36#ifdef \_\_cplusplus

37extern "C" {

38#endif

39

40/\*\*\*\* Callback functions \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

41

[ 50](group__bt__mcc.md#gab268faeca207e115ee1be0843ab8c342)typedef void (\*[bt\_mcc\_discover\_mcs\_cb](group__bt__mcc.md#gab268faeca207e115ee1be0843ab8c342))(struct bt\_conn \*conn, int err);

51

[ 61](group__bt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f)typedef void (\*[bt\_mcc\_read\_player\_name\_cb](group__bt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f))(struct bt\_conn \*conn, int err, const char \*name);

62

[ 72](group__bt__mcc.md#ga471d0491b70e5472e16c3035507761cc)typedef void (\*[bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__mcc.md#ga471d0491b70e5472e16c3035507761cc))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) icon\_id);

73

[ 83](group__bt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0)typedef void (\*[bt\_mcc\_read\_icon\_url\_cb](group__bt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0))(struct bt\_conn \*conn, int err, const char \*icon\_url);

84

[ 96](group__bt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688)typedef void (\*[bt\_mcc\_track\_changed\_ntf\_cb](group__bt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688))(struct bt\_conn \*conn, int err);

97

98

[ 108](group__bt__mcc.md#ga6927860f1803aeade4994610da32d402)typedef void (\*[bt\_mcc\_read\_track\_title\_cb](group__bt__mcc.md#ga6927860f1803aeade4994610da32d402))(struct bt\_conn \*conn, int err, const char \*title);

109

[ 119](group__bt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c)typedef void (\*[bt\_mcc\_read\_track\_duration\_cb](group__bt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c))(struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) dur);

120

[ 130](group__bt__mcc.md#ga128883c867b10e57d3f2f26a708b7263)typedef void (\*[bt\_mcc\_read\_track\_position\_cb](group__bt__mcc.md#ga128883c867b10e57d3f2f26a708b7263))(struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos);

131

[ 141](group__bt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff)typedef void (\*[bt\_mcc\_set\_track\_position\_cb](group__bt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff))(struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos);

142

[ 152](group__bt__mcc.md#ga6f5383be3f344c25361786d903640909)typedef void (\*[bt\_mcc\_read\_playback\_speed\_cb](group__bt__mcc.md#ga6f5383be3f344c25361786d903640909))(struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

153

[ 163](group__bt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779)typedef void (\*[bt\_mcc\_set\_playback\_speed\_cb](group__bt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779))(struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

164

[ 174](group__bt__mcc.md#ga3089e6165e8491325f7205279bb5bb83)typedef void (\*[bt\_mcc\_read\_seeking\_speed\_cb](group__bt__mcc.md#ga3089e6165e8491325f7205279bb5bb83))(struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

175

[ 185](group__bt__mcc.md#ga1fbf0b4fd624626127774d2662083875)typedef void (\*[bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__mcc.md#ga1fbf0b4fd624626127774d2662083875))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

186

[ 196](group__bt__mcc.md#ga28ac116604248643b0b203b4a314b7b1)typedef void (\*[bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__mcc.md#ga28ac116604248643b0b203b4a314b7b1))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

197

[ 207](group__bt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529)typedef void (\*[bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

208

[ 218](group__bt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2)typedef void (\*[bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

219

[ 229](group__bt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def)typedef void (\*[bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

230

[ 240](group__bt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4)typedef void (\*[bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

241

[ 251](group__bt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723)typedef void (\*[bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

252

[ 262](group__bt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)typedef void (\*[bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id);

263

[ 273](group__bt__mcc.md#gafb0869e0ef5332d39070081efdacf17c)typedef void (\*[bt\_mcc\_read\_playing\_order\_cb](group__bt__mcc.md#gafb0869e0ef5332d39070081efdacf17c))(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

274

[ 284](group__bt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7)typedef void (\*[bt\_mcc\_set\_playing\_order\_cb](group__bt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7))(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

285

[ 295](group__bt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0)typedef void (\*[bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0))(struct bt\_conn \*conn, int err,

296 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) orders);

297

[ 307](group__bt__mcc.md#ga200a827f4bf5d65570ddabd028269f77)typedef void (\*[bt\_mcc\_read\_media\_state\_cb](group__bt__mcc.md#ga200a827f4bf5d65570ddabd028269f77))(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

308

[ 318](group__bt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e)typedef void (\*[bt\_mcc\_send\_cmd\_cb](group__bt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e))(struct bt\_conn \*conn, int err, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

319

[ 333](group__bt__mcc.md#ga50da90a5c351c99494208b44096a61c8)typedef void (\*[bt\_mcc\_cmd\_ntf\_cb](group__bt__mcc.md#ga50da90a5c351c99494208b44096a61c8))(struct bt\_conn \*conn, int err, const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*ntf);

334

[ 344](group__bt__mcc.md#gab37df36e15132b9235d1093f5aa403cc)typedef void (\*[bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__mcc.md#gab37df36e15132b9235d1093f5aa403cc))(struct bt\_conn \*conn, int err,

345 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes);

346

[ 356](group__bt__mcc.md#ga9489c34b6006df8bd26e626030cab71f)typedef void (\*[bt\_mcc\_send\_search\_cb](group__bt__mcc.md#ga9489c34b6006df8bd26e626030cab71f))(struct bt\_conn \*conn, int err,

357 const struct [mpl\_search](structmpl__search.md) \*[search](structmpl__search.md#aa2332c1802786e2ef0486ede1c3a24c7));

358

[ 372](group__bt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3)typedef void (\*[bt\_mcc\_search\_ntf\_cb](group__bt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3))(struct bt\_conn \*conn, int err,

373 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code);

374

[ 388](group__bt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926)typedef void (\*[bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926))(struct bt\_conn \*conn,

389 int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

390

[ 400](group__bt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927)typedef void (\*[bt\_mcc\_read\_content\_control\_id\_cb](group__bt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927))(struct bt\_conn \*conn,

401 int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid);

402

403/\*\*\*\* Callback functions for the included Object Transfer service \*\*\*\*\*\*\*\*\*\*\*\*\*/

404

[ 413](group__bt__mcc.md#gaf186e6adefa296de4146502665d738b3)typedef void (\*[bt\_mcc\_otc\_obj\_selected\_cb](group__bt__mcc.md#gaf186e6adefa296de4146502665d738b3))(struct bt\_conn \*conn, int err);

414

[ 423](group__bt__mcc.md#ga9805222315ca6e6df0720233055af10c)typedef void (\*[bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__mcc.md#ga9805222315ca6e6df0720233055af10c))(struct bt\_conn \*conn, int err);

424

[ 436](group__bt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870)typedef void (\*[bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870))(struct bt\_conn \*conn, int err,

437 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

438

[ 450](group__bt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8)typedef void (\*[bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8))(struct bt\_conn \*conn, int err,

451 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

452

[ 464](group__bt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe)typedef void (\*[bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe))(struct bt\_conn \*conn, int err,

465 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

466

[ 478](group__bt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5)typedef void (\*[bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5))(struct bt\_conn \*conn, int err,

479 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

480

[ 492](group__bt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48)typedef void (\*[bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48))(struct bt\_conn \*conn, int err,

493 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

494

[ 506](group__bt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50)typedef void (\*[bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50))(struct bt\_conn \*conn, int err,

507 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

508

509

[ 513](structbt__mcc__cb.md)struct [bt\_mcc\_cb](structbt__mcc__cb.md) {

[ 515](structbt__mcc__cb.md#a2f48a0e0b891131347b0ddc2cb5a8ba7) [bt\_mcc\_discover\_mcs\_cb](group__bt__mcc.md#gab268faeca207e115ee1be0843ab8c342) [discover\_mcs](structbt__mcc__cb.md#a2f48a0e0b891131347b0ddc2cb5a8ba7);

[ 517](structbt__mcc__cb.md#aeea1ef17b3b1e24c965d71f210952079) [bt\_mcc\_read\_player\_name\_cb](group__bt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f) [read\_player\_name](structbt__mcc__cb.md#aeea1ef17b3b1e24c965d71f210952079);

518#if defined(CONFIG\_BT\_OTS\_CLIENT) || defined(\_\_DOXYGEN\_\_)

[ 520](structbt__mcc__cb.md#a00acb676c73ebbad2b0180b3e8373150) [bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__mcc.md#ga471d0491b70e5472e16c3035507761cc) [read\_icon\_obj\_id](structbt__mcc__cb.md#a00acb676c73ebbad2b0180b3e8373150);

521#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

522#if defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_PLAYER\_ICON\_URL) || defined(\_\_DOXYGEN\_\_)

[ 524](structbt__mcc__cb.md#a8c7b5954e286d074a94a39bee266082c) [bt\_mcc\_read\_icon\_url\_cb](group__bt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0) [read\_icon\_url](structbt__mcc__cb.md#a8c7b5954e286d074a94a39bee266082c);

525#endif /\* defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_PLAYER\_ICON\_URL) \*/

[ 527](structbt__mcc__cb.md#abb7769b73564a22645bfe6b11f239637) [bt\_mcc\_track\_changed\_ntf\_cb](group__bt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688) [track\_changed\_ntf](structbt__mcc__cb.md#abb7769b73564a22645bfe6b11f239637);

528#if defined(CONFIG\_BT\_MCC\_READ\_TRACK\_TITLE) || defined(\_\_DOXYGEN\_\_)

[ 530](structbt__mcc__cb.md#a3975e296b67eb244bf92254e9776ea3c) [bt\_mcc\_read\_track\_title\_cb](group__bt__mcc.md#ga6927860f1803aeade4994610da32d402) [read\_track\_title](structbt__mcc__cb.md#a3975e296b67eb244bf92254e9776ea3c);

531#endif /\* defined(CONFIG\_BT\_MCC\_READ\_TRACK\_TITLE) \*/

532#if defined(CONFIG\_BT\_MCC\_READ\_TRACK\_DURATION) || defined(\_\_DOXYGEN\_\_)

[ 534](structbt__mcc__cb.md#a85268d9ce708aef01aa528aaedf0f7e0) [bt\_mcc\_read\_track\_duration\_cb](group__bt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c) [read\_track\_duration](structbt__mcc__cb.md#a85268d9ce708aef01aa528aaedf0f7e0);

535#endif /\* defined(CONFIG\_BT\_MCC\_READ\_TRACK\_DURATION) \*/

536#if defined(CONFIG\_BT\_MCC\_READ\_TRACK\_POSITION) || defined(\_\_DOXYGEN\_\_)

[ 538](structbt__mcc__cb.md#ad1636e717ef5039586b7a1462041e888) [bt\_mcc\_read\_track\_position\_cb](group__bt__mcc.md#ga128883c867b10e57d3f2f26a708b7263) [read\_track\_position](structbt__mcc__cb.md#ad1636e717ef5039586b7a1462041e888);

539#endif /\* defined(CONFIG\_BT\_MCC\_READ\_TRACK\_POSITION) \*/

540#if defined(CONFIG\_BT\_MCC\_SET\_TRACK\_POSITION) || defined(\_\_DOXYGEN\_\_)

[ 542](structbt__mcc__cb.md#affa57da8f325dce8298d097af38d0d62) [bt\_mcc\_set\_track\_position\_cb](group__bt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff) [set\_track\_position](structbt__mcc__cb.md#affa57da8f325dce8298d097af38d0d62);

543#endif /\* defined(CONFIG\_BT\_MCC\_SET\_TRACK\_POSITION) \*/

544#if defined(CONFIG\_BT\_MCC\_READ\_PLAYBACK\_SPEED) || defined(\_\_DOXYGEN\_\_)

[ 546](structbt__mcc__cb.md#a47f8d92b18b0e4ffb3aacde05e7cb410) [bt\_mcc\_read\_playback\_speed\_cb](group__bt__mcc.md#ga6f5383be3f344c25361786d903640909) [read\_playback\_speed](structbt__mcc__cb.md#a47f8d92b18b0e4ffb3aacde05e7cb410);

547#endif /\* defined (CONFIG\_BT\_MCC\_READ\_PLAYBACK\_SPEED) \*/

548#if defined(CONFIG\_BT\_MCC\_SET\_PLAYBACK\_SPEED) || defined(\_\_DOXYGEN\_\_)

[ 550](structbt__mcc__cb.md#a5f87b5d07241b4124911be0cd6c43b37) [bt\_mcc\_set\_playback\_speed\_cb](group__bt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779) [set\_playback\_speed](structbt__mcc__cb.md#a5f87b5d07241b4124911be0cd6c43b37);

551#endif /\* defined (CONFIG\_BT\_MCC\_SET\_PLAYBACK\_SPEED) \*/

552#if defined(CONFIG\_BT\_MCC\_READ\_SEEKING\_SPEED) || defined(\_\_DOXYGEN\_\_)

[ 554](structbt__mcc__cb.md#a75c8e63baf45a119e9007f246362ab8d) [bt\_mcc\_read\_seeking\_speed\_cb](group__bt__mcc.md#ga3089e6165e8491325f7205279bb5bb83) [read\_seeking\_speed](structbt__mcc__cb.md#a75c8e63baf45a119e9007f246362ab8d);

555#endif /\* defined (CONFIG\_BT\_MCC\_READ\_SEEKING\_SPEED) \*/

556#if defined(CONFIG\_BT\_OTS\_CLIENT) || defined(\_\_DOXYGEN\_\_)

[ 558](structbt__mcc__cb.md#a810ceaee44fcbdec90a1ee227b6974df) [bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__mcc.md#ga1fbf0b4fd624626127774d2662083875) [read\_segments\_obj\_id](structbt__mcc__cb.md#a810ceaee44fcbdec90a1ee227b6974df);

[ 560](structbt__mcc__cb.md#a46bd2c23d92d8362cdf9ad4862b78407) [bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__mcc.md#ga28ac116604248643b0b203b4a314b7b1) [read\_current\_track\_obj\_id](structbt__mcc__cb.md#a46bd2c23d92d8362cdf9ad4862b78407);

[ 562](structbt__mcc__cb.md#ac9e182bbdd9671c5caee5bcd42198d90) [bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529) [set\_current\_track\_obj\_id](structbt__mcc__cb.md#ac9e182bbdd9671c5caee5bcd42198d90);

[ 564](structbt__mcc__cb.md#a540797123f8968b49a6e98b30ea534c8) [bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2) [read\_next\_track\_obj\_id](structbt__mcc__cb.md#a540797123f8968b49a6e98b30ea534c8);

[ 566](structbt__mcc__cb.md#a4f2ea54d6c60beb28feab7b6453aec7c) [bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def) [set\_next\_track\_obj\_id](structbt__mcc__cb.md#a4f2ea54d6c60beb28feab7b6453aec7c);

[ 568](structbt__mcc__cb.md#a0e7757b6f911456feaca931cd33f117f) [bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723) [read\_current\_group\_obj\_id](structbt__mcc__cb.md#a0e7757b6f911456feaca931cd33f117f);

[ 570](structbt__mcc__cb.md#ad8d3eff0cc183797280c9f668a840add) [bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c) [set\_current\_group\_obj\_id](structbt__mcc__cb.md#ad8d3eff0cc183797280c9f668a840add);

[ 572](structbt__mcc__cb.md#a87583247634728d3d9af7eb411d088a7) [bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4) [read\_parent\_group\_obj\_id](structbt__mcc__cb.md#a87583247634728d3d9af7eb411d088a7);

573#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

574#if defined(CONFIG\_BT\_MCC\_READ\_PLAYING\_ORDER) || defined(\_\_DOXYGEN\_\_)

[ 576](structbt__mcc__cb.md#a3538beef41edd96b8557b43c1266078b) [bt\_mcc\_read\_playing\_order\_cb](group__bt__mcc.md#gafb0869e0ef5332d39070081efdacf17c) [read\_playing\_order](structbt__mcc__cb.md#a3538beef41edd96b8557b43c1266078b);

577#endif /\* defined(CONFIG\_BT\_MCC\_READ\_PLAYING\_ORDER) \*/

578#if defined(CONFIG\_BT\_MCC\_SET\_PLAYING\_ORDER) || defined(\_\_DOXYGEN\_\_)

[ 580](structbt__mcc__cb.md#a00a0ba5ed665ef7fc2ca861d985ccd64) [bt\_mcc\_set\_playing\_order\_cb](group__bt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7) [set\_playing\_order](structbt__mcc__cb.md#a00a0ba5ed665ef7fc2ca861d985ccd64);

581#endif /\* defined(CONFIG\_BT\_MCC\_SET\_PLAYING\_ORDER) \*/

582#if defined(CONFIG\_BT\_MCC\_READ\_PLAYING\_ORDER\_SUPPORTED) || defined(\_\_DOXYGEN\_\_)

[ 584](structbt__mcc__cb.md#a929d7b8fc925961048d5ff5e70a5126e) [bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0) [read\_playing\_orders\_supported](structbt__mcc__cb.md#a929d7b8fc925961048d5ff5e70a5126e);

585#endif /\* defined(CONFIG\_BT\_MCC\_READ\_PLAYING\_ORDER\_SUPPORTED) \*/

586#if defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_STATE) || defined(\_\_DOXYGEN\_\_)

[ 588](structbt__mcc__cb.md#a38e4682608c7d7ff6c44431a6bdab3af) [bt\_mcc\_read\_media\_state\_cb](group__bt__mcc.md#ga200a827f4bf5d65570ddabd028269f77) [read\_media\_state](structbt__mcc__cb.md#a38e4682608c7d7ff6c44431a6bdab3af);

589#endif /\* defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_STATE) \*/

590#if defined(CONFIG\_BT\_MCC\_SET\_MEDIA\_CONTROL\_POINT) || defined(\_\_DOXYGEN\_\_)

[ 592](structbt__mcc__cb.md#a90e62e90752087da36122a65f6c9ed4e) [bt\_mcc\_send\_cmd\_cb](group__bt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e) [send\_cmd](structbt__mcc__cb.md#a90e62e90752087da36122a65f6c9ed4e);

593#endif /\* defined(CONFIG\_BT\_MCC\_SET\_MEDIA\_CONTROL\_POINT) \*/

[ 595](structbt__mcc__cb.md#a835f60ad32edc4311a624e779972f0d5) [bt\_mcc\_cmd\_ntf\_cb](group__bt__mcc.md#ga50da90a5c351c99494208b44096a61c8) [cmd\_ntf](structbt__mcc__cb.md#a835f60ad32edc4311a624e779972f0d5);

596#if defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_CONTROL\_POINT\_OPCODES\_SUPPORTED) || defined(\_\_DOXYGEN\_\_)

[ 598](structbt__mcc__cb.md#ad7ddcae67bf71030ac2d8438ac2e863f) [bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__mcc.md#gab37df36e15132b9235d1093f5aa403cc) [read\_opcodes\_supported](structbt__mcc__cb.md#ad7ddcae67bf71030ac2d8438ac2e863f);

599#endif /\* defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_CONTROL\_POINT\_OPCODES\_SUPPORTED) \*/

600#if defined(CONFIG\_BT\_OTS\_CLIENT) || defined(\_\_DOXYGEN\_\_)

[ 602](structbt__mcc__cb.md#a1c7277f390f6b478090611be9e82a4f8) [bt\_mcc\_send\_search\_cb](group__bt__mcc.md#ga9489c34b6006df8bd26e626030cab71f) [send\_search](structbt__mcc__cb.md#a1c7277f390f6b478090611be9e82a4f8);

[ 604](structbt__mcc__cb.md#a9f7f3424aa230a8752f40a40b82b0b66) [bt\_mcc\_search\_ntf\_cb](group__bt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3) [search\_ntf](structbt__mcc__cb.md#a9f7f3424aa230a8752f40a40b82b0b66);

[ 606](structbt__mcc__cb.md#aaa2bdfb99e5cd7c2a0d0c800533e8491) [bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926) [read\_search\_results\_obj\_id](structbt__mcc__cb.md#aaa2bdfb99e5cd7c2a0d0c800533e8491);

607#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

608#if defined(CONFIG\_BT\_MCC\_READ\_CONTENT\_CONTROL\_ID) || defined(\_\_DOXYGEN\_\_)

[ 610](structbt__mcc__cb.md#ae4d0e2e4df695352e8d2ed76db1f420e) [bt\_mcc\_read\_content\_control\_id\_cb](group__bt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927) [read\_content\_control\_id](structbt__mcc__cb.md#ae4d0e2e4df695352e8d2ed76db1f420e);

611#endif /\* defined(CONFIG\_BT\_MCC\_READ\_CONTENT\_CONTROL\_ID) \*/

612#if defined(CONFIG\_BT\_OTS\_CLIENT) || defined(\_\_DOXYGEN\_\_)

[ 614](structbt__mcc__cb.md#a17ebc9dbddd714d99b599b2a683ab771) [bt\_mcc\_otc\_obj\_selected\_cb](group__bt__mcc.md#gaf186e6adefa296de4146502665d738b3) [otc\_obj\_selected](structbt__mcc__cb.md#a17ebc9dbddd714d99b599b2a683ab771);

[ 616](structbt__mcc__cb.md#af1c9664a2459550af0a6ed611fd17263) [bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__mcc.md#ga9805222315ca6e6df0720233055af10c) [otc\_obj\_metadata](structbt__mcc__cb.md#af1c9664a2459550af0a6ed611fd17263);

[ 618](structbt__mcc__cb.md#a054e0cfb27c01f43d499a2c44788cb73) [bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870) [otc\_icon\_object](structbt__mcc__cb.md#a054e0cfb27c01f43d499a2c44788cb73);

[ 620](structbt__mcc__cb.md#a2c1b570ce8d83c3f20eb99807263a5cd) [bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8) [otc\_track\_segments\_object](structbt__mcc__cb.md#a2c1b570ce8d83c3f20eb99807263a5cd);

[ 622](structbt__mcc__cb.md#ad13669e60992a1a407534f387efd1da8) [bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe) [otc\_current\_track\_object](structbt__mcc__cb.md#ad13669e60992a1a407534f387efd1da8);

[ 624](structbt__mcc__cb.md#a52724924ab19f59cc936344ebe13d437) [bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5) [otc\_next\_track\_object](structbt__mcc__cb.md#a52724924ab19f59cc936344ebe13d437);

[ 626](structbt__mcc__cb.md#ac0e382f1117f983e7a2178fde274d460) [bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50) [otc\_current\_group\_object](structbt__mcc__cb.md#ac0e382f1117f983e7a2178fde274d460);

[ 628](structbt__mcc__cb.md#a872d0322ba3889f1f7d32e8966b53624) [bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48) [otc\_parent\_group\_object](structbt__mcc__cb.md#a872d0322ba3889f1f7d32e8966b53624);

629#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

630};

631

632/\*\*\*\* Functions \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

633

[ 641](group__bt__mcc.md#ga94de08bb0a1e1324600e4957b648e92b)int [bt\_mcc\_init](group__bt__mcc.md#ga94de08bb0a1e1324600e4957b648e92b)(struct [bt\_mcc\_cb](structbt__mcc__cb.md) \*cb);

642

643

[ 658](group__bt__mcc.md#gaa1f9ead03b4cccaff1e3390b8052b0f3)int [bt\_mcc\_discover\_mcs](group__bt__mcc.md#gaa1f9ead03b4cccaff1e3390b8052b0f3)(struct bt\_conn \*conn, bool subscribe);

659

[ 667](group__bt__mcc.md#ga724ce71fc88f1ca4bcf209c92c177f36)int [bt\_mcc\_read\_player\_name](group__bt__mcc.md#ga724ce71fc88f1ca4bcf209c92c177f36)(struct bt\_conn \*conn);

668

[ 676](group__bt__mcc.md#ga0e69de33c37957a2b5473df7d3c3f389)int [bt\_mcc\_read\_icon\_obj\_id](group__bt__mcc.md#ga0e69de33c37957a2b5473df7d3c3f389)(struct bt\_conn \*conn);

677

[ 685](group__bt__mcc.md#ga38733456db6bc6558a511e104577c9c9)int [bt\_mcc\_read\_icon\_url](group__bt__mcc.md#ga38733456db6bc6558a511e104577c9c9)(struct bt\_conn \*conn);

686

[ 694](group__bt__mcc.md#ga7dfa14489a4cea4b00053c9aa75cf373)int [bt\_mcc\_read\_track\_title](group__bt__mcc.md#ga7dfa14489a4cea4b00053c9aa75cf373)(struct bt\_conn \*conn);

695

[ 703](group__bt__mcc.md#ga50a45f043bd2ae1741a120e02e9dc2f5)int [bt\_mcc\_read\_track\_duration](group__bt__mcc.md#ga50a45f043bd2ae1741a120e02e9dc2f5)(struct bt\_conn \*conn);

704

[ 712](group__bt__mcc.md#gaf143098f5dfcfba01df3d6f06472779e)int [bt\_mcc\_read\_track\_position](group__bt__mcc.md#gaf143098f5dfcfba01df3d6f06472779e)(struct bt\_conn \*conn);

713

[ 722](group__bt__mcc.md#gad324366d33bef6b1ed1c8fc881bf44cf)int [bt\_mcc\_set\_track\_position](group__bt__mcc.md#gad324366d33bef6b1ed1c8fc881bf44cf)(struct bt\_conn \*conn, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos);

723

[ 731](group__bt__mcc.md#gaa566a4c42f0ab0ab6feddf4e25845609)int [bt\_mcc\_read\_playback\_speed](group__bt__mcc.md#gaa566a4c42f0ab0ab6feddf4e25845609)(struct bt\_conn \*conn);

732

[ 741](group__bt__mcc.md#ga1382e5b6000896dc94f6489909301719)int [bt\_mcc\_set\_playback\_speed](group__bt__mcc.md#ga1382e5b6000896dc94f6489909301719)(struct bt\_conn \*conn, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

742

[ 750](group__bt__mcc.md#ga366fdfaa23cef9f1c3ba7ddd36a67658)int [bt\_mcc\_read\_seeking\_speed](group__bt__mcc.md#ga366fdfaa23cef9f1c3ba7ddd36a67658)(struct bt\_conn \*conn);

751

[ 759](group__bt__mcc.md#ga4cb0a95e91d3ec00ede64663a2b932f0)int [bt\_mcc\_read\_segments\_obj\_id](group__bt__mcc.md#ga4cb0a95e91d3ec00ede64663a2b932f0)(struct bt\_conn \*conn);

760

[ 768](group__bt__mcc.md#ga5b3a8fb8e8251cf005b34e47619ae7b9)int [bt\_mcc\_read\_current\_track\_obj\_id](group__bt__mcc.md#ga5b3a8fb8e8251cf005b34e47619ae7b9)(struct bt\_conn \*conn);

769

[ 780](group__bt__mcc.md#ga8374ac230c5fe6b5a1bb7fa873fdeb49)int [bt\_mcc\_set\_current\_track\_obj\_id](group__bt__mcc.md#ga8374ac230c5fe6b5a1bb7fa873fdeb49)(struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

781

[ 789](group__bt__mcc.md#ga11e4c02ba0b1fbc197aaf071b82a1eed)int [bt\_mcc\_read\_next\_track\_obj\_id](group__bt__mcc.md#ga11e4c02ba0b1fbc197aaf071b82a1eed)(struct bt\_conn \*conn);

790

[ 801](group__bt__mcc.md#gafeebcbb0c77d5d4acbe151fd9888d084)int [bt\_mcc\_set\_next\_track\_obj\_id](group__bt__mcc.md#gafeebcbb0c77d5d4acbe151fd9888d084)(struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

802

[ 810](group__bt__mcc.md#ga8cb43a6947df48113b082d8cc8ccf25c)int [bt\_mcc\_read\_current\_group\_obj\_id](group__bt__mcc.md#ga8cb43a6947df48113b082d8cc8ccf25c)(struct bt\_conn \*conn);

811

[ 822](group__bt__mcc.md#gae3f385811f852d584595c6e531556aed)int [bt\_mcc\_set\_current\_group\_obj\_id](group__bt__mcc.md#gae3f385811f852d584595c6e531556aed)(struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

823

[ 831](group__bt__mcc.md#ga3ccd5961cc4c8d82fa988d300e12e1ae)int [bt\_mcc\_read\_parent\_group\_obj\_id](group__bt__mcc.md#ga3ccd5961cc4c8d82fa988d300e12e1ae)(struct bt\_conn \*conn);

832

[ 840](group__bt__mcc.md#ga077a134ff1404fb76aa756a5531fd1d7)int [bt\_mcc\_read\_playing\_order](group__bt__mcc.md#ga077a134ff1404fb76aa756a5531fd1d7)(struct bt\_conn \*conn);

841

[ 850](group__bt__mcc.md#ga05295649385c3a337401765627d09553)int [bt\_mcc\_set\_playing\_order](group__bt__mcc.md#ga05295649385c3a337401765627d09553)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

851

[ 859](group__bt__mcc.md#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)int [bt\_mcc\_read\_playing\_orders\_supported](group__bt__mcc.md#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)(struct bt\_conn \*conn);

860

[ 868](group__bt__mcc.md#gac1b440cfa54dd4b6e23bb47bf885f88d)int [bt\_mcc\_read\_media\_state](group__bt__mcc.md#gac1b440cfa54dd4b6e23bb47bf885f88d)(struct bt\_conn \*conn);

869

[ 880](group__bt__mcc.md#ga3f4a538bcf436e4e80b73ed6e077dfa0)int [bt\_mcc\_send\_cmd](group__bt__mcc.md#ga3f4a538bcf436e4e80b73ed6e077dfa0)(struct bt\_conn \*conn, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

881

[ 889](group__bt__mcc.md#ga692160554947f92e8c81912c5e597086)int [bt\_mcc\_read\_opcodes\_supported](group__bt__mcc.md#ga692160554947f92e8c81912c5e597086)(struct bt\_conn \*conn);

890

[ 901](group__bt__mcc.md#ga324161056e03195820bbd7cc77ff287d)int [bt\_mcc\_send\_search](group__bt__mcc.md#ga324161056e03195820bbd7cc77ff287d)(struct bt\_conn \*conn, const struct [mpl\_search](structmpl__search.md) \*search);

902

[ 910](group__bt__mcc.md#ga98814a516a027bdaa3250e93d55309fd)int [bt\_mcc\_read\_search\_results\_obj\_id](group__bt__mcc.md#ga98814a516a027bdaa3250e93d55309fd)(struct bt\_conn \*conn);

911

[ 919](group__bt__mcc.md#ga77cbf810c35d1a17efce1fae6a941963)int [bt\_mcc\_read\_content\_control\_id](group__bt__mcc.md#ga77cbf810c35d1a17efce1fae6a941963)(struct bt\_conn \*conn);

920

[ 928](group__bt__mcc.md#gadf687cb26a6d00bca73e273da583df88)int [bt\_mcc\_otc\_read\_object\_metadata](group__bt__mcc.md#gadf687cb26a6d00bca73e273da583df88)(struct bt\_conn \*conn);

929

[ 937](group__bt__mcc.md#gaba527d8f0307ab11150a5434231c0e7e)int [bt\_mcc\_otc\_read\_icon\_object](group__bt__mcc.md#gaba527d8f0307ab11150a5434231c0e7e)(struct bt\_conn \*conn);

938

[ 946](group__bt__mcc.md#gac22e840b65895aa018ab1b4535a87672)int [bt\_mcc\_otc\_read\_track\_segments\_object](group__bt__mcc.md#gac22e840b65895aa018ab1b4535a87672)(struct bt\_conn \*conn);

947

[ 955](group__bt__mcc.md#gac4b09a77df52d2681e7652591ca32bf8)int [bt\_mcc\_otc\_read\_current\_track\_object](group__bt__mcc.md#gac4b09a77df52d2681e7652591ca32bf8)(struct bt\_conn \*conn);

956

[ 964](group__bt__mcc.md#ga611c9edebff5b4347ad1241ffd19f49e)int [bt\_mcc\_otc\_read\_next\_track\_object](group__bt__mcc.md#ga611c9edebff5b4347ad1241ffd19f49e)(struct bt\_conn \*conn);

965

[ 973](group__bt__mcc.md#ga4b1ebe682ad134795f8a1b494244f8b6)int [bt\_mcc\_otc\_read\_current\_group\_object](group__bt__mcc.md#ga4b1ebe682ad134795f8a1b494244f8b6)(struct bt\_conn \*conn);

974

[ 982](group__bt__mcc.md#gae001cb2d701457ce083aa8a0fd5ec518)int [bt\_mcc\_otc\_read\_parent\_group\_object](group__bt__mcc.md#gae001cb2d701457ce083aa8a0fd5ec518)(struct bt\_conn \*conn);

983

[ 992](group__bt__mcc.md#gaa243806f65c4a37d41f25bcc4f1839fc)struct [bt\_ots\_client](structbt__ots__client.md) \*[bt\_mcc\_otc\_inst](group__bt__mcc.md#gaa243806f65c4a37d41f25bcc4f1839fc)(struct bt\_conn \*conn);

993

994#ifdef \_\_cplusplus

995}

996#endif

997

1001

1002#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCC\_\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_mcc\_set\_playing\_order](group__bt__mcc.md#ga05295649385c3a337401765627d09553)

int bt\_mcc\_set\_playing\_order(struct bt\_conn \*conn, uint8\_t order)

Set Playing Order.

[bt\_mcc\_read\_playing\_order](group__bt__mcc.md#ga077a134ff1404fb76aa756a5531fd1d7)

int bt\_mcc\_read\_playing\_order(struct bt\_conn \*conn)

Read Playing Order.

[bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50)

void(\* bt\_mcc\_otc\_read\_current\_group\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_current\_group\_object().

**Definition** mcc.h:506

[bt\_mcc\_read\_icon\_obj\_id](group__bt__mcc.md#ga0e69de33c37957a2b5473df7d3c3f389)

int bt\_mcc\_read\_icon\_obj\_id(struct bt\_conn \*conn)

Read Icon Object ID.

[bt\_mcc\_set\_track\_position\_cb](group__bt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff)

void(\* bt\_mcc\_set\_track\_position\_cb)(struct bt\_conn \*conn, int err, int32\_t pos)

Callback function for bt\_mcc\_set\_track\_position().

**Definition** mcc.h:141

[bt\_mcc\_read\_next\_track\_obj\_id](group__bt__mcc.md#ga11e4c02ba0b1fbc197aaf071b82a1eed)

int bt\_mcc\_read\_next\_track\_obj\_id(struct bt\_conn \*conn)

Read Next Track Object ID.

[bt\_mcc\_read\_track\_position\_cb](group__bt__mcc.md#ga128883c867b10e57d3f2f26a708b7263)

void(\* bt\_mcc\_read\_track\_position\_cb)(struct bt\_conn \*conn, int err, int32\_t pos)

Callback function for bt\_mcc\_read\_track\_position().

**Definition** mcc.h:130

[bt\_mcc\_set\_playback\_speed\_cb](group__bt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779)

void(\* bt\_mcc\_set\_playback\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)

Callback function for bt\_mcc\_set\_playback\_speed().

**Definition** mcc.h:163

[bt\_mcc\_set\_playback\_speed](group__bt__mcc.md#ga1382e5b6000896dc94f6489909301719)

int bt\_mcc\_set\_playback\_speed(struct bt\_conn \*conn, int8\_t speed)

Set Playback Speed.

[bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870)

void(\* bt\_mcc\_otc\_read\_icon\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_icon\_object().

**Definition** mcc.h:436

[bt\_mcc\_set\_playing\_order\_cb](group__bt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7)

void(\* bt\_mcc\_set\_playing\_order\_cb)(struct bt\_conn \*conn, int err, uint8\_t order)

Callback function for bt\_mcc\_set\_playing\_order().

**Definition** mcc.h:284

[bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8)

void(\* bt\_mcc\_otc\_read\_track\_segments\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_track\_segments\_object().

**Definition** mcc.h:450

[bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__mcc.md#ga1fbf0b4fd624626127774d2662083875)

void(\* bt\_mcc\_read\_segments\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_segments\_obj\_id().

**Definition** mcc.h:185

[bt\_mcc\_read\_media\_state\_cb](group__bt__mcc.md#ga200a827f4bf5d65570ddabd028269f77)

void(\* bt\_mcc\_read\_media\_state\_cb)(struct bt\_conn \*conn, int err, uint8\_t state)

Callback function for bt\_mcc\_read\_media\_state().

**Definition** mcc.h:307

[bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__mcc.md#ga28ac116604248643b0b203b4a314b7b1)

void(\* bt\_mcc\_read\_current\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_current\_track\_obj\_id().

**Definition** mcc.h:196

[bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def)

void(\* bt\_mcc\_set\_next\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_set\_next\_track\_obj\_id().

**Definition** mcc.h:229

[bt\_mcc\_read\_seeking\_speed\_cb](group__bt__mcc.md#ga3089e6165e8491325f7205279bb5bb83)

void(\* bt\_mcc\_read\_seeking\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)

Callback function for bt\_mcc\_read\_seeking\_speed().

**Definition** mcc.h:174

[bt\_mcc\_send\_search](group__bt__mcc.md#ga324161056e03195820bbd7cc77ff287d)

int bt\_mcc\_send\_search(struct bt\_conn \*conn, const struct mpl\_search \*search)

Send a Search command.

[bt\_mcc\_read\_seeking\_speed](group__bt__mcc.md#ga366fdfaa23cef9f1c3ba7ddd36a67658)

int bt\_mcc\_read\_seeking\_speed(struct bt\_conn \*conn)

Read Seeking speed.

[bt\_mcc\_read\_icon\_url](group__bt__mcc.md#ga38733456db6bc6558a511e104577c9c9)

int bt\_mcc\_read\_icon\_url(struct bt\_conn \*conn)

Read Icon Object URL.

[bt\_mcc\_read\_parent\_group\_obj\_id](group__bt__mcc.md#ga3ccd5961cc4c8d82fa988d300e12e1ae)

int bt\_mcc\_read\_parent\_group\_obj\_id(struct bt\_conn \*conn)

Read Parent Group Object ID.

[bt\_mcc\_send\_cmd](group__bt__mcc.md#ga3f4a538bcf436e4e80b73ed6e077dfa0)

int bt\_mcc\_send\_cmd(struct bt\_conn \*conn, const struct mpl\_cmd \*cmd)

Send a command.

[bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__mcc.md#ga471d0491b70e5472e16c3035507761cc)

void(\* bt\_mcc\_read\_icon\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t icon\_id)

Callback function for bt\_mcc\_read\_icon\_obj\_id().

**Definition** mcc.h:72

[bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4)

void(\* bt\_mcc\_read\_parent\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_parent\_group\_obj\_id().

**Definition** mcc.h:240

[bt\_mcc\_otc\_read\_current\_group\_object](group__bt__mcc.md#ga4b1ebe682ad134795f8a1b494244f8b6)

int bt\_mcc\_otc\_read\_current\_group\_object(struct bt\_conn \*conn)

Read the Current Group Object.

[bt\_mcc\_read\_segments\_obj\_id](group__bt__mcc.md#ga4cb0a95e91d3ec00ede64663a2b932f0)

int bt\_mcc\_read\_segments\_obj\_id(struct bt\_conn \*conn)

Read Track Segments Object ID.

[bt\_mcc\_read\_track\_duration](group__bt__mcc.md#ga50a45f043bd2ae1741a120e02e9dc2f5)

int bt\_mcc\_read\_track\_duration(struct bt\_conn \*conn)

Read Track Duration.

[bt\_mcc\_cmd\_ntf\_cb](group__bt__mcc.md#ga50da90a5c351c99494208b44096a61c8)

void(\* bt\_mcc\_cmd\_ntf\_cb)(struct bt\_conn \*conn, int err, const struct mpl\_cmd\_ntf \*ntf)

Callback function for command notifications.

**Definition** mcc.h:333

[bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926)

void(\* bt\_mcc\_read\_search\_results\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_search\_results\_obj\_id().

**Definition** mcc.h:388

[bt\_mcc\_read\_current\_track\_obj\_id](group__bt__mcc.md#ga5b3a8fb8e8251cf005b34e47619ae7b9)

int bt\_mcc\_read\_current\_track\_obj\_id(struct bt\_conn \*conn)

Read Current Track Object ID.

[bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723)

void(\* bt\_mcc\_read\_current\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_current\_group\_obj\_id().

**Definition** mcc.h:251

[bt\_mcc\_otc\_read\_next\_track\_object](group__bt__mcc.md#ga611c9edebff5b4347ad1241ffd19f49e)

int bt\_mcc\_otc\_read\_next\_track\_object(struct bt\_conn \*conn)

Read the Next Track Object.

[bt\_mcc\_track\_changed\_ntf\_cb](group__bt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688)

void(\* bt\_mcc\_track\_changed\_ntf\_cb)(struct bt\_conn \*conn, int err)

Callback function for track changed notifications.

**Definition** mcc.h:96

[bt\_mcc\_read\_opcodes\_supported](group__bt__mcc.md#ga692160554947f92e8c81912c5e597086)

int bt\_mcc\_read\_opcodes\_supported(struct bt\_conn \*conn)

Read Opcodes Supported.

[bt\_mcc\_read\_track\_title\_cb](group__bt__mcc.md#ga6927860f1803aeade4994610da32d402)

void(\* bt\_mcc\_read\_track\_title\_cb)(struct bt\_conn \*conn, int err, const char \*title)

Callback function for bt\_mcc\_read\_track\_title().

**Definition** mcc.h:108

[bt\_mcc\_read\_playback\_speed\_cb](group__bt__mcc.md#ga6f5383be3f344c25361786d903640909)

void(\* bt\_mcc\_read\_playback\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)

Callback function for bt\_mcc\_read\_playback\_speed().

**Definition** mcc.h:152

[bt\_mcc\_read\_player\_name](group__bt__mcc.md#ga724ce71fc88f1ca4bcf209c92c177f36)

int bt\_mcc\_read\_player\_name(struct bt\_conn \*conn)

Read Media Player Name.

[bt\_mcc\_read\_content\_control\_id](group__bt__mcc.md#ga77cbf810c35d1a17efce1fae6a941963)

int bt\_mcc\_read\_content\_control\_id(struct bt\_conn \*conn)

Read Content Control ID.

[bt\_mcc\_read\_track\_duration\_cb](group__bt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c)

void(\* bt\_mcc\_read\_track\_duration\_cb)(struct bt\_conn \*conn, int err, int32\_t dur)

Callback function for bt\_mcc\_read\_track\_duration().

**Definition** mcc.h:119

[bt\_mcc\_read\_track\_title](group__bt__mcc.md#ga7dfa14489a4cea4b00053c9aa75cf373)

int bt\_mcc\_read\_track\_title(struct bt\_conn \*conn)

Read Track Title.

[bt\_mcc\_set\_current\_track\_obj\_id](group__bt__mcc.md#ga8374ac230c5fe6b5a1bb7fa873fdeb49)

int bt\_mcc\_set\_current\_track\_obj\_id(struct bt\_conn \*conn, uint64\_t id)

Set Current Track Object ID.

[bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2)

void(\* bt\_mcc\_read\_next\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_next\_track\_obj\_id\_obj().

**Definition** mcc.h:218

[bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)

void(\* bt\_mcc\_set\_current\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t obj\_id)

Callback function for bt\_mcc\_set\_current\_group\_obj\_id().

**Definition** mcc.h:262

[bt\_mcc\_read\_current\_group\_obj\_id](group__bt__mcc.md#ga8cb43a6947df48113b082d8cc8ccf25c)

int bt\_mcc\_read\_current\_group\_obj\_id(struct bt\_conn \*conn)

Read Current Group Object ID.

[bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5)

void(\* bt\_mcc\_otc\_read\_next\_track\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_next\_track\_object().

**Definition** mcc.h:478

[bt\_mcc\_send\_search\_cb](group__bt__mcc.md#ga9489c34b6006df8bd26e626030cab71f)

void(\* bt\_mcc\_send\_search\_cb)(struct bt\_conn \*conn, int err, const struct mpl\_search \*search)

Callback function for bt\_mcc\_send\_search().

**Definition** mcc.h:356

[bt\_mcc\_init](group__bt__mcc.md#ga94de08bb0a1e1324600e4957b648e92b)

int bt\_mcc\_init(struct bt\_mcc\_cb \*cb)

Initialize Media Control Client.

[bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__mcc.md#ga9805222315ca6e6df0720233055af10c)

void(\* bt\_mcc\_otc\_obj\_metadata\_cb)(struct bt\_conn \*conn, int err)

Callback function for bt\_mcc\_otc\_read\_object\_metadata().

**Definition** mcc.h:423

[bt\_mcc\_read\_search\_results\_obj\_id](group__bt__mcc.md#ga98814a516a027bdaa3250e93d55309fd)

int bt\_mcc\_read\_search\_results\_obj\_id(struct bt\_conn \*conn)

Search Results Group Object ID.

[bt\_mcc\_discover\_mcs](group__bt__mcc.md#gaa1f9ead03b4cccaff1e3390b8052b0f3)

int bt\_mcc\_discover\_mcs(struct bt\_conn \*conn, bool subscribe)

Discover Media Control Service.

[bt\_mcc\_otc\_inst](group__bt__mcc.md#gaa243806f65c4a37d41f25bcc4f1839fc)

struct bt\_ots\_client \* bt\_mcc\_otc\_inst(struct bt\_conn \*conn)

Look up MCC OTC instance.

[bt\_mcc\_read\_playback\_speed](group__bt__mcc.md#gaa566a4c42f0ab0ab6feddf4e25845609)

int bt\_mcc\_read\_playback\_speed(struct bt\_conn \*conn)

Read Playback speed.

[bt\_mcc\_read\_player\_name\_cb](group__bt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f)

void(\* bt\_mcc\_read\_player\_name\_cb)(struct bt\_conn \*conn, int err, const char \*name)

Callback function for bt\_mcc\_read\_player\_name().

**Definition** mcc.h:61

[bt\_mcc\_read\_icon\_url\_cb](group__bt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0)

void(\* bt\_mcc\_read\_icon\_url\_cb)(struct bt\_conn \*conn, int err, const char \*icon\_url)

Callback function for bt\_mcc\_read\_icon\_url().

**Definition** mcc.h:83

[bt\_mcc\_search\_ntf\_cb](group__bt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3)

void(\* bt\_mcc\_search\_ntf\_cb)(struct bt\_conn \*conn, int err, uint8\_t result\_code)

Callback function for search notifications.

**Definition** mcc.h:372

[bt\_mcc\_discover\_mcs\_cb](group__bt__mcc.md#gab268faeca207e115ee1be0843ab8c342)

void(\* bt\_mcc\_discover\_mcs\_cb)(struct bt\_conn \*conn, int err)

Callback function for bt\_mcc\_discover\_mcs().

**Definition** mcc.h:50

[bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__mcc.md#gab37df36e15132b9235d1093f5aa403cc)

void(\* bt\_mcc\_read\_opcodes\_supported\_cb)(struct bt\_conn \*conn, int err, uint32\_t opcodes)

Callback function for bt\_mcc\_read\_opcodes\_supported().

**Definition** mcc.h:344

[bt\_mcc\_otc\_read\_icon\_object](group__bt__mcc.md#gaba527d8f0307ab11150a5434231c0e7e)

int bt\_mcc\_otc\_read\_icon\_object(struct bt\_conn \*conn)

Read the Icon Object.

[bt\_mcc\_read\_media\_state](group__bt__mcc.md#gac1b440cfa54dd4b6e23bb47bf885f88d)

int bt\_mcc\_read\_media\_state(struct bt\_conn \*conn)

Read Media State.

[bt\_mcc\_otc\_read\_track\_segments\_object](group__bt__mcc.md#gac22e840b65895aa018ab1b4535a87672)

int bt\_mcc\_otc\_read\_track\_segments\_object(struct bt\_conn \*conn)

Read the Track Segments Object.

[bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0)

void(\* bt\_mcc\_read\_playing\_orders\_supported\_cb)(struct bt\_conn \*conn, int err, uint16\_t orders)

Callback function for bt\_mcc\_read\_playing\_orders\_supported().

**Definition** mcc.h:295

[bt\_mcc\_otc\_read\_current\_track\_object](group__bt__mcc.md#gac4b09a77df52d2681e7652591ca32bf8)

int bt\_mcc\_otc\_read\_current\_track\_object(struct bt\_conn \*conn)

Read the Current Track Object.

[bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48)

void(\* bt\_mcc\_otc\_read\_parent\_group\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_parent\_group\_object().

**Definition** mcc.h:492

[bt\_mcc\_set\_track\_position](group__bt__mcc.md#gad324366d33bef6b1ed1c8fc881bf44cf)

int bt\_mcc\_set\_track\_position(struct bt\_conn \*conn, int32\_t pos)

Set Track position.

[bt\_mcc\_read\_content\_control\_id\_cb](group__bt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927)

void(\* bt\_mcc\_read\_content\_control\_id\_cb)(struct bt\_conn \*conn, int err, uint8\_t ccid)

Callback function for bt\_mcc\_read\_content\_control\_id().

**Definition** mcc.h:400

[bt\_mcc\_otc\_read\_object\_metadata](group__bt__mcc.md#gadf687cb26a6d00bca73e273da583df88)

int bt\_mcc\_otc\_read\_object\_metadata(struct bt\_conn \*conn)

Read the current object metadata.

[bt\_mcc\_otc\_read\_parent\_group\_object](group__bt__mcc.md#gae001cb2d701457ce083aa8a0fd5ec518)

int bt\_mcc\_otc\_read\_parent\_group\_object(struct bt\_conn \*conn)

Read the Parent Group Object.

[bt\_mcc\_set\_current\_group\_obj\_id](group__bt__mcc.md#gae3f385811f852d584595c6e531556aed)

int bt\_mcc\_set\_current\_group\_obj\_id(struct bt\_conn \*conn, uint64\_t id)

Set Current Group Object ID.

[bt\_mcc\_send\_cmd\_cb](group__bt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e)

void(\* bt\_mcc\_send\_cmd\_cb)(struct bt\_conn \*conn, int err, const struct mpl\_cmd \*cmd)

Callback function for bt\_mcc\_send\_cmd().

**Definition** mcc.h:318

[bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529)

void(\* bt\_mcc\_set\_current\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_set\_current\_track\_obj\_id().

**Definition** mcc.h:207

[bt\_mcc\_read\_track\_position](group__bt__mcc.md#gaf143098f5dfcfba01df3d6f06472779e)

int bt\_mcc\_read\_track\_position(struct bt\_conn \*conn)

Read Track Position.

[bt\_mcc\_otc\_obj\_selected\_cb](group__bt__mcc.md#gaf186e6adefa296de4146502665d738b3)

void(\* bt\_mcc\_otc\_obj\_selected\_cb)(struct bt\_conn \*conn, int err)

Callback function for object selected.

**Definition** mcc.h:413

[bt\_mcc\_read\_playing\_orders\_supported](group__bt__mcc.md#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)

int bt\_mcc\_read\_playing\_orders\_supported(struct bt\_conn \*conn)

Read Playing Orders Supported.

[bt\_mcc\_read\_playing\_order\_cb](group__bt__mcc.md#gafb0869e0ef5332d39070081efdacf17c)

void(\* bt\_mcc\_read\_playing\_order\_cb)(struct bt\_conn \*conn, int err, uint8\_t order)

Callback function for bt\_mcc\_read\_playing\_order().

**Definition** mcc.h:273

[bt\_mcc\_set\_next\_track\_obj\_id](group__bt__mcc.md#gafeebcbb0c77d5d4acbe151fd9888d084)

int bt\_mcc\_set\_next\_track\_obj\_id(struct bt\_conn \*conn, uint64\_t id)

Set Next Track Object ID.

[bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe)

void(\* bt\_mcc\_otc\_read\_current\_track\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_current\_track\_object().

**Definition** mcc.h:464

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[media\_proxy.h](media__proxy_8h.md)

Bluetooth Media Proxy APIs.

[net\_buf.h](net__buf_8h.md)

Buffer management.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

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

[bt\_mcc\_cb](structbt__mcc__cb.md)

Media control client callbacks.

**Definition** mcc.h:513

[bt\_mcc\_cb::set\_playing\_order](structbt__mcc__cb.md#a00a0ba5ed665ef7fc2ca861d985ccd64)

bt\_mcc\_set\_playing\_order\_cb set\_playing\_order

Callback when setting the playing order.

**Definition** mcc.h:580

[bt\_mcc\_cb::read\_icon\_obj\_id](structbt__mcc__cb.md#a00acb676c73ebbad2b0180b3e8373150)

bt\_mcc\_read\_icon\_obj\_id\_cb read\_icon\_obj\_id

Callback when reading the icon object ID.

**Definition** mcc.h:520

[bt\_mcc\_cb::otc\_icon\_object](structbt__mcc__cb.md#a054e0cfb27c01f43d499a2c44788cb73)

bt\_mcc\_otc\_read\_icon\_object\_cb otc\_icon\_object

Callback when reading the current icon object.

**Definition** mcc.h:618

[bt\_mcc\_cb::read\_current\_group\_obj\_id](structbt__mcc__cb.md#a0e7757b6f911456feaca931cd33f117f)

bt\_mcc\_read\_current\_group\_obj\_id\_cb read\_current\_group\_obj\_id

Callback when reading the current group object ID.

**Definition** mcc.h:568

[bt\_mcc\_cb::otc\_obj\_selected](structbt__mcc__cb.md#a17ebc9dbddd714d99b599b2a683ab771)

bt\_mcc\_otc\_obj\_selected\_cb otc\_obj\_selected

Callback when selecting an object.

**Definition** mcc.h:614

[bt\_mcc\_cb::send\_search](structbt__mcc__cb.md#a1c7277f390f6b478090611be9e82a4f8)

bt\_mcc\_send\_search\_cb send\_search

Callback when sending the a search query.

**Definition** mcc.h:602

[bt\_mcc\_cb::otc\_track\_segments\_object](structbt__mcc__cb.md#a2c1b570ce8d83c3f20eb99807263a5cd)

bt\_mcc\_otc\_read\_track\_segments\_object\_cb otc\_track\_segments\_object

Callback when reading the track segments object.

**Definition** mcc.h:620

[bt\_mcc\_cb::discover\_mcs](structbt__mcc__cb.md#a2f48a0e0b891131347b0ddc2cb5a8ba7)

bt\_mcc\_discover\_mcs\_cb discover\_mcs

Callback when discovery has finished.

**Definition** mcc.h:515

[bt\_mcc\_cb::read\_playing\_order](structbt__mcc__cb.md#a3538beef41edd96b8557b43c1266078b)

bt\_mcc\_read\_playing\_order\_cb read\_playing\_order

Callback when reading the playing order.

**Definition** mcc.h:576

[bt\_mcc\_cb::read\_media\_state](structbt__mcc__cb.md#a38e4682608c7d7ff6c44431a6bdab3af)

bt\_mcc\_read\_media\_state\_cb read\_media\_state

Callback when reading the media state.

**Definition** mcc.h:588

[bt\_mcc\_cb::read\_track\_title](structbt__mcc__cb.md#a3975e296b67eb244bf92254e9776ea3c)

bt\_mcc\_read\_track\_title\_cb read\_track\_title

Callback when reading the track title.

**Definition** mcc.h:530

[bt\_mcc\_cb::read\_current\_track\_obj\_id](structbt__mcc__cb.md#a46bd2c23d92d8362cdf9ad4862b78407)

bt\_mcc\_read\_current\_track\_obj\_id\_cb read\_current\_track\_obj\_id

Callback when reading the current track object ID.

**Definition** mcc.h:560

[bt\_mcc\_cb::read\_playback\_speed](structbt__mcc__cb.md#a47f8d92b18b0e4ffb3aacde05e7cb410)

bt\_mcc\_read\_playback\_speed\_cb read\_playback\_speed

Callback when reading the playback speed.

**Definition** mcc.h:546

[bt\_mcc\_cb::set\_next\_track\_obj\_id](structbt__mcc__cb.md#a4f2ea54d6c60beb28feab7b6453aec7c)

bt\_mcc\_set\_next\_track\_obj\_id\_cb set\_next\_track\_obj\_id

Callback when setting the next track object ID.

**Definition** mcc.h:566

[bt\_mcc\_cb::otc\_next\_track\_object](structbt__mcc__cb.md#a52724924ab19f59cc936344ebe13d437)

bt\_mcc\_otc\_read\_next\_track\_object\_cb otc\_next\_track\_object

Callback when reading the next track object.

**Definition** mcc.h:624

[bt\_mcc\_cb::read\_next\_track\_obj\_id](structbt__mcc__cb.md#a540797123f8968b49a6e98b30ea534c8)

bt\_mcc\_read\_next\_track\_obj\_id\_cb read\_next\_track\_obj\_id

Callback when reading the next track object ID.

**Definition** mcc.h:564

[bt\_mcc\_cb::set\_playback\_speed](structbt__mcc__cb.md#a5f87b5d07241b4124911be0cd6c43b37)

bt\_mcc\_set\_playback\_speed\_cb set\_playback\_speed

Callback when setting the playback speed.

**Definition** mcc.h:550

[bt\_mcc\_cb::read\_seeking\_speed](structbt__mcc__cb.md#a75c8e63baf45a119e9007f246362ab8d)

bt\_mcc\_read\_seeking\_speed\_cb read\_seeking\_speed

Callback when reading the seeking speed.

**Definition** mcc.h:554

[bt\_mcc\_cb::read\_segments\_obj\_id](structbt__mcc__cb.md#a810ceaee44fcbdec90a1ee227b6974df)

bt\_mcc\_read\_segments\_obj\_id\_cb read\_segments\_obj\_id

Callback when reading the segments object ID.

**Definition** mcc.h:558

[bt\_mcc\_cb::cmd\_ntf](structbt__mcc__cb.md#a835f60ad32edc4311a624e779972f0d5)

bt\_mcc\_cmd\_ntf\_cb cmd\_ntf

Callback command notifications.

**Definition** mcc.h:595

[bt\_mcc\_cb::read\_track\_duration](structbt__mcc__cb.md#a85268d9ce708aef01aa528aaedf0f7e0)

bt\_mcc\_read\_track\_duration\_cb read\_track\_duration

Callback when reading the track duration.

**Definition** mcc.h:534

[bt\_mcc\_cb::otc\_parent\_group\_object](structbt__mcc__cb.md#a872d0322ba3889f1f7d32e8966b53624)

bt\_mcc\_otc\_read\_parent\_group\_object\_cb otc\_parent\_group\_object

Callback when reading the parent group object.

**Definition** mcc.h:628

[bt\_mcc\_cb::read\_parent\_group\_obj\_id](structbt__mcc__cb.md#a87583247634728d3d9af7eb411d088a7)

bt\_mcc\_read\_parent\_group\_obj\_id\_cb read\_parent\_group\_obj\_id

Callback when reading the parent group object ID.

**Definition** mcc.h:572

[bt\_mcc\_cb::read\_icon\_url](structbt__mcc__cb.md#a8c7b5954e286d074a94a39bee266082c)

bt\_mcc\_read\_icon\_url\_cb read\_icon\_url

Callback when reading the icon URL.

**Definition** mcc.h:524

[bt\_mcc\_cb::send\_cmd](structbt__mcc__cb.md#a90e62e90752087da36122a65f6c9ed4e)

bt\_mcc\_send\_cmd\_cb send\_cmd

Callback when sending a command.

**Definition** mcc.h:592

[bt\_mcc\_cb::read\_playing\_orders\_supported](structbt__mcc__cb.md#a929d7b8fc925961048d5ff5e70a5126e)

bt\_mcc\_read\_playing\_orders\_supported\_cb read\_playing\_orders\_supported

Callback when reading the supported playing orders.

**Definition** mcc.h:584

[bt\_mcc\_cb::search\_ntf](structbt__mcc__cb.md#a9f7f3424aa230a8752f40a40b82b0b66)

bt\_mcc\_search\_ntf\_cb search\_ntf

Callback when receiving a search notification.

**Definition** mcc.h:604

[bt\_mcc\_cb::read\_search\_results\_obj\_id](structbt__mcc__cb.md#aaa2bdfb99e5cd7c2a0d0c800533e8491)

bt\_mcc\_read\_search\_results\_obj\_id\_cb read\_search\_results\_obj\_id

Callback when reading the search results object ID.

**Definition** mcc.h:606

[bt\_mcc\_cb::track\_changed\_ntf](structbt__mcc__cb.md#abb7769b73564a22645bfe6b11f239637)

bt\_mcc\_track\_changed\_ntf\_cb track\_changed\_ntf

Callback when getting a track changed notification.

**Definition** mcc.h:527

[bt\_mcc\_cb::otc\_current\_group\_object](structbt__mcc__cb.md#ac0e382f1117f983e7a2178fde274d460)

bt\_mcc\_otc\_read\_current\_group\_object\_cb otc\_current\_group\_object

Callback when reading the current group object.

**Definition** mcc.h:626

[bt\_mcc\_cb::set\_current\_track\_obj\_id](structbt__mcc__cb.md#ac9e182bbdd9671c5caee5bcd42198d90)

bt\_mcc\_set\_current\_track\_obj\_id\_cb set\_current\_track\_obj\_id

Callback when setting the current track object ID.

**Definition** mcc.h:562

[bt\_mcc\_cb::otc\_current\_track\_object](structbt__mcc__cb.md#ad13669e60992a1a407534f387efd1da8)

bt\_mcc\_otc\_read\_current\_track\_object\_cb otc\_current\_track\_object

Callback when reading the current track object.

**Definition** mcc.h:622

[bt\_mcc\_cb::read\_track\_position](structbt__mcc__cb.md#ad1636e717ef5039586b7a1462041e888)

bt\_mcc\_read\_track\_position\_cb read\_track\_position

Callback when reading the track position.

**Definition** mcc.h:538

[bt\_mcc\_cb::read\_opcodes\_supported](structbt__mcc__cb.md#ad7ddcae67bf71030ac2d8438ac2e863f)

bt\_mcc\_read\_opcodes\_supported\_cb read\_opcodes\_supported

Callback when reading the supported opcodes.

**Definition** mcc.h:598

[bt\_mcc\_cb::set\_current\_group\_obj\_id](structbt__mcc__cb.md#ad8d3eff0cc183797280c9f668a840add)

bt\_mcc\_set\_current\_group\_obj\_id\_cb set\_current\_group\_obj\_id

Callback when setting the current group object ID.

**Definition** mcc.h:570

[bt\_mcc\_cb::read\_content\_control\_id](structbt__mcc__cb.md#ae4d0e2e4df695352e8d2ed76db1f420e)

bt\_mcc\_read\_content\_control\_id\_cb read\_content\_control\_id

Callback when reading the content control ID.

**Definition** mcc.h:610

[bt\_mcc\_cb::read\_player\_name](structbt__mcc__cb.md#aeea1ef17b3b1e24c965d71f210952079)

bt\_mcc\_read\_player\_name\_cb read\_player\_name

Callback when reading the player name.

**Definition** mcc.h:517

[bt\_mcc\_cb::otc\_obj\_metadata](structbt__mcc__cb.md#af1c9664a2459550af0a6ed611fd17263)

bt\_mcc\_otc\_obj\_metadata\_cb otc\_obj\_metadata

Callback when receiving the current object metadata.

**Definition** mcc.h:616

[bt\_mcc\_cb::set\_track\_position](structbt__mcc__cb.md#affa57da8f325dce8298d097af38d0d62)

bt\_mcc\_set\_track\_position\_cb set\_track\_position

Callback when setting the track position.

**Definition** mcc.h:542

[bt\_ots\_client](structbt__ots__client.md)

OTS client instance.

**Definition** ots.h:819

[mpl\_cmd\_ntf](structmpl__cmd__ntf.md)

Media command notification.

**Definition** media\_proxy.h:73

[mpl\_cmd](structmpl__cmd.md)

Media player command.

**Definition** media\_proxy.h:61

[mpl\_search](structmpl__search.md)

Search.

**Definition** media\_proxy.h:92

[mpl\_search::search](structmpl__search.md#aa2332c1802786e2ef0486ede1c3a24c7)

char search[64]

Concatenated search control items - (type, length, param).

**Definition** media\_proxy.h:96

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [mcc.h](mcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
