---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/csip_8h_source.html
original_path: doxygen/html/csip_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

35#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

36#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

37#include <[zephyr/bluetooth/gap.h](gap_8h.md)>

38#include <[zephyr/kernel.h](kernel_8h.md)>

39#include <[zephyr/sys/slist.h](slist_8h.md)>

40

41#ifdef \_\_cplusplus

42extern "C" {

43#endif

44

[ 46](group__bt__csip.md#ga1633e4caaa03a21da0a5431f5f263076)#define BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE K\_SECONDS(10)

47

52#if defined(CONFIG\_BT\_CSIP\_SET\_COORDINATOR)

53#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES CONFIG\_BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES

54#else

[ 55](group__bt__csip.md#ga42702049524f7ce24dfb6061120414df)#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES 0

56#endif /\* CONFIG\_BT\_CSIP\_SET\_COORDINATOR \*/

57

[ 59](group__bt__csip.md#gac2aa2ce09ff4aad8bc423dd5b5643038)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT 0x00

[ 61](group__bt__csip.md#gae6422e7e38bacc39ed2f8d52efe9d6db)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC 0x01

[ 63](group__bt__csip.md#ga0175e269097a2b6f8f303ee97527db4a)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT 0x02

[ 65](group__bt__csip.md#gaa245a416becaaaeb118b440f9ba2431d)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY 0x03

66

[ 68](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)#define BT\_CSIP\_SIRK\_SIZE 16

69

[ 71](group__bt__csip.md#ga5b0149fec5d38e7003593c227b561506)#define BT\_CSIP\_RSI\_SIZE 6

72

73/\* Coordinate Set Identification Service Error codes \*/

[ 75](group__bt__csip.md#ga00f382d9fe9afb55acfd6f758cef6389)#define BT\_CSIP\_ERROR\_LOCK\_DENIED 0x80

[ 77](group__bt__csip.md#gac6eda3e7a9a06f86bc715df20e14daa1)#define BT\_CSIP\_ERROR\_LOCK\_RELEASE\_DENIED 0x81

[ 79](group__bt__csip.md#gaeca8a3a9e136882c200c432b9f83203e)#define BT\_CSIP\_ERROR\_LOCK\_INVAL\_VALUE 0x82

[ 81](group__bt__csip.md#ga4e0da5f82ef943e660f669a2962bcc7a)#define BT\_CSIP\_ERROR\_SIRK\_OOB\_ONLY 0x83

[ 83](group__bt__csip.md#gaabd5b74d0e805bfb0b492a45445ec4c4)#define BT\_CSIP\_ERROR\_LOCK\_ALREADY\_GRANTED 0x84

84

[ 93](group__bt__csip.md#ga04fcc2431bec35d53664c8f5ab18100d)#define BT\_CSIP\_DATA\_RSI(\_rsi) BT\_DATA(BT\_DATA\_CSIS\_RSI, \_rsi, BT\_CSIP\_RSI\_SIZE)

94

96struct bt\_csip\_set\_member\_svc\_inst;

97

[ 99](structbt__csip__set__member__cb.md)struct [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md) {

[ 111](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c) void (\*[lock\_changed](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c))(struct bt\_conn \*conn,

112 struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

113 bool locked);

114

[ 128](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[sirk\_read\_req](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9))(struct bt\_conn \*conn,

129 struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

130};

131

[ 133](structbt__csip__set__member__register__param.md)struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) {

[ 139](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_size](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83);

140

[ 147](structbt__csip__set__member__register__param.md#abad0332cc3747749673795d867f8e90f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sirk](structbt__csip__set__member__register__param.md#abad0332cc3747749673795d867f8e90f)[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)];

148

[ 154](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d) bool [lockable](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d);

155

[ 163](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rank](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a);

164

[ 166](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1) struct [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md) \*[cb](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1);

167

168#if CONFIG\_BT\_CSIP\_SET\_MEMBER\_MAX\_INSTANCE\_COUNT > 1 || defined(\_\_DOXYGEN\_\_)

[ 178](structbt__csip__set__member__register__param.md#a7b74ebf8608ba0a9c50d83d414ff15b2) const struct [bt\_gatt\_service](structbt__gatt__service.md) \*[parent](structbt__csip__set__member__register__param.md#a7b74ebf8608ba0a9c50d83d414ff15b2);

179#endif /\* CONFIG\_BT\_CSIP\_SET\_MEMBER\_MAX\_INSTANCE\_COUNT > 1 \*/

180};

181

[ 191](group__bt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c)void \*[bt\_csip\_set\_member\_svc\_decl\_get](group__bt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c)(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

192

[ 208](group__bt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)int [bt\_csip\_set\_member\_register](group__bt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)(const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param,

209 struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst);

210

[ 220](group__bt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)int [bt\_csip\_set\_member\_unregister](group__bt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

221

[ 228](group__bt__csip.md#gae07b5073f1dd3381195e3827e6a803f0)int [bt\_csip\_set\_member\_sirk](group__bt__csip.md#gae07b5073f1dd3381195e3827e6a803f0)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

229 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)]);

230

[ 237](group__bt__csip.md#gab614480b1f96620e74ab55de95b9ef5d)int [bt\_csip\_set\_member\_get\_sirk](group__bt__csip.md#gab614480b1f96620e74ab55de95b9ef5d)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

238 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)]);

239

[ 250](group__bt__csip.md#ga8c59233f7e4c8716042c20e25f42a474)int [bt\_csip\_set\_member\_generate\_rsi](group__bt__csip.md#ga8c59233f7e4c8716042c20e25f42a474)(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

251 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsi[[BT\_CSIP\_RSI\_SIZE](group__bt__csip.md#ga5b0149fec5d38e7003593c227b561506)]);

252

[ 264](group__bt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606)int [bt\_csip\_set\_member\_lock](group__bt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

265 bool lock, bool force);

266

[ 268](structbt__csip__set__coordinator__set__info.md)struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) {

[ 275](structbt__csip__set__coordinator__set__info.md#a50caa7b3a231e6944c807f7653edce3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sirk](structbt__csip__set__coordinator__set__info.md#a50caa7b3a231e6944c807f7653edce3c)[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)];

276

[ 282](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_size](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9);

283

[ 289](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rank](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c);

290

[ 292](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2) bool [lockable](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2);

293};

294

[ 301](structbt__csip__set__coordinator__csis__inst.md)struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) {

[ 303](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d) struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) [info](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d);

304

[ 306](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f) void \*[svc\_inst](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f);

307};

308

[ 310](structbt__csip__set__coordinator__set__member.md)struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) {

[ 312](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8) struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) [insts](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8)[[BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES](group__bt__csip.md#ga42702049524f7ce24dfb6061120414df)];

313};

314

[ 324](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c)typedef void (\*[bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c))(

325 struct bt\_conn \*conn,

326 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member,

327 int err, size\_t set\_count);

328

[ 337](group__bt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73)int [bt\_csip\_set\_coordinator\_discover](group__bt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73)(struct bt\_conn \*conn);

338

351struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*

[ 352](group__bt__csip.md#ga8c3666d8f20f909dd4fa2010ae02c9a5)[bt\_csip\_set\_coordinator\_set\_member\_by\_conn](group__bt__csip.md#ga8c3666d8f20f909dd4fa2010ae02c9a5)(const struct bt\_conn \*conn);

353

[ 360](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634)typedef void (\*[bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634))(int err);

361

[ 372](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b)typedef void (\*[bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b))(

373 struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst, bool locked);

374

[ 382](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2)typedef void (\*[bt\_csip\_set\_coordinator\_sirk\_changed\_cb](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2))(

383 struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst);

384

[ 399](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb)typedef void (\*[bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb))(

400 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

401 int err, bool locked,

402 struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member);

403

[ 409](structbt__csip__set__coordinator__cb.md)struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) {

[ 411](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0) [bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c) [discover](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0);

[ 413](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba) [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) [lock\_set](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba);

[ 415](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de) [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) [release\_set](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de);

[ 417](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1) [bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b) [lock\_changed](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1);

[ 419](structbt__csip__set__coordinator__cb.md#a5bb08e8ce5759f67d2ff02459efe114d) [bt\_csip\_set\_coordinator\_sirk\_changed\_cb](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2) [sirk\_changed](structbt__csip__set__coordinator__cb.md#a5bb08e8ce5759f67d2ff02459efe114d);

[ 421](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c) [bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb) [ordered\_access](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c);

422

425 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

427};

428

[ 437](group__bt__csip.md#gac2a5c323d472c58a7d0cc6060782133e)bool [bt\_csip\_set\_coordinator\_is\_set\_member](group__bt__csip.md#gac2a5c323d472c58a7d0cc6060782133e)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)],

438 struct [bt\_data](structbt__data.md) \*data);

439

[ 447](group__bt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37)int [bt\_csip\_set\_coordinator\_register\_cb](group__bt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37)(struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) \*cb);

448

[ 460](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9))(

461 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

462 struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[],

463 size\_t count);

464

[ 488](group__bt__csip.md#gacd83494562a62fbdbc7282107d4454b4)int [bt\_csip\_set\_coordinator\_ordered\_access](group__bt__csip.md#gacd83494562a62fbdbc7282107d4454b4)(

489 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[],

490 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

491 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

492 [bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9) cb);

493

[ 510](group__bt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)int [bt\_csip\_set\_coordinator\_lock](group__bt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)(const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members,

511 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

512 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info);

513

[ 528](group__bt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)int [bt\_csip\_set\_coordinator\_release](group__bt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)(const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members,

529 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

530 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info);

531

532#ifdef \_\_cplusplus

533}

534#endif

535

539

540#endif /\* ZEPHYR\_SUBSYS\_BLUETOOTH\_AUDIO\_CSIP\_H\_ \*/

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

**Definition** csip.h:399

[bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9)

bool(\* bt\_csip\_set\_coordinator\_ordered\_access\_t)(const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info, struct bt\_csip\_set\_coordinator\_set\_member \*members[], size\_t count)

Callback function definition for bt\_csip\_set\_coordinator\_ordered\_access().

**Definition** csip.h:460

[bt\_csip\_set\_coordinator\_lock](group__bt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)

int bt\_csip\_set\_coordinator\_lock(const struct bt\_csip\_set\_coordinator\_set\_member \*\*members, uint8\_t count, const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info)

Lock an array of set members.

[BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)

#define BT\_CSIP\_SIRK\_SIZE

Size of the Set Identification Resolving Key (SIRK).

**Definition** csip.h:68

[BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES](group__bt__csip.md#ga42702049524f7ce24dfb6061120414df)

#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES

Defines the maximum number of Coordinated Set Identification service instances for the Coordinated Se...

**Definition** csip.h:55

[bt\_csip\_set\_coordinator\_release](group__bt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)

int bt\_csip\_set\_coordinator\_release(const struct bt\_csip\_set\_coordinator\_set\_member \*\*members, uint8\_t count, const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info)

Release an array of set members.

[BT\_CSIP\_RSI\_SIZE](group__bt__csip.md#ga5b0149fec5d38e7003593c227b561506)

#define BT\_CSIP\_RSI\_SIZE

Size of the Resolvable Set Identifier (RSI).

**Definition** csip.h:71

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

**Definition** csip.h:372

[bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634)

void(\* bt\_csip\_set\_coordinator\_lock\_set\_cb)(int err)

Callback for locking a set across one or more devices.

**Definition** csip.h:360

[bt\_csip\_set\_member\_unregister](group__bt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)

int bt\_csip\_set\_member\_unregister(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Unregister a Coordinated Set Identification Service instance.

[bt\_csip\_set\_member\_register](group__bt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)

int bt\_csip\_set\_member\_register(const struct bt\_csip\_set\_member\_register\_param \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst)

Register a Coordinated Set Identification Service instance.

[bt\_csip\_set\_member\_get\_sirk](group__bt__csip.md#gab614480b1f96620e74ab55de95b9ef5d)

int bt\_csip\_set\_member\_get\_sirk(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, uint8\_t sirk[16])

Get the SIRK of a service instance.

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

**Definition** csip.h:382

[bt\_csip\_set\_member\_sirk](group__bt__csip.md#gae07b5073f1dd3381195e3827e6a803f0)

int bt\_csip\_set\_member\_sirk(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, const uint8\_t sirk[16])

Set the SIRK of a service instance.

[bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c)

void(\* bt\_csip\_set\_coordinator\_discover\_cb)(struct bt\_conn \*conn, const struct bt\_csip\_set\_coordinator\_set\_member \*member, int err, size\_t set\_count)

Callback for discovering Coordinated Set Identification Services.

**Definition** csip.h:324

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

[bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md)

Struct to hold the Coordinated Set Identification Profile Set Coordinator callbacks.

**Definition** csip.h:409

[bt\_csip\_set\_coordinator\_cb::lock\_set](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba)

bt\_csip\_set\_coordinator\_lock\_set\_cb lock\_set

Callback when locking a set has finished.

**Definition** csip.h:413

[bt\_csip\_set\_coordinator\_cb::sirk\_changed](structbt__csip__set__coordinator__cb.md#a5bb08e8ce5759f67d2ff02459efe114d)

bt\_csip\_set\_coordinator\_sirk\_changed\_cb sirk\_changed

Callback when a set's SIRK has changed.

**Definition** csip.h:419

[bt\_csip\_set\_coordinator\_cb::discover](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0)

bt\_csip\_set\_coordinator\_discover\_cb discover

Callback when discovery has finished.

**Definition** csip.h:411

[bt\_csip\_set\_coordinator\_cb::release\_set](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de)

bt\_csip\_set\_coordinator\_lock\_set\_cb release\_set

Callback when unlocking a set has finished.

**Definition** csip.h:415

[bt\_csip\_set\_coordinator\_cb::lock\_changed](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1)

bt\_csip\_set\_coordinator\_lock\_changed\_cb lock\_changed

Callback when a set's lock state has changed.

**Definition** csip.h:417

[bt\_csip\_set\_coordinator\_cb::ordered\_access](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c)

bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t ordered\_access

Callback for the ordered access procedure.

**Definition** csip.h:421

[bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md)

Struct representing a coordinated set instance on a remote device.

**Definition** csip.h:301

[bt\_csip\_set\_coordinator\_csis\_inst::info](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d)

struct bt\_csip\_set\_coordinator\_set\_info info

Information about the coordinated set.

**Definition** csip.h:303

[bt\_csip\_set\_coordinator\_csis\_inst::svc\_inst](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f)

void \* svc\_inst

Internally used pointer value.

**Definition** csip.h:306

[bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md)

Information about a specific set.

**Definition** csip.h:268

[bt\_csip\_set\_coordinator\_set\_info::rank](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c)

uint8\_t rank

The rank of the set on the remote device.

**Definition** csip.h:289

[bt\_csip\_set\_coordinator\_set\_info::sirk](structbt__csip__set__coordinator__set__info.md#a50caa7b3a231e6944c807f7653edce3c)

uint8\_t sirk[16]

The 16 octet set Set Identity Resolving Key (SIRK).

**Definition** csip.h:275

[bt\_csip\_set\_coordinator\_set\_info::lockable](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2)

bool lockable

Whether or not the set can be locked on this device.

**Definition** csip.h:292

[bt\_csip\_set\_coordinator\_set\_info::set\_size](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9)

uint8\_t set\_size

The size of the set.

**Definition** csip.h:282

[bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md)

Struct representing a remote device as a set member.

**Definition** csip.h:310

[bt\_csip\_set\_coordinator\_set\_member::insts](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8)

struct bt\_csip\_set\_coordinator\_csis\_inst insts[0]

Array of Coordinated Set Identification Service instances for the remote device.

**Definition** csip.h:312

[bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md)

Callback structure for the Coordinated Set Identification Service.

**Definition** csip.h:99

[bt\_csip\_set\_member\_cb::sirk\_read\_req](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9)

uint8\_t(\* sirk\_read\_req)(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Request from a peer device to read the sirk.

**Definition** csip.h:128

[bt\_csip\_set\_member\_cb::lock\_changed](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c)

void(\* lock\_changed)(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, bool locked)

Callback whenever the lock changes on the server.

**Definition** csip.h:111

[bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md)

Register structure for Coordinated Set Identification Service.

**Definition** csip.h:133

[bt\_csip\_set\_member\_register\_param::cb](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1)

struct bt\_csip\_set\_member\_cb \* cb

Pointer to the callback structure.

**Definition** csip.h:166

[bt\_csip\_set\_member\_register\_param::parent](structbt__csip__set__member__register__param.md#a7b74ebf8608ba0a9c50d83d414ff15b2)

const struct bt\_gatt\_service \* parent

Parent service pointer.

**Definition** csip.h:178

[bt\_csip\_set\_member\_register\_param::sirk](structbt__csip__set__member__register__param.md#abad0332cc3747749673795d867f8e90f)

uint8\_t sirk[16]

The unique Set Identity Resolving Key (SIRK).

**Definition** csip.h:147

[bt\_csip\_set\_member\_register\_param::lockable](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d)

bool lockable

Boolean to set whether the set is lockable by clients.

**Definition** csip.h:154

[bt\_csip\_set\_member\_register\_param::rank](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a)

uint8\_t rank

Rank of this device in this set.

**Definition** csip.h:163

[bt\_csip\_set\_member\_register\_param::set\_size](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83)

uint8\_t set\_size

Size of the set.

**Definition** csip.h:139

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:456

[bt\_gatt\_service](structbt__gatt__service.md)

GATT Service structure.

**Definition** gatt.h:331

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [csip.h](csip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
