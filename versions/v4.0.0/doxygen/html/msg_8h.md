---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/msg_8h.html
original_path: doxygen/html/msg_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msg.h File Reference

Message APIs.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`

[Go to the source code of this file.](msg_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) |
|  | Message sending context. [More...](structbt__mesh__msg__ctx.md#details) |
| struct | [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) |
|  | Acknowledged message context for tracking the status of model messages pending a response. [More...](structbt__mesh__msg__ack__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MIC\_SHORT](group__bt__mesh__msg.md#ga658d38a7be18355f6ecd5f7fb4dcabed)   4 |
|  | Length of a short Mesh MIC. |
| #define | [BT\_MESH\_MIC\_LONG](group__bt__mesh__msg.md#ga6e8fc0bb4ed35870c0f1652c18a8117d)   8 |
|  | Length of a long Mesh MIC. |
| #define | [BT\_MESH\_MODEL\_OP\_LEN](group__bt__mesh__msg.md#gad0b5f56cc9741fcd5dadf157c5e62701)(\_op) |
|  | Helper to determine the length of an opcode. |
| #define | [BT\_MESH\_MODEL\_BUF\_LEN](group__bt__mesh__msg.md#ga5352d6fa05808722eba8a76e2446eddb)(\_op, \_payload\_len) |
|  | Helper for model message buffer length. |
| #define | [BT\_MESH\_MODEL\_BUF\_LEN\_LONG\_MIC](group__bt__mesh__msg.md#gabb16a024db39706af46ad86e2b04b00d)(\_op, \_payload\_len) |
|  | Helper for model message buffer length. |
| #define | [BT\_MESH\_MODEL\_BUF\_DEFINE](group__bt__mesh__msg.md#ga6a61ace773e331d82860b343d51f62e7)(\_buf, \_op, \_payload\_len) |
|  | Define a Mesh model message buffer using [NET\_BUF\_SIMPLE\_DEFINE](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501 "NET_BUF_SIMPLE_DEFINE"). |
| #define | [BT\_MESH\_MSG\_CTX\_INIT](group__bt__mesh__msg.md#ga90200861df2575a974e7414e3642058a)(net\_key\_idx, app\_key\_idx, dst, ttl) |
|  | Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization. |
| #define | [BT\_MESH\_MSG\_CTX\_INIT\_APP](group__bt__mesh__msg.md#ga98470d8a351528f4ccb8c0ef2edbc030)(app\_key\_idx, dst) |
|  | Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization secured with Application Key. |
| #define | [BT\_MESH\_MSG\_CTX\_INIT\_DEV](group__bt__mesh__msg.md#ga3cab6b5e400a205befdc5a6c7609c453)(net\_key\_idx, dst) |
|  | Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization secured with Device Key of a remote device. |
| #define | [BT\_MESH\_MSG\_CTX\_INIT\_PUB](group__bt__mesh__msg.md#ga4afe7dad3e38f7e54d65ca608adc9ba3)(pub) |
|  | Helper for [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md "Message sending context.") structure initialization using Model Publication context. |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_model\_msg\_init](group__bt__mesh__msg.md#gaa26850aebc9bfc97d1dafb66ba02021c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcode) |
|  | Initialize a model message. |
| static void | [bt\_mesh\_msg\_ack\_ctx\_init](group__bt__mesh__msg.md#gadd25e335133fe29f234243a39f4d7626) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Initialize an acknowledged message context. |
| static void | [bt\_mesh\_msg\_ack\_ctx\_reset](group__bt__mesh__msg.md#ga86d3803bde26f496b7de3fa348a04525) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Reset the synchronization semaphore in an acknowledged message context. |
| void | [bt\_mesh\_msg\_ack\_ctx\_clear](group__bt__mesh__msg.md#ga3da92606640cdba69a676c2a03c72311) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Clear parameters of an acknowledged message context. |
| int | [bt\_mesh\_msg\_ack\_ctx\_prepare](group__bt__mesh__msg.md#ga1bb34a904103933140e2159cb53d49f5) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst, void \*user\_data) |
|  | Prepare an acknowledged message context for the incoming message to wait. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_msg\_ack\_ctx\_busy](group__bt__mesh__msg.md#ga974ba5d7df597a21945b75ac5919debd) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Check if the acknowledged message context is initialized with an opcode. |
| int | [bt\_mesh\_msg\_ack\_ctx\_wait](group__bt__mesh__msg.md#ga83561f4d003c6c3c2b91a6afd180d1fd) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for a message acknowledge. |
| static void | [bt\_mesh\_msg\_ack\_ctx\_rx](group__bt__mesh__msg.md#ga2b054f7dc01daeef067cd3d819a7c42c) (struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack) |
|  | Mark a message as acknowledged. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_msg\_ack\_ctx\_match](group__bt__mesh__msg.md#gae10c4229cabf7774684c99154d4ed8ae) (const struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, void \*\*user\_data) |
|  | Check if an opcode and address of a message matches the expected one. |

## Detailed Description

Message APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [msg.h](msg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
