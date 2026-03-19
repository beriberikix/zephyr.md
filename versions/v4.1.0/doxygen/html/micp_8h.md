---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/micp_8h.html
original_path: doxygen/html/micp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

micp.h File Reference

Bluetooth Microphone Control Profile (MICP) APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/aics.h](aics_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](micp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_micp\_mic\_dev\_register\_param](structbt__micp__mic__dev__register__param.md) |
|  | Register parameters structure for Microphone Control Service. [More...](structbt__micp__mic__dev__register__param.md#details) |
| struct | [bt\_micp\_included](structbt__micp__included.md) |
|  | Microphone Control Profile included services. [More...](structbt__micp__included.md#details) |
| struct | [bt\_micp\_mic\_dev\_cb](structbt__micp__mic__dev__cb.md) |
|  | Struct to hold the Microphone Device callbacks. [More...](structbt__micp__mic__dev__cb.md#details) |
| struct | [bt\_micp\_mic\_ctlr\_cb](structbt__micp__mic__ctlr__cb.md) |
|  | Struct to hold the Microphone Controller callbacks. [More...](structbt__micp__mic__ctlr__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MICP\_MIC\_DEV\_AICS\_CNT](group__bt__micp.md#ga46cc0362c55cd9bdaf331de834a5fef5)   0 |
|  | Defines the maximum number of Microphone Control Service instances for the Microphone Control Profile Microphone Device. |
| Application error codes | |
| #define | [BT\_MICP\_ERR\_MUTE\_DISABLED](group__bt__micp.md#ga31ce5cce4aa28662de82735241ee49d8)   0x80 |
|  | Mute/unmute commands are disabled. |
| Microphone Control Profile mute states | |
| #define | [BT\_MICP\_MUTE\_UNMUTED](group__bt__micp.md#gaaf0327be66ebf4b0dd23282d4a46aa54)   0x00 |
|  | The microphone state is unmuted. |
| #define | [BT\_MICP\_MUTE\_MUTED](group__bt__micp.md#ga5718e29fefc336fbee1875aa5b81f233)   0x01 |
|  | The microphone state is muted. |
| #define | [BT\_MICP\_MUTE\_DISABLED](group__bt__micp.md#gafc7ed719d471ca27aeb96aaa638c05cb)   0x02 |
|  | The microphone state is disabled and cannot be muted or unmuted. |

| Functions | |
| --- | --- |
| int | [bt\_micp\_mic\_dev\_register](group__bt__micp.md#ga5dee6c7a1115bffbea39ba0575f369fc) (struct [bt\_micp\_mic\_dev\_register\_param](structbt__micp__mic__dev__register__param.md) \*param) |
|  | Initialize the Microphone Control Profile Microphone Device. |
| int | [bt\_micp\_mic\_dev\_included\_get](group__bt__micp.md#ga0541a36655024d9eadcff2d3e0c877f6) (struct [bt\_micp\_included](structbt__micp__included.md) \*included) |
|  | Get Microphone Device included services. |
| int | [bt\_micp\_mic\_dev\_unmute](group__bt__micp.md#ga19ec08afa7784b80fce039fe84a4e33c) (void) |
|  | Unmute the Microphone Device. |
| int | [bt\_micp\_mic\_dev\_mute](group__bt__micp.md#ga47f971c9c259e43504d586a55cf22c4e) (void) |
|  | Mute the Microphone Device. |
| int | [bt\_micp\_mic\_dev\_mute\_disable](group__bt__micp.md#ga525c5d694f7d510d33f088e848733af6) (void) |
|  | Disable the mute functionality on the Microphone Device. |
| int | [bt\_micp\_mic\_dev\_mute\_get](group__bt__micp.md#ga263bf5cf51e4ef8d7e6986f0d8358da3) (void) |
|  | Read the mute state on the Microphone Device. |
| int | [bt\_micp\_mic\_ctlr\_included\_get](group__bt__micp.md#ga21e04942da32b15e75a0b0de3fb84167) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr, struct [bt\_micp\_included](structbt__micp__included.md) \*included) |
|  | Get Microphone Control Profile included services. |
| int | [bt\_micp\_mic\_ctlr\_conn\_get](group__bt__micp.md#ga4b564e6b315a3861f1c3ba6098eabfe1) (const struct bt\_micp\_mic\_ctlr \*mic\_ctlr, struct bt\_conn \*\*conn) |
|  | Get the connection pointer of a Microphone Controller instance. |
| struct bt\_micp\_mic\_ctlr \* | [bt\_micp\_mic\_ctlr\_get\_by\_conn](group__bt__micp.md#ga863030e1b836c01a1be964bce0c72025) (const struct bt\_conn \*conn) |
|  | Get the volume controller from a connection pointer. |
| int | [bt\_micp\_mic\_ctlr\_discover](group__bt__micp.md#ga26187007ebf35ba2a5c57a076a3a7212) (struct bt\_conn \*conn, struct bt\_micp\_mic\_ctlr \*\*mic\_ctlr) |
|  | Discover Microphone Control Service. |
| int | [bt\_micp\_mic\_ctlr\_unmute](group__bt__micp.md#ga6248c90bb94cd138c5bf9c68cffda4fe) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr) |
|  | Unmute a remote Microphone Device. |
| int | [bt\_micp\_mic\_ctlr\_mute](group__bt__micp.md#ga2d50f432703233c0f03cb139b6119faa) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr) |
|  | Mute a remote Microphone Device. |
| int | [bt\_micp\_mic\_ctlr\_mute\_get](group__bt__micp.md#ga5148e78053a3052d27677a1fa24e3847) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr) |
|  | Read the mute state of a remote Microphone Device. |
| int | [bt\_micp\_mic\_ctlr\_cb\_register](group__bt__micp.md#ga148ffcd0672adff9ccfaf35c522897c4) (struct [bt\_micp\_mic\_ctlr\_cb](structbt__micp__mic__ctlr__cb.md) \*cb) |
|  | Registers the callbacks used by Microphone Controller. |

## Detailed Description

Bluetooth Microphone Control Profile (MICP) APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [micp.h](micp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
