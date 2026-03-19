---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mesh__blob__cli.html
original_path: doxygen/html/group__bt__mesh__blob__cli.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh BLOB Transfer Client model API

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md) |
|  | Target node's Pull mode (Pull BLOB Transfer Mode) context used while sending chunks to the Target node. [More...](structbt__mesh__blob__target__pull.md#details) |
| struct | [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) |
|  | BLOB Transfer Client Target node. [More...](structbt__mesh__blob__target.md#details) |
| struct | [bt\_mesh\_blob\_xfer\_info](structbt__mesh__blob__xfer__info.md) |
|  | BLOB transfer information. [More...](structbt__mesh__blob__xfer__info.md#details) |
| struct | [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) |
|  | BLOB Transfer Client transfer inputs. [More...](structbt__mesh__blob__cli__inputs.md#details) |
| struct | [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) |
|  | Transfer capabilities of a Target node. [More...](structbt__mesh__blob__cli__caps.md#details) |
| struct | [bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md) |
|  | Event handler callbacks for the BLOB Transfer Client model. [More...](structbt__mesh__blob__cli__cb.md#details) |
| struct | [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) |
|  | BLOB Transfer Client model instance. [More...](structbt__mesh__blob__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_BLOB\_CLI](#ga882e9cec348625c7990de4ee5eb7ed5a)(\_cli) |
|  | BLOB Transfer Client model Composition Data entry. |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_blob\_cli\_state](#gac86db11f09e53adb2e012bf9e446d073) {     [BT\_MESH\_BLOB\_CLI\_STATE\_NONE](#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67) , [BT\_MESH\_BLOB\_CLI\_STATE\_CAPS\_GET](#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de) , [BT\_MESH\_BLOB\_CLI\_STATE\_START](#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2) , [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_START](#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2) ,     [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_SEND](#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9) , [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_CHECK](#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c) , [BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_CHECK](#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96) , [BT\_MESH\_BLOB\_CLI\_STATE\_CANCEL](#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646) ,     [BT\_MESH\_BLOB\_CLI\_STATE\_SUSPENDED](#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9) , [BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_PROGRESS\_GET](#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c)   } |
|  | BLOB Transfer Client state. [More...](#gac86db11f09e53adb2e012bf9e446d073) |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_blob\_cli\_caps\_get](#gac401336775dc6274450d5e27ea1cd720) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs) |
|  | Retrieve transfer capabilities for a list of Target nodes. |
| int | [bt\_mesh\_blob\_cli\_send](#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io) |
|  | Perform a BLOB transfer. |
| int | [bt\_mesh\_blob\_cli\_suspend](#ga78487f10fae6c87edaaf4e6ec8f7362c) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Suspend the active transfer. |
| int | [bt\_mesh\_blob\_cli\_resume](#ga5aed01e812215d153fdfafd6375cc453) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Resume the suspended transfer. |
| void | [bt\_mesh\_blob\_cli\_cancel](#ga222c650657e9a7958b119d4dddd55783) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Cancel an ongoing transfer. |
| int | [bt\_mesh\_blob\_cli\_xfer\_progress\_get](#ga17a73cb313dbfc6652b4bcf638b9a30f) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs) |
|  | Get the progress of BLOB transfer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get](#ga065196837cbf9d2626b5589ce2671441) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Get the current progress of the active transfer in percent. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_blob\_cli\_is\_busy](#ga37bbc559b48ea8cfe7cb3ddf8cad24da) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Get the current state of the BLOB Transfer Client. |
| void | [bt\_mesh\_blob\_cli\_set\_chunk\_interval\_ms](#ga047e0cd9817b2ff0a241b2ccfad2acf6) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) interval\_ms) |
|  | Set chunk sending interval in ms. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga882e9cec348625c7990de4ee5eb7ed5a)BT\_MESH\_MODEL\_BLOB\_CLI

| #define BT\_MESH\_MODEL\_BLOB\_CLI | ( |  | *\_cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_cli.h](blob__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_BLOB\_CLI](group__bt__mesh__access.md#ga17e2e59a1344e623fe9fec6e27b7f22e), \_bt\_mesh\_blob\_cli\_op, \

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \_cli, &\_bt\_mesh\_blob\_cli\_cb)

[BT\_MESH\_MODEL\_ID\_BLOB\_CLI](group__bt__mesh__access.md#ga17e2e59a1344e623fe9fec6e27b7f22e)

#define BT\_MESH\_MODEL\_ID\_BLOB\_CLI

BLOB Transfer Client.

**Definition** access.h:341

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:495

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

BLOB Transfer Client model Composition Data entry.

Parameters
:   | \_cli | Pointer to a [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md "Bluetooth Mesh BLOB Transfer Client model API") instance. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#gac86db11f09e53adb2e012bf9e446d073)bt\_mesh\_blob\_cli\_state

| enum [bt\_mesh\_blob\_cli\_state](#gac86db11f09e53adb2e012bf9e446d073) |
| --- |

`#include <[blob_cli.h](blob__cli_8h.md)>`

BLOB Transfer Client state.

| Enumerator | |
| --- | --- |
| BT\_MESH\_BLOB\_CLI\_STATE\_NONE | No transfer is active. |
| BT\_MESH\_BLOB\_CLI\_STATE\_CAPS\_GET | Retrieving transfer capabilities. |
| BT\_MESH\_BLOB\_CLI\_STATE\_START | Sending transfer start. |
| BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_START | Sending block start. |
| BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_SEND | Sending block chunks. |
| BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_CHECK | Checking block status. |
| BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_CHECK | Checking transfer status. |
| BT\_MESH\_BLOB\_CLI\_STATE\_CANCEL | Cancelling transfer. |
| BT\_MESH\_BLOB\_CLI\_STATE\_SUSPENDED | Transfer is suspended. |
| BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_PROGRESS\_GET | Checking transfer progress. |

## Function Documentation

## [◆ ](#ga222c650657e9a7958b119d4dddd55783)bt\_mesh\_blob\_cli\_cancel()

| void bt\_mesh\_blob\_cli\_cancel | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Cancel an ongoing transfer.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |

## [◆ ](#gac401336775dc6274450d5e27ea1cd720)bt\_mesh\_blob\_cli\_caps\_get()

| int bt\_mesh\_blob\_cli\_caps\_get | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \* | *inputs* ) |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Retrieve transfer capabilities for a list of Target nodes.

Queries the availability and capabilities of all Target nodes, producing a cumulative set of transfer capabilities for the Target nodes, and returning it through the [bt\_mesh\_blob\_cli\_cb::caps](structbt__mesh__blob__cli__cb.md#a58e749cadeb464299495ee74456c592c "bt_mesh_blob_cli_cb::caps") callback.

Retrieving the capabilities may take several seconds, depending on the number of Target nodes and mesh network performance. The end of the procedure is indicated through the [bt\_mesh\_blob\_cli\_cb::caps](structbt__mesh__blob__cli__cb.md#a58e749cadeb464299495ee74456c592c "bt_mesh_blob_cli_cb::caps") callback.

This procedure is not required, but strongly recommended as a preparation for a transfer to maximize performance and the chances of success.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |
    | inputs | Statically allocated BLOB Transfer Client transfer inputs. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga37bbc559b48ea8cfe7cb3ddf8cad24da)bt\_mesh\_blob\_cli\_is\_busy()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_blob\_cli\_is\_busy | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Get the current state of the BLOB Transfer Client.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |

Returns
:   true if the BLOB Transfer Client is currently participating in a transfer or retrieving the capabilities and false otherwise.

## [◆ ](#ga5aed01e812215d153fdfafd6375cc453)bt\_mesh\_blob\_cli\_resume()

| int bt\_mesh\_blob\_cli\_resume | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Resume the suspended transfer.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2)bt\_mesh\_blob\_cli\_send()

| int bt\_mesh\_blob\_cli\_send | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \* | *inputs*, |
|  |  | const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \* | *xfer*, |
|  |  | const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \* | *io* ) |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Perform a BLOB transfer.

Starts sending the transfer to the Target nodes. Only Target nodes with a `status` of [BT\_MESH\_BLOB\_SUCCESS](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d "BT_MESH_BLOB_SUCCESS") will be considered.

The transfer will keep going either until all Target nodes have been dropped, or the full BLOB has been sent.

The BLOB transfer may take several minutes, depending on the number of Target nodes, size of the BLOB and mesh network performance. The end of the transfer is indicated through the [bt\_mesh\_blob\_cli\_cb::end](structbt__mesh__blob__cli__cb.md#a60bc49eab376b055a8c21099f86fdde7 "bt_mesh_blob_cli_cb::end") callback.

A Client only supports one transfer at the time.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |
    | inputs | Statically allocated BLOB Transfer Client transfer inputs. |
    | xfer | Statically allocated transfer parameters. |
    | io | BLOB stream to read the transfer from. |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga047e0cd9817b2ff0a241b2ccfad2acf6)bt\_mesh\_blob\_cli\_set\_chunk\_interval\_ms()

| void bt\_mesh\_blob\_cli\_set\_chunk\_interval\_ms | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *interval\_ms* ) |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Set chunk sending interval in ms.

This function is optional, and can be used to define how fast chunks are sent in the BLOB Client Model. Without an added delay, for example a Bluetooth Mesh DFU can cause network blockage by constantly sending the next chunks, especially if the chunks are sent to group addresses or multiple unicast addresses.

Note
:   : Big intervals may cause timeouts. Increasing the `timeout_base` accordingly can circumvent this.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |
    | interval\_ms | the delay before each chunk is sent out in ms. |

## [◆ ](#ga78487f10fae6c87edaaf4e6ec8f7362c)bt\_mesh\_blob\_cli\_suspend()

| int bt\_mesh\_blob\_cli\_suspend | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Suspend the active transfer.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code otherwise.

## [◆ ](#ga065196837cbf9d2626b5589ce2671441)bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Get the current progress of the active transfer in percent.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |

Returns
:   The current transfer progress, or 0 if no transfer is active.

## [◆ ](#ga17a73cb313dbfc6652b4bcf638b9a30f)bt\_mesh\_blob\_cli\_xfer\_progress\_get()

| int bt\_mesh\_blob\_cli\_xfer\_progress\_get | ( | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \* | *inputs* ) |

`#include <[blob_cli.h](blob__cli_8h.md)>`

Get the progress of BLOB transfer.

This function can only be used if the BLOB Transfer Client is currently not performing a BLOB transfer. To get progress of the active BLOB transfer, use the [bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get](#ga065196837cbf9d2626b5589ce2671441) function.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |
    | inputs | Statically allocated BLOB Transfer Client transfer inputs. |

Returns
:   0 on success, or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
