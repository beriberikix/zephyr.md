---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__gatt__cb.html
original_path: doxygen/html/structbt__gatt__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

GATT callback structure.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [att\_mtu\_updated](#a93fe1a626ab59c38ef56f02671f88980) )(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rx) |
|  | The maximum ATT MTU on a connection has changed. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#af9fcf17dcea66b1dee8cc5ecd625cdec) |

## Detailed Description

GATT callback structure.

## Field Documentation

## [◆ ](#a93fe1a626ab59c38ef56f02671f88980)att\_mtu\_updated

| void(\* bt\_gatt\_cb::att\_mtu\_updated) (struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rx) |
| --- |

The maximum ATT MTU on a connection has changed.

This callback notifies the application that the maximum TX or RX ATT MTU has increased.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | tx | Updated TX ATT MTU. |
    | rx | Updated RX ATT MTU. |

## [◆ ](#af9fcf17dcea66b1dee8cc5ecd625cdec)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_gatt\_cb::node |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_cb](structbt__gatt__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
