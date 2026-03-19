---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__iso__chan__io__qos.html
original_path: doxygen/html/structbt__iso__chan__io__qos.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
|  | Channel PHY - See the BT\_GAP\_LE\_PHY\_\* values. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtn](#a5106bfd09f6be52604e7c7f0e3390684) |
|  | Channel Retransmission Number. |
| struct [bt\_iso\_chan\_path](structbt__iso__chan__path.md) \* | [path](#a725f7578282fbef6671e87bccdf4c85e) |
|  | Channel data path reference. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_pdu](#ae9e7678a63030353eea65152d89464cd) |
|  | Maximum PDU size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [burst\_number](#ac64a3ce7282ac8bc5b5420a46417b22c) |
|  | Burst number. |

## Detailed Description

ISO Channel IO QoS structure.

## Field Documentation

## [◆ ](#ac64a3ce7282ac8bc5b5420a46417b22c)burst\_number

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_io\_qos::burst\_number |
| --- |

Burst number.

Value range [BT\_ISO\_BN\_MIN](group__bt__iso.md#ga2905cddfa456fc846f0c8025487b404d "BT_ISO_BN_MIN") to [BT\_ISO\_BN\_MAX](group__bt__iso.md#gac05f4f51ea04962679f616bb167b724d "BT_ISO_BN_MAX").

## [◆ ](#ae9e7678a63030353eea65152d89464cd)max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_chan\_io\_qos::max\_pdu |
| --- |

Maximum PDU size.

Maximum size, in octets, of the payload from link layer to link layer.

Value range [BT\_ISO\_CONNECTED\_PDU\_MIN](group__bt__iso.md#ga4e29d5966f959114754d62a8763c8c1e "BT_ISO_CONNECTED_PDU_MIN") to [BT\_ISO\_PDU\_MAX](group__bt__iso.md#ga88fb5690cd1cab4e5e8d5c025cc1af00 "BT_ISO_PDU_MAX") for connected ISO.

Value range [BT\_ISO\_BROADCAST\_PDU\_MIN](group__bt__iso.md#gaee766ff789f1bf01f75c88112ddd2afa "BT_ISO_BROADCAST_PDU_MIN") to [BT\_ISO\_PDU\_MAX](group__bt__iso.md#ga88fb5690cd1cab4e5e8d5c025cc1af00 "BT_ISO_PDU_MAX") for broadcast ISO.

## [◆ ](#a725f7578282fbef6671e87bccdf4c85e)path

| struct [bt\_iso\_chan\_path](structbt__iso__chan__path.md)\* bt\_iso\_chan\_io\_qos::path |
| --- |

Channel data path reference.

Setting to NULL default to HCI data path (same as setting path.pid to [BT\_ISO\_DATA\_PATH\_HCI](group__bt__iso.md#gadd421c69edccfd695d728ded5feb6862 "BT_ISO_DATA_PATH_HCI")).

## [◆ ](#a2180a4f82e4cdf5288b7f67701a16ad6)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_io\_qos::phy |
| --- |

Channel PHY - See the BT\_GAP\_LE\_PHY\_\* values.

Setting [BT\_GAP\_LE\_PHY\_NONE](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20baaf7e1b40f6464a603e5116db269cacab "BT_GAP_LE_PHY_NONE") is invalid.

## [◆ ](#a5106bfd09f6be52604e7c7f0e3390684)rtn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_io\_qos::rtn |
| --- |

Channel Retransmission Number.

This value is ignored if any advanced ISO parameters are set.

## [◆ ](#ae52611dc326b6777620ff7aa43f566e9)sdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_chan\_io\_qos::sdu |
| --- |

Channel SDU.

Value range is [BT\_ISO\_MIN\_SDU](group__bt__iso.md#ga4cc5565eeda9a3661d49d485637d1db2 "BT_ISO_MIN_SDU") to [BT\_ISO\_MAX\_SDU](group__bt__iso.md#gaa5d5588e7229db16219b0c44921bbcf7 "BT_ISO_MAX_SDU").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
