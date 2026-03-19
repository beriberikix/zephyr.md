---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structhttp__resource__detail__static.html
original_path: doxygen/html/structhttp__resource__detail__static.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_resource\_detail\_static Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

Representation of a static server resource.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [http\_resource\_detail](structhttp__resource__detail.md) | [common](#a67e4e9166d571d44763f3f7cecd34725) |
|  | Common resource details. |
| const void \* | [static\_data](#a1ac562d11ee9b73c2cdcffe81f5a43b9) |
|  | Content of the static resource. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [static\_data\_len](#a177c212ecfd8e0320200b4ed841f0484) |
|  | Size of the static resource. |

## Detailed Description

Representation of a static server resource.

## Field Documentation

## [◆ ](#a67e4e9166d571d44763f3f7cecd34725)common

| struct [http\_resource\_detail](structhttp__resource__detail.md) http\_resource\_detail\_static::common |
| --- |

Common resource details.

## [◆ ](#a1ac562d11ee9b73c2cdcffe81f5a43b9)static\_data

| const void\* http\_resource\_detail\_static::static\_data |
| --- |

Content of the static resource.

## [◆ ](#a177c212ecfd8e0320200b4ed841f0484)static\_data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_resource\_detail\_static::static\_data\_len |
| --- |

Size of the static resource.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http\_resource\_detail\_static](structhttp__resource__detail__static.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
