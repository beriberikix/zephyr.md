---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__le__per__adv__sync__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Advertising set info structure.
[More...](#details)

`#include <[bluetooth.h](bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#ac10fc2e2d3ec2160db8c2aac148d18a2) |
|  | Periodic Advertiser Address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#acc0ef26c38279c9a67f8992005c2e58a) |
|  | Advertiser SID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a365a0d8577429e4ee96e977071c9a906) |
|  | Periodic advertising interval (N \* 1.25 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a4d9520ea6a803f8fe4f41190f55c26e5) |
|  | Advertiser PHY. |

## Detailed Description

Advertising set info structure.

## Field Documentation

## [◆ ](#ac10fc2e2d3ec2160db8c2aac148d18a2)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_le\_per\_adv\_sync\_info::addr |
| --- |

Periodic Advertiser Address.

## [◆ ](#a365a0d8577429e4ee96e977071c9a906)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_info::interval |
| --- |

Periodic advertising interval (N \* 1.25 ms).

## [◆ ](#a4d9520ea6a803f8fe4f41190f55c26e5)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_info::phy |
| --- |

Advertiser PHY.

## [◆ ](#acc0ef26c38279c9a67f8992005c2e58a)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_info::sid |
| --- |

Advertiser SID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
