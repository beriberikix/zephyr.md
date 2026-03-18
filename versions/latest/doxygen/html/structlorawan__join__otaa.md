---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structlorawan__join__otaa.html
original_path: doxygen/html/structlorawan__join__otaa.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lorawan\_join\_otaa Struct Reference

[Connectivity](group__connectivity.md) » [LoRaWAN APIs](group__lorawan__api.md)

LoRaWAN join parameters for over-the-Air activation (OTAA).
[More...](#details)

`#include <[lorawan.h](lorawan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [join\_eui](#aacf3523f615f08fac1993e0bdc354072) |
|  | Join EUI. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [nwk\_key](#af1a96b4fa17ee70ee0e8ba078b02a6bc) |
|  | Network Key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [app\_key](#a28dd704e28d0bed909c3e85e516c85ea) |
|  | Application Key. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dev\_nonce](#ab83167af58040f95072a95fbaed1ff5d) |
|  | Device Nonce. |

## Detailed Description

LoRaWAN join parameters for over-the-Air activation (OTAA).

Note that all of the fields use LoRaWAN 1.1 terminology.

All parameters are optional if a secure element is present in which case the values stored in the secure element will be used instead.

## Field Documentation

## [◆ ](#a28dd704e28d0bed909c3e85e516c85ea)app\_key

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* lorawan\_join\_otaa::app\_key |
| --- |

Application Key.

## [◆ ](#ab83167af58040f95072a95fbaed1ff5d)dev\_nonce

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lorawan\_join\_otaa::dev\_nonce |
| --- |

Device Nonce.

Starting with LoRaWAN 1.0.4 the DevNonce must be monotonically increasing for each OTAA join with the same EUI. The DevNonce should be stored in non-volatile memory by the application.

## [◆ ](#aacf3523f615f08fac1993e0bdc354072)join\_eui

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* lorawan\_join\_otaa::join\_eui |
| --- |

Join EUI.

## [◆ ](#af1a96b4fa17ee70ee0e8ba078b02a6bc)nwk\_key

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* lorawan\_join\_otaa::nwk\_key |
| --- |

Network Key.

---

The documentation for this struct was generated from the following file:

- zephyr/lorawan/[lorawan.h](lorawan_8h_source.md)

- [lorawan\_join\_otaa](structlorawan__join__otaa.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
