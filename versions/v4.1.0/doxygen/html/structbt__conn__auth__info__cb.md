---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__conn__auth__info__cb.html
original_path: doxygen/html/structbt__conn__auth__info__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_auth\_info\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Authenticated pairing information callback structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [pairing\_complete](#aea737700f2760de1ed26a721b5e860d2) )(struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bonded) |
|  | notify that pairing procedure was complete. |
| void(\* | [pairing\_failed](#ae7228bb82889eacebf67e1d4b3b23375) )(struct bt\_conn \*conn, enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) reason) |
|  | notify that pairing process has failed. |
| void(\* | [bond\_deleted](#af20b0d7fc5fd8399ad9368b3ef7067f8) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer) |
|  | Notify that bond has been deleted. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#afde62f2cdfb40b4154208f3c1c3dadc1) |
|  | Internally used field for list handling. |

## Detailed Description

Authenticated pairing information callback structure.

## Field Documentation

## [◆ ](#af20b0d7fc5fd8399ad9368b3ef7067f8)bond\_deleted

| void(\* bt\_conn\_auth\_info\_cb::bond\_deleted) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer) |
| --- |

Notify that bond has been deleted.

This callback notifies the application that the bond information for the remote peer has been deleted

Parameters
:   | id | Which local identity had the bond. |
    | --- | --- |
    | peer | Remote address. |

## [◆ ](#afde62f2cdfb40b4154208f3c1c3dadc1)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_conn\_auth\_info\_cb::node |
| --- |

Internally used field for list handling.

## [◆ ](#aea737700f2760de1ed26a721b5e860d2)pairing\_complete

| void(\* bt\_conn\_auth\_info\_cb::pairing\_complete) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bonded) |
| --- |

notify that pairing procedure was complete.

This callback notifies the application that the pairing procedure has been completed.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | bonded | Bond information has been distributed during the pairing procedure. |

## [◆ ](#ae7228bb82889eacebf67e1d4b3b23375)pairing\_failed

| void(\* bt\_conn\_auth\_info\_cb::pairing\_failed) (struct bt\_conn \*conn, enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) reason) |
| --- |

notify that pairing process has failed.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | reason | Pairing failed reason |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
