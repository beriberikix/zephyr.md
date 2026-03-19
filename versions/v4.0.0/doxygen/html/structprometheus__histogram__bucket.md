---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structprometheus__histogram__bucket.html
original_path: doxygen/html/structprometheus__histogram__bucket.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

prometheus\_histogram\_bucket Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Prometheus API](group__prometheus.md)

Prometheus histogram bucket definition.
[More...](#details)

`#include <[histogram.h](histogram_8h_source.md)>`

| Data Fields | |
| --- | --- |
| double | [upper\_bound](#aa18e37384ee094972b6a330bb4323fa3) |
|  | Upper bound value of bucket. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [count](#a93865334a397013506d39a28505586c4) |
|  | Cumulative count of observations in the bucket. |

## Detailed Description

Prometheus histogram bucket definition.

This structure defines a Prometheus histogram bucket.

## Field Documentation

## [◆ ](#a93865334a397013506d39a28505586c4)count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long prometheus\_histogram\_bucket::count |
| --- |

Cumulative count of observations in the bucket.

## [◆ ](#aa18e37384ee094972b6a330bb4323fa3)upper\_bound

| double prometheus\_histogram\_bucket::upper\_bound |
| --- |

Upper bound value of bucket.

---

The documentation for this struct was generated from the following file:

- zephyr/net/prometheus/[histogram.h](histogram_8h_source.md)

- [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
