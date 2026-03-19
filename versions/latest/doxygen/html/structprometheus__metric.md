---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structprometheus__metric.html
original_path: doxygen/html/structprometheus__metric.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a68b4a71af679bef383d635f1b0018dba) |
|  | Slist metric list node. |
| struct [prometheus\_collector](structprometheus__collector.md) \* | [collector](#a1138f189a5bdd44639dace426ef8f55a) |
|  | Back pointer to the collector that this metric belongs to. |
| void \* | [metric](#a67e8d38a696f2b20a076b8da6b1250e3) |
|  | Back pointer to the actual metric (counter, gauge, etc.). |
| enum [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) | [type](#a05e19d7781f4724dfe7776e62cd69ca2) |
|  | Type of the Prometheus metric. |
| const char \* | [name](#a5266bf5bd528cdd4c34ea56d7a96129d) |
|  | Name of the Prometheus metric. |
| const char \* | [description](#a9ceba3f813e1bcf36c333af975c7ac76) |
|  | Description of the Prometheus metric. |
| struct [prometheus\_label](structprometheus__label.md) | [labels](#af3ae0862633b2ce475f7c6851d13c3d1) [[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)] |
|  | Labels associated with the Prometheus metric. |
| int | [num\_labels](#a198f0ddcf143d8728d914ee34eb8cb78) |
|  | Number of labels associated with the Prometheus metric. |
| void \* | [user\_data](#ae2db853cae2c49634fda25eb23b825da) |
|  | User defined data. |

## Detailed Description

Type used to represent a Prometheus metric base.

Every metric has a [prometheus\_metric](structprometheus__metric.md "Type used to represent a Prometheus metric base.") structure associated used to control the metric access and usage.

## Field Documentation

## [◆ ](#a1138f189a5bdd44639dace426ef8f55a)collector

| struct [prometheus\_collector](structprometheus__collector.md)\* prometheus\_metric::collector |
| --- |

Back pointer to the collector that this metric belongs to.

## [◆ ](#a9ceba3f813e1bcf36c333af975c7ac76)description

| const char\* prometheus\_metric::description |
| --- |

Description of the Prometheus metric.

## [◆ ](#af3ae0862633b2ce475f7c6851d13c3d1)labels

| struct [prometheus\_label](structprometheus__label.md) prometheus\_metric::labels[[MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)] |
| --- |

Labels associated with the Prometheus metric.

## [◆ ](#a67e8d38a696f2b20a076b8da6b1250e3)metric

| void\* prometheus\_metric::metric |
| --- |

Back pointer to the actual metric (counter, gauge, etc.).

This is just a temporary solution, ultimate goal is to place this generic metrict struct into the actual metric struct.

## [◆ ](#a5266bf5bd528cdd4c34ea56d7a96129d)name

| const char\* prometheus\_metric::name |
| --- |

Name of the Prometheus metric.

## [◆ ](#a68b4a71af679bef383d635f1b0018dba)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) prometheus\_metric::node |
| --- |

Slist metric list node.

## [◆ ](#a198f0ddcf143d8728d914ee34eb8cb78)num\_labels

| int prometheus\_metric::num\_labels |
| --- |

Number of labels associated with the Prometheus metric.

## [◆ ](#a05e19d7781f4724dfe7776e62cd69ca2)type

| enum [prometheus\_metric\_type](group__prometheus.md#ga3499408dda4e539634c332c797651932) prometheus\_metric::type |
| --- |

Type of the Prometheus metric.

## [◆ ](#ae2db853cae2c49634fda25eb23b825da)user\_data

| void\* prometheus\_metric::user\_data |
| --- |

User defined data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[metric.h](metric_8h_source.md)

- [prometheus\_metric](structprometheus__metric.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
