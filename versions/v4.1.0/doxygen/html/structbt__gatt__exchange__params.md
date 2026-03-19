---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__gatt__exchange__params.html
original_path: doxygen/html/structbt__gatt__exchange__params.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_exchange\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Client APIs](group__bt__gatt__client.md)

GATT Exchange MTU parameters.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [func](#a76f4d3e779da9c725914574ac2e22ad1) )(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \*params) |
|  | Callback for MTU exchange response. |

## Detailed Description

GATT Exchange MTU parameters.

Used with [bt\_gatt\_exchange\_mtu()](group__bt__gatt__client.md#ga0f41da23c6559a8254b04295aff8198d "bt_gatt_exchange_mtu()") to initiate an MTU exchange. The response is handled in the callback `func`, which is called upon completion from the 'config BT\_RECV\_CONTEXT' context.

`params` must remain valid until the callback executes.

## Field Documentation

## [◆ ](#a76f4d3e779da9c725914574ac2e22ad1)func

| void(\* bt\_gatt\_exchange\_params::func) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \*params) |
| --- |

Callback for MTU exchange response.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
