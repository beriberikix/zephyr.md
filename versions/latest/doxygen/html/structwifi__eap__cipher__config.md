---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structwifi__eap__cipher__config.html
original_path: doxygen/html/structwifi__eap__cipher__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_eap\_cipher\_config Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

`#include <[wifi.h](wifi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char \* | [key\_mgmt](#a385d365bb70a70fa09d321c55988afcc) |
|  | Key management type string. |
| char \* | [openssl\_ciphers](#a14128465917447f38d3854444a9bf6e1) |
|  | OpenSSL cipher string. |
| char \* | [group\_cipher](#aa505ae934897742078aa46f1fdb5d0d1) |
|  | Group cipher cipher string. |
| char \* | [pairwise\_cipher](#a3917f94dfafb22df260db9c4a129c3c4) |
|  | Pairwise\_cipher cipher string. |
| char \* | [group\_mgmt\_cipher](#ab53f5b5419b2b8c8a869ba4f9d645a41) |
|  | Group management cipher string. |
| char \* | [tls\_flags](#ae9a4b8a0f0b47ac1065562ce287473a5) |
|  | Used to confiure TLS features. |

## Field Documentation

## [◆ ](#aa505ae934897742078aa46f1fdb5d0d1)group\_cipher

| char\* wifi\_eap\_cipher\_config::group\_cipher |
| --- |

Group cipher cipher string.

## [◆ ](#ab53f5b5419b2b8c8a869ba4f9d645a41)group\_mgmt\_cipher

| char\* wifi\_eap\_cipher\_config::group\_mgmt\_cipher |
| --- |

Group management cipher string.

## [◆ ](#a385d365bb70a70fa09d321c55988afcc)key\_mgmt

| char\* wifi\_eap\_cipher\_config::key\_mgmt |
| --- |

Key management type string.

## [◆ ](#a14128465917447f38d3854444a9bf6e1)openssl\_ciphers

| char\* wifi\_eap\_cipher\_config::openssl\_ciphers |
| --- |

OpenSSL cipher string.

## [◆ ](#a3917f94dfafb22df260db9c4a129c3c4)pairwise\_cipher

| char\* wifi\_eap\_cipher\_config::pairwise\_cipher |
| --- |

Pairwise\_cipher cipher string.

## [◆ ](#ae9a4b8a0f0b47ac1065562ce287473a5)tls\_flags

| char\* wifi\_eap\_cipher\_config::tls\_flags |
| --- |

Used to confiure TLS features.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi.h](wifi_8h_source.md)

- [wifi\_eap\_cipher\_config](structwifi__eap__cipher__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
