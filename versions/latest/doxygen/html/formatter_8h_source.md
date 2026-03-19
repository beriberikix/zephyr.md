---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/formatter_8h_source.html
original_path: doxygen/html/formatter_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

formatter.h

[Go to the documentation of this file.](formatter_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_FORMATTER\_H\_

8#define ZEPHYR\_INCLUDE\_PROMETHEUS\_FORMATTER\_H\_

9

18

19#include <[zephyr/net/prometheus/collector.h](collector_8h.md)>

20

[ 33](group__prometheus.md#ga7d219be7f2b3b49a2f936489bdf68fe8)int [prometheus\_format\_exposition](group__prometheus.md#ga7d219be7f2b3b49a2f936489bdf68fe8)(struct [prometheus\_collector](structprometheus__collector.md) \*collector, char \*buffer,

34 size\_t buffer\_size);

35

[ 49](group__prometheus.md#ga2240cf4f807fe7180f21c8fab3fbbd66)int [prometheus\_format\_one\_metric](group__prometheus.md#ga2240cf4f807fe7180f21c8fab3fbbd66)(struct [prometheus\_metric](structprometheus__metric.md) \*metric, char \*buffer,

50 size\_t buffer\_size, int \*written);

51

55

56#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_FORMATTER\_H\_ \*/

[collector.h](collector_8h.md)

Prometheus collector APIs.

[prometheus\_format\_one\_metric](group__prometheus.md#ga2240cf4f807fe7180f21c8fab3fbbd66)

int prometheus\_format\_one\_metric(struct prometheus\_metric \*metric, char \*buffer, size\_t buffer\_size, int \*written)

Format exposition data for one metric for Prometheus.

[prometheus\_format\_exposition](group__prometheus.md#ga7d219be7f2b3b49a2f936489bdf68fe8)

int prometheus\_format\_exposition(struct prometheus\_collector \*collector, char \*buffer, size\_t buffer\_size)

Format exposition data for Prometheus.

[prometheus\_collector](structprometheus__collector.md)

Prometheus collector definition.

**Definition** collector.h:50

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:47

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [formatter.h](formatter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
