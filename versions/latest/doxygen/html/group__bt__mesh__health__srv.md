---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__health__srv.html
original_path: doxygen/html/group__bt__mesh__health__srv.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Health Server Model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Health Server Model.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md) |
|  | Callback function for the Health Server model. [More...](structbt__mesh__health__srv__cb.md#details) |
| struct | [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md) |
|  | Mesh Health Server Model Context. [More...](structbt__mesh__health__srv.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_HEALTH\_PUB\_DEFINE](#ga35c500e915092ec365862b11e76f92ad)(\_name, \_max\_faults) |
|  | A helper to define a health publication context. |
| #define | [BT\_MESH\_MODEL\_HEALTH\_SRV](#ga0b1dbf65d378d563fb90a867ea857b99)(srv, pub) |
|  | Define a new health server model. |
| #define | [BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID](#ga240e4632cdf7c425d4beec3c6a290306)   0x0001 |
|  | Health Test Information Metadata ID. |
| #define | [BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA](#ga37a52318699187a92de82d45dccf325d)(tests) |
| #define | [BT\_MESH\_HEALTH\_TEST\_INFO](#ga29ca643e811a2c4f03eca7fed8d1cf4d)(cid, tests...) |
|  | Define a Health Test Info Metadata array. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_health\_srv\_fault\_update](#gad04789eb167b61d5ff19827c560ceb6e) (const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem) |
|  | Notify the stack that the fault array state of the given element has changed. |

## Detailed Description

Health Server Model.

## Macro Definition Documentation

## [◆ ](#ga35c500e915092ec365862b11e76f92ad)BT\_MESH\_HEALTH\_PUB\_DEFINE

| #define BT\_MESH\_HEALTH\_PUB\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_max\_faults* ) |

`#include <[health_srv.h](health__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_PUB\_DEFINE](group__bt__mesh__access.md#ga8334ff2da1f0dc3ab2fc914059c33622)(\_name, NULL, (1 + 3 + (\_max\_faults)))

[BT\_MESH\_MODEL\_PUB\_DEFINE](group__bt__mesh__access.md#ga8334ff2da1f0dc3ab2fc914059c33622)

#define BT\_MESH\_MODEL\_PUB\_DEFINE(\_name, \_update, \_msg\_len)

Define a model publication context.

**Definition** access.h:760

A helper to define a health publication context.

Parameters
:   | \_name | Name given to the publication context variable. |
    | --- | --- |
    | \_max\_faults | Maximum number of faults the element can have. |

## [◆ ](#ga29ca643e811a2c4f03eca7fed8d1cf4d)BT\_MESH\_HEALTH\_TEST\_INFO

| #define BT\_MESH\_HEALTH\_TEST\_INFO | ( |  | *cid*, |
| --- | --- | --- | --- |
|  |  |  | *tests...* ) |

`#include <[health_srv.h](health__srv_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)(cid), sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[]){ tests }), tests

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)

#define BT\_BYTES\_LIST\_LE16(\_v)

Encode 16-bit value into array values in little-endian format.

**Definition** byteorder.h:36

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Define a Health Test Info Metadata array.

Parameters
:   | cid | Company ID of the Health Test suite. |
    | --- | --- |
    | tests | A comma separated list of tests. |

Returns
:   A comma separated list of values that make Health Test Info Metadata

## [◆ ](#ga37a52318699187a92de82d45dccf325d)BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA

| #define BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA | ( |  | *tests* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[health_srv.h](health__srv_8h.md)>`

**Value:**

{ \

.len = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(tests), \

.id = [BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID](#ga240e4632cdf7c425d4beec3c6a290306), \

.data = tests, \

}

[BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID](#ga240e4632cdf7c425d4beec3c6a290306)

#define BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID

Health Test Information Metadata ID.

**Definition** health\_srv.h:191

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:124

## [◆ ](#ga240e4632cdf7c425d4beec3c6a290306)BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID

| #define BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID   0x0001 |
| --- |

`#include <[health_srv.h](health__srv_8h.md)>`

Health Test Information Metadata ID.

## [◆ ](#ga0b1dbf65d378d563fb90a867ea857b99)BT\_MESH\_MODEL\_HEALTH\_SRV

| #define BT\_MESH\_MODEL\_HEALTH\_SRV | ( |  | *srv*, |
| --- | --- | --- | --- |
|  |  |  | *pub* ) |

`#include <[health_srv.h](health__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_HEALTH\_SRV](group__bt__mesh__access.md#ga6416216348d7186f91175ca50bb8c903), bt\_mesh\_health\_srv\_op, \

pub, srv, &[bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md))

[BT\_MESH\_MODEL\_ID\_HEALTH\_SRV](group__bt__mesh__access.md#ga6416216348d7186f91175ca50bb8c903)

#define BT\_MESH\_MODEL\_ID\_HEALTH\_SRV

Health Server.

**Definition** access.h:183

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:491

[bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md)

Callback function for the Health Server model.

**Definition** health\_srv.h:28

Define a new health server model.

Note that this API needs to be repeated for each element that the application wants to have a health server model on. Each instance also needs a unique [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md "Mesh Health Server Model Context.") and [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md "Model publication context.") context.

Parameters
:   | srv | Pointer to a unique struct [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md "Mesh Health Server Model Context."). |
    | --- | --- |
    | pub | Pointer to a unique struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md "Model publication context."). |

Returns
:   New mesh model instance.

## Function Documentation

## [◆ ](#gad04789eb167b61d5ff19827c560ceb6e)bt\_mesh\_health\_srv\_fault\_update()

| int bt\_mesh\_health\_srv\_fault\_update | ( | const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \* | *elem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[health_srv.h](health__srv_8h.md)>`

Notify the stack that the fault array state of the given element has changed.

This prompts the Health server on this element to publish the current fault array if periodic publishing is disabled.

Parameters
:   | elem | Element to update the fault state of. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
