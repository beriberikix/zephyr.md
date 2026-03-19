---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/unionmqtt__evt__param.html
original_path: doxygen/html/unionmqtt__evt__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_evt\_param Union Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Defines event parameters notified along with asynchronous events to the application.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_connack\_param](structmqtt__connack__param.md) | [connack](#aa99a77bbade75b3f450088b32131f87a) |
|  | Parameters accompanying MQTT\_EVT\_CONNACK event. |
| struct [mqtt\_publish\_param](structmqtt__publish__param.md) | [publish](#a41be40873e1ebb9bf6fbf6dc9566d6ff) |
|  | Parameters accompanying MQTT\_EVT\_PUBLISH event. |
| struct [mqtt\_puback\_param](structmqtt__puback__param.md) | [puback](#a24bf756db9fa8cc67c0b02c4e2cb602c) |
|  | Parameters accompanying MQTT\_EVT\_PUBACK event. |
| struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) | [pubrec](#a3b31e1d94c480b8d0244cc12d1c25524) |
|  | Parameters accompanying MQTT\_EVT\_PUBREC event. |
| struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) | [pubrel](#a2269e07f580fb65df5f3d0832aa6b3af) |
|  | Parameters accompanying MQTT\_EVT\_PUBREL event. |
| struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) | [pubcomp](#ac3d564095019ccf57c10678a433bc31a) |
|  | Parameters accompanying MQTT\_EVT\_PUBCOMP event. |
| struct [mqtt\_suback\_param](structmqtt__suback__param.md) | [suback](#af6ce2426884d2faa443b3dfdaa45594c) |
|  | Parameters accompanying MQTT\_EVT\_SUBACK event. |
| struct [mqtt\_unsuback\_param](structmqtt__unsuback__param.md) | [unsuback](#ad040b028ed0aaabcaddedc204fb709d8) |
|  | Parameters accompanying MQTT\_EVT\_UNSUBACK event. |

## Detailed Description

Defines event parameters notified along with asynchronous events to the application.

## Field Documentation

## [◆ ](#aa99a77bbade75b3f450088b32131f87a)connack

| struct [mqtt\_connack\_param](structmqtt__connack__param.md) mqtt\_evt\_param::connack |
| --- |

Parameters accompanying MQTT\_EVT\_CONNACK event.

## [◆ ](#a24bf756db9fa8cc67c0b02c4e2cb602c)puback

| struct [mqtt\_puback\_param](structmqtt__puback__param.md) mqtt\_evt\_param::puback |
| --- |

Parameters accompanying MQTT\_EVT\_PUBACK event.

## [◆ ](#ac3d564095019ccf57c10678a433bc31a)pubcomp

| struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) mqtt\_evt\_param::pubcomp |
| --- |

Parameters accompanying MQTT\_EVT\_PUBCOMP event.

## [◆ ](#a41be40873e1ebb9bf6fbf6dc9566d6ff)publish

| struct [mqtt\_publish\_param](structmqtt__publish__param.md) mqtt\_evt\_param::publish |
| --- |

Parameters accompanying MQTT\_EVT\_PUBLISH event.

Note
:   PUBLISH event structure only contains payload size, the payload data parameter should be ignored. Payload content has to be read manually with [mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172 "mqtt_read_publish_payload") function.

## [◆ ](#a3b31e1d94c480b8d0244cc12d1c25524)pubrec

| struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) mqtt\_evt\_param::pubrec |
| --- |

Parameters accompanying MQTT\_EVT\_PUBREC event.

## [◆ ](#a2269e07f580fb65df5f3d0832aa6b3af)pubrel

| struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) mqtt\_evt\_param::pubrel |
| --- |

Parameters accompanying MQTT\_EVT\_PUBREL event.

## [◆ ](#af6ce2426884d2faa443b3dfdaa45594c)suback

| struct [mqtt\_suback\_param](structmqtt__suback__param.md) mqtt\_evt\_param::suback |
| --- |

Parameters accompanying MQTT\_EVT\_SUBACK event.

## [◆ ](#ad040b028ed0aaabcaddedc204fb709d8)unsuback

| struct [mqtt\_unsuback\_param](structmqtt__unsuback__param.md) mqtt\_evt\_param::unsuback |
| --- |

Parameters accompanying MQTT\_EVT\_UNSUBACK event.

---

The documentation for this union was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_evt\_param](unionmqtt__evt__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
