---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__client.html
original_path: doxygen/html/structmqtt__client.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_client Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

MQTT Client definition to maintain information relevant to the client.
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

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
| struct { |  |
| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md)   [user\_prop](#a726f5a806458d7dc9d6072dff74508fc) [CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |  |
|  | MQTT 5.0, chapter 3.1.3.2.8 User Property. [More...](#a726f5a806458d7dc9d6072dff74508fc) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [content\_type](#a89ce07fe536a502c051e4082b708155e) |  |
|  | MQTT 5.0, chapter 3.1.3.2.5 Content Type. [More...](#a89ce07fe536a502c051e4082b708155e) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [response\_topic](#ac6c53bf95f311a4df29d7db5f4c20b45) |  |
|  | MQTT 5.0, chapter 3.1.3.2.6 Response Topic. [More...](#ac6c53bf95f311a4df29d7db5f4c20b45) |
| struct [mqtt\_binstr](structmqtt__binstr.md)   [correlation\_data](#aac856189cedecf059f4ba723b06edda6) |  |
|  | MQTT 5.0, chapter 3.1.3.2.7 Correlation Data. [More...](#aac856189cedecf059f4ba723b06edda6) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [will\_delay\_interval](#a253bee13043ffe1ebe9c46299f8a238e) |  |
|  | MQTT 5.0, chapter 3.1.3.2.2 Will Delay Interval. [More...](#a253bee13043ffe1ebe9c46299f8a238e) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [message\_expiry\_interval](#a485855e9b09d0c48fb09c5673f38b5ee) |  |
|  | MQTT 5.0, chapter 3.1.3.2.4 Message Expiry Interval. [More...](#a485855e9b09d0c48fb09c5673f38b5ee) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [payload\_format\_indicator](#abdf2c45264ba77d584655b0cb6562c6b) |  |
|  | MQTT 5.0, chapter 3.1.3.2.3 Payload Format Indicator. [More...](#abdf2c45264ba77d584655b0cb6562c6b) |
| } | [will\_prop](#a0a1669a8be16d37819704ac60911de73) |
|  | MQTT 5.0 Will properties. |
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
| struct { |  |
| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md)   [user\_prop](#a726f5a806458d7dc9d6072dff74508fc) [CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |  |
|  | MQTT 5.0, chapter 3.1.2.11.8 User Property. [More...](#a726f5a806458d7dc9d6072dff74508fc) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [auth\_method](#ac899284f06f581cac0b647381c757287) |  |
|  | MQTT 5.0, chapter 3.1.2.11.9 Authentication Method. [More...](#ac899284f06f581cac0b647381c757287) |
| struct [mqtt\_binstr](structmqtt__binstr.md)   [auth\_data](#ae46c6695e9dfbf13cb895d8acad12d58) |  |
|  | MQTT 5.0, chapter 3.1.2.11.10 Authentication Data. [More...](#ae46c6695e9dfbf13cb895d8acad12d58) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [session\_expiry\_interval](#a1d0587f7b2be63eb74f9cba271c337fb) |  |
|  | MQTT 5.0, chapter 3.1.2.11.2 Session Expiry Interval. [More...](#a1d0587f7b2be63eb74f9cba271c337fb) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [maximum\_packet\_size](#a2d9fc66f26284f6ab90f79a4d7aef6d7) |  |
|  | MQTT 5.0, chapter 3.1.2.11.4 Maximum Packet Size. [More...](#a2d9fc66f26284f6ab90f79a4d7aef6d7) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [receive\_maximum](#a6700818bb78880e8b10878f31680f3d3) |  |
|  | MQTT 5.0, chapter 3.1.2.11.3 Receive Maximum. [More...](#a6700818bb78880e8b10878f31680f3d3) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [request\_response\_info](#a1c5a0e00803a745b2569452ed127440a) |  |
|  | MQTT 5.0, chapter 3.1.2.11.6 Request Response Information. [More...](#a1c5a0e00803a745b2569452ed127440a) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [request\_problem\_info](#a1a8f71b8756219a20404782c9aeff431) |  |
|  | MQTT 5.0, chapter 3.1.2.11.7 Request Response Information. [More...](#a1a8f71b8756219a20404782c9aeff431) |
| } | [prop](#a8c48cec6d0f895d05a8f933240348818) |
|  | MQTT 5.0 properties. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [will\_retain](#ac96879e15ccd829fbcf9b88913161c0d): 1 |
|  | Will retain flag, 1 if will message shall be retained persistently. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clean\_session](#aae9ecb0faf8dc4337579e0713d065184): 1 |
|  | Clean session flag indicating a fresh (1) or a retained session (0). |
| void \* | [user\_data](#afe138435d59720cc2c8c4b2756134a49) |
|  | User specific opaque data. |

## Detailed Description

MQTT Client definition to maintain information relevant to the client.

## Field Documentation

## [◆ ](#ae46c6695e9dfbf13cb895d8acad12d58)auth\_data

| struct [mqtt\_binstr](structmqtt__binstr.md) mqtt\_client::auth\_data |
| --- |

MQTT 5.0, chapter 3.1.2.11.10 Authentication Data.

## [◆ ](#ac899284f06f581cac0b647381c757287)auth\_method

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_client::auth\_method |
| --- |

MQTT 5.0, chapter 3.1.2.11.9 Authentication Method.

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

## [◆ ](#a89ce07fe536a502c051e4082b708155e)content\_type

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_client::content\_type |
| --- |

MQTT 5.0, chapter 3.1.3.2.5 Content Type.

## [◆ ](#aac856189cedecf059f4ba723b06edda6)correlation\_data

| struct [mqtt\_binstr](structmqtt__binstr.md) mqtt\_client::correlation\_data |
| --- |

MQTT 5.0, chapter 3.1.3.2.7 Correlation Data.

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

## [◆ ](#a2d9fc66f26284f6ab90f79a4d7aef6d7)maximum\_packet\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_client::maximum\_packet\_size |
| --- |

MQTT 5.0, chapter 3.1.2.11.4 Maximum Packet Size.

## [◆ ](#a485855e9b09d0c48fb09c5673f38b5ee)message\_expiry\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_client::message\_expiry\_interval |
| --- |

MQTT 5.0, chapter 3.1.3.2.4 Message Expiry Interval.

## [◆ ](#aef6da1db6f600a2bfd1c7dd0d78d1b6d)password

| struct [mqtt\_utf8](structmqtt__utf8.md)\* mqtt\_client::password |
| --- |

Password (if any) to be used for the connection.

Note that if password is provided, user name shall also be provided. NULL indicates no password.

## [◆ ](#abdf2c45264ba77d584655b0cb6562c6b)payload\_format\_indicator

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_client::payload\_format\_indicator |
| --- |

MQTT 5.0, chapter 3.1.3.2.3 Payload Format Indicator.

## [◆ ](#a8c48cec6d0f895d05a8f933240348818)[struct]

| struct { ... } mqtt\_client::prop |
| --- |

MQTT 5.0 properties.

## [◆ ](#a63e3c1b470a7de9d179b1c0686504a68)protocol\_version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_client::protocol\_version |
| --- |

MQTT protocol version.

## [◆ ](#a6700818bb78880e8b10878f31680f3d3)receive\_maximum

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_client::receive\_maximum |
| --- |

MQTT 5.0, chapter 3.1.2.11.3 Receive Maximum.

## [◆ ](#a1a8f71b8756219a20404782c9aeff431)request\_problem\_info

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_client::request\_problem\_info |
| --- |

MQTT 5.0, chapter 3.1.2.11.7 Request Response Information.

## [◆ ](#a1c5a0e00803a745b2569452ed127440a)request\_response\_info

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_client::request\_response\_info |
| --- |

MQTT 5.0, chapter 3.1.2.11.6 Request Response Information.

## [◆ ](#ac6c53bf95f311a4df29d7db5f4c20b45)response\_topic

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_client::response\_topic |
| --- |

MQTT 5.0, chapter 3.1.3.2.6 Response Topic.

## [◆ ](#a9f63fb54f8557135c1aa38a60bb7053c)rx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* mqtt\_client::rx\_buf |
| --- |

Receive buffer used for MQTT packet reception in RX path.

## [◆ ](#a66335741e991a2985ab5d4d7765651d2)rx\_buf\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_client::rx\_buf\_size |
| --- |

Size of receive buffer.

## [◆ ](#a1d0587f7b2be63eb74f9cba271c337fb)session\_expiry\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_client::session\_expiry\_interval |
| --- |

MQTT 5.0, chapter 3.1.2.11.2 Session Expiry Interval.

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

## [◆ ](#a726f5a806458d7dc9d6072dff74508fc)user\_prop

| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) mqtt\_client::user\_prop[CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |
| --- |

MQTT 5.0, chapter 3.1.3.2.8 User Property.

MQTT 5.0, chapter 3.1.2.11.8 User Property.

## [◆ ](#a253bee13043ffe1ebe9c46299f8a238e)will\_delay\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_client::will\_delay\_interval |
| --- |

MQTT 5.0, chapter 3.1.3.2.2 Will Delay Interval.

## [◆ ](#a7f4e9547b1d91edf21589334db711499)will\_message

| struct [mqtt\_utf8](structmqtt__utf8.md)\* mqtt\_client::will\_message |
| --- |

Will message.

Can be NULL. Non NULL value valid only if will topic is not NULL.

## [◆ ](#a0a1669a8be16d37819704ac60911de73)[struct]

| struct { ... } mqtt\_client::will\_prop |
| --- |

MQTT 5.0 Will properties.

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
