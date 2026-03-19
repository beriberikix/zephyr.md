---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structprometheus__metric.html
original_path: doxygen/html/structprometheus__metric.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_metric Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Type used to represent a Prometheus metric base.
[More...](#details)

`#include <[metric.h](metric_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) | [type](#a05e19d7781f4724dfe7776e62cd69ca2) |
|  | Type of the Prometheus metric. |
| char | [name](#af32069fd653d50cefce48c0e90c96b69) [32] |
|  | Name of the Prometheus metric. |
| char | [description](#af751f2601dafffdbe06acf63d4cdfcbf) [64] |
|  | Description of the Prometheus metric. |
| struct [prometheus\_label](structprometheus__label.md) | [labels](#af3ae0862633b2ce475f7c6851d13c3d1) [[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)] |
|  | Labels associated with the Prometheus metric. |
| int | [num\_labels](#a198f0ddcf143d8728d914ee34eb8cb78) |
|  | Number of labels associated with the Prometheus metric. |

## Detailed Description

Type used to represent a Prometheus metric base.

Every metric has a [prometheus\_metric](structprometheus__metric.md "Type used to represent a Prometheus metric base.") structure associated used to control the metric access and usage.

## Field Documentation

## [◆ ](#af751f2601dafffdbe06acf63d4cdfcbf)description

| char prometheus\_metric::description[64] |
| --- |

Description of the Prometheus metric.

## [◆ ](#af3ae0862633b2ce475f7c6851d13c3d1)labels

| struct [prometheus\_label](structprometheus__label.md) prometheus\_metric::labels[[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)] |
| --- |

Labels associated with the Prometheus metric.

## [◆ ](#af32069fd653d50cefce48c0e90c96b69)name

| char prometheus\_metric::name[32] |
| --- |

Name of the Prometheus metric.

## [◆ ](#a198f0ddcf143d8728d914ee34eb8cb78)num\_labels

| int prometheus\_metric::num\_labels |
| --- |

Number of labels associated with the Prometheus metric.

## [◆ ](#a05e19d7781f4724dfe7776e62cd69ca2)type

| enum [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) prometheus\_metric::type |
| --- |

Type of the Prometheus metric.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[metric.h](metric_8h_source.md)

- [prometheus\_metric](structprometheus__metric.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
