---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmqtt__topic__alias.html
original_path: doxygen/html/structmqtt__topic__alias.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_topic\_alias Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Abstracts aliased topic.
[More...](#details)

`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [topic\_buf](#af056af89763a7d39f513759dd1f7e8a7) [CONFIG\_MQTT\_TOPIC\_ALIAS\_STRING\_MAX] |
|  | UTF-8 encoded topic name. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [topic\_size](#aed7c3e3306dd3bf97073ca6b7f9c4902) |
|  | Topic name size. |

## Detailed Description

Abstracts aliased topic.

## Field Documentation

## [◆ ](#af056af89763a7d39f513759dd1f7e8a7)topic\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mqtt\_topic\_alias::topic\_buf[CONFIG\_MQTT\_TOPIC\_ALIAS\_STRING\_MAX] |
| --- |

UTF-8 encoded topic name.

## [◆ ](#aed7c3e3306dd3bf97073ca6b7f9c4902)topic\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mqtt\_topic\_alias::topic\_size |
| --- |

Topic name size.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_topic\_alias](structmqtt__topic__alias.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
