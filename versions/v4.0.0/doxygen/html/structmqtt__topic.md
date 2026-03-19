---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmqtt__topic.html
original_path: doxygen/html/structmqtt__topic.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_topic Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Abstracts MQTT UTF-8 encoded topic that can be subscribed to or published.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_utf8](structmqtt__utf8.md) | [topic](#ab859d08baf88e6a1ac5135e1e55158d5) |
|  | Topic on to be published or subscribed to. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [qos](#a780e90d62c094557bd3918de3b3921e6) |
|  | Quality of service requested for the subscription. |

## Detailed Description

Abstracts MQTT UTF-8 encoded topic that can be subscribed to or published.

## Field Documentation

## [◆ ](#a780e90d62c094557bd3918de3b3921e6)qos

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_topic::qos |
| --- |

Quality of service requested for the subscription.

[mqtt\_qos](group__mqtt__socket.md#ga396015e492b0fee8da37c7168d9cdb33 "mqtt_qos") for details.

## [◆ ](#ab859d08baf88e6a1ac5135e1e55158d5)topic

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_topic::topic |
| --- |

Topic on to be published or subscribed to.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_topic](structmqtt__topic.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
