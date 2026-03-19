---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/histogram_8h.html
original_path: doxygen/html/histogram_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

histogram.h File Reference

Prometheus histogram APIs.
[More...](#details)

`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/prometheus/metric.h](metric_8h_source.md)>`  
`#include <stddef.h>`

[Go to the source code of this file.](histogram_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md) |
|  | Prometheus histogram bucket definition. [More...](structprometheus__histogram__bucket.md#details) |
| struct | [prometheus\_histogram](structprometheus__histogram.md) |
|  | Type used to represent a Prometheus histogram metric. [More...](structprometheus__histogram.md#details) |

| Macros | |
| --- | --- |
| #define | [PROMETHEUS\_HISTOGRAM\_DEFINE](group__prometheus.md#gada4920e35290a96a76566cc6b4ab5a60)(\_name, \_detail) |
|  | Prometheus Histogram definition. |

| Functions | |
| --- | --- |
| int | [prometheus\_histogram\_observe](group__prometheus.md#gaf0f24e64833302b74397654001ca5026) (struct [prometheus\_histogram](structprometheus__histogram.md) \*histogram, double value) |
|  | Observe a value in a Prometheus histogram metric. |

## Detailed Description

Prometheus histogram APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [histogram.h](histogram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
