---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsockaddr__ll.html
original_path: doxygen/html/structsockaddr__ll.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sockaddr\_ll Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

Socket address struct for packet socket.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [sll\_family](#a4920e92fb0613ba8594a6b6c226048d9) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sll\_protocol](#a661e329c10a8f06a85ad831630273e49) |
| int | [sll\_ifindex](#a93b4976ed8e9d58cdcc620f5d1987f68) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sll\_hatype](#a2df317106a30498dd9f87e1d4eefc8fc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sll\_pkttype](#a2001fcf2627149283e3460b18f44b313) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sll\_halen](#acb72ab39a239d9e5752b7422dc9a2dc6) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sll\_addr](#aee52affe8837ffe1c32c94ce34117d6a) [8] |

## Detailed Description

Socket address struct for packet socket.

## Field Documentation

## [◆ ](#aee52affe8837ffe1c32c94ce34117d6a)sll\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sockaddr\_ll::sll\_addr[8] |
| --- |

## [◆ ](#a4920e92fb0613ba8594a6b6c226048d9)sll\_family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sockaddr\_ll::sll\_family |
| --- |

## [◆ ](#acb72ab39a239d9e5752b7422dc9a2dc6)sll\_halen

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sockaddr\_ll::sll\_halen |
| --- |

## [◆ ](#a2df317106a30498dd9f87e1d4eefc8fc)sll\_hatype

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sockaddr\_ll::sll\_hatype |
| --- |

## [◆ ](#a93b4976ed8e9d58cdcc620f5d1987f68)sll\_ifindex

| int sockaddr\_ll::sll\_ifindex |
| --- |

## [◆ ](#a2001fcf2627149283e3460b18f44b313)sll\_pkttype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sockaddr\_ll::sll\_pkttype |
| --- |

## [◆ ](#a661e329c10a8f06a85ad831630273e49)sll\_protocol

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sockaddr\_ll::sll\_protocol |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [sockaddr\_ll](structsockaddr__ll.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
