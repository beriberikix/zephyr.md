---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__linkaddr.html
original_path: doxygen/html/structnet__linkaddr.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_linkaddr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Link Address Library](group__net__linkaddr.md)

Hardware link address structure.
[More...](#details)

`#include <[net_linkaddr.h](net__linkaddr_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [addr](#a2176a9f7a444ac3b0108102d8cf852f0) |
|  | The array of byte representing the address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0) |
|  | Length of that address array. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a5f5b4c3d353261d0fab8011aa09f00d7) |
|  | What kind of address is this for. |

## Detailed Description

Hardware link address structure.

Used to hold the link address information

## Field Documentation

## [◆ ](#a2176a9f7a444ac3b0108102d8cf852f0)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* net\_linkaddr::addr |
| --- |

The array of byte representing the address.

## [◆ ](#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_linkaddr::len |
| --- |

Length of that address array.

## [◆ ](#a5f5b4c3d353261d0fab8011aa09f00d7)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_linkaddr::type |
| --- |

What kind of address is this for.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_linkaddr.h](net__linkaddr_8h_source.md)

- [net\_linkaddr](structnet__linkaddr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
