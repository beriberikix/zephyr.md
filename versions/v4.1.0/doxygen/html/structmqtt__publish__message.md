---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmqtt__publish__message.html
original_path: doxygen/html/structmqtt__publish__message.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_publish\_message Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Parameters for a publish message.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mqtt\_topic](structmqtt__topic.md) | [topic](#acf5dba605db61efe68ec29337eea95e9) |
|  | Topic on which data was published. |
| struct [mqtt\_binstr](structmqtt__binstr.md) | [payload](#a6cfed92c8f8fb319d3cbf40b956cb94d) |
|  | Payload on the topic published. |

## Detailed Description

Parameters for a publish message.

## Field Documentation

## [◆ ](#a6cfed92c8f8fb319d3cbf40b956cb94d)payload

| struct [mqtt\_binstr](structmqtt__binstr.md) mqtt\_publish\_message::payload |
| --- |

Payload on the topic published.

## [◆ ](#acf5dba605db61efe68ec29337eea95e9)topic

| struct [mqtt\_topic](structmqtt__topic.md) mqtt\_publish\_message::topic |
| --- |

Topic on which data was published.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_publish\_message](structmqtt__publish__message.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
