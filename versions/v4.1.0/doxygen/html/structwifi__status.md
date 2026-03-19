---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structwifi__status.html
original_path: doxygen/html/structwifi__status.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_status Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Generic Wi-Fi status for commands and events.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| int   [status](#aa1dbff8154400f8353693d387977008b) |  |
|  | Status value. [More...](#aa1dbff8154400f8353693d387977008b) |
| enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8)   [conn\_status](#a8f885e78366d0499e4ba8e15bef275ac) |  |
|  | Connection status. [More...](#a8f885e78366d0499e4ba8e15bef275ac) |
| enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a)   [disconn\_reason](#aa04b5033d93274badd27f702af9830bc) |  |
|  | Disconnection reason status. [More...](#aa04b5033d93274badd27f702af9830bc) |
| enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884)   [ap\_status](#a02f0fcc7ef57661ca95d0c99f045aef1) |  |
|  | Access point status. [More...](#a02f0fcc7ef57661ca95d0c99f045aef1) |
| }; |  |

## Detailed Description

Generic Wi-Fi status for commands and events.

## Field Documentation

## [◆ ](#a09c151ea393c9c1fa2cc9f5f75eab66a)[union]

| union { ... } [wifi\_status](structwifi__status.md) |
| --- |

## [◆ ](#a02f0fcc7ef57661ca95d0c99f045aef1)ap\_status

| enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) wifi\_status::ap\_status |
| --- |

Access point status.

## [◆ ](#a8f885e78366d0499e4ba8e15bef275ac)conn\_status

| enum [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) wifi\_status::conn\_status |
| --- |

Connection status.

## [◆ ](#aa04b5033d93274badd27f702af9830bc)disconn\_reason

| enum [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) wifi\_status::disconn\_reason |
| --- |

Disconnection reason status.

## [◆ ](#aa1dbff8154400f8353693d387977008b)status

| int wifi\_status::status |
| --- |

Status value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_status](structwifi__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
