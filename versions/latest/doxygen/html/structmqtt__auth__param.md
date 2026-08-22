---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__auth__param.html
original_path: doxygen/html/structmqtt__auth__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_auth\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for auth message.
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mqtt\_auth\_reason\_code](group__mqtt__socket.md#gacdbeff0450bbcd438cdf35cd543fc6d6) | [reason\_code](#adace77cd3860024ece2252ee41dcd134) |
| struct { |  |
| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md)   [user\_prop](#a1ad0e22ec7f3d5d1d304bacad06cb0c6) [CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |  |
|  | MQTT 5.0, chapter 3.15.2.2.5 User Property. [More...](#a1ad0e22ec7f3d5d1d304bacad06cb0c6) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [auth\_method](#a5602413c28ceadc87420f8c7a6c53489) |  |
|  | MQTT 5.0, chapter 3.15.2.2.2 Authentication Method. [More...](#a5602413c28ceadc87420f8c7a6c53489) |
| struct [mqtt\_binstr](structmqtt__binstr.md)   [auth\_data](#aaa1aa29efd09cf58aaf79b4e279dc2a9) |  |
|  | MQTT 5.0, chapter 3.15.2.2.3 Authentication Data. [More...](#aaa1aa29efd09cf58aaf79b4e279dc2a9) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [reason\_string](#a500d1b239b9882a1625d5d6035dd3199) |  |
|  | MQTT 5.0, chapter 3.15.2.2.4 Reason String. [More...](#a500d1b239b9882a1625d5d6035dd3199) |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_auth\_method](#a6cf278bec874623fcd97a5c5e7d43940) |  |
|  | Authentication Method property was present. [More...](#a6cf278bec874623fcd97a5c5e7d43940) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_auth\_data](#a32bfb124dbaa11a328e7300bc0890cfc) |  |
|  | Authentication Data property was present. [More...](#a32bfb124dbaa11a328e7300bc0890cfc) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_reason\_string](#a772343a4f3df425e54c00c43f5fdced4) |  |
|  | Reason String property was present. [More...](#a772343a4f3df425e54c00c43f5fdced4) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_user\_prop](#a50f570175c944f7e0dad4b276c07a6ea) |  |
|  | User Property property was present. [More...](#a50f570175c944f7e0dad4b276c07a6ea) |
| }   [rx](#a9403d927a86f90eb1847840d6f47fe37) |
|  | Flags indicating whether given property was present in received packet. [More...](#a9403d927a86f90eb1847840d6f47fe37) |
| } | [prop](#a6bd366cb6479370f9db0abaa22e1b803) |

## Detailed Description

Parameters for auth message.

## Field Documentation

## [◆ ](#aaa1aa29efd09cf58aaf79b4e279dc2a9)auth\_data

| struct [mqtt\_binstr](structmqtt__binstr.md) mqtt\_auth\_param::auth\_data |
| --- |

MQTT 5.0, chapter 3.15.2.2.3 Authentication Data.

## [◆ ](#a5602413c28ceadc87420f8c7a6c53489)auth\_method

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_auth\_param::auth\_method |
| --- |

MQTT 5.0, chapter 3.15.2.2.2 Authentication Method.

## [◆ ](#a32bfb124dbaa11a328e7300bc0890cfc)has\_auth\_data

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_auth\_param::has\_auth\_data |
| --- |

Authentication Data property was present.

## [◆ ](#a6cf278bec874623fcd97a5c5e7d43940)has\_auth\_method

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_auth\_param::has\_auth\_method |
| --- |

Authentication Method property was present.

## [◆ ](#a772343a4f3df425e54c00c43f5fdced4)has\_reason\_string

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_auth\_param::has\_reason\_string |
| --- |

Reason String property was present.

## [◆ ](#a50f570175c944f7e0dad4b276c07a6ea)has\_user\_prop

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_auth\_param::has\_user\_prop |
| --- |

User Property property was present.

## [◆ ](#a6bd366cb6479370f9db0abaa22e1b803)[struct]

| struct { ... } mqtt\_auth\_param::prop |
| --- |

## [◆ ](#adace77cd3860024ece2252ee41dcd134)reason\_code

| enum [mqtt\_auth\_reason\_code](group__mqtt__socket.md#gacdbeff0450bbcd438cdf35cd543fc6d6) mqtt\_auth\_param::reason\_code |
| --- |

## [◆ ](#a500d1b239b9882a1625d5d6035dd3199)reason\_string

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_auth\_param::reason\_string |
| --- |

MQTT 5.0, chapter 3.15.2.2.4 Reason String.

## [◆ ](#a9403d927a86f90eb1847840d6f47fe37)[struct]

| struct { ... } mqtt\_auth\_param::rx |
| --- |

Flags indicating whether given property was present in received packet.

## [◆ ](#a1ad0e22ec7f3d5d1d304bacad06cb0c6)user\_prop

| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) mqtt\_auth\_param::user\_prop[CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |
| --- |

MQTT 5.0, chapter 3.15.2.2.5 User Property.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_auth\_param](structmqtt__auth__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
