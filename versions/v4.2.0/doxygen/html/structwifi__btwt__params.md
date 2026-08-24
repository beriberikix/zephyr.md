---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structwifi__btwt__params.html
original_path: doxygen/html/structwifi__btwt__params.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_btwt\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi broadcast TWT parameters.
[More...](#details)

`#include <[zephyr/net/wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [btwt\_id](#ae52281d9f53e106fb9ed813131d8085e) |
|  | Broadcast TWT ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [btwt\_mantissa](#a2c1b3551a714fbf1b948ce4bcf805934) |
|  | Broadcast TWT mantissa. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [btwt\_exponent](#a76c97bcc132405d6a1a54bcca77054ac) |
|  | Broadcast TWT exponent. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [btwt\_nominal\_wake](#a0192d3a9334fc55a135206e6b74ea5b5) |
|  | Broadcast TWT range. |

## Detailed Description

Wi-Fi broadcast TWT parameters.

## Field Documentation

## [◆ ](#a76c97bcc132405d6a1a54bcca77054ac)btwt\_exponent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_btwt\_params::btwt\_exponent |
| --- |

Broadcast TWT exponent.

## [◆ ](#ae52281d9f53e106fb9ed813131d8085e)btwt\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_btwt\_params::btwt\_id |
| --- |

Broadcast TWT ID.

## [◆ ](#a2c1b3551a714fbf1b948ce4bcf805934)btwt\_mantissa

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_btwt\_params::btwt\_mantissa |
| --- |

Broadcast TWT mantissa.

## [◆ ](#a0192d3a9334fc55a135206e6b74ea5b5)btwt\_nominal\_wake

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_btwt\_params::btwt\_nominal\_wake |
| --- |

Broadcast TWT range.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_btwt\_params](structwifi__btwt__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
