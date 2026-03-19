---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/collector_8h.html
original_path: doxygen/html/collector_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

collector.h File Reference

Prometheus collector APIs.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
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
| #define | [PROMETHEUS\_COLLECTOR\_DEFINE](group__prometheus.md#gaab3a797c867c6492dedb2b51774a48e5)(\_name, ...) |
|  | Prometheus Collector definition. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [prometheus\_scrape\_cb\_t](group__prometheus.md#ga4e2541cb094915187157d44a29e2d6b5)) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, struct [prometheus\_metric](structprometheus__metric.md) \*metric, void \*user\_data) |
|  | Callback used to scrape a collector for a specific metric. |

| Functions | |
| --- | --- |
| int | [prometheus\_collector\_register\_metric](group__prometheus.md#ga976b9e82d747570cde631b03ee805a26) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, struct [prometheus\_metric](structprometheus__metric.md) \*metric) |
|  | Register a metric with a Prometheus collector. |
| const void \* | [prometheus\_collector\_get\_metric](group__prometheus.md#ga757252a9157538870b1360924b16d0e0) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, const char \*name) |
|  | Get a metric from a Prometheus collector. |
| int | [prometheus\_collector\_walk\_metrics](group__prometheus.md#ga1bbdd8d5447144b21d3cda1ddac38ff0) (struct prometheus\_collector\_walk\_context \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Walk through all metrics in a Prometheus collector and format them into a buffer. |
| static int | [prometheus\_collector\_walk\_init](group__prometheus.md#ga1c70215409029bbe163bdfdb03bfba43) (struct prometheus\_collector\_walk\_context \*ctx, struct [prometheus\_collector](structprometheus__collector.md) \*collector) |
|  | Initialize the walker context to walk through all metrics. |

## Detailed Description

Prometheus collector APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [collector.h](collector_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
