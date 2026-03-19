---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gauge_8h_source.html
original_path: doxygen/html/gauge_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gauge.h

[Go to the documentation of this file.](gauge_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_GAUGE\_H\_

8#define ZEPHYR\_INCLUDE\_PROMETHEUS\_GAUGE\_H\_

9

18

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

21

[ 28](structprometheus__gauge.md)struct [prometheus\_gauge](structprometheus__gauge.md) {

[ 30](structprometheus__gauge.md#a619e838dd218710d1563e50aaf4cb83b) struct [prometheus\_metric](structprometheus__metric.md) \*[base](structprometheus__gauge.md#a619e838dd218710d1563e50aaf4cb83b);

[ 32](structprometheus__gauge.md#aabf12d85b93d419e19d9c300cb6313a7) double [value](structprometheus__gauge.md#aabf12d85b93d419e19d9c300cb6313a7);

33};

34

[ 60](group__prometheus.md#ga5398af0cd3d15ced8053b621170a4565)#define PROMETHEUS\_GAUGE\_DEFINE(\_name, \_detail) \

61 static STRUCT\_SECTION\_ITERABLE(prometheus\_gauge, \_name) = {.base = (void \*)(\_detail), \

62 .value = 0}

63

[ 74](group__prometheus.md#ga3ddc5efbdb9639486862f3df4b845fce)int [prometheus\_gauge\_set](group__prometheus.md#ga3ddc5efbdb9639486862f3df4b845fce)(struct [prometheus\_gauge](structprometheus__gauge.md) \*gauge, double value);

75

79

80#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_GAUGE\_H\_ \*/

[prometheus\_gauge\_set](group__prometheus.md#ga3ddc5efbdb9639486862f3df4b845fce)

int prometheus\_gauge\_set(struct prometheus\_gauge \*gauge, double value)

Set the value of a Prometheus gauge metric.

[metric.h](metric_8h.md)

Prometheus metric interface.

[prometheus\_gauge](structprometheus__gauge.md)

Type used to represent a Prometheus gauge metric.

**Definition** gauge.h:28

[prometheus\_gauge::base](structprometheus__gauge.md#a619e838dd218710d1563e50aaf4cb83b)

struct prometheus\_metric \* base

Base of the Prometheus gauge metric.

**Definition** gauge.h:30

[prometheus\_gauge::value](structprometheus__gauge.md#aabf12d85b93d419e19d9c300cb6313a7)

double value

Value of the Prometheus gauge metric.

**Definition** gauge.h:32

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:48

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [gauge.h](gauge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
