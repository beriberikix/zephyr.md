---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__connack__param.html
original_path: doxygen/html/structmqtt__connack__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_connack\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for a connection acknowledgment (CONNACK).
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [session\_present\_flag](#ab123a8236804082667ad93ddd7e40e7a) |
|  | The Session Present flag enables a Client to establish whether the Client and Server have a consistent view about whether there is already stored Session state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [return\_code](#aae7a54dd6f62887b618f652f260ed6bd) |
|  | The appropriate non-zero Connect return code indicates if the Server is unable to process a connection request for some reason. |
| struct { |  |
| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md)   [user\_prop](#a29eed1a34902519380aa59757bde501c) [CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |  |
|  | MQTT 5.0, chapter 3.2.2.3.10 User Property. [More...](#a29eed1a34902519380aa59757bde501c) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [assigned\_client\_id](#a7f275e22d6cdf808b1f0a19c3f78f517) |  |
|  | MQTT 5.0, chapter 3.2.2.3.7 Assigned Client Identifier. [More...](#a7f275e22d6cdf808b1f0a19c3f78f517) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [reason\_string](#a5fbdc09eff6fef2f06a98c8f9faf0a03) |  |
|  | MQTT 5.0, chapter 3.2.2.3.9 Reason String. [More...](#a5fbdc09eff6fef2f06a98c8f9faf0a03) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [response\_information](#a1314e5735f128b905bd3d78beaee956e) |  |
|  | MQTT 5.0, chapter 3.2.2.3.15 Response Information. [More...](#a1314e5735f128b905bd3d78beaee956e) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [server\_reference](#a0426044dfe84d5160d1116018265eda3) |  |
|  | MQTT 5.0, chapter 3.2.2.3.16 Server Reference. [More...](#a0426044dfe84d5160d1116018265eda3) |
| struct [mqtt\_utf8](structmqtt__utf8.md)   [auth\_method](#abbd4490c94846009f79c741e3067c743) |  |
|  | MQTT 5.0, chapter 3.2.2.3.17 Authentication Method. [More...](#abbd4490c94846009f79c741e3067c743) |
| struct [mqtt\_binstr](structmqtt__binstr.md)   [auth\_data](#ad45d67943848406b290fee98e5d4d3ba) |  |
|  | MQTT 5.0, chapter 3.2.2.3.18 Authentication Data. [More...](#ad45d67943848406b290fee98e5d4d3ba) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [session\_expiry\_interval](#a7e47864579e36ea469d198ceb9cdd3f4) |  |
|  | MQTT 5.0, chapter 3.2.2.3.2 Session Expiry Interval. [More...](#a7e47864579e36ea469d198ceb9cdd3f4) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [maximum\_packet\_size](#a8e5cab6b3479fc9e902feb622008386a) |  |
|  | MQTT 5.0, chapter 3.2.2.3.6 Maximum Packet Size. [More...](#a8e5cab6b3479fc9e902feb622008386a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [receive\_maximum](#a9eecd31595fa1332a1cf4b661cedeae2) |  |
|  | MQTT 5.0, chapter 3.3.2.3.3 Receive Maximum. [More...](#a9eecd31595fa1332a1cf4b661cedeae2) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [topic\_alias\_maximum](#a09cdb8430a3ced98055b564716201bf1) |  |
|  | MQTT 5.0, chapter 3.2.2.3.8 Topic Alias Maximum. [More...](#a09cdb8430a3ced98055b564716201bf1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [server\_keep\_alive](#af21ff08751c63f17423500c33191fcdf) |  |
|  | MQTT 5.0, chapter 3.2.2.3.14 Server Keep Alive. [More...](#af21ff08751c63f17423500c33191fcdf) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [maximum\_qos](#a9c400f66c3a7eade5df879b328f4cb42) |  |
|  | MQTT 5.0, chapter 3.2.2.3.4 Maximum QoS. [More...](#a9c400f66c3a7eade5df879b328f4cb42) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [retain\_available](#af0810d9762a46f0ac7376becb631a9f7) |  |
|  | MQTT 5.0, chapter 3.2.2.3.5 Retain Available. [More...](#af0810d9762a46f0ac7376becb631a9f7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [wildcard\_sub\_available](#a1802487e00937da8e4261083b7229219) |  |
|  | MQTT 5.0, chapter 3.2.2.3.11 Wildcard Subscription Available. [More...](#a1802487e00937da8e4261083b7229219) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [subscription\_ids\_available](#ac3815c5ecaaeb8cea860ccd75f1d460a) |  |
|  | MQTT 5.0, chapter 3.2.2.3.12 Subscription Identifiers Available. [More...](#ac3815c5ecaaeb8cea860ccd75f1d460a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [shared\_sub\_available](#a3a21965017d0e9d15ed046eb0cfb461f) |  |
|  | MQTT 5.0, chapter 3.2.2.3.13 Shared Subscription Available. [More...](#a3a21965017d0e9d15ed046eb0cfb461f) |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_session\_expiry\_interval](#ae2c5b667e0e050611791160c8b7755ef) |  |
|  | Session Expiry Interval property was present. [More...](#ae2c5b667e0e050611791160c8b7755ef) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_receive\_maximum](#a1c37aaf9f6cde9f251b79af7144a099e) |  |
|  | Receive Maximum property was present. [More...](#a1c37aaf9f6cde9f251b79af7144a099e) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_maximum\_qos](#a0f02175c92a22ad05f370dd944ad6b1a) |  |
|  | Maximum QoS property was present. [More...](#a0f02175c92a22ad05f370dd944ad6b1a) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_retain\_available](#a7df963cce8b5ba99efe9888f742fad4f) |  |
|  | Retain Available property was present. [More...](#a7df963cce8b5ba99efe9888f742fad4f) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_maximum\_packet\_size](#a80932b53f13d5cb5c299f384c176e1af) |  |
|  | Maximum Packet Size property was present. [More...](#a80932b53f13d5cb5c299f384c176e1af) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_assigned\_client\_id](#af2655b3164805704e68d8ed69621a168) |  |
|  | Assigned Client Identifier property was present. [More...](#af2655b3164805704e68d8ed69621a168) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_topic\_alias\_maximum](#ac3f6a6b22fcf1ed55dc46d4b9b2079e6) |  |
|  | Topic Alias Maximum property was present. [More...](#ac3f6a6b22fcf1ed55dc46d4b9b2079e6) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_reason\_string](#a4f8092dc562fe27396c21e1329e19262) |  |
|  | Reason String property was present. [More...](#a4f8092dc562fe27396c21e1329e19262) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_user\_prop](#a4d1b50d148189053879ec80aa2688a2b) |  |
|  | User Property property was present. [More...](#a4d1b50d148189053879ec80aa2688a2b) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_wildcard\_sub\_available](#a3a6f8b9f79f81c34bda7aca99fa0682f) |  |
|  | Wildcard Subscription Available property was present. [More...](#a3a6f8b9f79f81c34bda7aca99fa0682f) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_subscription\_ids\_available](#a43ada81fd7746aab783a0d1cb4d4d645) |  |
|  | Subscription Identifiers Available property was present. [More...](#a43ada81fd7746aab783a0d1cb4d4d645) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_shared\_sub\_available](#a78dad1593aaa64c27263cafc61791a03) |  |
|  | Shared Subscription Available property was present. [More...](#a78dad1593aaa64c27263cafc61791a03) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_server\_keep\_alive](#a0d11efb926df6a0d65e879fee878bda0) |  |
|  | Server Keep Alive property was present. [More...](#a0d11efb926df6a0d65e879fee878bda0) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_response\_information](#a0f03ee47ace97ccaa841df5353e49f26) |  |
|  | Response Information property was present. [More...](#a0f03ee47ace97ccaa841df5353e49f26) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_server\_reference](#a351717d25bf8bc2d915506b5bc354214) |  |
|  | Server Reference property was present. [More...](#a351717d25bf8bc2d915506b5bc354214) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_auth\_method](#a7134eddbb0d497c6cfe85b6fcfc9efa1) |  |
|  | Authentication Method property was present. [More...](#a7134eddbb0d497c6cfe85b6fcfc9efa1) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [has\_auth\_data](#a6d7423e5c7234e97f79db2dd9e592d85) |  |
|  | Authentication Data property was present. [More...](#a6d7423e5c7234e97f79db2dd9e592d85) |
| }   [rx](#a3a7a8a6dbef8d5026717b98b4e949c4e) |
|  | Flags indicating whether given property was present in received packet. [More...](#a3a7a8a6dbef8d5026717b98b4e949c4e) |
| } | [prop](#a54ae953abeec2d31e7c82869302b492e) |

## Detailed Description

Parameters for a connection acknowledgment (CONNACK).

## Field Documentation

## [◆ ](#a7f275e22d6cdf808b1f0a19c3f78f517)assigned\_client\_id

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_connack\_param::assigned\_client\_id |
| --- |

MQTT 5.0, chapter 3.2.2.3.7 Assigned Client Identifier.

## [◆ ](#ad45d67943848406b290fee98e5d4d3ba)auth\_data

| struct [mqtt\_binstr](structmqtt__binstr.md) mqtt\_connack\_param::auth\_data |
| --- |

MQTT 5.0, chapter 3.2.2.3.18 Authentication Data.

## [◆ ](#abbd4490c94846009f79c741e3067c743)auth\_method

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_connack\_param::auth\_method |
| --- |

MQTT 5.0, chapter 3.2.2.3.17 Authentication Method.

## [◆ ](#af2655b3164805704e68d8ed69621a168)has\_assigned\_client\_id

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_assigned\_client\_id |
| --- |

Assigned Client Identifier property was present.

## [◆ ](#a6d7423e5c7234e97f79db2dd9e592d85)has\_auth\_data

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_auth\_data |
| --- |

Authentication Data property was present.

## [◆ ](#a7134eddbb0d497c6cfe85b6fcfc9efa1)has\_auth\_method

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_auth\_method |
| --- |

Authentication Method property was present.

## [◆ ](#a80932b53f13d5cb5c299f384c176e1af)has\_maximum\_packet\_size

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_maximum\_packet\_size |
| --- |

Maximum Packet Size property was present.

## [◆ ](#a0f02175c92a22ad05f370dd944ad6b1a)has\_maximum\_qos

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_maximum\_qos |
| --- |

Maximum QoS property was present.

## [◆ ](#a4f8092dc562fe27396c21e1329e19262)has\_reason\_string

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_reason\_string |
| --- |

Reason String property was present.

## [◆ ](#a1c37aaf9f6cde9f251b79af7144a099e)has\_receive\_maximum

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_receive\_maximum |
| --- |

Receive Maximum property was present.

## [◆ ](#a0f03ee47ace97ccaa841df5353e49f26)has\_response\_information

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_response\_information |
| --- |

Response Information property was present.

## [◆ ](#a7df963cce8b5ba99efe9888f742fad4f)has\_retain\_available

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_retain\_available |
| --- |

Retain Available property was present.

## [◆ ](#a0d11efb926df6a0d65e879fee878bda0)has\_server\_keep\_alive

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_server\_keep\_alive |
| --- |

Server Keep Alive property was present.

## [◆ ](#a351717d25bf8bc2d915506b5bc354214)has\_server\_reference

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_server\_reference |
| --- |

Server Reference property was present.

## [◆ ](#ae2c5b667e0e050611791160c8b7755ef)has\_session\_expiry\_interval

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_session\_expiry\_interval |
| --- |

Session Expiry Interval property was present.

## [◆ ](#a78dad1593aaa64c27263cafc61791a03)has\_shared\_sub\_available

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_shared\_sub\_available |
| --- |

Shared Subscription Available property was present.

## [◆ ](#a43ada81fd7746aab783a0d1cb4d4d645)has\_subscription\_ids\_available

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_subscription\_ids\_available |
| --- |

Subscription Identifiers Available property was present.

## [◆ ](#ac3f6a6b22fcf1ed55dc46d4b9b2079e6)has\_topic\_alias\_maximum

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_topic\_alias\_maximum |
| --- |

Topic Alias Maximum property was present.

## [◆ ](#a4d1b50d148189053879ec80aa2688a2b)has\_user\_prop

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_user\_prop |
| --- |

User Property property was present.

## [◆ ](#a3a6f8b9f79f81c34bda7aca99fa0682f)has\_wildcard\_sub\_available

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_connack\_param::has\_wildcard\_sub\_available |
| --- |

Wildcard Subscription Available property was present.

## [◆ ](#a8e5cab6b3479fc9e902feb622008386a)maximum\_packet\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_connack\_param::maximum\_packet\_size |
| --- |

MQTT 5.0, chapter 3.2.2.3.6 Maximum Packet Size.

## [◆ ](#a9c400f66c3a7eade5df879b328f4cb42)maximum\_qos

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_connack\_param::maximum\_qos |
| --- |

MQTT 5.0, chapter 3.2.2.3.4 Maximum QoS.

## [◆ ](#a54ae953abeec2d31e7c82869302b492e)[struct]

| struct { ... } mqtt\_connack\_param::prop |
| --- |

## [◆ ](#a5fbdc09eff6fef2f06a98c8f9faf0a03)reason\_string

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_connack\_param::reason\_string |
| --- |

MQTT 5.0, chapter 3.2.2.3.9 Reason String.

## [◆ ](#a9eecd31595fa1332a1cf4b661cedeae2)receive\_maximum

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_connack\_param::receive\_maximum |
| --- |

MQTT 5.0, chapter 3.3.2.3.3 Receive Maximum.

## [◆ ](#a1314e5735f128b905bd3d78beaee956e)response\_information

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_connack\_param::response\_information |
| --- |

MQTT 5.0, chapter 3.2.2.3.15 Response Information.

## [◆ ](#af0810d9762a46f0ac7376becb631a9f7)retain\_available

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_connack\_param::retain\_available |
| --- |

MQTT 5.0, chapter 3.2.2.3.5 Retain Available.

## [◆ ](#aae7a54dd6f62887b618f652f260ed6bd)return\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_connack\_param::return\_code |
| --- |

The appropriate non-zero Connect return code indicates if the Server is unable to process a connection request for some reason.

MQTT 3.1 - Return codes specified in [mqtt\_conn\_return\_code](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618 "mqtt_conn_return_code") MQTT 5.0 - Reason codes specified in [mqtt\_connack\_reason\_code](group__mqtt__socket.md#gae4c3fb5313addb72961ff578113d183a "mqtt_connack_reason_code")

## [◆ ](#a3a7a8a6dbef8d5026717b98b4e949c4e)[struct]

| struct { ... } mqtt\_connack\_param::rx |
| --- |

Flags indicating whether given property was present in received packet.

## [◆ ](#af21ff08751c63f17423500c33191fcdf)server\_keep\_alive

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_connack\_param::server\_keep\_alive |
| --- |

MQTT 5.0, chapter 3.2.2.3.14 Server Keep Alive.

## [◆ ](#a0426044dfe84d5160d1116018265eda3)server\_reference

| struct [mqtt\_utf8](structmqtt__utf8.md) mqtt\_connack\_param::server\_reference |
| --- |

MQTT 5.0, chapter 3.2.2.3.16 Server Reference.

## [◆ ](#a7e47864579e36ea469d198ceb9cdd3f4)session\_expiry\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_connack\_param::session\_expiry\_interval |
| --- |

MQTT 5.0, chapter 3.2.2.3.2 Session Expiry Interval.

## [◆ ](#ab123a8236804082667ad93ddd7e40e7a)session\_present\_flag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_connack\_param::session\_present\_flag |
| --- |

The Session Present flag enables a Client to establish whether the Client and Server have a consistent view about whether there is already stored Session state.

## [◆ ](#a3a21965017d0e9d15ed046eb0cfb461f)shared\_sub\_available

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_connack\_param::shared\_sub\_available |
| --- |

MQTT 5.0, chapter 3.2.2.3.13 Shared Subscription Available.

## [◆ ](#ac3815c5ecaaeb8cea860ccd75f1d460a)subscription\_ids\_available

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_connack\_param::subscription\_ids\_available |
| --- |

MQTT 5.0, chapter 3.2.2.3.12 Subscription Identifiers Available.

## [◆ ](#a09cdb8430a3ced98055b564716201bf1)topic\_alias\_maximum

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_connack\_param::topic\_alias\_maximum |
| --- |

MQTT 5.0, chapter 3.2.2.3.8 Topic Alias Maximum.

## [◆ ](#a29eed1a34902519380aa59757bde501c)user\_prop

| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) mqtt\_connack\_param::user\_prop[CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |
| --- |

MQTT 5.0, chapter 3.2.2.3.10 User Property.

## [◆ ](#a1802487e00937da8e4261083b7229219)wildcard\_sub\_available

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_connack\_param::wildcard\_sub\_available |
| --- |

MQTT 5.0, chapter 3.2.2.3.11 Wildcard Subscription Available.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_connack\_param](structmqtt__connack__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
