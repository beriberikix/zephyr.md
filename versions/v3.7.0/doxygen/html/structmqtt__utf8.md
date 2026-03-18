---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmqtt__utf8.html
original_path: doxygen/html/structmqtt__utf8.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_utf8 Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

Abstracts UTF-8 encoded strings.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [utf8](#a69a949e3c9cb1794f8d28091601eba16) |
|  | Pointer to UTF-8 string. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [size](#a2376f943335326dae74c798141326b70) |
|  | Size of UTF string, in bytes. |

## Detailed Description

Abstracts UTF-8 encoded strings.

## Field Documentation

## [◆ ](#a2376f943335326dae74c798141326b70)size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_utf8::size |
| --- |

Size of UTF string, in bytes.

## [◆ ](#a69a949e3c9cb1794f8d28091601eba16)utf8

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* mqtt\_utf8::utf8 |
| --- |

Pointer to UTF-8 string.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_utf8](structmqtt__utf8.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
