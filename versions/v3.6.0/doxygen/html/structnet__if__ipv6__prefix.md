---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__if__ipv6__prefix.html
original_path: doxygen/html/structnet__if__ipv6__prefix.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_ipv6\_prefix Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Network Interface IPv6 prefixes.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_timeout](structnet__timeout.md) | [lifetime](#a925a97a49d383bd4ce475f5d09fcb7e3) |
|  | Prefix lifetime. |
| struct [in6\_addr](structin6__addr.md) | [prefix](#a65b450d0942b3c96cfc575b462d82028) |
|  | IPv6 prefix. |
| struct [net\_if](structnet__if.md) \* | [iface](#a0e2d1997e2ccfe1e1af5f16e0c74ed92) |
|  | Backpointer to network interface where this prefix is used. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#a4d2bc2acbe51256b76cf4d3ced3aac39) |
|  | Prefix length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_infinite](#a22090441b27bed06098679bf23b4e1e9): 1 |
|  | Is the IP prefix valid forever. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_used](#a6a4295256957e5eddf149f1ceff62e3f): 1 |
|  | Is this prefix used or not. |

## Detailed Description

Network Interface IPv6 prefixes.

Stores the IPV6 prefixes assigned to this network interface.

## Field Documentation

## [◆ ](#a0e2d1997e2ccfe1e1af5f16e0c74ed92)iface

| struct [net\_if](structnet__if.md)\* net\_if\_ipv6\_prefix::iface |
| --- |

Backpointer to network interface where this prefix is used.

## [◆ ](#a22090441b27bed06098679bf23b4e1e9)is\_infinite

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv6\_prefix::is\_infinite |
| --- |

Is the IP prefix valid forever.

## [◆ ](#a6a4295256957e5eddf149f1ceff62e3f)is\_used

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv6\_prefix::is\_used |
| --- |

Is this prefix used or not.

## [◆ ](#a4d2bc2acbe51256b76cf4d3ced3aac39)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv6\_prefix::len |
| --- |

Prefix length.

## [◆ ](#a925a97a49d383bd4ce475f5d09fcb7e3)lifetime

| struct [net\_timeout](structnet__timeout.md) net\_if\_ipv6\_prefix::lifetime |
| --- |

Prefix lifetime.

## [◆ ](#a65b450d0942b3c96cfc575b462d82028)prefix

| struct [in6\_addr](structin6__addr.md) net\_if\_ipv6\_prefix::prefix |
| --- |

IPv6 prefix.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
