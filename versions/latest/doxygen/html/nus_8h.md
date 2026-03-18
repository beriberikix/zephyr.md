---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nus_8h.html
original_path: doxygen/html/nus_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nus.h File Reference

`#include <[zephyr/bluetooth/uuid.h](uuid_8h_source.md)>`  
`#include <[zephyr/bluetooth/services/nus/inst.h](inst_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](nus_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_nus\_cb](structbt__nus__cb.md) |
|  | Callbacks for getting notified on NUS Service occurrences. [More...](structbt__nus__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_UUID\_NUS\_SRV\_VAL](#a8da4aaa9c77a537805c7b5bff7fc4aa6)   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0x6e400001, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e) |
|  | UUIDs of Nordic UART GATT Service. |
| #define | [BT\_UUID\_NUS\_RX\_CHAR\_VAL](#ada90c739cf936ec52008fcc4f272e207)   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0x6e400002, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e) |
| #define | [BT\_UUID\_NUS\_TX\_CHAR\_VAL](#a7636b61879884e6f6fc8e871ae09160b)   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0x6e400003, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e) |
| #define | [BT\_NUS\_INST\_DEFINE](#a54ba967101dc2a5515b9cfd1272c569b)(\_name) |
|  | Macro to define instance of NUS Service. |

| Functions | |
| --- | --- |
| int | [bt\_nus\_inst\_cb\_register](#a84cb19f07f861963c73614a04c0a375f) (struct [bt\_nus\_inst](structbt__nus__inst.md) \*inst, struct [bt\_nus\_cb](structbt__nus__cb.md) \*cb, void \*ctx) |
|  | NUS server Instance callback register. |
| int | [bt\_nus\_inst\_send](#a997453fc8108f64a95186b130ea68076) (struct bt\_conn \*conn, struct [bt\_nus\_inst](structbt__nus__inst.md) \*inst, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Send Data to NUS Instance. |
| static int | [bt\_nus\_cb\_register](#a1a28f3d267b34856450f60803eed485f) (struct [bt\_nus\_cb](structbt__nus__cb.md) \*cb, void \*ctx) |
|  | NUS server callback register. |
| static int | [bt\_nus\_send](#a950188897461f1c1f78ffbabeae1180a) (struct bt\_conn \*conn, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Send Data over NUS. |

## Macro Definition Documentation

## [◆ ](#a54ba967101dc2a5515b9cfd1272c569b)BT\_NUS\_INST\_DEFINE

| #define BT\_NUS\_INST\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

Z\_INTERNAL\_BT\_NUS\_INST\_DEFINE(\_name)

Macro to define instance of NUS Service.

It allows users to define multiple NUS instances, analogous to Serial endpoints, and use each one for different purposes. A default NUS instance may be defined through Kconfig.

## [◆ ](#ada90c739cf936ec52008fcc4f272e207)BT\_UUID\_NUS\_RX\_CHAR\_VAL

| #define BT\_UUID\_NUS\_RX\_CHAR\_VAL   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0x6e400002, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e) |
| --- |

## [◆ ](#a8da4aaa9c77a537805c7b5bff7fc4aa6)BT\_UUID\_NUS\_SRV\_VAL

| #define BT\_UUID\_NUS\_SRV\_VAL   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0x6e400001, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e) |
| --- |

UUIDs of Nordic UART GATT Service.

Service: 6e400001-b5a3-f393-e0a9-e50e24dcca9e RX Char: 6e400002-b5a3-f393-e0a9-e50e24dcca9e TX Char: 6e400003-b5a3-f393-e0a9-e50e24dcca9e

## [◆ ](#a7636b61879884e6f6fc8e871ae09160b)BT\_UUID\_NUS\_TX\_CHAR\_VAL

| #define BT\_UUID\_NUS\_TX\_CHAR\_VAL   [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(0x6e400003, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e) |
| --- |

## Function Documentation

## [◆ ](#a1a28f3d267b34856450f60803eed485f)bt\_nus\_cb\_register()

| | int bt\_nus\_cb\_register | ( | struct [bt\_nus\_cb](structbt__nus__cb.md) \* | *cb*, | | --- | --- | --- | --- | |  |  | void \* | *ctx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

NUS server callback register.

Parameters
:   | cb | Pointer to callbacks structure. Must be valid throughout the lifetime of the application. |
    | --- | --- |
    | ctx | User context to be provided through the callback. |

Returns
:   0 on success, negative error code if failed.
:   -EINVAL in case `cb` is NULL

## [◆ ](#a84cb19f07f861963c73614a04c0a375f)bt\_nus\_inst\_cb\_register()

| int bt\_nus\_inst\_cb\_register | ( | struct [bt\_nus\_inst](structbt__nus__inst.md) \* | *inst*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_nus\_cb](structbt__nus__cb.md) \* | *cb*, |
|  |  | void \* | *ctx* ) |

NUS server Instance callback register.

This function registers callbacks that will be called in certain events related to NUS.

Parameters
:   | inst | Pointer to instance of NUS service. NULL if using default instance. |
    | --- | --- |
    | cb | Pointer to callbacks structure. Must be valid throughout the lifetime of the application. |
    | ctx | User context to be provided through the callback. |

Returns
:   0 on success
:   -EINVAL in case `cb` is NULL

## [◆ ](#a997453fc8108f64a95186b130ea68076)bt\_nus\_inst\_send()

| int bt\_nus\_inst\_send | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_nus\_inst](structbt__nus__inst.md) \* | *inst*, |
|  |  | const void \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

Send Data to NUS Instance.

Note
:   This API sends the data to the specified peer.

Parameters
:   | conn | Connection object to send data to. NULL if notifying all peers. |
    | --- | --- |
    | inst | Pointer to instance of NUS service. NULL if using default instance. |
    | data | Pointer to buffer with bytes to send. |
    | len | Length in bytes of data to send. |

Returns
:   0 on success, negative error code if failed.
:   -EAGAIN when Bluetooth stack has not been enabled.
:   -ENOTCONN when either no connection has been established or no peers have subscribed.

## [◆ ](#a950188897461f1c1f78ffbabeae1180a)bt\_nus\_send()

| | int bt\_nus\_send | ( | struct bt\_conn \* | *conn*, | | --- | --- | --- | --- | |  |  | const void \* | *data*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Send Data over NUS.

Note
:   This API sends the data to the specified peer.

Parameters
:   | conn | Connection object to send data to. NULL if notifying all peers. |
    | --- | --- |
    | data | Pointer to buffer with bytes to send. |
    | len | Length in bytes of data to send. |

Returns
:   0 on success, negative error code if failed.
:   -EAGAIN when Bluetooth stack has not been enabled.
:   -ENOTCONN when either no connection has been established or no peers have subscribed.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [nus.h](nus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
