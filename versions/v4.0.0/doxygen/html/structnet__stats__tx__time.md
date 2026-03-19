---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__stats__tx__time.html
original_path: doxygen/html/structnet__stats__tx__time.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_tx\_time Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Network packet transfer times for calculating average TX time.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sum](#af6f7a26c0344a0f93306e105a8917c3e) |
|  | Sum of network packet transfer times. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [count](#a7a652350ed04e53ba02aec294f8444b4) |
|  | Number of network packets transferred. |

## Detailed Description

Network packet transfer times for calculating average TX time.

## Field Documentation

## [◆ ](#a7a652350ed04e53ba02aec294f8444b4)count

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tx\_time::count |
| --- |

Number of network packets transferred.

## [◆ ](#af6f7a26c0344a0f93306e105a8917c3e)sum

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_stats\_tx\_time::sum |
| --- |

Sum of network packet transfer times.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_tx\_time](structnet__stats__tx__time.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
