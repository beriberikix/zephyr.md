---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__le__scan__recv__info.html
original_path: doxygen/html/structbt__le__scan__recv__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_scan\_recv\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

LE advertisement and scan response packet information.
[More...](#details)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a907fb7ec3c78d68da5015a8c3afc3084) |
|  | Advertiser LE address and type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a4df8d4e1fdd7514d170744856ebe7015) |
|  | Advertising Set Identifier. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#a88f677733147245ccbf861c7fc5e0f11) |
|  | Strength of advertiser signal. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#a2addeba6d2ec8e55dc5379adf6519148) |
|  | Transmit power of the advertiser. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_type](#adccb2ce5c6d228bd7f8f050088629524) |
|  | Advertising packet type. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [adv\_props](#af29ddfb59e286af9ca465cbd5a91bf2d) |
|  | Advertising packet properties bitfield. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a1060c5937708ff81a64f068e02fc7826) |
|  | Periodic advertising interval (N \* 1.25 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [primary\_phy](#a6189ed8453cb7907f34dc7dfaf1343bd) |
|  | Primary advertising channel PHY. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [secondary\_phy](#ac797291291dc7ba7ac171ed7f24f0d16) |
|  | Secondary advertising channel PHY. |

## Detailed Description

LE advertisement and scan response packet information.

## Field Documentation

## [◆ ](#a907fb7ec3c78d68da5015a8c3afc3084)addr

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_scan\_recv\_info::addr |
| --- |

Advertiser LE address and type.

If advertiser is anonymous then this address will be [BT\_ADDR\_LE\_ANY](group__bt__addr.md#ga17e9efacd50c682b2f709c217e920d48 "BT_ADDR_LE_ANY").

## [◆ ](#af29ddfb59e286af9ca465cbd5a91bf2d)adv\_props

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_scan\_recv\_info::adv\_props |
| --- |

Advertising packet properties bitfield.

Uses the BT\_GAP\_ADV\_PROP\_\* values. May indicate that this is a scan response if the value contains the [BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba55258ac9a7b355db87aeec5d443718f7 "BT_GAP_ADV_PROP_SCAN_RESPONSE") bit.

## [◆ ](#adccb2ce5c6d228bd7f8f050088629524)adv\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_scan\_recv\_info::adv\_type |
| --- |

Advertising packet type.

Uses the BT\_GAP\_ADV\_TYPE\_\* value.

May indicate that this is a scan response if the type is [BT\_GAP\_ADV\_TYPE\_SCAN\_RSP](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea5387de0177d3a9da9fd0c44ca30c7018 "BT_GAP_ADV_TYPE_SCAN_RSP").

## [◆ ](#a1060c5937708ff81a64f068e02fc7826)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_scan\_recv\_info::interval |
| --- |

Periodic advertising interval (N \* 1.25 ms).

If 0 there is no periodic advertising.

## [◆ ](#a6189ed8453cb7907f34dc7dfaf1343bd)primary\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_scan\_recv\_info::primary\_phy |
| --- |

Primary advertising channel PHY.

## [◆ ](#a88f677733147245ccbf861c7fc5e0f11)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_scan\_recv\_info::rssi |
| --- |

Strength of advertiser signal.

## [◆ ](#ac797291291dc7ba7ac171ed7f24f0d16)secondary\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_scan\_recv\_info::secondary\_phy |
| --- |

Secondary advertising channel PHY.

## [◆ ](#a4df8d4e1fdd7514d170744856ebe7015)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_scan\_recv\_info::sid |
| --- |

Advertising Set Identifier.

## [◆ ](#a2addeba6d2ec8e55dc5379adf6519148)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_scan\_recv\_info::tx\_power |
| --- |

Transmit power of the advertiser.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
