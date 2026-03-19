---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__stats_8h.html
original_path: doxygen/html/net__stats_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats.h File Reference

Network statistics.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`  
`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`

[Go to the source code of this file.](net__stats_8h_source.md)

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
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) |
|  | Network statistics counter. |

## Detailed Description

Network statistics.

Network statistics data. This should only be enabled when debugging as it consumes memory.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_stats.h](net__stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
