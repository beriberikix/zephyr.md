---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcoap__block__context.html
original_path: doxygen/html/structcoap__block__context.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_block\_context Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

Represents the current state of a block-wise transaction.
[More...](#details)

`#include <[coap.h](coap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [total\_size](#a27db79dc3a2af6dd9f41e3008dcde87a) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [current](#a474f54e2a29d41b9d449f8574e747067) |
| enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) | [block\_size](#a27eb897fa2d455eb79220f1654509da3) |

## Detailed Description

Represents the current state of a block-wise transaction.

## Field Documentation

## [◆ ](#a27eb897fa2d455eb79220f1654509da3)block\_size

| enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) coap\_block\_context::block\_size |
| --- |

## [◆ ](#a474f54e2a29d41b9d449f8574e747067)current

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) coap\_block\_context::current |
| --- |

## [◆ ](#a27db79dc3a2af6dd9f41e3008dcde87a)total\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) coap\_block\_context::total\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap.h](coap_8h_source.md)

- [coap\_block\_context](structcoap__block__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
