---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__stats__ipv6__mld.html
original_path: doxygen/html/structnet__stats__ipv6__mld.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_ipv6\_mld Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

IPv6 multicast listener daemon statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#a4879ff9e31f8b60973d3b169598e921d) |
|  | Number of received IPv6 MLD queries. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#ab397b74b14ce7047bf2fc63ca72ce1e5) |
|  | Number of sent IPv6 MLD reports. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#ad85dc87f57296a1e7d64e959b0370ee8) |
|  | Number of dropped IPv6 MLD packets. |

## Detailed Description

IPv6 multicast listener daemon statistics.

## Field Documentation

## [◆ ](#ad85dc87f57296a1e7d64e959b0370ee8)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv6\_mld::drop |
| --- |

Number of dropped IPv6 MLD packets.

## [◆ ](#a4879ff9e31f8b60973d3b169598e921d)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv6\_mld::recv |
| --- |

Number of received IPv6 MLD queries.

## [◆ ](#ab397b74b14ce7047bf2fc63ca72ce1e5)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv6\_mld::sent |
| --- |

Number of sent IPv6 MLD reports.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
