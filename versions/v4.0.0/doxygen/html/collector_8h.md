---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/collector_8h.html
original_path: doxygen/html/collector_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

collector.h File Reference

Prometheus collector APIs.
[More...](#details)

`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/prometheus/metric.h](metric_8h_source.md)>`  
`#include <stddef.h>`

[Go to the source code of this file.](collector_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [prometheus\_collector](structprometheus__collector.md) |
|  | Prometheus collector definition. [More...](structprometheus__collector.md#details) |

| Macros | |
| --- | --- |
| #define | [PROMETHEUS\_COLLECTOR\_DEFINE](group__prometheus.md#ga789b8557d1db7ad10133904e80e7f81c)(\_name) |
|  | Prometheus Collector definition. |

| Functions | |
| --- | --- |
| int | [prometheus\_collector\_register\_metric](group__prometheus.md#ga976b9e82d747570cde631b03ee805a26) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, struct [prometheus\_metric](structprometheus__metric.md) \*metric) |
|  | Register a metric with a Prometheus collector. |
| const void \* | [prometheus\_collector\_get\_metric](group__prometheus.md#ga428d008af1e84985bf7bce86ce0a408e) (const struct [prometheus\_collector](structprometheus__collector.md) \*collector, const char \*name) |
|  | Get a metric from a Prometheus collector. |

## Detailed Description

Prometheus collector APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [collector.h](collector_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
