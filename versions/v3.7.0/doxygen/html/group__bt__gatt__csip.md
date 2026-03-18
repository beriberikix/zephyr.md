---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__gatt__csip.html
original_path: doxygen/html/group__bt__gatt__csip.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Coordinated Set Identification Profile (CSIP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Coordinated Set Identification Profile (CSIP).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md) |
|  | Callback structure for the Coordinated Set Identification Service. [More...](structbt__csip__set__member__cb.md#details) |
| struct | [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) |
|  | Register structure for Coordinated Set Identification Service. [More...](structbt__csip__set__member__register__param.md#details) |
| struct | [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) |
|  | Information about a specific set. [More...](structbt__csip__set__coordinator__set__info.md#details) |
| struct | [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) |
|  | Struct representing a coordinated set instance on a remote device. [More...](structbt__csip__set__coordinator__csis__inst.md#details) |
| struct | [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) |
|  | Struct representing a remote device as a set member. [More...](structbt__csip__set__coordinator__set__member.md#details) |
| struct | [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) |
|  | Struct to hold the Coordinated Set Identification Profile Set Coordinator callbacks. [More...](structbt__csip__set__coordinator__cb.md#details) |
| struct | [bt\_pacs\_cap](structbt__pacs__cap.md) |
|  | Published Audio Capability structure. [More...](structbt__pacs__cap.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE](#ga1633e4caaa03a21da0a5431f5f263076)   [K\_SECONDS](group__clock__apis.md#gadc361472aea59267f6ea38f5e7c7ca2a)(10) |
|  | Recommended timer for member discovery. |
| #define | [BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES](#ga42702049524f7ce24dfb6061120414df)   0 |
|  | Defines the maximum number of Coordinated Set Identification service instances for the Coordinated Set Identification Set Coordinator. |
| #define | [BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT](#gac2aa2ce09ff4aad8bc423dd5b5643038)   0x00 |
|  | Accept the request to read the SIRK as plaintext. |
| #define | [BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC](#gae6422e7e38bacc39ed2f8d52efe9d6db)   0x01 |
|  | Accept the request to read the SIRK, but return encrypted SIRK. |
| #define | [BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT](#ga0175e269097a2b6f8f303ee97527db4a)   0x02 |
|  | Reject the request to read the SIRK. |
| #define | [BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY](#gaa245a416becaaaeb118b440f9ba2431d)   0x03 |
|  | SIRK is available only via an OOB procedure. |
| #define | [BT\_CSIP\_SIRK\_SIZE](#ga33069821c84e9b4c16c9d95d88c23158)   16 |
|  | Size of the Set Identification Resolving Key (SIRK). |
| #define | [BT\_CSIP\_RSI\_SIZE](#ga5b0149fec5d38e7003593c227b561506)   6 |
|  | Size of the Resolvable Set Identifier (RSI). |
| #define | [BT\_CSIP\_ERROR\_LOCK\_DENIED](#ga00f382d9fe9afb55acfd6f758cef6389)   0x80 |
|  | Service is already locked. |
| #define | [BT\_CSIP\_ERROR\_LOCK\_RELEASE\_DENIED](#gac6eda3e7a9a06f86bc715df20e14daa1)   0x81 |
|  | Service is not locked. |
| #define | [BT\_CSIP\_ERROR\_LOCK\_INVAL\_VALUE](#gaeca8a3a9e136882c200c432b9f83203e)   0x82 |
|  | Invalid lock value. |
| #define | [BT\_CSIP\_ERROR\_SIRK\_OOB\_ONLY](#ga4e0da5f82ef943e660f669a2962bcc7a)   0x83 |
|  | SIRK only available out-of-band. |
| #define | [BT\_CSIP\_ERROR\_LOCK\_ALREADY\_GRANTED](#gaabd5b74d0e805bfb0b492a45445ec4c4)   0x84 |
|  | Client is already owner of the lock. |
| #define | [BT\_CSIP\_DATA\_RSI](#ga04fcc2431bec35d53664c8f5ab18100d)(\_rsi) |
|  | Helper to declare [bt\_data](structbt__data.md "Bluetooth data.") array including RSI. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_csip\_set\_coordinator\_discover\_cb](#gaeee5f0691ba0d63a370ac5dd94cb4d5c)) (struct bt\_conn \*conn, const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member, int err, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) set\_count) |
|  | Callback for discovering Coordinated Set Identification Services. |
| typedef void(\* | [bt\_csip\_set\_coordinator\_lock\_set\_cb](#ga994431ea69920d9e84f35ca6e1e5f634)) (int err) |
|  | Callback for locking a set across one or more devices. |
| typedef void(\* | [bt\_csip\_set\_coordinator\_lock\_changed\_cb](#ga991ee886c814e0b72fa12ed58ef4a90b)) (struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) locked) |
|  | Callback when the lock value on a set of a connected device changes. |
| typedef void(\* | [bt\_csip\_set\_coordinator\_sirk\_changed\_cb](#gacdb98c9ae3248064e90352387df7cef2)) (struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst) |
|  | Callback when the SIRK value of a set of a connected device changes. |
| typedef void(\* | [bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](#ga0f2e0b610a4db975a72c6d9a645964cb)) (const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info, int err, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) locked, struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member) |
|  | Callback for [bt\_csip\_set\_coordinator\_ordered\_access()](#gacd83494562a62fbdbc7282107d4454b4). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_csip\_set\_coordinator\_ordered\_access\_t](#ga2ce69e3bf51622fd41389a12d26e2ba9)) (const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info, struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Callback function definition for [bt\_csip\_set\_coordinator\_ordered\_access()](#gacd83494562a62fbdbc7282107d4454b4). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_pacs\_cap\_foreach\_func\_t](#ga452591f80b6be5d79609b25ade2154a9)) (const struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap, void \*user\_data) |
|  | Published Audio Capability iterator callback. |

| Functions | |
| --- | --- |
| void \* | [bt\_csip\_set\_member\_svc\_decl\_get](#gabc8d9c8d2b2f73f5e18e7fdbce95389c) (const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst) |
|  | Get the service declaration attribute. |
| int | [bt\_csip\_set\_member\_register](#gab11184ace9246d4c5ead6bdc98ffa2ac) (const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst) |
|  | Register a Coordinated Set Identification Service instance. |
| int | [bt\_csip\_set\_member\_unregister](#ga9ee48e36fb33ee27e689d32f08f071a1) (struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst) |
|  | Unregister a Coordinated Set Identification Service instance. |
| int | [bt\_csip\_set\_member\_sirk](#gae07b5073f1dd3381195e3827e6a803f0) (struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[16]) |
|  | Set the SIRK of a service instance. |
| int | [bt\_csip\_set\_member\_get\_sirk](#gab614480b1f96620e74ab55de95b9ef5d) (struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[16]) |
|  | Get the SIRK of a service instance. |
| int | [bt\_csip\_set\_member\_generate\_rsi](#ga8c59233f7e4c8716042c20e25f42a474) (const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsi[6]) |
|  | Generate the Resolvable Set Identifier (RSI) value. |
| int | [bt\_csip\_set\_member\_lock](#ga95e2ba4b65ec42eedb26bf5ad181b606) (struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lock, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) force) |
|  | Locks a specific Coordinated Set Identification Service instance on the server. |
| int | [bt\_csip\_set\_coordinator\_discover](#ga7e7ea4a92bb76aded86807571a2cbb73) (struct bt\_conn \*conn) |
|  | Initialise the csip\_set\_coordinator instance for a connection. |
| struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \* | [bt\_csip\_set\_coordinator\_set\_member\_by\_conn](#ga8c3666d8f20f909dd4fa2010ae02c9a5) (const struct bt\_conn \*conn) |
|  | Get the set member from a connection pointer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_csip\_set\_coordinator\_is\_set\_member](#gac2a5c323d472c58a7d0cc6060782133e) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[16], struct [bt\_data](structbt__data.md) \*data) |
|  | Check if advertising data indicates a set member. |
| int | [bt\_csip\_set\_coordinator\_register\_cb](#ga08c514fda44e5a9b5cfc16be629c2b37) (struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) \*cb) |
|  | Registers callbacks for csip\_set\_coordinator. |
| int | [bt\_csip\_set\_coordinator\_ordered\_access](#gacd83494562a62fbdbc7282107d4454b4) (const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info, [bt\_csip\_set\_coordinator\_ordered\_access\_t](#ga2ce69e3bf51622fd41389a12d26e2ba9) cb) |
|  | Access Coordinated Set devices in an ordered manner as a client. |
| int | [bt\_csip\_set\_coordinator\_lock](#ga2d61e25d131631479e34a2c2edf3ebfa) (const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info) |
|  | Lock an array of set members. |
| int | [bt\_csip\_set\_coordinator\_release](#ga5391b625fbcfd66ab07e014659dc2e45) (const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info) |
|  | Release an array of set members. |
| void | [bt\_pacs\_cap\_foreach](#ga31e2c7e9a4b5b6a291b96832c1218a49) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, [bt\_pacs\_cap\_foreach\_func\_t](#ga452591f80b6be5d79609b25ade2154a9) func, void \*user\_data) |
|  | Published Audio Capability iterator. |
| int | [bt\_pacs\_cap\_register](#ga251b36d4f5775eea1f69873709f847cc) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap) |
|  | Register Published Audio Capability. |
| int | [bt\_pacs\_cap\_unregister](#ga4f6015eba63ffc7a9377afe54a290da1) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap) |
|  | Unregister Published Audio Capability. |
| int | [bt\_pacs\_set\_location](#gaff290fd59bb05012abcf405dbdc72884) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) location) |
|  | Set the location for an endpoint type. |
| int | [bt\_pacs\_set\_available\_contexts](#ga29a1ec26c1e5e82e02eac39e1088332c) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts) |
|  | Set the available contexts for an endpoint type. |
| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | [bt\_pacs\_get\_available\_contexts](#ga437d824d0a944b6c30db492dbe28514f) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Get the available contexts for an endpoint type. |
| int | [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](#ga12f283d2daf72302a01cefb4a4a8fc70) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) \*contexts) |
|  | Set the available contexts for a given connection. |
| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | [bt\_pacs\_get\_available\_contexts\_for\_conn](#ga7b28aa42525344445b20bb90a19441aa) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Get the available contexts for a given connection. |
| int | [bt\_pacs\_set\_supported\_contexts](#gabae9cf025f32ce80b660ebd7f95241b2) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts) |
|  | Set the supported contexts for an endpoint type. |

## Detailed Description

Coordinated Set Identification Profile (CSIP).

Published Audio Capabilities Service (PACS).

Since
:   3.0

Version
:   0.8.0

The Coordinated Set Identification Profile (CSIP) provides procedures to discover and coordinate sets of devices.

Since
:   3.0

Version
:   0.8.0

The Published Audio Capabilities Service (PACS) is used to expose capabilities to remote devices.

## Macro Definition Documentation

## [◆ ](#ga04fcc2431bec35d53664c8f5ab18100d)BT\_CSIP\_DATA\_RSI

| #define BT\_CSIP\_DATA\_RSI | ( |  | *\_rsi* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[csip.h](csip_8h.md)>`

**Value:**

[BT\_DATA](group__bt__gap.md#ga8481217e632522e1f322de87d745f8f0)([BT\_DATA\_CSIS\_RSI](group__bt__gap__defines.md#ga122da4184d606ae140f8a311aaebeedd), \_rsi, [BT\_CSIP\_RSI\_SIZE](#ga5b0149fec5d38e7003593c227b561506))

[BT\_DATA\_CSIS\_RSI](group__bt__gap__defines.md#ga122da4184d606ae140f8a311aaebeedd)

#define BT\_DATA\_CSIS\_RSI

CSIS Random Set ID type.

**Definition** gap.h:80

[BT\_DATA](group__bt__gap.md#ga8481217e632522e1f322de87d745f8f0)

#define BT\_DATA(\_type, \_data, \_data\_len)

Helper to declare elements of bt\_data arrays.

**Definition** bluetooth.h:470

[BT\_CSIP\_RSI\_SIZE](#ga5b0149fec5d38e7003593c227b561506)

#define BT\_CSIP\_RSI\_SIZE

Size of the Resolvable Set Identifier (RSI).

**Definition** csip.h:71

Helper to declare [bt\_data](structbt__data.md "Bluetooth data.") array including RSI.

This macro is mainly for creating an array of struct [bt\_data](structbt__data.md "Bluetooth data.") elements which is then passed to e.g. [bt\_le\_ext\_adv\_start()](group__bt__gap.md#gaf0f436c55482d9429f674303ae3aa815 "bt_le_ext_adv_start()").

Parameters
:   | \_rsi | Pointer to the RSI value |
    | --- | --- |

## [◆ ](#gaabd5b74d0e805bfb0b492a45445ec4c4)BT\_CSIP\_ERROR\_LOCK\_ALREADY\_GRANTED

| #define BT\_CSIP\_ERROR\_LOCK\_ALREADY\_GRANTED   0x84 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Client is already owner of the lock.

## [◆ ](#ga00f382d9fe9afb55acfd6f758cef6389)BT\_CSIP\_ERROR\_LOCK\_DENIED

| #define BT\_CSIP\_ERROR\_LOCK\_DENIED   0x80 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Service is already locked.

## [◆ ](#gaeca8a3a9e136882c200c432b9f83203e)BT\_CSIP\_ERROR\_LOCK\_INVAL\_VALUE

| #define BT\_CSIP\_ERROR\_LOCK\_INVAL\_VALUE   0x82 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Invalid lock value.

## [◆ ](#gac6eda3e7a9a06f86bc715df20e14daa1)BT\_CSIP\_ERROR\_LOCK\_RELEASE\_DENIED

| #define BT\_CSIP\_ERROR\_LOCK\_RELEASE\_DENIED   0x81 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Service is not locked.

## [◆ ](#ga4e0da5f82ef943e660f669a2962bcc7a)BT\_CSIP\_ERROR\_SIRK\_OOB\_ONLY

| #define BT\_CSIP\_ERROR\_SIRK\_OOB\_ONLY   0x83 |
| --- |

`#include <[csip.h](csip_8h.md)>`

SIRK only available out-of-band.

## [◆ ](#gac2aa2ce09ff4aad8bc423dd5b5643038)BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT

| #define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT   0x00 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Accept the request to read the SIRK as plaintext.

## [◆ ](#gae6422e7e38bacc39ed2f8d52efe9d6db)BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC

| #define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC   0x01 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Accept the request to read the SIRK, but return encrypted SIRK.

## [◆ ](#gaa245a416becaaaeb118b440f9ba2431d)BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY

| #define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY   0x03 |
| --- |

`#include <[csip.h](csip_8h.md)>`

SIRK is available only via an OOB procedure.

## [◆ ](#ga0175e269097a2b6f8f303ee97527db4a)BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT

| #define BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT   0x02 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Reject the request to read the SIRK.

## [◆ ](#ga5b0149fec5d38e7003593c227b561506)BT\_CSIP\_RSI\_SIZE

| #define BT\_CSIP\_RSI\_SIZE   6 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Size of the Resolvable Set Identifier (RSI).

## [◆ ](#ga1633e4caaa03a21da0a5431f5f263076)BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE

| #define BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE   [K\_SECONDS](group__clock__apis.md#gadc361472aea59267f6ea38f5e7c7ca2a)(10) |
| --- |

`#include <[csip.h](csip_8h.md)>`

Recommended timer for member discovery.

## [◆ ](#ga42702049524f7ce24dfb6061120414df)BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES

| #define BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES   0 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Defines the maximum number of Coordinated Set Identification service instances for the Coordinated Set Identification Set Coordinator.

## [◆ ](#ga33069821c84e9b4c16c9d95d88c23158)BT\_CSIP\_SIRK\_SIZE

| #define BT\_CSIP\_SIRK\_SIZE   16 |
| --- |

`#include <[csip.h](csip_8h.md)>`

Size of the Set Identification Resolving Key (SIRK).

## Typedef Documentation

## [◆ ](#gaeee5f0691ba0d63a370ac5dd94cb4d5c)bt\_csip\_set\_coordinator\_discover\_cb

| typedef void(\* bt\_csip\_set\_coordinator\_discover\_cb) (struct bt\_conn \*conn, const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member, int err, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) set\_count) |
| --- |

`#include <[csip.h](csip_8h.md)>`

Callback for discovering Coordinated Set Identification Services.

Parameters
:   | conn | Pointer to the remote device. |
    | --- | --- |
    | member | Pointer to the set member. |
    | err | 0 on success, or an errno value on error. |
    | set\_count | Number of sets on the member. |

## [◆ ](#ga991ee886c814e0b72fa12ed58ef4a90b)bt\_csip\_set\_coordinator\_lock\_changed\_cb

| typedef void(\* bt\_csip\_set\_coordinator\_lock\_changed\_cb) (struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) locked) |
| --- |

`#include <[csip.h](csip_8h.md)>`

Callback when the lock value on a set of a connected device changes.

Parameters
:   | inst | The Coordinated Set Identification Service instance that was changed. |
    | --- | --- |
    | locked | Whether the lock is locked or release. |

Returns
:   int Return 0 on success, or an errno value on error.

## [◆ ](#ga994431ea69920d9e84f35ca6e1e5f634)bt\_csip\_set\_coordinator\_lock\_set\_cb

| typedef void(\* bt\_csip\_set\_coordinator\_lock\_set\_cb) (int err) |
| --- |

`#include <[csip.h](csip_8h.md)>`

Callback for locking a set across one or more devices.

Parameters
:   | err | 0 on success, or an errno value on error. |
    | --- | --- |

## [◆ ](#ga0f2e0b610a4db975a72c6d9a645964cb)bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t

| typedef void(\* bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t) (const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info, int err, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) locked, struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member) |
| --- |

`#include <[csip.h](csip_8h.md)>`

Callback for [bt\_csip\_set\_coordinator\_ordered\_access()](#gacd83494562a62fbdbc7282107d4454b4).

If any of the set members supplied to [bt\_csip\_set\_coordinator\_ordered\_access()](#gacd83494562a62fbdbc7282107d4454b4) is in the locked state, this will be called with `locked` true and `member` will be the locked member, and the ordered access procedure is cancelled. Likewise, if any error occurs, the procedure will also be aborted.

Parameters
:   | set\_info | Pointer to the a specific set\_info struct. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail. |
    | locked | Whether the lock is locked or release. |
    | member | The locked member if `locked` is true, otherwise NULL. |

## [◆ ](#ga2ce69e3bf51622fd41389a12d26e2ba9)bt\_csip\_set\_coordinator\_ordered\_access\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_csip\_set\_coordinator\_ordered\_access\_t) (const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info, struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
| --- |

`#include <[csip.h](csip_8h.md)>`

Callback function definition for [bt\_csip\_set\_coordinator\_ordered\_access()](#gacd83494562a62fbdbc7282107d4454b4).

Parameters
:   | set\_info | Pointer to the a specific set\_info struct. |
    | --- | --- |
    | members | Array of members ordered by rank. The procedure shall be done on the members in ascending order. |
    | count | Number of members in `members`. |

Returns
:   true if the procedures can be successfully done, or false to stop the procedure.

## [◆ ](#gacdb98c9ae3248064e90352387df7cef2)bt\_csip\_set\_coordinator\_sirk\_changed\_cb

| typedef void(\* bt\_csip\_set\_coordinator\_sirk\_changed\_cb) (struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst) |
| --- |

`#include <[csip.h](csip_8h.md)>`

Callback when the SIRK value of a set of a connected device changes.

Parameters
:   | inst | The Coordinated Set Identification Service instance that was changed. The new SIRK can be accessed via the `inst.info`. |
    | --- | --- |

## [◆ ](#ga452591f80b6be5d79609b25ade2154a9)bt\_pacs\_cap\_foreach\_func\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_pacs\_cap\_foreach\_func\_t) (const struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap, void \*user\_data) |
| --- |

`#include <[pacs.h](pacs_8h.md)>`

Published Audio Capability iterator callback.

Parameters
:   | cap | Capability found. |
    | --- | --- |
    | user\_data | Data given. |

Returns
:   true to continue to the next capability
:   false to stop the iteration

## Function Documentation

## [◆ ](#ga7e7ea4a92bb76aded86807571a2cbb73)bt\_csip\_set\_coordinator\_discover()

| int bt\_csip\_set\_coordinator\_discover | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[csip.h](csip_8h.md)>`

Initialise the csip\_set\_coordinator instance for a connection.

This will do a discovery on the device and prepare the instance for following commands.

Parameters
:   | conn | Pointer to remote device to perform discovery on. |
    | --- | --- |

Returns
:   int Return 0 on success, or an errno value on error.

## [◆ ](#gac2a5c323d472c58a7d0cc6060782133e)bt\_csip\_set\_coordinator\_is\_set\_member()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_csip\_set\_coordinator\_is\_set\_member | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *sirk*[16], |
| --- | --- | --- | --- |
|  |  | struct [bt\_data](structbt__data.md) \* | *data* ) |

`#include <[csip.h](csip_8h.md)>`

Check if advertising data indicates a set member.

Parameters
:   | sirk | The SIRK of the set to check against |
    | --- | --- |
    | data | The advertising data |

Returns
:   true if the advertising data indicates a set member, false otherwise

## [◆ ](#ga2d61e25d131631479e34a2c2edf3ebfa)bt\_csip\_set\_coordinator\_lock()

| int bt\_csip\_set\_coordinator\_lock | ( | const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\* | *members*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *count*, |
|  |  | const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \* | *set\_info* ) |

`#include <[csip.h](csip_8h.md)>`

Lock an array of set members.

The members will be locked starting from lowest rank going up.

TODO: If locking fails, the already locked members will not be unlocked.

Parameters
:   | members | Array of set members to lock. |
    | --- | --- |
    | count | Number of set members in `members`. |
    | set\_info | Pointer to the a specific set\_info struct, as a member may be part of multiple sets. |

Returns
:   Return 0 on success, or an errno value on error.

## [◆ ](#gacd83494562a62fbdbc7282107d4454b4)bt\_csip\_set\_coordinator\_ordered\_access()

| int bt\_csip\_set\_coordinator\_ordered\_access | ( | const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \* | *members*[], |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *count*, |
|  |  | const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \* | *set\_info*, |
|  |  | [bt\_csip\_set\_coordinator\_ordered\_access\_t](#ga2ce69e3bf51622fd41389a12d26e2ba9) | *cb* ) |

`#include <[csip.h](csip_8h.md)>`

Access Coordinated Set devices in an ordered manner as a client.

This function will read the lock state of all devices and if all devices are in the unlocked state, then `cb` will be called with the same members as provided by `members`, but where the members are ordered by rank (if present). Once this procedure is finished or an error occurs, [bt\_csip\_set\_coordinator\_cb::ordered\_access](structbt__csip__set__coordinator__cb.md#ae8cf52f1ace4ea1d56ec2204c59bb71c "bt_csip_set_coordinator_cb::ordered_access") will be called.

This procedure only works if all the members have the lock characteristic, and all either has rank = 0 or unique ranks.

If any of the members are in the locked state, the procedure will be cancelled.

This can only be done on members that are bonded.

Parameters
:   | members | Array of set members to access. |
    | --- | --- |
    | count | Number of set members in `members`. |
    | set\_info | Pointer to the a specific set\_info struct, as a member may be part of multiple sets. |
    | cb | The callback function to be called for each member. |

## [◆ ](#ga08c514fda44e5a9b5cfc16be629c2b37)bt\_csip\_set\_coordinator\_register\_cb()

| int bt\_csip\_set\_coordinator\_register\_cb | ( | struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[csip.h](csip_8h.md)>`

Registers callbacks for csip\_set\_coordinator.

Parameters
:   | cb | Pointer to the callback structure. |
    | --- | --- |

Returns
:   Return 0 on success, or an errno value on error.

## [◆ ](#ga5391b625fbcfd66ab07e014659dc2e45)bt\_csip\_set\_coordinator\_release()

| int bt\_csip\_set\_coordinator\_release | ( | const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\* | *members*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *count*, |
|  |  | const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \* | *set\_info* ) |

`#include <[csip.h](csip_8h.md)>`

Release an array of set members.

The members will be released starting from highest rank going down.

Parameters
:   | members | Array of set members to lock. |
    | --- | --- |
    | count | Number of set members in `members`. |
    | set\_info | Pointer to the a specific set\_info struct, as a member may be part of multiple sets. |

Returns
:   Return 0 on success, or an errno value on error.

## [◆ ](#ga8c3666d8f20f909dd4fa2010ae02c9a5)bt\_csip\_set\_coordinator\_set\_member\_by\_conn()

| struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \* bt\_csip\_set\_coordinator\_set\_member\_by\_conn | ( | const struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[csip.h](csip_8h.md)>`

Get the set member from a connection pointer.

Get the Coordinated Set Identification Profile Set Coordinator pointer from a connection pointer. Only Set Coordinators that have been initiated via [bt\_csip\_set\_coordinator\_discover()](#ga7e7ea4a92bb76aded86807571a2cbb73) can be retrieved.

Parameters
:   | conn | Connection pointer. |
    | --- | --- |

Return values
:   | Pointer | to a Coordinated Set Identification Profile Set Coordinator instance |
    | --- | --- |
    | NULL | if `conn` is NULL or if the connection has not done discovery yet |

## [◆ ](#ga8c59233f7e4c8716042c20e25f42a474)bt\_csip\_set\_member\_generate\_rsi()

| int bt\_csip\_set\_member\_generate\_rsi | ( | const struct bt\_csip\_set\_member\_svc\_inst \* | *svc\_inst*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *rsi*[6] ) |

`#include <[csip.h](csip_8h.md)>`

Generate the Resolvable Set Identifier (RSI) value.

This will generate RSI for given `svc_inst` instance.

Parameters
:   | svc\_inst | Pointer to the Coordinated Set Identification Service. |
    | --- | --- |
    | rsi | Pointer to the 6-octet newly generated RSI data in little-endian. |

Returns
:   int 0 if on success, errno on error.

## [◆ ](#gab614480b1f96620e74ab55de95b9ef5d)bt\_csip\_set\_member\_get\_sirk()

| int bt\_csip\_set\_member\_get\_sirk | ( | struct bt\_csip\_set\_member\_svc\_inst \* | *svc\_inst*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *sirk*[16] ) |

`#include <[csip.h](csip_8h.md)>`

Get the SIRK of a service instance.

Parameters
:   | [in] | svc\_inst | Pointer to the registered Coordinated Set Identification Service. |
    | --- | --- | --- |
    | [out] | sirk | Array to store the SIRK in. |

## [◆ ](#ga95e2ba4b65ec42eedb26bf5ad181b606)bt\_csip\_set\_member\_lock()

| int bt\_csip\_set\_member\_lock | ( | struct bt\_csip\_set\_member\_svc\_inst \* | *svc\_inst*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *lock*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *force* ) |

`#include <[csip.h](csip_8h.md)>`

Locks a specific Coordinated Set Identification Service instance on the server.

Parameters
:   | svc\_inst | Pointer to the Coordinated Set Identification Service. |
    | --- | --- |
    | lock | If true lock the set, if false release the set. |
    | force | This argument only have meaning when `lock` is false (release) and will force release the lock, regardless of who took the lock. |

Returns
:   0 on success, GATT error on error.

## [◆ ](#gab11184ace9246d4c5ead6bdc98ffa2ac)bt\_csip\_set\_member\_register()

| int bt\_csip\_set\_member\_register | ( | const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_csip\_set\_member\_svc\_inst \*\* | *svc\_inst* ) |

`#include <[csip.h](csip_8h.md)>`

Register a Coordinated Set Identification Service instance.

This will register and enable the service and make it discoverable by clients.

This shall only be done as a server.

Parameters
:   |  | param | Coordinated Set Identification Service register parameters. |
    | --- | --- | --- |
    | [out] | svc\_inst | Pointer to the registered Coordinated Set Identification Service. |

Returns
:   0 if success, errno on failure.

## [◆ ](#gae07b5073f1dd3381195e3827e6a803f0)bt\_csip\_set\_member\_sirk()

| int bt\_csip\_set\_member\_sirk | ( | struct bt\_csip\_set\_member\_svc\_inst \* | *svc\_inst*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *sirk*[16] ) |

`#include <[csip.h](csip_8h.md)>`

Set the SIRK of a service instance.

Parameters
:   | svc\_inst | Pointer to the registered Coordinated Set Identification Service. |
    | --- | --- |
    | sirk | The new SIRK. |

## [◆ ](#gabc8d9c8d2b2f73f5e18e7fdbce95389c)bt\_csip\_set\_member\_svc\_decl\_get()

| void \* bt\_csip\_set\_member\_svc\_decl\_get | ( | const struct bt\_csip\_set\_member\_svc\_inst \* | *svc\_inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[csip.h](csip_8h.md)>`

Get the service declaration attribute.

The first service attribute can be included in any other GATT service.

Parameters
:   | svc\_inst | Pointer to the Coordinated Set Identification Service. |
    | --- | --- |

Returns
:   The first CSIS attribute instance.

## [◆ ](#ga9ee48e36fb33ee27e689d32f08f071a1)bt\_csip\_set\_member\_unregister()

| int bt\_csip\_set\_member\_unregister | ( | struct bt\_csip\_set\_member\_svc\_inst \* | *svc\_inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[csip.h](csip_8h.md)>`

Unregister a Coordinated Set Identification Service instance.

This will unregister and disable the service instance.

Parameters
:   | svc\_inst | Pointer to the registered Coordinated Set Identification Service. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga31e2c7e9a4b5b6a291b96832c1218a49)bt\_pacs\_cap\_foreach()

| void bt\_pacs\_cap\_foreach | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | [bt\_pacs\_cap\_foreach\_func\_t](#ga452591f80b6be5d79609b25ade2154a9) | *func*, |
|  |  | void \* | *user\_data* ) |

`#include <[pacs.h](pacs_8h.md)>`

Published Audio Capability iterator.

Iterate capabilities with endpoint direction specified.

Parameters
:   | dir | Direction of the endpoint to look capability for. |
    | --- | --- |
    | func | Callback function. |
    | user\_data | Data to pass to the callback. |

## [◆ ](#ga251b36d4f5775eea1f69873709f847cc)bt\_pacs\_cap\_register()

| int bt\_pacs\_cap\_register | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_pacs\_cap](structbt__pacs__cap.md) \* | *cap* ) |

`#include <[pacs.h](pacs_8h.md)>`

Register Published Audio Capability.

Register Audio Local Capability.

Parameters
:   | dir | Direction of the endpoint to register capability for. |
    | --- | --- |
    | cap | Capability structure. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4f6015eba63ffc7a9377afe54a290da1)bt\_pacs\_cap\_unregister()

| int bt\_pacs\_cap\_unregister | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_pacs\_cap](structbt__pacs__cap.md) \* | *cap* ) |

`#include <[pacs.h](pacs_8h.md)>`

Unregister Published Audio Capability.

Unregister Audio Local Capability.

Parameters
:   | dir | Direction of the endpoint to unregister capability for. |
    | --- | --- |
    | cap | Capability structure. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga12f283d2daf72302a01cefb4a4a8fc70)bt\_pacs\_conn\_set\_available\_contexts\_for\_conn()

| int bt\_pacs\_conn\_set\_available\_contexts\_for\_conn | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) \* | *contexts* ) |

`#include <[pacs.h](pacs_8h.md)>`

Set the available contexts for a given connection.

This function sets the available contexts value for a given `conn` connection object. If the `contexts` parameter is NULL the available contexts value is reset to default. The default value of the available contexts is set using [bt\_pacs\_set\_available\_contexts](#ga29a1ec26c1e5e82e02eac39e1088332c) function. The Available Context Value is reset to default on ACL disconnection.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | dir | Direction of the endpoints to change available contexts for. |
    | contexts | The contexts to be set or NULL to reset to default. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga437d824d0a944b6c30db492dbe28514f)bt\_pacs\_get\_available\_contexts()

| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) bt\_pacs\_get\_available\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pacs.h](pacs_8h.md)>`

Get the available contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to get contexts for. |
    | --- | --- |

Returns
:   Bitmask of available contexts.

## [◆ ](#ga7b28aa42525344445b20bb90a19441aa)bt\_pacs\_get\_available\_contexts\_for\_conn()

| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) bt\_pacs\_get\_available\_contexts\_for\_conn | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir* ) |

`#include <[pacs.h](pacs_8h.md)>`

Get the available contexts for a given connection.

This server function returns the available contexts value for a given `conn` connection object. The value returned is the one set with [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](#ga12f283d2daf72302a01cefb4a4a8fc70) function or the default value set with [bt\_pacs\_set\_available\_contexts](#ga29a1ec26c1e5e82e02eac39e1088332c) function.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | dir | Direction of the endpoints to get contexts for. |

Returns
:   Bitmask of available contexts.

Return values
:   | [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a "Prohibited.") | if `conn` or `dir` are invalid |
    | --- | --- |

## [◆ ](#ga29a1ec26c1e5e82e02eac39e1088332c)bt\_pacs\_set\_available\_contexts()

| int bt\_pacs\_set\_available\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *contexts* ) |

`#include <[pacs.h](pacs_8h.md)>`

Set the available contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change available contexts for. |
    | --- | --- |
    | contexts | The contexts to be set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaff290fd59bb05012abcf405dbdc72884)bt\_pacs\_set\_location()

| int bt\_pacs\_set\_location | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) | *location* ) |

`#include <[pacs.h](pacs_8h.md)>`

Set the location for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change location for. |
    | --- | --- |
    | location | The location to be set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gabae9cf025f32ce80b660ebd7f95241b2)bt\_pacs\_set\_supported\_contexts()

| int bt\_pacs\_set\_supported\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *contexts* ) |

`#include <[pacs.h](pacs_8h.md)>`

Set the supported contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change available contexts for. |
    | --- | --- |
    | contexts | The contexts to be set. |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
