---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmqtt__client.html
original_path: doxygen/html/structmqtt__client.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_client Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

MQTT Client definition to maintain information relevant to the client.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_internal](structmqtt__internal.md) | [internal](#a41cc1d3c5e5180af1d6376f88598678a) |
|  | MQTT client internal state. |
| struct [mqtt\_transport](structmqtt__transport.md) | [transport](#ac31a2ea9d67886f83fd3af88f33f36d9) |
|  | MQTT transport configuration and data. |
| struct [mqtt\_utf8](structmqtt__utf8.md) | [client\_id](#aabd419115c8637e4e4c0e6d23a5a984d) |
|  | Unique client identification to be used for the connection. |
| const void \* | [broker](#a72d61d9c0e717010ff90c2ed7fcddf5c) |
|  | Broker details, for example, address, port. |
| struct [mqtt\_utf8](structmqtt__utf8.md) \* | [user\_name](#ab271f2061fe3c9e3c1a76158a1c00449) |
|  | User name (if any) to be used for the connection. |
| struct [mqtt\_utf8](structmqtt__utf8.md) \* | [password](#aef6da1db6f600a2bfd1c7dd0d78d1b6d) |
|  | Password (if any) to be used for the connection. |
| struct [mqtt\_topic](structmqtt__topic.md) \* | [will\_topic](#a4b23a72831697b78dc4019a4b6ac97e4) |
|  | Will topic and QoS. |
| struct [mqtt\_utf8](structmqtt__utf8.md) \* | [will\_message](#a7f4e9547b1d91edf21589334db711499) |
|  | Will message. |
| [mqtt\_evt\_cb\_t](group__mqtt__socket.md#gabdf01ededb62ceb4c1608a64cb718a8c) | [evt\_cb](#a44c515b8b25d59554990f6193217d83f) |
|  | Application callback registered with the module to get MQTT events. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [rx\_buf](#a9f63fb54f8557135c1aa38a60bb7053c) |
|  | Receive buffer used for MQTT packet reception in RX path. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rx\_buf\_size](#a66335741e991a2985ab5d4d7765651d2) |
|  | Size of receive buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [tx\_buf](#ae582274bf396caa0a3427f1aeace639c) |
|  | Transmit buffer used for creating MQTT packet in TX path. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_buf\_size](#a4c456f4065e3bc20752d908f2d805667) |
|  | Size of transmit buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [keepalive](#aa65a4af5952634e4ff5c4bf700ccccd7) |
|  | Keepalive interval for this client in seconds. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [protocol\_version](#a63e3c1b470a7de9d179b1c0686504a68) |
|  | MQTT protocol version. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [unacked\_ping](#a67f76cd0feadf8ae11ed232dcc9ac1d1) |
|  | Unanswered PINGREQ count on this connection. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [will\_retain](#ac96879e15ccd829fbcf9b88913161c0d): 1 |
|  | Will retain flag, 1 if will message shall be retained persistently. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clean\_session](#aae9ecb0faf8dc4337579e0713d065184): 1 |
|  | Clean session flag indicating a fresh (1) or a retained session (0). |
| void \* | [user\_data](#afe138435d59720cc2c8c4b2756134a49) |
|  | User specific opaque data. |

## Detailed Description

MQTT Client definition to maintain information relevant to the client.

## Field Documentation

## [◆ ](#a72d61d9c0e717010ff90c2ed7fcddf5c)broker

| const void\* mqtt\_client::broker |
| --- |

Broker details, for example, address, port.

Address type should be compatible with transport used.

## [◆ ](#aae9ecb0faf8dc4337579e0713d065184)clean\_session

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_client::clean\_session |
| --- |

Clean session flag indicating a fresh (1) or a retained session (0).

Default is CONFIG\_MQTT\_CLEAN\_SESSION.

## [◆ ](#aabd419115c8637e4e4c0e6d23a5a984d)client\_id

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_client::client\_id |
| --- |

Unique client identification to be used for the connection.

## [◆ ](#a44c515b8b25d59554990f6193217d83f)evt\_cb

| [mqtt\_evt\_cb\_t](group__mqtt__socket.md#gabdf01ededb62ceb4c1608a64cb718a8c) mqtt\_client::evt\_cb |
| --- |

Application callback registered with the module to get MQTT events.

## [◆ ](#a41cc1d3c5e5180af1d6376f88598678a)internal

| struct [mqtt\_internal](structmqtt__internal.md) mqtt\_client::internal |
| --- |

MQTT client internal state.

## [◆ ](#aa65a4af5952634e4ff5c4bf700ccccd7)keepalive

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_client::keepalive |
| --- |

Keepalive interval for this client in seconds.

Default is CONFIG\_MQTT\_KEEPALIVE.

## [◆ ](#aef6da1db6f600a2bfd1c7dd0d78d1b6d)password

| struct [mqtt\_utf8](structmqtt__utf8.md)\* mqtt\_client::password |
| --- |

Password (if any) to be used for the connection.

Note that if password is provided, user name shall also be provided. NULL indicates no password.

## [◆ ](#a63e3c1b470a7de9d179b1c0686504a68)protocol\_version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_client::protocol\_version |
| --- |

MQTT protocol version.

## [◆ ](#a9f63fb54f8557135c1aa38a60bb7053c)rx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* mqtt\_client::rx\_buf |
| --- |

Receive buffer used for MQTT packet reception in RX path.

## [◆ ](#a66335741e991a2985ab5d4d7765651d2)rx\_buf\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_client::rx\_buf\_size |
| --- |

Size of receive buffer.

## [◆ ](#ac31a2ea9d67886f83fd3af88f33f36d9)transport

| struct [mqtt\_transport](structmqtt__transport.md) mqtt\_client::transport |
| --- |

MQTT transport configuration and data.

## [◆ ](#ae582274bf396caa0a3427f1aeace639c)tx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* mqtt\_client::tx\_buf |
| --- |

Transmit buffer used for creating MQTT packet in TX path.

## [◆ ](#a4c456f4065e3bc20752d908f2d805667)tx\_buf\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_client::tx\_buf\_size |
| --- |

Size of transmit buffer.

## [◆ ](#a67f76cd0feadf8ae11ed232dcc9ac1d1)unacked\_ping

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) mqtt\_client::unacked\_ping |
| --- |

Unanswered PINGREQ count on this connection.

## [◆ ](#afe138435d59720cc2c8c4b2756134a49)user\_data

| void\* mqtt\_client::user\_data |
| --- |

User specific opaque data.

## [◆ ](#ab271f2061fe3c9e3c1a76158a1c00449)user\_name

| struct [mqtt\_utf8](structmqtt__utf8.md)\* mqtt\_client::user\_name |
| --- |

User name (if any) to be used for the connection.

NULL indicates no user name.

## [◆ ](#a7f4e9547b1d91edf21589334db711499)will\_message

| struct [mqtt\_utf8](structmqtt__utf8.md)\* mqtt\_client::will\_message |
| --- |

Will message.

Can be NULL. Non NULL value valid only if will topic is not NULL.

## [◆ ](#ac96879e15ccd829fbcf9b88913161c0d)will\_retain

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_client::will\_retain |
| --- |

Will retain flag, 1 if will message shall be retained persistently.

## [◆ ](#a4b23a72831697b78dc4019a4b6ac97e4)will\_topic

| struct [mqtt\_topic](structmqtt__topic.md)\* mqtt\_client::will\_topic |
| --- |

Will topic and QoS.

Can be NULL.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_client](structmqtt__client.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
