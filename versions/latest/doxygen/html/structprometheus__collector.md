---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structprometheus__collector.html
original_path: doxygen/html/structprometheus__collector.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [metrics](#a389528dad4e2ada62ca85650b6be5972) |
|  | Array of metrics associated with the collector. |
| struct [k\_mutex](structk__mutex.md) | [lock](#a43e08aa447c0388d80771c33f59992b7) |
|  | Mutex to protect the metrics list manipulation. |
| [prometheus\_scrape\_cb\_t](group__prometheus.md#ga4e2541cb094915187157d44a29e2d6b5) | [user\_cb](#ae131dcdd35fbacd30a210b547718c6be) |
|  | User callback function. |
| void \* | [user\_data](#acd2c684c0c920f75e86d2560b4bb29e2) |
|  | User data. |

## Detailed Description

Prometheus collector definition.

This structure defines a Prometheus collector.

## Field Documentation

## [◆ ](#a43e08aa447c0388d80771c33f59992b7)lock

| struct [k\_mutex](structk__mutex.md) prometheus\_collector::lock |
| --- |

Mutex to protect the metrics list manipulation.

## [◆ ](#a389528dad4e2ada62ca85650b6be5972)metrics

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) prometheus\_collector::metrics |
| --- |

Array of metrics associated with the collector.

## [◆ ](#a050b6094f92369225dce734ef9f50476)name

| const char\* prometheus\_collector::name |
| --- |

Name of the collector.

## [◆ ](#ae131dcdd35fbacd30a210b547718c6be)user\_cb

| [prometheus\_scrape\_cb\_t](group__prometheus.md#ga4e2541cb094915187157d44a29e2d6b5) prometheus\_collector::user\_cb |
| --- |

User callback function.

If set, then the metric data is fetched via the function callback.

## [◆ ](#acd2c684c0c920f75e86d2560b4bb29e2)user\_data

| void\* prometheus\_collector::user\_data |
| --- |

User data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[collector.h](collector_8h_source.md)

- [prometheus\_collector](structprometheus__collector.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
