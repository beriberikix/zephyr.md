---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmqtt__publish__param.html
original_path: doxygen/html/structmqtt__publish__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_publish\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for a publish message (PUBLISH).
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_publish\_message](structmqtt__publish__message.md) | [message](#a9841a4fbb30b597a9710863ce6034688) |
|  | Messages including topic, QoS and its payload (if any) to be published. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#aac4c6ba605506c183d2d5bdd7e550b3e) |
|  | Message id used for the publish message. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dup\_flag](#a2c2062c2b3ad027d5dfea56cb81c48e7): 1 |
|  | Duplicate flag. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [retain\_flag](#a9b2c6fad5bf830276d8d3f6b5ab04210): 1 |
|  | Retain flag. |

## Detailed Description

Parameters for a publish message (PUBLISH).

## Field Documentation

## [◆ ](#a2c2062c2b3ad027d5dfea56cb81c48e7)dup\_flag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_publish\_param::dup\_flag |
| --- |

Duplicate flag.

If 1, it indicates the message is being retransmitted. Has no meaning with QoS 0.

## [◆ ](#a9841a4fbb30b597a9710863ce6034688)message

| struct [mqtt\_publish\_message](structmqtt__publish__message.md) mqtt\_publish\_param::message |
| --- |

Messages including topic, QoS and its payload (if any) to be published.

## [◆ ](#aac4c6ba605506c183d2d5bdd7e550b3e)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_publish\_param::message\_id |
| --- |

Message id used for the publish message.

Redundant for QoS 0.

## [◆ ](#a9b2c6fad5bf830276d8d3f6b5ab04210)retain\_flag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_publish\_param::retain\_flag |
| --- |

Retain flag.

If 1, the message shall be stored persistently by the broker.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_publish\_param](structmqtt__publish__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
