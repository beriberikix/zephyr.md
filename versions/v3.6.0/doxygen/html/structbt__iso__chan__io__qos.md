---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__iso__chan__io__qos.html
original_path: doxygen/html/structbt__iso__chan__io__qos.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_chan\_io\_qos Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Channel IO QoS structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sdu](#ae52611dc326b6777620ff7aa43f566e9) |
|  | Channel SDU. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a2180a4f82e4cdf5288b7f67701a16ad6) |
|  | Channel PHY - See BT\_GAP\_LE\_PHY for values. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtn](#a5106bfd09f6be52604e7c7f0e3390684) |
|  | Channel Retransmission Number. |
| struct [bt\_iso\_chan\_path](structbt__iso__chan__path.md) \* | [path](#a725f7578282fbef6671e87bccdf4c85e) |
|  | Channel data path reference. |

## Detailed Description

ISO Channel IO QoS structure.

## Field Documentation

## [◆ ](#a725f7578282fbef6671e87bccdf4c85e)path

| struct [bt\_iso\_chan\_path](structbt__iso__chan__path.md)\* bt\_iso\_chan\_io\_qos::path |
| --- |

Channel data path reference.

Setting to NULL default to HCI data path (same as setting path.pid to BT\_ISO\_DATA\_PATH\_HCI).

## [◆ ](#a2180a4f82e4cdf5288b7f67701a16ad6)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_io\_qos::phy |
| --- |

Channel PHY - See BT\_GAP\_LE\_PHY for values.

Setting BT\_GAP\_LE\_PHY\_NONE is invalid.

## [◆ ](#a5106bfd09f6be52604e7c7f0e3390684)rtn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_io\_qos::rtn |
| --- |

Channel Retransmission Number.

This value is ignored if any advanced ISO parameters are set.

## [◆ ](#ae52611dc326b6777620ff7aa43f566e9)sdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_chan\_io\_qos::sdu |
| --- |

Channel SDU.

Maximum value is BT\_ISO\_MAX\_SDU

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
