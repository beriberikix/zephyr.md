---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__stats__ppp.html
original_path: doxygen/html/structnet__stats__ppp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_ppp Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

All PPP specific statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_stats\_bytes](structnet__stats__bytes.md) | [bytes](#ab2b48da7f19d4b83e3f41b41979b7ed8) |
|  | Total number of bytes received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [pkts](#a71fc81f3c5f3e65a476b3391f086d340) |
|  | Total number of packets received and sent. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#ae2e0a47a539e9d7bc97f9c63f889b276) |
|  | Number of received and dropped PPP frames. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [chkerr](#a1332b31980f82236aeb0c3f9444e2ac6) |
|  | Number of received PPP frames with a bad checksum. |

## Detailed Description

All PPP specific statistics.

## Field Documentation

## [◆ ](#ab2b48da7f19d4b83e3f41b41979b7ed8)bytes

| struct [net\_stats\_bytes](structnet__stats__bytes.md) net\_stats\_ppp::bytes |
| --- |

Total number of bytes received and sent.

## [◆ ](#a1332b31980f82236aeb0c3f9444e2ac6)chkerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ppp::chkerr |
| --- |

Number of received PPP frames with a bad checksum.

## [◆ ](#ae2e0a47a539e9d7bc97f9c63f889b276)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_ppp::drop |
| --- |

Number of received and dropped PPP frames.

## [◆ ](#a71fc81f3c5f3e65a476b3391f086d340)pkts

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_ppp::pkts |
| --- |

Total number of packets received and sent.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_ppp](structnet__stats__ppp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
