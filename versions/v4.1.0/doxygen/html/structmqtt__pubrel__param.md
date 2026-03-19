---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmqtt__pubrel__param.html
original_path: doxygen/html/structmqtt__pubrel__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_pubrel\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for MQTT publish release (PUBREL).
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#a4333fba7ac37d5a68fe921453b56b572) |
|  | Message id of the PUBREC message being acknowledged. |

## Detailed Description

Parameters for MQTT publish release (PUBREL).

## Field Documentation

## [◆ ](#a4333fba7ac37d5a68fe921453b56b572)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_pubrel\_param::message\_id |
| --- |

Message id of the PUBREC message being acknowledged.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_pubrel\_param](structmqtt__pubrel__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
