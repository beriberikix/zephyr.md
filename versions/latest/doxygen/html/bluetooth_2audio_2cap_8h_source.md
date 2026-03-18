---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bluetooth_2audio_2cap_8h_source.html
original_path: doxygen/html/bluetooth_2audio_2cap_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cap.h

[Go to the documentation of this file.](bluetooth_2audio_2cap_8h.md)

1/\*

2 \* Copyright (c) 2022-2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CAP\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CAP\_H\_

9

21

22#include <[stdint.h](stdint_8h.md)>

23

24#include <[zephyr/bluetooth/audio/csip.h](csip_8h.md)>

25#include <[zephyr/bluetooth/iso.h](iso_8h.md)>

26#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

27#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

34struct bt\_cap\_broadcast\_source;

35

[ 54](group__bt__cap.md#gafcb9ea2122ff8058321cf85a22326abe)int [bt\_cap\_acceptor\_register](group__bt__cap.md#gafcb9ea2122ff8058321cf85a22326abe)(const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param,

55 struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst);

56

[ 58](structbt__cap__initiator__cb.md)struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) {

59#if defined(CONFIG\_BT\_BAP\_UNICAST\_CLIENT)

72 void (\*unicast\_discovery\_complete)(

73 struct bt\_conn \*conn, int err,

74 const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst);

75

86 void (\*unicast\_start\_complete)(int err, struct bt\_conn \*conn);

87

98 void (\*unicast\_update\_complete)(int err, struct bt\_conn \*conn);

99

110 void (\*unicast\_stop\_complete)(int err, struct bt\_conn \*conn);

111#endif /\* CONFIG\_BT\_BAP\_UNICAST\_CLIENT \*/

112};

113

[ 127](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d)int [bt\_cap\_initiator\_unicast\_discover](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d)(struct bt\_conn \*conn);

128

[ 130](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a)enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) {

[ 132](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468) [BT\_CAP\_SET\_TYPE\_AD\_HOC](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468),

[ 134](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4) [BT\_CAP\_SET\_TYPE\_CSIP](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4),

135};

136

[ 138](unionbt__cap__set__member.md)union [bt\_cap\_set\_member](unionbt__cap__set__member.md) {

[ 140](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973) struct bt\_conn \*[member](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973);

141

[ 143](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6) struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*[csip](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6);

144};

145

[ 146](structbt__cap__stream.md)struct [bt\_cap\_stream](structbt__cap__stream.md) {

[ 147](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18) struct [bt\_bap\_stream](structbt__bap__stream.md) [bap\_stream](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18);

[ 148](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba) struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*[ops](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba);

149};

150

[ 158](group__bt__cap.md#gac909b00d53cf35103382f0e1d9f426b7)void [bt\_cap\_stream\_ops\_register](group__bt__cap.md#gac909b00d53cf35103382f0e1d9f426b7)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*ops);

159

[ 175](group__bt__cap.md#ga2d8b15543105078b793462b762e27741)int [bt\_cap\_stream\_send](group__bt__cap.md#ga2d8b15543105078b793462b762e27741)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num);

176

[ 194](group__bt__cap.md#ga23618d1ab7690c4d3a567228c857c89e)int [bt\_cap\_stream\_send\_ts](group__bt__cap.md#ga23618d1ab7690c4d3a567228c857c89e)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num,

195 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

196

[ 210](group__bt__cap.md#ga7f3f6e98e7720a4711b658c4b7c85235)int [bt\_cap\_stream\_get\_tx\_sync](group__bt__cap.md#ga7f3f6e98e7720a4711b658c4b7c85235)(struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info);

211

[ 213](structbt__cap__unicast__audio__start__stream__param.md)struct [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md) {

[ 215](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b);

216

[ 218](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e);

219

[ 221](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb) struct bt\_bap\_ep \*[ep](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb);

222

[ 230](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a);

231};

232

[ 234](structbt__cap__unicast__audio__start__param.md)struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) {

[ 236](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5);

237

[ 239](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667) size\_t [count](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667);

240

[ 242](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b) struct [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md) \*[stream\_params](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b);

243};

244

[ 246](structbt__cap__unicast__audio__update__stream__param.md)struct [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) {

[ 248](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1);

249

[ 251](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c) size\_t [meta\_len](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c);

252

[ 258](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[meta](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0);

259};

260

[ 262](structbt__cap__unicast__audio__update__param.md)struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) {

[ 264](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd);

265

[ 267](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1) size\_t [count](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1);

268

[ 270](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb) struct [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) \*[stream\_params](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb);

271};

272

[ 274](structbt__cap__unicast__audio__stop__param.md)struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) {

[ 276](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa);

277

[ 279](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2) size\_t [count](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2);

280

[ 282](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82) struct [bt\_cap\_stream](structbt__cap__stream.md) \*\*[streams](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82);

283};

284

[ 292](group__bt__cap.md#ga54d7ad68f376998510aad9c3702e9364)int [bt\_cap\_initiator\_register\_cb](group__bt__cap.md#ga54d7ad68f376998510aad9c3702e9364)(const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb);

293

[ 309](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184)int [bt\_cap\_initiator\_unicast\_audio\_start](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184)(const struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) \*param);

310

[ 324](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639)int [bt\_cap\_initiator\_unicast\_audio\_update](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639)(const struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) \*param);

325

[ 339](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f)int [bt\_cap\_initiator\_unicast\_audio\_stop](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f)(const struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) \*param);

