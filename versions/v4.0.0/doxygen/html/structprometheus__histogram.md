---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structprometheus__histogram.html
original_path: doxygen/html/structprometheus__histogram.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_histogram Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Type used to represent a Prometheus histogram metric.
[More...](#details)

`#include <[histogram.h](histogram_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [prometheus\_metric](structprometheus__metric.md) \* | [base](#a951618ccaba4f4eac27efe21ea17fa90) |
|  | Base of the Prometheus histogram metric. |
| struct [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md) \* | [buckets](#a2f37871231727963173b7336ea8cfafb) |
|  | Array of buckets in the histogram. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [num\_buckets](#a01cfda4eab91d6776b7f7b11279d2785) |
|  | Number of buckets in the histogram. |
| double | [sum](#a65616857524ef4eeb09a577e0432e787) |
|  | Sum of all observed values in the histogram. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [count](#a6ae0aad29b927a729263324704917873) |
|  | Total count of observations in the histogram. |

## Detailed Description

Type used to represent a Prometheus histogram metric.

- References
- See [https://prometheus.io/docs/concepts/metric\_types/#histogram](https://prometheus.io/docs/concepts/metric_types/#histogram)

## Field Documentation

## [◆ ](#a951618ccaba4f4eac27efe21ea17fa90)base

| struct [prometheus\_metric](structprometheus__metric.md)\* prometheus\_histogram::base |
| --- |

Base of the Prometheus histogram metric.

## [◆ ](#a2f37871231727963173b7336ea8cfafb)buckets

| struct [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md)\* prometheus\_histogram::buckets |
| --- |

Array of buckets in the histogram.

## [◆ ](#a6ae0aad29b927a729263324704917873)count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long prometheus\_histogram::count |
| --- |

Total count of observations in the histogram.

## [◆ ](#a01cfda4eab91d6776b7f7b11279d2785)num\_buckets

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) prometheus\_histogram::num\_buckets |
| --- |

Number of buckets in the histogram.

## [◆ ](#a65616857524ef4eeb09a577e0432e787)sum

| double prometheus\_histogram::sum |
| --- |

Sum of all observed values in the histogram.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[histogram.h](histogram_8h_source.md)

- [prometheus\_histogram](structprometheus__histogram.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
