---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__udp.html
original_path: doxygen/html/structnet__stats__udp.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_udp Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

UDP statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#a2d884bf9106e60d430ffec7c7964a609) |
|  | Number of dropped UDP segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#a0ea91d85fe322661fb909f5e94e55a34) |
|  | Number of received UDP segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#ab4e8228c221901d3ded55f3f823bfa1c) |
|  | Number of sent UDP segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [chkerr](#a4c57d5f68ebda7981400729b9c7fe0f7) |
|  | Number of UDP segments with a bad checksum. |

## Detailed Description

UDP statistics.

## Field Documentation

## [◆ ](#a4c57d5f68ebda7981400729b9c7fe0f7)chkerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_udp::chkerr |
| --- |

Number of UDP segments with a bad checksum.

## [◆ ](#a2d884bf9106e60d430ffec7c7964a609)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_udp::drop |
| --- |

Number of dropped UDP segments.

## [◆ ](#a0ea91d85fe322661fb909f5e94e55a34)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_udp::recv |
| --- |

Number of received UDP segments.

## [◆ ](#ab4e8228c221901d3ded55f3f823bfa1c)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_udp::sent |
| --- |

Number of sent UDP segments.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_udp](structnet__stats__udp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