340

[ 363](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f)int [bt\_cap\_initiator\_unicast\_audio\_cancel](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f)(void);

364

[ 365](structbt__cap__initiator__broadcast__stream__param.md)struct [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) {

[ 367](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a) struct [bt\_cap\_stream](structbt__cap__stream.md) \*[stream](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a);

368

[ 373](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4) size\_t [data\_len](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4);

374

[ 376](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869);

377};

378

[ 379](structbt__cap__initiator__broadcast__subgroup__param.md)struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) {

[ 381](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769) size\_t [stream\_count](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769);

382

[ 384](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a) struct [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) \*[stream\_params](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a);

385

[ 387](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*[codec\_cfg](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47);

388};

389

[ 390](structbt__cap__initiator__broadcast__create__param.md)struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) {

[ 392](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b) size\_t [subgroup\_count](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b);

393

[ 395](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839) struct [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) \*[subgroup\_params](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839);

396

[ 398](structbt__cap__initiator__broadcast__create__param.md#af7533744fc262dac4d71bc98d33bbee2) struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \*[qos](structbt__cap__initiator__broadcast__create__param.md#af7533744fc262dac4d71bc98d33bbee2);

399

[ 407](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc);

408

[ 410](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542) bool [encryption](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542);

411

[ 424](structbt__cap__initiator__broadcast__create__param.md#a9053fbfd5b847db896b3d832338f6b92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__cap__initiator__broadcast__create__param.md#a9053fbfd5b847db896b3d832338f6b92)[[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)];

425

426#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS)

434 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irc;

435

442 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pto;

443

451 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) iso\_interval;

452#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

453};

454

[ 469](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4)int [bt\_cap\_initiator\_broadcast\_audio\_create](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4)(

470 const struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) \*param,

471 struct bt\_cap\_broadcast\_source \*\*broadcast\_source);

472

[ 492](group__bt__cap.md#ga2bd5f9c9de719a14ffc69827dbd4fa24)int [bt\_cap\_initiator\_broadcast\_audio\_start](group__bt__cap.md#ga2bd5f9c9de719a14ffc69827dbd4fa24)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

493 struct bt\_le\_ext\_adv \*adv);

[ 508](group__bt__cap.md#ga92336c4a56c667b608a86e45eb8d5073)int [bt\_cap\_initiator\_broadcast\_audio\_update](group__bt__cap.md#ga92336c4a56c667b608a86e45eb8d5073)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

509 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len);

510

[ 523](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e)int [bt\_cap\_initiator\_broadcast\_audio\_stop](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e)(struct bt\_cap\_broadcast\_source \*broadcast\_source);

524

[ 542](group__bt__cap.md#gac98ed5112d0ce0659bde86d149ea7b4c)int [bt\_cap\_initiator\_broadcast\_audio\_delete](group__bt__cap.md#gac98ed5112d0ce0659bde86d149ea7b4c)(struct bt\_cap\_broadcast\_source \*broadcast\_source);

543

[ 558](group__bt__cap.md#gafe675bb1b912915249dcd37da4967a63)int [bt\_cap\_initiator\_broadcast\_get\_id](group__bt__cap.md#gafe675bb1b912915249dcd37da4967a63)(const struct bt\_cap\_broadcast\_source \*broadcast\_source,

559 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const broadcast\_id);

560

[ 576](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)int [bt\_cap\_initiator\_broadcast\_get\_base](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)(struct bt\_cap\_broadcast\_source \*broadcast\_source,

577 struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf);

578

[ 579](structbt__cap__unicast__to__broadcast__param.md)struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) {

[ 581](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239) struct bt\_bap\_unicast\_group \*[unicast\_group](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239);

582

[ 589](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262) bool [encrypt](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262);

590

[ 603](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [broadcast\_code](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

604};

605

[ 622](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558)int [bt\_cap\_initiator\_unicast\_to\_broadcast](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558)(const struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) \*param,

623 struct bt\_cap\_broadcast\_source \*\*source);

624

[ 625](structbt__cap__broadcast__to__unicast__param.md)struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) {

[ 631](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9) struct bt\_cap\_broadcast\_source \*[broadcast\_source](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9);

632

[ 634](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf);

635

[ 643](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce) size\_t [count](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce);

644

[ 646](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*\*[members](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed);

647};

648

[ 665](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b)int [bt\_cap\_initiator\_broadcast\_to\_unicast](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b)(const struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) \*param,

666 struct bt\_bap\_unicast\_group \*\*unicast\_group);

