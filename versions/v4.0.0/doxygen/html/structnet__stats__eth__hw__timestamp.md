---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__stats__eth__hw__timestamp.html
original_path: doxygen/html/structnet__stats__eth__hw__timestamp.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_eth\_hw\_timestamp Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Ethernet hardware timestamp statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rx\_hwtstamp\_cleared](#acd3d5f72d7df568110d96093e0c9534d) |
|  | Number of RX hardware timestamp cleared. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_hwtstamp\_timeouts](#a41f605499dbf88a879522fdfa4633d9e) |
|  | Number of RX hardware timestamp timeout. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_hwtstamp\_skipped](#ae1f983faf4a999308c464e4af5a5284b) |
|  | Number of RX hardware timestamp skipped. |

## Detailed Description

Ethernet hardware timestamp statistics.

## Field Documentation

## [◆ ](#acd3d5f72d7df568110d96093e0c9534d)rx\_hwtstamp\_cleared

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_hw\_timestamp::rx\_hwtstamp\_cleared |
| --- |

Number of RX hardware timestamp cleared.

## [◆ ](#ae1f983faf4a999308c464e4af5a5284b)tx\_hwtstamp\_skipped

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_skipped |
| --- |

Number of RX hardware timestamp skipped.

## [◆ ](#a41f605499dbf88a879522fdfa4633d9e)tx\_hwtstamp\_timeouts

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth\_hw\_timestamp::tx\_hwtstamp\_timeouts |
| --- |

Number of RX hardware timestamp timeout.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
