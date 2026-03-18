---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__dfd__srv.html
original_path: doxygen/html/group__bt__mesh__dfd__srv.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Firmware Distribution Server model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Firmware Distribution models](group__bt__mesh__dfd.md)

API for the Firmware Distribution Server model.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dfd\_srv\_cb](structbt__mesh__dfd__srv__cb.md) |
|  | Firmware Distribution Server callbacks: [More...](structbt__mesh__dfd__srv__cb.md#details) |
| struct | [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) |
|  | Firmware Distribution Server instance. [More...](structbt__mesh__dfd__srv.md#details) |

| Macros | |
| --- | --- |
| #define | [CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX](#ga126e2d4df8f58b7de36da46c14b2c804)   0 |
| #define | [CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_MAX\_SIZE](#gab26590917c9de6edaccf07540c88f7c1)   0 |
| #define | [CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_SPACE](#ga394c367492c72f66231b5cf3e2789f5f)   0 |
| #define | [BT\_MESH\_DFD\_SRV\_INIT](#ga20b1232269b2e859608c21e84305196c)(\_cb) |
|  | Initialization parameters for the [Firmware Distribution Server model](group__bt__mesh__dfd__srv.md "Firmware Distribution Server model"). |
| #define | [BT\_MESH\_MODEL\_DFD\_SRV](#ga27457d4d72119ab080828359d43ad6cf)(\_srv) |
|  | Firmware Distribution Server model Composition Data entry. |

## Detailed Description

API for the Firmware Distribution Server model.

## Macro Definition Documentation

## [◆ ](#ga20b1232269b2e859608c21e84305196c)BT\_MESH\_DFD\_SRV\_INIT

| #define BT\_MESH\_DFD\_SRV\_INIT | ( |  | *\_cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfd_srv.h](dfd__srv_8h.md)>`

**Value:**

{ \

.cb = \_cb, \

.dfu = [BT\_MESH\_DFU\_CLI\_INIT](group__bt__mesh__dfu__cli.md#ga0b10a95f9b7c806bfd8649280f535c96)(&\_bt\_mesh\_dfd\_srv\_dfu\_cb), \

.upload = { \

.blob = { .cb = &\_bt\_mesh\_dfd\_srv\_blob\_cb }, \

}, \

}

[BT\_MESH\_DFU\_CLI\_INIT](group__bt__mesh__dfu__cli.md#ga0b10a95f9b7c806bfd8649280f535c96)

#define BT\_MESH\_DFU\_CLI\_INIT(\_handlers)

Initialization parameters for the Firmware Uppdate Client model.

**Definition** dfu\_cli.h:36

Initialization parameters for the [Firmware Distribution Server model](group__bt__mesh__dfd__srv.md "Firmware Distribution Server model").

Parameters
:   | [in] | \_cb | Pointer to a [bt\_mesh\_dfd\_srv\_cb](structbt__mesh__dfd__srv__cb.md "bt_mesh_dfd_srv_cb") instance. |
    | --- | --- | --- |

## [◆ ](#ga27457d4d72119ab080828359d43ad6cf)BT\_MESH\_MODEL\_DFD\_SRV

| #define BT\_MESH\_MODEL\_DFD\_SRV | ( |  | *\_srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfd_srv.h](dfd__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_DFU\_CLI](group__bt__mesh__dfu__cli.md#gadee3710bb46d907a51232ca42cca7c2d)(&(\_srv)->dfu), \

BT\_MESH\_MODEL\_BLOB\_SRV(&(\_srv)->upload.blob), \

BT\_MESH\_MODEL\_CB([BT\_MESH\_MODEL\_ID\_DFD\_SRV](group__bt__mesh__access.md#gaf4309dea32d05274f8f3a6ea45faba38), \_bt\_mesh\_dfd\_srv\_op, NULL, \

\_srv, &\_bt\_mesh\_dfd\_srv\_cb)

[BT\_MESH\_MODEL\_ID\_DFD\_SRV](group__bt__mesh__access.md#gaf4309dea32d05274f8f3a6ea45faba38)

#define BT\_MESH\_MODEL\_ID\_DFD\_SRV

Firmware Distribution Server.

**Definition** access.h:351

[BT\_MESH\_MODEL\_DFU\_CLI](group__bt__mesh__dfu__cli.md#gadee3710bb46d907a51232ca42cca7c2d)

#define BT\_MESH\_MODEL\_DFU\_CLI(\_cli)

Firmware Update Client model Composition Data entry.

**Definition** dfu\_cli.h:48

Firmware Distribution Server model Composition Data entry.

Parameters
:   | \_srv | Pointer to a [Firmware Distribution Server model](group__bt__mesh__dfd__srv.md "Firmware Distribution Server model") instance. |
    | --- | --- |

## [◆ ](#gab26590917c9de6edaccf07540c88f7c1)CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_MAX\_SIZE

| #define CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_MAX\_SIZE   0 |
| --- |

`#include <[dfd_srv.h](dfd__srv_8h.md)>`

## [◆ ](#ga394c367492c72f66231b5cf3e2789f5f)CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_SPACE

| #define CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_SPACE   0 |
| --- |

`#include <[dfd_srv.h](dfd__srv_8h.md)>`

## [◆ ](#ga126e2d4df8f58b7de36da46c14b2c804)CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX

| #define CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX   0 |
| --- |

`#include <[dfd_srv.h](dfd__srv_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
