---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__blob__cli__cb.html
original_path: doxygen/html/structbt__mesh__blob__cli__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_cli\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md)

Event handler callbacks for the BLOB Transfer Client model.
[More...](#details)

`#include <[blob_cli.h](blob__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [caps](#a58e749cadeb464299495ee74456c592c) )(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) \*caps) |
|  | Capabilities retrieval completion callback. |
| void(\* | [lost\_target](#a26a5ebe87db105900b150f71d770234d) )(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) \*target, enum [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) reason) |
|  | Target node loss callback. |
| void(\* | [suspended](#a154a3308167eda4cd93ac28e379c52bc) )(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Transfer is suspended. |
| void(\* | [end](#a60bc49eab376b055a8c21099f86fdde7) )(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) success) |
|  | Transfer end callback. |
| void(\* | [xfer\_progress](#a4b01ef0ab0a367739a75751b57149546) )(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) \*target, const struct [bt\_mesh\_blob\_xfer\_info](structbt__mesh__blob__xfer__info.md) \*info) |
|  | Transfer progress callback. |
| void(\* | [xfer\_progress\_complete](#abb4a4d4d24bef076aad7ae56b08d23ed) )(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | End of Get Transfer Progress procedure. |

## Detailed Description

Event handler callbacks for the BLOB Transfer Client model.

All handlers are optional.

## Field Documentation

## [◆ ](#a58e749cadeb464299495ee74456c592c)caps

| void(\* bt\_mesh\_blob\_cli\_cb::caps) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) \*caps) |
| --- |

Capabilities retrieval completion callback.

Called when the capabilities retrieval procedure completes, indicating that a common set of acceptable transfer parameters have been established for the given list of Target nodes. All compatible Target nodes have status code [BT\_MESH\_BLOB\_SUCCESS](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d "BT_MESH_BLOB_SUCCESS").

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |
    | [caps](#a58e749cadeb464299495ee74456c592c) | Safe transfer capabilities if the transfer capabilities of at least one Target node has satisfied the Client, or NULL otherwise. |

## [◆ ](#a60bc49eab376b055a8c21099f86fdde7)end

| void(\* bt\_mesh\_blob\_cli\_cb::end) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) success) |
| --- |

Transfer end callback.

Called when the transfer ends.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |
    | xfer | Completed transfer. |
    | success | Status of the transfer. Is `true` if at least one Target node received the whole transfer. |

## [◆ ](#a26a5ebe87db105900b150f71d770234d)lost\_target

| void(\* bt\_mesh\_blob\_cli\_cb::lost\_target) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) \*target, enum [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) reason) |
| --- |

Target node loss callback.

Called whenever a Target node has been lost due to some error in the transfer. Losing a Target node is not considered a fatal error for the Client until all Target nodes have been lost.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |
    | target | Target node that was lost. |
    | reason | Reason for the Target node loss. |

## [◆ ](#a154a3308167eda4cd93ac28e379c52bc)suspended

| void(\* bt\_mesh\_blob\_cli\_cb::suspended) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
| --- |

Transfer is suspended.

Called when the transfer is suspended due to response timeout from all Target nodes.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |

## [◆ ](#a4b01ef0ab0a367739a75751b57149546)xfer\_progress

| void(\* bt\_mesh\_blob\_cli\_cb::xfer\_progress) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) \*target, const struct [bt\_mesh\_blob\_xfer\_info](structbt__mesh__blob__xfer__info.md) \*info) |
| --- |

Transfer progress callback.

The content of `info` is invalidated upon exit from the callback. Therefore it needs to be copied if it is planned to be used later.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |
    | target | Target node that responded to the request. |
    | info | BLOB transfer information. |

## [◆ ](#abb4a4d4d24bef076aad7ae56b08d23ed)xfer\_progress\_complete

| void(\* bt\_mesh\_blob\_cli\_cb::xfer\_progress\_complete) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
| --- |

End of Get Transfer Progress procedure.

Called when all Target nodes have responded or the procedure timed-out.

Parameters
:   | cli | BLOB Transfer Client instance. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_cli.h](blob__cli_8h_source.md)

- [bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
