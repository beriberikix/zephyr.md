---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/csip_8h.html
original_path: doxygen/html/csip_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

csip.h File Reference

Bluetooth Coordinated Set Identification Profile (CSIP) APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <zephyr/autoconf.h>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/gap.h](gap_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](csip_8h_source.md)

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

| Macros | |
| --- | --- |
| #define | [BT\_CSIP\_SET\_COORDINATOR\_DISCOVER\_TIMER\_VALUE](group__bt__csip.md#ga1633e4caaa03a21da0a5431f5f263076)   [K\_SECONDS](group__clock__apis.md#gadc361472aea59267f6ea38f5e7c7ca2a)(10) |
|  | Recommended timer for member discovery. |
| #define | [BT\_CSIP\_SET\_COORDINATOR\_MAX\_CSIS\_INSTANCES](group__bt__csip.md#ga42702049524f7ce24dfb6061120414df)   0 |
|  | Defines the maximum number of Coordinated Set Identification service instances for the Coordinated Set Identification Set Coordinator. |
| #define | [BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT](group__bt__csip.md#gac2aa2ce09ff4aad8bc423dd5b5643038)   0x00 |
|  | Accept the request to read the SIRK as plaintext. |
| #define | [BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_ACCEPT\_ENC](group__bt__csip.md#gae6422e7e38bacc39ed2f8d52efe9d6db)   0x01 |
|  | Accept the request to read the SIRK, but return encrypted SIRK. |
| #define | [BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_REJECT](group__bt__csip.md#ga0175e269097a2b6f8f303ee97527db4a)   0x02 |
|  | Reject the request to read the SIRK. |
| #define | [BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_OOB\_ONLY](group__bt__csip.md#gaa245a416becaaaeb118b440f9ba2431d)   0x03 |
|  | SIRK is available only via an OOB procedure. |
| #define | [BT\_CSIP\_SIRK\_SIZE](group__bt__csip.md#ga33069821c84e9b4c16c9d95d88c23158)   16 |
|  | Size of the Set Identification Resolving Key (SIRK). |
| #define | [BT\_CSIP\_RSI\_SIZE](group__bt__csip.md#ga5b0149fec5d38e7003593c227b561506)   6 |
|  | Size of the Resolvable Set Identifier (RSI). |
| #define | [BT\_CSIP\_ERROR\_LOCK\_DENIED](group__bt__csip.md#ga00f382d9fe9afb55acfd6f758cef6389)   0x80 |
|  | Service is already locked. |
| #define | [BT\_CSIP\_ERROR\_LOCK\_RELEASE\_DENIED](group__bt__csip.md#gac6eda3e7a9a06f86bc715df20e14daa1)   0x81 |
|  | Service is not locked. |
| #define | [BT\_CSIP\_ERROR\_LOCK\_INVAL\_VALUE](group__bt__csip.md#gaeca8a3a9e136882c200c432b9f83203e)   0x82 |
|  | Invalid lock value. |
| #define | [BT\_CSIP\_ERROR\_SIRK\_OOB\_ONLY](group__bt__csip.md#ga4e0da5f82ef943e660f669a2962bcc7a)   0x83 |
|  | SIRK only available out-of-band. |
| #define | [BT\_CSIP\_ERROR\_LOCK\_ALREADY\_GRANTED](group__bt__csip.md#gaabd5b74d0e805bfb0b492a45445ec4c4)   0x84 |
|  | Client is already owner of the lock. |
| #define | [BT\_CSIP\_DATA\_RSI](group__bt__csip.md#ga04fcc2431bec35d53664c8f5ab18100d)(\_rsi) |
|  | Helper to declare [bt\_data](structbt__data.md "Bluetooth data.") array including RSI. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c)) (struct bt\_conn \*conn, const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member, int err, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) set\_count) |
|  | Callback for discovering Coordinated Set Identification Services. |
| typedef void(\* | [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634)) (int err) |
|  | Callback for locking a set across one or more devices. |
| typedef void(\* | [bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b)) (struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) locked) |
|  | Callback when the lock value on a set of a connected device changes. |
| typedef void(\* | [bt\_csip\_set\_coordinator\_sirk\_changed\_cb](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2)) (struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*inst) |
|  | Callback when the SIRK value of a set of a connected device changes. |
| typedef void(\* | [bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb)) (const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info, int err, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) locked, struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member) |
|  | Callback for [bt\_csip\_set\_coordinator\_ordered\_access()](group__bt__csip.md#gacd83494562a62fbdbc7282107d4454b4 "Access Coordinated Set devices in an ordered manner as a client."). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9)) (const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info, struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Callback function definition for [bt\_csip\_set\_coordinator\_ordered\_access()](group__bt__csip.md#gacd83494562a62fbdbc7282107d4454b4 "Access Coordinated Set devices in an ordered manner as a client."). |

| Functions | |
| --- | --- |
| void \* | [bt\_csip\_set\_member\_svc\_decl\_get](group__bt__csip.md#gabc8d9c8d2b2f73f5e18e7fdbce95389c) (const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst) |
|  | Get the service declaration attribute. |
| int | [bt\_csip\_set\_member\_register](group__bt__csip.md#gab11184ace9246d4c5ead6bdc98ffa2ac) (const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst) |
|  | Register a Coordinated Set Identification Service instance. |
| int | [bt\_csip\_set\_member\_unregister](group__bt__csip.md#ga9ee48e36fb33ee27e689d32f08f071a1) (struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst) |
|  | Unregister a Coordinated Set Identification Service instance. |
| int | [bt\_csip\_set\_member\_sirk](group__bt__csip.md#gae07b5073f1dd3381195e3827e6a803f0) (struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[16]) |
|  | Set the SIRK of a service instance. |
| int | [bt\_csip\_set\_member\_get\_sirk](group__bt__csip.md#gab614480b1f96620e74ab55de95b9ef5d) (struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[16]) |
|  | Get the SIRK of a service instance. |
| int | [bt\_csip\_set\_member\_generate\_rsi](group__bt__csip.md#ga8c59233f7e4c8716042c20e25f42a474) (const struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsi[6]) |
|  | Generate the Resolvable Set Identifier (RSI) value. |
| int | [bt\_csip\_set\_member\_lock](group__bt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606) (struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lock, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) force) |
|  | Locks a specific Coordinated Set Identification Service instance on the server. |
| int | [bt\_csip\_set\_coordinator\_discover](group__bt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73) (struct bt\_conn \*conn) |
|  | Initialise the csip\_set\_coordinator instance for a connection. |
| struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \* | [bt\_csip\_set\_coordinator\_set\_member\_by\_conn](group__bt__csip.md#ga8c3666d8f20f909dd4fa2010ae02c9a5) (const struct bt\_conn \*conn) |
|  | Get the set member from a connection pointer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_csip\_set\_coordinator\_is\_set\_member](group__bt__csip.md#gac2a5c323d472c58a7d0cc6060782133e) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sirk[16], struct [bt\_data](structbt__data.md) \*data) |
|  | Check if advertising data indicates a set member. |
| int | [bt\_csip\_set\_coordinator\_register\_cb](group__bt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37) (struct [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md) \*cb) |
|  | Registers callbacks for csip\_set\_coordinator. |
| int | [bt\_csip\_set\_coordinator\_ordered\_access](group__bt__csip.md#gacd83494562a62fbdbc7282107d4454b4) (const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*members[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info, [bt\_csip\_set\_coordinator\_ordered\_access\_t](group__bt__csip.md#ga2ce69e3bf51622fd41389a12d26e2ba9) cb) |
|  | Access Coordinated Set devices in an ordered manner as a client. |
| int | [bt\_csip\_set\_coordinator\_lock](group__bt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa) (const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info) |
|  | Lock an array of set members. |
| int | [bt\_csip\_set\_coordinator\_release](group__bt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45) (const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*\*members, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, const struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) \*set\_info) |
|  | Release an array of set members. |

## Detailed Description

Bluetooth Coordinated Set Identification Profile (CSIP) APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [csip.h](csip_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
