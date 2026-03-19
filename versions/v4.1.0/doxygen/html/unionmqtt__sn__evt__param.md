---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unionmqtt__sn__evt__param.html
original_path: doxygen/html/unionmqtt__sn__evt__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_sn\_evt\_param Union Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT-SN Client library](group__mqtt__sn__socket.md)

Event metadata.
[More...](#details)

`#include <[mqtt_sn.h](mqtt__sn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| struct [mqtt\_sn\_data](structmqtt__sn__data.md)   [data](#a2440375957dae427bb61526331052567) |  |
|  | The payload data associated with the event. [More...](#a2440375957dae427bb61526331052567) |
| enum [mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd)   [topic\_type](#ab7930bb48e91a24a79593e375f17cdf1) |  |
|  | The type of topic for the event. [More...](#ab7930bb48e91a24a79593e375f17cdf1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [topic\_id](#ae79e9793f8fc70cc781c4527d8f8496d) |  |
|  | The identifier for the topic of the event. [More...](#ae79e9793f8fc70cc781c4527d8f8496d) |
| } | [publish](#afa0ea7d03a7ffdc95c68848af4c9f3ae) |
|  | Structure holding publish event details. |

## Detailed Description

Event metadata.

## Field Documentation

## [◆ ](#a2440375957dae427bb61526331052567)data

| struct [mqtt\_sn\_data](structmqtt__sn__data.md) mqtt\_sn\_evt\_param::data |
| --- |

The payload data associated with the event.

## [◆ ](#afa0ea7d03a7ffdc95c68848af4c9f3ae)[struct]

| struct { ... } mqtt\_sn\_evt\_param::publish |
| --- |

Structure holding publish event details.

## [◆ ](#ae79e9793f8fc70cc781c4527d8f8496d)topic\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_sn\_evt\_param::topic\_id |
| --- |

The identifier for the topic of the event.

## [◆ ](#ab7930bb48e91a24a79593e375f17cdf1)topic\_type

| enum [mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd) mqtt\_sn\_evt\_param::topic\_type |
| --- |

The type of topic for the event.

---

The documentation for this union was generated from the following file:

- zephyr/net/[mqtt\_sn.h](mqtt__sn_8h_source.md)

- [mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
