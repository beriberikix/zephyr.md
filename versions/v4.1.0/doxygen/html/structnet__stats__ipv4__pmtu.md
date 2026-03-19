---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__ipv4__pmtu.html
original_path: doxygen/html/structnet__stats__ipv4__pmtu.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_ipv4\_pmtu Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

IPv4 Path MTU Discovery statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#ad35f9defad7c5ce29e510b8051788977) |
|  | Number of dropped IPv4 PMTU packets. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#a64245eb7b9b1fcfa0f0efcb53eff7ec2) |
|  | Number of received IPv4 PMTU packets. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#a44f1028694d4001cd4a43f925f0bf0da) |
|  | Number of sent IPv4 PMTU packets. |

## Detailed Description

IPv4 Path MTU Discovery statistics.

## Field Documentation

## [◆ ](#ad35f9defad7c5ce29e510b8051788977)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv4\_pmtu::drop |
| --- |

Number of dropped IPv4 PMTU packets.

## [◆ ](#a64245eb7b9b1fcfa0f0efcb53eff7ec2)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv4\_pmtu::recv |
| --- |

Number of received IPv4 PMTU packets.

## [◆ ](#a44f1028694d4001cd4a43f925f0bf0da)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ipv4\_pmtu::sent |
| --- |

Number of sent IPv4 PMTU packets.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_ipv4\_pmtu](structnet__stats__ipv4__pmtu.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
