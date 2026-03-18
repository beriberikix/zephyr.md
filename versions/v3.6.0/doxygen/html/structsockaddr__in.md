---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsockaddr__in.html
original_path: doxygen/html/structsockaddr__in.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sockaddr\_in Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

Socket address struct for IPv4.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [sin\_family](#a9a7d98bb8e18f4a06a021c32d6cc7117) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sin\_port](#a3cf9239fdd8bd32855d66a4b86349fbb) |
| struct [in\_addr](structin__addr.md) | [sin\_addr](#a4ea5f2f1138e5c8597097db255a9ec6c) |

## Detailed Description

Socket address struct for IPv4.

## Field Documentation

## [◆ ](#a4ea5f2f1138e5c8597097db255a9ec6c)sin\_addr

| struct [in\_addr](structin__addr.md) sockaddr\_in::sin\_addr |
| --- |

## [◆ ](#a9a7d98bb8e18f4a06a021c32d6cc7117)sin\_family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sockaddr\_in::sin\_family |
| --- |

## [◆ ](#a3cf9239fdd8bd32855d66a4b86349fbb)sin\_port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sockaddr\_in::sin\_port |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [sockaddr\_in](structsockaddr__in.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
