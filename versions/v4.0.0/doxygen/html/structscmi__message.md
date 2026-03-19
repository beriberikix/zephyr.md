---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structscmi__message.html
original_path: doxygen/html/structscmi__message.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

scmi\_message Struct Reference

SCMI message structure.
[More...](#details)

`#include <[protocol.h](protocol_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hdr](#a4b329136651a527d51310af82dc24795) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#aad4f7713d97765414e21a4cb6ed4b01f) |
| void \* | [content](#ae868ec173129a6f81c895279e95bb52d) |

## Detailed Description

SCMI message structure.

## Field Documentation

## [◆ ](#ae868ec173129a6f81c895279e95bb52d)content

| void\* scmi\_message::content |
| --- |

## [◆ ](#a4b329136651a527d51310af82dc24795)hdr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_message::hdr |
| --- |

## [◆ ](#aad4f7713d97765414e21a4cb6ed4b01f)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) scmi\_message::len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/scmi/[protocol.h](protocol_8h_source.md)

- [scmi\_message](structscmi__message.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
