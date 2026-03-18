---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsockaddr__ll__ptr.html
original_path: doxygen/html/structsockaddr__ll__ptr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sockaddr\_ll\_ptr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [sll\_family](#aab6bfff94bf5880375e7538be72a11c1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sll\_protocol](#ad25fe5fef518de3652cf67d25582e50c) |
| int | [sll\_ifindex](#a47a2543cc247cba79cbaaf82787aa9cf) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sll\_hatype](#a337cef9822b70d31b50135f158c54b5d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sll\_pkttype](#a6fa3dcd69fefa59a6da37bde8160104b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sll\_halen](#ab27a07520cee5183aa62e7a0615f1c5f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [sll\_addr](#a28579052ff6eda21d5f060e2c8de2421) |

## Field Documentation

## [◆ ](#a28579052ff6eda21d5f060e2c8de2421)sll\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* sockaddr\_ll\_ptr::sll\_addr |
| --- |

## [◆ ](#aab6bfff94bf5880375e7538be72a11c1)sll\_family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sockaddr\_ll\_ptr::sll\_family |
| --- |

## [◆ ](#ab27a07520cee5183aa62e7a0615f1c5f)sll\_halen

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sockaddr\_ll\_ptr::sll\_halen |
| --- |

## [◆ ](#a337cef9822b70d31b50135f158c54b5d)sll\_hatype

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sockaddr\_ll\_ptr::sll\_hatype |
| --- |

## [◆ ](#a47a2543cc247cba79cbaaf82787aa9cf)sll\_ifindex

| int sockaddr\_ll\_ptr::sll\_ifindex |
| --- |

## [◆ ](#a6fa3dcd69fefa59a6da37bde8160104b)sll\_pkttype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sockaddr\_ll\_ptr::sll\_pkttype |
| --- |

## [◆ ](#ad25fe5fef518de3652cf67d25582e50c)sll\_protocol

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sockaddr\_ll\_ptr::sll\_protocol |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [sockaddr\_ll\_ptr](structsockaddr__ll__ptr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
