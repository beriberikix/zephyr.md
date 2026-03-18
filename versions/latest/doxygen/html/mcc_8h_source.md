---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mcc_8h_source.html
original_path: doxygen/html/mcc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcc.h

[Go to the documentation of this file.](mcc_8h.md)

1

14

15/\*

16 \* Copyright (c) 2019 - 2021 Nordic Semiconductor ASA

17 \*

18 \* SPDX-License-Identifier: Apache-2.0

19 \*/

20

21#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCC\_

22#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCC\_

23

24#include <[stdint.h](stdint_8h.md)>

25

26#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

27#include <[zephyr/net/buf.h](net_2buf_8h.md)>

28#include <[zephyr/bluetooth/audio/media\_proxy.h](media__proxy_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34/\*\*\*\* Callback functions \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

35

[ 44](group__bt__gatt__mcc.md#gab268faeca207e115ee1be0843ab8c342)typedef void (\*[bt\_mcc\_discover\_mcs\_cb](group__bt__gatt__mcc.md#gab268faeca207e115ee1be0843ab8c342))(struct bt\_conn \*conn, int err);

45

[ 55](group__bt__gatt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f)typedef void (\*[bt\_mcc\_read\_player\_name\_cb](group__bt__gatt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f))(struct bt\_conn \*conn, int err, const char \*name);

56

[ 66](group__bt__gatt__mcc.md#ga471d0491b70e5472e16c3035507761cc)typedef void (\*[bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__gatt__mcc.md#ga471d0491b70e5472e16c3035507761cc))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) icon\_id);

67

[ 77](group__bt__gatt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0)typedef void (\*[bt\_mcc\_read\_icon\_url\_cb](group__bt__gatt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0))(struct bt\_conn \*conn, int err, const char \*icon\_url);

78

[ 90](group__bt__gatt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688)typedef void (\*[bt\_mcc\_track\_changed\_ntf\_cb](group__bt__gatt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688))(struct bt\_conn \*conn, int err);

91

92

[ 102](group__bt__gatt__mcc.md#ga6927860f1803aeade4994610da32d402)typedef void (\*[bt\_mcc\_read\_track\_title\_cb](group__bt__gatt__mcc.md#ga6927860f1803aeade4994610da32d402))(struct bt\_conn \*conn, int err, const char \*title);

103

[ 113](group__bt__gatt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c)typedef void (\*[bt\_mcc\_read\_track\_duration\_cb](group__bt__gatt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c))(struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) dur);

114

[ 124](group__bt__gatt__mcc.md#ga128883c867b10e57d3f2f26a708b7263)typedef void (\*[bt\_mcc\_read\_track\_position\_cb](group__bt__gatt__mcc.md#ga128883c867b10e57d3f2f26a708b7263))(struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos);

125

[ 135](group__bt__gatt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff)typedef void (\*[bt\_mcc\_set\_track\_position\_cb](group__bt__gatt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff))(struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos);

136

[ 146](group__bt__gatt__mcc.md#ga6f5383be3f344c25361786d903640909)typedef void (\*[bt\_mcc\_read\_playback\_speed\_cb](group__bt__gatt__mcc.md#ga6f5383be3f344c25361786d903640909))(struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

147

[ 157](group__bt__gatt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779)typedef void (\*[bt\_mcc\_set\_playback\_speed\_cb](group__bt__gatt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779))(struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

158

[ 168](group__bt__gatt__mcc.md#ga3089e6165e8491325f7205279bb5bb83)typedef void (\*[bt\_mcc\_read\_seeking\_speed\_cb](group__bt__gatt__mcc.md#ga3089e6165e8491325f7205279bb5bb83))(struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

169

[ 179](group__bt__gatt__mcc.md#ga1fbf0b4fd624626127774d2662083875)typedef void (\*[bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__gatt__mcc.md#ga1fbf0b4fd624626127774d2662083875))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

180

[ 190](group__bt__gatt__mcc.md#ga28ac116604248643b0b203b4a314b7b1)typedef void (\*[bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga28ac116604248643b0b203b4a314b7b1))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

191

[ 201](group__bt__gatt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529)typedef void (\*[bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

202

[ 212](group__bt__gatt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2)typedef void (\*[bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

213

[ 223](group__bt__gatt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def)typedef void (\*[bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

224

[ 234](group__bt__gatt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4)typedef void (\*[bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

235

[ 245](group__bt__gatt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723)typedef void (\*[bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

246

[ 256](group__bt__gatt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)typedef void (\*[bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c))(struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id);

257

[ 267](group__bt__gatt__mcc.md#gafb0869e0ef5332d39070081efdacf17c)typedef void (\*[bt\_mcc\_read\_playing\_order\_cb](group__bt__gatt__mcc.md#gafb0869e0ef5332d39070081efdacf17c))(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

268

[ 278](group__bt__gatt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7)typedef void (\*[bt\_mcc\_set\_playing\_order\_cb](group__bt__gatt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7))(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

279

[ 289](group__bt__gatt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0)typedef void (\*[bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__gatt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0))(struct bt\_conn \*conn, int err,

290 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) orders);

291

[ 301](group__bt__gatt__mcc.md#ga200a827f4bf5d65570ddabd028269f77)typedef void (\*[bt\_mcc\_read\_media\_state\_cb](group__bt__gatt__mcc.md#ga200a827f4bf5d65570ddabd028269f77))(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

302

[ 312](group__bt__gatt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e)typedef void (\*[bt\_mcc\_send\_cmd\_cb](group__bt__gatt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e))(struct bt\_conn \*conn, int err, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

313

[ 327](group__bt__gatt__mcc.md#ga50da90a5c351c99494208b44096a61c8)typedef void (\*[bt\_mcc\_cmd\_ntf\_cb](group__bt__gatt__mcc.md#ga50da90a5c351c99494208b44096a61c8))(struct bt\_conn \*conn, int err, const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*ntf);

328

[ 338](group__bt__gatt__mcc.md#gab37df36e15132b9235d1093f5aa403cc)typedef void (\*[bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__gatt__mcc.md#gab37df36e15132b9235d1093f5aa403cc))(struct bt\_conn \*conn, int err,

339 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes);

340

[ 350](group__bt__gatt__mcc.md#ga9489c34b6006df8bd26e626030cab71f)typedef void (\*[bt\_mcc\_send\_search\_cb](group__bt__gatt__mcc.md#ga9489c34b6006df8bd26e626030cab71f))(struct bt\_conn \*conn, int err,

351 const struct [mpl\_search](structmpl__search.md) \*[search](structmpl__search.md#aa2332c1802786e2ef0486ede1c3a24c7));

352

[ 366](group__bt__gatt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3)typedef void (\*[bt\_mcc\_search\_ntf\_cb](group__bt__gatt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3))(struct bt\_conn \*conn, int err,

367 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code);

368

[ 382](group__bt__gatt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926)typedef void (\*[bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__gatt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926))(struct bt\_conn \*conn,

383 int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

384

[ 394](group__bt__gatt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927)typedef void (\*[bt\_mcc\_read\_content\_control\_id\_cb](group__bt__gatt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927))(struct bt\_conn \*conn,

395 int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid);

396

397/\*\*\*\* Callback functions for the included Object Transfer service \*\*\*\*\*\*\*\*\*\*\*\*\*/

398

[ 407](group__bt__gatt__mcc.md#gaf186e6adefa296de4146502665d738b3)typedef void (\*[bt\_mcc\_otc\_obj\_selected\_cb](group__bt__gatt__mcc.md#gaf186e6adefa296de4146502665d738b3))(struct bt\_conn \*conn, int err);

408

[ 417](group__bt__gatt__mcc.md#ga9805222315ca6e6df0720233055af10c)typedef void (\*[bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__gatt__mcc.md#ga9805222315ca6e6df0720233055af10c))(struct bt\_conn \*conn, int err);

418

[ 430](group__bt__gatt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870)typedef void (\*[bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__gatt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870))(struct bt\_conn \*conn, int err,

431 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

432

[ 444](group__bt__gatt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8)typedef void (\*[bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__gatt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8))(struct bt\_conn \*conn, int err,

445 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

446

[ 458](group__bt__gatt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe)typedef void (\*[bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__gatt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe))(struct bt\_conn \*conn, int err,

459 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

460

[ 472](group__bt__gatt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5)typedef void (\*[bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__gatt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5))(struct bt\_conn \*conn, int err,

473 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

474

[ 486](group__bt__gatt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48)typedef void (\*[bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__gatt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48))(struct bt\_conn \*conn, int err,

487 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

488

[ 500](group__bt__gatt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50)typedef void (\*[bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__gatt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50))(struct bt\_conn \*conn, int err,

501 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

502

503

[ 507](structbt__mcc__cb.md)struct [bt\_mcc\_cb](structbt__mcc__cb.md) {

[ 508](structbt__mcc__cb.md#a2f48a0e0b891131347b0ddc2cb5a8ba7) [bt\_mcc\_discover\_mcs\_cb](group__bt__gatt__mcc.md#gab268faeca207e115ee1be0843ab8c342) [discover\_mcs](structbt__mcc__cb.md#a2f48a0e0b891131347b0ddc2cb5a8ba7);

[ 509](structbt__mcc__cb.md#aeea1ef17b3b1e24c965d71f210952079) [bt\_mcc\_read\_player\_name\_cb](group__bt__gatt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f) [read\_player\_name](structbt__mcc__cb.md#aeea1ef17b3b1e24c965d71f210952079);

510#ifdef CONFIG\_BT\_OTS\_CLIENT

511 [bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__gatt__mcc.md#ga471d0491b70e5472e16c3035507761cc) read\_icon\_obj\_id;

512#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

513#if defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_PLAYER\_ICON\_URL)

514 [bt\_mcc\_read\_icon\_url\_cb](group__bt__gatt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0) read\_icon\_url;

515#endif /\* defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_PLAYER\_ICON\_URL) \*/

[ 516](structbt__mcc__cb.md#abb7769b73564a22645bfe6b11f239637) [bt\_mcc\_track\_changed\_ntf\_cb](group__bt__gatt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688) [track\_changed\_ntf](structbt__mcc__cb.md#abb7769b73564a22645bfe6b11f239637);

517#if defined(CONFIG\_BT\_MCC\_READ\_TRACK\_TITLE)

518 [bt\_mcc\_read\_track\_title\_cb](group__bt__gatt__mcc.md#ga6927860f1803aeade4994610da32d402) read\_track\_title;

519#endif /\* defined(CONFIG\_BT\_MCC\_READ\_TRACK\_TITLE) \*/

520#if defined(CONFIG\_BT\_MCC\_READ\_TRACK\_DURATION)

521 [bt\_mcc\_read\_track\_duration\_cb](group__bt__gatt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c) read\_track\_duration;

522#endif /\* defined(CONFIG\_BT\_MCC\_READ\_TRACK\_DURATION) \*/

523#if defined(CONFIG\_BT\_MCC\_READ\_TRACK\_POSITION)

524 [bt\_mcc\_read\_track\_position\_cb](group__bt__gatt__mcc.md#ga128883c867b10e57d3f2f26a708b7263) read\_track\_position;

525#endif /\* defined(CONFIG\_BT\_MCC\_READ\_TRACK\_POSITION) \*/

526#if defined(CONFIG\_BT\_MCC\_SET\_TRACK\_POSITION)

527 [bt\_mcc\_set\_track\_position\_cb](group__bt__gatt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff) set\_track\_position;

528#endif /\* defined(CONFIG\_BT\_MCC\_SET\_TRACK\_POSITION) \*/

529#if defined(CONFIG\_BT\_MCC\_READ\_PLAYBACK\_SPEED)

530 [bt\_mcc\_read\_playback\_speed\_cb](group__bt__gatt__mcc.md#ga6f5383be3f344c25361786d903640909) read\_playback\_speed;

531#endif /\* defined (CONFIG\_BT\_MCC\_READ\_PLAYBACK\_SPEED) \*/

532#if defined(CONFIG\_BT\_MCC\_SET\_PLAYBACK\_SPEED)

533 [bt\_mcc\_set\_playback\_speed\_cb](group__bt__gatt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779) set\_playback\_speed;

534#endif /\* defined (CONFIG\_BT\_MCC\_SET\_PLAYBACK\_SPEED) \*/

535#if defined(CONFIG\_BT\_MCC\_READ\_SEEKING\_SPEED)

536 [bt\_mcc\_read\_seeking\_speed\_cb](group__bt__gatt__mcc.md#ga3089e6165e8491325f7205279bb5bb83) read\_seeking\_speed;

537#endif /\* defined (CONFIG\_BT\_MCC\_READ\_SEEKING\_SPEED) \*/

538#ifdef CONFIG\_BT\_OTS\_CLIENT

539 [bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__gatt__mcc.md#ga1fbf0b4fd624626127774d2662083875) read\_segments\_obj\_id;

540 [bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga28ac116604248643b0b203b4a314b7b1) read\_current\_track\_obj\_id;

541 [bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529) set\_current\_track\_obj\_id;

542 [bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2) read\_next\_track\_obj\_id;

543 [bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def) set\_next\_track\_obj\_id;

544 [bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723) read\_current\_group\_obj\_id;

545 [bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c) set\_current\_group\_obj\_id;

546 [bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4) read\_parent\_group\_obj\_id;

547#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

548#if defined(CONFIG\_BT\_MCC\_READ\_PLAYING\_ORDER)

549 [bt\_mcc\_read\_playing\_order\_cb](group__bt__gatt__mcc.md#gafb0869e0ef5332d39070081efdacf17c) read\_playing\_order;

550#endif /\* defined(CONFIG\_BT\_MCC\_READ\_PLAYING\_ORDER) \*/

551#if defined(CONFIG\_BT\_MCC\_SET\_PLAYING\_ORDER)

552 [bt\_mcc\_set\_playing\_order\_cb](group__bt__gatt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7) set\_playing\_order;

553#endif /\* defined(CONFIG\_BT\_MCC\_SET\_PLAYING\_ORDER) \*/

554#if defined(CONFIG\_BT\_MCC\_READ\_PLAYING\_ORDER\_SUPPORTED)

555 [bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__gatt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0) read\_playing\_orders\_supported;

556#endif /\* defined(CONFIG\_BT\_MCC\_READ\_PLAYING\_ORDER\_SUPPORTED) \*/

557#if defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_STATE)

558 [bt\_mcc\_read\_media\_state\_cb](group__bt__gatt__mcc.md#ga200a827f4bf5d65570ddabd028269f77) read\_media\_state;

559#endif /\* defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_STATE) \*/

560#if defined(CONFIG\_BT\_MCC\_SET\_MEDIA\_CONTROL\_POINT)

561 [bt\_mcc\_send\_cmd\_cb](group__bt__gatt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e) send\_cmd;

562#endif /\* defined(CONFIG\_BT\_MCC\_SET\_MEDIA\_CONTROL\_POINT) \*/

[ 563](structbt__mcc__cb.md#a835f60ad32edc4311a624e779972f0d5) [bt\_mcc\_cmd\_ntf\_cb](group__bt__gatt__mcc.md#ga50da90a5c351c99494208b44096a61c8) [cmd\_ntf](structbt__mcc__cb.md#a835f60ad32edc4311a624e779972f0d5);

564#if defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_CONTROL\_POINT\_OPCODES\_SUPPORTED)

565 [bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__gatt__mcc.md#gab37df36e15132b9235d1093f5aa403cc) read\_opcodes\_supported;

566#endif /\* defined(CONFIG\_BT\_MCC\_READ\_MEDIA\_CONTROL\_POINT\_OPCODES\_SUPPORTED) \*/

567#ifdef CONFIG\_BT\_OTS\_CLIENT

568 [bt\_mcc\_send\_search\_cb](group__bt__gatt__mcc.md#ga9489c34b6006df8bd26e626030cab71f) send\_search;

569 [bt\_mcc\_search\_ntf\_cb](group__bt__gatt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3) search\_ntf;

570 [bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__gatt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926) read\_search\_results\_obj\_id;

571#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

572#if defined(CONFIG\_BT\_MCC\_READ\_CONTENT\_CONTROL\_ID)

573 [bt\_mcc\_read\_content\_control\_id\_cb](group__bt__gatt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927) read\_content\_control\_id;

574#endif /\* defined(CONFIG\_BT\_MCC\_READ\_CONTENT\_CONTROL\_ID) \*/

575#ifdef CONFIG\_BT\_OTS\_CLIENT

576 [bt\_mcc\_otc\_obj\_selected\_cb](group__bt__gatt__mcc.md#gaf186e6adefa296de4146502665d738b3) otc\_obj\_selected;

577 [bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__gatt__mcc.md#ga9805222315ca6e6df0720233055af10c) otc\_obj\_metadata;

578 [bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__gatt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870) otc\_icon\_object;

579 [bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__gatt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8) otc\_track\_segments\_object;

580 [bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__gatt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe) otc\_current\_track\_object;

581 [bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__gatt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5) otc\_next\_track\_object;

582 [bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__gatt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50) otc\_current\_group\_object;

583 [bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__gatt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48) otc\_parent\_group\_object;

584#endif /\* CONFIG\_BT\_OTS\_CLIENT \*/

585};

586

587/\*\*\*\* Functions \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

588

[ 596](group__bt__gatt__mcc.md#ga94de08bb0a1e1324600e4957b648e92b)int [bt\_mcc\_init](group__bt__gatt__mcc.md#ga94de08bb0a1e1324600e4957b648e92b)(struct [bt\_mcc\_cb](structbt__mcc__cb.md) \*cb);

597

598

[ 613](group__bt__gatt__mcc.md#gaa1f9ead03b4cccaff1e3390b8052b0f3)int [bt\_mcc\_discover\_mcs](group__bt__gatt__mcc.md#gaa1f9ead03b4cccaff1e3390b8052b0f3)(struct bt\_conn \*conn, bool subscribe);

614

[ 622](group__bt__gatt__mcc.md#ga724ce71fc88f1ca4bcf209c92c177f36)int [bt\_mcc\_read\_player\_name](group__bt__gatt__mcc.md#ga724ce71fc88f1ca4bcf209c92c177f36)(struct bt\_conn \*conn);

623

[ 631](group__bt__gatt__mcc.md#ga0e69de33c37957a2b5473df7d3c3f389)int [bt\_mcc\_read\_icon\_obj\_id](group__bt__gatt__mcc.md#ga0e69de33c37957a2b5473df7d3c3f389)(struct bt\_conn \*conn);

632

[ 640](group__bt__gatt__mcc.md#ga38733456db6bc6558a511e104577c9c9)int [bt\_mcc\_read\_icon\_url](group__bt__gatt__mcc.md#ga38733456db6bc6558a511e104577c9c9)(struct bt\_conn \*conn);

641

[ 649](group__bt__gatt__mcc.md#ga7dfa14489a4cea4b00053c9aa75cf373)int [bt\_mcc\_read\_track\_title](group__bt__gatt__mcc.md#ga7dfa14489a4cea4b00053c9aa75cf373)(struct bt\_conn \*conn);

650

[ 658](group__bt__gatt__mcc.md#ga50a45f043bd2ae1741a120e02e9dc2f5)int [bt\_mcc\_read\_track\_duration](group__bt__gatt__mcc.md#ga50a45f043bd2ae1741a120e02e9dc2f5)(struct bt\_conn \*conn);

659

[ 667](group__bt__gatt__mcc.md#gaf143098f5dfcfba01df3d6f06472779e)int [bt\_mcc\_read\_track\_position](group__bt__gatt__mcc.md#gaf143098f5dfcfba01df3d6f06472779e)(struct bt\_conn \*conn);

668

[ 677](group__bt__gatt__mcc.md#gad324366d33bef6b1ed1c8fc881bf44cf)int [bt\_mcc\_set\_track\_position](group__bt__gatt__mcc.md#gad324366d33bef6b1ed1c8fc881bf44cf)(struct bt\_conn \*conn, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos);

678

[ 686](group__bt__gatt__mcc.md#gaa566a4c42f0ab0ab6feddf4e25845609)int [bt\_mcc\_read\_playback\_speed](group__bt__gatt__mcc.md#gaa566a4c42f0ab0ab6feddf4e25845609)(struct bt\_conn \*conn);

687

[ 696](group__bt__gatt__mcc.md#ga1382e5b6000896dc94f6489909301719)int [bt\_mcc\_set\_playback\_speed](group__bt__gatt__mcc.md#ga1382e5b6000896dc94f6489909301719)(struct bt\_conn \*conn, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed);

697

[ 705](group__bt__gatt__mcc.md#ga366fdfaa23cef9f1c3ba7ddd36a67658)int [bt\_mcc\_read\_seeking\_speed](group__bt__gatt__mcc.md#ga366fdfaa23cef9f1c3ba7ddd36a67658)(struct bt\_conn \*conn);

706

[ 714](group__bt__gatt__mcc.md#ga4cb0a95e91d3ec00ede64663a2b932f0)int [bt\_mcc\_read\_segments\_obj\_id](group__bt__gatt__mcc.md#ga4cb0a95e91d3ec00ede64663a2b932f0)(struct bt\_conn \*conn);

715

[ 723](group__bt__gatt__mcc.md#ga5b3a8fb8e8251cf005b34e47619ae7b9)int [bt\_mcc\_read\_current\_track\_obj\_id](group__bt__gatt__mcc.md#ga5b3a8fb8e8251cf005b34e47619ae7b9)(struct bt\_conn \*conn);

724

[ 735](group__bt__gatt__mcc.md#ga8374ac230c5fe6b5a1bb7fa873fdeb49)int [bt\_mcc\_set\_current\_track\_obj\_id](group__bt__gatt__mcc.md#ga8374ac230c5fe6b5a1bb7fa873fdeb49)(struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

736

[ 744](group__bt__gatt__mcc.md#ga11e4c02ba0b1fbc197aaf071b82a1eed)int [bt\_mcc\_read\_next\_track\_obj\_id](group__bt__gatt__mcc.md#ga11e4c02ba0b1fbc197aaf071b82a1eed)(struct bt\_conn \*conn);

745

[ 756](group__bt__gatt__mcc.md#gafeebcbb0c77d5d4acbe151fd9888d084)int [bt\_mcc\_set\_next\_track\_obj\_id](group__bt__gatt__mcc.md#gafeebcbb0c77d5d4acbe151fd9888d084)(struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

757

[ 765](group__bt__gatt__mcc.md#ga8cb43a6947df48113b082d8cc8ccf25c)int [bt\_mcc\_read\_current\_group\_obj\_id](group__bt__gatt__mcc.md#ga8cb43a6947df48113b082d8cc8ccf25c)(struct bt\_conn \*conn);

766

[ 777](group__bt__gatt__mcc.md#gae3f385811f852d584595c6e531556aed)int [bt\_mcc\_set\_current\_group\_obj\_id](group__bt__gatt__mcc.md#gae3f385811f852d584595c6e531556aed)(struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id);

778

[ 786](group__bt__gatt__mcc.md#ga3ccd5961cc4c8d82fa988d300e12e1ae)int [bt\_mcc\_read\_parent\_group\_obj\_id](group__bt__gatt__mcc.md#ga3ccd5961cc4c8d82fa988d300e12e1ae)(struct bt\_conn \*conn);

787

[ 795](group__bt__gatt__mcc.md#ga077a134ff1404fb76aa756a5531fd1d7)int [bt\_mcc\_read\_playing\_order](group__bt__gatt__mcc.md#ga077a134ff1404fb76aa756a5531fd1d7)(struct bt\_conn \*conn);

796

[ 805](group__bt__gatt__mcc.md#ga05295649385c3a337401765627d09553)int [bt\_mcc\_set\_playing\_order](group__bt__gatt__mcc.md#ga05295649385c3a337401765627d09553)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order);

806

[ 814](group__bt__gatt__mcc.md#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)int [bt\_mcc\_read\_playing\_orders\_supported](group__bt__gatt__mcc.md#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)(struct bt\_conn \*conn);

815

[ 823](group__bt__gatt__mcc.md#gac1b440cfa54dd4b6e23bb47bf885f88d)int [bt\_mcc\_read\_media\_state](group__bt__gatt__mcc.md#gac1b440cfa54dd4b6e23bb47bf885f88d)(struct bt\_conn \*conn);

824

[ 835](group__bt__gatt__mcc.md#ga3f4a538bcf436e4e80b73ed6e077dfa0)int [bt\_mcc\_send\_cmd](group__bt__gatt__mcc.md#ga3f4a538bcf436e4e80b73ed6e077dfa0)(struct bt\_conn \*conn, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

836

[ 844](group__bt__gatt__mcc.md#ga692160554947f92e8c81912c5e597086)int [bt\_mcc\_read\_opcodes\_supported](group__bt__gatt__mcc.md#ga692160554947f92e8c81912c5e597086)(struct bt\_conn \*conn);

845

[ 856](group__bt__gatt__mcc.md#ga324161056e03195820bbd7cc77ff287d)int [bt\_mcc\_send\_search](group__bt__gatt__mcc.md#ga324161056e03195820bbd7cc77ff287d)(struct bt\_conn \*conn, const struct [mpl\_search](structmpl__search.md) \*search);

857

[ 865](group__bt__gatt__mcc.md#ga98814a516a027bdaa3250e93d55309fd)int [bt\_mcc\_read\_search\_results\_obj\_id](group__bt__gatt__mcc.md#ga98814a516a027bdaa3250e93d55309fd)(struct bt\_conn \*conn);

866

[ 874](group__bt__gatt__mcc.md#ga77cbf810c35d1a17efce1fae6a941963)int [bt\_mcc\_read\_content\_control\_id](group__bt__gatt__mcc.md#ga77cbf810c35d1a17efce1fae6a941963)(struct bt\_conn \*conn);

875

[ 883](group__bt__gatt__mcc.md#gadf687cb26a6d00bca73e273da583df88)int [bt\_mcc\_otc\_read\_object\_metadata](group__bt__gatt__mcc.md#gadf687cb26a6d00bca73e273da583df88)(struct bt\_conn \*conn);

884

[ 892](group__bt__gatt__mcc.md#gaba527d8f0307ab11150a5434231c0e7e)int [bt\_mcc\_otc\_read\_icon\_object](group__bt__gatt__mcc.md#gaba527d8f0307ab11150a5434231c0e7e)(struct bt\_conn \*conn);

893

[ 901](group__bt__gatt__mcc.md#gac22e840b65895aa018ab1b4535a87672)int [bt\_mcc\_otc\_read\_track\_segments\_object](group__bt__gatt__mcc.md#gac22e840b65895aa018ab1b4535a87672)(struct bt\_conn \*conn);

902

[ 910](group__bt__gatt__mcc.md#gac4b09a77df52d2681e7652591ca32bf8)int [bt\_mcc\_otc\_read\_current\_track\_object](group__bt__gatt__mcc.md#gac4b09a77df52d2681e7652591ca32bf8)(struct bt\_conn \*conn);

911

[ 919](group__bt__gatt__mcc.md#ga611c9edebff5b4347ad1241ffd19f49e)int [bt\_mcc\_otc\_read\_next\_track\_object](group__bt__gatt__mcc.md#ga611c9edebff5b4347ad1241ffd19f49e)(struct bt\_conn \*conn);

920

[ 928](group__bt__gatt__mcc.md#ga4b1ebe682ad134795f8a1b494244f8b6)int [bt\_mcc\_otc\_read\_current\_group\_object](group__bt__gatt__mcc.md#ga4b1ebe682ad134795f8a1b494244f8b6)(struct bt\_conn \*conn);

929

[ 937](group__bt__gatt__mcc.md#gae001cb2d701457ce083aa8a0fd5ec518)int [bt\_mcc\_otc\_read\_parent\_group\_object](group__bt__gatt__mcc.md#gae001cb2d701457ce083aa8a0fd5ec518)(struct bt\_conn \*conn);

938

[ 947](group__bt__gatt__mcc.md#gaa243806f65c4a37d41f25bcc4f1839fc)struct [bt\_ots\_client](structbt__ots__client.md) \*[bt\_mcc\_otc\_inst](group__bt__gatt__mcc.md#gaa243806f65c4a37d41f25bcc4f1839fc)(struct bt\_conn \*conn);

948

949#ifdef \_\_cplusplus

950}

951#endif

952

956

957#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCC\_\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_mcc\_set\_playing\_order](group__bt__gatt__mcc.md#ga05295649385c3a337401765627d09553)

int bt\_mcc\_set\_playing\_order(struct bt\_conn \*conn, uint8\_t order)

Set Playing Order.

[bt\_mcc\_read\_playing\_order](group__bt__gatt__mcc.md#ga077a134ff1404fb76aa756a5531fd1d7)

int bt\_mcc\_read\_playing\_order(struct bt\_conn \*conn)

Read Playing Order.

[bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__gatt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50)

void(\* bt\_mcc\_otc\_read\_current\_group\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_current\_group\_object().

**Definition** mcc.h:500

[bt\_mcc\_read\_icon\_obj\_id](group__bt__gatt__mcc.md#ga0e69de33c37957a2b5473df7d3c3f389)

int bt\_mcc\_read\_icon\_obj\_id(struct bt\_conn \*conn)

Read Icon Object ID.

[bt\_mcc\_set\_track\_position\_cb](group__bt__gatt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff)

void(\* bt\_mcc\_set\_track\_position\_cb)(struct bt\_conn \*conn, int err, int32\_t pos)

Callback function for bt\_mcc\_set\_track\_position().

**Definition** mcc.h:135

[bt\_mcc\_read\_next\_track\_obj\_id](group__bt__gatt__mcc.md#ga11e4c02ba0b1fbc197aaf071b82a1eed)

int bt\_mcc\_read\_next\_track\_obj\_id(struct bt\_conn \*conn)

Read Next Track Object ID.

[bt\_mcc\_read\_track\_position\_cb](group__bt__gatt__mcc.md#ga128883c867b10e57d3f2f26a708b7263)

void(\* bt\_mcc\_read\_track\_position\_cb)(struct bt\_conn \*conn, int err, int32\_t pos)

Callback function for bt\_mcc\_read\_track\_position().

**Definition** mcc.h:124

[bt\_mcc\_set\_playback\_speed\_cb](group__bt__gatt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779)

void(\* bt\_mcc\_set\_playback\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)

Callback function for bt\_mcc\_set\_playback\_speed().

**Definition** mcc.h:157

[bt\_mcc\_set\_playback\_speed](group__bt__gatt__mcc.md#ga1382e5b6000896dc94f6489909301719)

int bt\_mcc\_set\_playback\_speed(struct bt\_conn \*conn, int8\_t speed)

Set Playback Speed.

[bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__gatt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870)

void(\* bt\_mcc\_otc\_read\_icon\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_icon\_object().

**Definition** mcc.h:430

[bt\_mcc\_set\_playing\_order\_cb](group__bt__gatt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7)

void(\* bt\_mcc\_set\_playing\_order\_cb)(struct bt\_conn \*conn, int err, uint8\_t order)

Callback function for bt\_mcc\_set\_playing\_order().

**Definition** mcc.h:278

[bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__gatt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8)

void(\* bt\_mcc\_otc\_read\_track\_segments\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_track\_segments\_object().

**Definition** mcc.h:444

[bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__gatt__mcc.md#ga1fbf0b4fd624626127774d2662083875)

void(\* bt\_mcc\_read\_segments\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_segments\_obj\_id().

**Definition** mcc.h:179

[bt\_mcc\_read\_media\_state\_cb](group__bt__gatt__mcc.md#ga200a827f4bf5d65570ddabd028269f77)

void(\* bt\_mcc\_read\_media\_state\_cb)(struct bt\_conn \*conn, int err, uint8\_t state)

Callback function for bt\_mcc\_read\_media\_state().

**Definition** mcc.h:301

[bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga28ac116604248643b0b203b4a314b7b1)

void(\* bt\_mcc\_read\_current\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_current\_track\_obj\_id().

**Definition** mcc.h:190

[bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def)

void(\* bt\_mcc\_set\_next\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_set\_next\_track\_obj\_id().

**Definition** mcc.h:223

[bt\_mcc\_read\_seeking\_speed\_cb](group__bt__gatt__mcc.md#ga3089e6165e8491325f7205279bb5bb83)

void(\* bt\_mcc\_read\_seeking\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)

Callback function for bt\_mcc\_read\_seeking\_speed().

**Definition** mcc.h:168

[bt\_mcc\_send\_search](group__bt__gatt__mcc.md#ga324161056e03195820bbd7cc77ff287d)

int bt\_mcc\_send\_search(struct bt\_conn \*conn, const struct mpl\_search \*search)

Send a Search command.

[bt\_mcc\_read\_seeking\_speed](group__bt__gatt__mcc.md#ga366fdfaa23cef9f1c3ba7ddd36a67658)

int bt\_mcc\_read\_seeking\_speed(struct bt\_conn \*conn)

Read Seeking speed.

[bt\_mcc\_read\_icon\_url](group__bt__gatt__mcc.md#ga38733456db6bc6558a511e104577c9c9)

int bt\_mcc\_read\_icon\_url(struct bt\_conn \*conn)

Read Icon Object URL.

[bt\_mcc\_read\_parent\_group\_obj\_id](group__bt__gatt__mcc.md#ga3ccd5961cc4c8d82fa988d300e12e1ae)

int bt\_mcc\_read\_parent\_group\_obj\_id(struct bt\_conn \*conn)

Read Parent Group Object ID.

[bt\_mcc\_send\_cmd](group__bt__gatt__mcc.md#ga3f4a538bcf436e4e80b73ed6e077dfa0)

int bt\_mcc\_send\_cmd(struct bt\_conn \*conn, const struct mpl\_cmd \*cmd)

Send a command.

[bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__gatt__mcc.md#ga471d0491b70e5472e16c3035507761cc)

void(\* bt\_mcc\_read\_icon\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t icon\_id)

Callback function for bt\_mcc\_read\_icon\_obj\_id().

**Definition** mcc.h:66

[bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4)

void(\* bt\_mcc\_read\_parent\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_parent\_group\_obj\_id().

**Definition** mcc.h:234

[bt\_mcc\_otc\_read\_current\_group\_object](group__bt__gatt__mcc.md#ga4b1ebe682ad134795f8a1b494244f8b6)

int bt\_mcc\_otc\_read\_current\_group\_object(struct bt\_conn \*conn)

Read the Current Group Object.

[bt\_mcc\_read\_segments\_obj\_id](group__bt__gatt__mcc.md#ga4cb0a95e91d3ec00ede64663a2b932f0)

int bt\_mcc\_read\_segments\_obj\_id(struct bt\_conn \*conn)

Read Track Segments Object ID.

[bt\_mcc\_read\_track\_duration](group__bt__gatt__mcc.md#ga50a45f043bd2ae1741a120e02e9dc2f5)

int bt\_mcc\_read\_track\_duration(struct bt\_conn \*conn)

Read Track Duration.

[bt\_mcc\_cmd\_ntf\_cb](group__bt__gatt__mcc.md#ga50da90a5c351c99494208b44096a61c8)

void(\* bt\_mcc\_cmd\_ntf\_cb)(struct bt\_conn \*conn, int err, const struct mpl\_cmd\_ntf \*ntf)

Callback function for command notifications.

**Definition** mcc.h:327

[bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__gatt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926)

void(\* bt\_mcc\_read\_search\_results\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_search\_results\_obj\_id().

**Definition** mcc.h:382

[bt\_mcc\_read\_current\_track\_obj\_id](group__bt__gatt__mcc.md#ga5b3a8fb8e8251cf005b34e47619ae7b9)

int bt\_mcc\_read\_current\_track\_obj\_id(struct bt\_conn \*conn)

Read Current Track Object ID.

[bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723)

void(\* bt\_mcc\_read\_current\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_current\_group\_obj\_id().

**Definition** mcc.h:245

[bt\_mcc\_otc\_read\_next\_track\_object](group__bt__gatt__mcc.md#ga611c9edebff5b4347ad1241ffd19f49e)

int bt\_mcc\_otc\_read\_next\_track\_object(struct bt\_conn \*conn)

Read the Next Track Object.

[bt\_mcc\_track\_changed\_ntf\_cb](group__bt__gatt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688)

void(\* bt\_mcc\_track\_changed\_ntf\_cb)(struct bt\_conn \*conn, int err)

Callback function for track changed notifications.

**Definition** mcc.h:90

[bt\_mcc\_read\_opcodes\_supported](group__bt__gatt__mcc.md#ga692160554947f92e8c81912c5e597086)

int bt\_mcc\_read\_opcodes\_supported(struct bt\_conn \*conn)

Read Opcodes Supported.

[bt\_mcc\_read\_track\_title\_cb](group__bt__gatt__mcc.md#ga6927860f1803aeade4994610da32d402)

void(\* bt\_mcc\_read\_track\_title\_cb)(struct bt\_conn \*conn, int err, const char \*title)

Callback function for bt\_mcc\_read\_track\_title().

**Definition** mcc.h:102

[bt\_mcc\_read\_playback\_speed\_cb](group__bt__gatt__mcc.md#ga6f5383be3f344c25361786d903640909)

void(\* bt\_mcc\_read\_playback\_speed\_cb)(struct bt\_conn \*conn, int err, int8\_t speed)

Callback function for bt\_mcc\_read\_playback\_speed().

**Definition** mcc.h:146

[bt\_mcc\_read\_player\_name](group__bt__gatt__mcc.md#ga724ce71fc88f1ca4bcf209c92c177f36)

int bt\_mcc\_read\_player\_name(struct bt\_conn \*conn)

Read Media Player Name.

[bt\_mcc\_read\_content\_control\_id](group__bt__gatt__mcc.md#ga77cbf810c35d1a17efce1fae6a941963)

int bt\_mcc\_read\_content\_control\_id(struct bt\_conn \*conn)

Read Content Control ID.

[bt\_mcc\_read\_track\_duration\_cb](group__bt__gatt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c)

void(\* bt\_mcc\_read\_track\_duration\_cb)(struct bt\_conn \*conn, int err, int32\_t dur)

Callback function for bt\_mcc\_read\_track\_duration().

**Definition** mcc.h:113

[bt\_mcc\_read\_track\_title](group__bt__gatt__mcc.md#ga7dfa14489a4cea4b00053c9aa75cf373)

int bt\_mcc\_read\_track\_title(struct bt\_conn \*conn)

Read Track Title.

[bt\_mcc\_set\_current\_track\_obj\_id](group__bt__gatt__mcc.md#ga8374ac230c5fe6b5a1bb7fa873fdeb49)

int bt\_mcc\_set\_current\_track\_obj\_id(struct bt\_conn \*conn, uint64\_t id)

Set Current Track Object ID.

[bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2)

void(\* bt\_mcc\_read\_next\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_read\_next\_track\_obj\_id\_obj().

**Definition** mcc.h:212

[bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__gatt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)

void(\* bt\_mcc\_set\_current\_group\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t obj\_id)

Callback function for bt\_mcc\_set\_current\_group\_obj\_id().

**Definition** mcc.h:256

[bt\_mcc\_read\_current\_group\_obj\_id](group__bt__gatt__mcc.md#ga8cb43a6947df48113b082d8cc8ccf25c)

int bt\_mcc\_read\_current\_group\_obj\_id(struct bt\_conn \*conn)

Read Current Group Object ID.

[bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__gatt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5)

void(\* bt\_mcc\_otc\_read\_next\_track\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_next\_track\_object().

**Definition** mcc.h:472

[bt\_mcc\_send\_search\_cb](group__bt__gatt__mcc.md#ga9489c34b6006df8bd26e626030cab71f)

void(\* bt\_mcc\_send\_search\_cb)(struct bt\_conn \*conn, int err, const struct mpl\_search \*search)

Callback function for bt\_mcc\_send\_search().

**Definition** mcc.h:350

[bt\_mcc\_init](group__bt__gatt__mcc.md#ga94de08bb0a1e1324600e4957b648e92b)

int bt\_mcc\_init(struct bt\_mcc\_cb \*cb)

Initialize Media Control Client.

[bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__gatt__mcc.md#ga9805222315ca6e6df0720233055af10c)

void(\* bt\_mcc\_otc\_obj\_metadata\_cb)(struct bt\_conn \*conn, int err)

Callback function for bt\_mcc\_otc\_read\_object\_meatadata().

**Definition** mcc.h:417

[bt\_mcc\_read\_search\_results\_obj\_id](group__bt__gatt__mcc.md#ga98814a516a027bdaa3250e93d55309fd)

int bt\_mcc\_read\_search\_results\_obj\_id(struct bt\_conn \*conn)

Search Results Group Object ID.

[bt\_mcc\_discover\_mcs](group__bt__gatt__mcc.md#gaa1f9ead03b4cccaff1e3390b8052b0f3)

int bt\_mcc\_discover\_mcs(struct bt\_conn \*conn, bool subscribe)

Discover Media Control Service.

[bt\_mcc\_otc\_inst](group__bt__gatt__mcc.md#gaa243806f65c4a37d41f25bcc4f1839fc)

struct bt\_ots\_client \* bt\_mcc\_otc\_inst(struct bt\_conn \*conn)

Look up MCC OTC instance.

[bt\_mcc\_read\_playback\_speed](group__bt__gatt__mcc.md#gaa566a4c42f0ab0ab6feddf4e25845609)

int bt\_mcc\_read\_playback\_speed(struct bt\_conn \*conn)

Read Playback speed.

[bt\_mcc\_read\_player\_name\_cb](group__bt__gatt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f)

void(\* bt\_mcc\_read\_player\_name\_cb)(struct bt\_conn \*conn, int err, const char \*name)

Callback function for bt\_mcc\_read\_player\_name().

**Definition** mcc.h:55

[bt\_mcc\_read\_icon\_url\_cb](group__bt__gatt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0)

void(\* bt\_mcc\_read\_icon\_url\_cb)(struct bt\_conn \*conn, int err, const char \*icon\_url)

Callback function for bt\_mcc\_read\_icon\_url().

**Definition** mcc.h:77

[bt\_mcc\_search\_ntf\_cb](group__bt__gatt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3)

void(\* bt\_mcc\_search\_ntf\_cb)(struct bt\_conn \*conn, int err, uint8\_t result\_code)

Callback function for search notifications.

**Definition** mcc.h:366

[bt\_mcc\_discover\_mcs\_cb](group__bt__gatt__mcc.md#gab268faeca207e115ee1be0843ab8c342)

void(\* bt\_mcc\_discover\_mcs\_cb)(struct bt\_conn \*conn, int err)

Callback function for bt\_mcc\_discover\_mcs().

**Definition** mcc.h:44

[bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__gatt__mcc.md#gab37df36e15132b9235d1093f5aa403cc)

void(\* bt\_mcc\_read\_opcodes\_supported\_cb)(struct bt\_conn \*conn, int err, uint32\_t opcodes)

Callback function for bt\_mcc\_read\_opcodes\_supported().

**Definition** mcc.h:338

[bt\_mcc\_otc\_read\_icon\_object](group__bt__gatt__mcc.md#gaba527d8f0307ab11150a5434231c0e7e)

int bt\_mcc\_otc\_read\_icon\_object(struct bt\_conn \*conn)

Read the Icon Object.

[bt\_mcc\_read\_media\_state](group__bt__gatt__mcc.md#gac1b440cfa54dd4b6e23bb47bf885f88d)

int bt\_mcc\_read\_media\_state(struct bt\_conn \*conn)

Read Media State.

[bt\_mcc\_otc\_read\_track\_segments\_object](group__bt__gatt__mcc.md#gac22e840b65895aa018ab1b4535a87672)

int bt\_mcc\_otc\_read\_track\_segments\_object(struct bt\_conn \*conn)

Read the Track Segments Object.

[bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__gatt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0)

void(\* bt\_mcc\_read\_playing\_orders\_supported\_cb)(struct bt\_conn \*conn, int err, uint16\_t orders)

Callback function for bt\_mcc\_read\_playing\_orders\_supported().

**Definition** mcc.h:289

[bt\_mcc\_otc\_read\_current\_track\_object](group__bt__gatt__mcc.md#gac4b09a77df52d2681e7652591ca32bf8)

int bt\_mcc\_otc\_read\_current\_track\_object(struct bt\_conn \*conn)

Read the Current Track Object.

[bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__gatt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48)

void(\* bt\_mcc\_otc\_read\_parent\_group\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_parent\_group\_object().

**Definition** mcc.h:486

[bt\_mcc\_set\_track\_position](group__bt__gatt__mcc.md#gad324366d33bef6b1ed1c8fc881bf44cf)

int bt\_mcc\_set\_track\_position(struct bt\_conn \*conn, int32\_t pos)

Set Track position.

[bt\_mcc\_read\_content\_control\_id\_cb](group__bt__gatt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927)

void(\* bt\_mcc\_read\_content\_control\_id\_cb)(struct bt\_conn \*conn, int err, uint8\_t ccid)

Callback function for bt\_mcc\_read\_content\_control\_id().

**Definition** mcc.h:394

[bt\_mcc\_otc\_read\_object\_metadata](group__bt__gatt__mcc.md#gadf687cb26a6d00bca73e273da583df88)

int bt\_mcc\_otc\_read\_object\_metadata(struct bt\_conn \*conn)

Read the current object metadata.

[bt\_mcc\_otc\_read\_parent\_group\_object](group__bt__gatt__mcc.md#gae001cb2d701457ce083aa8a0fd5ec518)

int bt\_mcc\_otc\_read\_parent\_group\_object(struct bt\_conn \*conn)

Read the Parent Group Object.

[bt\_mcc\_set\_current\_group\_obj\_id](group__bt__gatt__mcc.md#gae3f385811f852d584595c6e531556aed)

int bt\_mcc\_set\_current\_group\_obj\_id(struct bt\_conn \*conn, uint64\_t id)

Set Current Group Object ID.

[bt\_mcc\_send\_cmd\_cb](group__bt__gatt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e)

void(\* bt\_mcc\_send\_cmd\_cb)(struct bt\_conn \*conn, int err, const struct mpl\_cmd \*cmd)

Callback function for bt\_mcc\_send\_cmd().

**Definition** mcc.h:312

[bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__gatt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529)

void(\* bt\_mcc\_set\_current\_track\_obj\_id\_cb)(struct bt\_conn \*conn, int err, uint64\_t id)

Callback function for bt\_mcc\_set\_current\_track\_obj\_id().

**Definition** mcc.h:201

[bt\_mcc\_read\_track\_position](group__bt__gatt__mcc.md#gaf143098f5dfcfba01df3d6f06472779e)

int bt\_mcc\_read\_track\_position(struct bt\_conn \*conn)

Read Track Position.

[bt\_mcc\_otc\_obj\_selected\_cb](group__bt__gatt__mcc.md#gaf186e6adefa296de4146502665d738b3)

void(\* bt\_mcc\_otc\_obj\_selected\_cb)(struct bt\_conn \*conn, int err)

Callback function for object selected.

**Definition** mcc.h:407

[bt\_mcc\_read\_playing\_orders\_supported](group__bt__gatt__mcc.md#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)

int bt\_mcc\_read\_playing\_orders\_supported(struct bt\_conn \*conn)

Read Playing Orders Supported.

[bt\_mcc\_read\_playing\_order\_cb](group__bt__gatt__mcc.md#gafb0869e0ef5332d39070081efdacf17c)

void(\* bt\_mcc\_read\_playing\_order\_cb)(struct bt\_conn \*conn, int err, uint8\_t order)

Callback function for bt\_mcc\_read\_playing\_order().

**Definition** mcc.h:267

[bt\_mcc\_set\_next\_track\_obj\_id](group__bt__gatt__mcc.md#gafeebcbb0c77d5d4acbe151fd9888d084)

int bt\_mcc\_set\_next\_track\_obj\_id(struct bt\_conn \*conn, uint64\_t id)

Set Next Track Object ID.

[bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__gatt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe)

void(\* bt\_mcc\_otc\_read\_current\_track\_object\_cb)(struct bt\_conn \*conn, int err, struct net\_buf\_simple \*buf)

Callback function for bt\_mcc\_otc\_read\_current\_track\_object().

**Definition** mcc.h:458

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[media\_proxy.h](media__proxy_8h.md)

[buf.h](net_2buf_8h.md)

Buffer management.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

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

**Definition** mcc.h:507

[bt\_mcc\_cb::discover\_mcs](structbt__mcc__cb.md#a2f48a0e0b891131347b0ddc2cb5a8ba7)

bt\_mcc\_discover\_mcs\_cb discover\_mcs

**Definition** mcc.h:508

[bt\_mcc\_cb::cmd\_ntf](structbt__mcc__cb.md#a835f60ad32edc4311a624e779972f0d5)

bt\_mcc\_cmd\_ntf\_cb cmd\_ntf

**Definition** mcc.h:563

[bt\_mcc\_cb::track\_changed\_ntf](structbt__mcc__cb.md#abb7769b73564a22645bfe6b11f239637)

bt\_mcc\_track\_changed\_ntf\_cb track\_changed\_ntf

**Definition** mcc.h:516

[bt\_mcc\_cb::read\_player\_name](structbt__mcc__cb.md#aeea1ef17b3b1e24c965d71f210952079)

bt\_mcc\_read\_player\_name\_cb read\_player\_name

**Definition** mcc.h:509

[bt\_ots\_client](structbt__ots__client.md)

OTS client instance.

**Definition** ots.h:819

[mpl\_cmd\_ntf](structmpl__cmd__ntf.md)

Media command notification.

**Definition** media\_proxy.h:64

[mpl\_cmd](structmpl__cmd.md)

Media player command.

**Definition** media\_proxy.h:55

[mpl\_search](structmpl__search.md)

Search.

**Definition** media\_proxy.h:81

[mpl\_search::search](structmpl__search.md#aa2332c1802786e2ef0486ede1c3a24c7)

char search[64]

**Definition** media\_proxy.h:83

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [mcc.h](mcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
