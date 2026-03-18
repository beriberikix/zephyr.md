---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structlwm2m__obj__path.html
original_path: doxygen/html/structlwm2m__obj__path.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lwm2m\_obj\_path Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [LwM2M high-level API](group__lwm2m__api.md)

LwM2M object path structure.
[More...](#details)

`#include <[lwm2m.h](lwm2m_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_id](#ad1cf2b4f67b059e92853a05e2d070bb7) |
|  | Object ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_inst\_id](#a7ae1a626b6f4b4c9cdc3e1a99d644ff2) |
|  | Object instance ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [res\_id](#ac52cc68142a270b4bab8edfc7cb8b106) |
|  | Resource ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [res\_inst\_id](#a924d75187c05b64989b6eed69b563c29) |
|  | Resource instance ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [level](#aaeb8482037aa5d9b389236eb9f3e2984) |
|  | Path level (0-4). |

## Detailed Description

LwM2M object path structure.

## Field Documentation

## [◆ ](#aaeb8482037aa5d9b389236eb9f3e2984)level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lwm2m\_obj\_path::level |
| --- |

Path level (0-4).

Ex. 4 = resource instance.

## [◆ ](#ad1cf2b4f67b059e92853a05e2d070bb7)obj\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lwm2m\_obj\_path::obj\_id |
| --- |

Object ID.

## [◆ ](#a7ae1a626b6f4b4c9cdc3e1a99d644ff2)obj\_inst\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lwm2m\_obj\_path::obj\_inst\_id |
| --- |

Object instance ID.

## [◆ ](#ac52cc68142a270b4bab8edfc7cb8b106)res\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lwm2m\_obj\_path::res\_id |
| --- |

Resource ID.

## [◆ ](#a924d75187c05b64989b6eed69b563c29)res\_inst\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lwm2m\_obj\_path::res\_inst\_id |
| --- |

Resource instance ID.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lwm2m.h](lwm2m_8h_source.md)

- [lwm2m\_obj\_path](structlwm2m__obj__path.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
