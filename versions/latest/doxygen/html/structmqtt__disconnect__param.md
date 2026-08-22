---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__disconnect__param.html
original_path: doxygen/html/structmqtt__disconnect__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_disconnect\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for disconnect message.
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mqtt\_disconnect\_reason\_code](group__mqtt__socket.md#gaaf563f26ca66841145643a657119d780) | [reason\_code](#aa1b60dae11e0cad827e2d9942c1137e4) |
| struct { |  |
| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md)   [user\_prop](#a03050c6d4879f0d0eb62093b340bb99c) [CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |  |
|  | MQTT 5.0, chapter 3.14.2.2.4 User Property. [More...](#a03050c6d4879f0d0eb62093b340bb99c) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [reason\_string](#a7a3b72acdd5a2d239c9e3d78e59bb4c2) |  |
|  | MQTT 5.0, chapter 3.14.2.2.3 Reason String. [More...](#a7a3b72acdd5a2d239c9e3d78e59bb4c2) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [server\_reference](#aa44656e2663a058070a3d30e3bdabee9) |  |
|  | MQTT 5.0, chapter 3.14.2.2.5 Server Reference. [More...](#aa44656e2663a058070a3d30e3bdabee9) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [session\_expiry\_interval](#a9a0531c1fb9b95019bb49f1642d54b07) |  |
|  | MQTT 5.0, chapter 3.14.2.2.2 Session Expiry Interval. [More...](#a9a0531c1fb9b95019bb49f1642d54b07) |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_session\_expiry\_interval](#a2360cc037d244abed416ace079f82257) |  |
|  | Session Expiry Interval property was present. [More...](#a2360cc037d244abed416ace079f82257) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_reason\_string](#ae2077e489cf38f4bccfebb78a840b9fe) |  |
|  | Reason String property was present. [More...](#ae2077e489cf38f4bccfebb78a840b9fe) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_user\_prop](#a02b38f24432c8def5dcda439bc8e9ab7) |  |
|  | User Property property was present. [More...](#a02b38f24432c8def5dcda439bc8e9ab7) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_server\_reference](#a8891e52deb9c40f4f838f1df67db9794) |  |
|  | Server Reference property was present. [More...](#a8891e52deb9c40f4f838f1df67db9794) |
| }   [rx](#a6fb48a1ddf15d525f13f979758a06132) |
|  | Flags indicating whether given property was present in received packet. [More...](#a6fb48a1ddf15d525f13f979758a06132) |
| } | [prop](#aa211770e88640378928e3ed3d09c23ac) |
|  | MQTT 5.0 properties. |

## Detailed Description

Parameters for disconnect message.

## Field Documentation

## [◆ ](#ae2077e489cf38f4bccfebb78a840b9fe)has\_reason\_string

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_disconnect\_param::has\_reason\_string |
| --- |

Reason String property was present.

## [◆ ](#a8891e52deb9c40f4f838f1df67db9794)has\_server\_reference

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_disconnect\_param::has\_server\_reference |
| --- |

Server Reference property was present.

## [◆ ](#a2360cc037d244abed416ace079f82257)has\_session\_expiry\_interval

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_disconnect\_param::has\_session\_expiry\_interval |
| --- |

Session Expiry Interval property was present.

## [◆ ](#a02b38f24432c8def5dcda439bc8e9ab7)has\_user\_prop

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_disconnect\_param::has\_user\_prop |
| --- |

User Property property was present.

## [◆ ](#aa211770e88640378928e3ed3d09c23ac)[struct]

| struct { ... } mqtt\_disconnect\_param::prop |
| --- |

MQTT 5.0 properties.

## [◆ ](#aa1b60dae11e0cad827e2d9942c1137e4)reason\_code

| enum [mqtt\_disconnect\_reason\_code](group__mqtt__socket.md#gaaf563f26ca66841145643a657119d780) mqtt\_disconnect\_param::reason\_code |
| --- |

## [◆ ](#a7a3b72acdd5a2d239c9e3d78e59bb4c2)reason\_string

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_disconnect\_param::reason\_string |
| --- |

MQTT 5.0, chapter 3.14.2.2.3 Reason String.

## [◆ ](#a6fb48a1ddf15d525f13f979758a06132)[struct]

| struct { ... } mqtt\_disconnect\_param::rx |
| --- |

Flags indicating whether given property was present in received packet.

## [◆ ](#aa44656e2663a058070a3d30e3bdabee9)server\_reference

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_disconnect\_param::server\_reference |
| --- |

MQTT 5.0, chapter 3.14.2.2.5 Server Reference.

## [◆ ](#a9a0531c1fb9b95019bb49f1642d54b07)session\_expiry\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_disconnect\_param::session\_expiry\_interval |
| --- |

MQTT 5.0, chapter 3.14.2.2.2 Session Expiry Interval.

## [◆ ](#a03050c6d4879f0d0eb62093b340bb99c)user\_prop

| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) mqtt\_disconnect\_param::user\_prop[CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |
| --- |

MQTT 5.0, chapter 3.14.2.2.4 User Property.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_disconnect\_param](structmqtt__disconnect__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
