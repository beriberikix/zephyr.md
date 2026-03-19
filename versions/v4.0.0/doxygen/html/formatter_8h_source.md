---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/formatter_8h_source.html
original_path: doxygen/html/formatter_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 33](group__prometheus.md#ga23b33f57ee6ad1154f7903b505e604b1)int [prometheus\_format\_exposition](group__prometheus.md#ga23b33f57ee6ad1154f7903b505e604b1)(const struct [prometheus\_collector](structprometheus__collector.md) \*collector, char \*buffer,

34 size\_t buffer\_size);

35

39

40#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_FORMATTER\_H\_ \*/

[collector.h](collector_8h.md)

Prometheus collector APIs.

[prometheus\_format\_exposition](group__prometheus.md#ga23b33f57ee6ad1154f7903b505e604b1)

int prometheus\_format\_exposition(const struct prometheus\_collector \*collector, char \*buffer, size\_t buffer\_size)

Format exposition data for Prometheus.

[prometheus\_collector](structprometheus__collector.md)

Prometheus collector definition.

**Definition** collector.h:32

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [formatter.h](formatter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
