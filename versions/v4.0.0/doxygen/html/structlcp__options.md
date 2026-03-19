---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlcp__options.html
original_path: doxygen/html/structlcp__options.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lcp\_options Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [PPP L2/driver Support Functions](group__ppp.md)

Link control protocol options.
[More...](#details)

`#include <[ppp.h](net_2ppp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [magic](#a68d9f004596bfac6dea9b14bd22e9dda) |
|  | Magic number. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [async\_map](#a2672e1374c25aac1571adccadda5283e) |
|  | Async char map. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mru](#a028da648c4b8cdd9330d9195a161e847) |
|  | Maximum Receive Unit value. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [auth\_proto](#a560d009cb642fff99ef83a9e6c056c6b) |
|  | Which authentication protocol was negotiated (0 means none). |

## Detailed Description

Link control protocol options.

## Field Documentation

## [◆ ](#a2672e1374c25aac1571adccadda5283e)async\_map

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lcp\_options::async\_map |
| --- |

Async char map.

## [◆ ](#a560d009cb642fff99ef83a9e6c056c6b)auth\_proto

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lcp\_options::auth\_proto |
| --- |

Which authentication protocol was negotiated (0 means none).

## [◆ ](#a68d9f004596bfac6dea9b14bd22e9dda)magic

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lcp\_options::magic |
| --- |

Magic number.

## [◆ ](#a028da648c4b8cdd9330d9195a161e847)mru

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lcp\_options::mru |
| --- |

Maximum Receive Unit value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ppp.h](net_2ppp_8h_source.md)

- [lcp\_options](structlcp__options.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
