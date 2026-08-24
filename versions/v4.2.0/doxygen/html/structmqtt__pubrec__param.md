---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__pubrec__param.html
original_path: doxygen/html/structmqtt__pubrec__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_pubrec\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for MQTT publish receive (PUBREC).
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#ab0f92884dbd6e63894210ff7f57fe62c) |
|  | Message id of the PUBLISH message being acknowledged. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reason\_code](#a4d52112e88d954a88e4c65c9be5b0b93) |
|  | MQTT 5.0 reason code. |
| struct [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) | [prop](#acf7d23d86fa5a7d935711459e52b092d) |
|  | MQTT 5.0 properties. |

## Detailed Description

Parameters for MQTT publish receive (PUBREC).

## Field Documentation

## [◆ ](#ab0f92884dbd6e63894210ff7f57fe62c)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_pubrec\_param::message\_id |
| --- |

Message id of the PUBLISH message being acknowledged.

## [◆ ](#acf7d23d86fa5a7d935711459e52b092d)prop

| struct [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) mqtt\_pubrec\_param::prop |
| --- |

MQTT 5.0 properties.

## [◆ ](#a4d52112e88d954a88e4c65c9be5b0b93)reason\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_pubrec\_param::reason\_code |
| --- |

MQTT 5.0 reason code.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_pubrec\_param](structmqtt__pubrec__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
