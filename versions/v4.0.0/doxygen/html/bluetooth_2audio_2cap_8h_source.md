---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bluetooth_2audio_2cap_8h_source.html
original_path: doxygen/html/bluetooth_2audio_2cap_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cap.h

[Go to the documentation of this file.](bluetooth_2audio_2cap_8h.md)

1

5

6/\*

7 \* Copyright (c) 2022-2024 Nordic Semiconductor ASA

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

[ 71](group__bt__cap.md#gafcb9ea2122ff8058321cf85a22326abe)int [bt\_cap\_acceptor\_register](group__bt__cap.md#gafcb9ea2122ff8058321cf85a22326abe)(const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param,

72 struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst);

73

[ 75](structbt__cap__initiator__cb.md)struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) {

76#if defined(CONFIG\_BT\_BAP\_UNICAST\_CLIENT) || defined(\_\_DOXYGEN\_\_)

[ 90](structbt__cap__initiator__cb.md#a642a2f48e8f870bb1681ba58aa119de9) void (\*[unicast\_discovery\_complete](structbt__cap__initiator__cb.md#a642a2f48e8f870bb1681ba58aa119de9))(

91 struct bt\_conn \*conn, int err,

92 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member,

93 const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst);

94

[ 105](structbt__cap__initiator__cb.md#aa70de1dda73ffdcbb8287f8f174984ea) void (\*[unicast\_start\_complete](structbt__cap__initiator__cb.md#aa70de1dda73ffdcbb8287f8f174984ea))(int err, struct bt\_conn \*conn);

106

[ 117](structbt__cap__initiator__cb.md#a95266741841fca83cd2769c76652154e) void (\*[unicast\_update\_complete](structbt__cap__initiator__cb.md#a95266741841fca83cd2769c76652154e))(int err, struct bt\_conn \*conn);

118

[ 129](structbt__cap__initiator__cb.md#a2e910a82209d144878b6c69c1b2723ba) void (\*[unicast\_stop\_complete](structbt__cap__initiator__cb.md#a2e910a82209d144878b6c69c1b2723ba))(int err, struct bt\_conn \*conn);

130#endif /\* CONFIG\_BT\_BAP\_UNICAST\_CLIENT \*/

131};

132

[ 146](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d)int [bt\_cap\_initiator\_unicast\_discover](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d)(struct bt\_conn \*conn);

147

[ 149](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a)enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) {

[ 151](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468) [BT\_CAP\_SET\_TYPE\_AD\_HOC](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468),

[ 153](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4) [BT\_CAP\_SET\_TYPE\_CSIP](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4),

154};

155

[ 157](unionbt__cap__set__member.md)union [bt\_cap\_set\_member](unionbt__cap__set__member.md) {

[ 159](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973) struct bt\_conn \*[member](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973);

160

[ 162](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6) struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*[csip](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6);

163};

164

[ 171](structbt__cap__stream.md)struct [bt\_cap\_stream](structbt__cap__stream.md) {

[ 173](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18) struct [bt\_bap\_stream](structbt__bap__stream.md) [bap\_stream](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18);

174

[ 176](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba) struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*[ops](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba);

177};

178

[ 187](group__bt__cap.md#gac909b00d53cf35103382f0e1d9f426b7)void [bt\_cap\_stream\_ops\_register](group__bt__cap.md#gac909b00d53cf35103382f0e1d9f426b7)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*ops);

188

[ 204](group__bt__cap.md#ga2d8b15543105078b793462b762e27741)int [bt\_cap\_stream\_send](group__bt__cap.md#ga2d8b15543105078b793462b762e27741)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num);

205

[ 223](group__bt__cap.md#ga23618d1ab7690c4d3a567228c857c89e)int [bt\_cap\_stream\_send\_ts](group__bt__cap.md#ga23618d1ab7690c4d3a567228c857c89e)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num,

224 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

225

[ 239](group__bt__cap.md#ga7f3f6e98e7720a4711b658c4b7c85235)int [bt\_cap\_stream\_get\_tx\_sync](group__bt__cap.md#ga7f3f6e98e7720a4711b658c4b7c85235)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info);

240

[ 242](structbt__cap__unicast__audio__start__stream__param.md)struct [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md) {

[ 244](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b);

245

[ 247](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e);

248

[ 250](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb) struct bt\_bap\_ep \*[ep](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb);

251

[ 262](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a);

263};

264

[ 266](structbt__cap__unicast__audio__start__param.md)struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) {

[ 268](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5);

269

[ 271](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667) size\_t [count](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667);

272

[ 274](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b) struct [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md) \*[stream\_params](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b);

275};

276

[ 278](structbt__cap__unicast__audio__update__stream__param.md)struct [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) {

[ 280](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1);

281

[ 283](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c) size\_t [meta\_len](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c);

284

[ 290](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[meta](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0);

291};

292

[ 294](structbt__cap__unicast__audio__update__param.md)struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) {

[ 296](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd);

297

[ 299](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1) size\_t [count](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1);

300

[ 302](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb) struct [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) \*[stream\_params](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb);

303};

304

[ 306](structbt__cap__unicast__audio__stop__param.md)struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) {

[ 308](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa);

309

[ 311](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2) size\_t [count](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2);

312

[ 314](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82) struct [bt\_cap\_stream](structbt__cap__stream.md) \*\*[streams](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82);

315

[ 317](structbt__cap__unicast__audio__stop__param.md#a1cbd7ee2e4ceafd2da2858dc7c941d78) bool [release](structbt__cap__unicast__audio__stop__param.md#a1cbd7ee2e4ceafd2da2858dc7c941d78);

318};

319

[ 327](group__bt__cap.md#ga54d7ad68f376998510aad9c3702e9364)int [bt\_cap\_initiator\_register\_cb](group__bt__cap.md#ga54d7ad68f376998510aad9c3702e9364)(const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb);

328

[ 337](group__bt__cap.md#gaa7286837f37da38afec8c5c955306b61)int [bt\_cap\_initiator\_unregister\_cb](group__bt__cap.md#gaa7286837f37da38afec8c5c955306b61)(const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb);

338

[ 357](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184)int [bt\_cap\_initiator\_unicast\_audio\_start](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184)(const struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) \*param);

358

[ 372](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639)int [bt\_cap\_initiator\_unicast\_audio\_update](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639)(const struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) \*param);

373

[ 390](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f)int [bt\_cap\_initiator\_unicast\_audio\_stop](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f)(const struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) \*param);

391

[ 415](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f)int [bt\_cap\_initiator\_unicast\_audio\_cancel](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f)(void);

416

[ 421](structbt__cap__initiator__broadcast__stream__param.md)struct [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) {

[ 423](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a);

424

[ 429](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4) size\_t [data\_len](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4);

430

[ 432](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869);

433};

434

[ 439](structbt__cap__initiator__broadcast__subgroup__param.md)struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) {

[ 441](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769) size\_t [stream\_count](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769);

442

[ 444](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a) struct [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) \*[stream\_params](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a);

445

[ 447](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47);

448};

449

[ 451](structbt__cap__initiator__broadcast__create__param.md)struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) {

[ 453](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b) size\_t [subgroup\_count](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b);

454

[ 456](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839) struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) \*[subgroup\_params](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839);

457

[ 459](structbt__cap__initiator__broadcast__create__param.md#a142125e620776aed464d90f280ef1a4c) struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*[qos](structbt__cap__initiator__broadcast__create__param.md#a142125e620776aed464d90f280ef1a4c);

460

[ 468](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc);

469

[ 471](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542) bool [encryption](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542);

472

[ 485](structbt__cap__initiator__broadcast__create__param.md#aa4d6fbd5bd13963004e381b987bbeb4d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__cap__initiator__broadcast__create__param.md#aa4d6fbd5bd13963004e381b987bbeb4d)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

486

487#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 495](structbt__cap__initiator__broadcast__create__param.md#a6f562b7a696472b7784ca2e1ced4997a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__cap__initiator__broadcast__create__param.md#a6f562b7a696472b7784ca2e1ced4997a);

496

[ 504](structbt__cap__initiator__broadcast__create__param.md#a01d6ffb369caaf808d4b55b3b1748890) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__cap__initiator__broadcast__create__param.md#a01d6ffb369caaf808d4b55b3b1748890);

505

[ 513](structbt__cap__initiator__broadcast__create__param.md#a8eedd8f9a896931f75642576ca37c7d5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__cap__initiator__broadcast__create__param.md#a8eedd8f9a896931f75642576ca37c7d5);

514#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

515};

516

[ 531](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4)int [bt\_cap\_initiator\_broadcast\_audio\_create](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4)(

532 const struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) \*param,

533 struct bt\_cap\_broadcast\_source \*\*broadcast\_source);

534

[ 554](group__bt__cap.md#ga2bd5f9c9de719a14ffc69827dbd4fa24)int [bt\_cap\_initiator\_broadcast\_audio\_start](group__bt__cap.md#ga2bd5f9c9de719a14ffc69827dbd4fa24)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

555 struct bt\_le\_ext\_adv \*adv);

[ 570](group__bt__cap.md#ga92336c4a56c667b608a86e45eb8d5073)int [bt\_cap\_initiator\_broadcast\_audio\_update](group__bt__cap.md#ga92336c4a56c667b608a86e45eb8d5073)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

571 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

572

[ 585](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e)int [bt\_cap\_initiator\_broadcast\_audio\_stop](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e)(struct bt\_cap\_broadcast\_source \*broadcast\_source);

586

[ 604](group__bt__cap.md#gac98ed5112d0ce0659bde86d149ea7b4c)int [bt\_cap\_initiator\_broadcast\_audio\_delete](group__bt__cap.md#gac98ed5112d0ce0659bde86d149ea7b4c)(struct bt\_cap\_broadcast\_source \*broadcast\_source);

605

[ 621](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)int [bt\_cap\_initiator\_broadcast\_get\_base](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

622 struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf);

623

[ 625](structbt__cap__unicast__to__broadcast__param.md)struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) {

[ 627](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239) struct bt\_bap\_unicast\_group \*[unicast\_group](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239);

628

[ 635](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262) bool [encrypt](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262);

636

[ 649](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

650};

651

[ 668](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558)int [bt\_cap\_initiator\_unicast\_to\_broadcast](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558)(const struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) \*param,

669 struct bt\_cap\_broadcast\_source \*\*source);

670

[ 672](structbt__cap__broadcast__to__unicast__param.md)struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) {

[ 678](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9) struct bt\_cap\_broadcast\_source \*[broadcast\_source](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9);

679

[ 681](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf);

682

[ 690](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce) size\_t [count](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce);

691

[ 693](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*\*[members](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed);

694};

695

[ 712](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b)int [bt\_cap\_initiator\_broadcast\_to\_unicast](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b)(const struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) \*param,

713 struct bt\_bap\_unicast\_group \*\*unicast\_group);

714

[ 716](structbt__cap__commander__cb.md)struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) {

[ 730](structbt__cap__commander__cb.md#af989b3ebe7e5cc83a1ca4b2ef080e14d) void (\*[discovery\_complete](structbt__cap__commander__cb.md#af989b3ebe7e5cc83a1ca4b2ef080e14d))(struct bt\_conn \*conn, int err,

731 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member,

732 const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst);

733

734#if defined(CONFIG\_BT\_VCP\_VOL\_CTLR) || defined(\_\_DOXYGEN\_\_)

[ 745](structbt__cap__commander__cb.md#a3a7777603c23c14bc9d01cf29bc70ef7) void (\*[volume\_changed](structbt__cap__commander__cb.md#a3a7777603c23c14bc9d01cf29bc70ef7))(struct bt\_conn \*conn, int err);

746

[ 757](structbt__cap__commander__cb.md#acc9fcedf7f7abe86e055d48e6df124c7) void (\*[volume\_mute\_changed](structbt__cap__commander__cb.md#acc9fcedf7f7abe86e055d48e6df124c7))(struct bt\_conn \*conn, int err);

758

759#if defined(CONFIG\_BT\_VCP\_VOL\_CTLR\_VOCS) || defined(\_\_DOXYGEN\_\_)

[ 770](structbt__cap__commander__cb.md#a3bacfffef8d122db4574463777dfd507) void (\*[volume\_offset\_changed](structbt__cap__commander__cb.md#a3bacfffef8d122db4574463777dfd507))(struct bt\_conn \*conn, int err);

771#endif /\* CONFIG\_BT\_VCP\_VOL\_CTLR\_VOCS \*/

772#endif /\* CONFIG\_BT\_VCP\_VOL\_CTLR \*/

773#if defined(CONFIG\_BT\_MICP\_MIC\_CTLR) || defined(\_\_DOXYGEN\_\_)

[ 784](structbt__cap__commander__cb.md#aa49e7eaf5c45d70c800f28b81f9967e5) void (\*[microphone\_mute\_changed](structbt__cap__commander__cb.md#aa49e7eaf5c45d70c800f28b81f9967e5))(struct bt\_conn \*conn, int err);

785#if defined(CONFIG\_BT\_MICP\_MIC\_CTLR\_AICS) || defined(\_\_DOXYGEN\_\_)

[ 796](structbt__cap__commander__cb.md#a1e83872924e1aa1293c499184ade9173) void (\*[microphone\_gain\_changed](structbt__cap__commander__cb.md#a1e83872924e1aa1293c499184ade9173))(struct bt\_conn \*conn, int err);

797#endif /\* CONFIG\_BT\_MICP\_MIC\_CTLR\_AICS \*/

798#endif /\* CONFIG\_BT\_MICP\_MIC\_CTLR \*/

799

800#if defined(CONFIG\_BT\_BAP\_BROADCAST\_ASSISTANT) || defined(\_\_DOXYGEN\_\_)

[ 811](structbt__cap__commander__cb.md#a14f6a51db5a76aac015a5de617712af3) void (\*[broadcast\_reception\_start](structbt__cap__commander__cb.md#a14f6a51db5a76aac015a5de617712af3))(struct bt\_conn \*conn, int err);

[ 822](structbt__cap__commander__cb.md#a2188c52e3daf0a695d7c42e6cac561cf) void (\*[broadcast\_reception\_stop](structbt__cap__commander__cb.md#a2188c52e3daf0a695d7c42e6cac561cf))(struct bt\_conn \*conn, int err);

823#endif /\* CONFIG\_BT\_BAP\_BROADCAST\_ASSISTANT \*/

824};

825

[ 835](group__bt__cap.md#gab6239c91b9d210872396860619fb8687)int [bt\_cap\_commander\_register\_cb](group__bt__cap.md#gab6239c91b9d210872396860619fb8687)(const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb);

836

[ 845](group__bt__cap.md#ga38928945e67835983de3fc639c8f2764)int [bt\_cap\_commander\_unregister\_cb](group__bt__cap.md#ga38928945e67835983de3fc639c8f2764)(const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb);

846

[ 865](group__bt__cap.md#ga165c67bddcbe220050293a4c73fb6ede)int [bt\_cap\_commander\_discover](group__bt__cap.md#ga165c67bddcbe220050293a4c73fb6ede)(struct bt\_conn \*conn);

866

[ 890](group__bt__cap.md#ga7abf029533fed391930257605f3c752c)int [bt\_cap\_commander\_cancel](group__bt__cap.md#ga7abf029533fed391930257605f3c752c)(void);

891

[ 896](structbt__cap__commander__broadcast__reception__start__member__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) {

[ 898](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7);

899

[ 901](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e);

902

[ 904](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362);

905

[ 911](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pa\_interval](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c);

912

[ 914](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0);

915

[ 921](structbt__cap__commander__broadcast__reception__start__member__param.md#af1d74b691a3fe3d590b355d47112240b) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) [subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#af1d74b691a3fe3d590b355d47112240b)[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS];

922

[ 924](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63) size\_t [num\_subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63);

925};

926

[ 928](structbt__cap__commander__broadcast__reception__start__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) {

[ 930](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1);

931

[ 933](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041) struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) \*[param](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041);

934

[ 936](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7) size\_t [count](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7);

937};

938

[ 947](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9)int [bt\_cap\_commander\_broadcast\_reception\_start](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9)(

948 const struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) \*param);

949

951

[ 952](structbt__cap__commander__broadcast__reception__stop__member__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md) {

[ 954](structbt__cap__commander__broadcast__reception__stop__member__param.md#aa934af2e197c129b1fcb1eea9359ea6d) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__broadcast__reception__stop__member__param.md#aa934af2e197c129b1fcb1eea9359ea6d);

955

[ 957](structbt__cap__commander__broadcast__reception__stop__member__param.md#a72d606f6a83b1c84aa41d9db22cb955a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [src\_id](structbt__cap__commander__broadcast__reception__stop__member__param.md#a72d606f6a83b1c84aa41d9db22cb955a);

958

[ 960](structbt__cap__commander__broadcast__reception__stop__member__param.md#aeeab53e8bd7ae4f36433c0d4b60c313b) size\_t [num\_subgroups](structbt__cap__commander__broadcast__reception__stop__member__param.md#aeeab53e8bd7ae4f36433c0d4b60c313b);

961};

962

[ 963](structbt__cap__commander__broadcast__reception__stop__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) {

[ 965](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460);

966

[ 968](structbt__cap__commander__broadcast__reception__stop__param.md#a36ce7cd132cd41a55872985433c2934d) struct [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md) \*[param](structbt__cap__commander__broadcast__reception__stop__param.md#a36ce7cd132cd41a55872985433c2934d);

969

[ 971](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593) size\_t [count](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593);

972};

973

[ 982](group__bt__cap.md#gac5b2b6d617a092fb98b23c41b2f52d15)int [bt\_cap\_commander\_broadcast\_reception\_stop](group__bt__cap.md#gac5b2b6d617a092fb98b23c41b2f52d15)(

983 const struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) \*param);

984

[ 986](structbt__cap__commander__change__volume__param.md)struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) {

[ 988](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88);

989

[ 991](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531);

992

[ 994](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640) size\_t [count](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640);

995

[ 997](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [volume](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49);

998};

999

[ 1007](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6)int [bt\_cap\_commander\_change\_volume](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6)(const struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) \*param);

1008

[ 1013](structbt__cap__commander__change__volume__offset__member__param.md)struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) {

[ 1015](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4);

1016

[ 1022](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [offset](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8);

1023};

1024

[ 1026](structbt__cap__commander__change__volume__offset__param.md)struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) {

[ 1028](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd);

1029

[ 1031](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d) struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) \*[param](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d);

1032

[ 1034](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b) size\_t [count](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b);

1035};

1036

[ 1044](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa)int [bt\_cap\_commander\_change\_volume\_offset](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa)(

1045 const struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) \*param);

1046

[ 1048](structbt__cap__commander__change__volume__mute__state__param.md)struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) {

[ 1050](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775);

1051

[ 1053](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1);

1054

[ 1056](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8) size\_t [count](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8);

1057

[ 1063](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd) bool [mute](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd);

1064};

1065

[ 1073](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4)int [bt\_cap\_commander\_change\_volume\_mute\_state](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4)(

1074 const struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) \*param);

1075

[ 1077](structbt__cap__commander__change__microphone__mute__state__param.md)struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) {

[ 1079](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0);

1080

[ 1082](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1);

1083

[ 1085](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e) size\_t [count](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e);

1086

[ 1092](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8) bool [mute](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8);

1093};

1094

[ 1102](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54)int [bt\_cap\_commander\_change\_microphone\_mute\_state](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54)(

1103 const struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) \*param);

1104

[ 1109](structbt__cap__commander__change__microphone__gain__setting__member__param.md)struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) {

[ 1111](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e);

1112

[ 1114](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [gain](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196);

1115};

1116

[ 1118](structbt__cap__commander__change__microphone__gain__setting__param.md)struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) {

[ 1120](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673);

1121

[ 1123](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8) struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) \*[param](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8);

1124

[ 1126](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349) size\_t [count](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349);

1127};

1128

[ 1136](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b)int [bt\_cap\_commander\_change\_microphone\_gain\_setting](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b)(

1137 const struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) \*param);

1138#ifdef \_\_cplusplus

1139}

1140#endif

1141

1145

1146#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CAP\_H\_ \*/

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

[bt\_cap\_initiator\_broadcast\_get\_base](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)

int bt\_cap\_initiator\_broadcast\_get\_base(struct bt\_cap\_broadcast\_source \*broadcast\_source, struct net\_buf\_simple \*base\_buf)

Get the Broadcast Audio Stream Endpoint of a Common Audio Profile broadcast source.

[bt\_cap\_initiator\_broadcast\_audio\_create](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4)

int bt\_cap\_initiator\_broadcast\_audio\_create(const struct bt\_cap\_initiator\_broadcast\_create\_param \*param, struct bt\_cap\_broadcast\_source \*\*broadcast\_source)

Create a Common Audio Profile broadcast source.

[bt\_cap\_commander\_cancel](group__bt__cap.md#ga7abf029533fed391930257605f3c752c)

int bt\_cap\_commander\_cancel(void)

Cancel any current Common Audio Profile commander procedure.

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

**Definition** cap.h:149

[bt\_cap\_initiator\_unicast\_audio\_start](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184)

int bt\_cap\_initiator\_unicast\_audio\_start(const struct bt\_cap\_unicast\_audio\_start\_param \*param)

Setup and start unicast audio streams for a set of devices.

[bt\_cap\_commander\_change\_volume\_offset](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa)

int bt\_cap\_commander\_change\_volume\_offset(const struct bt\_cap\_commander\_change\_volume\_offset\_param \*param)

Change the volume offset on one or more Common Audio Profile Acceptors.

[bt\_cap\_initiator\_broadcast\_audio\_stop](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e)

int bt\_cap\_initiator\_broadcast\_audio\_stop(struct bt\_cap\_broadcast\_source \*broadcast\_source)

Stop broadcast audio streams for a Common Audio Profile broadcast source.

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

**Definition** cap.h:153

[BT\_CAP\_SET\_TYPE\_AD\_HOC](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468)

@ BT\_CAP\_SET\_TYPE\_AD\_HOC

The set is an ad-hoc set.

**Definition** cap.h:151

[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)

#define BT\_ISO\_BROADCAST\_CODE\_SIZE

Broadcast code size.

**Definition** iso.h:129

[iso.h](iso_8h.md)

Bluetooth ISO handling.

[net\_buf.h](net__buf_8h.md)

Buffer management.

[stdbool.h](stdbool_8h.md)

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

**Definition** bap.h:537

[bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md)

QoS configuration structure.

**Definition** bap.h:128

[bt\_bap\_stream\_ops](structbt__bap__stream__ops.md)

Stream operation.

**Definition** bap.h:781

[bt\_bap\_stream](structbt__bap__stream.md)

Basic Audio Profile stream structure.

**Definition** bap.h:740

[bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md)

Parameters for bt\_cap\_initiator\_broadcast\_to\_unicast().

**Definition** cap.h:672

[bt\_cap\_broadcast\_to\_unicast\_param::members](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed)

union bt\_cap\_set\_member \*\* members

Coordinated or ad-hoc set members.

**Definition** cap.h:693

[bt\_cap\_broadcast\_to\_unicast\_param::type](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:681

[bt\_cap\_broadcast\_to\_unicast\_param::count](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce)

size\_t count

The number of set members in members.

**Definition** cap.h:690

[bt\_cap\_broadcast\_to\_unicast\_param::broadcast\_source](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9)

struct bt\_cap\_broadcast\_source \* broadcast\_source

The source broadcast source with the streams.

**Definition** cap.h:678

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md)

Parameters part of bt\_cap\_commander\_broadcast\_reception\_start\_param for bt\_cap\_commander\_broadcast\_re...

**Definition** cap.h:896

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::num\_subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63)

size\_t num\_subgroups

Number of subgroups.

**Definition** cap.h:924

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::pa\_interval](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c)

uint16\_t pa\_interval

Periodic advertising interval in milliseconds.

**Definition** cap.h:911

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::broadcast\_id](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0)

uint32\_t broadcast\_id

24-bit broadcast ID

**Definition** cap.h:914

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::addr](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e)

bt\_addr\_le\_t addr

Address of the advertiser.

**Definition** cap.h:901

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::member](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:898

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::adv\_sid](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362)

