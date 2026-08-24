---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__pubrel__param.html
original_path: doxygen/html/structmqtt__pubrel__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_pubrel\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for MQTT publish release (PUBREL).
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#a4333fba7ac37d5a68fe921453b56b572) |
|  | Message id of the PUBREC message being acknowledged. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reason\_code](#a8fe8b7921add0b5fa2926a9eec68d102) |
|  | MQTT 5.0 reason code. |
| struct [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) | [prop](#a4e2c97c37bc4c43fd4a63391372dfed3) |
|  | MQTT 5.0 properties. |

## Detailed Description

Parameters for MQTT publish release (PUBREL).

## Field Documentation

## [◆ ](#a4333fba7ac37d5a68fe921453b56b572)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_pubrel\_param::message\_id |
| --- |

Message id of the PUBREC message being acknowledged.

## [◆ ](#a4e2c97c37bc4c43fd4a63391372dfed3)prop

| struct [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) mqtt\_pubrel\_param::prop |
| --- |

MQTT 5.0 properties.

## [◆ ](#a8fe8b7921add0b5fa2926a9eec68d102)reason\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_pubrel\_param::reason\_code |
| --- |

MQTT 5.0 reason code.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_pubrel\_param](structmqtt__pubrel__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