667

[ 669](structbt__cap__commander__cb.md)struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) {

[ 682](structbt__cap__commander__cb.md#af891c2a8a9a39bd081cd9d4f5eb3a468) void (\*[discovery\_complete](structbt__cap__commander__cb.md#af891c2a8a9a39bd081cd9d4f5eb3a468))(struct bt\_conn \*conn, int err,

683 const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst);

684

685#if defined(CONFIG\_BT\_VCP\_VOL\_CTLR)

696 void (\*volume\_changed)(struct bt\_conn \*conn, int err);

697

698#if defined(CONFIG\_BT\_VCP\_VOL\_CTLR\_VOCS)

709 void (\*volume\_offset\_changed)(struct bt\_conn \*conn, int err);

710#endif /\* CONFIG\_BT\_VCP\_VOL\_CTLR\_VOCS \*/

711#endif /\* CONFIG\_BT\_VCP\_VOL\_CTLR \*/

712};

713

[ 723](group__bt__cap.md#gab6239c91b9d210872396860619fb8687)int [bt\_cap\_commander\_register\_cb](group__bt__cap.md#gab6239c91b9d210872396860619fb8687)(const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb);

724

[ 733](group__bt__cap.md#ga38928945e67835983de3fc639c8f2764)int [bt\_cap\_commander\_unregister\_cb](group__bt__cap.md#ga38928945e67835983de3fc639c8f2764)(const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb);

734

[ 753](group__bt__cap.md#ga165c67bddcbe220050293a4c73fb6ede)int [bt\_cap\_commander\_discover](group__bt__cap.md#ga165c67bddcbe220050293a4c73fb6ede)(struct bt\_conn \*conn);

754

[ 777](group__bt__cap.md#ga7abf029533fed391930257605f3c752c)int [bt\_cap\_commander\_cancel](group__bt__cap.md#ga7abf029533fed391930257605f3c752c)(void);

778

[ 779](structbt__cap__commander__broadcast__reception__start__member__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) {

[ 781](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7);

782

[ 784](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e);

785

[ 787](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_sid](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362);

788

[ 794](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pa\_interval](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c);

795

[ 797](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [broadcast\_id](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0);

798

[ 804](structbt__cap__commander__broadcast__reception__start__member__param.md#aee95783800cd7e36daa6aafe4b23f26b) struct [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) \*[subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#aee95783800cd7e36daa6aafe4b23f26b);

805

[ 807](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63) size\_t [num\_subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63);

808};

809

[ 811](structbt__cap__commander__broadcast__reception__start__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) {

[ 813](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1);

814

[ 816](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041) struct [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) \*[param](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041);

817

[ 819](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7) size\_t [count](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7);

820};

821

[ 830](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9)int [bt\_cap\_commander\_broadcast\_reception\_start](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9)(

831 const struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) \*param);

832

[ 834](structbt__cap__commander__broadcast__reception__stop__param.md)struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) {

[ 836](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460);

837

[ 839](structbt__cap__commander__broadcast__reception__stop__param.md#a34baa58b3c5b14b23f85950778708d88) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__broadcast__reception__stop__param.md#a34baa58b3c5b14b23f85950778708d88);

840

[ 842](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593) size\_t [count](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593);

843};

844

[ 853](group__bt__cap.md#gac5b2b6d617a092fb98b23c41b2f52d15)int [bt\_cap\_commander\_broadcast\_reception\_stop](group__bt__cap.md#gac5b2b6d617a092fb98b23c41b2f52d15)(

854 const struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) \*param);

855

[ 857](structbt__cap__commander__change__volume__param.md)struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) {

[ 859](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88);

860

[ 862](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531);

863

[ 865](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640) size\_t [count](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640);

866

[ 868](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [volume](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49);

869};

870

[ 878](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6)int [bt\_cap\_commander\_change\_volume](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6)(const struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) \*param);

879

[ 880](structbt__cap__commander__change__volume__offset__member__param.md)struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) {

[ 882](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4);

883

[ 889](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [offset](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8);

890};

891

[ 893](structbt__cap__commander__change__volume__offset__param.md)struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) {

[ 895](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd);

896

[ 898](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d) struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) \*[param](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d);

899

[ 901](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b) size\_t [count](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b);

902};

903

[ 911](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa)int [bt\_cap\_commander\_change\_volume\_offset](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa)(

912 const struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) \*param);

913

[ 915](structbt__cap__commander__change__volume__mute__state__param.md)struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) {

[ 917](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775);

918

[ 920](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1);

921

[ 923](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8) size\_t [count](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8);

924

[ 930](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd) bool [mute](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd);

931};

