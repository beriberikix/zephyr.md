---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__net__stats.html
original_path: doxygen/html/group__net__stats.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| #define | [NET\_STATS\_GET\_METRIC\_NAME](#ga2a1dcb35c366878ef5f675d6bc649223)(\_name) |
| #define | [NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx) |
| #define | [NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, var) |
| #define | [NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, \_not\_used) |
| #define | [NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE](#gafc6b5e19cd9407c28cf151820b76a287)(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr) |
| #define | [NET\_STATS\_PROMETHEUS\_GAUGE\_DEFINE](#ga162fa8a0ea4939e5768a0cc64210dd6a)(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr) |
| #define | [NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE](#gab02b7f2c5c424723aed7a6aedd1181f9)(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr) |
| #define | [NET\_STATS\_PROMETHEUS\_HISTOGRAM\_DEFINE](#gae82639c2bed1c646cda66b49ae2f6de9)(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV6](#gaef8debd9597dae9e8ec2ef91d6e645cc)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV4](#gafa2e6de020b887512a3cebe75253fb18)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_ICMP](#ga96beec38aeb91a9d95b4e1e415c0d229)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_UDP](#ga2d400caf2103d6718bc2871abba3eddb)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_TCP](#ga1b581725d1a8652a0b40e71ac2e99261)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV6\_ND](#ga1cc29c5da3740b2623fd625f9f360c6d)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV6\_PMTU](#ga2593a73001deea960ccfb80cf71489d4)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IPV4\_PMTU](#gaaa0bc9dd9f53da03492d10c399db8eab)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_MLD](#ga5c4827a519269cc00323dfe57921117b)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_IGMP](#ga8782a593de8ae207e57abfcc9477e256)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_DNS](#gaef54299a895568956cbae9960c7bf844)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_TX\_TIME](#gaf0c1ee536e8a816c537b6cf7344353f4)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS\_RX\_TIME](#ga2b9c4b3dc4cd1cd2b79801e7a4b58849)(iface, dev\_id, sfx) |
| #define | [NET\_STATS\_PROMETHEUS](#gac79e6cd416c92f9d26843900a084b375)(iface, dev\_id, sfx) |

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

## Macro Definition Documentation

## [◆ ](#gab58d7d437d4fa9836a826ee59e2d081d)NET\_STATS\_GET\_COLLECTOR\_NAME

| #define NET\_STATS\_GET\_COLLECTOR\_NAME | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

net\_stats\_##dev\_id##\_##sfx##\_collector

## [◆ ](#gabb15df6c3c85b85756ef5d2d51d0afb2)NET\_STATS\_GET\_INSTANCE

| #define NET\_STATS\_GET\_INSTANCE | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *sfx*, |
|  |  |  | *\_not\_used* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_##dev\_id##\_##sfx)

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

## [◆ ](#ga2a1dcb35c366878ef5f675d6bc649223)NET\_STATS\_GET\_METRIC\_NAME

| #define NET\_STATS\_GET\_METRIC\_NAME | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

\_name

## [◆ ](#gab66b3c8d32d2f02add08c332460d5cd6)NET\_STATS\_GET\_VAR

| #define NET\_STATS\_GET\_VAR | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *sfx*, |
|  |  |  | *var* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

zephyr\_net\_##var

## [◆ ](#gac79e6cd416c92f9d26843900a084b375)NET\_STATS\_PROMETHEUS

| #define NET\_STATS\_PROMETHEUS | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

[NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE](#gafc6b5e19cd9407c28cf151820b76a287)( \

"Processing error", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, process\_error), \

"error\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, processing\_error), \

&(iface)->stats.processing\_error); \

/\* IP layer error statistics \*/ \

NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

"IP proto error", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, ip\_proto\_error), \

"error\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, ip\_errors\_protoerr), \

&(iface)->stats.ip\_errors.protoerr); \

NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

"IP version/header len error", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, ip\_vhl\_error), \

"error\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, ip\_errors\_vhlerr), \

&(iface)->stats.ip\_errors.vhlerr); \

NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

"IP header len error (high byte)", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, ip\_hblen\_error), \

"error\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, ip\_errors\_hblenerr), \

&(iface)->stats.ip\_errors.hblenerr); \

NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

"IP header len error (low byte)", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, ip\_lblen\_error), \

"error\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, ip\_errors\_lblenerr), \

&(iface)->stats.ip\_errors.lblenerr); \

NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

"IP fragment error", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, ip\_frag\_error), \

"error\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, ip\_errors\_fragerr), \

&(iface)->stats.ip\_errors.fragerr); \

NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

"IP checksum error", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, ip\_chk\_error), \

"error\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, ip\_errors\_chkerr), \

&(iface)->stats.ip\_errors.chkerr); \

/\* General network statistics \*/ \

NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

"Bytes received", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, bytes\_recv), \

"byte\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, bytes\_recv), \

&(iface)->stats.bytes.received); \

NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE( \

"Bytes sent", \

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)(dev\_id, sfx, bytes\_sent), \

"byte\_count", \

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)(dev\_id, sfx), \

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)(dev\_id, sfx, bytes\_sent), \

&(iface)->stats.bytes.sent); \

NET\_STATS\_PROMETHEUS\_IPV6(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_IPV4(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_ICMP(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_UDP(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_TCP(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_IPV6\_ND(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_IPV6\_PMTU(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_IPV4\_PMTU(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_MLD(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_IGMP(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_DNS(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_TX\_TIME(iface, dev\_id, sfx); \

NET\_STATS\_PROMETHEUS\_RX\_TIME(iface, dev\_id, sfx)

[NET\_STATS\_GET\_COLLECTOR\_NAME](#gab58d7d437d4fa9836a826ee59e2d081d)

#define NET\_STATS\_GET\_COLLECTOR\_NAME(dev\_id, sfx)

**Definition** net\_stats.h:887

[NET\_STATS\_GET\_VAR](#gab66b3c8d32d2f02add08c332460d5cd6)

#define NET\_STATS\_GET\_VAR(dev\_id, sfx, var)

**Definition** net\_stats.h:888

[NET\_STATS\_GET\_INSTANCE](#gabb15df6c3c85b85756ef5d2d51d0afb2)

#define NET\_STATS\_GET\_INSTANCE(dev\_id, sfx, \_not\_used)

**Definition** net\_stats.h:889

[NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE](#gafc6b5e19cd9407c28cf151820b76a287)

#define NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE(\_desc, \_labelval, \_not\_used, \_collector, \_name, \_stat\_var\_ptr)

**Definition** net\_stats.h:896

## [◆ ](#gafc6b5e19cd9407c28cf151820b76a287)NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE

| #define NET\_STATS\_PROMETHEUS\_COUNTER\_DEFINE | ( |  | *\_desc*, |
| --- | --- | --- | --- |
|  |  |  | *\_labelval*, |
|  |  |  | *\_not\_used*, |
|  |  |  | *\_collector*, |
|  |  |  | *\_name*, |
|  |  |  | *\_stat\_var\_ptr* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

static [PROMETHEUS\_COUNTER\_DEFINE](group__prometheus.md#gadbfcfc7904d6388d2c9dc81d4803264c)( \

[NET\_STATS\_GET\_METRIC\_NAME](#ga2a1dcb35c366878ef5f675d6bc649223)(\_name), \

\_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

&(\_collector), \_stat\_var\_ptr)

[NET\_STATS\_GET\_METRIC\_NAME](#ga2a1dcb35c366878ef5f675d6bc649223)

#define NET\_STATS\_GET\_METRIC\_NAME(\_name)

**Definition** net\_stats.h:886

[PROMETHEUS\_COUNTER\_DEFINE](group__prometheus.md#gadbfcfc7904d6388d2c9dc81d4803264c)

#define PROMETHEUS\_COUNTER\_DEFINE(\_name, \_desc, \_label, \_collector,...)

Prometheus Counter definition.

**Definition** counter.h:60

## [◆ ](#gaef54299a895568956cbae9960c7bf844)NET\_STATS\_PROMETHEUS\_DNS

| #define NET\_STATS\_PROMETHEUS\_DNS | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#ga162fa8a0ea4939e5768a0cc64210dd6a)NET\_STATS\_PROMETHEUS\_GAUGE\_DEFINE

| #define NET\_STATS\_PROMETHEUS\_GAUGE\_DEFINE | ( |  | *\_desc*, |
| --- | --- | --- | --- |
|  |  |  | *\_labelval*, |
|  |  |  | *\_not\_used*, |
|  |  |  | *\_collector*, |
|  |  |  | *\_name*, |
|  |  |  | *\_stat\_var\_ptr* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

static [PROMETHEUS\_GAUGE\_DEFINE](group__prometheus.md#ga362e708722846a3ca9299e8994becd13)( \

[NET\_STATS\_GET\_METRIC\_NAME](#ga2a1dcb35c366878ef5f675d6bc649223)(\_name), \

\_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

&(\_collector), \_stat\_var\_ptr)

[PROMETHEUS\_GAUGE\_DEFINE](group__prometheus.md#ga362e708722846a3ca9299e8994becd13)

#define PROMETHEUS\_GAUGE\_DEFINE(\_name, \_desc, \_label, \_collector,...)

Prometheus Gauge definition.

**Definition** gauge.h:59

## [◆ ](#gae82639c2bed1c646cda66b49ae2f6de9)NET\_STATS\_PROMETHEUS\_HISTOGRAM\_DEFINE

| #define NET\_STATS\_PROMETHEUS\_HISTOGRAM\_DEFINE | ( |  | *\_desc*, |
| --- | --- | --- | --- |
|  |  |  | *\_labelval*, |
|  |  |  | *\_not\_used*, |
|  |  |  | *\_collector*, |
|  |  |  | *\_name*, |
|  |  |  | *\_stat\_var\_ptr* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

static [PROMETHEUS\_HISTOGRAM\_DEFINE](group__prometheus.md#gaf2ddb4e016104faaf543d9a028756a0c)( \

[NET\_STATS\_GET\_METRIC\_NAME](#ga2a1dcb35c366878ef5f675d6bc649223)(\_name), \

\_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

&(\_collector), \_stat\_var\_ptr)

[PROMETHEUS\_HISTOGRAM\_DEFINE](group__prometheus.md#gaf2ddb4e016104faaf543d9a028756a0c)

#define PROMETHEUS\_HISTOGRAM\_DEFINE(\_name, \_desc, \_label, \_collector,...)

Prometheus Histogram definition.

**Definition** histogram.h:79

## [◆ ](#ga96beec38aeb91a9d95b4e1e415c0d229)NET\_STATS\_PROMETHEUS\_ICMP

| #define NET\_STATS\_PROMETHEUS\_ICMP | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#ga8782a593de8ae207e57abfcc9477e256)NET\_STATS\_PROMETHEUS\_IGMP

| #define NET\_STATS\_PROMETHEUS\_IGMP | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#gafa2e6de020b887512a3cebe75253fb18)NET\_STATS\_PROMETHEUS\_IPV4

| #define NET\_STATS\_PROMETHEUS\_IPV4 | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#gaaa0bc9dd9f53da03492d10c399db8eab)NET\_STATS\_PROMETHEUS\_IPV4\_PMTU

| #define NET\_STATS\_PROMETHEUS\_IPV4\_PMTU | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#gaef8debd9597dae9e8ec2ef91d6e645cc)NET\_STATS\_PROMETHEUS\_IPV6

| #define NET\_STATS\_PROMETHEUS\_IPV6 | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#ga1cc29c5da3740b2623fd625f9f360c6d)NET\_STATS\_PROMETHEUS\_IPV6\_ND

| #define NET\_STATS\_PROMETHEUS\_IPV6\_ND | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#ga2593a73001deea960ccfb80cf71489d4)NET\_STATS\_PROMETHEUS\_IPV6\_PMTU

| #define NET\_STATS\_PROMETHEUS\_IPV6\_PMTU | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#ga5c4827a519269cc00323dfe57921117b)NET\_STATS\_PROMETHEUS\_MLD

| #define NET\_STATS\_PROMETHEUS\_MLD | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#ga2b9c4b3dc4cd1cd2b79801e7a4b58849)NET\_STATS\_PROMETHEUS\_RX\_TIME

| #define NET\_STATS\_PROMETHEUS\_RX\_TIME | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#gab02b7f2c5c424723aed7a6aedd1181f9)NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE

| #define NET\_STATS\_PROMETHEUS\_SUMMARY\_DEFINE | ( |  | *\_desc*, |
| --- | --- | --- | --- |
|  |  |  | *\_labelval*, |
|  |  |  | *\_not\_used*, |
|  |  |  | *\_collector*, |
|  |  |  | *\_name*, |
|  |  |  | *\_stat\_var\_ptr* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

**Value:**

static [PROMETHEUS\_SUMMARY\_DEFINE](group__prometheus.md#gaa3c043be86118ff9e8122136edc89cc4)( \

[NET\_STATS\_GET\_METRIC\_NAME](#ga2a1dcb35c366878ef5f675d6bc649223)(\_name), \

\_desc, ({ .key = "nic", .value = &\_labelval[1] }), \

&(\_collector), \_stat\_var\_ptr)

[PROMETHEUS\_SUMMARY\_DEFINE](group__prometheus.md#gaa3c043be86118ff9e8122136edc89cc4)

#define PROMETHEUS\_SUMMARY\_DEFINE(\_name, \_desc, \_label, \_collector,...)

Prometheus Summary definition.

**Definition** summary.h:83

## [◆ ](#ga1b581725d1a8652a0b40e71ac2e99261)NET\_STATS\_PROMETHEUS\_TCP

| #define NET\_STATS\_PROMETHEUS\_TCP | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#gaf0c1ee536e8a816c537b6cf7344353f4)NET\_STATS\_PROMETHEUS\_TX\_TIME

| #define NET\_STATS\_PROMETHEUS\_TX\_TIME | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## [◆ ](#ga2d400caf2103d6718bc2871abba3eddb)NET\_STATS\_PROMETHEUS\_UDP

| #define NET\_STATS\_PROMETHEUS\_UDP | ( |  | *iface*, |
| --- | --- | --- | --- |
|  |  |  | *dev\_id*, |
|  |  |  | *sfx* ) |

`#include <[net_stats.h](net__stats_8h.md)>`

## Typedef Documentation

## [◆ ](#ga05ec15873e79256c287f21b6b6fcd752)net\_stats\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_stats\_t](#ga05ec15873e79256c287f21b6b6fcd752) |
| --- |

`#include <[net_stats.h](net__stats_8h.md)>`

Network statistics counter.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
