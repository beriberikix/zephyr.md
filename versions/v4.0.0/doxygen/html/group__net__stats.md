---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__net__stats.html
original_path: doxygen/html/group__net__stats.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Statistics Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network statistics library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_stats\_bytes](structnet__stats__bytes.md) |
|  | Number of bytes sent and received. [More...](structnet__stats__bytes.md#details) |
| struct | [net\_stats\_pkts](structnet__stats__pkts.md) |
|  | Number of network packets sent and received. [More...](structnet__stats__pkts.md#details) |
| struct | [net\_stats\_ip](structnet__stats__ip.md) |
|  | IP layer statistics. [More...](structnet__stats__ip.md#details) |
| struct | [net\_stats\_ip\_errors](structnet__stats__ip__errors.md) |
|  | IP layer error statistics. [More...](structnet__stats__ip__errors.md#details) |
| struct | [net\_stats\_icmp](structnet__stats__icmp.md) |
|  | ICMP statistics. [More...](structnet__stats__icmp.md#details) |
| struct | [net\_stats\_tcp](structnet__stats__tcp.md) |
|  | TCP statistics. [More...](structnet__stats__tcp.md#details) |
| struct | [net\_stats\_udp](structnet__stats__udp.md) |
|  | UDP statistics. [More...](structnet__stats__udp.md#details) |
| struct | [net\_stats\_ipv6\_nd](structnet__stats__ipv6__nd.md) |
|  | IPv6 neighbor discovery statistics. [More...](structnet__stats__ipv6__nd.md#details) |
| struct | [net\_stats\_ipv6\_mld](structnet__stats__ipv6__mld.md) |
|  | IPv6 multicast listener daemon statistics. [More...](structnet__stats__ipv6__mld.md#details) |
| struct | [net\_stats\_ipv4\_igmp](structnet__stats__ipv4__igmp.md) |
|  | IPv4 IGMP daemon statistics. [More...](structnet__stats__ipv4__igmp.md#details) |
| struct | [net\_stats\_dns](structnet__stats__dns.md) |
|  | DNS statistics. [More...](structnet__stats__dns.md#details) |
| struct | [net\_stats\_tx\_time](structnet__stats__tx__time.md) |
|  | Network packet transfer times for calculating average TX time. [More...](structnet__stats__tx__time.md#details) |
| struct | [net\_stats\_rx\_time](structnet__stats__rx__time.md) |
|  | Network packet receive times for calculating average RX time. [More...](structnet__stats__rx__time.md#details) |
| struct | [net\_stats\_tc](structnet__stats__tc.md) |
|  | Traffic class statistics. [More...](structnet__stats__tc.md#details) |
| struct | [net\_stats\_pm](structnet__stats__pm.md) |
|  | Power management statistics. [More...](structnet__stats__pm.md#details) |
| struct | [net\_stats](structnet__stats.md) |
|  | All network statistics in one struct. [More...](structnet__stats.md#details) |
| struct | [net\_stats\_eth\_errors](structnet__stats__eth__errors.md) |
|  | Ethernet error statistics. [More...](structnet__stats__eth__errors.md#details) |
| struct | [net\_stats\_eth\_flow](structnet__stats__eth__flow.md) |
|  | Ethernet flow control statistics. [More...](structnet__stats__eth__flow.md#details) |
| struct | [net\_stats\_eth\_csum](structnet__stats__eth__csum.md) |
|  | Ethernet checksum statistics. [More...](structnet__stats__eth__csum.md#details) |
| struct | [net\_stats\_eth\_hw\_timestamp](structnet__stats__eth__hw__timestamp.md) |
|  | Ethernet hardware timestamp statistics. [More...](structnet__stats__eth__hw__timestamp.md#details) |
| struct | [net\_stats\_eth](structnet__stats__eth.md) |
|  | All Ethernet specific statistics. [More...](structnet__stats__eth.md#details) |
| struct | [net\_stats\_ppp](structnet__stats__ppp.md) |
|  | All PPP specific statistics. [More...](structnet__stats__ppp.md#details) |
| struct | [net\_stats\_sta\_mgmt](structnet__stats__sta__mgmt.md) |
|  | All Wi-Fi management statistics. [More...](structnet__stats__sta__mgmt.md#details) |
| struct | [net\_stats\_wifi](structnet__stats__wifi.md) |
|  | All Wi-Fi specific statistics. [More...](structnet__stats__wifi.md#details) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_stats\_t](#ga05ec15873e79256c287f21b6b6fcd752) |
|  | Network statistics counter. |

## Detailed Description

Network statistics library.

Since
:   1.5

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#ga05ec15873e79256c287f21b6b6fcd752)net\_stats\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_stats\_t](#ga05ec15873e79256c287f21b6b6fcd752) |
| --- |

`#include <[net_stats.h](net__stats_8h.md)>`

Network statistics counter.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
