---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsensing__connection.html
original_path: doxygen/html/structsensing__connection.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_connection Struct Reference

[Sensing](group__sensing.md) » [Sensing Sensor API](group__sensing__sensor.md)

Connection between a source and sink of sensor data.
[More...](#details)

`#include <[sensing_sensor.h](sensing__sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [snode](#a0ed58bb9a5227c6113c9eb4e5568729b) |
| struct [sensing\_sensor](structsensing__sensor.md) \* | [source](#ab5cb1fd5ed2de2bf7a41143fc4cdc51b) |
| struct [sensing\_sensor](structsensing__sensor.md) \* | [sink](#a79223ce36e160a3f2b8adffccaf7fb09) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval](#a9c6a1b8bc3c5b80d2368fb01b316391c) |
| int | [sensitivity](#a1c831b73840d686b742b90eebaf42083) [CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT] |
| void \* | [data](#a3d3d6463ff7c6a142657c6a8b016ea53) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [next\_consume\_time](#ae3d82838cca620f234d3a4638c91d61a) |
| struct [sensing\_callback\_list](structsensing__callback__list.md) \* | [callback\_list](#a3ab7dc6ce305b594661e5ab9dbfa0512) |

## Detailed Description

Connection between a source and sink of sensor data.

## Field Documentation

## [◆ ](#a3ab7dc6ce305b594661e5ab9dbfa0512)callback\_list

| struct [sensing\_callback\_list](structsensing__callback__list.md)\* sensing\_connection::callback\_list |
| --- |

## [◆ ](#a3d3d6463ff7c6a142657c6a8b016ea53)data

| void\* sensing\_connection::data |
| --- |

## [◆ ](#a9c6a1b8bc3c5b80d2368fb01b316391c)interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_connection::interval |
| --- |

## [◆ ](#ae3d82838cca620f234d3a4638c91d61a)next\_consume\_time

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sensing\_connection::next\_consume\_time |
| --- |

## [◆ ](#a1c831b73840d686b742b90eebaf42083)sensitivity

| int sensing\_connection::sensitivity[CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT] |
| --- |

## [◆ ](#a79223ce36e160a3f2b8adffccaf7fb09)sink

| struct [sensing\_sensor](structsensing__sensor.md)\* sensing\_connection::sink |
| --- |

## [◆ ](#a0ed58bb9a5227c6113c9eb4e5568729b)snode

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) sensing\_connection::snode |
| --- |

## [◆ ](#ab5cb1fd5ed2de2bf7a41143fc4cdc51b)source

| struct [sensing\_sensor](structsensing__sensor.md)\* sensing\_connection::source |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing\_sensor.h](sensing__sensor_8h_source.md)

- [sensing\_connection](structsensing__connection.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
