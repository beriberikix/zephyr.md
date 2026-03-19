---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/metric_8h.html
original_path: doxygen/html/metric_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

metric.h File Reference

Prometheus metric interface.
[More...](#details)

`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/prometheus/label.h](label_8h_source.md)>`

[Go to the source code of this file.](metric_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [prometheus\_metric](structprometheus__metric.md) |
|  | Type used to represent a Prometheus metric base. [More...](structprometheus__metric.md#details) |

| Macros | |
| --- | --- |
| #define | [MAX\_METRIC\_NAME\_LENGTH](group__prometheus.md#ga0c2758847b60dece283eda02678edce8)   32 |
| #define | [MAX\_METRIC\_DESCRIPTION\_LENGTH](group__prometheus.md#ga9b788e35d8854a54faff830295b5b6ab)   64 |

| Enumerations | |
| --- | --- |
| enum | [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) { [PROMETHEUS\_COUNTER](group__prometheus.md#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b) = 0 , [PROMETHEUS\_GAUGE](group__prometheus.md#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd) , [PROMETHEUS\_SUMMARY](group__prometheus.md#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074) , [PROMETHEUS\_HISTOGRAM](group__prometheus.md#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf) } |
|  | Prometheus metric types. [More...](group__prometheus.md#ga3499408dda4e539634c332c797651932) |

## Detailed Description

Prometheus metric interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [metric.h](metric_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
