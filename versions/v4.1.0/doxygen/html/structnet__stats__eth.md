---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__stats__eth.html
original_path: doxygen/html/structnet__stats__eth.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_eth Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

All Ethernet specific statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_stats\_bytes](structnet__stats__bytes.md) | [bytes](#a8c5cf1ead8ba214425a16fed1c2ad0fb) |
|  | Total number of bytes received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [pkts](#a97bd6026b16890743f344751a21107f1) |
|  | Total number of packets received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [broadcast](#a054beb909134b0e0f22f5df599549128) |
|  | Total number of broadcast packets received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [multicast](#a4f6a2903330518a132e7e547820e0bf2) |
|  | Total number of multicast packets received and sent. |
| struct [net\_stats\_pkts](structnet__stats__pkts.md) | [errors](#a9c869740f416fbe0b54d7fefacb1fe29) |
|  | Total number of errors in RX and TX. |
| struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) | [error\_details](#a922feddb17fc020371f1bcc52c709415) |
|  | Total number of errors in RX and TX. |
| struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) | [flow\_control](#a643010ac6360c8c0c08016725ba12222) |
|  | Total number of flow control errors in RX and TX. |
| struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) | [csum](#a2169ae06bace1a93663bccf88c8d7a29) |
|  | Total number of checksum errors in RX and TX. |
| struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) | [hw\_timestamp](#a44667efff73c17c089ed22d5b0da5ad3) |
|  | Total number of hardware timestamp errors in RX and TX. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [collisions](#a822d4205791f59999c842610522f6fc5) |
|  | Total number of collisions. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_dropped](#a257c349cf3d32d38796e3899e702454a) |
|  | Total number of dropped TX packets. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_timeout\_count](#ab351258ae82abd09759d37774559d8bc) |
|  | Total number of TX timeout errors. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [tx\_restart\_queue](#a6699012226e25e8bad39076fed6dbfb5) |
|  | Total number of TX queue restarts. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [unknown\_protocol](#afaacee7cc1d0a35ae2344175421c40dd) |
|  | Total number of RX unknown protocol packets. |

## Detailed Description

All Ethernet specific statistics.

## Field Documentation

## [◆ ](#a054beb909134b0e0f22f5df599549128)broadcast

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_eth::broadcast |
| --- |

Total number of broadcast packets received and sent.

## [◆ ](#a8c5cf1ead8ba214425a16fed1c2ad0fb)bytes

| struct [net\_stats\_bytes](structnet__stats__bytes.md) net\_stats\_eth::bytes |
| --- |

Total number of bytes received and sent.

## [◆ ](#a822d4205791f59999c842610522f6fc5)collisions

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth::collisions |
| --- |

Total number of collisions.

## [◆ ](#a2169ae06bace1a93663bccf88c8d7a29)csum

| struct [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) net\_stats\_eth::csum |
| --- |

Total number of checksum errors in RX and TX.

## [◆ ](#a922feddb17fc020371f1bcc52c709415)error\_details

| struct [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) net\_stats\_eth::error\_details |
| --- |

Total number of errors in RX and TX.

## [◆ ](#a9c869740f416fbe0b54d7fefacb1fe29)errors

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_eth::errors |
| --- |

Total number of errors in RX and TX.

## [◆ ](#a643010ac6360c8c0c08016725ba12222)flow\_control

| struct [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) net\_stats\_eth::flow\_control |
| --- |

Total number of flow control errors in RX and TX.

## [◆ ](#a44667efff73c17c089ed22d5b0da5ad3)hw\_timestamp

| struct [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) net\_stats\_eth::hw\_timestamp |
| --- |

Total number of hardware timestamp errors in RX and TX.

## [◆ ](#a4f6a2903330518a132e7e547820e0bf2)multicast

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_eth::multicast |
| --- |

Total number of multicast packets received and sent.

## [◆ ](#a97bd6026b16890743f344751a21107f1)pkts

| struct [net\_stats\_pkts](structnet__stats__pkts.md) net\_stats\_eth::pkts |
| --- |

Total number of packets received and sent.

## [◆ ](#a257c349cf3d32d38796e3899e702454a)tx\_dropped

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth::tx\_dropped |
| --- |

Total number of dropped TX packets.

## [◆ ](#a6699012226e25e8bad39076fed6dbfb5)tx\_restart\_queue

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth::tx\_restart\_queue |
| --- |

Total number of TX queue restarts.

## [◆ ](#ab351258ae82abd09759d37774559d8bc)tx\_timeout\_count

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth::tx\_timeout\_count |
| --- |

Total number of TX timeout errors.

## [◆ ](#afaacee7cc1d0a35ae2344175421c40dd)unknown\_protocol

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_eth::unknown\_protocol |
| --- |

Total number of RX unknown protocol packets.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_eth](structnet__stats__eth.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
