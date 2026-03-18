---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structieee802154__security__params.html
original_path: doxygen/html/structieee802154__security__params.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_security\_params Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Net Management](group__ieee802154__mgmt.md)

Security parameters.
[More...](#details)

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key](#ae47ed5df4c70bfd4a28319d35f34c940) [16] |
|  | secKeyDescriptor.secKey |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key\_len](#a03ba0953eaea5035346b35e0555beb9c) |
|  | Key length of 16 bytes is mandatory for standards conformance. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key\_mode](#a5b6248a76d95ede67495f765d4d35b57): 2 |
|  | secKeyIdMode |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [level](#a50b7b0cbb4151234747c41d41e6fd656): 3 |
|  | Used instead of a frame-specific SecurityLevel parameter when constructing the auxiliary security header. |

## Detailed Description

Security parameters.

Used to setup the link-layer security settings, see tables 9-9 and 9-10 in section 9.5.

## Field Documentation

## [◆ ](#ae47ed5df4c70bfd4a28319d35f34c940)key

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_security\_params::key[16] |
| --- |

secKeyDescriptor.secKey

## [◆ ](#a03ba0953eaea5035346b35e0555beb9c)key\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_security\_params::key\_len |
| --- |

Key length of 16 bytes is mandatory for standards conformance.

## [◆ ](#a5b6248a76d95ede67495f765d4d35b57)key\_mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_security\_params::key\_mode |
| --- |

secKeyIdMode

## [◆ ](#a50b7b0cbb4151234747c41d41e6fd656)level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_security\_params::level |
| --- |

Used instead of a frame-specific SecurityLevel parameter when constructing the auxiliary security header.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_mgmt.h](ieee802154__mgmt_8h_source.md)

- [ieee802154\_security\_params](structieee802154__security__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
