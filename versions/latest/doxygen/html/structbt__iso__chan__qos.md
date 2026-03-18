---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__iso__chan__qos.html
original_path: doxygen/html/structbt__iso__chan__qos.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_chan\_qos Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Channel QoS structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md) \* | [rx](#ac231434d1798f431c4fbac5a759784a5) |
|  | Channel Receiving QoS. |
| struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md) \* | [tx](#a47a99a6ccfa5f1e0c9fb859e66d2e9e3) |
|  | Channel Transmission QoS. |

## Detailed Description

ISO Channel QoS structure.

## Field Documentation

## [◆ ](#ac231434d1798f431c4fbac5a759784a5)rx

| struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md)\* bt\_iso\_chan\_qos::rx |
| --- |

Channel Receiving QoS.

Setting NULL disables data path BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST.

Can only be set for a connected isochronous channel, or a broadcast isochronous receiver.

## [◆ ](#a47a99a6ccfa5f1e0c9fb859e66d2e9e3)tx

| struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md)\* bt\_iso\_chan\_qos::tx |
| --- |

Channel Transmission QoS.

Setting NULL disables data path BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTRL.

Can only be set for a connected isochronous channel, or a broadcast isochronous transmitter.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_chan\_qos](structbt__iso__chan__qos.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
