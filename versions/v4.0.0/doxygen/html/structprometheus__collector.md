---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structprometheus__collector.html
original_path: doxygen/html/structprometheus__collector.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_collector Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Prometheus collector definition.
[More...](#details)

`#include <[collector.h](collector_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#a050b6094f92369225dce734ef9f50476) |
|  | Name of the collector. |
| struct [prometheus\_metric](structprometheus__metric.md) \* | [metric](#a3200e70f16799313b33e9cf3a5949f0c) [CONFIG\_PROMETHEUS\_MAX\_METRICS] |
|  | Array of metrics associated with the collector. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a1bf1167b74db303eab6bf561e823a6ea) |
|  | Number of metrics associated with the collector. |

## Detailed Description

Prometheus collector definition.

This structure defines a Prometheus collector.

## Field Documentation

## [◆ ](#a3200e70f16799313b33e9cf3a5949f0c)metric

| struct [prometheus\_metric](structprometheus__metric.md)\* prometheus\_collector::metric[CONFIG\_PROMETHEUS\_MAX\_METRICS] |
| --- |

Array of metrics associated with the collector.

## [◆ ](#a050b6094f92369225dce734ef9f50476)name

| const char\* prometheus\_collector::name |
| --- |

Name of the collector.

## [◆ ](#a1bf1167b74db303eab6bf561e823a6ea)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) prometheus\_collector::size |
| --- |

Number of metrics associated with the collector.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[collector.h](collector_8h_source.md)

- [prometheus\_collector](structprometheus__collector.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
