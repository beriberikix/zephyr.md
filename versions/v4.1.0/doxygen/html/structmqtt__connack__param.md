---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmqtt__connack__param.html
original_path: doxygen/html/structmqtt__connack__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_connack\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for a connection acknowledgment (CONNACK).
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [session\_present\_flag](#ab123a8236804082667ad93ddd7e40e7a) |
|  | The Session Present flag enables a Client to establish whether the Client and Server have a consistent view about whether there is already stored Session state. |
| enum [mqtt\_conn\_return\_code](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618) | [return\_code](#a07e8ca2df92b2f83fc9e732a9c9964f4) |
|  | The appropriate non-zero Connect return code indicates if the Server is unable to process a connection request for some reason. |

## Detailed Description

Parameters for a connection acknowledgment (CONNACK).

## Field Documentation

## [◆ ](#a07e8ca2df92b2f83fc9e732a9c9964f4)return\_code

| enum [mqtt\_conn\_return\_code](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618) mqtt\_connack\_param::return\_code |
| --- |

The appropriate non-zero Connect return code indicates if the Server is unable to process a connection request for some reason.

## [◆ ](#ab123a8236804082667ad93ddd7e40e7a)session\_present\_flag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_connack\_param::session\_present\_flag |
| --- |

The Session Present flag enables a Client to establish whether the Client and Server have a consistent view about whether there is already stored Session state.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_connack\_param](structmqtt__connack__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
