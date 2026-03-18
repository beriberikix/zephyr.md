---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structk__msgq__attrs.html
original_path: doxygen/html/structk__msgq__attrs.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_msgq\_attrs Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Message Queue APIs](group__msgq__apis.md)

Message Queue Attributes.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [msg\_size](#a7d1d72946bdd517c07da37493a89e30e) |
|  | Message Size. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_msgs](#ad0f5894ba0da840b91eb85015252e649) |
|  | Maximal number of messages. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [used\_msgs](#a00f936870442fa455117cbdd7821fac5) |
|  | Used messages. |

## Detailed Description

Message Queue Attributes.

## Field Documentation

## [◆ ](#ad0f5894ba0da840b91eb85015252e649)max\_msgs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_msgq\_attrs::max\_msgs |
| --- |

Maximal number of messages.

## [◆ ](#a7d1d72946bdd517c07da37493a89e30e)msg\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_msgq\_attrs::msg\_size |
| --- |

Message Size.

## [◆ ](#a00f936870442fa455117cbdd7821fac5)used\_msgs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_msgq\_attrs::used\_msgs |
| --- |

Used messages.

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_msgq\_attrs](structk__msgq__attrs.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