932

[ 940](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4)int [bt\_cap\_commander\_change\_volume\_mute\_state](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4)(

941 const struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) \*param);

942

[ 944](structbt__cap__commander__change__microphone__mute__state__param.md)struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) {

[ 946](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0);

947

[ 949](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \*[members](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1);

950

[ 952](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e) size\_t [count](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e);

953

[ 959](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8) bool [mute](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8);

960};

961

[ 969](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54)int [bt\_cap\_commander\_change\_microphone\_mute\_state](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54)(

970 const struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) \*param);

971

[ 972](structbt__cap__commander__change__microphone__gain__setting__member__param.md)struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) {

[ 974](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e) union [bt\_cap\_set\_member](unionbt__cap__set__member.md) [member](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e);

975

[ 977](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [gain](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196);

978};

979

[ 981](structbt__cap__commander__change__microphone__gain__setting__param.md)struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) {

[ 983](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673) enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) [type](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673);

984

[ 986](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8) struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) \*[param](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8);

987

[ 989](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349) size\_t [count](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349);

990};

991

[ 999](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b)int [bt\_cap\_commander\_change\_microphone\_gain\_setting](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b)(

1000 const struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) \*param);

1001#ifdef \_\_cplusplus

1002}

1003#endif

1004

1008

1009#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CAP\_H\_ \*/

[bap.h](bap_8h.md)

Header for Bluetooth BAP.

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[csip.h](csip_8h.md)

[BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)

#define BT\_AUDIO\_BROADCAST\_CODE\_SIZE

**Definition** audio.h:42

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

**Definition** cap.h:130

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

