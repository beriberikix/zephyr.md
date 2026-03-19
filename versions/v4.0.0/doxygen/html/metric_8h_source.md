---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/metric_8h_source.html
original_path: doxygen/html/metric_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

metric.h

[Go to the documentation of this file.](metric_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_METRIC\_H\_

8#define ZEPHYR\_INCLUDE\_PROMETHEUS\_METRIC\_H\_

9

18

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20#include <[zephyr/net/prometheus/label.h](label_8h.md)>

21

[ 28](group__prometheus.md#ga3499408dda4e539634c332c797651932)enum [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) {

[ 30](group__prometheus.md#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b) [PROMETHEUS\_COUNTER](group__prometheus.md#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b) = 0,

[ 32](group__prometheus.md#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd) [PROMETHEUS\_GAUGE](group__prometheus.md#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd),

[ 34](group__prometheus.md#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074) [PROMETHEUS\_SUMMARY](group__prometheus.md#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074),

[ 36](group__prometheus.md#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf) [PROMETHEUS\_HISTOGRAM](group__prometheus.md#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf),

37};

38

[ 39](group__prometheus.md#ga0c2758847b60dece283eda02678edce8)#define MAX\_METRIC\_NAME\_LENGTH 32

[ 40](group__prometheus.md#ga9b788e35d8854a54faff830295b5b6ab)#define MAX\_METRIC\_DESCRIPTION\_LENGTH 64

41

[ 48](structprometheus__metric.md)struct [prometheus\_metric](structprometheus__metric.md) {

[ 50](structprometheus__metric.md#a05e19d7781f4724dfe7776e62cd69ca2) enum [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) [type](structprometheus__metric.md#a05e19d7781f4724dfe7776e62cd69ca2);

[ 52](structprometheus__metric.md#af32069fd653d50cefce48c0e90c96b69) char [name](structprometheus__metric.md#af32069fd653d50cefce48c0e90c96b69)[[MAX\_METRIC\_NAME\_LENGTH](group__prometheus.md#ga0c2758847b60dece283eda02678edce8)];

[ 54](structprometheus__metric.md#af751f2601dafffdbe06acf63d4cdfcbf) char [description](structprometheus__metric.md#af751f2601dafffdbe06acf63d4cdfcbf)[[MAX\_METRIC\_DESCRIPTION\_LENGTH](group__prometheus.md#ga9b788e35d8854a54faff830295b5b6ab)];

[ 56](structprometheus__metric.md#af3ae0862633b2ce475f7c6851d13c3d1) struct [prometheus\_label](structprometheus__label.md) [labels](structprometheus__metric.md#af3ae0862633b2ce475f7c6851d13c3d1)[[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)];

[ 58](structprometheus__metric.md#a198f0ddcf143d8728d914ee34eb8cb78) int [num\_labels](structprometheus__metric.md#a198f0ddcf143d8728d914ee34eb8cb78);

59 /\* Add any other necessary fields \*/

60};

61

65

66#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_METRIC\_H\_ \*/

[MAX\_METRIC\_NAME\_LENGTH](group__prometheus.md#ga0c2758847b60dece283eda02678edce8)

#define MAX\_METRIC\_NAME\_LENGTH

**Definition** metric.h:39

[prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932)

prometheus\_metric\_type

Prometheus metric types.

**Definition** metric.h:28

[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)

#define MAX\_PROMETHEUS\_LABELS\_PER\_METRIC

**Definition** label.h:24

[MAX\_METRIC\_DESCRIPTION\_LENGTH](group__prometheus.md#ga9b788e35d8854a54faff830295b5b6ab)

#define MAX\_METRIC\_DESCRIPTION\_LENGTH

**Definition** metric.h:40

[PROMETHEUS\_HISTOGRAM](group__prometheus.md#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf)

@ PROMETHEUS\_HISTOGRAM

Prometheus Histogram.

**Definition** metric.h:36

[PROMETHEUS\_GAUGE](group__prometheus.md#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd)

@ PROMETHEUS\_GAUGE

Prometheus Gauge.

**Definition** metric.h:32

[PROMETHEUS\_SUMMARY](group__prometheus.md#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074)

@ PROMETHEUS\_SUMMARY

Prometheus Summary.

**Definition** metric.h:34

[PROMETHEUS\_COUNTER](group__prometheus.md#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b)

@ PROMETHEUS\_COUNTER

Prometheus Counter.

**Definition** metric.h:30

[label.h](label_8h.md)

Prometheus label interface.

[prometheus\_label](structprometheus__label.md)

Prometheus label definition.

**Definition** label.h:31

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:48

[prometheus\_metric::type](structprometheus__metric.md#a05e19d7781f4724dfe7776e62cd69ca2)

enum prometheus\_metric\_type type

Type of the Prometheus metric.

**Definition** metric.h:50

[prometheus\_metric::num\_labels](structprometheus__metric.md#a198f0ddcf143d8728d914ee34eb8cb78)

int num\_labels

Number of labels associated with the Prometheus metric.

**Definition** metric.h:58

[prometheus\_metric::name](structprometheus__metric.md#af32069fd653d50cefce48c0e90c96b69)

char name[32]

Name of the Prometheus metric.

**Definition** metric.h:52

[prometheus\_metric::labels](structprometheus__metric.md#af3ae0862633b2ce475f7c6851d13c3d1)

struct prometheus\_label labels[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC]

Labels associated with the Prometheus metric.

**Definition** metric.h:56

[prometheus\_metric::description](structprometheus__metric.md#af751f2601dafffdbe06acf63d4cdfcbf)

char description[64]

Description of the Prometheus metric.

**Definition** metric.h:54

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [metric.h](metric_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
