---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net_2prometheus_2counter_8h_source.html
original_path: doxygen/html/net_2prometheus_2counter_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter.h

[Go to the documentation of this file.](net_2prometheus_2counter_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_COUNTER\_H\_

8#define ZEPHYR\_INCLUDE\_PROMETHEUS\_COUNTER\_H\_

9

18

19#include <[stdint.h](stdint_8h.md)>

20

21#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

22#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

23

[ 30](structprometheus__counter.md)struct [prometheus\_counter](structprometheus__counter.md) {

[ 32](structprometheus__counter.md#a1fcd8ff14fafd229356a8082027affea) struct [prometheus\_metric](structprometheus__metric.md) \*[base](structprometheus__counter.md#a1fcd8ff14fafd229356a8082027affea);

[ 34](structprometheus__counter.md#a048376a671e83df41034908b85e9e234) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structprometheus__counter.md#a048376a671e83df41034908b85e9e234);

35};

36

[ 61](group__prometheus.md#ga467bbac42b48995598dbd370277b243b)#define PROMETHEUS\_COUNTER\_DEFINE(\_name, \_detail) \

62 static STRUCT\_SECTION\_ITERABLE(prometheus\_counter, \_name) = {.base = (void \*)(\_detail), \

63 .value = 0}

64

[ 71](group__prometheus.md#ga911670f61fa22d3834aecf5351c944e4)int [prometheus\_counter\_inc](group__prometheus.md#ga911670f61fa22d3834aecf5351c944e4)(struct [prometheus\_counter](structprometheus__counter.md) \*counter);

72

76

77#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_COUNTER\_H\_ \*/

[prometheus\_counter\_inc](group__prometheus.md#ga911670f61fa22d3834aecf5351c944e4)

int prometheus\_counter\_inc(struct prometheus\_counter \*counter)

Increment the value of a Prometheus counter metric Increments the value of the specified counter metr...

[metric.h](metric_8h.md)

Prometheus metric interface.

[stdint.h](stdint_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[prometheus\_counter](structprometheus__counter.md)

Type used to represent a Prometheus counter metric.

**Definition** counter.h:30

[prometheus\_counter::value](structprometheus__counter.md#a048376a671e83df41034908b85e9e234)

uint64\_t value

Value of the Prometheus counter metric.

**Definition** counter.h:34

[prometheus\_counter::base](structprometheus__counter.md#a1fcd8ff14fafd229356a8082027affea)

struct prometheus\_metric \* base

Base of the Prometheus counter metric.

**Definition** counter.h:32

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:48

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [counter.h](net_2prometheus_2counter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
