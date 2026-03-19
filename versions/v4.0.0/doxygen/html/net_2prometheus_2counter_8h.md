---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net_2prometheus_2counter_8h.html
original_path: doxygen/html/net_2prometheus_2counter_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter.h File Reference

Prometheus counter APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/prometheus/metric.h](metric_8h_source.md)>`

[Go to the source code of this file.](net_2prometheus_2counter_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [prometheus\_counter](structprometheus__counter.md) |
|  | Type used to represent a Prometheus counter metric. [More...](structprometheus__counter.md#details) |

| Macros | |
| --- | --- |
| #define | [PROMETHEUS\_COUNTER\_DEFINE](group__prometheus.md#ga467bbac42b48995598dbd370277b243b)(\_name, \_detail) |
|  | Prometheus Counter definition. |

| Functions | |
| --- | --- |
| int | [prometheus\_counter\_inc](group__prometheus.md#ga911670f61fa22d3834aecf5351c944e4) (struct [prometheus\_counter](structprometheus__counter.md) \*counter) |
|  | Increment the value of a Prometheus counter metric Increments the value of the specified counter metric by one. |

## Detailed Description

Prometheus counter APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [counter.h](net_2prometheus_2counter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
