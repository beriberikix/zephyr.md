---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__hb__cb.html
original_path: doxygen/html/structbt__mesh__hb__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_hb\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Heartbeat](group__bt__mesh__heartbeat.md)

Heartbeat callback structure.
[More...](#details)

`#include <[heartbeat.h](heartbeat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [recv](#aa3b85249e1a40842c0f937385a72103f) )(const struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*sub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hops, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) feat) |
|  | Receive callback for heartbeats. |
| void(\* | [sub\_end](#aa979e024174fa19f047a26f94b54a9d3) )(const struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*sub) |
|  | Subscription end callback for heartbeats. |
| void(\* | [pub\_sent](#acc5559541f53e2987899433d4d434557) )(const struct [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) \*pub) |
|  | Publication sent callback for heartbeats. |

## Detailed Description

Heartbeat callback structure.

## Field Documentation

## [◆ ](#acc5559541f53e2987899433d4d434557)pub\_sent

| void(\* bt\_mesh\_hb\_cb::pub\_sent) (const struct [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) \*pub) |
| --- |

Publication sent callback for heartbeats.

Gets called when the heartbeat is successfully published.

Parameters
:   | pub | Current Heartbeat publication parameters. |
    | --- | --- |

## [◆ ](#aa3b85249e1a40842c0f937385a72103f)recv

| void(\* bt\_mesh\_hb\_cb::recv) (const struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*sub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hops, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) feat) |
| --- |

Receive callback for heartbeats.

Gets called on every received Heartbeat that matches the current Heartbeat subscription parameters.

Parameters
:   | sub | Current Heartbeat subscription parameters. |
    | --- | --- |
    | hops | The number of hops the Heartbeat was received with. |
    | feat | The feature set of the publishing node. The value is a bitmap of [BT\_MESH\_FEAT\_RELAY](group__bt__mesh.md#gac588eefe83db94784a420ce063f02b55 "BT_MESH_FEAT_RELAY"), [BT\_MESH\_FEAT\_PROXY](group__bt__mesh.md#gaee648ce202316c56d4d588cb0ad5aeb4 "BT_MESH_FEAT_PROXY"), [BT\_MESH\_FEAT\_FRIEND](group__bt__mesh.md#ga8f27086b3bc3c4a6e14621836f9f8e80 "BT_MESH_FEAT_FRIEND") and [BT\_MESH\_FEAT\_LOW\_POWER](group__bt__mesh.md#gaad71a36c82b4e4d3fa334ecff5cc0171 "BT_MESH_FEAT_LOW_POWER"). |

## [◆ ](#aa979e024174fa19f047a26f94b54a9d3)sub\_end

| void(\* bt\_mesh\_hb\_cb::sub\_end) (const struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*sub) |
| --- |

Subscription end callback for heartbeats.

Gets called when the subscription period ends, providing a summary of the received heartbeat messages.

Parameters
:   | sub | Current Heartbeat subscription parameters. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[heartbeat.h](heartbeat_8h_source.md)

- [bt\_mesh\_hb\_cb](structbt__mesh__hb__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
