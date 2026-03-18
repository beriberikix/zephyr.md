---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__stats__tc.html
original_path: doxygen/html/structnet__stats__tc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_tc Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Traffic class statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| struct [net\_stats\_tx\_time](structnet__stats__tx__time.md)   [tx\_time](#a30288ef3bb0796cd18c3cf0aedbe875a) |  |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [pkts](#a6614b5f5186635415a7d787260c39248) |  |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [bytes](#a192a7ec0d24bce9e62f766e481ee5709) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [priority](#a8a5c2e59990407ddbfc7973a1c183bf6) |  |
| } | [sent](#a303e66b023d64b46b621e3384be8b822) [1] |
| struct { |  |
| struct [net\_stats\_rx\_time](structnet__stats__rx__time.md)   [rx\_time](#a8ea00824bb0fb18e4d8912343e01c3b7) |  |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [pkts](#a6614b5f5186635415a7d787260c39248) |  |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [bytes](#a192a7ec0d24bce9e62f766e481ee5709) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [priority](#a8a5c2e59990407ddbfc7973a1c183bf6) |  |
| } | [recv](#a7afde5c8f85e6bef304493d9c2fa6fdb) [1] |

## Detailed Description

Traffic class statistics.

## Field Documentation

## [◆ ](#a192a7ec0d24bce9e62f766e481ee5709)bytes

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tc::bytes |
| --- |

## [◆ ](#a6614b5f5186635415a7d787260c39248)pkts

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tc::pkts |
| --- |

## [◆ ](#a8a5c2e59990407ddbfc7973a1c183bf6)priority

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_stats\_tc::priority |
| --- |

## [◆ ](#a7afde5c8f85e6bef304493d9c2fa6fdb)[struct]

| struct { ... } net\_stats\_tc::recv[ 1 ] |
| --- |

## [◆ ](#a8ea00824bb0fb18e4d8912343e01c3b7)rx\_time

| struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) net\_stats\_tc::rx\_time |
| --- |

## [◆ ](#a303e66b023d64b46b621e3384be8b822)[struct]

| struct { ... } net\_stats\_tc::sent[ 1 ] |
| --- |

## [◆ ](#a30288ef3bb0796cd18c3cf0aedbe875a)tx\_time

| struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) net\_stats\_tc::tx\_time |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_tc](structnet__stats__tc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
