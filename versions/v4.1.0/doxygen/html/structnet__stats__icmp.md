---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__icmp.html
original_path: doxygen/html/structnet__stats__icmp.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_icmp Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

ICMP statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#ae6f226b55565c11fca0c9e099f08c267) |
|  | Number of received ICMP packets. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#a2d6eb7dfc8f4b439b399b039022f2889) |
|  | Number of sent ICMP packets. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#a755f3388c05d4bd2988ddd16d1a4cf32) |
|  | Number of dropped ICMP packets. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [typeerr](#ae1a29dd9b8e1ce9a737fa7f36c805cd4) |
|  | Number of ICMP packets with a wrong type. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [chkerr](#a6662bc547107a08c52e902a2446629bf) |
|  | Number of ICMP packets with a bad checksum. |

## Detailed Description

ICMP statistics.

## Field Documentation

## [◆ ](#a6662bc547107a08c52e902a2446629bf)chkerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_icmp::chkerr |
| --- |

Number of ICMP packets with a bad checksum.

## [◆ ](#a755f3388c05d4bd2988ddd16d1a4cf32)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_icmp::drop |
| --- |

Number of dropped ICMP packets.

## [◆ ](#ae6f226b55565c11fca0c9e099f08c267)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_icmp::recv |
| --- |

Number of received ICMP packets.

## [◆ ](#a2d6eb7dfc8f4b439b399b039022f2889)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_icmp::sent |
| --- |

Number of sent ICMP packets.

## [◆ ](#ae1a29dd9b8e1ce9a737fa7f36c805cd4)typeerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_icmp::typeerr |
| --- |

Number of ICMP packets with a wrong type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_icmp](structnet__stats__icmp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
