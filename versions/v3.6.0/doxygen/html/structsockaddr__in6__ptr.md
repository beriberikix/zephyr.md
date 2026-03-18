---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsockaddr__in6__ptr.html
original_path: doxygen/html/structsockaddr__in6__ptr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sockaddr\_in6\_ptr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [sin6\_family](#a5de1da662d5fb57417a593cee8cc82de) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sin6\_port](#a64be2e93c2453899af630428089086cc) |
| struct [in6\_addr](structin6__addr.md) \* | [sin6\_addr](#af594f9662b0785a8f527bb9fcb95d92d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sin6\_scope\_id](#a9fe0b00f5081d4e027e15497304bc55b) |

## Field Documentation

## [◆ ](#af594f9662b0785a8f527bb9fcb95d92d)sin6\_addr

| struct [in6\_addr](structin6__addr.md)\* sockaddr\_in6\_ptr::sin6\_addr |
| --- |

## [◆ ](#a5de1da662d5fb57417a593cee8cc82de)sin6\_family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sockaddr\_in6\_ptr::sin6\_family |
| --- |

## [◆ ](#a64be2e93c2453899af630428089086cc)sin6\_port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sockaddr\_in6\_ptr::sin6\_port |
| --- |

## [◆ ](#a9fe0b00f5081d4e027e15497304bc55b)sin6\_scope\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sockaddr\_in6\_ptr::sin6\_scope\_id |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [sockaddr\_in6\_ptr](structsockaddr__in6__ptr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