[bt\_cap\_initiator\_broadcast\_get\_id](group__bt__cap.md#gafe675bb1b912915249dcd37da4967a63)

int bt\_cap\_initiator\_broadcast\_get\_id(const struct bt\_cap\_broadcast\_source \*broadcast\_source, uint32\_t \*const broadcast\_id)

Get the broadcast ID of a Common Audio Profile broadcast source.

[bt\_cap\_commander\_change\_volume](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6)

int bt\_cap\_commander\_change\_volume(const struct bt\_cap\_commander\_change\_volume\_param \*param)

Change the volume on one or more Common Audio Profile Acceptors.

[BT\_CAP\_SET\_TYPE\_CSIP](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4)

@ BT\_CAP\_SET\_TYPE\_CSIP

The set is a CSIP Coordinated Set.

**Definition** cap.h:134

[BT\_CAP\_SET\_TYPE\_AD\_HOC](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468)

@ BT\_CAP\_SET\_TYPE\_AD\_HOC

The set is an ad-hoc set.

**Definition** cap.h:132

[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)

#define BT\_ISO\_BROADCAST\_CODE\_SIZE

Broadcast code size.

**Definition** iso.h:107

[iso.h](iso_8h.md)

Bluetooth ISO handling.

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

**Definition** audio.h:584

[bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)

Codec QoS structure.

**Definition** audio.h:702

[bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md)

Struct to hold subgroup specific information for the receive state.

**Definition** bap.h:249

[bt\_bap\_stream\_ops](structbt__bap__stream__ops.md)

Stream operation.

**Definition** bap.h:467

[bt\_bap\_stream](structbt__bap__stream.md)

Basic Audio Profile stream structure.

**Definition** bap.h:427

[bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md)

**Definition** cap.h:625

[bt\_cap\_broadcast\_to\_unicast\_param::members](structbt__cap__broadcast__to__unicast__param.md#a0914773df714195549d48d96672e63ed)

union bt\_cap\_set\_member \*\* members

Coordinated or ad-hoc set members.

**Definition** cap.h:646

[bt\_cap\_broadcast\_to\_unicast\_param::type](structbt__cap__broadcast__to__unicast__param.md#a7686cb6ef199865d94616b6aae670cdf)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:634

[bt\_cap\_broadcast\_to\_unicast\_param::count](structbt__cap__broadcast__to__unicast__param.md#aaa5aa4c7540f75f391cf212308a7a9ce)

size\_t count

The number of set members in members.

**Definition** cap.h:643

[bt\_cap\_broadcast\_to\_unicast\_param::broadcast\_source](structbt__cap__broadcast__to__unicast__param.md#aeb6b9c09c50b5b1f7556b1ca0f2b49c9)

struct bt\_cap\_broadcast\_source \* broadcast\_source

The source broadcast source with the streams.

**Definition** cap.h:631

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md)

**Definition** cap.h:779

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::num\_subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#a184f2623ab759832a3ec9770b14c9c63)

size\_t num\_subgroups

Number of subgroups.

**Definition** cap.h:807

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::pa\_interval](structbt__cap__commander__broadcast__reception__start__member__param.md#a1ba6b20f822f38dd4a0ce1f8b2f2671c)

uint16\_t pa\_interval

Periodic advertising interval in milliseconds.

**Definition** cap.h:794

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::broadcast\_id](structbt__cap__commander__broadcast__reception__start__member__param.md#a8e6d5d1004d13069739229a7eec3abc0)

uint32\_t broadcast\_id

24-bit broadcast ID

**Definition** cap.h:797

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::addr](structbt__cap__commander__broadcast__reception__start__member__param.md#a93d6b4c76e730f282d24b2086c10aa3e)

bt\_addr\_le\_t addr

Address of the advertiser.

**Definition** cap.h:784

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::member](structbt__cap__commander__broadcast__reception__start__member__param.md#abf47aafab0b076da675182308d89bff7)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:781

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::adv\_sid](structbt__cap__commander__broadcast__reception__start__member__param.md#acc52738756124db042ea884c82163362)

uint8\_t adv\_sid

SID of the advertising set.

**Definition** cap.h:787

[bt\_cap\_commander\_broadcast\_reception\_start\_member\_param::subgroups](structbt__cap__commander__broadcast__reception__start__member__param.md#aee95783800cd7e36daa6aafe4b23f26b)

struct bt\_bap\_bass\_subgroup \* subgroups

Pointer to array of subgroups.

**Definition** cap.h:804

[bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md)

Parameters for starting broadcast reception.

**Definition** cap.h:811

[bt\_cap\_commander\_broadcast\_reception\_start\_param::param](structbt__cap__commander__broadcast__reception__start__param.md#a8bac9170f48f34fd2239da9a6d994041)

struct bt\_cap\_commander\_broadcast\_reception\_start\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:816

[bt\_cap\_commander\_broadcast\_reception\_start\_param::count](structbt__cap__commander__broadcast__reception__start__param.md#ab0fe6fe27946a349ac33f11526ca13b7)

size\_t count

The number of parameters in param.

**Definition** cap.h:819

[bt\_cap\_commander\_broadcast\_reception\_start\_param::type](structbt__cap__commander__broadcast__reception__start__param.md#ae4c1e6d7b345b8764f695ada56483aa1)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:813

[bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md)

Parameters for stopping broadcast reception.

**Definition** cap.h:834

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::members](structbt__cap__commander__broadcast__reception__stop__param.md#a34baa58b3c5b14b23f85950778708d88)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:839

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::type](structbt__cap__commander__broadcast__reception__stop__param.md#a35bc972b00c10b90544da19c659fc460)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:836

[bt\_cap\_commander\_broadcast\_reception\_stop\_param::count](structbt__cap__commander__broadcast__reception__stop__param.md#add81cdf1e3bad07b43602c8ce7c47593)

size\_t count

The number of members in members.

**Definition** cap.h:842

[bt\_cap\_commander\_cb](structbt__cap__commander__cb.md)

Callback structure for CAP procedures.

**Definition** cap.h:669

[bt\_cap\_commander\_cb::discovery\_complete](structbt__cap__commander__cb.md#af891c2a8a9a39bd081cd9d4f5eb3a468)

void(\* discovery\_complete)(struct bt\_conn \*conn, int err, const struct bt\_csip\_set\_coordinator\_csis\_inst \*csis\_inst)

Callback for bt\_cap\_initiator\_unicast\_discover().

**Definition** cap.h:682

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md)

**Definition** cap.h:972

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param::member](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a5cc34236153e6a737f71cbc77f5f840e)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:974

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param::gain](structbt__cap__commander__change__microphone__gain__setting__member__param.md#a8fdcc5ec143b5a73c369d6e15d276196)

int8\_t gain

The microphone gain setting to set.

**Definition** cap.h:977

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md)

Parameters for changing microphone mute state.

**Definition** cap.h:981

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::type](structbt__cap__commander__change__microphone__gain__setting__param.md#abac0f4da7b8b05067636539b2e9f9673)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:983

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::param](structbt__cap__commander__change__microphone__gain__setting__param.md#ade5a93aee8bcff628228664c4a8428a8)

struct bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:986

[bt\_cap\_commander\_change\_microphone\_gain\_setting\_param::count](structbt__cap__commander__change__microphone__gain__setting__param.md#ae78e5d4761df00c8c8e2cfcb3e727349)

size\_t count

The number of parameters in param.

**Definition** cap.h:989

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md)

Parameters for changing microphone mute state.

**Definition** cap.h:944

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::mute](structbt__cap__commander__change__microphone__mute__state__param.md#a1b6e22c9c41eb24b3961927b45c98af8)

bool mute

The microphone mute state to set.

**Definition** cap.h:959

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::count](structbt__cap__commander__change__microphone__mute__state__param.md#a96007101444d3cd61dda067fa072580e)

size\_t count

The number of members in members.

**Definition** cap.h:952

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::members](structbt__cap__commander__change__microphone__mute__state__param.md#a9c989fe2446ee2e055778c063a6b6de1)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:949

[bt\_cap\_commander\_change\_microphone\_mute\_state\_param::type](structbt__cap__commander__change__microphone__mute__state__param.md#a9cdb1eda2108fc341a6d7268fac689b0)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:946

[bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md)

Parameters for changing volume mute state.

**Definition** cap.h:915

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::count](structbt__cap__commander__change__volume__mute__state__param.md#a784542a30164a62d44fcd3f801bc29f8)

size\_t count

The number of members in members.

**Definition** cap.h:923

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::mute](structbt__cap__commander__change__volume__mute__state__param.md#ad4cc775dc74540a2b40126dba96776cd)

bool mute

The volume mute state to set.

**Definition** cap.h:930

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::type](structbt__cap__commander__change__volume__mute__state__param.md#ae4b664c4b8da062a83dfcc32ebd28775)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:917

[bt\_cap\_commander\_change\_volume\_mute\_state\_param::members](structbt__cap__commander__change__volume__mute__state__param.md#af54b6898bfcd42188cf45d65c72217d1)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:920

[bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md)

**Definition** cap.h:880

[bt\_cap\_commander\_change\_volume\_offset\_member\_param::offset](structbt__cap__commander__change__volume__offset__member__param.md#a7d9e94cd9eb79f1f7a14c8b9bb84e5a8)

int16\_t offset

The offset to set.

**Definition** cap.h:889

[bt\_cap\_commander\_change\_volume\_offset\_member\_param::member](structbt__cap__commander__change__volume__offset__member__param.md#a8e2e4f07be565ef1067d4955ebef50d4)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:882

[bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md)

Parameters for changing volume offset.

**Definition** cap.h:893

[bt\_cap\_commander\_change\_volume\_offset\_param::param](structbt__cap__commander__change__volume__offset__param.md#a2610505f60d1a67ffef916dadefe841d)

struct bt\_cap\_commander\_change\_volume\_offset\_member\_param \* param

The set of devices for this procedure.

**Definition** cap.h:898

[bt\_cap\_commander\_change\_volume\_offset\_param::type](structbt__cap__commander__change__volume__offset__param.md#a8c22810a91d3109c3d633156bf16dffd)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:895

[bt\_cap\_commander\_change\_volume\_offset\_param::count](structbt__cap__commander__change__volume__offset__param.md#ae3d416680196b0ee753a80d6fccb468b)

size\_t count

The number of parameters in param.

**Definition** cap.h:901

[bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md)

Parameters for changing absolute volume.

**Definition** cap.h:857

[bt\_cap\_commander\_change\_volume\_param::count](structbt__cap__commander__change__volume__param.md#a37198e9118f80e5521f140b6aa1d2640)

size\_t count

The number of members in members.

**Definition** cap.h:865

[bt\_cap\_commander\_change\_volume\_param::members](structbt__cap__commander__change__volume__param.md#a983656766a28118b018a70fef186f531)

union bt\_cap\_set\_member \* members

Coordinated or ad-hoc set member.

**Definition** cap.h:862

[bt\_cap\_commander\_change\_volume\_param::type](structbt__cap__commander__change__volume__param.md#ad98625aa08f54759efd349921d104c88)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:859

[bt\_cap\_commander\_change\_volume\_param::volume](structbt__cap__commander__change__volume__param.md#ada17f89c8948246d68818f2e44d5ea49)

uint8\_t volume

The absolute volume to set.

**Definition** cap.h:868

[bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md)

**Definition** cap.h:390

[bt\_cap\_initiator\_broadcast\_create\_param::subgroup\_params](structbt__cap__initiator__broadcast__create__param.md#a2eafc157450237cf311d6144e7431839)

struct bt\_cap\_initiator\_broadcast\_subgroup\_param \* subgroup\_params

Array of stream parameters.

**Definition** cap.h:395

[bt\_cap\_initiator\_broadcast\_create\_param::encryption](structbt__cap__initiator__broadcast__create__param.md#a4432bee0e365c189996b9f70c7226542)

bool encryption

Whether or not to encrypt the streams.

**Definition** cap.h:410

[bt\_cap\_initiator\_broadcast\_create\_param::broadcast\_code](structbt__cap__initiator__broadcast__create__param.md#a9053fbfd5b847db896b3d832338f6b92)

uint8\_t broadcast\_code[BT\_AUDIO\_BROADCAST\_CODE\_SIZE]

16-octet broadcast code.

**Definition** cap.h:424

[bt\_cap\_initiator\_broadcast\_create\_param::packing](structbt__cap__initiator__broadcast__create__param.md#ae81ee3dada58a3354c70401380916cbc)

uint8\_t packing

Broadcast Source packing mode.

**Definition** cap.h:407

[bt\_cap\_initiator\_broadcast\_create\_param::subgroup\_count](structbt__cap__initiator__broadcast__create__param.md#aee3e0244b59503311bc445f36977a85b)

size\_t subgroup\_count

The number of parameters in subgroup\_params.

**Definition** cap.h:392

[bt\_cap\_initiator\_broadcast\_create\_param::qos](structbt__cap__initiator__broadcast__create__param.md#af7533744fc262dac4d71bc98d33bbee2)

struct bt\_audio\_codec\_qos \* qos

Quality of Service configuration.

**Definition** cap.h:398

[bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md)

**Definition** cap.h:365

[bt\_cap\_initiator\_broadcast\_stream\_param::data](structbt__cap__initiator__broadcast__stream__param.md#a72720e8423dbeb0341041cc24a9e0869)

uint8\_t \* data

BIS Codec Specific Configuration.

**Definition** cap.h:376

[bt\_cap\_initiator\_broadcast\_stream\_param::stream](structbt__cap__initiator__broadcast__stream__param.md#a7e5ddb85024b58d6ecbb6d7f70ef5c6a)

struct bt\_cap\_stream \* stream

Audio stream.

**Definition** cap.h:367

[bt\_cap\_initiator\_broadcast\_stream\_param::data\_len](structbt__cap__initiator__broadcast__stream__param.md#aa4677e278d6d4823551ccfd9c27c68a4)

size\_t data\_len

The length of the p data array.

**Definition** cap.h:373

[bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md)

**Definition** cap.h:379

[bt\_cap\_initiator\_broadcast\_subgroup\_param::stream\_params](structbt__cap__initiator__broadcast__subgroup__param.md#a32e99898ee97a56105497c3ae480692a)

struct bt\_cap\_initiator\_broadcast\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:384

[bt\_cap\_initiator\_broadcast\_subgroup\_param::stream\_count](structbt__cap__initiator__broadcast__subgroup__param.md#a577a27836a02c7a6219182f1cb0bd769)

size\_t stream\_count

The number of parameters in stream\_params.

**Definition** cap.h:381

[bt\_cap\_initiator\_broadcast\_subgroup\_param::codec\_cfg](structbt__cap__initiator__broadcast__subgroup__param.md#a62d3a6a13a10f3bd594f064e761dba47)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Subgroup Codec configuration.

**Definition** cap.h:387

[bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md)

Callback structure for CAP procedures.

**Definition** cap.h:58

[bt\_cap\_stream](structbt__cap__stream.md)

**Definition** cap.h:146

[bt\_cap\_stream::ops](structbt__cap__stream.md#aa58c47ace3f844533ab545906ede52ba)

struct bt\_bap\_stream\_ops \* ops

**Definition** cap.h:148

[bt\_cap\_stream::bap\_stream](structbt__cap__stream.md#ad9d974d18ec42079b81107485b43bc18)

struct bt\_bap\_stream bap\_stream

**Definition** cap.h:147

[bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_start() function.

**Definition** cap.h:234

[bt\_cap\_unicast\_audio\_start\_param::type](structbt__cap__unicast__audio__start__param.md#a7d0055719cee1cb1b0a7c1b6dc88bda5)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:236

[bt\_cap\_unicast\_audio\_start\_param::count](structbt__cap__unicast__audio__start__param.md#acacd3692c807c536882dccaea074f667)

size\_t count

The number of parameters in stream\_params.

**Definition** cap.h:239

[bt\_cap\_unicast\_audio\_start\_param::stream\_params](structbt__cap__unicast__audio__start__param.md#af3e7a147448a19d2fb1ef802c525636b)

struct bt\_cap\_unicast\_audio\_start\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:242

[bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md)

Stream specific parameters for the bt\_cap\_initiator\_unicast\_audio\_start() function.

**Definition** cap.h:213

[bt\_cap\_unicast\_audio\_start\_stream\_param::stream](structbt__cap__unicast__audio__start__stream__param.md#a109acdedd1249ea8342f06de28989d4e)

struct bt\_cap\_stream \* stream

Stream for the member.

**Definition** cap.h:218

[bt\_cap\_unicast\_audio\_start\_stream\_param::codec\_cfg](structbt__cap__unicast__audio__start__stream__param.md#a5cf7ff347ff602bc4387e5b75f09205a)

struct bt\_audio\_codec\_cfg \* codec\_cfg

Codec configuration.

**Definition** cap.h:230

[bt\_cap\_unicast\_audio\_start\_stream\_param::member](structbt__cap__unicast__audio__start__stream__param.md#a9613a24e05a362a2f70d8e433ca6b42b)

union bt\_cap\_set\_member member

Coordinated or ad-hoc set member.

**Definition** cap.h:215

[bt\_cap\_unicast\_audio\_start\_stream\_param::ep](structbt__cap__unicast__audio__start__stream__param.md#aa9a13263d287a2ddb241a8dc13baeffb)

struct bt\_bap\_ep \* ep

Endpoint reference for the stream.

**Definition** cap.h:221

[bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_stop() function.

**Definition** cap.h:274

[bt\_cap\_unicast\_audio\_stop\_param::count](structbt__cap__unicast__audio__stop__param.md#a11b5ac19301ce8ebd2c35df45c60bfe2)

size\_t count

The number of streams in streams.

**Definition** cap.h:279

[bt\_cap\_unicast\_audio\_stop\_param::type](structbt__cap__unicast__audio__stop__param.md#a773eedda9ae8969e8749d56ffa3d1afa)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:276

[bt\_cap\_unicast\_audio\_stop\_param::streams](structbt__cap__unicast__audio__stop__param.md#a94707060a6ef15dd8d3e48eae526aa82)

struct bt\_cap\_stream \*\* streams

Array of streams to stop.

**Definition** cap.h:282

[bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md)

Parameters for the bt\_cap\_initiator\_unicast\_audio\_update() function.

**Definition** cap.h:262

[bt\_cap\_unicast\_audio\_update\_param::stream\_params](structbt__cap__unicast__audio__update__param.md#a3d8f940d8401b8524764e7ecab3cfacb)

struct bt\_cap\_unicast\_audio\_update\_stream\_param \* stream\_params

Array of stream parameters.

**Definition** cap.h:270

[bt\_cap\_unicast\_audio\_update\_param::type](structbt__cap__unicast__audio__update__param.md#a768029ce89b74e0bcc06bb50f1fd8dcd)

enum bt\_cap\_set\_type type

The type of the set.

**Definition** cap.h:264

[bt\_cap\_unicast\_audio\_update\_param::count](structbt__cap__unicast__audio__update__param.md#ac8982f313161380af536d41ec48dcba1)

size\_t count

The number of parameters in stream\_params.

**Definition** cap.h:267

[bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md)

Stream specific parameters for the bt\_cap\_initiator\_unicast\_audio\_update() function.

**Definition** cap.h:246

[bt\_cap\_unicast\_audio\_update\_stream\_param::meta\_len](structbt__cap__unicast__audio__update__stream__param.md#a07c1ab3158377ce51d94084ad7dc3e9c)

size\_t meta\_len

The length of meta.

**Definition** cap.h:251

[bt\_cap\_unicast\_audio\_update\_stream\_param::stream](structbt__cap__unicast__audio__update__stream__param.md#a7a2042834b79ca37e3b3df9fc2f8a7a1)

struct bt\_cap\_stream \* stream

Stream to update.

**Definition** cap.h:248

[bt\_cap\_unicast\_audio\_update\_stream\_param::meta](structbt__cap__unicast__audio__update__stream__param.md#a87833f9e91b47513a27db0aa7692d8c0)

uint8\_t \* meta

The new metadata.

**Definition** cap.h:258

[bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md)

**Definition** cap.h:579

[bt\_cap\_unicast\_to\_broadcast\_param::unicast\_group](structbt__cap__unicast__to__broadcast__param.md#a249a8ae6be36346c78dddb4406ed5239)

struct bt\_bap\_unicast\_group \* unicast\_group

The source unicast group with the streams.

**Definition** cap.h:581

[bt\_cap\_unicast\_to\_broadcast\_param::broadcast\_code](structbt__cap__unicast__to__broadcast__param.md#ad27a5f69ce697f029887e597090120a3)

uint8\_t broadcast\_code[BT\_ISO\_BROADCAST\_CODE\_SIZE]

16-octet broadcast code.

**Definition** cap.h:603

[bt\_cap\_unicast\_to\_broadcast\_param::encrypt](structbt__cap__unicast__to__broadcast__param.md#ae8ebc736ab9a00ab3ed6e997e2806262)

bool encrypt

Whether or not to encrypt the streams.

**Definition** cap.h:589

[bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md)

Struct representing a coordinated set instance on a remote device.

**Definition** csip.h:268

[bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md)

Register structure for Coordinated Set Identification Service.

**Definition** csip.h:111

[bt\_iso\_tx\_info](structbt__iso__tx__info.md)

ISO Meta Data structure for transmitted ISO packets.

**Definition** iso.h:303

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[bt\_cap\_set\_member](unionbt__cap__set__member.md)

Represents a Common Audio Set member that are either in a Coordinated or ad-hoc set.

**Definition** cap.h:138

[bt\_cap\_set\_member::member](unionbt__cap__set__member.md#a692a1be2fbd79c4b6a0fbce564ff2973)

struct bt\_conn \* member

Connection pointer if the type is BT\_CAP\_SET\_TYPE\_AD\_HOC.

**Definition** cap.h:140

[bt\_cap\_set\_member::csip](unionbt__cap__set__member.md#ac17db41d21a92d8d128b70962e4eb2d6)

struct bt\_csip\_set\_coordinator\_csis\_inst \* csip

CSIP Coordinated Set struct used if type is BT\_CAP\_SET\_TYPE\_CSIP.

**Definition** cap.h:143

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [cap.h](bluetooth_2audio_2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
