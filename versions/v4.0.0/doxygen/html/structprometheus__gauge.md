---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structprometheus__gauge.html
original_path: doxygen/html/structprometheus__gauge.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_gauge Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Type used to represent a Prometheus gauge metric.
[More...](#details)

`#include <[gauge.h](gauge_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [prometheus\_metric](structprometheus__metric.md) \* | [base](#a619e838dd218710d1563e50aaf4cb83b) |
|  | Base of the Prometheus gauge metric. |
| double | [value](#aabf12d85b93d419e19d9c300cb6313a7) |
|  | Value of the Prometheus gauge metric. |

## Detailed Description

Type used to represent a Prometheus gauge metric.

- References
- See [https://prometheus.io/docs/concepts/metric\_types/#gauge](https://prometheus.io/docs/concepts/metric_types/#gauge)

## Field Documentation

## [◆ ](#a619e838dd218710d1563e50aaf4cb83b)base

| struct [prometheus\_metric](structprometheus__metric.md)\* prometheus\_gauge::base |
| --- |

Base of the Prometheus gauge metric.

## [◆ ](#aabf12d85b93d419e19d9c300cb6313a7)value

| double prometheus\_gauge::value |
| --- |

Value of the Prometheus gauge metric.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[gauge.h](gauge_8h_source.md)

- [prometheus\_gauge](structprometheus__gauge.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
