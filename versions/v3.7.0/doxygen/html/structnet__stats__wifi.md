---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__stats__wifi.html
original_path: doxygen/html/structnet__stats__wifi.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_wifi Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

All Wi-Fi specific statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) | [sta\_mgmt](#a8bee22961545674e6ab100b58a04bf91) |
|  | Total number of beacon errors. |
| struct [net\_stats\_bytes](structnet__stats__bytes.md) | [bytes](#aa055b1e8bd8f1e50815c1028b562be07) |
|  | Total number of bytes received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [pkts](#adbcdb2dd8733f2917c00a0b2d365393b) |
|  | Total number of packets received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [broadcast](#a03dc04638c4b670bd7f3520d45fc1eda) |
|  | Total number of broadcast packets received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [multicast](#a7e7f68215101885fd51c70e981da26e7) |
|  | Total number of multicast packets received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [errors](#ae0149e64a94a9f96eb6680f94793c8c4) |
|  | Total number of errors in RX and TX. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [unicast](#ae80dcd73a3c5ce3ec3282d1ae827b338) |
|  | Total number of unicast packets received and sent. |

## Detailed Description

All Wi-Fi specific statistics.

## Field Documentation

## [◆ ](#a03dc04638c4b670bd7f3520d45fc1eda)broadcast

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_wifi::broadcast |
| --- |

Total number of broadcast packets received and sent.

## [◆ ](#aa055b1e8bd8f1e50815c1028b562be07)bytes

| struct [net\_stats\_bytes](structnet__stats__bytes.md) net\_stats\_wifi::bytes |
| --- |

Total number of bytes received and sent.

## [◆ ](#ae0149e64a94a9f96eb6680f94793c8c4)errors

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_wifi::errors |
| --- |

Total number of errors in RX and TX.

## [◆ ](#a7e7f68215101885fd51c70e981da26e7)multicast

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_wifi::multicast |
| --- |

Total number of multicast packets received and sent.

## [◆ ](#adbcdb2dd8733f2917c00a0b2d365393b)pkts

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_wifi::pkts |
| --- |

Total number of packets received and sent.

## [◆ ](#a8bee22961545674e6ab100b58a04bf91)sta\_mgmt

| struct [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) net\_stats\_wifi::sta\_mgmt |
| --- |

Total number of beacon errors.

## [◆ ](#ae80dcd73a3c5ce3ec3282d1ae827b338)unicast

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_wifi::unicast |
| --- |

Total number of unicast packets received and sent.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_wifi](structnet__stats__wifi.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
