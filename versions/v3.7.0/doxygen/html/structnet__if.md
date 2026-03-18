---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__if.html
original_path: doxygen/html/structnet__if.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Network Interface structure.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_if\_dev](structnet__if__dev.md) \* | [if\_dev](#a0982ba2019cdaa7701162e60fdb2171e) |
|  | The [net\_if\_dev](structnet__if__dev.md "Network Interface Device structure.") instance the [net\_if](structnet__if.md "Network Interface structure.") is related to. |
| struct [net\_if\_config](structnet__if__config.md) | [config](#a5e71962f55bdead7bfbbb96518c6c404) |
|  | Network interface instance configuration. |
| struct [k\_mutex](structk__mutex.md) | [lock](#ace2233b71da53ff0fc7cd564ccfc5a03) |
|  | Mutex protecting this network interface instance. |
| struct [k\_mutex](structk__mutex.md) | [tx\_lock](#af00f729ebddfdcf725169f61b6cd586b) |
|  | Mutex used when sending data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pe\_enabled](#aa96a6a2d55f6a4ece2f340eef526ef56): 1 |
|  | Network interface specific flags. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pe\_prefer\_public](#aec585e283c9053443ff05b364acf76eb): 1 |
|  | If PE is enabled, then this tells whether public addresses are preferred over temporary ones for this interface. |

## Detailed Description

Network Interface structure.

Used to handle a network interface on top of a [net\_if\_dev](structnet__if__dev.md "Network Interface Device structure.") instance. There can be many [net\_if](structnet__if.md "Network Interface structure.") instance against the same [net\_if\_dev](structnet__if__dev.md "Network Interface Device structure.") instance.

## Field Documentation

## [◆ ](#a5e71962f55bdead7bfbbb96518c6c404)config

| struct [net\_if\_config](structnet__if__config.md) net\_if::config |
| --- |

Network interface instance configuration.

## [◆ ](#a0982ba2019cdaa7701162e60fdb2171e)if\_dev

| struct [net\_if\_dev](structnet__if__dev.md)\* net\_if::if\_dev |
| --- |

The [net\_if\_dev](structnet__if__dev.md "Network Interface Device structure.") instance the [net\_if](structnet__if.md "Network Interface structure.") is related to.

## [◆ ](#ace2233b71da53ff0fc7cd564ccfc5a03)lock

| struct [k\_mutex](structk__mutex.md) net\_if::lock |
| --- |

Mutex protecting this network interface instance.

## [◆ ](#aa96a6a2d55f6a4ece2f340eef526ef56)pe\_enabled

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if::pe\_enabled |
| --- |

Network interface specific flags.

Enable IPv6 privacy extension (RFC 8981), this is enabled by default if PE support is enabled in configuration.

## [◆ ](#aec585e283c9053443ff05b364acf76eb)pe\_prefer\_public

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if::pe\_prefer\_public |
| --- |

If PE is enabled, then this tells whether public addresses are preferred over temporary ones for this interface.

## [◆ ](#af00f729ebddfdcf725169f61b6cd586b)tx\_lock

| struct [k\_mutex](structk__mutex.md) net\_if::tx\_lock |
| --- |

Mutex used when sending data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if](structnet__if.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
