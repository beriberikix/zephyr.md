---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsockaddr__in__ptr.html
original_path: doxygen/html/structsockaddr__in__ptr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sockaddr\_in\_ptr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [sin\_family](#ae8ca040f7813d6974e0440f877df6744) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sin\_port](#aab1491a8d77ca11d8104ef3ef1bace80) |
| struct [in\_addr](structin__addr.md) \* | [sin\_addr](#a02d48b07cb42745a729428fc9f4af765) |

## Field Documentation

## [◆ ](#a02d48b07cb42745a729428fc9f4af765)sin\_addr

| struct [in\_addr](structin__addr.md)\* sockaddr\_in\_ptr::sin\_addr |
| --- |

## [◆ ](#ae8ca040f7813d6974e0440f877df6744)sin\_family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sockaddr\_in\_ptr::sin\_family |
| --- |

## [◆ ](#aab1491a8d77ca11d8104ef3ef1bace80)sin\_port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sockaddr\_in\_ptr::sin\_port |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [sockaddr\_in\_ptr](structsockaddr__in__ptr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
