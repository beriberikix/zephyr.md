---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__broadcast__assistant__cb.html
original_path: doxygen/html/structbt__bap__broadcast__assistant__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_broadcast\_assistant\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Struct to hold the Basic Audio Profile Broadcast Assistant callbacks.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [discover](#a01ad0a89db9041670f6a68d6f1680988) )(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_state\_count) |
|  | Callback function for bt\_bap\_broadcast\_assistant\_discover. |
| void(\* | [scan](#ab88d98b1e742ccd36aac69069ebf3f61) )(const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) broadcast\_id) |
|  | Callback function for Broadcast Audio Scan Service client scan results. |
| void(\* | [recv\_state](#a629ff4299b8ae5bcbddf28338caddfd0) )(struct bt\_conn \*conn, int err, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Callback function for when a receive state is read or updated. |
| void(\* | [recv\_state\_removed](#af3fb53d95cdc7ba202657e4c54e0b2b8) )(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id) |
|  | Callback function for when a receive state is removed. |
| void(\* | [scan\_start](#ad2bdfcc0147a751910d82232a77e34f8) )(struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_bap\_broadcast\_assistant\_scan\_start()](group__bt__bap.md#ga98ac067e66d263aa41fc6f8df6bb9126 "Scan start for BISes for a remote server."). |
| void(\* | [scan\_stop](#a80296a38e664aabff7ec27e007c59e95) )(struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_bap\_broadcast\_assistant\_scan\_stop()](group__bt__bap.md#ga76cae35df980b78a10551811050b2760 "Stop remote scanning for BISes for a server."). |
| void(\* | [add\_src](#ad909b9e6e3c35be10a29ee5a4b7213fb) )(struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_bap\_broadcast\_assistant\_add\_src()](group__bt__bap.md#gac93cb4cab33d0b937e752bc0b71cad9e "Add a source on the server."). |
| void(\* | [mod\_src](#ab24e3ecb9764ca833524b787126b8c2c) )(struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_bap\_broadcast\_assistant\_mod\_src()](group__bt__bap.md#gaa9c292a7dcb470926d8d7d4be699a0c7 "Modify a source on the server."). |
| void(\* | [broadcast\_code](#a09de9cb86dad76b485ff52257a0c68dc) )(struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_bap\_broadcast\_assistant\_set\_broadcast\_code()](group__bt__bap.md#gabcec07689c13a996bcb9d2d417347dbb "Set a broadcast code to the specified receive state."). |
| void(\* | [rem\_src](#af0cf259088cd793152390b21813a9481) )(struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_bap\_broadcast\_assistant\_rem\_src()](group__bt__bap.md#ga09785690db551677a043fcaa2fdb7f29 "Remove a source from the server."). |

## Detailed Description

Struct to hold the Basic Audio Profile Broadcast Assistant callbacks.

These can be registered for usage with [bt\_bap\_broadcast\_assistant\_register\_cb()](group__bt__bap.md#gabab24c44e9833029965475ad7b149e6e "Registers the callbacks used by Broadcast Audio Scan Service client.").

## Field Documentation

## [◆ ](#ad909b9e6e3c35be10a29ee5a4b7213fb)add\_src

| void(\* bt\_bap\_broadcast\_assistant\_cb::add\_src) (struct bt\_conn \*conn, int err) |
| --- |

Callback function for [bt\_bap\_broadcast\_assistant\_add\_src()](group__bt__bap.md#gac93cb4cab33d0b937e752bc0b71cad9e "Add a source on the server.").

Parameters
:   | conn | The connection to the peer device. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on fail. |

## [◆ ](#a09de9cb86dad76b485ff52257a0c68dc)broadcast\_code

| void(\* bt\_bap\_broadcast\_assistant\_cb::broadcast\_code) (struct bt\_conn \*conn, int err) |
| --- |

Callback function for [bt\_bap\_broadcast\_assistant\_set\_broadcast\_code()](group__bt__bap.md#gabcec07689c13a996bcb9d2d417347dbb "Set a broadcast code to the specified receive state.").

Parameters
:   | conn | The connection to the peer device. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on fail. |

## [◆ ](#a01ad0a89db9041670f6a68d6f1680988)discover

| void(\* bt\_bap\_broadcast\_assistant\_cb::discover) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) recv\_state\_count) |
| --- |

Callback function for bt\_bap\_broadcast\_assistant\_discover.

Parameters
:   | conn | The connection that was used to discover Broadcast Audio Scan Service. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or ERRNO on fail. |
    | recv\_state\_count | Number of receive states on the server. |

## [◆ ](#ab24e3ecb9764ca833524b787126b8c2c)mod\_src

| void(\* bt\_bap\_broadcast\_assistant\_cb::mod\_src) (struct bt\_conn \*conn, int err) |
| --- |

Callback function for [bt\_bap\_broadcast\_assistant\_mod\_src()](group__bt__bap.md#gaa9c292a7dcb470926d8d7d4be699a0c7 "Modify a source on the server.").

Parameters
:   | conn | The connection to the peer device. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on fail. |

## [◆ ](#a629ff4299b8ae5bcbddf28338caddfd0)recv\_state

| void(\* bt\_bap\_broadcast\_assistant\_cb::recv\_state) (struct bt\_conn \*conn, int err, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Callback function for when a receive state is read or updated.

Called whenever a receive state is read or updated.

Parameters
:   | conn | The connection to the Broadcast Audio Scan Service server. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on fail. |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The receive state or NULL if the receive state is empty. |

## [◆ ](#af3fb53d95cdc7ba202657e4c54e0b2b8)recv\_state\_removed

| void(\* bt\_bap\_broadcast\_assistant\_cb::recv\_state\_removed) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id) |
| --- |

Callback function for when a receive state is removed.

Parameters
:   | conn | The connection to the Broadcast Audio Scan Service server. |
    | --- | --- |
    | src\_id | The receive state. |

## [◆ ](#af0cf259088cd793152390b21813a9481)rem\_src

| void(\* bt\_bap\_broadcast\_assistant\_cb::rem\_src) (struct bt\_conn \*conn, int err) |
| --- |

Callback function for [bt\_bap\_broadcast\_assistant\_rem\_src()](group__bt__bap.md#ga09785690db551677a043fcaa2fdb7f29 "Remove a source from the server.").

Parameters
:   | conn | The connection to the peer device. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on fail. |

## [◆ ](#ab88d98b1e742ccd36aac69069ebf3f61)scan

| void(\* bt\_bap\_broadcast\_assistant\_cb::scan) (const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) broadcast\_id) |
| --- |

Callback function for Broadcast Audio Scan Service client scan results.

Called when the scanner finds an advertiser that advertises the BT\_UUID\_BROADCAST\_AUDIO UUID.

Parameters
:   | info | Advertiser information. |
    | --- | --- |
    | broadcast\_id | 24-bit broadcast ID. |

## [◆ ](#ad2bdfcc0147a751910d82232a77e34f8)scan\_start

| void(\* bt\_bap\_broadcast\_assistant\_cb::scan\_start) (struct bt\_conn \*conn, int err) |
| --- |

Callback function for [bt\_bap\_broadcast\_assistant\_scan\_start()](group__bt__bap.md#ga98ac067e66d263aa41fc6f8df6bb9126 "Scan start for BISes for a remote server.").

Parameters
:   | conn | The connection to the peer device. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on fail. |

## [◆ ](#a80296a38e664aabff7ec27e007c59e95)scan\_stop

| void(\* bt\_bap\_broadcast\_assistant\_cb::scan\_stop) (struct bt\_conn \*conn, int err) |
| --- |

Callback function for [bt\_bap\_broadcast\_assistant\_scan\_stop()](group__bt__bap.md#ga76cae35df980b78a10551811050b2760 "Stop remote scanning for BISes for a server.").

Parameters
:   | conn | The connection to the peer device. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on fail. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
