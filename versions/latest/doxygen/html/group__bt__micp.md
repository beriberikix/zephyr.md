---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__micp.html
original_path: doxygen/html/group__bt__micp.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Microphone Control Profile (MICP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Microphone Control Profile (MICP).
[More...](#details)

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
| #define | [BT\_MICP\_MIC\_DEV\_AICS\_CNT](#ga46cc0362c55cd9bdaf331de834a5fef5)   0 |
|  | Defines the maximum number of Microphone Control Service instances for the Microphone Control Profile Microphone Device. |

| Functions | |
| --- | --- |
| int | [bt\_micp\_mic\_dev\_register](#ga5dee6c7a1115bffbea39ba0575f369fc) (struct [bt\_micp\_mic\_dev\_register\_param](structbt__micp__mic__dev__register__param.md) \*param) |
|  | Initialize the Microphone Control Profile Microphone Device. |
| int | [bt\_micp\_mic\_dev\_included\_get](#ga0541a36655024d9eadcff2d3e0c877f6) (struct [bt\_micp\_included](structbt__micp__included.md) \*included) |
|  | Get Microphone Device included services. |
| int | [bt\_micp\_mic\_dev\_unmute](#ga19ec08afa7784b80fce039fe84a4e33c) (void) |
|  | Unmute the Microphone Device. |
| int | [bt\_micp\_mic\_dev\_mute](#ga47f971c9c259e43504d586a55cf22c4e) (void) |
|  | Mute the Microphone Device. |
| int | [bt\_micp\_mic\_dev\_mute\_disable](#ga525c5d694f7d510d33f088e848733af6) (void) |
|  | Disable the mute functionality on the Microphone Device. |
| int | [bt\_micp\_mic\_dev\_mute\_get](#ga263bf5cf51e4ef8d7e6986f0d8358da3) (void) |
|  | Read the mute state on the Microphone Device. |
| int | [bt\_micp\_mic\_ctlr\_included\_get](#ga21e04942da32b15e75a0b0de3fb84167) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr, struct [bt\_micp\_included](structbt__micp__included.md) \*included) |
|  | Get Microphone Control Profile included services. |
| int | [bt\_micp\_mic\_ctlr\_conn\_get](#ga4b564e6b315a3861f1c3ba6098eabfe1) (const struct bt\_micp\_mic\_ctlr \*mic\_ctlr, struct bt\_conn \*\*conn) |
|  | Get the connection pointer of a Microphone Controller instance. |
| struct bt\_micp\_mic\_ctlr \* | [bt\_micp\_mic\_ctlr\_get\_by\_conn](#ga863030e1b836c01a1be964bce0c72025) (const struct bt\_conn \*conn) |
|  | Get the volume controller from a connection pointer. |
| int | [bt\_micp\_mic\_ctlr\_discover](#ga26187007ebf35ba2a5c57a076a3a7212) (struct bt\_conn \*conn, struct bt\_micp\_mic\_ctlr \*\*mic\_ctlr) |
|  | Discover Microphone Control Service. |
| int | [bt\_micp\_mic\_ctlr\_unmute](#ga6248c90bb94cd138c5bf9c68cffda4fe) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr) |
|  | Unmute a remote Microphone Device. |
| int | [bt\_micp\_mic\_ctlr\_mute](#ga2d50f432703233c0f03cb139b6119faa) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr) |
|  | Mute a remote Microphone Device. |
| int | [bt\_micp\_mic\_ctlr\_mute\_get](#ga5148e78053a3052d27677a1fa24e3847) (struct bt\_micp\_mic\_ctlr \*mic\_ctlr) |
|  | Read the mute state of a remote Microphone Device. |
| int | [bt\_micp\_mic\_ctlr\_cb\_register](#ga148ffcd0672adff9ccfaf35c522897c4) (struct [bt\_micp\_mic\_ctlr\_cb](structbt__micp__mic__ctlr__cb.md) \*cb) |
|  | Registers the callbacks used by Microphone Controller. |

| Application error codes | |
| --- | --- |
| #define | [BT\_MICP\_ERR\_MUTE\_DISABLED](#ga31ce5cce4aa28662de82735241ee49d8)   0x80 |
|  | Mute/unmute commands are disabled. |

| Microphone Control Profile mute states | |
| --- | --- |
| #define | [BT\_MICP\_MUTE\_UNMUTED](#gaaf0327be66ebf4b0dd23282d4a46aa54)   0x00 |
|  | The microphone state is unmuted. |
| #define | [BT\_MICP\_MUTE\_MUTED](#ga5718e29fefc336fbee1875aa5b81f233)   0x01 |
|  | The microphone state is muted. |
| #define | [BT\_MICP\_MUTE\_DISABLED](#gafc7ed719d471ca27aeb96aaa638c05cb)   0x02 |
|  | The microphone state is disabled and cannot be muted or unmuted. |

## Detailed Description

Microphone Control Profile (MICP).

Since
:   2.7

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga31ce5cce4aa28662de82735241ee49d8)BT\_MICP\_ERR\_MUTE\_DISABLED

| #define BT\_MICP\_ERR\_MUTE\_DISABLED   0x80 |
| --- |

`#include <[micp.h](micp_8h.md)>`

Mute/unmute commands are disabled.

## [◆ ](#ga46cc0362c55cd9bdaf331de834a5fef5)BT\_MICP\_MIC\_DEV\_AICS\_CNT

| #define BT\_MICP\_MIC\_DEV\_AICS\_CNT   0 |
| --- |

`#include <[micp.h](micp_8h.md)>`

Defines the maximum number of Microphone Control Service instances for the Microphone Control Profile Microphone Device.

## [◆ ](#gafc7ed719d471ca27aeb96aaa638c05cb)BT\_MICP\_MUTE\_DISABLED

| #define BT\_MICP\_MUTE\_DISABLED   0x02 |
| --- |

`#include <[micp.h](micp_8h.md)>`

The microphone state is disabled and cannot be muted or unmuted.

## [◆ ](#ga5718e29fefc336fbee1875aa5b81f233)BT\_MICP\_MUTE\_MUTED

| #define BT\_MICP\_MUTE\_MUTED   0x01 |
| --- |

`#include <[micp.h](micp_8h.md)>`

The microphone state is muted.

## [◆ ](#gaaf0327be66ebf4b0dd23282d4a46aa54)BT\_MICP\_MUTE\_UNMUTED

| #define BT\_MICP\_MUTE\_UNMUTED   0x00 |
| --- |

`#include <[micp.h](micp_8h.md)>`

The microphone state is unmuted.

## Function Documentation

## [◆ ](#ga148ffcd0672adff9ccfaf35c522897c4)bt\_micp\_mic\_ctlr\_cb\_register()

| int bt\_micp\_mic\_ctlr\_cb\_register | ( | struct [bt\_micp\_mic\_ctlr\_cb](structbt__micp__mic__ctlr__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Registers the callbacks used by Microphone Controller.

This can only be done as the client.

Parameters
:   | cb | The callback structure. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga4b564e6b315a3861f1c3ba6098eabfe1)bt\_micp\_mic\_ctlr\_conn\_get()

| int bt\_micp\_mic\_ctlr\_conn\_get | ( | const struct bt\_micp\_mic\_ctlr \* | *mic\_ctlr*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \*\* | *conn* ) |

`#include <[micp.h](micp_8h.md)>`

Get the connection pointer of a Microphone Controller instance.

Get the Bluetooth connection pointer of a Microphone Controller instance.

Parameters
:   | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- |
    | conn | Connection pointer. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga26187007ebf35ba2a5c57a076a3a7212)bt\_micp\_mic\_ctlr\_discover()

| int bt\_micp\_mic\_ctlr\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_micp\_mic\_ctlr \*\* | *mic\_ctlr* ) |

`#include <[micp.h](micp_8h.md)>`

Discover Microphone Control Service.

This will start a GATT discovery and setup handles and subscriptions. This shall be called once before any other actions can be executed for the peer device, and the [bt\_micp\_mic\_ctlr\_cb::discover](structbt__micp__mic__ctlr__cb.md#a2359b88344bf36c3a491b0126dac006b "bt_micp_mic_ctlr_cb::discover") callback will notify when it is possible to start remote operations.

- Parameters
  :   |  | conn | The connection to initialize the profile for. |
      | --- | --- | --- |
      | [out] | mic\_ctlr | Valid remote instance object on success. |

  Returns
  :   0 on success, GATT error value on fail.

## [◆ ](#ga863030e1b836c01a1be964bce0c72025)bt\_micp\_mic\_ctlr\_get\_by\_conn()

| struct bt\_micp\_mic\_ctlr \* bt\_micp\_mic\_ctlr\_get\_by\_conn | ( | const struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Get the volume controller from a connection pointer.

Get the Volume Control Profile Volume Controller pointer from a connection pointer. Only volume controllers that have been initiated via [bt\_micp\_mic\_ctlr\_discover()](#ga26187007ebf35ba2a5c57a076a3a7212) can be retrieved.

Parameters
:   | conn | Connection pointer. |
    | --- | --- |

Return values
:   | Pointer | to a Microphone Control Profile Microphone Controller instance |
    | --- | --- |
    | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | if `conn` is NULL or if the connection has not done discovery yet |

## [◆ ](#ga21e04942da32b15e75a0b0de3fb84167)bt\_micp\_mic\_ctlr\_included\_get()

| int bt\_micp\_mic\_ctlr\_included\_get | ( | struct bt\_micp\_mic\_ctlr \* | *mic\_ctlr*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_micp\_included](structbt__micp__included.md) \* | *included* ) |

`#include <[micp.h](micp_8h.md)>`

Get Microphone Control Profile included services.

Returns a pointer to a struct that contains information about the Microphone Control Profile included services instances, such as pointers to the Audio Input Control Service instances.

Requires that `CONFIG_BT_MICP_MIC_CTLR_AICS` is enabled.

Parameters
:   |  | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- | --- |
    | [out] | included | Pointer to store the result in. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga2d50f432703233c0f03cb139b6119faa)bt\_micp\_mic\_ctlr\_mute()

| int bt\_micp\_mic\_ctlr\_mute | ( | struct bt\_micp\_mic\_ctlr \* | *mic\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Mute a remote Microphone Device.

Parameters
:   | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga5148e78053a3052d27677a1fa24e3847)bt\_micp\_mic\_ctlr\_mute\_get()

| int bt\_micp\_mic\_ctlr\_mute\_get | ( | struct bt\_micp\_mic\_ctlr \* | *mic\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Read the mute state of a remote Microphone Device.

Parameters
:   | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga6248c90bb94cd138c5bf9c68cffda4fe)bt\_micp\_mic\_ctlr\_unmute()

| int bt\_micp\_mic\_ctlr\_unmute | ( | struct bt\_micp\_mic\_ctlr \* | *mic\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Unmute a remote Microphone Device.

Parameters
:   | mic\_ctlr | Microphone Controller instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga0541a36655024d9eadcff2d3e0c877f6)bt\_micp\_mic\_dev\_included\_get()

| int bt\_micp\_mic\_dev\_included\_get | ( | struct [bt\_micp\_included](structbt__micp__included.md) \* | *included* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Get Microphone Device included services.

Returns a pointer to a struct that contains information about the Microphone Device included Audio Input Control Service instances.

Requires that `CONFIG_BT_MICP_MIC_DEV_AICS` is enabled.

Parameters
:   | included | Pointer to store the result in. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga47f971c9c259e43504d586a55cf22c4e)bt\_micp\_mic\_dev\_mute()

| int bt\_micp\_mic\_dev\_mute | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Mute the Microphone Device.

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga525c5d694f7d510d33f088e848733af6)bt\_micp\_mic\_dev\_mute\_disable()

| int bt\_micp\_mic\_dev\_mute\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Disable the mute functionality on the Microphone Device.

Can be reenabled by called [bt\_micp\_mic\_dev\_mute](#ga47f971c9c259e43504d586a55cf22c4e) or [bt\_micp\_mic\_dev\_unmute](#ga19ec08afa7784b80fce039fe84a4e33c).

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga263bf5cf51e4ef8d7e6986f0d8358da3)bt\_micp\_mic\_dev\_mute\_get()

| int bt\_micp\_mic\_dev\_mute\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Read the mute state on the Microphone Device.

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga5dee6c7a1115bffbea39ba0575f369fc)bt\_micp\_mic\_dev\_register()

| int bt\_micp\_mic\_dev\_register | ( | struct [bt\_micp\_mic\_dev\_register\_param](structbt__micp__mic__dev__register__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Initialize the Microphone Control Profile Microphone Device.

This will enable the Microphone Control Service instance and make it discoverable by Microphone Controllers.

Parameters
:   | param | Pointer to an initialization structure. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga19ec08afa7784b80fce039fe84a4e33c)bt\_micp\_mic\_dev\_unmute()

| int bt\_micp\_mic\_dev\_unmute | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[micp.h](micp_8h.md)>`

Unmute the Microphone Device.

Returns
:   0 on success, GATT error value on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
