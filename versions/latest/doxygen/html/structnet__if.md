---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__if.html
original_path: doxygen/html/structnet__if.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| struct [k\_mutex](structk__mutex.md) | [tx\_lock](#af00f729ebddfdcf725169f61b6cd586b) |

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

## [◆ ](#af00f729ebddfdcf725169f61b6cd586b)tx\_lock

| struct [k\_mutex](structk__mutex.md) net\_if::tx\_lock |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if](structnet__if.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
