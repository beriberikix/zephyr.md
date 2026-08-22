---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__publish__param.html
original_path: doxygen/html/structmqtt__publish__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_publish\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for a publish message (PUBLISH).
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

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
| struct { |  |
| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md)   [user\_prop](#a813b18b4c859fb5e703d90fc8eb9bd2e) [CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |  |
|  | MQTT 5.0, chapter 3.3.2.3.7 User Property. [More...](#a813b18b4c859fb5e703d90fc8eb9bd2e) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [response\_topic](#a63e9311cf0acf33386ceb8328b040d2a) |  |
|  | MQTT 5.0, chapter 3.3.2.3.5 Response Topic. [More...](#a63e9311cf0acf33386ceb8328b040d2a) |
| struct [mqtt\_binstr](structmqtt__binstr.md)   [correlation\_data](#ab98e52ae704c6e988d554cf388b2ec0c) |  |
|  | MQTT 5.0, chapter 3.3.2.3.6 Correlation Data. [More...](#ab98e52ae704c6e988d554cf388b2ec0c) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [content\_type](#a8f76494a04d91150aee2ed7e9a271243) |  |
|  | MQTT 5.0, chapter 3.3.2.3.9 Content Type. [More...](#a8f76494a04d91150aee2ed7e9a271243) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [subscription\_identifier](#a5edb680fe44b795b02e35fcb73b98efa) [CONFIG\_MQTT\_SUBSCRIPTION\_ID\_PROPERTIES\_MAX] |  |
|  | MQTT 5.0, chapter 3.3.2.3.8 Subscription Identifier. [More...](#a5edb680fe44b795b02e35fcb73b98efa) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [message\_expiry\_interval](#a4a486b254bd8e0f081251f8ca087e9d2) |  |
|  | MQTT 5.0, chapter 3.3.2.3.3 Message Expiry Interval. [More...](#a4a486b254bd8e0f081251f8ca087e9d2) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [topic\_alias](#a13bf77403471f79687fe63a93cd1627d) |  |
|  | MQTT 5.0, chapter 3.3.2.3.4 Topic Alias. [More...](#a13bf77403471f79687fe63a93cd1627d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [payload\_format\_indicator](#a8d9905f31bfc9072516f00082eda9c50) |  |
|  | MQTT 5.0, chapter 3.3.2.3.2 Payload Format Indicator. [More...](#a8d9905f31bfc9072516f00082eda9c50) |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_payload\_format\_indicator](#a4190ccdfbf97a4ef63121e6a841d5f79) |  |
|  | Payload Format Indicator property was present. [More...](#a4190ccdfbf97a4ef63121e6a841d5f79) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_message\_expiry\_interval](#a85e5a3a9c7347c506780627515dc84ea) |  |
|  | Message Expiry Interval property was present. [More...](#a85e5a3a9c7347c506780627515dc84ea) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_topic\_alias](#a36a4d07ed13c5d4befc51a6285606090) |  |
|  | Topic Alias property was present. [More...](#a36a4d07ed13c5d4befc51a6285606090) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_response\_topic](#aafc5473b88a64df887751903314f0fac) |  |
|  | Response Topic property was present. [More...](#aafc5473b88a64df887751903314f0fac) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_correlation\_data](#a599f8830ef4b42a68955ad58411ef0f1) |  |
|  | Correlation Data property was present. [More...](#a599f8830ef4b42a68955ad58411ef0f1) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_user\_prop](#a5e4b146a69c82fa36fd43adb8658ef5f) |  |
|  | User Property property was present. [More...](#a5e4b146a69c82fa36fd43adb8658ef5f) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_subscription\_identifier](#aab2664e89f086b62b9af5cd481fccde3) |  |
|  | Subscription Identifier property was present. [More...](#aab2664e89f086b62b9af5cd481fccde3) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_content\_type](#a00413022cecf2a624506ab5da630aefa) |  |
|  | Content Type property was present. [More...](#a00413022cecf2a624506ab5da630aefa) |
| }   [rx](#a9cf950636bfa82b88bd4c3fc562c8f71) |
|  | Flags indicating whether given property was present in received packet. [More...](#a9cf950636bfa82b88bd4c3fc562c8f71) |
| } | [prop](#a5e87084f72285ebdf5d26aca0eed6f00) |
|  | MQTT 5.0 properties. |

## Detailed Description

Parameters for a publish message (PUBLISH).

## Field Documentation

## [◆ ](#a8f76494a04d91150aee2ed7e9a271243)content\_type

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_publish\_param::content\_type |
| --- |

MQTT 5.0, chapter 3.3.2.3.9 Content Type.

## [◆ ](#ab98e52ae704c6e988d554cf388b2ec0c)correlation\_data

| struct [mqtt\_binstr](structmqtt__binstr.md) mqtt\_publish\_param::correlation\_data |
| --- |

MQTT 5.0, chapter 3.3.2.3.6 Correlation Data.

## [◆ ](#a2c2062c2b3ad027d5dfea56cb81c48e7)dup\_flag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_publish\_param::dup\_flag |
| --- |

Duplicate flag.

If 1, it indicates the message is being retransmitted. Has no meaning with QoS 0.

## [◆ ](#a00413022cecf2a624506ab5da630aefa)has\_content\_type

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_publish\_param::has\_content\_type |
| --- |

Content Type property was present.

## [◆ ](#a599f8830ef4b42a68955ad58411ef0f1)has\_correlation\_data

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_publish\_param::has\_correlation\_data |
| --- |

Correlation Data property was present.

## [◆ ](#a85e5a3a9c7347c506780627515dc84ea)has\_message\_expiry\_interval

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_publish\_param::has\_message\_expiry\_interval |
| --- |

Message Expiry Interval property was present.

## [◆ ](#a4190ccdfbf97a4ef63121e6a841d5f79)has\_payload\_format\_indicator

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_publish\_param::has\_payload\_format\_indicator |
| --- |

Payload Format Indicator property was present.

## [◆ ](#aafc5473b88a64df887751903314f0fac)has\_response\_topic

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_publish\_param::has\_response\_topic |
| --- |

Response Topic property was present.

## [◆ ](#aab2664e89f086b62b9af5cd481fccde3)has\_subscription\_identifier

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_publish\_param::has\_subscription\_identifier |
| --- |

Subscription Identifier property was present.

## [◆ ](#a36a4d07ed13c5d4befc51a6285606090)has\_topic\_alias

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_publish\_param::has\_topic\_alias |
| --- |

Topic Alias property was present.

## [◆ ](#a5e4b146a69c82fa36fd43adb8658ef5f)has\_user\_prop

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_publish\_param::has\_user\_prop |
| --- |

User Property property was present.

## [◆ ](#a9841a4fbb30b597a9710863ce6034688)message

| struct [mqtt\_publish\_message](structmqtt__publish__message.md) mqtt\_publish\_param::message |
| --- |

Messages including topic, QoS and its payload (if any) to be published.

## [◆ ](#a4a486b254bd8e0f081251f8ca087e9d2)message\_expiry\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_publish\_param::message\_expiry\_interval |
| --- |

MQTT 5.0, chapter 3.3.2.3.3 Message Expiry Interval.

## [◆ ](#aac4c6ba605506c183d2d5bdd7e550b3e)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_publish\_param::message\_id |
| --- |

Message id used for the publish message.

Redundant for QoS 0.

## [◆ ](#a8d9905f31bfc9072516f00082eda9c50)payload\_format\_indicator

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_publish\_param::payload\_format\_indicator |
| --- |

MQTT 5.0, chapter 3.3.2.3.2 Payload Format Indicator.

## [◆ ](#a5e87084f72285ebdf5d26aca0eed6f00)[struct]

| struct { ... } mqtt\_publish\_param::prop |
| --- |

MQTT 5.0 properties.

## [◆ ](#a63e9311cf0acf33386ceb8328b040d2a)response\_topic

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_publish\_param::response\_topic |
| --- |

MQTT 5.0, chapter 3.3.2.3.5 Response Topic.

## [◆ ](#a9b2c6fad5bf830276d8d3f6b5ab04210)retain\_flag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_publish\_param::retain\_flag |
| --- |

Retain flag.

If 1, the message shall be stored persistently by the broker.

## [◆ ](#a9cf950636bfa82b88bd4c3fc562c8f71)[struct]

| struct { ... } mqtt\_publish\_param::rx |
| --- |

Flags indicating whether given property was present in received packet.

## [◆ ](#a5edb680fe44b795b02e35fcb73b98efa)subscription\_identifier

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_publish\_param::subscription\_identifier[CONFIG\_MQTT\_SUBSCRIPTION\_ID\_PROPERTIES\_MAX] |
| --- |

MQTT 5.0, chapter 3.3.2.3.8 Subscription Identifier.

## [◆ ](#a13bf77403471f79687fe63a93cd1627d)topic\_alias

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_publish\_param::topic\_alias |
| --- |

MQTT 5.0, chapter 3.3.2.3.4 Topic Alias.

## [◆ ](#a813b18b4c859fb5e703d90fc8eb9bd2e)user\_prop

| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) mqtt\_publish\_param::user\_prop[CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |
| --- |

MQTT 5.0, chapter 3.3.2.3.7 User Property.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_publish\_param](structmqtt__publish__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
