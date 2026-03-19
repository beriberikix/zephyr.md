---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structiovec.html
original_path: doxygen/html/structiovec.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iovec Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

IO vector array element.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [iov\_base](#a07aeddeccf80f14520fdd7ef0759442b) |
|  | Pointer to data. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [iov\_len](#a17b5ac2078fd1adfabb262a95808a07d) |
|  | Length of the data. |

## Detailed Description

IO vector array element.

## Field Documentation

## [◆ ](#a07aeddeccf80f14520fdd7ef0759442b)iov\_base

| void\* iovec::iov\_base |
| --- |

Pointer to data.

## [◆ ](#a17b5ac2078fd1adfabb262a95808a07d)iov\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) iovec::iov\_len |
| --- |

Length of the data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [iovec](structiovec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
