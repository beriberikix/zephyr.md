---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__stats__ip__errors.html
original_path: doxygen/html/structnet__stats__ip__errors.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_ip\_errors Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

IP layer error statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [vhlerr](#a3e476f659ebeaa5c5f7b6dad2d90326f) |
|  | Number of packets dropped due to wrong IP version or header length. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [hblenerr](#a06b35742c418ebc6414fcb5c7002edde) |
|  | Number of packets dropped due to wrong IP length, high byte. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [lblenerr](#a9b4bf05e9df13e1d99518125b9067bef) |
|  | Number of packets dropped due to wrong IP length, low byte. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [fragerr](#ab84ee9dfbe5da391d60c6e3ae9abea16) |
|  | Number of packets dropped because they were IP fragments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [chkerr](#a872cc0beca45bbe87ae794dd8ca4e301) |
|  | Number of packets dropped due to IP checksum errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [protoerr](#a978b1c23847e707ac1fa27c2b34fa85d) |
|  | Number of packets dropped because they were neither ICMP, UDP nor TCP. |

## Detailed Description

IP layer error statistics.

## Field Documentation

## [◆ ](#a872cc0beca45bbe87ae794dd8ca4e301)chkerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip\_errors::chkerr |
| --- |

Number of packets dropped due to IP checksum errors.

## [◆ ](#ab84ee9dfbe5da391d60c6e3ae9abea16)fragerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip\_errors::fragerr |
| --- |

Number of packets dropped because they were IP fragments.

## [◆ ](#a06b35742c418ebc6414fcb5c7002edde)hblenerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip\_errors::hblenerr |
| --- |

Number of packets dropped due to wrong IP length, high byte.

## [◆ ](#a9b4bf05e9df13e1d99518125b9067bef)lblenerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip\_errors::lblenerr |
| --- |

Number of packets dropped due to wrong IP length, low byte.

## [◆ ](#a978b1c23847e707ac1fa27c2b34fa85d)protoerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip\_errors::protoerr |
| --- |

Number of packets dropped because they were neither ICMP, UDP nor TCP.

## [◆ ](#a3e476f659ebeaa5c5f7b6dad2d90326f)vhlerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ip\_errors::vhlerr |
| --- |

Number of packets dropped due to wrong IP version or header length.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_ip\_errors](structnet__stats__ip__errors.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
