---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__subscription__list.html
original_path: doxygen/html/structmqtt__subscription__list.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_subscription\_list Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for subscribe/unsubscribe message.
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_topic](structmqtt__topic.md) \* | [list](#ae9db5f602e3c649b1ccc180aef6c4b4e) |
|  | Array containing topics along with QoS for each. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [list\_count](#aa44e0af3526ee0424627bb24a90ea6b1) |
|  | Number of topics in the subscription list. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#a0667dcd4bd5eb5fe1b13b4df1bf2c26f) |
|  | Message id used to identify subscription request. |
| struct { |  |
| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md)   [user\_prop](#a9736f9d14db3097c2081e81e765a60ec) [CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |  |
|  | MQTT 5.0, chapter 3.8.2.1.3 / 3.10.2.1.2 User Property. [More...](#a9736f9d14db3097c2081e81e765a60ec) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [subscription\_identifier](#a314f91139b4a837b173a6a930c3bdc6b) |  |
|  | MQTT 5.0, chapter 3.8.2.1.2 Subscription Identifier. [More...](#a314f91139b4a837b173a6a930c3bdc6b) |
| } | [prop](#a97fefa83de8657d85b0f76013ca1f222) |
|  | MQTT 5.0 properties. |

## Detailed Description

Parameters for subscribe/unsubscribe message.

## Field Documentation

## [◆ ](#ae9db5f602e3c649b1ccc180aef6c4b4e)list

| struct [mqtt\_topic](structmqtt__topic.md)\* mqtt\_subscription\_list::list |
| --- |

Array containing topics along with QoS for each.

## [◆ ](#aa44e0af3526ee0424627bb24a90ea6b1)list\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_subscription\_list::list\_count |
| --- |

Number of topics in the subscription list.

## [◆ ](#a0667dcd4bd5eb5fe1b13b4df1bf2c26f)message\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_subscription\_list::message\_id |
| --- |

Message id used to identify subscription request.

## [◆ ](#a97fefa83de8657d85b0f76013ca1f222)[struct]

| struct { ... } mqtt\_subscription\_list::prop |
| --- |

MQTT 5.0 properties.

## [◆ ](#a314f91139b4a837b173a6a930c3bdc6b)subscription\_identifier

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_subscription\_list::subscription\_identifier |
| --- |

MQTT 5.0, chapter 3.8.2.1.2 Subscription Identifier.

Ignored for UNSUBSCRIBE requests.

## [◆ ](#a9736f9d14db3097c2081e81e765a60ec)user\_prop

| struct [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) mqtt\_subscription\_list::user\_prop[CONFIG\_MQTT\_USER\_PROPERTIES\_MAX] |
| --- |

MQTT 5.0, chapter 3.8.2.1.3 / 3.10.2.1.2 User Property.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_subscription\_list](structmqtt__subscription__list.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
