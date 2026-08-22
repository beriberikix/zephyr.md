---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__transport.html
original_path: doxygen/html/structmqtt__transport.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_transport Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

MQTT transport specific data.
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [mqtt\_transport\_type](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4) | [type](#a47b49927c79e67b202112c68b53d83f4) |
|  | Transport type selection for client instance. |
| const char \* | [if\_name](#a7cfdf50105a275612dbda28e7c02808e) |
|  | Name of the interface that the MQTT client instance should be bound to. |
| union { |  |
| struct { |  |
| int   [sock](#a3b4589dd05394589e7af460761b800bf) |  |
|  | Socket descriptor. [More...](#a3b4589dd05394589e7af460761b800bf) |
| }   [tcp](#af65e3f0284ba9d881c5b916749f097b2) |
|  | TCP socket transport for MQTT. [More...](#af65e3f0284ba9d881c5b916749f097b2) |
| }; |  |
|  | Use either unsecured TCP or secured TLS transport. |

## Detailed Description

MQTT transport specific data.

## Field Documentation

## [◆ ](#a5e496cc21ba5d6088183efd57a9db959)[union]

| union { ... } [mqtt\_transport](structmqtt__transport.md) |
| --- |

Use either unsecured TCP or secured TLS transport.

## [◆ ](#a7cfdf50105a275612dbda28e7c02808e)if\_name

| const char\* mqtt\_transport::if\_name |
| --- |

Name of the interface that the MQTT client instance should be bound to.

Leave as NULL if not specified.

## [◆ ](#a3b4589dd05394589e7af460761b800bf)sock

| int mqtt\_transport::sock |
| --- |

Socket descriptor.

## [◆ ](#af65e3f0284ba9d881c5b916749f097b2)[struct]

| struct { ... } mqtt\_transport::tcp |
| --- |

TCP socket transport for MQTT.

## [◆ ](#a47b49927c79e67b202112c68b53d83f4)type

| enum [mqtt\_transport\_type](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4) mqtt\_transport::type |
| --- |

Transport type selection for client instance.

[mqtt\_transport\_type](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4 "mqtt_transport_type") for possible values. MQTT\_TRANSPORT\_MAX is not a valid type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_transport](structmqtt__transport.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
