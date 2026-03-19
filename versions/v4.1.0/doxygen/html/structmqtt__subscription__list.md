---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmqtt__subscription__list.html
original_path: doxygen/html/structmqtt__subscription__list.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_subscription\_list Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

List of topics in a subscription request.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_topic](structmqtt__topic.md) \* | [list](#ae9db5f602e3c649b1ccc180aef6c4b4e) |
|  | Array containing topics along with QoS for each. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [list\_count](#aa44e0af3526ee0424627bb24a90ea6b1) |
|  | Number of topics in the subscription list. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [message\_id](#a0667dcd4bd5eb5fe1b13b4df1bf2c26f) |
|  | Message id used to identify subscription request. |

## Detailed Description

List of topics in a subscription request.

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

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_subscription\_list](structmqtt__subscription__list.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
