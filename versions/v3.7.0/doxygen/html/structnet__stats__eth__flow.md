---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__stats__eth__flow.html
original_path: doxygen/html/structnet__stats__eth__flow.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_eth\_flow Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Ethernet flow control statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_flow\_control\_xon](#a08e5da4ff78fe3893b9c9a628cefe4f2) |
|  | Number of RX XON flow control. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_flow\_control\_xoff](#a8f9b93537b3c11be70f276aaa72cb637) |
|  | Number of RX XOFF flow control. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_flow\_control\_xon](#a31412e8bf9d38ba630ea856e958a48d7) |
|  | Number of TX XON flow control. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_flow\_control\_xoff](#a969d81f9db20312d2d2aa7f70f93bdd5) |
|  | Number of TX XOFF flow control. |

## Detailed Description

Ethernet flow control statistics.

## Field Documentation

## [◆ ](#a8f9b93537b3c11be70f276aaa72cb637)rx\_flow\_control\_xoff

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_flow::rx\_flow\_control\_xoff |
| --- |

Number of RX XOFF flow control.

## [◆ ](#a08e5da4ff78fe3893b9c9a628cefe4f2)rx\_flow\_control\_xon

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_flow::rx\_flow\_control\_xon |
| --- |

Number of RX XON flow control.

## [◆ ](#a969d81f9db20312d2d2aa7f70f93bdd5)tx\_flow\_control\_xoff

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_flow::tx\_flow\_control\_xoff |
| --- |

Number of TX XOFF flow control.

## [◆ ](#a31412e8bf9d38ba630ea856e958a48d7)tx\_flow\_control\_xon

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_flow::tx\_flow\_control\_xon |
| --- |

Number of TX XON flow control.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_eth\_flow](structnet__stats__eth__flow.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
