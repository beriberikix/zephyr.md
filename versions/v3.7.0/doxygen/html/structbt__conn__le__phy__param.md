---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__conn__le__phy__param.html
original_path: doxygen/html/structbt__conn__le__phy__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_phy\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Preferred PHY parameters for LE connections.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [options](#a889dae2cdc2fba43f9f1194d26c4b737) |
|  | Connection PHY options. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pref\_tx\_phy](#ace64d2181ecc25ecdfa374f7f4bcf664) |
|  | Bitmask of preferred transmit PHYs. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pref\_rx\_phy](#a8d576bed5d9dfe9ca9a694d6d295afbc) |
|  | Bitmask of preferred receive PHYs. |

## Detailed Description

Preferred PHY parameters for LE connections.

## Field Documentation

## [◆ ](#a889dae2cdc2fba43f9f1194d26c4b737)options

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_phy\_param::options |
| --- |

Connection PHY options.

## [◆ ](#a8d576bed5d9dfe9ca9a694d6d295afbc)pref\_rx\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_phy\_param::pref\_rx\_phy |
| --- |

Bitmask of preferred receive PHYs.

## [◆ ](#ace64d2181ecc25ecdfa374f7f4bcf664)pref\_tx\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_phy\_param::pref\_tx\_phy |
| --- |

Bitmask of preferred transmit PHYs.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
