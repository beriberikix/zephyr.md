---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structprometheus__counter.html
original_path: doxygen/html/structprometheus__counter.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_counter Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Type used to represent a Prometheus counter metric.
[More...](#details)

`#include <[counter.h](net_2prometheus_2counter_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [prometheus\_metric](structprometheus__metric.md) | [base](#a33714d75e20f8a69a7068c5c57fe3a37) |
|  | Base of the Prometheus counter metric. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [value](#a048376a671e83df41034908b85e9e234) |
|  | Value of the Prometheus counter metric. |
| void \* | [user\_data](#a28793edc31342bd6572493d7aa72eaca) |
|  | User data. |

## Detailed Description

Type used to represent a Prometheus counter metric.

- References
- See [https://prometheus.io/docs/concepts/metric\_types/#counter](https://prometheus.io/docs/concepts/metric_types/#counter)

## Field Documentation

## [◆ ](#a33714d75e20f8a69a7068c5c57fe3a37)base

| struct [prometheus\_metric](structprometheus__metric.md) prometheus\_counter::base |
| --- |

Base of the Prometheus counter metric.

## [◆ ](#a28793edc31342bd6572493d7aa72eaca)user\_data

| void\* prometheus\_counter::user\_data |
| --- |

User data.

## [◆ ](#a048376a671e83df41034908b85e9e234)value

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) prometheus\_counter::value |
| --- |

Value of the Prometheus counter metric.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[counter.h](net_2prometheus_2counter_8h_source.md)

- [prometheus\_counter](structprometheus__counter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
