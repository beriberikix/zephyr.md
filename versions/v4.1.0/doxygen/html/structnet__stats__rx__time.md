---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__rx__time.html
original_path: doxygen/html/structnet__stats__rx__time.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_rx\_time Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Network packet receive times for calculating average RX time.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sum](#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d) |
|  | Sum of network packet receive times. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [count](#a68247051b064de081fa2e84118192958) |
|  | Number of network packets received. |

## Detailed Description

Network packet receive times for calculating average RX time.

## Field Documentation

## [◆ ](#a68247051b064de081fa2e84118192958)count

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_rx\_time::count |
| --- |

Number of network packets received.

## [◆ ](#a4b84c2ae2fda8fcd75fdf1bf0b2aae8d)sum

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_stats\_rx\_time::sum |
| --- |

Sum of network packet receive times.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_rx\_time](structnet__stats__rx__time.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
