---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/msos__desc_8h.html
original_path: doxygen/html/msos__desc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msos\_desc.h File Reference

MS OS 2.0 descriptor definitions.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](msos__desc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [msosv2\_descriptor\_set\_header](structmsosv2__descriptor__set__header.md) |
| struct | [msosv2\_configuration\_subset\_header](structmsosv2__configuration__subset__header.md) |
| struct | [msosv2\_function\_subset\_header](structmsosv2__function__subset__header.md) |
| struct | [msosv2\_compatible\_id](structmsosv2__compatible__id.md) |
| struct | [msosv2\_guids\_property](structmsosv2__guids__property.md) |

| Macros | |
| --- | --- |
| #define | [DEVICE\_INTERFACE\_GUIDS\_PROPERTY\_NAME](#a927c65f355232352e67c60efdd293cff) |

| Enumerations | |
| --- | --- |
| enum | [msosv2\_descriptor\_index](#ab443ad91634b7a8fb19fc2aa7108e631) { [MS\_OS\_20\_DESCRIPTOR\_INDEX](#ab443ad91634b7a8fb19fc2aa7108e631abe0e6e00164db250e4ad900f418a57d5) = 0x07 , [MS\_OS\_20\_SET\_ALT\_ENUMERATION](#ab443ad91634b7a8fb19fc2aa7108e631a2ae9d4948f03b7d9623c547daa0a9116) = 0x08 } |
| enum | [msosv2\_descriptor\_type](#ae46389cacf4c5cca962702fcf0f6feb5) {     [MS\_OS\_20\_SET\_HEADER\_DESCRIPTOR](#ae46389cacf4c5cca962702fcf0f6feb5ac74a28d4e873b255d5b027af5ffffb5d) = 0x00 , [MS\_OS\_20\_SUBSET\_HEADER\_CONFIGURATION](#ae46389cacf4c5cca962702fcf0f6feb5afe117782c0101a880e152a8a1110ecbc) = 0x01 , [MS\_OS\_20\_SUBSET\_HEADER\_FUNCTION](#ae46389cacf4c5cca962702fcf0f6feb5a1200730075635cba8dea3420be41d1a7) = 0x02 , [MS\_OS\_20\_FEATURE\_COMPATIBLE\_ID](#ae46389cacf4c5cca962702fcf0f6feb5adf3b0e226fd373b882e27ed494fba265) = 0x03 ,     [MS\_OS\_20\_FEATURE\_REG\_PROPERTY](#ae46389cacf4c5cca962702fcf0f6feb5ad49ae449e2e2ff519a69018612ab5e62) = 0x04 , [MS\_OS\_20\_FEATURE\_MIN\_RESUME\_TIME](#ae46389cacf4c5cca962702fcf0f6feb5a7061acf1dbbeb7e2fbb88d149d295009) = 0x05 , [MS\_OS\_20\_FEATURE\_MODEL\_ID](#ae46389cacf4c5cca962702fcf0f6feb5ac7fc46a0124656e986871ae3b085536c) = 0x06 , [MS\_OS\_20\_FEATURE\_CCGP\_DEVICE](#ae46389cacf4c5cca962702fcf0f6feb5ab457a91ffd658376d87d7d32ad770004) = 0x07 ,     [MS\_OS\_20\_FEATURE\_VENDOR\_REVISION](#ae46389cacf4c5cca962702fcf0f6feb5a2f7940f495e1a996692f474a456d63d6) = 0x08   } |
| enum | [msosv2\_property\_data\_type](#a1afad4029116a837d4430a0ea976254f) {     [MS\_OS\_20\_PROPERTY\_DATA\_RESERVED](#a1afad4029116a837d4430a0ea976254fac1e0035b4badb15f714bff249514ef17) = 0 , [MS\_OS\_20\_PROPERTY\_DATA\_REG\_SZ](#a1afad4029116a837d4430a0ea976254fa404430118680c625a399662e981c4489) = 1 , [MS\_OS\_20\_PROPERTY\_DATA\_REG\_EXPAND\_SZ](#a1afad4029116a837d4430a0ea976254fa9245e361cbe8425c1b54958ba0c0902c) = 2 , [MS\_OS\_20\_PROPERTY\_DATA\_REG\_BINARY](#a1afad4029116a837d4430a0ea976254fae8bd325ca3f9cc1d33d229d0de14aba1) = 3 ,     [MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_LITTLE\_ENDIAN](#a1afad4029116a837d4430a0ea976254faa831bf4ba88de3eb768745c41a8dee10) = 4 , [MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_BIG\_ENDIAN](#a1afad4029116a837d4430a0ea976254fa969e1f96f1582db317bbf96d183ae670) = 5 , [MS\_OS\_20\_PROPERTY\_DATA\_REG\_LINK](#a1afad4029116a837d4430a0ea976254fa4050949a26b3a61f1aeecc996eb02d81) = 6 , [MS\_OS\_20\_PROPERTY\_DATA\_REG\_MULTI\_SZ](#a1afad4029116a837d4430a0ea976254fa89b2d8dfbddc343879edc14a5c9f93f5) = 7   } |

## Detailed Description

MS OS 2.0 descriptor definitions.

## Macro Definition Documentation

## [◆ ](#a927c65f355232352e67c60efdd293cff)DEVICE\_INTERFACE\_GUIDS\_PROPERTY\_NAME

| #define DEVICE\_INTERFACE\_GUIDS\_PROPERTY\_NAME |
| --- |

**Value:**

'D', 0x00, 'e', 0x00, 'v', 0x00, 'i', 0x00, 'c', 0x00, 'e', 0x00, \

'I', 0x00, 'n', 0x00, 't', 0x00, 'e', 0x00, 'r', 0x00, 'f', 0x00, \

'a', 0x00, 'c', 0x00, 'e', 0x00, 'G', 0x00, 'U', 0x00, 'I', 0x00, \

'D', 0x00, 's', 0x00, 0x00, 0x00

## Enumeration Type Documentation

## [◆ ](#ab443ad91634b7a8fb19fc2aa7108e631)msosv2\_descriptor\_index

| enum [msosv2\_descriptor\_index](#ab443ad91634b7a8fb19fc2aa7108e631) |
| --- |

| Enumerator | |
| --- | --- |
| MS\_OS\_20\_DESCRIPTOR\_INDEX |  |
| MS\_OS\_20\_SET\_ALT\_ENUMERATION |  |

## [◆ ](#ae46389cacf4c5cca962702fcf0f6feb5)msosv2\_descriptor\_type

| enum [msosv2\_descriptor\_type](#ae46389cacf4c5cca962702fcf0f6feb5) |
| --- |

| Enumerator | |
| --- | --- |
| MS\_OS\_20\_SET\_HEADER\_DESCRIPTOR |  |
| MS\_OS\_20\_SUBSET\_HEADER\_CONFIGURATION |  |
| MS\_OS\_20\_SUBSET\_HEADER\_FUNCTION |  |
| MS\_OS\_20\_FEATURE\_COMPATIBLE\_ID |  |
| MS\_OS\_20\_FEATURE\_REG\_PROPERTY |  |
| MS\_OS\_20\_FEATURE\_MIN\_RESUME\_TIME |  |
| MS\_OS\_20\_FEATURE\_MODEL\_ID |  |
| MS\_OS\_20\_FEATURE\_CCGP\_DEVICE |  |
| MS\_OS\_20\_FEATURE\_VENDOR\_REVISION |  |

## [◆ ](#a1afad4029116a837d4430a0ea976254f)msosv2\_property\_data\_type

| enum [msosv2\_property\_data\_type](#a1afad4029116a837d4430a0ea976254f) |
| --- |

| Enumerator | |
| --- | --- |
| MS\_OS\_20\_PROPERTY\_DATA\_RESERVED |  |
| MS\_OS\_20\_PROPERTY\_DATA\_REG\_SZ |  |
| MS\_OS\_20\_PROPERTY\_DATA\_REG\_EXPAND\_SZ |  |
| MS\_OS\_20\_PROPERTY\_DATA\_REG\_BINARY |  |
| MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_LITTLE\_ENDIAN |  |
| MS\_OS\_20\_PROPERTY\_DATA\_REG\_DWORD\_BIG\_ENDIAN |  |
| MS\_OS\_20\_PROPERTY\_DATA\_REG\_LINK |  |
| MS\_OS\_20\_PROPERTY\_DATA\_REG\_MULTI\_SZ |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [msos\_desc.h](msos__desc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
