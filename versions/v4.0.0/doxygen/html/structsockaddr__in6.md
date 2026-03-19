---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsockaddr__in6.html
original_path: doxygen/html/structsockaddr__in6.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sockaddr\_in6 Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

Socket address struct for IPv6.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [sin6\_family](#aefa41e43be9c615f8cfd6266c0ed1687) |
|  | AF\_INET6. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sin6\_port](#a4fc2b7a478d258e9e778772701096022) |
|  | Port number. |
| struct [in6\_addr](structin6__addr.md) | [sin6\_addr](#a219e7f3ecd6d7dcf8fc2465475be490f) |
|  | IPv6 address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sin6\_scope\_id](#a1daad78c9848862ab33a48e05fa8cf17) |
|  | Interfaces for a scope. |

## Detailed Description

Socket address struct for IPv6.

## Field Documentation

## [◆ ](#a219e7f3ecd6d7dcf8fc2465475be490f)sin6\_addr

| struct [in6\_addr](structin6__addr.md) sockaddr\_in6::sin6\_addr |
| --- |

IPv6 address.

## [◆ ](#aefa41e43be9c615f8cfd6266c0ed1687)sin6\_family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sockaddr\_in6::sin6\_family |
| --- |

AF\_INET6.

## [◆ ](#a4fc2b7a478d258e9e778772701096022)sin6\_port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sockaddr\_in6::sin6\_port |
| --- |

Port number.

## [◆ ](#a1daad78c9848862ab33a48e05fa8cf17)sin6\_scope\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sockaddr\_in6::sin6\_scope\_id |
| --- |

Interfaces for a scope.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [sockaddr\_in6](structsockaddr__in6.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
