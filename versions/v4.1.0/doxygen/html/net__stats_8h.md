---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__stats_8h.html
original_path: doxygen/html/net__stats_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
`#include <[zephyr/net/prometheus/collector.h](collector_8h_source.md)>`  
`#include <[zephyr/net/prometheus/counter.h](net_2prometheus_2counter_8h_source.md)>`  
`#include <[zephyr/net/prometheus/metric.h](metric_8h_source.md)>`  
`#include <[zephyr/net/prometheus/gauge.h](gauge_8h_source.md)>`  
`#include <[zephyr/net/prometheus/histogram.h](histogram_8h_source.md)>`  
`#include <[zephyr/net/prometheus/summary.h](summary_8h_source.md)>`

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
| struct | [net\_stats\_ipv6\_pmtu](structnet__stats__ipv6__pmtu.md) |
|  | IPv6 Path MTU Discovery statistics. [More...](structnet__stats__ipv6__pmtu.md#details) |
| struct | [net\_stats\_ipv4\_pmtu](structnet__stats__ipv4__pmtu.md) |
|  | IPv4 Path MTU Discovery statistics. [More...](structnet__stats__ipv4__pmtu.md#details) |
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

| Macros | |
| --- | --- |
| #define | [NET\_STATS\_GET\_METRIC\_NAME](group__net__stats.md#ga2a1dcb35c366878ef5f675d6bc649223)(\_name) |
| #define | [NET\_STATS\_GET\_COLLECTOR\_NAME](group__net__stats.md#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx) |
| #define | [NET\_STATS\_GET\_VAR](group__net__stats.md#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, var) |
| #define | [NET\_STATS\_GET\_INSTANCE](group__net__stats.md#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, \_not\_used) |
| #define | [NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE](group__net__stats.md#gafc6b5e19cd9407c28cf151820b76a287)(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr) |
| #define | [NET\_STATS\_PROMETHEUS\_GAUGE\_DEFINE](group__net__stats.md#ga162fa8a0ea4939e5768a0cc64210dd6a)(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr) |
| #define | [NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE](group__net__stats.md#gab02b7f2c5c424723aed7a6aedd1181f9)(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr) |
| #define | [NET\_STATS\_PROMETHEUS\_HISTOGRAM\_DEFINE](group__net__stats.md#gae82639c2bed1c646cda66b49ae2f6de9)(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV6](group__net__stats.md#gaef8debd9597dae9e8ec2ef91d6e645cc)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV4](group__net__stats.md#gafa2e6de020b887512a3cebe75253fb18)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_ICMP](group__net__stats.md#ga96beec38aeb91a9d95b4e1e415c0d229)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_UDP](group__net__stats.md#ga2d400caf2103d6718bc2871abba3eddb)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_TCP](group__net__stats.md#ga1b581725d1a8652a0b40e71ac2e99261)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV6\_ND](group__net__stats.md#ga1cc29c5da3740b2623fd625f9f360c6d)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV6\_PMTU](group__net__stats.md#ga2593a73001deea960ccfb80cf71489d4)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV4\_PMTU](group__net__stats.md#gaaa0bc9dd9f53da03492d10c399db8eab)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_MLD](group__net__stats.md#ga5c4827a519269cc00323dfe57921117b)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IGMP](group__net__stats.md#ga8782a593de8ae207e57abfcc9477e256)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_DNS](group__net__stats.md#gaef54299a895568956cbae9960c7bf844)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_TX\_TIME](group__net__stats.md#gaf0c1ee536e8a816c537b6cf7344353f4)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_RX\_TIME](group__net__stats.md#ga2b9c4b3dc4cd1cd2b79801e7a4b58849)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS](group__net__stats.md#gac79e6cd416c92f9d26843900a084b375)(iface, dev\_id, sfx) |

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
