---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__ipv6__pmtu.html
original_path: doxygen/html/structnet__stats__ipv6__pmtu.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_ipv6\_pmtu Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

IPv6 Path MTU Discovery statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#a68b19ebb61e84eb876178a31c7a4e327) |
|  | Number of dropped IPv6 PMTU packets. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#a66346cd9140e30727d77648f65345762) |
|  | Number of received IPv6 PMTU packets. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#a698f5794b73896f7a66def2d3209fafd) |
|  | Number of sent IPv6 PMTU packets. |

## Detailed Description

IPv6 Path MTU Discovery statistics.

## Field Documentation

## [◆ ](#a68b19ebb61e84eb876178a31c7a4e327)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv6\_pmtu::drop |
| --- |

Number of dropped IPv6 PMTU packets.

## [◆ ](#a66346cd9140e30727d77648f65345762)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv6\_pmtu::recv |
| --- |

Number of received IPv6 PMTU packets.

## [◆ ](#a698f5794b73896f7a66def2d3209fafd)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv6\_pmtu::sent |
| --- |

Number of sent IPv6 PMTU packets.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_ipv6\_pmtu](structnet__stats__ipv6__pmtu.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
