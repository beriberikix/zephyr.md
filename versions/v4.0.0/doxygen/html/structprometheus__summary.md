---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structprometheus__summary.html
original_path: doxygen/html/structprometheus__summary.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_summary Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Type used to represent a Prometheus summary metric.
[More...](#details)

`#include <[summary.h](summary_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [prometheus\_metric](structprometheus__metric.md) \* | [base](#a4af4a8982ac633944e97480c9dbc0119) |
|  | Base of the Prometheus summary metric. |
| struct [prometheus\_summary\_quantile](structprometheus__summary__quantile.md) \* | [quantiles](#a2fa33910c03339df68c33b54d5f267d7) |
|  | Array of quantiles associated with the Prometheus summary metric. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [num\_quantiles](#a7e2604e9c9891137e7232ccaa9014c59) |
|  | Number of quantiles associated with the Prometheus summary metric. |
| double | [sum](#aead1e2754a146d36564472f8a1867da7) |
|  | Sum of all observed values in the summary metric. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [count](#a6cd8daf6014b485ccbca0dd3194e5d87) |
|  | Total count of observations in the summary metric. |

## Detailed Description

Type used to represent a Prometheus summary metric.

- References
- See [https://prometheus.io/docs/concepts/metric\_types/#summary](https://prometheus.io/docs/concepts/metric_types/#summary)

## Field Documentation

## [◆ ](#a4af4a8982ac633944e97480c9dbc0119)base

| struct [prometheus\_metric](structprometheus__metric.md)\* prometheus\_summary::base |
| --- |

Base of the Prometheus summary metric.

## [◆ ](#a6cd8daf6014b485ccbca0dd3194e5d87)count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long prometheus\_summary::count |
| --- |

Total count of observations in the summary metric.

## [◆ ](#a7e2604e9c9891137e7232ccaa9014c59)num\_quantiles

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) prometheus\_summary::num\_quantiles |
| --- |

Number of quantiles associated with the Prometheus summary metric.

## [◆ ](#a2fa33910c03339df68c33b54d5f267d7)quantiles

| struct [prometheus\_summary\_quantile](structprometheus__summary__quantile.md)\* prometheus\_summary::quantiles |
| --- |

Array of quantiles associated with the Prometheus summary metric.

## [◆ ](#aead1e2754a146d36564472f8a1867da7)sum

| double prometheus\_summary::sum |
| --- |

Sum of all observed values in the summary metric.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[summary.h](summary_8h_source.md)

- [prometheus\_summary](structprometheus__summary.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
