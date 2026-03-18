---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__le__per__adv__sync__subevent__params.html
original_path: doxygen/html/structbt__le__per__adv__sync__subevent__params.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_subevent\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [properties](#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4) |
|  | Periodic Advertising Properties. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subevents](#a867c66bf09461a4369da3d250701d2ae) |
|  | Number of subevents to sync to. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [subevents](#a5ac4e81ddd63797f921105748344c125) |
|  | The subevent(s) to synchronize with. |

## Field Documentation

## [◆ ](#a867c66bf09461a4369da3d250701d2ae)num\_subevents

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_subevent\_params::num\_subevents |
| --- |

Number of subevents to sync to.

## [◆ ](#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4)properties

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_subevent\_params::properties |
| --- |

Periodic Advertising Properties.

Bit 6 is include TxPower, all others RFU.

## [◆ ](#a5ac4e81ddd63797f921105748344c125)subevents

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_le\_per\_adv\_sync\_subevent\_params::subevents |
| --- |

The subevent(s) to synchronize with.

The array must have [num\_subevents](#a867c66bf09461a4369da3d250701d2ae) elements.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
