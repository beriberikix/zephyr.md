---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlwm2m__time__series__elem.html
original_path: doxygen/html/structlwm2m__time__series__elem.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lwm2m\_time\_series\_elem Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [LwM2M high-level API](group__lwm2m__api.md)

LwM2M Time series data structure.
[More...](#details)

`#include <[lwm2m.h](lwm2m_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) | [t](#acd00227c551b6ee1960b3881819ef90b) |
|  | Cached data Unix timestamp. |
| union { |  |
| }; |  |
|  | Element value. |

## Detailed Description

LwM2M Time series data structure.

## Field Documentation

## [◆ ](#a270084824d5685f4e9552d4249218c0b)[union]

| union { ... } [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) |
| --- |

Element value.

## [◆ ](#acd00227c551b6ee1960b3881819ef90b)t

| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) lwm2m\_time\_series\_elem::t |
| --- |

Cached data Unix timestamp.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lwm2m.h](lwm2m_8h_source.md)

- [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
