---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__dfu__cli.html
original_path: doxygen/html/group__bt__mesh__dfu__cli.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Firmware Uppdate Client model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md)

API for the Bluetooth Mesh Firmware Update Client model.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md) |
|  | DFU Target node. [More...](structbt__mesh__dfu__target.md#details) |
| struct | [bt\_mesh\_dfu\_metadata\_status](structbt__mesh__dfu__metadata__status.md) |
|  | Metadata status response. [More...](structbt__mesh__dfu__metadata__status.md#details) |
| struct | [bt\_mesh\_dfu\_target\_status](structbt__mesh__dfu__target__status.md) |
|  | DFU Target node status parameters. [More...](structbt__mesh__dfu__target__status.md#details) |
| struct | [bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md) |
|  | Firmware Update Client event callbacks. [More...](structbt__mesh__dfu__cli__cb.md#details) |
| struct | [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) |
|  | Firmware Update Client model instance. [More...](structbt__mesh__dfu__cli.md#details) |
| struct | [bt\_mesh\_dfu\_cli\_xfer\_blob\_params](structbt__mesh__dfu__cli__xfer__blob__params.md) |
|  | BLOB parameters for Firmware Update Client transfer: [More...](structbt__mesh__dfu__cli__xfer__blob__params.md#details) |
| struct | [bt\_mesh\_dfu\_cli\_xfer](structbt__mesh__dfu__cli__xfer.md) |
|  | Firmware Update Client transfer parameters: [More...](structbt__mesh__dfu__cli__xfer.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_DFU\_CLI\_INIT](#ga0b10a95f9b7c806bfd8649280f535c96)(\_handlers) |
|  | Initialization parameters for the [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md "Firmware Uppdate Client model"). |
| #define | [BT\_MESH\_MODEL\_DFU\_CLI](#gadee3710bb46d907a51232ca42cca7c2d)(\_cli) |
|  | Firmware Update Client model Composition Data entry. |

| Typedefs | |
| --- | --- |
| typedef enum [bt\_mesh\_dfu\_iter](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6)(\* | [bt\_mesh\_dfu\_img\_cb\_t](#ga2967b89e8fc3b848b70e493f6e821761)) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) total, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, void \*cb\_data) |
|  | DFU image callback. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_dfu\_cli\_send](#ga20764694315adb4f846dcff20f377417) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_dfu\_cli\_xfer](structbt__mesh__dfu__cli__xfer.md) \*xfer) |
|  | Start distributing a DFU. |
| int | [bt\_mesh\_dfu\_cli\_suspend](#gaa1ed22da058839c9f3234ce2e41eda32) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Suspend a DFU transfer. |
| int | [bt\_mesh\_dfu\_cli\_resume](#ga0011fb5c03e6e8c2babfb677d528033b) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Resume the suspended transfer. |
| int | [bt\_mesh\_dfu\_cli\_cancel](#ga4c7353f45a6e33884844fd9d2f443750) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx) |
|  | Cancel a DFU transfer. |
| int | [bt\_mesh\_dfu\_cli\_apply](#ga2904ba992a00ee9fba6704c1efc8f074) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Apply the completed DFU transfer. |
| int | [bt\_mesh\_dfu\_cli\_confirm](#gaf76f0cdb5c6b0df12ddb495c718c3c93) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Confirm that the active transfer has been applied on the Target nodes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_dfu\_cli\_progress](#ga073c5bc227040f1f33e7b3f2fe69a309) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Get progress as a percentage of completion. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_dfu\_cli\_is\_busy](#gad6308700322d96676635bcf0b70c74f7) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Check whether a DFU transfer is in progress. |
| int | [bt\_mesh\_dfu\_cli\_imgs\_get](#ga4c33f9457d4f367760a51a771dfd2671) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [bt\_mesh\_dfu\_img\_cb\_t](#ga2967b89e8fc3b848b70e493f6e821761) cb, void \*cb\_data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_count) |
|  | Perform a DFU image list request. |
| int | [bt\_mesh\_dfu\_cli\_metadata\_check](#ga20b3e7d3d3640149a20d698a6aa7dca5) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_idx, const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot, struct [bt\_mesh\_dfu\_metadata\_status](structbt__mesh__dfu__metadata__status.md) \*rsp) |
|  | Perform a metadata check for the given DFU image slot. |
| int | [bt\_mesh\_dfu\_cli\_status\_get](#gab754da11705a2d6a24ec828aa7862579) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, struct [bt\_mesh\_dfu\_target\_status](structbt__mesh__dfu__target__status.md) \*rsp) |
|  | Get the status of a Target node. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_dfu\_cli\_timeout\_get](#ga3dd10bd1e8673973fd6db98d3ebda354) (void) |
|  | Get the current procedure timeout value. |
| void | [bt\_mesh\_dfu\_cli\_timeout\_set](#ga603adf5b40b6e382c9035c9f2bad99a9) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the procedure timeout value. |

## Detailed Description

API for the Bluetooth Mesh Firmware Update Client model.

## Macro Definition Documentation

## [◆ ](#ga0b10a95f9b7c806bfd8649280f535c96)BT\_MESH\_DFU\_CLI\_INIT

| #define BT\_MESH\_DFU\_CLI\_INIT | ( |  | *\_handlers* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

**Value:**

{ \

.cb = \_handlers, \

.blob = { .cb = &\_bt\_mesh\_dfu\_cli\_blob\_handlers }, \

}

Initialization parameters for the [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md "Firmware Uppdate Client model").

See also
:   [bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md "Firmware Update Client event callbacks.").

Parameters
:   | \_handlers | Handler callback structure. |
    | --- | --- |

## [◆ ](#gadee3710bb46d907a51232ca42cca7c2d)BT\_MESH\_MODEL\_DFU\_CLI

| #define BT\_MESH\_MODEL\_DFU\_CLI | ( |  | *\_cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_BLOB\_CLI](group__bt__mesh__blob__cli.md#ga882e9cec348625c7990de4ee5eb7ed5a)(&(\_cli)->blob), \

BT\_MESH\_MODEL\_CB([BT\_MESH\_MODEL\_ID\_DFU\_CLI](group__bt__mesh__access.md#gaf477a37238ec577000a646af40862ee1), \_bt\_mesh\_dfu\_cli\_op, NULL, \

\_cli, &\_bt\_mesh\_dfu\_cli\_cb)

[BT\_MESH\_MODEL\_ID\_DFU\_CLI](group__bt__mesh__access.md#gaf477a37238ec577000a646af40862ee1)

#define BT\_MESH\_MODEL\_ID\_DFU\_CLI

Firmware Update Client.

**Definition** access.h:353

[BT\_MESH\_MODEL\_BLOB\_CLI](group__bt__mesh__blob__cli.md#ga882e9cec348625c7990de4ee5eb7ed5a)

#define BT\_MESH\_MODEL\_BLOB\_CLI(\_cli)

BLOB Transfer Client model Composition Data entry.

**Definition** blob\_cli.h:33

Firmware Update Client model Composition Data entry.

Parameters
:   | \_cli | Pointer to a [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md "Firmware Uppdate Client model") instance. |
    | --- | --- |

## Typedef Documentation

## [◆ ](#ga2967b89e8fc3b848b70e493f6e821761)bt\_mesh\_dfu\_img\_cb\_t

| typedef enum [bt\_mesh\_dfu\_iter](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6)(\* bt\_mesh\_dfu\_img\_cb\_t) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) total, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, void \*cb\_data) |
| --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

DFU image callback.

The image callback is called for every DFU image on the Target node when calling [bt\_mesh\_dfu\_cli\_imgs\_get](#ga4c33f9457d4f367760a51a771dfd2671).

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |
    | ctx | Message context of the received message. |
    | idx | Image index. |
    | total | Total number of images on the Target node. |
    | img | Image information for the given image index. |
    | cb\_data | Callback data. |

Return values
:   | [BT\_MESH\_DFU\_ITER\_STOP](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be "Stop iterating.") | Stop iterating through the image list and return from [bt\_mesh\_dfu\_cli\_imgs\_get](#ga4c33f9457d4f367760a51a771dfd2671). |
    | --- | --- |
    | [BT\_MESH\_DFU\_ITER\_CONTINUE](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba "Continue iterating.") | Continue iterating through the image list if any images remain. |

## Function Documentation

## [◆ ](#ga2904ba992a00ee9fba6704c1efc8f074)bt\_mesh\_dfu\_cli\_apply()

| int bt\_mesh\_dfu\_cli\_apply | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Apply the completed DFU transfer.

A transfer can only be applied after it has ended successfully. The Firmware Update Client's `applied` callback is called at the end of the apply procedure.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga4c7353f45a6e33884844fd9d2f443750)bt\_mesh\_dfu\_cli\_cancel()

| int bt\_mesh\_dfu\_cli\_cancel | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx* ) |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Cancel a DFU transfer.

Will cancel the ongoing DFU transfer, or the transfer on a specific Target node if `ctx` is valid.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |
    | ctx | Message context, or NULL to cancel the ongoing DFU transfer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gaf76f0cdb5c6b0df12ddb495c718c3c93)bt\_mesh\_dfu\_cli\_confirm()

| int bt\_mesh\_dfu\_cli\_confirm | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Confirm that the active transfer has been applied on the Target nodes.

A transfer can only be confirmed after it has been applied. The Firmware Update Client's `confirmed` callback is called at the end of the confirm procedure.

Target nodes that have reported the effect as [BT\_MESH\_DFU\_EFFECT\_UNPROV](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211 "BT_MESH_DFU_EFFECT_UNPROV") are expected to not respond to the query, and will fail if they do.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga4c33f9457d4f367760a51a771dfd2671)bt\_mesh\_dfu\_cli\_imgs\_get()

| int bt\_mesh\_dfu\_cli\_imgs\_get | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [bt\_mesh\_dfu\_img\_cb\_t](#ga2967b89e8fc3b848b70e493f6e821761) | *cb*, |
|  |  | void \* | *cb\_data*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *max\_count* ) |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Perform a DFU image list request.

Requests the full list of DFU images on a Target node, and iterates through them, calling the `cb` for every image.

The DFU image list request can be used to determine which image index the Target node holds its different firmwares in.

Waits for a response until the procedure timeout expires.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |
    | ctx | Message context. |
    | cb | Callback to call for each image index. |
    | cb\_data | Callback data to pass to `cb`. |
    | max\_count | Max number of images to return. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gad6308700322d96676635bcf0b70c74f7)bt\_mesh\_dfu\_cli\_is\_busy()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_dfu\_cli\_is\_busy | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Check whether a DFU transfer is in progress.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |

Returns
:   true if the BLOB Transfer Client is currently participating in a transfer, false otherwise.

## [◆ ](#ga20b3e7d3d3640149a20d698a6aa7dca5)bt\_mesh\_dfu\_cli\_metadata\_check()

| int bt\_mesh\_dfu\_cli\_metadata\_check | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *img\_idx*, |
|  |  | const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \* | *slot*, |
|  |  | struct [bt\_mesh\_dfu\_metadata\_status](structbt__mesh__dfu__metadata__status.md) \* | *rsp* ) |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Perform a metadata check for the given DFU image slot.

The metadata check procedure allows the Firmware Update Client to check if a Target node will accept a transfer of this DFU image slot, and what the effect would be.

Waits for a response until the procedure timeout expires.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |
    | ctx | Message context. |
    | img\_idx | Target node's image index to check. |
    | slot | DFU image slot to check for. |
    | rsp | Metadata status response buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga073c5bc227040f1f33e7b3f2fe69a309)bt\_mesh\_dfu\_cli\_progress()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_cli\_progress | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Get progress as a percentage of completion.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |

Returns
:   The progress of the current transfer in percent, or 0 if no transfer is active.

## [◆ ](#ga0011fb5c03e6e8c2babfb677d528033b)bt\_mesh\_dfu\_cli\_resume()

| int bt\_mesh\_dfu\_cli\_resume | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Resume the suspended transfer.

Parameters
:   | cli | Firmware Update Client instance. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga20764694315adb4f846dcff20f377417)bt\_mesh\_dfu\_cli\_send()

| int bt\_mesh\_dfu\_cli\_send | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \* | *inputs*, |
|  |  | const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \* | *io*, |
|  |  | const struct [bt\_mesh\_dfu\_cli\_xfer](structbt__mesh__dfu__cli__xfer.md) \* | *xfer* ) |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Start distributing a DFU.

Starts distribution of the firmware in the given slot to the list of DFU Target nodes in `ctx`. The transfer runs in the background, and its end is signalled through the [bt\_mesh\_dfu\_cli\_cb::ended](structbt__mesh__dfu__cli__cb.md#aa3c8985490a6b2bd6fcd81dff0132060 "bt_mesh_dfu_cli_cb::ended") callback.

Note
:   The BLOB Transfer Client transfer inputs `targets` list must point to a list of [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md "bt_mesh_dfu_target") nodes.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |
    | inputs | BLOB Transfer Client transfer inputs. |
    | io | BLOB stream to read BLOB from. |
    | xfer | Firmware Update Client transfer parameters. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gab754da11705a2d6a24ec828aa7862579)bt\_mesh\_dfu\_cli\_status\_get()

| int bt\_mesh\_dfu\_cli\_status\_get | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | struct [bt\_mesh\_dfu\_target\_status](structbt__mesh__dfu__target__status.md) \* | *rsp* ) |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Get the status of a Target node.

Parameters
:   | cli | Firmware Update Client model instance. |
    | --- | --- |
    | ctx | Message context. |
    | rsp | Response data buffer. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#gaa1ed22da058839c9f3234ce2e41eda32)bt\_mesh\_dfu\_cli\_suspend()

| int bt\_mesh\_dfu\_cli\_suspend | ( | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Suspend a DFU transfer.

Parameters
:   | cli | Firmware Update Client instance. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga3dd10bd1e8673973fd6db98d3ebda354)bt\_mesh\_dfu\_cli\_timeout\_get()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) bt\_mesh\_dfu\_cli\_timeout\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Get the current procedure timeout value.

Returns
:   The configured procedure timeout.

## [◆ ](#ga603adf5b40b6e382c9035c9f2bad99a9)bt\_mesh\_dfu\_cli\_timeout\_set()

| void bt\_mesh\_dfu\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_cli.h](dfu__cli_8h.md)>`

Set the procedure timeout value.

Parameters
:   | timeout | The new procedure timeout. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
