---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__dfu__srv.html
original_path: doxygen/html/group__bt__mesh__dfu__srv.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Firmware Update Server model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md)

API for the Bluetooth Mesh Firmware Update Server model.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dfu\_srv\_cb](structbt__mesh__dfu__srv__cb.md) |
|  | Firmware Update Server event callbacks. [More...](structbt__mesh__dfu__srv__cb.md#details) |
| struct | [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) |
|  | Firmware Update Server instance. [More...](structbt__mesh__dfu__srv.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_DFU\_SRV\_INIT](#ga8467cd5241dfdcd7add718bbaae6fa60)(\_handlers, \_imgs, \_img\_count) |
|  | Initialization parameters for [Firmware Update Server model](group__bt__mesh__dfu__srv.md "Firmware Update Server model"). |
| #define | [BT\_MESH\_MODEL\_DFU\_SRV](#gafdf78cc0f99668d38df4f29138392632)(\_srv) |
|  | Firmware Update Server model entry. |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_dfu\_srv\_verified](#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Accept the received DFU transfer. |
| void | [bt\_mesh\_dfu\_srv\_rejected](#ga77142a1f3cfe2ff1d53332114f977b38) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Reject the received DFU transfer. |
| void | [bt\_mesh\_dfu\_srv\_cancel](#gaf5a00dd89faf52cd7797c54c572e1211) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Cancel the ongoing DFU transfer. |
| void | [bt\_mesh\_dfu\_srv\_applied](#ga45aef92fe1de4c45ccb5369c1f5222ee) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Confirm that the received DFU transfer was applied. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_dfu\_srv\_is\_busy](#ga94107fb1ca9207fc6918eae1fb1b3755) (const struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Check if the Firmware Update Server is busy processing a transfer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_dfu\_srv\_progress](#ga9f125ace97a40f060e0d8c59fd49f514) (const struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Get the progress of the current DFU procedure, in percent. |

## Detailed Description

API for the Bluetooth Mesh Firmware Update Server model.

## Macro Definition Documentation

## [◆ ](#ga8467cd5241dfdcd7add718bbaae6fa60)BT\_MESH\_DFU\_SRV\_INIT

| #define BT\_MESH\_DFU\_SRV\_INIT | ( |  | *\_handlers*, |
| --- | --- | --- | --- |
|  |  |  | *\_imgs*, |
|  |  |  | *\_img\_count* ) |

`#include <[dfu_srv.h](dfu__srv_8h.md)>`

**Value:**

{ \

.blob = { .cb = &\_bt\_mesh\_dfu\_srv\_blob\_cb }, .cb = \_handlers, \

.imgs = \_imgs, .img\_count = \_img\_count, \

}

Initialization parameters for [Firmware Update Server model](group__bt__mesh__dfu__srv.md "Firmware Update Server model").

Parameters
:   | \_handlers | DFU handler function structure. |
    | --- | --- |
    | \_imgs | List of [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md "bt_mesh_dfu_img") managed by this Server. |
    | \_img\_count | Number of DFU images managed by this Server. |

## [◆ ](#gafdf78cc0f99668d38df4f29138392632)BT\_MESH\_MODEL\_DFU\_SRV

| #define BT\_MESH\_MODEL\_DFU\_SRV | ( |  | *\_srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_srv.h](dfu__srv_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_BLOB\_SRV](group__bt__mesh__blob__srv.md#gad9db3253c13d50cfb6c89dff881dbfe9)(&(\_srv)->blob), \

BT\_MESH\_MODEL\_CB([BT\_MESH\_MODEL\_ID\_DFU\_SRV](group__bt__mesh__access.md#ga0215c2c8cd16ab6536ea243864f9604e), \_bt\_mesh\_dfu\_srv\_op, NULL, \

\_srv, &\_bt\_mesh\_dfu\_srv\_cb)

[BT\_MESH\_MODEL\_ID\_DFU\_SRV](group__bt__mesh__access.md#ga0215c2c8cd16ab6536ea243864f9604e)

#define BT\_MESH\_MODEL\_ID\_DFU\_SRV

Firmware Update Server.

**Definition** access.h:347

[BT\_MESH\_MODEL\_BLOB\_SRV](group__bt__mesh__blob__srv.md#gad9db3253c13d50cfb6c89dff881dbfe9)

#define BT\_MESH\_MODEL\_BLOB\_SRV(\_srv)

BLOB Transfer Server model composition data entry.

**Definition** blob\_srv.h:43

Firmware Update Server model entry.

Parameters
:   | \_srv | Pointer to a [Firmware Update Server model](group__bt__mesh__dfu__srv.md "Firmware Update Server model") instance. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga45aef92fe1de4c45ccb5369c1f5222ee)bt\_mesh\_dfu\_srv\_applied()

| void bt\_mesh\_dfu\_srv\_applied | ( | struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_srv.h](dfu__srv_8h.md)>`

Confirm that the received DFU transfer was applied.

Should be called as a result of the [bt\_mesh\_dfu\_srv\_cb::apply](structbt__mesh__dfu__srv__cb.md#afe4b6ca9f56938695addba6ecc18bb4b "bt_mesh_dfu_srv_cb::apply") callback.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |

## [◆ ](#gaf5a00dd89faf52cd7797c54c572e1211)bt\_mesh\_dfu\_srv\_cancel()

| void bt\_mesh\_dfu\_srv\_cancel | ( | struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_srv.h](dfu__srv_8h.md)>`

Cancel the ongoing DFU transfer.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |

## [◆ ](#ga94107fb1ca9207fc6918eae1fb1b3755)bt\_mesh\_dfu\_srv\_is\_busy()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_dfu\_srv\_is\_busy | ( | const struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_srv.h](dfu__srv_8h.md)>`

Check if the Firmware Update Server is busy processing a transfer.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |

Returns
:   true if a DFU procedure is in progress, false otherwise.

## [◆ ](#ga9f125ace97a40f060e0d8c59fd49f514)bt\_mesh\_dfu\_srv\_progress()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_srv\_progress | ( | const struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_srv.h](dfu__srv_8h.md)>`

Get the progress of the current DFU procedure, in percent.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |

Returns
:   The current transfer progress in percent.

## [◆ ](#ga77142a1f3cfe2ff1d53332114f977b38)bt\_mesh\_dfu\_srv\_rejected()

| void bt\_mesh\_dfu\_srv\_rejected | ( | struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_srv.h](dfu__srv_8h.md)>`

Reject the received DFU transfer.

Should be called at the end of a successful DFU transfer.

If the DFU transfer completes successfully, the application should verify the image validity (including any image authentication or integrity checks), and call this function if one of the checks fail.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |

## [◆ ](#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)bt\_mesh\_dfu\_srv\_verified()

| void bt\_mesh\_dfu\_srv\_verified | ( | struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \* | *srv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dfu_srv.h](dfu__srv_8h.md)>`

Accept the received DFU transfer.

Should be called at the end of a successful DFU transfer.

If the DFU transfer completes successfully, the application should verify the image validity (including any image authentication or integrity checks), and call this function if the image is ready to be applied.

Parameters
:   | srv | Firmware Update Server instance. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
