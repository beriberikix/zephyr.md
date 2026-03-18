---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/csip_8h_source.html
original_path: doxygen/html/csip_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

csip.h

[Go to the documentation of this file.](csip_8h.md)

1

6

7#ifndef ZEPHYR\_SUBSYS\_BLUETOOTH\_AUDIO\_CSIP\_H\_

8#define ZEPHYR\_SUBSYS\_BLUETOOTH\_AUDIO\_CSIP\_H\_

9

20

21#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 28](group__bt__gatt__csip.md#ga1633e4caaa03a21da0a5431f5f263076)#define BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE K\_SECONDS(10)

29

30#if defined(CONFIG\_BT\_CSIP\_SET\_COORDINATOR)

31#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES CONFIG\_BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES

32#else

[ 33](group__bt__gatt__csip.md#ga42702049524f7ce24dfb6061120414df)#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES 0

34#endif /\* CONFIG\_BT\_CSIP\_SET\_COORDINATOR \*/

35

[ 37](group__bt__gatt__csip.md#gac2aa2ce09ff4aad8bc423dd5b5643038)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT 0x00

[ 39](group__bt__gatt__csip.md#gae6422e7e38bacc39ed2f8d52efe9d6db)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC 0x01

[ 41](group__bt__gatt__csip.md#ga0175e269097a2b6f8f303ee97527db4a)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT 0x02

[ 43](group__bt__gatt__csip.md#gaa245a416becaaaeb118b440f9ba2431d)#define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY 0x03

44

[ 46](group__bt__gatt__csip.md#ga36281b214afb9aea38161558883edb31)#define BT\_CSIP\_SET\_SIRK\_SIZE 16

47

[ 49](group__bt__gatt__csip.md#ga5b0149fec5d38e7003593c227b561506)#define BT\_CSIP\_RSI\_SIZE 6

50

51/\* Coordinate Set Identification Service Error codes \*/

[ 53](group__bt__gatt__csip.md#ga00f382d9fe9afb55acfd6f758cef6389)#define BT\_CSIP\_ERROR\_LOCK\_DENIED 0x80

[ 55](group__bt__gatt__csip.md#gac6eda3e7a9a06f86bc715df20e14daa1)#define BT\_CSIP\_ERROR\_LOCK\_RELEASE\_DENIED 0x81

[ 57](group__bt__gatt__csip.md#gaeca8a3a9e136882c200c432b9f83203e)#define BT\_CSIP\_ERROR\_LOCK\_INVAL\_VALUE 0x82

[ 59](group__bt__gatt__csip.md#ga4e0da5f82ef943e660f669a2962bcc7a)#define BT\_CSIP\_ERROR\_SIRK\_OOB\_ONLY 0x83

[ 61](group__bt__gatt__csip.md#gaabd5b74d0e805bfb0b492a45445ec4c4)#define BT\_CSIP\_ERROR\_LOCK\_ALREADY\_GRANTED 0x84

62

[ 71](group__bt__gatt__csip.md#ga04fcc2431bec35d53664c8f5ab18100d)#define BT\_CSIP\_DATA\_RSI(\_rsi) BT\_DATA(BT\_DATA\_CSIS\_RSI, \_rsi, BT\_CSIP\_RSI\_SIZE)

72

74struct bt\_csip\_set\_member\_svc\_inst;

75

[ 77](structbt__csip__set__member__cb.md)struct [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md) {

[ 89](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c) void (\*[lock\_changed](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c))(struct bt\_conn \*conn,

90 struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

91 bool locked);

92

[ 106](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[sirk\_read\_req](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9))(struct bt\_conn \*conn,

107 struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

108};

109

[ 111](structbt__csip__set__member__register__param.md)struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) {

[ 117](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_size](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83);

118

[ 125](structbt__csip__set__member__register__param.md#a30e502d6f9c13e0cbf1903755f51c085) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_sirk](structbt__csip__set__member__register__param.md#a30e502d6f9c13e0cbf1903755f51c085)[[BT\_CSIP\_SET\_SIRK\_SIZE](group__bt__gatt__csip.md#ga36281b214afb9aea38161558883edb31)];

126

[ 132](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d) bool [lockable](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d);

133

[ 141](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rank](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a);

142

[ 144](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1) struct [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md) \*[cb](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1);

145

146#if CONFIG\_BT\_CSIP\_SET\_MEMBER\_MAX\_INSTANCE\_COUNT > 1

156 const struct [bt\_gatt\_service](structbt__gatt__service.md) \*parent;

157#endif /\* CONFIG\_BT\_CSIP\_SET\_MEMBER\_MAX\_INSTANCE\_COUNT > 1 \*/

158};

159

[ 169](group__bt__gatt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c)void \*[bt\_csip\_set\_member\_svc\_decl\_get](group__bt__gatt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c)(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

170

[ 186](group__bt__gatt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)int [bt\_csip\_set\_member\_register](group__bt__gatt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)(const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param,

187 struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst);

188

[ 198](group__bt__gatt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)int [bt\_csip\_set\_member\_unregister](group__bt__gatt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

199

[ 205](group__bt__gatt__csip.md#gadf1b8981bf6220d0b0d522330c0f0c85)void [bt\_csip\_set\_member\_print\_sirk](group__bt__gatt__csip.md#gadf1b8981bf6220d0b0d522330c0f0c85)(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst);

206

[ 217](group__bt__gatt__csip.md#ga8c59233f7e4c8716042c20e25f42a474)int [bt\_csip\_set\_member\_generate\_rsi](group__bt__gatt__csip.md#ga8c59233f7e4c8716042c20e25f42a474)(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

218 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsi[[BT\_CSIP\_RSI\_SIZE](group__bt__gatt__csip.md#ga5b0149fec5d38e7003593c227b561506)]);

219

[ 231](group__bt__gatt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606)int [bt\_csip\_set\_member\_lock](group__bt__gatt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606)(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst,

232 bool lock, bool force);

233

[ 235](structbt__csip__set__coordinator__set__info.md)struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) {

[ 242](structbt__csip__set__coordinator__set__info.md#ac20e97e3a8041ff6dfac7c51fb4b1e99) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_sirk](structbt__csip__set__coordinator__set__info.md#ac20e97e3a8041ff6dfac7c51fb4b1e99)[[BT\_CSIP\_SET\_SIRK\_SIZE](group__bt__gatt__csip.md#ga36281b214afb9aea38161558883edb31)];

243

[ 249](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [set\_size](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9);

250

[ 256](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rank](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c);

257

[ 259](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2) bool [lockable](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2);

260};

261

[ 268](structbt__csip__set__coordinator__csis__inst.md)struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) {

[ 269](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d) struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) [info](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d);

270

[ 272](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f) void \*[svc\_inst](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f);

273};

274

[ 276](structbt__csip__set__coordinator__set__member.md)struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) {

[ 278](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8) struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) [insts](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8)[[BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES](group__bt__gatt__csip.md#ga42702049524f7ce24dfb6061120414df)];

279};

280

[ 290](group__bt__gatt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c)typedef void (\*[bt\_csip\_set\_coordinator\_discover\_cb](group__bt__gatt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c))(

291 struct bt\_conn \*conn,

292 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member,

293 int err, size\_t set\_count);

294

[ 303](group__bt__gatt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73)int [bt\_csip\_set\_coordinator\_discover](group__bt__gatt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73)(struct bt\_conn \*conn);

304

[ 311](group__bt__gatt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634)typedef void (\*[bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__gatt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634))(int err);

312

[ 323](group__bt__gatt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b)typedef void (\*[bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__gatt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b))(

324 struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst, bool locked);

325

[ 340](group__bt__gatt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb)typedef void (\*[bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__gatt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb))(

341 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

342 int err, bool locked,

343 struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member);

344

[ 345](structbt__csip__set__coordinator__cb.md)struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) {

346 /\* Set callbacks \*/

[ 347](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba) [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__gatt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) [lock\_set](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba);

[ 348](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de) [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__gatt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) [release\_set](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de);

[ 349](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1) [bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__gatt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b) [lock\_changed](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1);

350

351 /\* Device specific callbacks \*/

[ 352](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0) [bt\_csip\_set\_coordinator\_discover\_cb](group__bt__gatt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c) [discover](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0);

[ 353](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c) [bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__gatt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb) [ordered\_access](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c);

354

356 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

357};

358

[ 367](group__bt__gatt__csip.md#ga327a16ba31841beec6250499a6daa7e8)bool [bt\_csip\_set\_coordinator\_is\_set\_member](group__bt__gatt__csip.md#ga327a16ba31841beec6250499a6daa7e8)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) set\_sirk[[BT\_CSIP\_SET\_SIRK\_SIZE](group__bt__gatt__csip.md#ga36281b214afb9aea38161558883edb31)],

368 struct [bt\_data](structbt__data.md) \*data);

369

[ 377](group__bt__gatt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37)int [bt\_csip\_set\_coordinator\_register\_cb](group__bt__gatt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37)(struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) \*cb);

378

[ 390](group__bt__gatt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__gatt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9))(

391 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

392 struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[],

393 size\_t count);

394

[ 418](group__bt__gatt__csip.md#gacd83494562a62fbdbc7282107d4454b4)int [bt\_csip\_set\_coordinator\_ordered\_access](group__bt__gatt__csip.md#gacd83494562a62fbdbc7282107d4454b4)(

419 const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[],

420 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

421 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info,

422 [bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__gatt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9) cb);

423

[ 438](group__bt__gatt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)int [bt\_csip\_set\_coordinator\_lock](group__bt__gatt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)(const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members,

439 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

440 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info);

441

[ 454](group__bt__gatt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)int [bt\_csip\_set\_coordinator\_release](group__bt__gatt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)(const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members,

455 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count,

456 const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info);

457

458

459#ifdef \_\_cplusplus

460}

461#endif

462

466

467#endif /\* ZEPHYR\_SUBSYS\_BLUETOOTH\_AUDIO\_CSIP\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_csip\_set\_coordinator\_register\_cb](group__bt__gatt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37)

int bt\_csip\_set\_coordinator\_register\_cb(struct bt\_csip\_set\_coordinator\_cb \*cb)

Registers callbacks for csip\_set\_coordinator.

[bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__gatt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb)

void(\* bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t)(const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info, int err, bool locked, struct bt\_csip\_set\_coordinator\_set\_member \*member)

Callback for bt\_csip\_set\_coordinator\_ordered\_access().

**Definition** csip.h:340

[bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__gatt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9)

bool(\* bt\_csip\_set\_coordinator\_ordered\_access\_t)(const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info, struct bt\_csip\_set\_coordinator\_set\_member \*members[], size\_t count)

Callback function definition for bt\_csip\_set\_coordinator\_ordered\_access().

**Definition** csip.h:390

[bt\_csip\_set\_coordinator\_lock](group__bt__gatt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa)

int bt\_csip\_set\_coordinator\_lock(const struct bt\_csip\_set\_coordinator\_set\_member \*\*members, uint8\_t count, const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info)

Lock an array of set members.

[bt\_csip\_set\_coordinator\_is\_set\_member](group__bt__gatt__csip.md#ga327a16ba31841beec6250499a6daa7e8)

bool bt\_csip\_set\_coordinator\_is\_set\_member(const uint8\_t set\_sirk[16], struct bt\_data \*data)

Check if advertising data indicates a set member.

[BT\_CSIP\_SET\_SIRK\_SIZE](group__bt__gatt__csip.md#ga36281b214afb9aea38161558883edb31)

#define BT\_CSIP\_SET\_SIRK\_SIZE

Size of the Set Identification Resolving Key (SIRK).

**Definition** csip.h:46

[BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES](group__bt__gatt__csip.md#ga42702049524f7ce24dfb6061120414df)

#define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES

**Definition** csip.h:33

[bt\_csip\_set\_coordinator\_release](group__bt__gatt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45)

int bt\_csip\_set\_coordinator\_release(const struct bt\_csip\_set\_coordinator\_set\_member \*\*members, uint8\_t count, const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info)

Release an array of set members.

[BT\_CSIP\_RSI\_SIZE](group__bt__gatt__csip.md#ga5b0149fec5d38e7003593c227b561506)

#define BT\_CSIP\_RSI\_SIZE

Size of the Resolvable Set Identifier (RSI).

**Definition** csip.h:49

[bt\_csip\_set\_coordinator\_discover](group__bt__gatt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73)

int bt\_csip\_set\_coordinator\_discover(struct bt\_conn \*conn)

Initialise the csip\_set\_coordinator instance for a connection.

[bt\_csip\_set\_member\_generate\_rsi](group__bt__gatt__csip.md#ga8c59233f7e4c8716042c20e25f42a474)

int bt\_csip\_set\_member\_generate\_rsi(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, uint8\_t rsi[6])

Generate the Resolvable Set Identifier (RSI) value.

[bt\_csip\_set\_member\_lock](group__bt__gatt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606)

int bt\_csip\_set\_member\_lock(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, bool lock, bool force)

Locks a specific Coordinated Set Identification Service instance on the server.

[bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__gatt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b)

void(\* bt\_csip\_set\_coordinator\_lock\_changed\_cb)(struct bt\_csip\_set\_coordinator\_csis\_inst \*inst, bool locked)

Callback when the lock value on a set of a connected device changes.

**Definition** csip.h:323

[bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__gatt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634)

void(\* bt\_csip\_set\_coordinator\_lock\_set\_cb)(int err)

Callback for locking a set across one or more devices.

**Definition** csip.h:311

[bt\_csip\_set\_member\_unregister](group__bt__gatt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1)

int bt\_csip\_set\_member\_unregister(struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Unregister a Coordinated Set Identification Service instance.

[bt\_csip\_set\_member\_register](group__bt__gatt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac)

int bt\_csip\_set\_member\_register(const struct bt\_csip\_set\_member\_register\_param \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst)

Register a Coordinated Set Identification Service instance.

[bt\_csip\_set\_member\_svc\_decl\_get](group__bt__gatt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c)

void \* bt\_csip\_set\_member\_svc\_decl\_get(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Get the service declaration attribute.

[bt\_csip\_set\_coordinator\_ordered\_access](group__bt__gatt__csip.md#gacd83494562a62fbdbc7282107d4454b4)

int bt\_csip\_set\_coordinator\_ordered\_access(const struct bt\_csip\_set\_coordinator\_set\_member \*members[], uint8\_t count, const struct bt\_csip\_set\_coordinator\_set\_info \*set\_info, bt\_csip\_set\_coordinator\_ordered\_access\_t cb)

Access Coordinated Set devices in an ordered manner as a client.

[bt\_csip\_set\_member\_print\_sirk](group__bt__gatt__csip.md#gadf1b8981bf6220d0b0d522330c0f0c85)

void bt\_csip\_set\_member\_print\_sirk(const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Print the SIRK to the debug output.

[bt\_csip\_set\_coordinator\_discover\_cb](group__bt__gatt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c)

void(\* bt\_csip\_set\_coordinator\_discover\_cb)(struct bt\_conn \*conn, const struct bt\_csip\_set\_coordinator\_set\_member \*member, int err, size\_t set\_count)

Callback for discovering Coordinated Set Identification Services.

**Definition** csip.h:290

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md)

**Definition** csip.h:345

[bt\_csip\_set\_coordinator\_cb::lock\_set](structbt__csip__set__coordinator__cb.md#a25474d60bcd8ee07ef3691554d9bd7ba)

bt\_csip\_set\_coordinator\_lock\_set\_cb lock\_set

**Definition** csip.h:347

[bt\_csip\_set\_coordinator\_cb::discover](structbt__csip__set__coordinator__cb.md#a724060375ef6f53fcdbabcc12032a4b0)

bt\_csip\_set\_coordinator\_discover\_cb discover

**Definition** csip.h:352

[bt\_csip\_set\_coordinator\_cb::release\_set](structbt__csip__set__coordinator__cb.md#acc1efc493dd05f14fdc010240982e0de)

bt\_csip\_set\_coordinator\_lock\_set\_cb release\_set

**Definition** csip.h:348

[bt\_csip\_set\_coordinator\_cb::lock\_changed](structbt__csip__set__coordinator__cb.md#adfa831556d13dbda8f06f69f69f9cac1)

bt\_csip\_set\_coordinator\_lock\_changed\_cb lock\_changed

**Definition** csip.h:349

[bt\_csip\_set\_coordinator\_cb::ordered\_access](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c)

bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t ordered\_access

**Definition** csip.h:353

[bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md)

Struct representing a coordinated set instance on a remote device.

**Definition** csip.h:268

[bt\_csip\_set\_coordinator\_csis\_inst::info](structbt__csip__set__coordinator__csis__inst.md#a0c407932ad1fb5e36cd19daf28bac96d)

struct bt\_csip\_set\_coordinator\_set\_info info

**Definition** csip.h:269

[bt\_csip\_set\_coordinator\_csis\_inst::svc\_inst](structbt__csip__set__coordinator__csis__inst.md#a7e7210dded5a084c5d45f9209895e37f)

void \* svc\_inst

Internally used pointer value.

**Definition** csip.h:272

[bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md)

Information about a specific set.

**Definition** csip.h:235

[bt\_csip\_set\_coordinator\_set\_info::rank](structbt__csip__set__coordinator__set__info.md#a362fd6d8afbde9eb77d4f9a47aecb03c)

uint8\_t rank

The rank of the set on on the remote device.

**Definition** csip.h:256

[bt\_csip\_set\_coordinator\_set\_info::lockable](structbt__csip__set__coordinator__set__info.md#aa85b6a24ea8f020bb1312065e461c4b2)

bool lockable

Whether or not the set can be locked on this device.

**Definition** csip.h:259

[bt\_csip\_set\_coordinator\_set\_info::set\_sirk](structbt__csip__set__coordinator__set__info.md#ac20e97e3a8041ff6dfac7c51fb4b1e99)

uint8\_t set\_sirk[16]

The 16 octet set Set Identity Resolving Key (SIRK).

**Definition** csip.h:242

[bt\_csip\_set\_coordinator\_set\_info::set\_size](structbt__csip__set__coordinator__set__info.md#ac969998670d04d6dea96ea6f666f3fc9)

uint8\_t set\_size

The size of the set.

**Definition** csip.h:249

[bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md)

Struct representing a remote device as a set member.

**Definition** csip.h:276

[bt\_csip\_set\_coordinator\_set\_member::insts](structbt__csip__set__coordinator__set__member.md#a8527f8a3ab6966c9de155d0e10c0b7e8)

struct bt\_csip\_set\_coordinator\_csis\_inst insts[0]

Array of Coordinated Set Identification Service instances for the remote device.

**Definition** csip.h:278

[bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md)

Callback structure for the Coordinated Set Identification Service.

**Definition** csip.h:77

[bt\_csip\_set\_member\_cb::sirk\_read\_req](structbt__csip__set__member__cb.md#a30b2f68aff4b75ffcc8e9d7e2de2afd9)

uint8\_t(\* sirk\_read\_req)(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst)

Request from a peer device to read the sirk.

**Definition** csip.h:106

[bt\_csip\_set\_member\_cb::lock\_changed](structbt__csip__set__member__cb.md#a46e18120caf78788f0928ada2c92ca5c)

void(\* lock\_changed)(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, bool locked)

Callback whenever the lock changes on the server.

**Definition** csip.h:89

[bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md)

Register structure for Coordinated Set Identification Service.

**Definition** csip.h:111

[bt\_csip\_set\_member\_register\_param::cb](structbt__csip__set__member__register__param.md#a1878a8d50ab190920435aaef611b69f1)

struct bt\_csip\_set\_member\_cb \* cb

Pointer to the callback structure.

**Definition** csip.h:144

[bt\_csip\_set\_member\_register\_param::set\_sirk](structbt__csip__set__member__register__param.md#a30e502d6f9c13e0cbf1903755f51c085)

uint8\_t set\_sirk[16]

The unique Set Identity Resolving Key (SIRK).

**Definition** csip.h:125

[bt\_csip\_set\_member\_register\_param::lockable](structbt__csip__set__member__register__param.md#abc87df6590e3c55a2cd860f86398346d)

bool lockable

Boolean to set whether the set is lockable by clients.

**Definition** csip.h:132

[bt\_csip\_set\_member\_register\_param::rank](structbt__csip__set__member__register__param.md#af38436c47f52ec285cadb5d23c67ea0a)

uint8\_t rank

Rank of this device in this set.

**Definition** csip.h:141

[bt\_csip\_set\_member\_register\_param::set\_size](structbt__csip__set__member__register__param.md#af8814b6e0695001e0a70025f5c2b4e83)

uint8\_t set\_size

Size of the set.

**Definition** csip.h:117

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:439

[bt\_gatt\_service](structbt__gatt__service.md)

GATT Service structure.

**Definition** gatt.h:195

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [csip.h](csip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
