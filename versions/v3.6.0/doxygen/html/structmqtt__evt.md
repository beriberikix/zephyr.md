---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmqtt__evt.html
original_path: doxygen/html/structmqtt__evt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_evt Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Defines MQTT asynchronous event notified to the application.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mqtt\_evt\_type](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91) | [type](#a79d7a198d8ed9959bb7aae835b6301c2) |
|  | Identifies the event. |
| union [mqtt\_evt\_param](unionmqtt__evt__param.md) | [param](#aca1085171667c46b2438f66d9227e07c) |
|  | Contains parameters (if any) accompanying the event. |
| int | [result](#aa1a4304d4aa70440ba630f3fe5e76d2f) |
|  | Event result. |

## Detailed Description

Defines MQTT asynchronous event notified to the application.

## Field Documentation

## [◆ ](#aca1085171667c46b2438f66d9227e07c)param

| union [mqtt\_evt\_param](unionmqtt__evt__param.md) mqtt\_evt::param |
| --- |

Contains parameters (if any) accompanying the event.

## [◆ ](#aa1a4304d4aa70440ba630f3fe5e76d2f)result

| int mqtt\_evt::result |
| --- |

Event result.

0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#a79d7a198d8ed9959bb7aae835b6301c2)type

| enum [mqtt\_evt\_type](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91) mqtt\_evt::type |
| --- |

Identifies the event.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_evt](structmqtt__evt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
