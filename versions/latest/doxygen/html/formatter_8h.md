---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/formatter_8h.html
original_path: doxygen/html/formatter_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

formatter.h File Reference

Prometheus formatter APIs.
[More...](#details)

`#include <[zephyr/net/prometheus/collector.h](collector_8h_source.md)>`

[Go to the source code of this file.](formatter_8h_source.md)

| Functions | |
| --- | --- |
| int | [prometheus\_format\_exposition](group__prometheus.md#ga7d219be7f2b3b49a2f936489bdf68fe8) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Format exposition data for Prometheus. |
| int | [prometheus\_format\_one\_metric](group__prometheus.md#ga2240cf4f807fe7180f21c8fab3fbbd66) (struct [prometheus\_metric](structprometheus__metric.md) \*metric, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size, int \*written) |
|  | Format exposition data for one metric for Prometheus. |

## Detailed Description

Prometheus formatter APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [formatter.h](formatter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
