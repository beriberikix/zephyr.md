---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structnet__stats__pkt__filter.html
original_path: doxygen/html/structnet__stats__pkt__filter.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_pkt\_filter Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Network packet filter statistics.
[More...](#details)

`#include <[zephyr/net/net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [drop](#a62d2d86781e6224b09f21929f27b2ef7) |  |
|  | Network packets dropped at network interface level. [More...](#a62d2d86781e6224b09f21929f27b2ef7) |
| } | [rx](#a8cf9912d574873832b85a614eb776789) |
|  | Network packet filter RX statistics. |
| struct { |  |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [drop](#a62d2d86781e6224b09f21929f27b2ef7) |  |
|  | Network packets dropped at network interface level. [More...](#a62d2d86781e6224b09f21929f27b2ef7) |
| } | [tx](#a5e88001e143c0adb129ca93b108c277d) |
|  | Network packet filter TX statistics. |

## Detailed Description

Network packet filter statistics.

## Field Documentation

## [◆ ](#a62d2d86781e6224b09f21929f27b2ef7)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_pkt\_filter::drop |
| --- |

Network packets dropped at network interface level.

## [◆ ](#a8cf9912d574873832b85a614eb776789)[struct]

| struct { ... } net\_stats\_pkt\_filter::rx |
| --- |

Network packet filter RX statistics.

## [◆ ](#a5e88001e143c0adb129ca93b108c277d)[struct]

| struct { ... } net\_stats\_pkt\_filter::tx |
| --- |

Network packet filter TX statistics.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_pkt\_filter](structnet__stats__pkt__filter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
