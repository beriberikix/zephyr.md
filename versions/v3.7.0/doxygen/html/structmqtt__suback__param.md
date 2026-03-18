---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmqtt__suback__param.html
original_path: doxygen/html/structmqtt__suback__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_suback\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for MQTT subscription acknowledgment (SUBACK).
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#a985b53444e7b2c10ab68844fcee34ee4) |
|  | Message id of the SUBSCRIBE message being acknowledged. |
| struct [mqtt\_binstr](structmqtt__binstr.md) | [return\_codes](#a94ef5183aa3438db0521f445650c5868) |
|  | Return codes indicating maximum QoS level granted for each topic in the subscription list. |

## Detailed Description

Parameters for MQTT subscription acknowledgment (SUBACK).

## Field Documentation

## [◆ ](#a985b53444e7b2c10ab68844fcee34ee4)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_suback\_param::message\_id |
| --- |

Message id of the SUBSCRIBE message being acknowledged.

## [◆ ](#a94ef5183aa3438db0521f445650c5868)return\_codes

| struct [mqtt\_binstr](structmqtt__binstr.md) mqtt\_suback\_param::return\_codes |
| --- |

Return codes indicating maximum QoS level granted for each topic in the subscription list.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_suback\_param](structmqtt__suback__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
