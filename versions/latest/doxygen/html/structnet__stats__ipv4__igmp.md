---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__stats__ipv4__igmp.html
original_path: doxygen/html/structnet__stats__ipv4__igmp.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_ipv4\_igmp Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

IPv4 IGMP daemon statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#a469113de7af0ba42dbd1b0365d00602c) |
|  | Number of received IPv4 IGMP queries. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#a955e20a6ee5e19e08000b3114b9d71a6) |
|  | Number of sent IPv4 IGMP reports. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#a1c37702ff837b8c5cc9df5f690e7678c) |
|  | Number of dropped IPv4 IGMP packets. |

## Detailed Description

IPv4 IGMP daemon statistics.

## Field Documentation

## [◆ ](#a1c37702ff837b8c5cc9df5f690e7678c)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv4\_igmp::drop |
| --- |

Number of dropped IPv4 IGMP packets.

## [◆ ](#a469113de7af0ba42dbd1b0365d00602c)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv4\_igmp::recv |
| --- |

Number of received IPv4 IGMP queries.

## [◆ ](#a955e20a6ee5e19e08000b3114b9d71a6)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv4\_igmp::sent |
| --- |

Number of sent IPv4 IGMP reports.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
