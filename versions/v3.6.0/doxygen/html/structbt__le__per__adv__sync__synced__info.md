---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__le__per__adv__sync__synced__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__synced__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_synced\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a7ca99b0596b08d153d3ba5310adab125) |
|  | Advertiser LE address and type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a5489c3038f7fff596316a456fc8d580b) |
|  | Advertiser SID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a5304e1826face35c506f3b8f6cad7df2) |
|  | Periodic advertising interval (N \* 1.25 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a8b7709011541e95ceaeac379cc3143bb) |
|  | Advertiser PHY. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [recv\_enabled](#a0dd4b7646da0fadc48e94ff3dc91ef83) |
|  | True if receiving periodic advertisements, false otherwise. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [service\_data](#adee2bdafa86a0c3c1dfb4660e85396a3) |
|  | Service Data provided by the peer when sync is transferred. |
| struct bt\_conn \* | [conn](#ada4cda53aa87f29d54f6cd88134efe14) |
|  | Peer that transferred the periodic advertising sync. |

## Field Documentation

## [◆ ](#a7ca99b0596b08d153d3ba5310adab125)addr

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_per\_adv\_sync\_synced\_info::addr |
| --- |

Advertiser LE address and type.

## [◆ ](#ada4cda53aa87f29d54f6cd88134efe14)conn

| struct bt\_conn\* bt\_le\_per\_adv\_sync\_synced\_info::conn |
| --- |

Peer that transferred the periodic advertising sync.

Will always be 0 when the sync is locally created.

## [◆ ](#a5304e1826face35c506f3b8f6cad7df2)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_synced\_info::interval |
| --- |

Periodic advertising interval (N \* 1.25 ms).

## [◆ ](#a8b7709011541e95ceaeac379cc3143bb)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_synced\_info::phy |
| --- |

Advertiser PHY.

## [◆ ](#a0dd4b7646da0fadc48e94ff3dc91ef83)recv\_enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_le\_per\_adv\_sync\_synced\_info::recv\_enabled |
| --- |

True if receiving periodic advertisements, false otherwise.

## [◆ ](#adee2bdafa86a0c3c1dfb4660e85396a3)service\_data

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_synced\_info::service\_data |
| --- |

Service Data provided by the peer when sync is transferred.

Will always be 0 when the sync is locally created.

## [◆ ](#a5489c3038f7fff596316a456fc8d580b)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_synced\_info::sid |
| --- |

Advertiser SID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
