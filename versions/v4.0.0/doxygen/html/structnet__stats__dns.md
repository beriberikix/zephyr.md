---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__stats__dns.html
original_path: doxygen/html/structnet__stats__dns.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_dns Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

DNS statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#abc9be2039a3ff9e62b956ae27fd0ab84) |
|  | Number of received DNS queries. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#ac07b9f4d084b978cc11e7799fb71a435) |
|  | Number of sent DNS responses. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#a04756603a183f35dbf6f55000556b546) |
|  | Number of dropped DNS packets. |

## Detailed Description

DNS statistics.

## Field Documentation

## [◆ ](#a04756603a183f35dbf6f55000556b546)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_dns::drop |
| --- |

Number of dropped DNS packets.

## [◆ ](#abc9be2039a3ff9e62b956ae27fd0ab84)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_dns::recv |
| --- |

Number of received DNS queries.

## [◆ ](#ac07b9f4d084b978cc11e7799fb71a435)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_dns::sent |
| --- |

Number of sent DNS responses.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_dns](structnet__stats__dns.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
