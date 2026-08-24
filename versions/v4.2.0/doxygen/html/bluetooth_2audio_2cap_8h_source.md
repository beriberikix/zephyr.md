---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/bluetooth_2audio_2cap_8h_source.html
original_path: doxygen/html/bluetooth_2audio_2cap_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cap.h

[Go to the documentation of this file.](bluetooth_2audio_2cap_8h.md)

1

5

6/\*

7 \* Copyright (c) 2022-2025 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CAP\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CAP\_H\_

14

32

33#include <[stdbool.h](stdbool_8h.md)>

34#include <stddef.h>

35#include <[stdint.h](stdint_8h.md)>

36

37#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

38#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>

39#include <[zephyr/bluetooth/audio/csip.h](csip_8h.md)>

40#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

41#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

42#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

43#include <[zephyr/bluetooth/iso.h](iso_8h.md)>

44#include <[zephyr/net\_buf.h](net__buf_8h.md)>

45

46#ifdef \_\_cplusplus

47extern "C" {

48#endif

49

51struct bt\_cap\_broadcast\_source;

52

54struct bt\_cap\_unicast\_group;

55

[ 74](group__bt__cap.md#gafcb9ea2122ff8058321cf85a22326abe)int [bt\_cap\_acceptor\_register](group__bt__cap.md#gafcb9ea2122ff8058321cf85a22326abe)(const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param,

75 struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst);

76

[ 78](structbt__cap__initiator__cb.md)struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) {

79#if defined(CONFIG\_BT\_BAP\_UNICAST\_CLIENT) || defined(\_\_DOXYGEN\_\_)

[ 93](structbt__cap__initiator__cb.md#a642a2f48e8f870bb1681ba58aa119de9) void (\*[unicast\_discovery\_complete](structbt__cap__initiator__cb.md#a642a2f48e8f870bb1681ba58aa119de9))(

94 struct bt\_conn \*conn, int err,

95 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member,

96 const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst);

97

[ 108](structbt__cap__initiator__cb.md#aa70de1dda73ffdcbb8287f8f174984ea) void (\*[unicast\_start\_complete](structbt__cap__initiator__cb.md#aa70de1dda73ffdcbb8287f8f174984ea))(int err, struct bt\_conn \*conn);

109

[ 120](structbt__cap__initiator__cb.md#a95266741841fca83cd2769c76652154e) void (\*[unicast\_update\_complete](structbt__cap__initiator__cb.md#a95266741841fca83cd2769c76652154e))(int err, struct bt\_conn \*conn);

121

[ 132](structbt__cap__initiator__cb.md#a2e910a82209d144878b6c69c1b2723ba) void (\*[unicast\_stop\_complete](structbt__cap__initiator__cb.md#a2e910a82209d144878b6c69c1b2723ba))(int err, struct bt\_conn \*conn);

133#endif /\* CONFIG\_BT\_BAP\_UNICAST\_CLIENT \*/

134#if defined(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE)

140 void (\*broadcast\_started)(struct bt\_cap\_broadcast\_source \*source);

141

148 void (\*broadcast\_stopped)(struct bt\_cap\_broadcast\_source \*source, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

149#endif /\* CONFIG\_BT\_BAP\_BROADCAST\_SOURCE \*/

150};

151

[ 165](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d)int [bt\_cap\_initiator\_unicast\_discover](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d)(struct bt\_conn \*conn);

166

[ 168](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a)enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) {

[ 170](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468) [BT\_CAP\_SET\_TYPE\_AD\_HOC](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468),

[ 172](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4) [BT\_CAP\_SET\_TYPE\_CSIP](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4),

173};

174

[ 176](unionbt__cap__set__member.md)union [bt\_cap\_set\_member](unionbt__cap__set__member.md) {

[ 178](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973) struct bt\_conn \*[member](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973);

179

[ 181](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6) struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*[csip](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6);

182};

183

[ 190](structbt__cap__stream.md)struct [bt\_cap\_stream](structbt__cap__stream.md) {

[ 192](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18) struct [bt\_bap\_stream](structbt__bap__stream.md) [bap\_stream](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18);

193

[ 195](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba) struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*[ops](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba);

196};

197

[ 206](group__bt__cap.md#gac909b00d53cf35103382f0e1d9f426b7)void [bt\_cap\_stream\_ops\_register](group__bt__cap.md#gac909b00d53cf35103382f0e1d9f426b7)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*ops);

207

[ 223](group__bt__cap.md#ga2d8b15543105078b793462b762e27741)int [bt\_cap\_stream\_send](group__bt__cap.md#ga2d8b15543105078b793462b762e27741)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num);

224

[ 242](group__bt__cap.md#ga23618d1ab7690c4d3a567228c857c89e)int [bt\_cap\_stream\_send\_ts](group__bt__cap.md#ga23618d1ab7690c4d3a567228c857c89e)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num,

243 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

244

[ 258](group__bt__cap.md#ga7f3f6e98e7720a4711b658c4b7c85235)int [bt\_cap\_stream\_get\_tx\_sync](group__bt__cap.md#ga7f3f6e98e7720a4711b658c4b7c85235)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info);

259

[ 261](structbt__cap__unicast__group__stream__param.md)struct [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md) {

[ 263](structbt__cap__unicast__group__stream__param.md#a16aacd43bb7b449648ab6a5a89999fba) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__unicast__group__stream__param.md#a16aacd43bb7b449648ab6a5a89999fba);

264

[ 266](structbt__cap__unicast__group__stream__param.md#af55f6b576509853d39b1fe68bcec348a) struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*[qos\_cfg](structbt__cap__unicast__group__stream__param.md#af55f6b576509853d39b1fe68bcec348a);

267};

268

[ 275](structbt__cap__unicast__group__stream__pair__param.md)struct [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md) {

[ 277](structbt__cap__unicast__group__stream__pair__param.md#a19d49ab8c0daa7e6a4c73563952ae461) struct [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md) \*[rx\_param](structbt__cap__unicast__group__stream__pair__param.md#a19d49ab8c0daa7e6a4c73563952ae461);

278

[ 280](structbt__cap__unicast__group__stream__pair__param.md#a6edeca159371f3a70cc5a1f662a0e45c) struct [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md) \*[tx\_param](structbt__cap__unicast__group__stream__pair__param.md#a6edeca159371f3a70cc5a1f662a0e45c);

281};

282

[ 284](structbt__cap__unicast__group__param.md)struct [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md) {

[ 286](structbt__cap__unicast__group__param.md#ab9748e9e230048af64ce9c9ce1006952) size\_t [params\_count](structbt__cap__unicast__group__param.md#ab9748e9e230048af64ce9c9ce1006952);

287

[ 289](structbt__cap__unicast__group__param.md#a64ca2c5cc4f34821e567841ec8efe67b) struct [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md) \*[params](structbt__cap__unicast__group__param.md#a64ca2c5cc4f34821e567841ec8efe67b);

290

[ 298](structbt__cap__unicast__group__param.md#a97e67b903e72dd1f0fef4961810288b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__cap__unicast__group__param.md#a97e67b903e72dd1f0fef4961810288b1);

299

300#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 309](structbt__cap__unicast__group__param.md#adb6cb5686b3d827156aef325b3dcdc84) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_to\_p\_ft](structbt__cap__unicast__group__param.md#adb6cb5686b3d827156aef325b3dcdc84);

310

[ 319](structbt__cap__unicast__group__param.md#ab424be389b026ac5857e3bec1c3d686f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_to\_c\_ft](structbt__cap__unicast__group__param.md#ab424be389b026ac5857e3bec1c3d686f);

320

[ 328](structbt__cap__unicast__group__param.md#ac52a0e09e3978a084e4fe558e4a5a848) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__cap__unicast__group__param.md#ac52a0e09e3978a084e4fe558e4a5a848);

329#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

330};

331

[ 345](group__bt__cap.md#ga299ee8321aa5059e48244e1ae8080637)int [bt\_cap\_unicast\_group\_create](group__bt__cap.md#ga299ee8321aa5059e48244e1ae8080637)(const struct [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md) \*param,

346 struct bt\_cap\_unicast\_group \*\*unicast\_group);

347

[ 363](group__bt__cap.md#ga6c862b49aa1339225aeb05fad32c2f06)int [bt\_cap\_unicast\_group\_reconfig](group__bt__cap.md#ga6c862b49aa1339225aeb05fad32c2f06)(struct bt\_cap\_unicast\_group \*unicast\_group,

364 const struct [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md) \*param);

365

[ 385](group__bt__cap.md#ga7b5d30c07e57f4db23f72836a3b12b2b)int [bt\_cap\_unicast\_group\_add\_streams](group__bt__cap.md#ga7b5d30c07e57f4db23f72836a3b12b2b)(struct bt\_cap\_unicast\_group \*unicast\_group,

386 const struct [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md) params[],

387 size\_t num\_param);

388

[ 399](group__bt__cap.md#ga9af37b30b6c858c24892eb1739b5330a)int [bt\_cap\_unicast\_group\_delete](group__bt__cap.md#ga9af37b30b6c858c24892eb1739b5330a)(struct bt\_cap\_unicast\_group \*unicast\_group);

400

[ 409](group__bt__cap.md#gaeaad4ea5142afe5dca741b72795ae3aa)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_cap\_unicast\_group\_foreach\_stream\_func\_t](group__bt__cap.md#gaeaad4ea5142afe5dca741b72795ae3aa))(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream,

410 void \*user\_data);

411

[ 423](group__bt__cap.md#ga6c13996298c3e3aa33eb40f74b7bfe44)int [bt\_cap\_unicast\_group\_foreach\_stream](group__bt__cap.md#ga6c13996298c3e3aa33eb40f74b7bfe44)(struct bt\_cap\_unicast\_group \*unicast\_group,

424 [bt\_cap\_unicast\_group\_foreach\_stream\_func\_t](group__bt__cap.md#gaeaad4ea5142afe5dca741b72795ae3aa) func,

425 void \*user\_data);

426

[ 428](structbt__cap__unicast__audio__start__stream__param.md)struct [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md) {

[ 430](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b);

431

[ 433](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e);

434

[ 436](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb) struct bt\_bap\_ep \*[ep](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb);

437

[ 448](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a);

449};

450

[ 452](structbt__cap__unicast__audio__start__param.md)struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) {

[ 454](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5);

455

[ 457](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667) size\_t [count](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667);

458

[ 460](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b) struct [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md) \*[stream\_params](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b);

461};

462

[ 464](structbt__cap__unicast__audio__update__stream__param.md)struct [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) {

[ 466](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1);

467

[ 469](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c) size\_t [meta\_len](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c);

470

[ 476](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[meta](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0);

477};

478

[ 480](structbt__cap__unicast__audio__update__param.md)struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) {

[ 482](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd);

483

[ 485](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1) size\_t [count](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1);

486

[ 488](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb) struct [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) \*[stream\_params](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb);

489};

490

[ 492](structbt__cap__unicast__audio__stop__param.md)struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) {

[ 494](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa);

495

[ 497](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2) size\_t [count](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2);

498

[ 500](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82) struct [bt\_cap\_stream](structbt__cap__stream.md) \*\*[streams](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82);

501

[ 503](structbt__cap__unicast__audio__stop__param.md#a1cbd7ee2e4ceafd2da2858dc7c941d78) bool [release](structbt__cap__unicast__audio__stop__param.md#a1cbd7ee2e4ceafd2da2858dc7c941d78);

504};

505

[ 513](group__bt__cap.md#ga54d7ad68f376998510aad9c3702e9364)int [bt\_cap\_initiator\_register\_cb](group__bt__cap.md#ga54d7ad68f376998510aad9c3702e9364)(const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb);

514

[ 523](group__bt__cap.md#gaa7286837f37da38afec8c5c955306b61)int [bt\_cap\_initiator\_unregister\_cb](group__bt__cap.md#gaa7286837f37da38afec8c5c955306b61)(const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb);

524

[ 543](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184)int [bt\_cap\_initiator\_unicast\_audio\_start](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184)(const struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) \*param);

544

[ 558](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639)int [bt\_cap\_initiator\_unicast\_audio\_update](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639)(const struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) \*param);

559

[ 576](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f)int [bt\_cap\_initiator\_unicast\_audio\_stop](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f)(const struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) \*param);

577

[ 601](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f)int [bt\_cap\_initiator\_unicast\_audio\_cancel](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f)(void);

602

[ 607](structbt__cap__initiator__broadcast__stream__param.md)struct [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) {

[ 609](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a);

610

[ 615](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4) size\_t [data\_len](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4);

616

[ 618](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869);

619};

620

[ 625](structbt__cap__initiator__broadcast__subgroup__param.md)struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) {

[ 627](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769) size\_t [stream\_count](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769);

628

[ 630](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a) struct [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) \*[stream\_params](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a);

631

[ 633](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47);

634};

635

[ 637](structbt__cap__initiator__broadcast__create__param.md)struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) {

[ 639](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b) size\_t [subgroup\_count](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b);

640

[ 642](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839) struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) \*[subgroup\_params](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839);

643

[ 645](structbt__cap__initiator__broadcast__create__param.md#a142125e620776aed464d90f280ef1a4c) struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*[qos](structbt__cap__initiator__broadcast__create__param.md#a142125e620776aed464d90f280ef1a4c);

646

[ 654](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc);

655

[ 657](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542) bool [encryption](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542);

658

[ 671](structbt__cap__initiator__broadcast__create__param.md#aa4d6fbd5bd13963004e381b987bbeb4d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__cap__initiator__broadcast__create__param.md#aa4d6fbd5bd13963004e381b987bbeb4d)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

672

673#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 681](structbt__cap__initiator__broadcast__create__param.md#a6f562b7a696472b7784ca2e1ced4997a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__cap__initiator__broadcast__create__param.md#a6f562b7a696472b7784ca2e1ced4997a);

682

[ 690](structbt__cap__initiator__broadcast__create__param.md#a01d6ffb369caaf808d4b55b3b1748890) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__cap__initiator__broadcast__create__param.md#a01d6ffb369caaf808d4b55b3b1748890);

691

[ 699](structbt__cap__initiator__broadcast__create__param.md#a8eedd8f9a896931f75642576ca37c7d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__cap__initiator__broadcast__create__param.md#a8eedd8f9a896931f75642576ca37c7d5);

700#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

701};

702

[ 722](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4)int [bt\_cap\_initiator\_broadcast\_audio\_create](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4)(

723 const struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) \*param,

724 struct bt\_cap\_broadcast\_source \*\*broadcast\_source);

725

[ 745](group__bt__cap.md#ga2bd5f9c9de719a14ffc69827dbd4fa24)int [bt\_cap\_initiator\_broadcast\_audio\_start](group__bt__cap.md#ga2bd5f9c9de719a14ffc69827dbd4fa24)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

746 struct bt\_le\_ext\_adv \*adv);

[ 761](group__bt__cap.md#ga92336c4a56c667b608a86e45eb8d5073)int [bt\_cap\_initiator\_broadcast\_audio\_update](group__bt__cap.md#ga92336c4a56c667b608a86e45eb8d5073)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

762 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

763

[ 776](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e)int [bt\_cap\_initiator\_broadcast\_audio\_stop](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e)(struct bt\_cap\_broadcast\_source \*broadcast\_source);

777

[ 795](group__bt__cap.md#gac98ed5112d0ce0659bde86d149ea7b4c)int [bt\_cap\_initiator\_broadcast\_audio\_delete](group__bt__cap.md#gac98ed5112d0ce0659bde86d149ea7b4c)(struct bt\_cap\_broadcast\_source \*broadcast\_source);

796

[ 812](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)int [bt\_cap\_initiator\_broadcast\_get\_base](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

813 struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf);

814

[ 816](structbt__cap__unicast__to__broadcast__param.md)struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) {

[ 818](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239) struct bt\_bap\_unicast\_group \*[unicast\_group](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239);

819

[ 826](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262) bool [encrypt](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262);

827

[ 840](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

841};

842

[ 859](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558)int [bt\_cap\_initiator\_unicast\_to\_broadcast](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558)(const struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) \*param,

860 struct bt\_cap\_broadcast\_source \*\*source);

861

[ 863](structbt__cap__broadcast__to__unicast__param.md)struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) {

[ 869](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9) struct bt\_cap\_broadcast\_source \*[broadcast\_source](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9);

870

[ 872](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf);

873

[ 881](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce) size\_t [count](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce);

882

[ 884](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*\*[members](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed);

885};

886

[ 903](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b)int [bt\_cap\_initiator\_broadcast\_to\_unicast](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b)(const struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) \*param,

904 struct bt\_bap\_unicast\_group \*\*unicast\_group);

905

[ 907](structbt__cap__commander__cb.md)struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) {

[ 921](structbt__cap__commander__cb.md#af989b3ebe7e5cc83a1ca4b2ef080e14d) void (\*[discovery\_complete](structbt__cap__commander__cb.md#af989b3ebe7e5cc83a1ca4b2ef080e14d))(struct bt\_conn \*conn, int err,

922 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member,

923 const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst);

924

925#if defined(CONFIG\_BT\_VCP\_VOL\_CTLR) || defined(\_\_DOXYGEN\_\_)

[ 936](structbt__cap__commander__cb.md#a3a7777603c23c14bc9d01cf29bc70ef7) void (\*[volume\_changed](structbt__cap__commander__cb.md#a3a7777603c23c14bc9d01cf29bc70ef7))(struct bt\_conn \*conn, int err);

937

[ 948](structbt__cap__commander__cb.md#acc9fcedf7f7abe86e055d48e6df124c7) void (\*[volume\_mute\_changed](structbt__cap__commander__cb.md#acc9fcedf7f7abe86e055d48e6df124c7))(struct bt\_conn \*conn, int err);

949

950#if defined(CONFIG\_BT\_VCP\_VOL\_CTLR\_VOCS) || defined(\_\_DOXYGEN\_\_)

[ 961](structbt__cap__commander__cb.md#a3bacfffef8d122db4574463777dfd507) void (\*[volume\_offset\_changed](structbt__cap__commander__cb.md#a3bacfffef8d122db4574463777dfd507))(struct bt\_conn \*conn, int err);

962#endif /\* CONFIG\_BT\_VCP\_VOL\_CTLR\_VOCS \*/

963#endif /\* CONFIG\_BT\_VCP\_VOL\_CTLR \*/

964#if defined(CONFIG\_BT\_MICP\_MIC\_CTLR) || defined(\_\_DOXYGEN\_\_)

[ 975](structbt__cap__commander__cb.md#aa49e7eaf5c45d70c800f28b81f9967e5) void (\*[microphone\_mute\_changed](structbt__cap__commander__cb.md#aa49e7eaf5c45d70c800f28b81f9967e5))(struct bt\_conn \*conn, int err);

976#if defined(CONFIG\_BT\_MICP\_MIC\_CTLR\_AICS) || defined(\_\_DOXYGEN\_\_)

[ 987](structbt__cap__commander__cb.md#a1e83872924e1aa1293c499184ade9173) void (\*[microphone\_gain\_changed](structbt__cap__commander__cb.md#a1e83872924e1aa1293c499184ade9173))(struct bt\_conn \*conn, int err);

988#endif /\* CONFIG\_BT\_MICP\_MIC\_CTLR\_AICS \*/

989#endif /\* CONFIG\_BT\_MICP\_MIC\_CTLR \*/

990

991#if defined(CONFIG\_BT\_BAP\_BROADCAST\_ASSISTANT) || defined(\_\_DOXYGEN\_\_)

[ 1002](structbt__cap__commander__cb.md#a14f6a51db5a76aac015a5de617712af3) void (\*[broadcast\_reception\_start](structbt__cap__commander__cb.md#a14f6a51db5a76aac015a5de617712af3))(struct bt\_conn \*conn, int err);

[ 1013](structbt__cap__commander__cb.md#a2188c52e3daf0a695d7c42e6cac561cf) void (\*[broadcast\_reception\_stop](structbt__cap__commander__cb.md#a2188c52e3daf0a695d7c42e6cac561cf))(struct bt\_conn \*conn, int err);

[ 1024](structbt__cap__commander__cb.md#a7dfa1903f5cd71e67b6da0f5ff2fb299) void (\*[distribute\_broadcast\_code](structbt__cap__commander__cb.md#a7dfa1903f5cd71e67b6da0f5ff2fb299))(struct bt\_conn \*conn, int err);

1025#endif /\* CONFIG\_BT\_BAP\_BROADCAST\_ASSISTANT \*/

1026};

1027

[ 1037](group__bt__cap.md#gab6239c91b9d210872396860619fb8687)int [bt\_cap\_commander\_register\_cb](group__bt__cap.md#gab6239c91b9d210872396860619fb8687)(const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb);

1038

[ 1047](group__bt__cap.md#ga38928945e67835983de3fc639c8f2764)int [bt\_cap\_commander\_unregister\_cb](group__bt__cap.md#ga38928945e67835983de3fc639c8f2764)(const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb);

1048

[ 1067](group__bt__cap.md#ga165c67bddcbe220050293a4c73fb6ede)int [bt\_cap\_commander\_discover](group__bt__cap.md#ga165c67bddcbe220050293a4c73fb6ede)(struct bt\_conn \*conn);

1068

[ 1092](group__bt__cap.md#ga7abf029533fed391930257605f3c752c)int [bt\_cap\_commander\_cancel](group__bt__cap.md#ga7abf029533fed391930257605f3c752c)(void);

1093

[ 1098](structbt__cap__commander__broadcast__reception__start__member__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) {

[ 1100](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7);

1101

[ 1103](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e);

1104

[ 1106](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362);

1107

[ 1113](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pa\_interval](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c);

1114

[ 1116](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0);

1117

[ 1123](structbt__cap__commander__broadcast__reception__start__member__param.md#a2222f8ae46afed4760db56079779532d) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) [subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#a2222f8ae46afed4760db56079779532d)[[BT\_BAP\_BASS\_MAX\_SUBGROUPS](group__bt__bap.md#ga443c212a736852305715452e7f165a9e)];

1124

[ 1126](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63) size\_t [num\_subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63);

1127};

1128

[ 1130](structbt__cap__commander__broadcast__reception__start__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) {

[ 1132](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1);

1133

[ 1135](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041) struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) \*[param](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041);

1136

[ 1138](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7) size\_t [count](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7);

1139};

1140

[ 1149](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9)int [bt\_cap\_commander\_broadcast\_reception\_start](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9)(

1150 const struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) \*param);

1151

[ 1153](structbt__cap__commander__broadcast__reception__stop__member__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md) {

[ 1155](structbt__cap__commander__broadcast__reception__stop__member__param.md#aa934af2e197c129b1fcb1eea9359ea6d) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__broadcast__reception__stop__member__param.md#aa934af2e197c129b1fcb1eea9359ea6d);

1156

[ 1158](structbt__cap__commander__broadcast__reception__stop__member__param.md#a72d606f6a83b1c84aa41d9db22cb955a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__cap__commander__broadcast__reception__stop__member__param.md#a72d606f6a83b1c84aa41d9db22cb955a);

1159

[ 1161](structbt__cap__commander__broadcast__reception__stop__member__param.md#aeeab53e8bd7ae4f36433c0d4b60c313b) size\_t [num\_subgroups](structbt__cap__commander__broadcast__reception__stop__member__param.md#aeeab53e8bd7ae4f36433c0d4b60c313b);

1162};

1163

[ 1165](structbt__cap__commander__broadcast__reception__stop__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) {

[ 1167](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460);

1168

[ 1170](structbt__cap__commander__broadcast__reception__stop__param.md#a36ce7cd132cd41a55872985433c2934d) struct [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md) \*[param](structbt__cap__commander__broadcast__reception__stop__param.md#a36ce7cd132cd41a55872985433c2934d);

1171

[ 1173](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593) size\_t [count](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593);

1174};

1175

[ 1184](group__bt__cap.md#gac5b2b6d617a092fb98b23c41b2f52d15)int [bt\_cap\_commander\_broadcast\_reception\_stop](group__bt__cap.md#gac5b2b6d617a092fb98b23c41b2f52d15)(

1185 const struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) \*param);

1186

[ 1188](structbt__cap__commander__distribute__broadcast__code__member__param.md)struct [bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param](structbt__cap__commander__distribute__broadcast__code__member__param.md) {

[ 1190](structbt__cap__commander__distribute__broadcast__code__member__param.md#acd5d185c590ea9a64faebd354a3d5d4a) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__distribute__broadcast__code__member__param.md#acd5d185c590ea9a64faebd354a3d5d4a);

1191

[ 1193](structbt__cap__commander__distribute__broadcast__code__member__param.md#ad240bb7e1e9ad5c40eb1a031a6fbc2fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__cap__commander__distribute__broadcast__code__member__param.md#ad240bb7e1e9ad5c40eb1a031a6fbc2fe);

1194};

1195

[ 1197](structbt__cap__commander__distribute__broadcast__code__param.md)struct [bt\_cap\_commander\_distribute\_broadcast\_code\_param](structbt__cap__commander__distribute__broadcast__code__param.md) {

[ 1199](structbt__cap__commander__distribute__broadcast__code__param.md#a9605ad1590ff0279b46d639d38278933) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__distribute__broadcast__code__param.md#a9605ad1590ff0279b46d639d38278933);

1200

[ 1202](structbt__cap__commander__distribute__broadcast__code__param.md#a03be4b2fac7803de233c8a1024640cc2) struct [bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param](structbt__cap__commander__distribute__broadcast__code__member__param.md) \*[param](structbt__cap__commander__distribute__broadcast__code__param.md#a03be4b2fac7803de233c8a1024640cc2);

1203

[ 1205](structbt__cap__commander__distribute__broadcast__code__param.md#a86316e3bf53edca67e0743072f0f2ee3) size\_t [count](structbt__cap__commander__distribute__broadcast__code__param.md#a86316e3bf53edca67e0743072f0f2ee3);

1206

[ 1217](structbt__cap__commander__distribute__broadcast__code__param.md#ac7d426c975c1e2324f52486abf9298b9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__cap__commander__distribute__broadcast__code__param.md#ac7d426c975c1e2324f52486abf9298b9)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

1218};

1219

[ 1228](group__bt__cap.md#gaf86582ad529b6ee801d1154db7e33827)int [bt\_cap\_commander\_distribute\_broadcast\_code](group__bt__cap.md#gaf86582ad529b6ee801d1154db7e33827)(

1229 const struct [bt\_cap\_commander\_distribute\_broadcast\_code\_param](structbt__cap__commander__distribute__broadcast__code__param.md) \*param);

1230

[ 1232](structbt__cap__commander__change__volume__param.md)struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) {

[ 1234](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88);

1235

[ 1237](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531);

1238

[ 1240](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640) size\_t [count](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640);

1241

[ 1243](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [volume](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49);

1244};

1245

[ 1253](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6)int [bt\_cap\_commander\_change\_volume](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6)(const struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) \*param);

1254

[ 1259](structbt__cap__commander__change__volume__offset__member__param.md)struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) {

[ 1261](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4);

1262

[ 1268](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [offset](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8);

1269};

1270

[ 1272](structbt__cap__commander__change__volume__offset__param.md)struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) {

[ 1274](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd);

1275

[ 1277](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d) struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) \*[param](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d);

1278

[ 1280](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b) size\_t [count](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b);

1281};

1282

[ 1290](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa)int [bt\_cap\_commander\_change\_volume\_offset](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa)(

1291 const struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) \*param);

1292

[ 1294](structbt__cap__commander__change__volume__mute__state__param.md)struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) {

[ 1296](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775);

1297

[ 1299](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1);

1300

[ 1302](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8) size\_t [count](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8);

1303

[ 1309](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd) bool [mute](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd);

1310};

1311

[ 1319](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4)int [bt\_cap\_commander\_change\_volume\_mute\_state](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4)(

1320 const struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) \*param);

1321

[ 1323](structbt__cap__commander__change__microphone__mute__state__param.md)struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) {

[ 1325](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0);

1326

[ 1328](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1);

1329

[ 1331](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e) size\_t [count](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e);

1332

[ 1338](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8) bool [mute](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8);

1339};

1340

[ 1348](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54)int [bt\_cap\_commander\_change\_microphone\_mute\_state](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54)(

1349 const struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) \*param);

1350

[ 1355](structbt__cap__commander__change__microphone__gain__setting__member__param.md)struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) {

[ 1357](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e);

1358

[ 1360](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [gain](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196);

1361};

1362

[ 1364](structbt__cap__commander__change__microphone__gain__setting__param.md)struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) {

[ 1366](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673);

1367

[ 1369](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8) struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) \*[param](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8);

1370

[ 1372](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349) size\_t [count](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349);

1373};

1374

[ 1382](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b)int [bt\_cap\_commander\_change\_microphone\_gain\_setting](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b)(

1383 const struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) \*param);

1384#ifdef \_\_cplusplus

1385}

1386#endif

1387

1391

1392#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CAP\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[bap.h](bap_8h.md)

Header for Bluetooth BAP.

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[csip.h](csip_8h.md)

Bluetooth Coordinated Set Identification Profile (CSIP) APIs.

[BT\_BAP\_BASS\_MAX\_SUBGROUPS](group__bt__bap.md#ga443c212a736852305715452e7f165a9e)

#define BT\_BAP\_BASS\_MAX\_SUBGROUPS

Maximum number of subgroups supported in the BAP Scan Delegator API.

**Definition** bap.h:48

[bt\_cap\_commander\_discover](group__bt__cap.md#ga165c67bddcbe220050293a4c73fb6ede)

int bt\_cap\_commander\_discover(struct bt\_conn \*conn)

Discovers audio support on a remote device.

[bt\_cap\_commander\_change\_microphone\_mute\_state](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54)

int bt\_cap\_commander\_change\_microphone\_mute\_state(const struct bt\_cap\_commander\_change\_microphone\_mute\_state\_param \*param)

Change the microphone mute state on one or more Common Audio Profile Acceptors.

[bt\_cap\_stream\_send\_ts](group__bt__cap.md#ga23618d1ab7690c4d3a567228c857c89e)

int bt\_cap\_stream\_send\_ts(struct bt\_cap\_stream \*stream, struct net\_buf \*buf, uint16\_t seq\_num, uint32\_t ts)

Send data to Common Audio Profile stream with timestamp.

[bt\_cap\_commander\_broadcast\_reception\_start](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9)

int bt\_cap\_commander\_broadcast\_reception\_start(const struct bt\_cap\_commander\_broadcast\_reception\_start\_param \*param)

Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.

[bt\_cap\_unicast\_group\_create](group__bt__cap.md#ga299ee8321aa5059e48244e1ae8080637)

int bt\_cap\_unicast\_group\_create(const struct bt\_cap\_unicast\_group\_param \*param, struct bt\_cap\_unicast\_group \*\*unicast\_group)

Create unicast group.

[bt\_cap\_initiator\_broadcast\_audio\_start](group__bt__cap.md#ga2bd5f9c9de719a14ffc69827dbd4fa24)

int bt\_cap\_initiator\_broadcast\_audio\_start(struct bt\_cap\_broadcast\_source \*broadcast\_source, struct bt\_le\_ext\_adv \*adv)

Start Common Audio Profile broadcast source.

[bt\_cap\_stream\_send](group__bt__cap.md#ga2d8b15543105078b793462b762e27741)

int bt\_cap\_stream\_send(struct bt\_cap\_stream \*stream, struct net\_buf \*buf, uint16\_t seq\_num)

Send data to Common Audio Profile stream without timestamp.

[bt\_cap\_initiator\_broadcast\_to\_unicast](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b)

int bt\_cap\_initiator\_broadcast\_to\_unicast(const struct bt\_cap\_broadcast\_to\_unicast\_param \*param, struct bt\_bap\_unicast\_group \*\*unicast\_group)

Hands over the data streams in a broadcast source to a unicast group.

[bt\_cap\_commander\_unregister\_cb](group__bt__cap.md#ga38928945e67835983de3fc639c8f2764)

int bt\_cap\_commander\_unregister\_cb(const struct bt\_cap\_commander\_cb \*cb)

Unregister Common Audio Profile Commander callbacks.

[bt\_cap\_initiator\_register\_cb](group__bt__cap.md#ga54d7ad68f376998510aad9c3702e9364)

int bt\_cap\_initiator\_register\_cb(const struct bt\_cap\_initiator\_cb \*cb)

Register Common Audio Profile Initiator callbacks.

[bt\_cap\_initiator\_unicast\_to\_broadcast](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558)

int bt\_cap\_initiator\_unicast\_to\_broadcast(const struct bt\_cap\_unicast\_to\_broadcast\_param \*param, struct bt\_cap\_broadcast\_source \*\*source)

Hands over the data streams in a unicast group to a broadcast source.

[bt\_cap\_unicast\_group\_foreach\_stream](group__bt__cap.md#ga6c13996298c3e3aa33eb40f74b7bfe44)

int bt\_cap\_unicast\_group\_foreach\_stream(struct bt\_cap\_unicast\_group \*unicast\_group, bt\_cap\_unicast\_group\_foreach\_stream\_func\_t func, void \*user\_data)

Iterate through all streams in a unicast group.

[bt\_cap\_unicast\_group\_reconfig](group__bt__cap.md#ga6c862b49aa1339225aeb05fad32c2f06)

int bt\_cap\_unicast\_group\_reconfig(struct bt\_cap\_unicast\_group \*unicast\_group, const struct bt\_cap\_unicast\_group\_param \*param)

Reconfigure unicast group.

[bt\_cap\_initiator\_broadcast\_get\_base](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)

int bt\_cap\_initiator\_broadcast\_get\_base(struct bt\_cap\_broadcast\_source \*broadcast\_source, struct net\_buf\_simple \*base\_buf)

Get the Broadcast Audio Stream Endpoint of a Common Audio Profile broadcast source.

[bt\_cap\_initiator\_broadcast\_audio\_create](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4)

int bt\_cap\_initiator\_broadcast\_audio\_create(const struct bt\_cap\_initiator\_broadcast\_create\_param \*param, struct bt\_cap\_broadcast\_source \*\*broadcast\_source)

Create a Common Audio Profile broadcast source.

[bt\_cap\_commander\_cancel](group__bt__cap.md#ga7abf029533fed391930257605f3c752c)

int bt\_cap\_commander\_cancel(void)

Cancel any current Common Audio Profile commander procedure.

[bt\_cap\_unicast\_group\_add\_streams](group__bt__cap.md#ga7b5d30c07e57f4db23f72836a3b12b2b)

int bt\_cap\_unicast\_group\_add\_streams(struct bt\_cap\_unicast\_group \*unicast\_group, const struct bt\_cap\_unicast\_group\_stream\_pair\_param params[], size\_t num\_param)

Add streams to a unicast group as a unicast client.

[bt\_cap\_stream\_get\_tx\_sync](group__bt__cap.md#ga7f3f6e98e7720a4711b658c4b7c85235)

int bt\_cap\_stream\_get\_tx\_sync(struct bt\_cap\_stream \*stream, struct bt\_iso\_tx\_info \*info)

Get ISO transmission timing info for a Common Audio Profile stream.

[bt\_cap\_initiator\_broadcast\_audio\_update](group__bt__cap.md#ga92336c4a56c667b608a86e45eb8d5073)

int bt\_cap\_initiator\_broadcast\_audio\_update(struct bt\_cap\_broadcast\_source \*broadcast\_source, const uint8\_t meta[], size\_t meta\_len)

Update broadcast audio streams for a Common Audio Profile broadcast source.

[bt\_cap\_initiator\_unicast\_audio\_update](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639)

int bt\_cap\_initiator\_unicast\_audio\_update(const struct bt\_cap\_unicast\_audio\_update\_param \*param)

Update unicast audio streams.

[bt\_cap\_commander\_change\_microphone\_gain\_setting](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b)

int bt\_cap\_commander\_change\_microphone\_gain\_setting(const struct bt\_cap\_commander\_change\_microphone\_gain\_setting\_param \*param)

Change the microphone gain setting on one or more Common Audio Profile Acceptors.

[bt\_cap\_unicast\_group\_delete](group__bt__cap.md#ga9af37b30b6c858c24892eb1739b5330a)

int bt\_cap\_unicast\_group\_delete(struct bt\_cap\_unicast\_group \*unicast\_group)

Delete audio unicast group.

[bt\_cap\_initiator\_unicast\_audio\_cancel](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f)

int bt\_cap\_initiator\_unicast\_audio\_cancel(void)

Cancel any current Common Audio Profile procedure.

[bt\_cap\_initiator\_unregister\_cb](group__bt__cap.md#gaa7286837f37da38afec8c5c955306b61)

int bt\_cap\_initiator\_unregister\_cb(const struct bt\_cap\_initiator\_cb \*cb)

Unregister Common Audio Profile Initiator callbacks.

[bt\_cap\_commander\_register\_cb](group__bt__cap.md#gab6239c91b9d210872396860619fb8687)

int bt\_cap\_commander\_register\_cb(const struct bt\_cap\_commander\_cb \*cb)

Register Common Audio Profile Commander callbacks.

[bt\_cap\_initiator\_unicast\_discover](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d)

int bt\_cap\_initiator\_unicast\_discover(struct bt\_conn \*conn)

Discovers audio support on a remote device.

[bt\_cap\_commander\_broadcast\_reception\_stop](group__bt__cap.md#gac5b2b6d617a092fb98b23c41b2f52d15)

int bt\_cap\_commander\_broadcast\_reception\_stop(const struct bt\_cap\_commander\_broadcast\_reception\_stop\_param \*param)

Stops the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.

[bt\_cap\_commander\_change\_volume\_mute\_state](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4)

int bt\_cap\_commander\_change\_volume\_mute\_state(const struct bt\_cap\_commander\_change\_volume\_mute\_state\_param \*param)

Change the volume mute state on one or more Common Audio Profile Acceptors.

[bt\_cap\_stream\_ops\_register](group__bt__cap.md#gac909b00d53cf35103382f0e1d9f426b7)

void bt\_cap\_stream\_ops\_register(struct bt\_cap\_stream \*stream, struct bt\_bap\_stream\_ops \*ops)

Register Audio operations for a Common Audio Profile stream.

[bt\_cap\_initiator\_broadcast\_audio\_delete](group__bt__cap.md#gac98ed5112d0ce0659bde86d149ea7b4c)

int bt\_cap\_initiator\_broadcast\_audio\_delete(struct bt\_cap\_broadcast\_source \*broadcast\_source)

Delete Common Audio Profile broadcast source.

[bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a)

bt\_cap\_set\_type

Type of CAP set.

**Definition** cap.h:168

[bt\_cap\_initiator\_unicast\_audio\_start](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184)

int bt\_cap\_initiator\_unicast\_audio\_start(const struct bt\_cap\_unicast\_audio\_start\_param \*param)

Setup and start unicast audio streams for a set of devices.

[bt\_cap\_commander\_change\_volume\_offset](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa)

int bt\_cap\_commander\_change\_volume\_offset(const struct bt\_cap\_commander\_change\_volume\_offset\_param \*param)

Change the volume offset on one or more Common Audio Profile Acceptors.

[bt\_cap\_initiator\_broadcast\_audio\_stop](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e)

int bt\_cap\_initiator\_broadcast\_audio\_stop(struct bt\_cap\_broadcast\_source \*broadcast\_source)

Stop broadcast audio streams for a Common Audio Profile broadcast source.

[bt\_cap\_unicast\_group\_foreach\_stream\_func\_t](group__bt__cap.md#gaeaad4ea5142afe5dca741b72795ae3aa)

bool(\* bt\_cap\_unicast\_group\_foreach\_stream\_func\_t)(struct bt\_cap\_stream \*stream, void \*user\_data)

Callback function for bt\_bap\_unicast\_group\_foreach\_stream().

**Definition** cap.h:409

[bt\_cap\_commander\_distribute\_broadcast\_code](group__bt__cap.md#gaf86582ad529b6ee801d1154db7e33827)

int bt\_cap\_commander\_distribute\_broadcast\_code(const struct bt\_cap\_commander\_distribute\_broadcast\_code\_param \*param)

Distributes the broadcast code on one or more remote Common Audio Profile Acceptors.

[bt\_cap\_acceptor\_register](group__bt__cap.md#gafcb9ea2122ff8058321cf85a22326abe)

int bt\_cap\_acceptor\_register(const struct bt\_csip\_set\_member\_register\_param \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst)

Register the Common Audio Service.

[bt\_cap\_initiator\_unicast\_audio\_stop](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f)

int bt\_cap\_initiator\_unicast\_audio\_stop(const struct bt\_cap\_unicast\_audio\_stop\_param \*param)

Stop unicast audio streams.

[bt\_cap\_commander\_change\_volume](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6)

int bt\_cap\_commander\_change\_volume(const struct bt\_cap\_commander\_change\_volume\_param \*param)

Change the volume on one or more Common Audio Profile Acceptors.

[BT\_CAP\_SET\_TYPE\_CSIP](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4)

@ BT\_CAP\_SET\_TYPE\_CSIP

The set is a CSIP Coordinated Set.

**Definition** cap.h:172

[BT\_CAP\_SET\_TYPE\_AD\_HOC](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468)

@ BT\_CAP\_SET\_TYPE\_AD\_HOC

The set is an ad-hoc set.

**Definition** cap.h:170

[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)

#define BT\_ISO\_BROADCAST\_CODE\_SIZE

Broadcast code size.

**Definition** iso.h:141

[iso.h](iso_8h.md)

Bluetooth ISO handling.

[net\_buf.h](net__buf_8h.md)

Buffer management.

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

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:718

[bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md)

Struct to hold subgroup specific information for the receive state.

**Definition** bap.h:641

[bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md)

QoS configuration structure.

**Definition** bap.h:232

[bt\_bap\_stream\_ops](structbt__bap__stream__ops.md)

Stream operation.

**Definition** bap.h:933

[bt\_bap\_stream](structbt__bap__stream.md)

Basic Audio Profile stream structure.

**Definition** bap.h:890

[bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md)

Parameters for bt\_cap\_initiator\_broadcast\_to\_unicast().

**Definition** cap.h:863

[bt\_cap\_broadcast\_to\_unicast\_param::members](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed)

union bt\_cap\_set\_member \*\* members

Coordinated or ad-hoc set members.

**Definition** cap.h:884

[bt\_cap\_broadcast\_to\_unicast\_param::type](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:872

[bt\_cap\_broadcast\_to\_unicast\_param::count](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce)

size\_t count

The number of set members in members.

**Definition** cap.h:881

[bt\_cap\_broadcast\_to\_unicast\_param::broadcast\_source](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9)

struct bt\_cap\_broadcast\_source \* broadcast\_source

The source broadcast source with the streams.

**Definition** cap.h:869

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md)

Parameters part of bt\_cap\_commander\_broadcast\_reception\_start\_param for bt\_cap\_commander\_broadcast\_re...

**Definition** cap.h:1098

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::num\_subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63)

size\_t num\_subgroups

Number of subgroups.

**Definition** cap.h:1126

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::pa\_interval](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c)

uint16\_t pa\_interval

Periodic advertising interval in milliseconds.

**Definition** cap.h:1113

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#a2222f8ae46afed4760db56079779532d)

struct bt\_bap\_bass\_subgroup subgroups[BT\_BAP\_BASS\_MAX\_SUBGROUPS]

Pointer to array of subgroups.

**Definition** cap.h:1123

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::broadcast\_id](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0)

uint32\_t broadcast\_id

24-bit broadcast ID

**Definition** cap.h:1116

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::addr](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e)

bt\_addr\_le\_t addr

Address of the advertiser.

**Definition** cap.h:1103

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::member](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:1100

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::adv\_sid](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362)

uint8\_t adv\_sid

SID of the advertising set.

**Definition** cap.h:1106

[bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md)

Parameters for starting broadcast reception.

**Definition** cap.h:1130

[bt\_cap\_commander\_broadcast\_reception\_start\_param::param](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041)

struct bt\_cap\_commander\_broadcast\_reception\_start\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:1135

[bt\_cap\_commander\_broadcast\_reception\_start\_param::count](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7)

size\_t count

The number of parameters in param.

**Definition** cap.h:1138

[bt\_cap\_commander\_broadcast\_reception\_start\_param::type](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1132

[bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md)

Member parameters for stopping broadcast reception.

**Definition** cap.h:1153

[bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::src\_id](structbt__cap__commander__broadcast__reception__stop__member__param.md#a72d606f6a83b1c84aa41d9db22cb955a)

uint8\_t src\_id

Source ID of the receive state.

**Definition** cap.h:1158

[bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::member](structbt__cap__commander__broadcast__reception__stop__member__param.md#aa934af2e197c129b1fcb1eea9359ea6d)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:1155

[bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::num\_subgroups](structbt__cap__commander__broadcast__reception__stop__member__param.md#aeeab53e8bd7ae4f36433c0d4b60c313b)

size\_t num\_subgroups

Number of subgroups.

**Definition** cap.h:1161

[bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md)

Parameters for stopping broadcast reception.

**Definition** cap.h:1165

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::type](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1167

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::param](structbt__cap__commander__broadcast__reception__stop__param.md#a36ce7cd132cd41a55872985433c2934d)

struct bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:1170

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::count](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593)

size\_t count

The number of parameters in param.

**Definition** cap.h:1173

[bt\_cap\_commander\_cb](structbt__cap__commander__cb.md)

Callback structure for CAP procedures.

**Definition** cap.h:907

[bt\_cap\_commander\_cb::broadcast\_reception\_start](structbt__cap__commander__cb.md#a14f6a51db5a76aac015a5de617712af3)

void(\* broadcast\_reception\_start)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_broadcast\_reception\_start().

**Definition** cap.h:1002

[bt\_cap\_commander\_cb::microphone\_gain\_changed](structbt__cap__commander__cb.md#a1e83872924e1aa1293c499184ade9173)

void(\* microphone\_gain\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_microphone\_gain\_setting().

**Definition** cap.h:987

[bt\_cap\_commander\_cb::broadcast\_reception\_stop](structbt__cap__commander__cb.md#a2188c52e3daf0a695d7c42e6cac561cf)

void(\* broadcast\_reception\_stop)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_broadcast\_reception\_stop().

**Definition** cap.h:1013

[bt\_cap\_commander\_cb::volume\_changed](structbt__cap__commander__cb.md#a3a7777603c23c14bc9d01cf29bc70ef7)

void(\* volume\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_volume().

**Definition** cap.h:936

[bt\_cap\_commander\_cb::volume\_offset\_changed](structbt__cap__commander__cb.md#a3bacfffef8d122db4574463777dfd507)

void(\* volume\_offset\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_volume\_offset().

**Definition** cap.h:961

[bt\_cap\_commander\_cb::distribute\_broadcast\_code](structbt__cap__commander__cb.md#a7dfa1903f5cd71e67b6da0f5ff2fb299)

void(\* distribute\_broadcast\_code)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_distribute\_broadcast\_code().

**Definition** cap.h:1024

[bt\_cap\_commander\_cb::microphone\_mute\_changed](structbt__cap__commander__cb.md#aa49e7eaf5c45d70c800f28b81f9967e5)

void(\* microphone\_mute\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_microphone\_mute\_state().

**Definition** cap.h:975

[bt\_cap\_commander\_cb::volume\_mute\_changed](structbt__cap__commander__cb.md#acc9fcedf7f7abe86e055d48e6df124c7)

void(\* volume\_mute\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_volume\_mute\_state().

**Definition** cap.h:948

[bt\_cap\_commander\_cb::discovery\_complete](structbt__cap__commander__cb.md#af989b3ebe7e5cc83a1ca4b2ef080e14d)

void(\* discovery\_complete)(struct bt\_conn \*conn, int err, const struct bt\_csip\_set\_coordinator\_set\_member \*member, const struct bt\_csip\_set\_coordinator\_csis\_inst \*csis\_inst)

Callback for bt\_cap\_initiator\_unicast\_discover().

**Definition** cap.h:921

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md)

Parameters part of bt\_cap\_commander\_change\_microphone\_gain\_setting\_param for bt\_cap\_commander\_change\_...

**Definition** cap.h:1355

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param::member](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:1357

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param::gain](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196)

int8\_t gain

The microphone gain setting to set.

**Definition** cap.h:1360

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md)

Parameters for changing microphone mute state.

**Definition** cap.h:1364

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::type](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1366

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::param](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8)

struct bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:1369

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::count](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349)

size\_t count

The number of parameters in param.

**Definition** cap.h:1372

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md)

Parameters for changing microphone mute state.

**Definition** cap.h:1323

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::mute](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8)

bool mute

The microphone mute state to set.

**Definition** cap.h:1338

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::count](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e)

size\_t count

The number of members in members.

**Definition** cap.h:1331

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::members](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:1328

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::type](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1325

[bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md)

Parameters for changing volume mute state.

**Definition** cap.h:1294

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::count](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8)

size\_t count

The number of members in members.

**Definition** cap.h:1302

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::mute](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd)

bool mute

The volume mute state to set.

**Definition** cap.h:1309

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::type](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1296

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::members](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:1299

[bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md)

Parameters part of bt\_cap\_commander\_change\_volume\_offset\_param for bt\_cap\_commander\_change\_volume\_off...

**Definition** cap.h:1259

[bt\_cap\_commander\_change\_volume\_offset\_member\_param::offset](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8)

int16\_t offset

The offset to set.

**Definition** cap.h:1268

[bt\_cap\_commander\_change\_volume\_offset\_member\_param::member](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:1261

[bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md)

Parameters for changing volume offset.

**Definition** cap.h:1272

[bt\_cap\_commander\_change\_volume\_offset\_param::param](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d)

struct bt\_cap\_commander\_change\_volume\_offset\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:1277

[bt\_cap\_commander\_change\_volume\_offset\_param::type](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1274

[bt\_cap\_commander\_change\_volume\_offset\_param::count](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b)

size\_t count

The number of parameters in param.

**Definition** cap.h:1280

[bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md)

Parameters for changing absolute volume.

**Definition** cap.h:1232

[bt\_cap\_commander\_change\_volume\_param::count](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640)

size\_t count

The number of members in members.

**Definition** cap.h:1240

[bt\_cap\_commander\_change\_volume\_param::members](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:1237

[bt\_cap\_commander\_change\_volume\_param::type](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1234

[bt\_cap\_commander\_change\_volume\_param::volume](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49)

uint8\_t volume

The absolute volume to set.

**Definition** cap.h:1243

[bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param](structbt__cap__commander__distribute__broadcast__code__member__param.md)

Member parameters for distributing broadcast code.

**Definition** cap.h:1188

[bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param::member](structbt__cap__commander__distribute__broadcast__code__member__param.md#acd5d185c590ea9a64faebd354a3d5d4a)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:1190

[bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param::src\_id](structbt__cap__commander__distribute__broadcast__code__member__param.md#ad240bb7e1e9ad5c40eb1a031a6fbc2fe)

uint8\_t src\_id

Source ID of the receive state.

**Definition** cap.h:1193

[bt\_cap\_commander\_distribute\_broadcast\_code\_param](structbt__cap__commander__distribute__broadcast__code__param.md)

Parameters for distributing broadcast code.

**Definition** cap.h:1197

[bt\_cap\_commander\_distribute\_broadcast\_code\_param::param](structbt__cap__commander__distribute__broadcast__code__param.md#a03be4b2fac7803de233c8a1024640cc2)

struct bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:1202

[bt\_cap\_commander\_distribute\_broadcast\_code\_param::count](structbt__cap__commander__distribute__broadcast__code__param.md#a86316e3bf53edca67e0743072f0f2ee3)

size\_t count

The number of parameters in param.

**Definition** cap.h:1205

[bt\_cap\_commander\_distribute\_broadcast\_code\_param::type](structbt__cap__commander__distribute__broadcast__code__param.md#a9605ad1590ff0279b46d639d38278933)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1199

[bt\_cap\_commander\_distribute\_broadcast\_code\_param::broadcast\_code](structbt__cap__commander__distribute__broadcast__code__param.md#ac7d426c975c1e2324f52486abf9298b9)

uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]

16-octet broadcast code.

**Definition** cap.h:1217

[bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md)

Parameters for \* bt\_cap\_initiator\_broadcast\_audio\_create().

**Definition** cap.h:637

[bt\_cap\_initiator\_broadcast\_create\_param::pto](structbt__cap__initiator__broadcast__create__param.md#a01d6ffb369caaf808d4b55b3b1748890)

uint8\_t pto

Pre-transmission offset.

**Definition** cap.h:690

[bt\_cap\_initiator\_broadcast\_create\_param::qos](structbt__cap__initiator__broadcast__create__param.md#a142125e620776aed464d90f280ef1a4c)

struct bt\_bap\_qos\_cfg \* qos

Quality of Service configuration.

**Definition** cap.h:645

[bt\_cap\_initiator\_broadcast\_create\_param::subgroup\_params](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839)

struct bt\_cap\_initiator\_broadcast\_subgroup\_param \* subgroup\_params

Array of stream parameters.

**Definition** cap.h:642

[bt\_cap\_initiator\_broadcast\_create\_param::encryption](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542)

bool encryption

Whether or not to encrypt the streams.

**Definition** cap.h:657

[bt\_cap\_initiator\_broadcast\_create\_param::irc](structbt__cap__initiator__broadcast__create__param.md#a6f562b7a696472b7784ca2e1ced4997a)

uint8\_t irc

Immediate Repetition Count.

**Definition** cap.h:681

[bt\_cap\_initiator\_broadcast\_create\_param::iso\_interval](structbt__cap__initiator__broadcast__create__param.md#a8eedd8f9a896931f75642576ca37c7d5)

uint16\_t iso\_interval

ISO interval.

**Definition** cap.h:699

[bt\_cap\_initiator\_broadcast\_create\_param::broadcast\_code](structbt__cap__initiator__broadcast__create__param.md#aa4d6fbd5bd13963004e381b987bbeb4d)

uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]

16-octet broadcast code.

**Definition** cap.h:671

[bt\_cap\_initiator\_broadcast\_create\_param::packing](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc)

uint8\_t packing

Broadcast Source packing mode.

**Definition** cap.h:654

[bt\_cap\_initiator\_broadcast\_create\_param::subgroup\_count](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b)

size\_t subgroup\_count

The number of parameters in subgroup\_params.

**Definition** cap.h:639

[bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md)

Parameters part of bt\_cap\_initiator\_broadcast\_subgroup\_param for bt\_cap\_initiator\_broadcast\_audio\_cre...

**Definition** cap.h:607

[bt\_cap\_initiator\_broadcast\_stream\_param::data](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869)

uint8\_t \* data

BIS Codec Specific Configuration.

**Definition** cap.h:618

[bt\_cap\_initiator\_broadcast\_stream\_param::stream](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a)

struct bt\_cap\_stream \* stream

Audio stream.

**Definition** cap.h:609

[bt\_cap\_initiator\_broadcast\_stream\_param::data\_len](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4)

size\_t data\_len

The length of the p data array.

**Definition** cap.h:615

[bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md)

Parameters part of bt\_cap\_initiator\_broadcast\_create\_param for bt\_cap\_initiator\_broadcast\_audio\_creat...

**Definition** cap.h:625

[bt\_cap\_initiator\_broadcast\_subgroup\_param::stream\_params](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a)

struct bt\_cap\_initiator\_broadcast\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:630

[bt\_cap\_initiator\_broadcast\_subgroup\_param::stream\_count](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769)

size\_t stream\_count

The number of parameters in stream\_params.

**Definition** cap.h:627

[bt\_cap\_initiator\_broadcast\_subgroup\_param::codec\_cfg](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Subgroup Codec configuration.

**Definition** cap.h:633

[bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md)

Callback structure for CAP procedures.

**Definition** cap.h:78

[bt\_cap\_initiator\_cb::unicast\_stop\_complete](structbt__cap__initiator__cb.md#a2e910a82209d144878b6c69c1b2723ba)

void(\* unicast\_stop\_complete)(int err, struct bt\_conn \*conn)

Callback for bt\_cap\_initiator\_unicast\_audio\_stop().

**Definition** cap.h:132

[bt\_cap\_initiator\_cb::unicast\_discovery\_complete](structbt__cap__initiator__cb.md#a642a2f48e8f870bb1681ba58aa119de9)

void(\* unicast\_discovery\_complete)(struct bt\_conn \*conn, int err, const struct bt\_csip\_set\_coordinator\_set\_member \*member, const struct bt\_csip\_set\_coordinator\_csis\_inst \*csis\_inst)

Callback for bt\_cap\_initiator\_unicast\_discover().

**Definition** cap.h:93

[bt\_cap\_initiator\_cb::unicast\_update\_complete](structbt__cap__initiator__cb.md#a95266741841fca83cd2769c76652154e)

void(\* unicast\_update\_complete)(int err, struct bt\_conn \*conn)

Callback for bt\_cap\_initiator\_unicast\_audio\_update().

**Definition** cap.h:120

[bt\_cap\_initiator\_cb::unicast\_start\_complete](structbt__cap__initiator__cb.md#aa70de1dda73ffdcbb8287f8f174984ea)

void(\* unicast\_start\_complete)(int err, struct bt\_conn \*conn)

Callback for bt\_cap\_initiator\_unicast\_audio\_start().

**Definition** cap.h:108

[bt\_cap\_stream](structbt__cap__stream.md)

Common Audio Profile stream structure.

**Definition** cap.h:190

[bt\_cap\_stream::ops](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba)

struct bt\_bap\_stream\_ops \* ops

Audio stream operations.

**Definition** cap.h:195

[bt\_cap\_stream::bap\_stream](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18)

struct bt\_bap\_stream bap\_stream

The underlying BAP audio stream.

**Definition** cap.h:192

[bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_start() function.

**Definition** cap.h:452

[bt\_cap\_unicast\_audio\_start\_param::type](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:454

[bt\_cap\_unicast\_audio\_start\_param::count](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667)

size\_t count

The number of parameters in stream\_params.

**Definition** cap.h:457

[bt\_cap\_unicast\_audio\_start\_param::stream\_params](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b)

struct bt\_cap\_unicast\_audio\_start\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:460

[bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md)

Stream specific parameters for the bt\_cap\_initiator\_unicast\_audio\_start() function.

**Definition** cap.h:428

[bt\_cap\_unicast\_audio\_start\_stream\_param::stream](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e)

struct bt\_cap\_stream \* stream

Stream for the member.

**Definition** cap.h:433

[bt\_cap\_unicast\_audio\_start\_stream\_param::codec\_cfg](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Codec configuration.

**Definition** cap.h:448

[bt\_cap\_unicast\_audio\_start\_stream\_param::member](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:430

[bt\_cap\_unicast\_audio\_start\_stream\_param::ep](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb)

struct bt\_bap\_ep \* ep

Endpoint reference for the stream.

**Definition** cap.h:436

[bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_stop() function.

**Definition** cap.h:492

[bt\_cap\_unicast\_audio\_stop\_param::count](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2)

size\_t count

The number of streams in streams.

**Definition** cap.h:497

[bt\_cap\_unicast\_audio\_stop\_param::release](structbt__cap__unicast__audio__stop__param.md#a1cbd7ee2e4ceafd2da2858dc7c941d78)

bool release

Whether to release the streams after they have stopped.

**Definition** cap.h:503

[bt\_cap\_unicast\_audio\_stop\_param::type](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:494

[bt\_cap\_unicast\_audio\_stop\_param::streams](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82)

struct bt\_cap\_stream \*\* streams

Array of streams to stop.

**Definition** cap.h:500

[bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_update() function.

**Definition** cap.h:480

[bt\_cap\_unicast\_audio\_update\_param::stream\_params](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb)

struct bt\_cap\_unicast\_audio\_update\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:488

[bt\_cap\_unicast\_audio\_update\_param::type](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:482

[bt\_cap\_unicast\_audio\_update\_param::count](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1)

size\_t count

The number of parameters in stream\_params.

**Definition** cap.h:485

[bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md)

Stream specific parameters for the bt\_cap\_initiator\_unicast\_audio\_update() function.

**Definition** cap.h:464

[bt\_cap\_unicast\_audio\_update\_stream\_param::meta\_len](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c)

size\_t meta\_len

The length of meta.

**Definition** cap.h:469

[bt\_cap\_unicast\_audio\_update\_stream\_param::stream](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1)

struct bt\_cap\_stream \* stream

Stream to update.

**Definition** cap.h:466

[bt\_cap\_unicast\_audio\_update\_stream\_param::meta](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0)

uint8\_t \* meta

The new metadata.

**Definition** cap.h:476

[bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md)

Parameters for the creating unicast groups with bt\_cap\_unicast\_group\_create().

**Definition** cap.h:284

[bt\_cap\_unicast\_group\_param::params](structbt__cap__unicast__group__param.md#a64ca2c5cc4f34821e567841ec8efe67b)

struct bt\_cap\_unicast\_group\_stream\_pair\_param \* params

Array of stream parameters.

**Definition** cap.h:289

[bt\_cap\_unicast\_group\_param::packing](structbt__cap__unicast__group__param.md#a97e67b903e72dd1f0fef4961810288b1)

uint8\_t packing

Unicast Group packing mode.

**Definition** cap.h:298

[bt\_cap\_unicast\_group\_param::p\_to\_c\_ft](structbt__cap__unicast__group__param.md#ab424be389b026ac5857e3bec1c3d686f)

uint8\_t p\_to\_c\_ft

Peripheral to Central flush timeout.

**Definition** cap.h:319

[bt\_cap\_unicast\_group\_param::params\_count](structbt__cap__unicast__group__param.md#ab9748e9e230048af64ce9c9ce1006952)

size\_t params\_count

The number of parameters in params.

**Definition** cap.h:286

[bt\_cap\_unicast\_group\_param::iso\_interval](structbt__cap__unicast__group__param.md#ac52a0e09e3978a084e4fe558e4a5a848)

uint16\_t iso\_interval

ISO interval.

**Definition** cap.h:328

[bt\_cap\_unicast\_group\_param::c\_to\_p\_ft](structbt__cap__unicast__group__param.md#adb6cb5686b3d827156aef325b3dcdc84)

uint8\_t c\_to\_p\_ft

Central to Peripheral flush timeout.

**Definition** cap.h:309

[bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md)

Parameter struct for the unicast group functions.

**Definition** cap.h:275

[bt\_cap\_unicast\_group\_stream\_pair\_param::rx\_param](structbt__cap__unicast__group__stream__pair__param.md#a19d49ab8c0daa7e6a4c73563952ae461)

struct bt\_cap\_unicast\_group\_stream\_param \* rx\_param

Pointer to a receiving stream parameters.

**Definition** cap.h:277

[bt\_cap\_unicast\_group\_stream\_pair\_param::tx\_param](structbt__cap__unicast__group__stream__pair__param.md#a6edeca159371f3a70cc5a1f662a0e45c)

struct bt\_cap\_unicast\_group\_stream\_param \* tx\_param

Pointer to a transmitting stream parameters.

**Definition** cap.h:280

[bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md)

Parameter struct for each stream in the unicast group.

**Definition** cap.h:261

[bt\_cap\_unicast\_group\_stream\_param::stream](structbt__cap__unicast__group__stream__param.md#a16aacd43bb7b449648ab6a5a89999fba)

struct bt\_cap\_stream \* stream

Pointer to a stream object.

**Definition** cap.h:263

[bt\_cap\_unicast\_group\_stream\_param::qos\_cfg](structbt__cap__unicast__group__stream__param.md#af55f6b576509853d39b1fe68bcec348a)

struct bt\_bap\_qos\_cfg \* qos\_cfg

The QoS settings for the stream object.

**Definition** cap.h:266

[bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md)

Parameters for bt\_cap\_initiator\_unicast\_to\_broadcast().

**Definition** cap.h:816

[bt\_cap\_unicast\_to\_broadcast\_param::unicast\_group](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239)

struct bt\_bap\_unicast\_group \* unicast\_group

The source unicast group with the streams.

**Definition** cap.h:818

[bt\_cap\_unicast\_to\_broadcast\_param::broadcast\_code](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3)

uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]

16-octet broadcast code.

**Definition** cap.h:840

[bt\_cap\_unicast\_to\_broadcast\_param::encrypt](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262)

bool encrypt

Whether or not to encrypt the streams.

**Definition** cap.h:826

[bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md)

Struct representing a coordinated set instance on a remote device.

**Definition** csip.h:357

[bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md)

Struct representing a remote device as a set member.

**Definition** csip.h:366

[bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md)

Register structure for Coordinated Set Identification Service.

**Definition** csip.h:134

[bt\_iso\_tx\_info](structbt__iso__tx__info.md)

ISO Meta Data structure for transmitted ISO packets.

**Definition** iso.h:373

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[bt\_cap\_set\_member](unionbt__cap__set__member.md)

Represents a Common Audio Set member that are either in a Coordinated or ad-hoc set.

**Definition** cap.h:176

[bt\_cap\_set\_member::member](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973)

struct bt\_conn \* member

Connection pointer if the type is BT\_CAP\_SET\_TYPE\_AD\_HOC.

**Definition** cap.h:178

[bt\_cap\_set\_member::csip](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6)

struct bt\_csip\_set\_coordinator\_csis\_inst \* csip

CSIP Coordinated Set struct used if type is BT\_CAP\_SET\_TYPE\_CSIP.

**Definition** cap.h:181

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [cap.h](bluetooth_2audio_2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
