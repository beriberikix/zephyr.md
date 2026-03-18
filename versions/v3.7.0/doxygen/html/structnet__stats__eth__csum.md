---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__stats__eth__csum.html
original_path: doxygen/html/structnet__stats__eth__csum.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_eth\_csum Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Ethernet checksum statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_csum\_offload\_good](#a1f1ba5c01c6232cd739d069ddb871b17) |
|  | Number of good RX checksum offloading. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_csum\_offload\_errors](#ac4fc04d66193070d4f52a4c07f29ccce) |
|  | Number of failed RX checksum offloading. |

## Detailed Description

Ethernet checksum statistics.

## Field Documentation

## [◆ ](#ac4fc04d66193070d4f52a4c07f29ccce)rx\_csum\_offload\_errors

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_csum::rx\_csum\_offload\_errors |
| --- |

Number of failed RX checksum offloading.

## [◆ ](#a1f1ba5c01c6232cd739d069ddb871b17)rx\_csum\_offload\_good

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_csum::rx\_csum\_offload\_good |
| --- |

Number of good RX checksum offloading.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_eth\_csum](structnet__stats__eth__csum.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
