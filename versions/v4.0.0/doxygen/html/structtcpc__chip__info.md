---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structtcpc__chip__info.html
original_path: doxygen/html/structtcpc__chip__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcpc\_chip\_info Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Type-C Port Controller API](group__usb__type__c__port__controller__api.md)

TCPC Chip Information.
[More...](#details)

`#include <[usbc_tcpc.h](usbc__tcpc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vendor\_id](#ab48400ea4209d5443e5b7e0bfee6c4fc) |
|  | Vendor Id. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [product\_id](#a14c11999ef548e41f4338f3e7208b7a9) |
|  | Product Id. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [device\_id](#a9e76ee3bcc395dbb77d7a065f6181cd6) |
|  | Device Id. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [fw\_version\_number](#a7789339580e2774d18a8f4c78332f774) |
|  | Firmware version number. |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [min\_req\_fw\_version\_string](#a677a85ef27f0d5db969ce3232506d1bb) [8] |  |
|  | Minimum Required firmware version string. [More...](#a677a85ef27f0d5db969ce3232506d1bb) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)   [min\_req\_fw\_version\_number](#a8d66f33379493e1a0ed707b3715f863a) |  |
|  | Minimum Required firmware version number. [More...](#a8d66f33379493e1a0ed707b3715f863a) |
| }; |  |

## Detailed Description

TCPC Chip Information.

## Field Documentation

## [◆ ](#ab0964dfb0a6ea8d41373be2b4989f9b3)[union]

| union { ... } [tcpc\_chip\_info](structtcpc__chip__info.md) |
| --- |

## [◆ ](#a9e76ee3bcc395dbb77d7a065f6181cd6)device\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tcpc\_chip\_info::device\_id |
| --- |

Device Id.

## [◆ ](#a7789339580e2774d18a8f4c78332f774)fw\_version\_number

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tcpc\_chip\_info::fw\_version\_number |
| --- |

Firmware version number.

## [◆ ](#a8d66f33379493e1a0ed707b3715f863a)min\_req\_fw\_version\_number

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tcpc\_chip\_info::min\_req\_fw\_version\_number |
| --- |

Minimum Required firmware version number.

## [◆ ](#a677a85ef27f0d5db969ce3232506d1bb)min\_req\_fw\_version\_string

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tcpc\_chip\_info::min\_req\_fw\_version\_string[8] |
| --- |

Minimum Required firmware version string.

## [◆ ](#a14c11999ef548e41f4338f3e7208b7a9)product\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tcpc\_chip\_info::product\_id |
| --- |

Product Id.

## [◆ ](#ab48400ea4209d5443e5b7e0bfee6c4fc)vendor\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tcpc\_chip\_info::vendor\_id |
| --- |

Vendor Id.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_tcpc.h](usbc__tcpc_8h_source.md)

- [tcpc\_chip\_info](structtcpc__chip__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