uint8\_t adv\_sid

SID of the advertising set.

**Definition** cap.h:904

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#af1d74b691a3fe3d590b355d47112240b)

struct bt\_bap\_bass\_subgroup subgroups[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]

Pointer to array of subgroups.

**Definition** cap.h:921

[bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md)

Parameters for starting broadcast reception.

**Definition** cap.h:928

[bt\_cap\_commander\_broadcast\_reception\_start\_param::param](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041)

struct bt\_cap\_commander\_broadcast\_reception\_start\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:933

[bt\_cap\_commander\_broadcast\_reception\_start\_param::count](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7)

size\_t count

The number of parameters in param.

**Definition** cap.h:936

[bt\_cap\_commander\_broadcast\_reception\_start\_param::type](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:930

[bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md)

Parameters for stopping broadcast reception.

**Definition** cap.h:952

[bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::src\_id](structbt__cap__commander__broadcast__reception__stop__member__param.md#a72d606f6a83b1c84aa41d9db22cb955a)

uint8\_t src\_id

Source ID of the receive state.

**Definition** cap.h:957

[bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::member](structbt__cap__commander__broadcast__reception__stop__member__param.md#aa934af2e197c129b1fcb1eea9359ea6d)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:954

[bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param::num\_subgroups](structbt__cap__commander__broadcast__reception__stop__member__param.md#aeeab53e8bd7ae4f36433c0d4b60c313b)

size\_t num\_subgroups

Number of subgroups.

**Definition** cap.h:960

[bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md)

**Definition** cap.h:963

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::type](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:965

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::param](structbt__cap__commander__broadcast__reception__stop__param.md#a36ce7cd132cd41a55872985433c2934d)

struct bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:968

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::count](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593)

size\_t count

The number of parameters in param.

**Definition** cap.h:971

[bt\_cap\_commander\_cb](structbt__cap__commander__cb.md)

Callback structure for CAP procedures.

**Definition** cap.h:716

[bt\_cap\_commander\_cb::broadcast\_reception\_start](structbt__cap__commander__cb.md#a14f6a51db5a76aac015a5de617712af3)

void(\* broadcast\_reception\_start)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_broadcast\_reception\_start().

**Definition** cap.h:811

[bt\_cap\_commander\_cb::microphone\_gain\_changed](structbt__cap__commander__cb.md#a1e83872924e1aa1293c499184ade9173)

void(\* microphone\_gain\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_microphone\_gain\_setting().

**Definition** cap.h:796

[bt\_cap\_commander\_cb::broadcast\_reception\_stop](structbt__cap__commander__cb.md#a2188c52e3daf0a695d7c42e6cac561cf)

void(\* broadcast\_reception\_stop)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_broadcast\_reception\_stop().

**Definition** cap.h:822

[bt\_cap\_commander\_cb::volume\_changed](structbt__cap__commander__cb.md#a3a7777603c23c14bc9d01cf29bc70ef7)

void(\* volume\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_volume().

**Definition** cap.h:745

[bt\_cap\_commander\_cb::volume\_offset\_changed](structbt__cap__commander__cb.md#a3bacfffef8d122db4574463777dfd507)

void(\* volume\_offset\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_volume\_offset().

**Definition** cap.h:770

[bt\_cap\_commander\_cb::microphone\_mute\_changed](structbt__cap__commander__cb.md#aa49e7eaf5c45d70c800f28b81f9967e5)

void(\* microphone\_mute\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_microphone\_mute\_state().

**Definition** cap.h:784

[bt\_cap\_commander\_cb::volume\_mute\_changed](structbt__cap__commander__cb.md#acc9fcedf7f7abe86e055d48e6df124c7)

void(\* volume\_mute\_changed)(struct bt\_conn \*conn, int err)

Callback for bt\_cap\_commander\_change\_volume\_mute\_state().

**Definition** cap.h:757

[bt\_cap\_commander\_cb::discovery\_complete](structbt__cap__commander__cb.md#af989b3ebe7e5cc83a1ca4b2ef080e14d)

void(\* discovery\_complete)(struct bt\_conn \*conn, int err, const struct bt\_csip\_set\_coordinator\_set\_member \*member, const struct bt\_csip\_set\_coordinator\_csis\_inst \*csis\_inst)

Callback for bt\_cap\_initiator\_unicast\_discover().

**Definition** cap.h:730

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md)

Parameters part of bt\_cap\_commander\_change\_microphone\_gain\_setting\_param for bt\_cap\_commander\_change\_...

**Definition** cap.h:1109

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param::member](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:1111

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param::gain](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196)

int8\_t gain

The microphone gain setting to set.

**Definition** cap.h:1114

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md)

Parameters for changing microphone mute state.

**Definition** cap.h:1118

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::type](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1120

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::param](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8)

struct bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:1123

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::count](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349)

size\_t count

The number of parameters in param.

**Definition** cap.h:1126

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md)

Parameters for changing microphone mute state.

**Definition** cap.h:1077

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::mute](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8)

bool mute

The microphone mute state to set.

**Definition** cap.h:1092

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::count](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e)

size\_t count

The number of members in members.

**Definition** cap.h:1085

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::members](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:1082

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::type](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1079

[bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md)

Parameters for changing volume mute state.

**Definition** cap.h:1048

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::count](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8)

size\_t count

The number of members in members.

**Definition** cap.h:1056

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::mute](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd)

bool mute

The volume mute state to set.

**Definition** cap.h:1063

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::type](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1050

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::members](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:1053

[bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md)

Parameters part of bt\_cap\_commander\_change\_volume\_offset\_param for bt\_cap\_commander\_change\_volume\_off...

**Definition** cap.h:1013

[bt\_cap\_commander\_change\_volume\_offset\_member\_param::offset](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8)

int16\_t offset

The offset to set.

**Definition** cap.h:1022

[bt\_cap\_commander\_change\_volume\_offset\_member\_param::member](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:1015

[bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md)

Parameters for changing volume offset.

**Definition** cap.h:1026

[bt\_cap\_commander\_change\_volume\_offset\_param::param](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d)

struct bt\_cap\_commander\_change\_volume\_offset\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:1031

[bt\_cap\_commander\_change\_volume\_offset\_param::type](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:1028

[bt\_cap\_commander\_change\_volume\_offset\_param::count](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b)

size\_t count

The number of parameters in param.

**Definition** cap.h:1034

[bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md)

Parameters for changing absolute volume.

**Definition** cap.h:986

[bt\_cap\_commander\_change\_volume\_param::count](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640)

size\_t count

The number of members in members.

**Definition** cap.h:994

[bt\_cap\_commander\_change\_volume\_param::members](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:991

[bt\_cap\_commander\_change\_volume\_param::type](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:988

[bt\_cap\_commander\_change\_volume\_param::volume](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49)

uint8\_t volume

The absolute volume to set.

**Definition** cap.h:997

[bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md)

Parameters for \* bt\_cap\_initiator\_broadcast\_audio\_create().

**Definition** cap.h:451

[bt\_cap\_initiator\_broadcast\_create\_param::pto](structbt__cap__initiator__broadcast__create__param.md#a01d6ffb369caaf808d4b55b3b1748890)

uint8\_t pto

Pre-transmission offset.

**Definition** cap.h:504

[bt\_cap\_initiator\_broadcast\_create\_param::qos](structbt__cap__initiator__broadcast__create__param.md#a142125e620776aed464d90f280ef1a4c)

struct bt\_bap\_qos\_cfg \* qos

Quality of Service configuration.

**Definition** cap.h:459

[bt\_cap\_initiator\_broadcast\_create\_param::subgroup\_params](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839)

struct bt\_cap\_initiator\_broadcast\_subgroup\_param \* subgroup\_params

Array of stream parameters.

**Definition** cap.h:456

[bt\_cap\_initiator\_broadcast\_create\_param::encryption](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542)

bool encryption

Whether or not to encrypt the streams.

**Definition** cap.h:471

[bt\_cap\_initiator\_broadcast\_create\_param::irc](structbt__cap__initiator__broadcast__create__param.md#a6f562b7a696472b7784ca2e1ced4997a)

uint8\_t irc

Immediate Repetition Count.

**Definition** cap.h:495

[bt\_cap\_initiator\_broadcast\_create\_param::iso\_interval](structbt__cap__initiator__broadcast__create__param.md#a8eedd8f9a896931f75642576ca37c7d5)

uint16\_t iso\_interval

ISO interval.

**Definition** cap.h:513

[bt\_cap\_initiator\_broadcast\_create\_param::broadcast\_code](structbt__cap__initiator__broadcast__create__param.md#aa4d6fbd5bd13963004e381b987bbeb4d)

uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]

16-octet broadcast code.

**Definition** cap.h:485

[bt\_cap\_initiator\_broadcast\_create\_param::packing](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc)

uint8\_t packing

Broadcast Source packing mode.

**Definition** cap.h:468

[bt\_cap\_initiator\_broadcast\_create\_param::subgroup\_count](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b)

size\_t subgroup\_count

The number of parameters in subgroup\_params.

**Definition** cap.h:453

[bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md)

Parameters part of bt\_cap\_initiator\_broadcast\_subgroup\_param for bt\_cap\_initiator\_broadcast\_audio\_cre...

**Definition** cap.h:421

[bt\_cap\_initiator\_broadcast\_stream\_param::data](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869)

uint8\_t \* data

BIS Codec Specific Configuration.

**Definition** cap.h:432

[bt\_cap\_initiator\_broadcast\_stream\_param::stream](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a)

struct bt\_cap\_stream \* stream

Audio stream.

**Definition** cap.h:423

[bt\_cap\_initiator\_broadcast\_stream\_param::data\_len](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4)

size\_t data\_len

The length of the p data array.

**Definition** cap.h:429

[bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md)

Parameters part of bt\_cap\_initiator\_broadcast\_create\_param for bt\_cap\_initiator\_broadcast\_audio\_creat...

**Definition** cap.h:439

[bt\_cap\_initiator\_broadcast\_subgroup\_param::stream\_params](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a)

struct bt\_cap\_initiator\_broadcast\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:444

[bt\_cap\_initiator\_broadcast\_subgroup\_param::stream\_count](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769)

size\_t stream\_count

The number of parameters in stream\_params.

**Definition** cap.h:441

[bt\_cap\_initiator\_broadcast\_subgroup\_param::codec\_cfg](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Subgroup Codec configuration.

**Definition** cap.h:447

[bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md)

Callback structure for CAP procedures.

**Definition** cap.h:75

[bt\_cap\_initiator\_cb::unicast\_stop\_complete](structbt__cap__initiator__cb.md#a2e910a82209d144878b6c69c1b2723ba)

void(\* unicast\_stop\_complete)(int err, struct bt\_conn \*conn)

Callback for bt\_cap\_initiator\_unicast\_audio\_stop().

**Definition** cap.h:129

[bt\_cap\_initiator\_cb::unicast\_discovery\_complete](structbt__cap__initiator__cb.md#a642a2f48e8f870bb1681ba58aa119de9)

void(\* unicast\_discovery\_complete)(struct bt\_conn \*conn, int err, const struct bt\_csip\_set\_coordinator\_set\_member \*member, const struct bt\_csip\_set\_coordinator\_csis\_inst \*csis\_inst)

Callback for bt\_cap\_initiator\_unicast\_discover().

**Definition** cap.h:90

[bt\_cap\_initiator\_cb::unicast\_update\_complete](structbt__cap__initiator__cb.md#a95266741841fca83cd2769c76652154e)

void(\* unicast\_update\_complete)(int err, struct bt\_conn \*conn)

Callback for bt\_cap\_initiator\_unicast\_audio\_update().

**Definition** cap.h:117

[bt\_cap\_initiator\_cb::unicast\_start\_complete](structbt__cap__initiator__cb.md#aa70de1dda73ffdcbb8287f8f174984ea)

void(\* unicast\_start\_complete)(int err, struct bt\_conn \*conn)

Callback for bt\_cap\_initiator\_unicast\_audio\_start().

**Definition** cap.h:105

[bt\_cap\_stream](structbt__cap__stream.md)

Common Audio Profile stream structure.

**Definition** cap.h:171

[bt\_cap\_stream::ops](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba)

struct bt\_bap\_stream\_ops \* ops

Audio stream operations.

**Definition** cap.h:176

[bt\_cap\_stream::bap\_stream](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18)

struct bt\_bap\_stream bap\_stream

The underlying BAP audio stream.

**Definition** cap.h:173

[bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_start() function.

**Definition** cap.h:266

[bt\_cap\_unicast\_audio\_start\_param::type](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:268

[bt\_cap\_unicast\_audio\_start\_param::count](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667)

size\_t count

The number of parameters in stream\_params.

**Definition** cap.h:271

[bt\_cap\_unicast\_audio\_start\_param::stream\_params](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b)

struct bt\_cap\_unicast\_audio\_start\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:274

[bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md)

Stream specific parameters for the bt\_cap\_initiator\_unicast\_audio\_start() function.

**Definition** cap.h:242

[bt\_cap\_unicast\_audio\_start\_stream\_param::stream](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e)

struct bt\_cap\_stream \* stream

Stream for the member.

**Definition** cap.h:247

[bt\_cap\_unicast\_audio\_start\_stream\_param::codec\_cfg](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Codec configuration.

**Definition** cap.h:262

[bt\_cap\_unicast\_audio\_start\_stream\_param::member](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:244

[bt\_cap\_unicast\_audio\_start\_stream\_param::ep](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb)

struct bt\_bap\_ep \* ep

Endpoint reference for the stream.

**Definition** cap.h:250

[bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_stop() function.

**Definition** cap.h:306

[bt\_cap\_unicast\_audio\_stop\_param::count](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2)

size\_t count

The number of streams in streams.

**Definition** cap.h:311

[bt\_cap\_unicast\_audio\_stop\_param::release](structbt__cap__unicast__audio__stop__param.md#a1cbd7ee2e4ceafd2da2858dc7c941d78)

bool release

Whether to release the streams after they have stopped.

**Definition** cap.h:317

[bt\_cap\_unicast\_audio\_stop\_param::type](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:308

[bt\_cap\_unicast\_audio\_stop\_param::streams](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82)

struct bt\_cap\_stream \*\* streams

Array of streams to stop.

**Definition** cap.h:314

[bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_update() function.

**Definition** cap.h:294

[bt\_cap\_unicast\_audio\_update\_param::stream\_params](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb)

struct bt\_cap\_unicast\_audio\_update\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:302

[bt\_cap\_unicast\_audio\_update\_param::type](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:296

[bt\_cap\_unicast\_audio\_update\_param::count](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1)

size\_t count

The number of parameters in stream\_params.

**Definition** cap.h:299

[bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md)

Stream specific parameters for the bt\_cap\_initiator\_unicast\_audio\_update() function.

**Definition** cap.h:278

[bt\_cap\_unicast\_audio\_update\_stream\_param::meta\_len](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c)

size\_t meta\_len

The length of meta.

**Definition** cap.h:283

[bt\_cap\_unicast\_audio\_update\_stream\_param::stream](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1)

struct bt\_cap\_stream \* stream

Stream to update.

**Definition** cap.h:280

[bt\_cap\_unicast\_audio\_update\_stream\_param::meta](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0)

uint8\_t \* meta

The new metadata.

**Definition** cap.h:290

[bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md)

Parameters for bt\_cap\_initiator\_unicast\_to\_broadcast().

**Definition** cap.h:625

[bt\_cap\_unicast\_to\_broadcast\_param::unicast\_group](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239)

struct bt\_bap\_unicast\_group \* unicast\_group

The source unicast group with the streams.

**Definition** cap.h:627

[bt\_cap\_unicast\_to\_broadcast\_param::broadcast\_code](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3)

uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]

16-octet broadcast code.

**Definition** cap.h:649

[bt\_cap\_unicast\_to\_broadcast\_param::encrypt](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262)

bool encrypt

Whether or not to encrypt the streams.

**Definition** cap.h:635

[bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md)

Struct representing a coordinated set instance on a remote device.

**Definition** csip.h:301

[bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md)

Struct representing a remote device as a set member.

**Definition** csip.h:310

[bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md)

Register structure for Coordinated Set Identification Service.

**Definition** csip.h:133

[bt\_iso\_tx\_info](structbt__iso__tx__info.md)

ISO Meta Data structure for transmitted ISO packets.

**Definition** iso.h:346

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[bt\_cap\_set\_member](unionbt__cap__set__member.md)

Represents a Common Audio Set member that are either in a Coordinated or ad-hoc set.

**Definition** cap.h:157

[bt\_cap\_set\_member::member](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973)

struct bt\_conn \* member

Connection pointer if the type is BT\_CAP\_SET\_TYPE\_AD\_HOC.

**Definition** cap.h:159

[bt\_cap\_set\_member::csip](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6)

struct bt\_csip\_set\_coordinator\_csis\_inst \* csip

CSIP Coordinated Set struct used if type is BT\_CAP\_SET\_TYPE\_CSIP.

**Definition** cap.h:162

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [cap.h](bluetooth_2audio_2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
