---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__blob__srv.html
original_path: doxygen/html/group__bt__mesh__blob__srv.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh BLOB Transfer Server model API

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md) |
|  | BLOB Transfer Server model event handlers. [More...](structbt__mesh__blob__srv__cb.md#details) |
| struct | [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) |
|  | BLOB Transfer Server instance. [More...](structbt__mesh__blob__srv.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_BLOB\_BLOCKS\_MAX](#gaae3dfbf15f33739bc0a42c924de99cba)   1 |
|  | Max number of blocks in a single transfer. |
| #define | [BT\_MESH\_MODEL\_BLOB\_SRV](#gad9db3253c13d50cfb6c89dff881dbfe9)(\_srv) |
|  | BLOB Transfer Server model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_blob\_srv\_recv](#ga5d35f13eeb6f7a1fb252e8fb905e9cb3) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout\_base) |
|  | Prepare BLOB Transfer Server for an incoming transfer. |
| int | [bt\_mesh\_blob\_srv\_cancel](#gae8739e96f2157f588072e91b51891835) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
|  | Cancel the current BLOB transfer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_blob\_srv\_is\_busy](#gaa7a253c9a577eaa1307bc0e6b93a3d66) (const struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
|  | Get the current state of the BLOB Transfer Server. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_blob\_srv\_progress](#ga674b59ff721575539818ef74e8d1b91c) (const struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
|  | Get the current progress of the active transfer in percent. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaae3dfbf15f33739bc0a42c924de99cba)BT\_MESH\_BLOB\_BLOCKS\_MAX

| #define BT\_MESH\_BLOB\_BLOCKS\_MAX   1 |
| --- |

`#include <[blob_srv.h](blob__srv_8h.md)>`

Max number of blocks in a single transfer.

## [◆ ](#gad9db3253c13d50cfb6c89dff881dbfe9)BT\_MESH\_MODEL\_BLOB\_SRV

| #define BT\_MESH\_MODEL\_BLOB\_SRV | ( |  | *\_srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_srv.h](blob__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_BLOB\_SRV](group__bt__mesh__access.md#gae85d4cf7aad4e94582c24f79d6f60904), \_bt\_mesh\_blob\_srv\_op, \

NULL, \_srv, &\_bt\_mesh\_blob\_srv\_cb)

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

[BT\_MESH\_MODEL\_ID\_BLOB\_SRV](group__bt__mesh__access.md#gae85d4cf7aad4e94582c24f79d6f60904)

#define BT\_MESH\_MODEL\_ID\_BLOB\_SRV

BLOB Transfer Server.

**Definition** access.h:335

BLOB Transfer Server model composition data entry.

Parameters
:   | \_srv | Pointer to a [Bluetooth Mesh BLOB Transfer Server model API](group__bt__mesh__blob__srv.md "Bluetooth Mesh BLOB Transfer Server model API") instance. |
    | --- | --- |

## Function Documentation

## [◆ ](#gae8739e96f2157f588072e91b51891835)bt\_mesh\_blob\_srv\_cancel()

| int bt\_mesh\_blob\_srv\_cancel | ( | struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_srv.h](blob__srv_8h.md)>`

Cancel the current BLOB transfer.

Tells the BLOB Transfer Client to drop this device from the list of Targets for the current transfer. Note that the client may continue sending the transfer to other Targets.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaa7a253c9a577eaa1307bc0e6b93a3d66)bt\_mesh\_blob\_srv\_is\_busy()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_blob\_srv\_is\_busy | ( | const struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_srv.h](blob__srv_8h.md)>`

Get the current state of the BLOB Transfer Server.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |

Returns
:   true if the BLOB Transfer Server is currently participating in a transfer, false otherwise.

## [◆ ](#ga674b59ff721575539818ef74e8d1b91c)bt\_mesh\_blob\_srv\_progress()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_srv\_progress | ( | const struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[blob_srv.h](blob__srv_8h.md)>`

Get the current progress of the active transfer in percent.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |

Returns
:   The current transfer progress, or 0 if no transfer is active.

## [◆ ](#ga5d35f13eeb6f7a1fb252e8fb905e9cb3)bt\_mesh\_blob\_srv\_recv()

| int bt\_mesh\_blob\_srv\_recv | ( | struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \* | *srv*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id*, |
|  |  | const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \* | *io*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ttl*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *timeout\_base* ) |

`#include <[blob_srv.h](blob__srv_8h.md)>`

Prepare BLOB Transfer Server for an incoming transfer.

Before a BLOB Transfer Server can receive a transfer, the transfer must be prepared through some application level mechanism. The BLOB Transfer Server will only accept incoming transfers with a matching BLOB ID.

Parameters
:   | srv | BLOB Transfer Server instance. |
    | --- | --- |
    | id | BLOB ID to accept. |
    | io | BLOB stream to write the incoming BLOB to. |
    | ttl | Time to live value to use in responses to the BLOB Transfer Client. |
    | timeout\_base | Extra time for the Client to respond in addition to the base 10 seconds, in 10-second increments. |

Returns
:   0 on success, or (negative) error code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
