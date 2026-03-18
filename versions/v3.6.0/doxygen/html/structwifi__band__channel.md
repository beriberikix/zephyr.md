---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structwifi__band__channel.html
original_path: doxygen/html/structwifi__band__channel.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_band\_channel Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi structure to uniquely identify a band-channel pair.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [band](#a4a932599429f37231f76c3064ec5efb3) |
|  | Frequency band. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel](#acd0dd7366de3650124dad7232a58ade0) |
|  | Channel. |

## Detailed Description

Wi-Fi structure to uniquely identify a band-channel pair.

## Field Documentation

## [◆ ](#a4a932599429f37231f76c3064ec5efb3)band

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_band\_channel::band |
| --- |

Frequency band.

## [◆ ](#acd0dd7366de3650124dad7232a58ade0)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_band\_channel::channel |
| --- |

Channel.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_band\_channel](structwifi__band__channel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
