---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structhttp__resource__detail.html
original_path: doxygen/html/structhttp__resource__detail.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_resource\_detail Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

Representation of a server resource, common for all resource types.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bitmask\_of\_supported\_http\_methods](#ae391e85a5713bceef9228b93e876c817) |
|  | Bitmask of supported HTTP methods ([http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8 "http_method")). |
| enum [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) | [type](#af90b58f593a0c5c8506efc7a54a9cf68) |
|  | Resource type. |
| int | [path\_len](#ac3aa9d4f3781a974739810af5a9e8860) |
|  | Length of the URL path. |
| const char \* | [content\_encoding](#ae5b2415ad3e42c164c4e20fd5bb67bd4) |
|  | Content encoding of the resource. |
| const char \* | [content\_type](#acea8d8ff42d8b6ba7d451d3c4de40084) |
|  | Content type of the resource. |

## Detailed Description

Representation of a server resource, common for all resource types.

## Field Documentation

## [◆ ](#ae391e85a5713bceef9228b93e876c817)bitmask\_of\_supported\_http\_methods

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) http\_resource\_detail::bitmask\_of\_supported\_http\_methods |
| --- |

Bitmask of supported HTTP methods ([http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8 "http_method")).

## [◆ ](#ae5b2415ad3e42c164c4e20fd5bb67bd4)content\_encoding

| const char\* http\_resource\_detail::content\_encoding |
| --- |

Content encoding of the resource.

## [◆ ](#acea8d8ff42d8b6ba7d451d3c4de40084)content\_type

| const char\* http\_resource\_detail::content\_type |
| --- |

Content type of the resource.

## [◆ ](#ac3aa9d4f3781a974739810af5a9e8860)path\_len

| int http\_resource\_detail::path\_len |
| --- |

Length of the URL path.

## [◆ ](#af90b58f593a0c5c8506efc7a54a9cf68)type

| enum [http\_resource\_type](group__http__server.md#ga23d0077fb99827b25491111bd74d00af) http\_resource\_detail::type |
| --- |

Resource type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http\_resource\_detail](structhttp__resource__detail.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
