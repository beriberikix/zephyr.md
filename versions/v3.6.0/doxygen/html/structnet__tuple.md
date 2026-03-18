---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__tuple.html
original_path: doxygen/html/structnet__tuple.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_tuple Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

IPv6/IPv4 network connection tuple.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_addr \* | [remote\_addr](#a8f9a1aab3c3aedeead795ca6624d4d6d) |
|  | IPv6/IPv4 remote address. |
| struct net\_addr \* | [local\_addr](#af7004f8f8d74d49d6771393825612294) |
|  | IPv6/IPv4 local address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [remote\_port](#ab4c31093a23bc60d8dcf5b784e3fb39a) |
|  | UDP/TCP remote port. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [local\_port](#a9a1cd0dd55a9e866cb0e910120362b7e) |
|  | UDP/TCP local port. |
| enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) | [ip\_proto](#aa9eeba2c8e263afbf6368e04353d6014) |
|  | IP protocol. |

## Detailed Description

IPv6/IPv4 network connection tuple.

## Field Documentation

## [◆ ](#aa9eeba2c8e263afbf6368e04353d6014)ip\_proto

| enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) net\_tuple::ip\_proto |
| --- |

IP protocol.

## [◆ ](#af7004f8f8d74d49d6771393825612294)local\_addr

| struct net\_addr\* net\_tuple::local\_addr |
| --- |

IPv6/IPv4 local address.

## [◆ ](#a9a1cd0dd55a9e866cb0e910120362b7e)local\_port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_tuple::local\_port |
| --- |

UDP/TCP local port.

## [◆ ](#a8f9a1aab3c3aedeead795ca6624d4d6d)remote\_addr

| struct net\_addr\* net\_tuple::remote\_addr |
| --- |

IPv6/IPv4 remote address.

## [◆ ](#ab4c31093a23bc60d8dcf5b784e3fb39a)remote\_port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_tuple::remote\_port |
| --- |

UDP/TCP remote port.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [net\_tuple](structnet__tuple.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
