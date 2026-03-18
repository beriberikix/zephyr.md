---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlorawan__join__abp.html
original_path: doxygen/html/structlorawan__join__abp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lorawan\_join\_abp Struct Reference

[Connectivity](group__connectivity.md) » [LoRaWAN APIs](group__lorawan__api.md)

LoRaWAN join parameters for activation by personalization (ABP).
[More...](#details)

`#include <[lorawan.h](lorawan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dev\_addr](#ad132826d04b66f145865f9a30ff03fff) |
|  | Device address on the network. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [app\_skey](#a8019bead1dfdda7a0b05f35f128edca5) |
|  | Application session key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [nwk\_skey](#aa389fec6799b12e750d57aaf0b34e6b0) |
|  | Network session key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [app\_eui](#a7a409fa2f3761c49085818768a62d216) |
|  | Application EUI. |

## Detailed Description

LoRaWAN join parameters for activation by personalization (ABP).

## Field Documentation

## [◆ ](#a7a409fa2f3761c49085818768a62d216)app\_eui

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* lorawan\_join\_abp::app\_eui |
| --- |

Application EUI.

## [◆ ](#a8019bead1dfdda7a0b05f35f128edca5)app\_skey

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* lorawan\_join\_abp::app\_skey |
| --- |

Application session key.

## [◆ ](#ad132826d04b66f145865f9a30ff03fff)dev\_addr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lorawan\_join\_abp::dev\_addr |
| --- |

Device address on the network.

## [◆ ](#aa389fec6799b12e750d57aaf0b34e6b0)nwk\_skey

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* lorawan\_join\_abp::nwk\_skey |
| --- |

Network session key.

---

The documentation for this struct was generated from the following file:

- zephyr/lorawan/[lorawan.h](lorawan_8h_source.md)

- [lorawan\_join\_abp](structlorawan__join__abp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
