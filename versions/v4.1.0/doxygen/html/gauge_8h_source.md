---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gauge_8h_source.html
original_path: doxygen/html/gauge_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gauge.h

[Go to the documentation of this file.](gauge_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \* Copyright (c) 2024 Nordic Semiconductor

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_GAUGE\_H\_

9#define ZEPHYR\_INCLUDE\_PROMETHEUS\_GAUGE\_H\_

10

19

20#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

21#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

22

[ 29](structprometheus__gauge.md)struct [prometheus\_gauge](structprometheus__gauge.md) {

[ 31](structprometheus__gauge.md#a6ad64e6b7806165cb4d78ac29ff3ae27) struct [prometheus\_metric](structprometheus__metric.md) [base](structprometheus__gauge.md#a6ad64e6b7806165cb4d78ac29ff3ae27);

[ 33](structprometheus__gauge.md#aabf12d85b93d419e19d9c300cb6313a7) double [value](structprometheus__gauge.md#aabf12d85b93d419e19d9c300cb6313a7);

[ 35](structprometheus__gauge.md#a3c935bf93e23c10961e3160cce45e741) void \*[user\_data](structprometheus__gauge.md#a3c935bf93e23c10961e3160cce45e741);

36};

37

[ 59](group__prometheus.md#ga362e708722846a3ca9299e8994becd13)#define PROMETHEUS\_GAUGE\_DEFINE(\_name, \_desc, \_label, \_collector, ...) \

60 STRUCT\_SECTION\_ITERABLE(prometheus\_gauge, \_name) = { \

61 .base.name = STRINGIFY(\_name), \

62 .base.type = PROMETHEUS\_GAUGE, \

63 .base.description = \_desc, \

64 .base.labels[0] = \_\_DEBRACKET \_label, \

65 .base.num\_labels = 1, \

66 .base.collector = \_collector, \

67 .value = 0.0, \

68 .user\_data = COND\_CODE\_0( \

69 NUM\_VA\_ARGS\_LESS\_1(LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), \

70 (NULL), \

71 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))), \

72 }

73

[ 84](group__prometheus.md#ga3ddc5efbdb9639486862f3df4b845fce)int [prometheus\_gauge\_set](group__prometheus.md#ga3ddc5efbdb9639486862f3df4b845fce)(struct [prometheus\_gauge](structprometheus__gauge.md) \*gauge, double value);

85

89

90#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_GAUGE\_H\_ \*/

[prometheus\_gauge\_set](group__prometheus.md#ga3ddc5efbdb9639486862f3df4b845fce)

int prometheus\_gauge\_set(struct prometheus\_gauge \*gauge, double value)

Set the value of a Prometheus gauge metric.

[metric.h](metric_8h.md)

Prometheus metric interface.

[prometheus\_gauge](structprometheus__gauge.md)

Type used to represent a Prometheus gauge metric.

**Definition** gauge.h:29

[prometheus\_gauge::user\_data](structprometheus__gauge.md#a3c935bf93e23c10961e3160cce45e741)

void \* user\_data

User data.

**Definition** gauge.h:35

[prometheus\_gauge::base](structprometheus__gauge.md#a6ad64e6b7806165cb4d78ac29ff3ae27)

struct prometheus\_metric base

Base of the Prometheus gauge metric.

**Definition** gauge.h:31

[prometheus\_gauge::value](structprometheus__gauge.md#aabf12d85b93d419e19d9c300cb6313a7)

double value

Value of the Prometheus gauge metric.

**Definition** gauge.h:33

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:47

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [gauge.h](gauge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
