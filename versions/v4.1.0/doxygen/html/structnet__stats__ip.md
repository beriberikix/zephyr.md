---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__ip.html
original_path: doxygen/html/structnet__stats__ip.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_ip Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

IP layer statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#ab6a6373368dd24cb51504c5729d535d3) |
|  | Number of received packets at the IP layer. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#abbe676bbe9faa89b2b6b8c4950b1c9d5) |
|  | Number of sent packets at the IP layer. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [forwarded](#a4bb82a5ebebaa3e8a11973c07eed96a0) |
|  | Number of forwarded packets at the IP layer. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#ac86399b70d7f761162e5336dd15589eb) |
|  | Number of dropped packets at the IP layer. |

## Detailed Description

IP layer statistics.

## Field Documentation

## [◆ ](#ac86399b70d7f761162e5336dd15589eb)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip::drop |
| --- |

Number of dropped packets at the IP layer.

## [◆ ](#a4bb82a5ebebaa3e8a11973c07eed96a0)forwarded

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip::forwarded |
| --- |

Number of forwarded packets at the IP layer.

## [◆ ](#ab6a6373368dd24cb51504c5729d535d3)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip::recv |
| --- |

Number of received packets at the IP layer.

## [◆ ](#abbe676bbe9faa89b2b6b8c4950b1c9d5)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip::sent |
| --- |

Number of sent packets at the IP layer.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_ip](structnet__stats__ip.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
