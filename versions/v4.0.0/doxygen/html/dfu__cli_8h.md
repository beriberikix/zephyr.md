---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dfu__cli_8h.html
original_path: doxygen/html/dfu__cli_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu\_cli.h File Reference

`#include <[zephyr/bluetooth/mesh/access.h](access_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/blob_cli.h](blob__cli_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/dfu.h](dfu_8h_source.md)>`

[Go to the source code of this file.](dfu__cli_8h_source.md)

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
| #define | [BT\_MESH\_DFU\_CLI\_INIT](group__bt__mesh__dfu__cli.md#ga0b10a95f9b7c806bfd8649280f535c96)(\_handlers) |
|  | Initialization parameters for the [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md "Firmware Uppdate Client model"). |
| #define | [BT\_MESH\_MODEL\_DFU\_CLI](group__bt__mesh__dfu__cli.md#gadee3710bb46d907a51232ca42cca7c2d)(\_cli) |
|  | Firmware Update Client model Composition Data entry. |

| Typedefs | |
| --- | --- |
| typedef enum [bt\_mesh\_dfu\_iter](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6)(\* | [bt\_mesh\_dfu\_img\_cb\_t](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761)) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) total, const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, void \*cb\_data) |
|  | DFU image callback. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_dfu\_cli\_send](group__bt__mesh__dfu__cli.md#ga20764694315adb4f846dcff20f377417) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, const struct [bt\_mesh\_dfu\_cli\_xfer](structbt__mesh__dfu__cli__xfer.md) \*xfer) |
|  | Start distributing a DFU. |
| int | [bt\_mesh\_dfu\_cli\_suspend](group__bt__mesh__dfu__cli.md#gaa1ed22da058839c9f3234ce2e41eda32) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Suspend a DFU transfer. |
| int | [bt\_mesh\_dfu\_cli\_resume](group__bt__mesh__dfu__cli.md#ga0011fb5c03e6e8c2babfb677d528033b) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Resume the suspended transfer. |
| int | [bt\_mesh\_dfu\_cli\_cancel](group__bt__mesh__dfu__cli.md#ga4c7353f45a6e33884844fd9d2f443750) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx) |
|  | Cancel a DFU transfer. |
| int | [bt\_mesh\_dfu\_cli\_apply](group__bt__mesh__dfu__cli.md#ga2904ba992a00ee9fba6704c1efc8f074) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Apply the completed DFU transfer. |
| int | [bt\_mesh\_dfu\_cli\_confirm](group__bt__mesh__dfu__cli.md#gaf76f0cdb5c6b0df12ddb495c718c3c93) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Confirm that the active transfer has been applied on the Target nodes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_dfu\_cli\_progress](group__bt__mesh__dfu__cli.md#ga073c5bc227040f1f33e7b3f2fe69a309) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Get progress as a percentage of completion. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_dfu\_cli\_is\_busy](group__bt__mesh__dfu__cli.md#gad6308700322d96676635bcf0b70c74f7) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli) |
|  | Check whether a DFU transfer is in progress. |
| int | [bt\_mesh\_dfu\_cli\_imgs\_get](group__bt__mesh__dfu__cli.md#ga4c33f9457d4f367760a51a771dfd2671) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [bt\_mesh\_dfu\_img\_cb\_t](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761) cb, void \*cb\_data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_count) |
|  | Perform a DFU image list request. |
| int | [bt\_mesh\_dfu\_cli\_metadata\_check](group__bt__mesh__dfu__cli.md#ga20b3e7d3d3640149a20d698a6aa7dca5) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_idx, const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot, struct [bt\_mesh\_dfu\_metadata\_status](structbt__mesh__dfu__metadata__status.md) \*rsp) |
|  | Perform a metadata check for the given DFU image slot. |
| int | [bt\_mesh\_dfu\_cli\_status\_get](group__bt__mesh__dfu__cli.md#gab754da11705a2d6a24ec828aa7862579) (struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, struct [bt\_mesh\_dfu\_target\_status](structbt__mesh__dfu__target__status.md) \*rsp) |
|  | Get the status of a Target node. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_dfu\_cli\_timeout\_get](group__bt__mesh__dfu__cli.md#ga3dd10bd1e8673973fd6db98d3ebda354) (void) |
|  | Get the current procedure timeout value. |
| void | [bt\_mesh\_dfu\_cli\_timeout\_set](group__bt__mesh__dfu__cli.md#ga603adf5b40b6e382c9035c9f2bad99a9) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the procedure timeout value. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfu\_cli.h](dfu__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
