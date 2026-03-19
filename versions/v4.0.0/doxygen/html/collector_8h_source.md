---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/collector_8h_source.html
original_path: doxygen/html/collector_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

collector.h

[Go to the documentation of this file.](collector_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_COLLECTOR\_H\_

8#define ZEPHYR\_INCLUDE\_PROMETHEUS\_COLLECTOR\_H\_

9

21

22#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

23#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

24

25#include <stddef.h>

26

[ 32](structprometheus__collector.md)struct [prometheus\_collector](structprometheus__collector.md) {

[ 34](structprometheus__collector.md#a050b6094f92369225dce734ef9f50476) const char \*[name](structprometheus__collector.md#a050b6094f92369225dce734ef9f50476);

[ 36](structprometheus__collector.md#a3200e70f16799313b33e9cf3a5949f0c) struct [prometheus\_metric](structprometheus__metric.md) \*[metric](structprometheus__collector.md#a3200e70f16799313b33e9cf3a5949f0c)[CONFIG\_PROMETHEUS\_MAX\_METRICS];

[ 38](structprometheus__collector.md#a1bf1167b74db303eab6bf561e823a6ea) size\_t [size](structprometheus__collector.md#a1bf1167b74db303eab6bf561e823a6ea);

39};

40

[ 48](group__prometheus.md#ga789b8557d1db7ad10133904e80e7f81c)#define PROMETHEUS\_COLLECTOR\_DEFINE(\_name) \

49 static STRUCT\_SECTION\_ITERABLE(prometheus\_collector, \_name) = { \

50 .name = STRINGIFY(\_name), .size = 0, .metric = {0}}

51

[ 64](group__prometheus.md#ga976b9e82d747570cde631b03ee805a26)int [prometheus\_collector\_register\_metric](group__prometheus.md#ga976b9e82d747570cde631b03ee805a26)(struct [prometheus\_collector](structprometheus__collector.md) \*collector,

65 struct [prometheus\_metric](structprometheus__metric.md) \*metric);

66

[ 76](group__prometheus.md#ga428d008af1e84985bf7bce86ce0a408e)const void \*[prometheus\_collector\_get\_metric](group__prometheus.md#ga428d008af1e84985bf7bce86ce0a408e)(const struct [prometheus\_collector](structprometheus__collector.md) \*collector,

77 const char \*[name](structprometheus__metric.md#af32069fd653d50cefce48c0e90c96b69));

78

82

83#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_COLLECTOR\_H\_ \*/

[prometheus\_collector\_get\_metric](group__prometheus.md#ga428d008af1e84985bf7bce86ce0a408e)

const void \* prometheus\_collector\_get\_metric(const struct prometheus\_collector \*collector, const char \*name)

Get a metric from a Prometheus collector.

[prometheus\_collector\_register\_metric](group__prometheus.md#ga976b9e82d747570cde631b03ee805a26)

int prometheus\_collector\_register\_metric(struct prometheus\_collector \*collector, struct prometheus\_metric \*metric)

Register a metric with a Prometheus collector.

[metric.h](metric_8h.md)

Prometheus metric interface.

[prometheus\_collector](structprometheus__collector.md)

Prometheus collector definition.

**Definition** collector.h:32

[prometheus\_collector::name](structprometheus__collector.md#a050b6094f92369225dce734ef9f50476)

const char \* name

Name of the collector.

**Definition** collector.h:34

[prometheus\_collector::size](structprometheus__collector.md#a1bf1167b74db303eab6bf561e823a6ea)

size\_t size

Number of metrics associated with the collector.

**Definition** collector.h:38

[prometheus\_collector::metric](structprometheus__collector.md#a3200e70f16799313b33e9cf3a5949f0c)

struct prometheus\_metric \* metric[CONFIG\_PROMETHEUS\_MAX\_METRICS]

Array of metrics associated with the collector.

**Definition** collector.h:36

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:48

[prometheus\_metric::name](structprometheus__metric.md#af32069fd653d50cefce48c0e90c96b69)

char name[32]

Name of the Prometheus metric.

**Definition** metric.h:52

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [collector.h](collector_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
