---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/metric_8h_source.html
original_path: doxygen/html/metric_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

metric.h

[Go to the documentation of this file.](metric_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \* Copyright (c) 2024 Nordic Semiconductor

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_METRIC\_H\_

9#define ZEPHYR\_INCLUDE\_PROMETHEUS\_METRIC\_H\_

10

19

20#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

21#include <[zephyr/sys/slist.h](slist_8h.md)>

22#include <[zephyr/net/prometheus/label.h](label_8h.md)>

23

[ 30](group__prometheus.md#ga3499408dda4e539634c332c797651932)enum [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) {

[ 32](group__prometheus.md#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b) [PROMETHEUS\_COUNTER](group__prometheus.md#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b) = 0,

[ 34](group__prometheus.md#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd) [PROMETHEUS\_GAUGE](group__prometheus.md#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd),

[ 36](group__prometheus.md#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074) [PROMETHEUS\_SUMMARY](group__prometheus.md#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074),

[ 38](group__prometheus.md#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf) [PROMETHEUS\_HISTOGRAM](group__prometheus.md#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf),

39};

40

[ 47](structprometheus__metric.md)struct [prometheus\_metric](structprometheus__metric.md) {

[ 49](structprometheus__metric.md#a68b4a71af679bef383d635f1b0018dba) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structprometheus__metric.md#a68b4a71af679bef383d635f1b0018dba);

[ 51](structprometheus__metric.md#a1138f189a5bdd44639dace426ef8f55a) struct [prometheus\_collector](structprometheus__collector.md) \*[collector](structprometheus__metric.md#a1138f189a5bdd44639dace426ef8f55a);

[ 56](structprometheus__metric.md#a67e8d38a696f2b20a076b8da6b1250e3) void \*[metric](structprometheus__metric.md#a67e8d38a696f2b20a076b8da6b1250e3);

[ 58](structprometheus__metric.md#a05e19d7781f4724dfe7776e62cd69ca2) enum [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) [type](structprometheus__metric.md#a05e19d7781f4724dfe7776e62cd69ca2);

[ 60](structprometheus__metric.md#a5266bf5bd528cdd4c34ea56d7a96129d) const char \*[name](structprometheus__metric.md#a5266bf5bd528cdd4c34ea56d7a96129d);

[ 62](structprometheus__metric.md#a9ceba3f813e1bcf36c333af975c7ac76) const char \*[description](structprometheus__metric.md#a9ceba3f813e1bcf36c333af975c7ac76);

[ 64](structprometheus__metric.md#af3ae0862633b2ce475f7c6851d13c3d1) struct [prometheus\_label](structprometheus__label.md) [labels](structprometheus__metric.md#af3ae0862633b2ce475f7c6851d13c3d1)[[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)];

[ 66](structprometheus__metric.md#a198f0ddcf143d8728d914ee34eb8cb78) int [num\_labels](structprometheus__metric.md#a198f0ddcf143d8728d914ee34eb8cb78);

[ 68](structprometheus__metric.md#ae2db853cae2c49634fda25eb23b825da) void \*[user\_data](structprometheus__metric.md#ae2db853cae2c49634fda25eb23b825da);

69 /\* Add any other necessary fields \*/

70};

71

75

76#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_METRIC\_H\_ \*/

[prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932)

prometheus\_metric\_type

Prometheus metric types.

**Definition** metric.h:30

[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)

#define MAX\_PROMETHEUS\_LABELS\_PER\_METRIC

**Definition** label.h:23

[PROMETHEUS\_HISTOGRAM](group__prometheus.md#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf)

@ PROMETHEUS\_HISTOGRAM

Prometheus Histogram.

**Definition** metric.h:38

[PROMETHEUS\_GAUGE](group__prometheus.md#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd)

@ PROMETHEUS\_GAUGE

Prometheus Gauge.

**Definition** metric.h:34

[PROMETHEUS\_SUMMARY](group__prometheus.md#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074)

@ PROMETHEUS\_SUMMARY

Prometheus Summary.

**Definition** metric.h:36

[PROMETHEUS\_COUNTER](group__prometheus.md#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b)

@ PROMETHEUS\_COUNTER

Prometheus Counter.

**Definition** metric.h:32

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[label.h](label_8h.md)

Prometheus label interface.

[slist.h](slist_8h.md)

[prometheus\_collector](structprometheus__collector.md)

Prometheus collector definition.

**Definition** collector.h:50

[prometheus\_label](structprometheus__label.md)

Prometheus label definition.

**Definition** label.h:31

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:47

[prometheus\_metric::type](structprometheus__metric.md#a05e19d7781f4724dfe7776e62cd69ca2)

enum prometheus\_metric\_type type

Type of the Prometheus metric.

**Definition** metric.h:58

[prometheus\_metric::collector](structprometheus__metric.md#a1138f189a5bdd44639dace426ef8f55a)

struct prometheus\_collector \* collector

Back pointer to the collector that this metric belongs to.

**Definition** metric.h:51

[prometheus\_metric::num\_labels](structprometheus__metric.md#a198f0ddcf143d8728d914ee34eb8cb78)

int num\_labels

Number of labels associated with the Prometheus metric.

**Definition** metric.h:66

[prometheus\_metric::name](structprometheus__metric.md#a5266bf5bd528cdd4c34ea56d7a96129d)

const char \* name

Name of the Prometheus metric.

**Definition** metric.h:60

[prometheus\_metric::metric](structprometheus__metric.md#a67e8d38a696f2b20a076b8da6b1250e3)

void \* metric

Back pointer to the actual metric (counter, gauge, etc.).

**Definition** metric.h:56

[prometheus\_metric::node](structprometheus__metric.md#a68b4a71af679bef383d635f1b0018dba)

sys\_snode\_t node

Slist metric list node.

**Definition** metric.h:49

[prometheus\_metric::description](structprometheus__metric.md#a9ceba3f813e1bcf36c333af975c7ac76)

const char \* description

Description of the Prometheus metric.

**Definition** metric.h:62

[prometheus\_metric::user\_data](structprometheus__metric.md#ae2db853cae2c49634fda25eb23b825da)

void \* user\_data

User defined data.

**Definition** metric.h:68

[prometheus\_metric::labels](structprometheus__metric.md#af3ae0862633b2ce475f7c6851d13c3d1)

struct prometheus\_label labels[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC]

Labels associated with the Prometheus metric.

**Definition** metric.h:64

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [metric.h](metric_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
