---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/summary_8h.html
original_path: doxygen/html/summary_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

summary.h File Reference

Prometheus summary APIs.
[More...](#details)

`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/prometheus/metric.h](metric_8h_source.md)>`  
`#include <stddef.h>`

[Go to the source code of this file.](summary_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [prometheus\_summary\_quantile](structprometheus__summary__quantile.md) |
|  | Prometheus summary quantile definition. [More...](structprometheus__summary__quantile.md#details) |
| struct | [prometheus\_summary](structprometheus__summary.md) |
|  | Type used to represent a Prometheus summary metric. [More...](structprometheus__summary.md#details) |

| Macros | |
| --- | --- |
| #define | [PROMETHEUS\_SUMMARY\_DEFINE](group__prometheus.md#gaa3c043be86118ff9e8122136edc89cc4)(\_name, \_desc, \_label, \_collector, ...) |
|  | Prometheus Summary definition. |

| Functions | |
| --- | --- |
| int | [prometheus\_summary\_observe](group__prometheus.md#ga7683de05e8b135161120ad5d3f2edc2c) (struct [prometheus\_summary](structprometheus__summary.md) \*summary, double value) |
|  | Observes a value in a Prometheus summary metric. |
| int | [prometheus\_summary\_observe\_set](group__prometheus.md#ga98369eb2a7c8ce36f7570ed5b55410d8) (struct [prometheus\_summary](structprometheus__summary.md) \*summary, double value, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long count) |
|  | Set the summary value to specific value. |

## Detailed Description

Prometheus summary APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [summary.h](summary_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
