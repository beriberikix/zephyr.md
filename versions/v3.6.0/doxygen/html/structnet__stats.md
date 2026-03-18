---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__stats.html
original_path: doxygen/html/structnet__stats.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

All network statistics in one struct.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [processing\_error](#a3a4c90661d6b310b628262228a341fe2) |
|  | Count of malformed packets or packets we do not have handler for. |
| struct [net\_stats\_bytes](structnet__stats__bytes.md) | [bytes](#a7a28233e6d23efdce0143469b9bb6c05) |
|  | This calculates amount of data transferred through all the network interfaces. |
| struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) | [ip\_errors](#ac42cb13954d164e92a1ef60919a2a34e) |
|  | IP layer errors. |

## Detailed Description

All network statistics in one struct.

## Field Documentation

## [◆ ](#a7a28233e6d23efdce0143469b9bb6c05)bytes

| struct [net\_stats\_bytes](structnet__stats__bytes.md) net\_stats::bytes |
| --- |

This calculates amount of data transferred through all the network interfaces.

## [◆ ](#ac42cb13954d164e92a1ef60919a2a34e)ip\_errors

| struct [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) net\_stats::ip\_errors |
| --- |

IP layer errors.

## [◆ ](#a3a4c90661d6b310b628262228a341fe2)processing\_error

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats::processing\_error |
| --- |

Count of malformed packets or packets we do not have handler for.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats](structnet__stats.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
