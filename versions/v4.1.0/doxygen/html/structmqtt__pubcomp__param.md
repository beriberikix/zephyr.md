---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmqtt__pubcomp__param.html
original_path: doxygen/html/structmqtt__pubcomp__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_pubcomp\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for MQTT publish complete (PUBCOMP).
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#ae8484ad4d62f953ecace6c990002e316) |
|  | Message id of the PUBREL message being acknowledged. |

## Detailed Description

Parameters for MQTT publish complete (PUBCOMP).

## Field Documentation

## [◆ ](#ae8484ad4d62f953ecace6c990002e316)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_pubcomp\_param::message\_id |
| --- |

Message id of the PUBREL message being acknowledged.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
