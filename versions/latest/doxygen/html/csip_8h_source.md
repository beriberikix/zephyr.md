---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/csip_8h_source.html
original_path: doxygen/html/csip_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

csip.h

[Go to the documentation of this file.](csip_8h.md)

1

5

6/\*

7 \* Copyright (c) 2021-2024 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_SUBSYS\_BLUETOOTH\_AUDIO\_CSIP\_H\_

13#define ZEPHYR\_SUBSYS\_BLUETOOTH\_AUDIO\_CSIP\_H\_

14

29

30#include <[stdbool.h](stdbool_8h.md)>

31#include <stddef.h>

32#include <[stdint.h](stdint_8h.md)>

33

34#include <zephyr/autoconf.h>

35#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

36#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

37#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

38#include <[zephyr/bluetooth/gap.h](gap_8h.md)>

39#include <[zephyr/kernel.h](kernel_8h.md)>

40#include <[zephyr/sys/slist.h](slist_8h.md)>

41

42#ifdef \_\_cplusplus

43extern "C" {

44#endif

45

[ 47](group__bt__csip.md#ga1633e4caaa03a21da0a5431f5f263076)#define BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE K\_SECONDS(10)

48

53#if defined(CONFIG\_BT\_CSIP\_SET\_COORDINATOR)

54#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES CONFIG\_BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES

55#else

[ 56](group__bt__csip.md#ga42702049524f7ce24dfb6061120414df)#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES 0

57#endif /\* CONFIG\_BT\_CSIP\_SET\_COORDINATOR \*/

58

[ 60](group__bt__csip.md#gac2aa2ce09ff4aad8bc423dd5b5643038)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT 0x00

[ 62](group__bt__csip.md#gae6422e7e38bacc39ed2f8d52efe9d6db)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC 0x01

[ 64](group__bt__csip.md#ga0175e269097a2b6f8f303ee97527db4a)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT 0x02

[ 66](group__bt__csip.md#gaa245a416becaaaeb118b440f9ba2431d)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY 0x03

67

[ 69](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)#define BT\_CSIP\_SIRK\_SIZE 16

70

[ 72](group__bt__csip.md#ga5b0149fec5d38e7003593c227b561506)#define BT\_CSIP\_RSI\_SIZE 6

73

74/\* Coordinate Set Identification Service Error codes \*/

[ 76](group__bt__csip.md#ga00f382d9fe9afb55acfd6f758cef6389)#define BT\_CSIP\_ERROR\_LOCK\_DENIED 0x80

[ 78](group__bt__csip.md#gac6eda3e7a9a06f86bc715df20e14daa1)#define BT\_CSIP\_ERROR\_LOCK\_RELEASE\_DENIED 0x81

[ 80](group__bt__csip.md#gaeca8a3a9e136882c200c432b9f83203e)#define BT\_CSIP\_ERROR\_LOCK\_INVAL\_VALUE 0x82

[ 82](group__bt__csip.md#ga4e0da5f82ef943e660f669a2962bcc7a)#define BT\_CSIP\_ERROR\_SIRK\_OOB\_ONLY 0x83

[ 84](group__bt__csip.md#gaabd5b74d0e805bfb0b492a45445ec4c4)#define BT\_CSIP\_ERROR\_LOCK\_ALREADY\_GRANTED 0x84

85

[ 94](group__bt__csip.md#ga04fcc2431bec35d53664c8f5ab18100d)#define BT\_CSIP\_DATA\_RSI(\_rsi) BT\_DATA(BT\_DATA\_CSIS\_RSI, \_rsi, BT\_CSIP\_RSI\_SIZE)

95

97struct bt\_csip\_set\_member\_svc\_inst;

98

[ 100](structbt__csip__set__member__cb.md)struct [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md) {

[ 112](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c) void (\*[lock\_changed](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c))(struct bt\_conn \*conn,

113 struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

114 bool locked);

115

[ 129](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[sirk\_read\_req](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9))(struct bt\_conn \*conn,

130 struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

131};

132

[ 134](structbt__csip__set__member__register__param.md)struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) {

[ 140](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_size](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83);

141

[ 148](structbt__csip__set__member__register__param.md#abad0332cc3747749673795d867f8e90f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sirk](structbt__csip__set__member__register__param.md#abad0332cc3747749673795d867f8e90f)[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)];

149

[ 155](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d) bool [lockable](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d);

156

[ 164](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rank](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a);

165

[ 167](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1) struct [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md) \*[cb](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1);

168

169#if CONFIG\_BT\_CSIP\_SET\_MEMBER\_MAX\_INSTANCE\_COUNT > 1 || defined(\_\_DOXYGEN\_\_)

[ 179](structbt__csip__set__member__register__param.md#a7b74ebf8608ba0a9c50d83d414ff15b2) const struct [bt\_gatt\_service](structbt__gatt__service.md) \*[parent](structbt__csip__set__member__register__param.md#a7b74ebf8608ba0a9c50d83d414ff15b2);

180#endif /\* CONFIG\_BT\_CSIP\_SET\_MEMBER\_MAX\_INSTANCE\_COUNT > 1 \*/

181};

182

[ 192](group__bt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c)void \*[bt\_csip\_set\_member\_svc\_decl\_get](group__bt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c)(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

193

[ 209](group__bt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)int [bt\_csip\_set\_member\_register](group__bt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)(const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param,

210 struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst);

211

[ 221](group__bt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)int [bt\_csip\_set\_member\_unregister](group__bt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

222

[ 229](group__bt__csip.md#gae07b5073f1dd3381195e3827e6a803f0)int [bt\_csip\_set\_member\_sirk](group__bt__csip.md#gae07b5073f1dd3381195e3827e6a803f0)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

230 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)]);

231

[ 252](group__bt__csip.md#gaef51ab05dbe9d8a69674f7020e8f837f)int [bt\_csip\_set\_member\_set\_size\_and\_rank](group__bt__csip.md#gaef51ab05dbe9d8a69674f7020e8f837f)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size,

253 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rank);

254

[ 256](structbt__csip__set__member__set__info.md)struct [bt\_csip\_set\_member\_set\_info](structbt__csip__set__member__set__info.md) {

[ 258](structbt__csip__set__member__set__info.md#aec69fc3bc6e66d7bda2810c20a260d9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sirk](structbt__csip__set__member__set__info.md#aec69fc3bc6e66d7bda2810c20a260d9c)[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)];

259

[ 261](structbt__csip__set__member__set__info.md#afcb0ae1252ca6ac09fbdaaf5c8ae8dfa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_size](structbt__csip__set__member__set__info.md#afcb0ae1252ca6ac09fbdaaf5c8ae8dfa);

262

[ 268](structbt__csip__set__member__set__info.md#aa715eda78908c603ec11a48846018845) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rank](structbt__csip__set__member__set__info.md#aa715eda78908c603ec11a48846018845);

269

[ 271](structbt__csip__set__member__set__info.md#a52ba91f4e3ee911f575160355368aae5) bool [lockable](structbt__csip__set__member__set__info.md#a52ba91f4e3ee911f575160355368aae5): 1;

272

[ 274](structbt__csip__set__member__set__info.md#ae0e082aac881500f2005489d6aa88090) bool [locked](structbt__csip__set__member__set__info.md#ae0e082aac881500f2005489d6aa88090): 1;

275

[ 281](structbt__csip__set__member__set__info.md#a75ca9b78932626f167b186b203611c27) [bt\_addr\_le\_t](structbt__addr__le__t.md) [lock\_client\_addr](structbt__csip__set__member__set__info.md#a75ca9b78932626f167b186b203611c27);

282};

283

[ 293](group__bt__csip.md#gad80917089bc7e629cc3cb9d7fbf6cf45)int [bt\_csip\_set\_member\_get\_info](group__bt__csip.md#gad80917089bc7e629cc3cb9d7fbf6cf45)(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

294 struct [bt\_csip\_set\_member\_set\_info](structbt__csip__set__member__set__info.md) \*info);

295

[ 306](group__bt__csip.md#ga8c59233f7e4c8716042c20e25f42a474)int [bt\_csip\_set\_member\_generate\_rsi](group__bt__csip.md#ga8c59233f7e4c8716042c20e25f42a474)(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

307 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsi[[BT\_CSIP\_RSI\_SIZE](group__bt__csip.md#ga5b0149fec5d38e7003593c227b561506)]);

308

[ 320](group__bt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606)int [bt\_csip\_set\_member\_lock](group__bt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

321 bool lock, bool force);

322

[ 324](structbt__csip__set__coordinator__set__info.md)struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) {

[ 331](structbt__csip__set__coordinator__set__info.md#a50caa7b3a231e6944c807f7653edce3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sirk](structbt__csip__set__coordinator__set__info.md#a50caa7b3a231e6944c807f7653edce3c)[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)];

332

[ 338](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_size](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9);

339

[ 345](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rank](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c);

346

[ 348](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2) bool [lockable](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2);

349};

350

[ 357](structbt__csip__set__coordinator__csis__inst.md)struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) {

[ 359](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d) struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) [info](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d);

360

[ 362](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f) void \*[svc\_inst](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f);

363};

364

[ 366](structbt__csip__set__coordinator__set__member.md)struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) {

[ 368](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8) struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) [insts](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8)[[BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES](group__bt__csip.md#ga42702049524f7ce24dfb6061120414df)];

369};

370

[ 380](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c)typedef void (\*[bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c))(

381 struct bt\_conn \*conn,

382 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member,

383 int err, size\_t set\_count);

384

[ 393](group__bt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73)int [bt\_csip\_set\_coordinator\_discover](group__bt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73)(struct bt\_conn \*conn);

394

407struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*

[ 408](group__bt__csip.md#ga8c3666d8f20f909dd4fa2010ae02c9a5)[bt\_csip\_set\_coordinator\_set\_member\_by\_conn](group__bt__csip.md#ga8c3666d8f20f909dd4fa2010ae02c9a5)(const struct bt\_conn \*conn);

409

[ 416](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634)typedef void (\*[bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634))(int err);

417

[ 428](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b)typedef void (\*[bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b))(

429 struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst, bool locked);

430

[ 438](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2)typedef void (\*[bt\_csip\_set\_coordinator\_sirk\_changed\_cb](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2))(

439 struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst);

440

[ 456](group__bt__csip.md#gaee24f364c90cdcd0b6f49c8b297a34a7)typedef void (\*[bt\_csip\_set\_coordinator\_size\_changed\_cb](group__bt__csip.md#gaee24f364c90cdcd0b6f49c8b297a34a7))(

457 struct bt\_conn \*conn, const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst);

458

[ 473](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb)typedef void (\*[bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb))(

474 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

475 int err, bool locked,

476 struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member);

477

[ 483](structbt__csip__set__coordinator__cb.md)struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) {

[ 485](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0) [bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c) [discover](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0);

[ 487](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba) [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) [lock\_set](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba);

[ 489](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de) [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) [release\_set](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de);

[ 491](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1) [bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b) [lock\_changed](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1);

[ 493](structbt__csip__set__coordinator__cb.md#a5bb08e8ce5759f67d2ff02459efe114d) [bt\_csip\_set\_coordinator\_sirk\_changed\_cb](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2) [sirk\_changed](structbt__csip__set__coordinator__cb.md#a5bb08e8ce5759f67d2ff02459efe114d);

[ 495](structbt__csip__set__coordinator__cb.md#ab328cf27c2966d7762d82ffb0d334d68) [bt\_csip\_set\_coordinator\_size\_changed\_cb](group__bt__csip.md#gaee24f364c90cdcd0b6f49c8b297a34a7) [size\_changed](structbt__csip__set__coordinator__cb.md#ab328cf27c2966d7762d82ffb0d334d68);

[ 497](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c) [bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb) [ordered\_access](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c);

498

501 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

503};

504

[ 513](group__bt__csip.md#gac2a5c323d472c58a7d0cc6060782133e)bool [bt\_csip\_set\_coordinator\_is\_set\_member](group__bt__csip.md#gac2a5c323d472c58a7d0cc6060782133e)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)],

514 struct [bt\_data](structbt__data.md) \*data);

515

[ 523](group__bt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37)int [bt\_csip\_set\_coordinator\_register\_cb](group__bt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37)(struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) \*cb);

524

[ 536](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9))(

537 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

538 struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[],

539 size\_t count);

540

[ 564](group__bt__csip.md#gacd83494562a62fbdbc7282107d4454b4)int [bt\_csip\_set\_coordinator\_ordered\_access](group__bt__csip.md#gacd83494562a62fbdbc7282107d4454b4)(

565 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[],

566 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

567 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

568 [bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9) cb);

569

[ 586](group__bt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)int [bt\_csip\_set\_coordinator\_lock](group__bt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)(const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members,

587 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

588 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info);

589

[ 604](group__bt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)int [bt\_csip\_set\_coordinator\_release](group__bt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)(const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members,

605 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

606 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info);

607

608#ifdef \_\_cplusplus

609}

610#endif

611

615

616#endif /\* ZEPHYR\_SUBSYS\_BLUETOOTH\_AUDIO\_CSIP\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[gap.h](gap_8h.md)

Bluetooth Generic Access Profile defines and Assigned Numbers.

[bt\_csip\_set\_coordinator\_register\_cb](group__bt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37)

int bt\_csip\_set\_coordinator\_register\_cb(struct bt\_csip\_set\_coordinator\_cb \*cb)

Registers callbacks for csip\_set\_coordinator.

[bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb)

void(\* bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t)(const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info, int err, bool locked, struct bt\_csip\_set\_coordinator\_set\_member \*member)

Callback for bt\_csip\_set\_coordinator\_ordered\_access().

**Definition** csip.h:473

[bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9)

bool(\* bt\_csip\_set\_coordinator\_ordered\_access\_t)(const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info, struct bt\_csip\_set\_coordinator\_set\_member \*members[], size\_t count)

Callback function definition for bt\_csip\_set\_coordinator\_ordered\_access().

**Definition** csip.h:536

[bt\_csip\_set\_coordinator\_lock](group__bt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)

int bt\_csip\_set\_coordinator\_lock(const struct bt\_csip\_set\_coordinator\_set\_member \*\*members, uint8\_t count, const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info)

Lock an array of set members.

[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)

#define BT\_CSIP\_SIRK\_SIZE

Size of the Set Identification Resolving Key (SIRK).

**Definition** csip.h:69

[BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES](group__bt__csip.md#ga42702049524f7ce24dfb6061120414df)

#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES

Defines the maximum number of Coordinated Set Identification service instances for the Coordinated Se...

**Definition** csip.h:56

[bt\_csip\_set\_coordinator\_release](group__bt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)

int bt\_csip\_set\_coordinator\_release(const struct bt\_csip\_set\_coordinator\_set\_member \*\*members, uint8\_t count, const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info)

Release an array of set members.

[BT\_CSIP\_RSI\_SIZE](group__bt__csip.md#ga5b0149fec5d38e7003593c227b561506)

#define BT\_CSIP\_RSI\_SIZE

Size of the Resolvable Set Identifier (RSI).

**Definition** csip.h:72

[bt\_csip\_set\_coordinator\_discover](group__bt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73)

int bt\_csip\_set\_coordinator\_discover(struct bt\_conn \*conn)

Initialise the csip\_set\_coordinator instance for a connection.

[bt\_csip\_set\_coordinator\_set\_member\_by\_conn](group__bt__csip.md#ga8c3666d8f20f909dd4fa2010ae02c9a5)

struct bt\_csip\_set\_coordinator\_set\_member \* bt\_csip\_set\_coordinator\_set\_member\_by\_conn(const struct bt\_conn \*conn)

Get the set member from a connection pointer.

[bt\_csip\_set\_member\_generate\_rsi](group__bt__csip.md#ga8c59233f7e4c8716042c20e25f42a474)

int bt\_csip\_set\_member\_generate\_rsi(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, uint8\_t rsi[6])

Generate the Resolvable Set Identifier (RSI) value.

[bt\_csip\_set\_member\_lock](group__bt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606)

int bt\_csip\_set\_member\_lock(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, bool lock, bool force)

Locks a specific Coordinated Set Identification Service instance on the server.

[bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b)

void(\* bt\_csip\_set\_coordinator\_lock\_changed\_cb)(struct bt\_csip\_set\_coordinator\_csis\_inst \*inst, bool locked)

Callback when the lock value on a set of a connected device changes.

**Definition** csip.h:428

[bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634)

void(\* bt\_csip\_set\_coordinator\_lock\_set\_cb)(int err)

Callback for locking a set across one or more devices.

**Definition** csip.h:416

[bt\_csip\_set\_member\_unregister](group__bt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)

int bt\_csip\_set\_member\_unregister(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Unregister a Coordinated Set Identification Service instance.

[bt\_csip\_set\_member\_register](group__bt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)

int bt\_csip\_set\_member\_register(const struct bt\_csip\_set\_member\_register\_param \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst)

Register a Coordinated Set Identification Service instance.

[bt\_csip\_set\_member\_svc\_decl\_get](group__bt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c)

void \* bt\_csip\_set\_member\_svc\_decl\_get(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Get the service declaration attribute.

[bt\_csip\_set\_coordinator\_is\_set\_member](group__bt__csip.md#gac2a5c323d472c58a7d0cc6060782133e)

bool bt\_csip\_set\_coordinator\_is\_set\_member(const uint8\_t sirk[16], struct bt\_data \*data)

Check if advertising data indicates a set member.

[bt\_csip\_set\_coordinator\_ordered\_access](group__bt__csip.md#gacd83494562a62fbdbc7282107d4454b4)

int bt\_csip\_set\_coordinator\_ordered\_access(const struct bt\_csip\_set\_coordinator\_set\_member \*members[], uint8\_t count, const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info, bt\_csip\_set\_coordinator\_ordered\_access\_t cb)

Access Coordinated Set devices in an ordered manner as a client.

[bt\_csip\_set\_coordinator\_sirk\_changed\_cb](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2)

void(\* bt\_csip\_set\_coordinator\_sirk\_changed\_cb)(struct bt\_csip\_set\_coordinator\_csis\_inst \*inst)

Callback when the SIRK value of a set of a connected device changes.

**Definition** csip.h:438

[bt\_csip\_set\_member\_get\_info](group__bt__csip.md#gad80917089bc7e629cc3cb9d7fbf6cf45)

int bt\_csip\_set\_member\_get\_info(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, struct bt\_csip\_set\_member\_set\_info \*info)

Get information about a service instances.

[bt\_csip\_set\_member\_sirk](group__bt__csip.md#gae07b5073f1dd3381195e3827e6a803f0)

int bt\_csip\_set\_member\_sirk(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, const uint8\_t sirk[16])

Set the SIRK of a service instance.

[bt\_csip\_set\_coordinator\_size\_changed\_cb](group__bt__csip.md#gaee24f364c90cdcd0b6f49c8b297a34a7)

void(\* bt\_csip\_set\_coordinator\_size\_changed\_cb)(struct bt\_conn \*conn, const struct bt\_csip\_set\_coordinator\_csis\_inst \*inst)

Callback when the size of a set of a connected device changes.

**Definition** csip.h:456

[bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c)

void(\* bt\_csip\_set\_coordinator\_discover\_cb)(struct bt\_conn \*conn, const struct bt\_csip\_set\_coordinator\_set\_member \*member, int err, size\_t set\_count)

Callback for discovering Coordinated Set Identification Services.

**Definition** csip.h:380

[bt\_csip\_set\_member\_set\_size\_and\_rank](group__bt__csip.md#gaef51ab05dbe9d8a69674f7020e8f837f)

int bt\_csip\_set\_member\_set\_size\_and\_rank(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, uint8\_t size, uint8\_t rank)

Set a new size and rank for a service instance.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](kernel_8h.md)

Public kernel APIs.

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md)

Struct to hold the Coordinated Set Identification Profile Set Coordinator callbacks.

**Definition** csip.h:483

[bt\_csip\_set\_coordinator\_cb::lock\_set](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba)

bt\_csip\_set\_coordinator\_lock\_set\_cb lock\_set

Callback when locking a set has finished.

**Definition** csip.h:487

[bt\_csip\_set\_coordinator\_cb::sirk\_changed](structbt__csip__set__coordinator__cb.md#a5bb08e8ce5759f67d2ff02459efe114d)

bt\_csip\_set\_coordinator\_sirk\_changed\_cb sirk\_changed

Callback when a set's SIRK has changed.

**Definition** csip.h:493

[bt\_csip\_set\_coordinator\_cb::discover](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0)

bt\_csip\_set\_coordinator\_discover\_cb discover

Callback when discovery has finished.

**Definition** csip.h:485

[bt\_csip\_set\_coordinator\_cb::size\_changed](structbt__csip__set__coordinator__cb.md#ab328cf27c2966d7762d82ffb0d334d68)

bt\_csip\_set\_coordinator\_size\_changed\_cb size\_changed

Callback when a set's size has changed.

**Definition** csip.h:495

[bt\_csip\_set\_coordinator\_cb::release\_set](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de)

bt\_csip\_set\_coordinator\_lock\_set\_cb release\_set

Callback when unlocking a set has finished.

**Definition** csip.h:489

[bt\_csip\_set\_coordinator\_cb::lock\_changed](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1)

bt\_csip\_set\_coordinator\_lock\_changed\_cb lock\_changed

Callback when a set's lock state has changed.

**Definition** csip.h:491

[bt\_csip\_set\_coordinator\_cb::ordered\_access](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c)

bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t ordered\_access

Callback for the ordered access procedure.

**Definition** csip.h:497

[bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md)

Struct representing a coordinated set instance on a remote device.

**Definition** csip.h:357

[bt\_csip\_set\_coordinator\_csis\_inst::info](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d)

struct bt\_csip\_set\_coordinator\_set\_info info

Information about the coordinated set.

**Definition** csip.h:359

[bt\_csip\_set\_coordinator\_csis\_inst::svc\_inst](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f)

void \* svc\_inst

Internally used pointer value.

**Definition** csip.h:362

[bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md)

Information about a specific set.

**Definition** csip.h:324

[bt\_csip\_set\_coordinator\_set\_info::rank](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c)

uint8\_t rank

The rank of the set on the remote device.

**Definition** csip.h:345

[bt\_csip\_set\_coordinator\_set\_info::sirk](structbt__csip__set__coordinator__set__info.md#a50caa7b3a231e6944c807f7653edce3c)

uint8\_t sirk[16]

The 16 octet set Set Identity Resolving Key (SIRK).

**Definition** csip.h:331

[bt\_csip\_set\_coordinator\_set\_info::lockable](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2)

bool lockable

Whether or not the set can be locked on this device.

**Definition** csip.h:348

[bt\_csip\_set\_coordinator\_set\_info::set\_size](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9)

uint8\_t set\_size

The size of the set.

**Definition** csip.h:338

[bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md)

Struct representing a remote device as a set member.

**Definition** csip.h:366

[bt\_csip\_set\_coordinator\_set\_member::insts](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8)

struct bt\_csip\_set\_coordinator\_csis\_inst insts[0]

Array of Coordinated Set Identification Service instances for the remote device.

**Definition** csip.h:368

[bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md)

Callback structure for the Coordinated Set Identification Service.

**Definition** csip.h:100

[bt\_csip\_set\_member\_cb::sirk\_read\_req](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9)

uint8\_t(\* sirk\_read\_req)(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Request from a peer device to read the sirk.

**Definition** csip.h:129

[bt\_csip\_set\_member\_cb::lock\_changed](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c)

void(\* lock\_changed)(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, bool locked)

Callback whenever the lock changes on the server.

**Definition** csip.h:112

[bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md)

Register structure for Coordinated Set Identification Service.

**Definition** csip.h:134

[bt\_csip\_set\_member\_register\_param::cb](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1)

struct bt\_csip\_set\_member\_cb \* cb

Pointer to the callback structure.

**Definition** csip.h:167

[bt\_csip\_set\_member\_register\_param::parent](structbt__csip__set__member__register__param.md#a7b74ebf8608ba0a9c50d83d414ff15b2)

const struct bt\_gatt\_service \* parent

Parent service pointer.

**Definition** csip.h:179

[bt\_csip\_set\_member\_register\_param::sirk](structbt__csip__set__member__register__param.md#abad0332cc3747749673795d867f8e90f)

uint8\_t sirk[16]

The unique Set Identity Resolving Key (SIRK).

**Definition** csip.h:148

[bt\_csip\_set\_member\_register\_param::lockable](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d)

bool lockable

Boolean to set whether the set is lockable by clients.

**Definition** csip.h:155

[bt\_csip\_set\_member\_register\_param::rank](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a)

uint8\_t rank

Rank of this device in this set.

**Definition** csip.h:164

[bt\_csip\_set\_member\_register\_param::set\_size](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83)

uint8\_t set\_size

Size of the set.

**Definition** csip.h:140

[bt\_csip\_set\_member\_set\_info](structbt__csip__set__member__set__info.md)

Struct to hold information about a service instance.

**Definition** csip.h:256

[bt\_csip\_set\_member\_set\_info::lockable](structbt__csip__set__member__set__info.md#a52ba91f4e3ee911f575160355368aae5)

bool lockable

Whether the set is lockable.

**Definition** csip.h:271

[bt\_csip\_set\_member\_set\_info::lock\_client\_addr](structbt__csip__set__member__set__info.md#a75ca9b78932626f167b186b203611c27)

bt\_addr\_le\_t lock\_client\_addr

The address of the client that currently holds the lock.

**Definition** csip.h:281

[bt\_csip\_set\_member\_set\_info::rank](structbt__csip__set__member__set__info.md#aa715eda78908c603ec11a48846018845)

uint8\_t rank

The rank.

**Definition** csip.h:268

[bt\_csip\_set\_member\_set\_info::locked](structbt__csip__set__member__set__info.md#ae0e082aac881500f2005489d6aa88090)

bool locked

Whether the set is currently locked.

**Definition** csip.h:274

[bt\_csip\_set\_member\_set\_info::sirk](structbt__csip__set__member__set__info.md#aec69fc3bc6e66d7bda2810c20a260d9c)

uint8\_t sirk[16]

The 16-octet SIRK.

**Definition** csip.h:258

[bt\_csip\_set\_member\_set\_info::set\_size](structbt__csip__set__member__set__info.md#afcb0ae1252ca6ac09fbdaaf5c8ae8dfa)

uint8\_t set\_size

The set size.

**Definition** csip.h:261

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:531

[bt\_gatt\_service](structbt__gatt__service.md)

GATT Service structure.

**Definition** gatt.h:332

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [csip.h](csip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
