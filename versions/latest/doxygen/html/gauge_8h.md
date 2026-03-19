---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gauge_8h.html
original_path: doxygen/html/gauge_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gauge.h File Reference

Prometheus gauge APIs.
[More...](#details)

`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/prometheus/metric.h](metric_8h_source.md)>`

[Go to the source code of this file.](gauge_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [prometheus\_gauge](structprometheus__gauge.md) |
|  | Type used to represent a Prometheus gauge metric. [More...](structprometheus__gauge.md#details) |

| Macros | |
| --- | --- |
| #define | [PROMETHEUS\_GAUGE\_DEFINE](group__prometheus.md#ga362e708722846a3ca9299e8994becd13)(\_name, \_desc, \_label, \_collector, ...) |
|  | Prometheus Gauge definition. |

| Functions | |
| --- | --- |
| int | [prometheus\_gauge\_set](group__prometheus.md#ga3ddc5efbdb9639486862f3df4b845fce) (struct [prometheus\_gauge](structprometheus__gauge.md) \*gauge, double value) |
|  | Set the value of a Prometheus gauge metric. |

## Detailed Description

Prometheus gauge APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [gauge.h](gauge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
