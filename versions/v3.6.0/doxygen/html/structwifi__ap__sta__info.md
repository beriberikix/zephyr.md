---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structwifi__ap__sta__info.html
original_path: doxygen/html/structwifi__ap__sta__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_ap\_sta\_info Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

AP mode - connected STA details.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) | [link\_mode](#a7d8bd52340d4937a4b5b7d2c00662441) |
|  | Link mode, see enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62 "Wi-Fi link operating modes."). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mac](#a2a2fc109525e72ee7f18cced3b881107) [6] |
|  | MAC address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mac\_length](#a7f7c8b144bb3464af5213708591eefda) |
|  | MAC address length. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [twt\_capable](#a838c9a4288c9bc7e97afe2334c678f34) |
|  | is TWT capable ? |

## Detailed Description

AP mode - connected STA details.

## Field Documentation

## [◆ ](#a7d8bd52340d4937a4b5b7d2c00662441)link\_mode

| enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) wifi\_ap\_sta\_info::link\_mode |
| --- |

Link mode, see enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62 "Wi-Fi link operating modes.").

## [◆ ](#a2a2fc109525e72ee7f18cced3b881107)mac

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_ap\_sta\_info::mac[6] |
| --- |

MAC address.

## [◆ ](#a7f7c8b144bb3464af5213708591eefda)mac\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_ap\_sta\_info::mac\_length |
| --- |

MAC address length.

## [◆ ](#a838c9a4288c9bc7e97afe2334c678f34)twt\_capable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_ap\_sta\_info::twt\_capable |
| --- |

is TWT capable ?

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
