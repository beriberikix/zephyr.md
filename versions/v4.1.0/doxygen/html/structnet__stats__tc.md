---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__tc.html
original_path: doxygen/html/structnet__stats__tc.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
|  | Helper for calculating average TX time statistics. [More...](#a30288ef3bb0796cd18c3cf0aedbe875a) |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [pkts](#a6614b5f5186635415a7d787260c39248) |  |
|  | Number of packets sent for this traffic class. [More...](#a6614b5f5186635415a7d787260c39248) |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [dropped](#a1794f71f7fe7b3d20d406be4b28eb032) |  |
|  | Number of packets dropped for this traffic class. [More...](#a1794f71f7fe7b3d20d406be4b28eb032) |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [bytes](#a192a7ec0d24bce9e62f766e481ee5709) |  |
|  | Number of bytes sent for this traffic class. [More...](#a192a7ec0d24bce9e62f766e481ee5709) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [priority](#a8a5c2e59990407ddbfc7973a1c183bf6) |  |
|  | Priority of this traffic class. [More...](#a8a5c2e59990407ddbfc7973a1c183bf6) |
| } | [sent](#a8d6a3ebcc49ce8c34a5faae986f648e2) [NET\_TC\_TX\_STATS\_COUNT] |
|  | TX statistics for each traffic class. |
| struct { |  |
| struct [net\_stats\_rx\_time](structnet__stats__rx__time.md)   [rx\_time](#a8ea00824bb0fb18e4d8912343e01c3b7) |  |
|  | Helper for calculating average RX time statistics. [More...](#a8ea00824bb0fb18e4d8912343e01c3b7) |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [pkts](#a6614b5f5186635415a7d787260c39248) |  |
|  | Number of packets received for this traffic class. [More...](#a6614b5f5186635415a7d787260c39248) |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [dropped](#a1794f71f7fe7b3d20d406be4b28eb032) |  |
|  | Number of packets dropped for this traffic class. [More...](#a1794f71f7fe7b3d20d406be4b28eb032) |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752)   [bytes](#a192a7ec0d24bce9e62f766e481ee5709) |  |
|  | Number of bytes received for this traffic class. [More...](#a192a7ec0d24bce9e62f766e481ee5709) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [priority](#a8a5c2e59990407ddbfc7973a1c183bf6) |  |
|  | Priority of this traffic class. [More...](#a8a5c2e59990407ddbfc7973a1c183bf6) |
| } | [recv](#a2c8826e27ff59154f14a1755ffd4c594) [NET\_TC\_RX\_STATS\_COUNT] |
|  | RX statistics for each traffic class. |

## Detailed Description

Traffic class statistics.

## Field Documentation

## [◆ ](#a192a7ec0d24bce9e62f766e481ee5709)bytes

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tc::bytes |
| --- |

Number of bytes sent for this traffic class.

Number of bytes received for this traffic class.

## [◆ ](#a1794f71f7fe7b3d20d406be4b28eb032)dropped

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tc::dropped |
| --- |

Number of packets dropped for this traffic class.

## [◆ ](#a6614b5f5186635415a7d787260c39248)pkts

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tc::pkts |
| --- |

Number of packets sent for this traffic class.

Number of packets received for this traffic class.

## [◆ ](#a8a5c2e59990407ddbfc7973a1c183bf6)priority

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_stats\_tc::priority |
| --- |

Priority of this traffic class.

## [◆ ](#a2c8826e27ff59154f14a1755ffd4c594)[struct]

| struct { ... } net\_stats\_tc::recv[NET\_TC\_RX\_STATS\_COUNT] |
| --- |

RX statistics for each traffic class.

## [◆ ](#a8ea00824bb0fb18e4d8912343e01c3b7)rx\_time

| struct [net\_stats\_rx\_time](structnet__stats__rx__time.md) net\_stats\_tc::rx\_time |
| --- |

Helper for calculating average RX time statistics.

## [◆ ](#a8d6a3ebcc49ce8c34a5faae986f648e2)[struct]

| struct { ... } net\_stats\_tc::sent[NET\_TC\_TX\_STATS\_COUNT] |
| --- |

TX statistics for each traffic class.

## [◆ ](#a30288ef3bb0796cd18c3cf0aedbe875a)tx\_time

| struct [net\_stats\_tx\_time](structnet__stats__tx__time.md) net\_stats\_tc::tx\_time |
| --- |

Helper for calculating average TX time statistics.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_tc](structnet__stats__tc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
