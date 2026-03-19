---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structprometheus__summary__quantile.html
original_path: doxygen/html/structprometheus__summary__quantile.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_summary\_quantile Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Prometheus summary quantile definition.
[More...](#details)

`#include <[summary.h](summary_8h_source.md)>`

| Data Fields | |
| --- | --- |
| double | [quantile](#a811db0cddd6fd444a899be83e4116b92) |
|  | Quantile of the summary. |
| double | [value](#a53fb78e35a0748f568d7bb15b083b037) |
|  | Value of the quantile. |
| void \* | [user\_data](#a788d30204d7ce61940741cefd2c073f6) |
|  | User data. |

## Detailed Description

Prometheus summary quantile definition.

This structure defines a Prometheus summary quantile.

## Field Documentation

## [◆ ](#a811db0cddd6fd444a899be83e4116b92)quantile

| double prometheus\_summary\_quantile::quantile |
| --- |

Quantile of the summary.

## [◆ ](#a788d30204d7ce61940741cefd2c073f6)user\_data

| void\* prometheus\_summary\_quantile::user\_data |
| --- |

User data.

## [◆ ](#a53fb78e35a0748f568d7bb15b083b037)value

| double prometheus\_summary\_quantile::value |
| --- |

Value of the quantile.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[summary.h](summary_8h_source.md)

- [prometheus\_summary\_quantile](structprometheus__summary__quantile.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
