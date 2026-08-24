---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__common__ack__properties.html
original_path: doxygen/html/structmqtt__common__ack__properties.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_common\_ack\_properties Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Common MQTT 5.0 properties shared across all ack-type messages.
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) | [user\_prop](#aa827f37cfc537e00e8ff4e774ec9b835) [CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |
|  | MQTT 5.0, chapter 3.4.2.2.3 User Property. |
| struct [mqtt\_utf8](structmqtt__utf8.md) | [reason\_string](#a282e39c4e3bdcebf331969fdf0a60570) |
|  | MQTT 5.0, chapter 3.4.2.2.2 Reason String. |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_reason\_string](#abf672bc44df434fe2dd4f519343d6480) |  |
|  | Reason String property was present. [More...](#abf672bc44df434fe2dd4f519343d6480) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_user\_prop](#a69d6a6795e309cb64bff1dd3eeb698c6) |  |
|  | User Property property was present. [More...](#a69d6a6795e309cb64bff1dd3eeb698c6) |
| } | [rx](#a87c543e4eb14b9e1e1fbd9fe7d4b047b) |
|  | Flags indicating whether given property was present in received packet. |

## Detailed Description

Common MQTT 5.0 properties shared across all ack-type messages.

## Field Documentation

## [◆ ](#abf672bc44df434fe2dd4f519343d6480)has\_reason\_string

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_common\_ack\_properties::has\_reason\_string |
| --- |

Reason String property was present.

## [◆ ](#a69d6a6795e309cb64bff1dd3eeb698c6)has\_user\_prop

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_common\_ack\_properties::has\_user\_prop |
| --- |

User Property property was present.

## [◆ ](#a282e39c4e3bdcebf331969fdf0a60570)reason\_string

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_common\_ack\_properties::reason\_string |
| --- |

MQTT 5.0, chapter 3.4.2.2.2 Reason String.

## [◆ ](#a87c543e4eb14b9e1e1fbd9fe7d4b047b)[struct]

| struct { ... } mqtt\_common\_ack\_properties::rx |
| --- |

Flags indicating whether given property was present in received packet.

## [◆ ](#aa827f37cfc537e00e8ff4e774ec9b835)user\_prop

| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) mqtt\_common\_ack\_properties::user\_prop[CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |
| --- |

MQTT 5.0, chapter 3.4.2.2.3 User Property.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
