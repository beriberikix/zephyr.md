---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmqtt__sn__client.html
original_path: doxygen/html/structmqtt__sn__client.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_sn\_client Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT-SN Client library](group__mqtt__sn__socket.md)

Structure describing an MQTT-SN client.
[More...](#details)

`#include <[mqtt_sn.h](mqtt__sn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_sn\_data](structmqtt__sn__data.md) | [client\_id](#a9cbf86052061b55a93356346cae75e8b) |
|  | 1-23 character unique client ID |
| struct [mqtt\_sn\_data](structmqtt__sn__data.md) | [will\_topic](#af70196b9800123e2f9c36362cfb8b6be) |
|  | Topic for Will message. |
| struct [mqtt\_sn\_data](structmqtt__sn__data.md) | [will\_msg](#a9d2397f5ff59a51630f5b82f94c92327) |
|  | Will message. |
| enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) | [will\_qos](#a42d76db9cbcc9770246241283bb65486) |
|  | Quality of Service for the Will message. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [will\_retain](#ad8f5b3b7815033cfecda7519ca657724) |
|  | Flag indicating if the will message should be retained by the broker. |
| struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \* | [transport](#aec0d4d3f436d7c7d40e2548d7c6575c1) |
|  | Underlying transport to be used by the client. |
| struct [net\_buf\_simple](structnet__buf__simple.md) | [tx](#a3802bd92a42e421a5d733c64b53473db) |
|  | Buffer for outgoing data. |
| struct [net\_buf\_simple](structnet__buf__simple.md) | [rx](#aec40ceeac5a4160b058ee6a7676ec68f) |
|  | Buffer for incoming data. |
| [mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a) | [evt\_cb](#ac2b8e9d7d4c246c5d5538922a1e9887b) |
|  | Event callback. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [next\_msg\_id](#a05b83c732ed9199dac0110cfb1e56563) |
|  | Message ID for the next message to be sent. |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [publish](#a32efbccbf7b1820ff5092896130e6b7e) |
|  | List of pending publish messages. |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [topic](#aa47e6426ca7e8434734377a85f586b84) |
|  | List of registered topics. |
| int | [state](#a02a38427caa60c51f85661efe58813f6) |
|  | Current state of the MQTT-SN client. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [last\_ping](#af400a2f993c27e0f25a4325daeacee28) |
|  | Timestamp of the last ping request. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ping\_retries](#a2be2f7d041f325dda14007864e03fb70) |
|  | Number of retries for failed ping attempts. |
| struct [k\_work\_delayable](structk__work__delayable.md) | [process\_work](#a65bb52c8a5ecbd81e743fdc7c213b43a) |
|  | Delayable work structure for processing MQTT-SN events. |

## Detailed Description

Structure describing an MQTT-SN client.

## Field Documentation

## [◆ ](#a9cbf86052061b55a93356346cae75e8b)client\_id

| struct [mqtt\_sn\_data](structmqtt__sn__data.md) mqtt\_sn\_client::client\_id |
| --- |

1-23 character unique client ID

## [◆ ](#ac2b8e9d7d4c246c5d5538922a1e9887b)evt\_cb

| [mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a) mqtt\_sn\_client::evt\_cb |
| --- |

Event callback.

## [◆ ](#af400a2f993c27e0f25a4325daeacee28)last\_ping

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) mqtt\_sn\_client::last\_ping |
| --- |

Timestamp of the last ping request.

## [◆ ](#a05b83c732ed9199dac0110cfb1e56563)next\_msg\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_sn\_client::next\_msg\_id |
| --- |

Message ID for the next message to be sent.

## [◆ ](#a2be2f7d041f325dda14007864e03fb70)ping\_retries

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_sn\_client::ping\_retries |
| --- |

Number of retries for failed ping attempts.

## [◆ ](#a65bb52c8a5ecbd81e743fdc7c213b43a)process\_work

| struct [k\_work\_delayable](structk__work__delayable.md) mqtt\_sn\_client::process\_work |
| --- |

Delayable work structure for processing MQTT-SN events.

## [◆ ](#a32efbccbf7b1820ff5092896130e6b7e)publish

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) mqtt\_sn\_client::publish |
| --- |

List of pending publish messages.

## [◆ ](#aec40ceeac5a4160b058ee6a7676ec68f)rx

| struct [net\_buf\_simple](structnet__buf__simple.md) mqtt\_sn\_client::rx |
| --- |

Buffer for incoming data.

## [◆ ](#a02a38427caa60c51f85661efe58813f6)state

| int mqtt\_sn\_client::state |
| --- |

Current state of the MQTT-SN client.

## [◆ ](#aa47e6426ca7e8434734377a85f586b84)topic

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) mqtt\_sn\_client::topic |
| --- |

List of registered topics.

## [◆ ](#aec0d4d3f436d7c7d40e2548d7c6575c1)transport

| struct [mqtt\_sn\_transport](structmqtt__sn__transport.md)\* mqtt\_sn\_client::transport |
| --- |

Underlying transport to be used by the client.

## [◆ ](#a3802bd92a42e421a5d733c64b53473db)tx

| struct [net\_buf\_simple](structnet__buf__simple.md) mqtt\_sn\_client::tx |
| --- |

Buffer for outgoing data.

## [◆ ](#a9d2397f5ff59a51630f5b82f94c92327)will\_msg

| struct [mqtt\_sn\_data](structmqtt__sn__data.md) mqtt\_sn\_client::will\_msg |
| --- |

Will message.

Must be initialized before connecting with will=true

## [◆ ](#a42d76db9cbcc9770246241283bb65486)will\_qos

| enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) mqtt\_sn\_client::will\_qos |
| --- |

Quality of Service for the Will message.

## [◆ ](#ad8f5b3b7815033cfecda7519ca657724)will\_retain

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mqtt\_sn\_client::will\_retain |
| --- |

Flag indicating if the will message should be retained by the broker.

## [◆ ](#af70196b9800123e2f9c36362cfb8b6be)will\_topic

| struct [mqtt\_sn\_data](structmqtt__sn__data.md) mqtt\_sn\_client::will\_topic |
| --- |

Topic for Will message.

Must be initialized before connecting with will=true

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt\_sn.h](mqtt__sn_8h_source.md)

- [mqtt\_sn\_client](structmqtt__sn__client.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
