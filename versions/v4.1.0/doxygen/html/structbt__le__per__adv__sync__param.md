---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__per__adv__sync__param.html
original_path: doxygen/html/structbt__le__per__adv__sync__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#ac93adedad747f61a771ac5445e486b74) |
|  | Periodic Advertiser Address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a70795642ee94dd9e87f0cf251c095e7f) |
|  | Advertiser SID. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [options](#a4252f2b3b453c2f9c8fbf8c35a618ff2) |
|  | Bit-field of periodic advertising sync options. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [skip](#af9abb65547fb5bfea65f4c22963c7da0) |
|  | Maximum event skip. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout](#a301cfd3d6e5620d29c021ababe104754) |
|  | Synchronization timeout (N \* 10 ms). |

## Field Documentation

## [◆ ](#ac93adedad747f61a771ac5445e486b74)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_le\_per\_adv\_sync\_param::addr |
| --- |

Periodic Advertiser Address.

Only valid if not using the periodic advertising list (BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST)

## [◆ ](#a4252f2b3b453c2f9c8fbf8c35a618ff2)options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_per\_adv\_sync\_param::options |
| --- |

Bit-field of periodic advertising sync options.

## [◆ ](#a70795642ee94dd9e87f0cf251c095e7f)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_param::sid |
| --- |

Advertiser SID.

Only valid if not using the periodic advertising list (BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST)

## [◆ ](#af9abb65547fb5bfea65f4c22963c7da0)skip

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_param::skip |
| --- |

Maximum event skip.

Maximum number of periodic advertising events that can be skipped after a successful receive. Range: 0x0000 to 0x01F3

## [◆ ](#a301cfd3d6e5620d29c021ababe104754)timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_param::timeout |
| --- |

Synchronization timeout (N \* 10 ms).

Synchronization timeout for the periodic advertising sync. Range 0x000A to 0x4000 (100 ms to 163840 ms)

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
