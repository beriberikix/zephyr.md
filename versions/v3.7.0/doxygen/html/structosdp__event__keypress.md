---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structosdp__event__keypress.html
original_path: doxygen/html/structosdp__event__keypress.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_event\_keypress Struct Reference

OSDP Event Keypad.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [reader\_no](#ae6964a42e982021ef44372dca6af1166) |
|  | Reader number. |
| int | [length](#a41460942a34a488c78712bfba164f865) |
|  | Length of keypress data in bytes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a88ac427349340142426e69fb99242cb4) [64] |
|  | Keypress data of *length* bytes. |

## Detailed Description

OSDP Event Keypad.

## Field Documentation

## [◆ ](#a88ac427349340142426e69fb99242cb4)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_event\_keypress::data[64] |
| --- |

Keypress data of *length* bytes.

## [◆ ](#a41460942a34a488c78712bfba164f865)length

| int osdp\_event\_keypress::length |
| --- |

Length of keypress data in bytes.

## [◆ ](#ae6964a42e982021ef44372dca6af1166)reader\_no

| int osdp\_event\_keypress::reader\_no |
| --- |

Reader number.

In context of readers attached to current PD, this number indicated this number. This is not supported by LibOSDP.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_event\_keypress](structosdp__event__keypress.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
