---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__unsuback__param.html
original_path: doxygen/html/structmqtt__unsuback__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_unsuback\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for MQTT unsubscribe acknowledgment (UNSUBACK).
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#aa453177181e07cd0532b8cf591be0f32) |
|  | Message id of the UNSUBSCRIBE message being acknowledged. |
| struct [mqtt\_binstr](structmqtt__binstr.md) | [reason\_codes](#a992c0c038413377c8edd701d2ef8455e) |
|  | Reason codes corresponding to each topic in the unsubscription list. |
| struct [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) | [prop](#a543fb60386725e9096bb0243beaa1181) |
|  | MQTT 5.0 properties. |

## Detailed Description

Parameters for MQTT unsubscribe acknowledgment (UNSUBACK).

## Field Documentation

## [◆ ](#aa453177181e07cd0532b8cf591be0f32)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_unsuback\_param::message\_id |
| --- |

Message id of the UNSUBSCRIBE message being acknowledged.

## [◆ ](#a543fb60386725e9096bb0243beaa1181)prop

| struct [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) mqtt\_unsuback\_param::prop |
| --- |

MQTT 5.0 properties.

## [◆ ](#a992c0c038413377c8edd701d2ef8455e)reason\_codes

| struct [mqtt\_binstr](structmqtt__binstr.md) mqtt\_unsuback\_param::reason\_codes |
| --- |

Reason codes corresponding to each topic in the unsubscription list.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_unsuback\_param](structmqtt__unsuback__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
