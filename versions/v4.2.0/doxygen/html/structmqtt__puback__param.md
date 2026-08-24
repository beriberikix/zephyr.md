---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__puback__param.html
original_path: doxygen/html/structmqtt__puback__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_puback\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for MQTT publish acknowledgment (PUBACK).
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#a727b919b853e77e480fb841e74a2dedf) |
|  | Message id of the PUBLISH message being acknowledged. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reason\_code](#a44307fc6b172729478f1d097bbaf34bb) |
|  | MQTT 5.0 reason code. |
| struct [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) | [prop](#a5fbbc6613660883a96aa37c8def6baa5) |
|  | MQTT 5.0 properties. |

## Detailed Description

Parameters for MQTT publish acknowledgment (PUBACK).

## Field Documentation

## [◆ ](#a727b919b853e77e480fb841e74a2dedf)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_puback\_param::message\_id |
| --- |

Message id of the PUBLISH message being acknowledged.

## [◆ ](#a5fbbc6613660883a96aa37c8def6baa5)prop

| struct [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) mqtt\_puback\_param::prop |
| --- |

MQTT 5.0 properties.

## [◆ ](#a44307fc6b172729478f1d097bbaf34bb)reason\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_puback\_param::reason\_code |
| --- |

MQTT 5.0 reason code.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_puback\_param](structmqtt__puback__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
