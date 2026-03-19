---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mesh__msg.html
original_path: doxygen/html/group__bt__mesh__msg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Message

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Message.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) |
|  | Message sending context. [More...](structbt__mesh__msg__ctx.md#details) |
| struct | [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) |
|  | Acknowledged message context for tracking the status of model messages pending a response. [More...](structbt__mesh__msg__ack__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MIC\_SHORT](#ga658d38a7be18355f6ecd5f7fb4dcabed)   4 |
|  | Length of a short Mesh MIC. |
| #define | [BT\_MESH\_MIC\_LONG](#ga6e8fc0bb4ed35870c0f1652c18a8117d)   8 |
|  | Length of a long Mesh MIC. |
| #define | [BT\_MESH\_MODEL\_OP\_LEN](#gad0b5f56cc9741fcd5dadf157c5e62701)(\_op) |
|  | Helper to determine the length of an opcode. |
| #define | [BT\_MESH\_MODEL\_BUF\_LEN](#ga5352d6fa05808722eba8a76e2446eddb)(\_op, \_payload\_len) |
|  | Helper for model message buffer length. |
| #define | [BT\_MESH\_MODEL\_BUF\_LEN\_LONG\_MIC](#gabb16a024db39706af46ad86e2b04b00d)(\_op, \_payload\_len) |
|  | Helper for model message buffer length. |
| #define | [BT\_MESH\_MODEL\_BUF\_DEFINE](#ga6a61ace773e331d82860b343d51f62e7)(\_buf, \_op, \_payload\_len) |
|  | Define a Mesh model message buffer using [NET\_BUF\_SIMPLE\_DEFINE](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501 "NET_BUF_SIMPLE_DEFINE"). |
| #define | [BT\_MESH\_MSG\_CTX\_INIT](#ga90200861df2575a974e7414e3642058a)(net\_key\_idx, app\_key\_idx, dst, ttl) |
|  | Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization. |
| #define | [BT\_MESH\_MSG\_CTX\_INIT\_APP](#ga98470d8a351528f4ccb8c0ef2edbc030)(app\_key\_idx, dst) |
|  | Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization secured with Application Key. |
| #define | [BT\_MESH\_MSG\_CTX\_INIT\_DEV](#ga3cab6b5e400a205befdc5a6c7609c453)(net\_key\_idx, dst) |
|  | Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization secured with Device Key of a remote device. |
| #define | [BT\_MESH\_MSG\_CTX\_INIT\_PUB](#ga4afe7dad3e38f7e54d65ca608adc9ba3)(pub) |
|  | Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization using Model Publication context. |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_model\_msg\_init](#gaa26850aebc9bfc97d1dafb66ba02021c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcode) |
|  | Initialize a model message. |
| static void | [bt\_mesh\_msg\_ack\_ctx\_init](#gadd25e335133fe29f234243a39f4d7626) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Initialize an acknowledged message context. |
| static void | [bt\_mesh\_msg\_ack\_ctx\_reset](#ga86d3803bde26f496b7de3fa348a04525) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Reset the synchronization semaphore in an acknowledged message context. |
| void | [bt\_mesh\_msg\_ack\_ctx\_clear](#ga3da92606640cdba69a676c2a03c72311) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Clear parameters of an acknowledged message context. |
| int | [bt\_mesh\_msg\_ack\_ctx\_prepare](#ga1bb34a904103933140e2159cb53d49f5) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst, void \*user\_data) |
|  | Prepare an acknowledged message context for the incoming message to wait. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_msg\_ack\_ctx\_busy](#ga974ba5d7df597a21945b75ac5919debd) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Check if the acknowledged message context is initialized with an opcode. |
| int | [bt\_mesh\_msg\_ack\_ctx\_wait](#ga83561f4d003c6c3c2b91a6afd180d1fd) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for a message acknowledge. |
| static void | [bt\_mesh\_msg\_ack\_ctx\_rx](#ga2b054f7dc01daeef067cd3d819a7c42c) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Mark a message as acknowledged. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_msg\_ack\_ctx\_match](#gae10c4229cabf7774684c99154d4ed8ae) (const struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, void \*\*user\_data) |
|  | Check if an opcode and address of a message matches the expected one. |

## Detailed Description

Message.

## Macro Definition Documentation

## [◆ ](#ga6e8fc0bb4ed35870c0f1652c18a8117d)BT\_MESH\_MIC\_LONG

| #define BT\_MESH\_MIC\_LONG   8 |
| --- |

`#include <[msg.h](msg_8h.md)>`

Length of a long Mesh MIC.

## [◆ ](#ga658d38a7be18355f6ecd5f7fb4dcabed)BT\_MESH\_MIC\_SHORT

| #define BT\_MESH\_MIC\_SHORT   4 |
| --- |

`#include <[msg.h](msg_8h.md)>`

Length of a short Mesh MIC.

## [◆ ](#ga6a61ace773e331d82860b343d51f62e7)BT\_MESH\_MODEL\_BUF\_DEFINE

| #define BT\_MESH\_MODEL\_BUF\_DEFINE | ( |  | *\_buf*, |
| --- | --- | --- | --- |
|  |  |  | *\_op*, |
|  |  |  | *\_payload\_len* ) |

`#include <[msg.h](msg_8h.md)>`

**Value:**

[NET\_BUF\_SIMPLE\_DEFINE](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501)(\_buf, [BT\_MESH\_MODEL\_BUF\_LEN](#ga5352d6fa05808722eba8a76e2446eddb)(\_op, (\_payload\_len)))

[BT\_MESH\_MODEL\_BUF\_LEN](#ga5352d6fa05808722eba8a76e2446eddb)

#define BT\_MESH\_MODEL\_BUF\_LEN(\_op, \_payload\_len)

Helper for model message buffer length.

**Definition** msg.h:50

[NET\_BUF\_SIMPLE\_DEFINE](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501)

#define NET\_BUF\_SIMPLE\_DEFINE(\_name, \_size)

Define a net\_buf\_simple stack variable.

**Definition** net\_buf.h:48

Define a Mesh model message buffer using [NET\_BUF\_SIMPLE\_DEFINE](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501 "NET_BUF_SIMPLE_DEFINE").

Parameters
:   | \_buf | Buffer name. |
    | --- | --- |
    | \_op | Opcode of the message. |
    | \_payload\_len | Length of the model message payload. |

## [◆ ](#ga5352d6fa05808722eba8a76e2446eddb)BT\_MESH\_MODEL\_BUF\_LEN

| #define BT\_MESH\_MODEL\_BUF\_LEN | ( |  | *\_op*, |
| --- | --- | --- | --- |
|  |  |  | *\_payload\_len* ) |

`#include <[msg.h](msg_8h.md)>`

**Value:**

([BT\_MESH\_MODEL\_OP\_LEN](#gad0b5f56cc9741fcd5dadf157c5e62701)(\_op) + (\_payload\_len) + [BT\_MESH\_MIC\_SHORT](#ga658d38a7be18355f6ecd5f7fb4dcabed))

[BT\_MESH\_MIC\_SHORT](#ga658d38a7be18355f6ecd5f7fb4dcabed)

#define BT\_MESH\_MIC\_SHORT

Length of a short Mesh MIC.

**Definition** msg.h:30

[BT\_MESH\_MODEL\_OP\_LEN](#gad0b5f56cc9741fcd5dadf157c5e62701)

#define BT\_MESH\_MODEL\_OP\_LEN(\_op)

Helper to determine the length of an opcode.

**Definition** msg.h:39

Helper for model message buffer length.

Returns the length of a Mesh model message buffer, including the opcode length and a short MIC.

Parameters
:   | \_op | Opcode of the message. |
    | --- | --- |
    | \_payload\_len | Length of the model payload. |

## [◆ ](#gabb16a024db39706af46ad86e2b04b00d)BT\_MESH\_MODEL\_BUF\_LEN\_LONG\_MIC

| #define BT\_MESH\_MODEL\_BUF\_LEN\_LONG\_MIC | ( |  | *\_op*, |
| --- | --- | --- | --- |
|  |  |  | *\_payload\_len* ) |

`#include <[msg.h](msg_8h.md)>`

**Value:**

([BT\_MESH\_MODEL\_OP\_LEN](#gad0b5f56cc9741fcd5dadf157c5e62701)(\_op) + (\_payload\_len) + [BT\_MESH\_MIC\_LONG](#ga6e8fc0bb4ed35870c0f1652c18a8117d))

[BT\_MESH\_MIC\_LONG](#ga6e8fc0bb4ed35870c0f1652c18a8117d)

#define BT\_MESH\_MIC\_LONG

Length of a long Mesh MIC.

**Definition** msg.h:32

Helper for model message buffer length.

Returns the length of a Mesh model message buffer, including the opcode length and a long MIC.

Parameters
:   | \_op | Opcode of the message. |
    | --- | --- |
    | \_payload\_len | Length of the model payload. |

## [◆ ](#gad0b5f56cc9741fcd5dadf157c5e62701)BT\_MESH\_MODEL\_OP\_LEN

| #define BT\_MESH\_MODEL\_OP\_LEN | ( |  | *\_op* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[msg.h](msg_8h.md)>`

**Value:**

((\_op) <= 0xff ? 1 : (\_op) <= 0xffff ? 2 : 3)

Helper to determine the length of an opcode.

Parameters
:   | \_op | Opcode. |
    | --- | --- |

## [◆ ](#ga90200861df2575a974e7414e3642058a)BT\_MESH\_MSG\_CTX\_INIT

| #define BT\_MESH\_MSG\_CTX\_INIT | ( |  | *net\_key\_idx*, |
| --- | --- | --- | --- |
|  |  |  | *app\_key\_idx*, |
|  |  |  | *dst*, |
|  |  |  | *ttl* ) |

`#include <[msg.h](msg_8h.md)>`

**Value:**

{ \

.net\_idx = (net\_key\_idx), \

.app\_idx = (app\_key\_idx), \

.addr = (dst), \

.send\_ttl = (ttl), \

}

Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization.

Note
:   If `dst` is a Virtual Address, Label UUID shall be initialized separately.

Parameters
:   | net\_key\_idx | NetKey Index of the subnet to send the message on. Only used if `app_key_idx` points to devkey. |
    | --- | --- |
    | app\_key\_idx | AppKey Index to encrypt the message with. |
    | dst | Remote addr. |
    | ttl | Time To Live. |

## [◆ ](#ga98470d8a351528f4ccb8c0ef2edbc030)BT\_MESH\_MSG\_CTX\_INIT\_APP

| #define BT\_MESH\_MSG\_CTX\_INIT\_APP | ( |  | *app\_key\_idx*, |
| --- | --- | --- | --- |
|  |  |  | *dst* ) |

`#include <[msg.h](msg_8h.md)>`

**Value:**

[BT\_MESH\_MSG\_CTX\_INIT](#ga90200861df2575a974e7414e3642058a)(0, app\_key\_idx, dst, [BT\_MESH\_TTL\_DEFAULT](group__bt__mesh__access.md#ga16516272b42420263b1c47c3ea16c0c8))

[BT\_MESH\_TTL\_DEFAULT](group__bt__mesh__access.md#ga16516272b42420263b1c47c3ea16c0c8)

#define BT\_MESH\_TTL\_DEFAULT

Special TTL value to request using configured default TTL.

**Definition** access.h:960

[BT\_MESH\_MSG\_CTX\_INIT](#ga90200861df2575a974e7414e3642058a)

#define BT\_MESH\_MSG\_CTX\_INIT(net\_key\_idx, app\_key\_idx, dst, ttl)

Helper for bt\_mesh\_msg\_ctx structure initialization.

**Definition** msg.h:119

Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization secured with Application Key.

Parameters
:   | app\_key\_idx | AppKey Index to encrypt the message with. |
    | --- | --- |
    | dst | Remote addr. |

## [◆ ](#ga3cab6b5e400a205befdc5a6c7609c453)BT\_MESH\_MSG\_CTX\_INIT\_DEV

| #define BT\_MESH\_MSG\_CTX\_INIT\_DEV | ( |  | *net\_key\_idx*, |
| --- | --- | --- | --- |
|  |  |  | *dst* ) |

`#include <[msg.h](msg_8h.md)>`

**Value:**

[BT\_MESH\_MSG\_CTX\_INIT](#ga90200861df2575a974e7414e3642058a)(net\_key\_idx, [BT\_MESH\_KEY\_DEV\_REMOTE](group__bt__mesh__access.md#gaaa6ffb62df5d6d55c831d4d9860fc7eb), dst, [BT\_MESH\_TTL\_DEFAULT](group__bt__mesh__access.md#ga16516272b42420263b1c47c3ea16c0c8))

[BT\_MESH\_KEY\_DEV\_REMOTE](group__bt__mesh__access.md#gaaa6ffb62df5d6d55c831d4d9860fc7eb)

#define BT\_MESH\_KEY\_DEV\_REMOTE

Remote device key.

**Definition** access.h:71

Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization secured with Device Key of a remote device.

Parameters
:   | net\_key\_idx | NetKey Index of the subnet to send the message on. |
    | --- | --- |
    | dst | Remote addr. |

## [◆ ](#ga4afe7dad3e38f7e54d65ca608adc9ba3)BT\_MESH\_MSG\_CTX\_INIT\_PUB

| #define BT\_MESH\_MSG\_CTX\_INIT\_PUB | ( |  | *pub* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[msg.h](msg_8h.md)>`

**Value:**

{ \

.app\_idx = (pub)->key, \

.addr = (pub)->addr, \

.send\_ttl = (pub)->ttl, \

.uuid = (pub)->uuid, \

}

Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization using Model Publication context.

Parameters
:   | pub | Pointer to a model publication context. |
    | --- | --- |

## Function Documentation

## [◆ ](#gaa26850aebc9bfc97d1dafb66ba02021c)bt\_mesh\_model\_msg\_init()

| void bt\_mesh\_model\_msg\_init | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *msg*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *opcode* ) |

`#include <[msg.h](msg_8h.md)>`

Initialize a model message.

Clears the message buffer contents, and encodes the given opcode. The message buffer will be ready for filling in payload data.

Parameters
:   | msg | Message buffer. |
    | --- | --- |
    | opcode | Opcode to encode. |

## [◆ ](#ga974ba5d7df597a21945b75ac5919debd)bt\_mesh\_msg\_ack\_ctx\_busy()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_msg\_ack\_ctx\_busy | ( | struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \* | *ack* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[msg.h](msg_8h.md)>`

Check if the acknowledged message context is initialized with an opcode.

Parameters
:   | ack | Acknowledged message context. |
    | --- | --- |

Returns
:   true if the acknowledged message context is initialized with an opcode, false otherwise.

## [◆ ](#ga3da92606640cdba69a676c2a03c72311)bt\_mesh\_msg\_ack\_ctx\_clear()

| void bt\_mesh\_msg\_ack\_ctx\_clear | ( | struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \* | *ack* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[msg.h](msg_8h.md)>`

Clear parameters of an acknowledged message context.

This function clears the opcode, remote address and user data set by [bt\_mesh\_msg\_ack\_ctx\_prepare](#ga1bb34a904103933140e2159cb53d49f5).

Parameters
:   | ack | Acknowledged message context to be cleared. |
    | --- | --- |

## [◆ ](#gadd25e335133fe29f234243a39f4d7626)bt\_mesh\_msg\_ack\_ctx\_init()

| | void bt\_mesh\_msg\_ack\_ctx\_init | ( | struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \* | *ack* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[msg.h](msg_8h.md)>`

Initialize an acknowledged message context.

Initializes semaphore used for synchronization between [bt\_mesh\_msg\_ack\_ctx\_wait](#ga83561f4d003c6c3c2b91a6afd180d1fd) and [bt\_mesh\_msg\_ack\_ctx\_rx](#ga2b054f7dc01daeef067cd3d819a7c42c) calls. Call this function before using [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md "bt_mesh_msg_ack_ctx").

Parameters
:   | ack | Acknowledged message context to initialize. |
    | --- | --- |

## [◆ ](#gae10c4229cabf7774684c99154d4ed8ae)bt\_mesh\_msg\_ack\_ctx\_match()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_msg\_ack\_ctx\_match | ( | const struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \* | *ack*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *op*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | void \*\* | *user\_data* ) |

`#include <[msg.h](msg_8h.md)>`

Check if an opcode and address of a message matches the expected one.

Parameters
:   | ack | Acknowledged message context to be checked. |
    | --- | --- |
    | op | OpCode of the incoming message. |
    | addr | Source address of the incoming message. |
    | user\_data | If not NULL, returns a user data stored in the acknowledged message context by [bt\_mesh\_msg\_ack\_ctx\_prepare](#ga1bb34a904103933140e2159cb53d49f5). |

Returns
:   true if the incoming message matches the expected one, false otherwise.

## [◆ ](#ga1bb34a904103933140e2159cb53d49f5)bt\_mesh\_msg\_ack\_ctx\_prepare()

| int bt\_mesh\_msg\_ack\_ctx\_prepare | ( | struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \* | *ack*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *op*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *dst*, |
|  |  | void \* | *user\_data* ) |

`#include <[msg.h](msg_8h.md)>`

Prepare an acknowledged message context for the incoming message to wait.

This function sets the opcode, remote address of the incoming message and stores the user data. Use this function before calling [bt\_mesh\_msg\_ack\_ctx\_wait](#ga83561f4d003c6c3c2b91a6afd180d1fd).

Parameters
:   | ack | Acknowledged message context to prepare. |
    | --- | --- |
    | op | The message OpCode. |
    | dst | Destination address of the message. |
    | user\_data | User data for the acknowledged message context. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga86d3803bde26f496b7de3fa348a04525)bt\_mesh\_msg\_ack\_ctx\_reset()

| | void bt\_mesh\_msg\_ack\_ctx\_reset | ( | struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \* | *ack* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[msg.h](msg_8h.md)>`

Reset the synchronization semaphore in an acknowledged message context.

This function aborts call to [bt\_mesh\_msg\_ack\_ctx\_wait](#ga83561f4d003c6c3c2b91a6afd180d1fd).

Parameters
:   | ack | Acknowledged message context to be reset. |
    | --- | --- |

## [◆ ](#ga2b054f7dc01daeef067cd3d819a7c42c)bt\_mesh\_msg\_ack\_ctx\_rx()

| | void bt\_mesh\_msg\_ack\_ctx\_rx | ( | struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \* | *ack* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[msg.h](msg_8h.md)>`

Mark a message as acknowledged.

This function unblocks call to [bt\_mesh\_msg\_ack\_ctx\_wait](#ga83561f4d003c6c3c2b91a6afd180d1fd).

Parameters
:   | ack | Context of a message to be acknowledged. |
    | --- | --- |

## [◆ ](#ga83561f4d003c6c3c2b91a6afd180d1fd)bt\_mesh\_msg\_ack\_ctx\_wait()

| int bt\_mesh\_msg\_ack\_ctx\_wait | ( | struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \* | *ack*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[msg.h](msg_8h.md)>`

Wait for a message acknowledge.

This function blocks execution until [bt\_mesh\_msg\_ack\_ctx\_rx](#ga2b054f7dc01daeef067cd3d819a7c42c) is called or by timeout.

Parameters
:   | ack | Acknowledged message context of the message to wait for. |
    | --- | --- |
    | timeout | Wait timeout. |

Returns
:   0 on success, or (negative) error code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
