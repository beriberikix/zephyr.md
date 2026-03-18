---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmqtt__sn__evt.html
original_path: doxygen/html/structmqtt__sn__evt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_sn\_evt Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT-SN Client library](group__mqtt__sn__socket.md)

MQTT-SN event structure to be handled by the event callback.
[More...](#details)

`#include <[mqtt_sn.h](mqtt__sn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42) | [type](#aef636c6acdc17831acb44095fbef1885) |
|  | Event type. |
| union [mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md) | [param](#a8e75d71d1b38e1b84bf1ad20063ec4e8) |
|  | Event parameters. |

## Detailed Description

MQTT-SN event structure to be handled by the event callback.

## Field Documentation

## [◆ ](#a8e75d71d1b38e1b84bf1ad20063ec4e8)param

| union [mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md) mqtt\_sn\_evt::param |
| --- |

Event parameters.

## [◆ ](#aef636c6acdc17831acb44095fbef1885)type

| enum [mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42) mqtt\_sn\_evt::type |
| --- |

Event type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt\_sn.h](mqtt__sn_8h_source.md)

- [mqtt\_sn\_evt](structmqtt__sn__evt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
