---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structprometheus__label.html
original_path: doxygen/html/structprometheus__label.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_label Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Prometheus label definition.
[More...](#details)

`#include <[label.h](label_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [key](#a7abd6764903181f17ba88bd1745de72c) [16] |
|  | Prometheus metric label key. |
| char | [value](#a4e5ef1b230708ad9bfc4f61a933fbc36) [16] |
|  | Prometheus metric label value. |

## Detailed Description

Prometheus label definition.

This structure defines a Prometheus label.

## Field Documentation

## [◆ ](#a7abd6764903181f17ba88bd1745de72c)key

| char prometheus\_label::key[16] |
| --- |

Prometheus metric label key.

## [◆ ](#a4e5ef1b230708ad9bfc4f61a933fbc36)value

| char prometheus\_label::value[16] |
| --- |

Prometheus metric label value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[label.h](label_8h_source.md)

- [prometheus\_label](structprometheus__label.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
