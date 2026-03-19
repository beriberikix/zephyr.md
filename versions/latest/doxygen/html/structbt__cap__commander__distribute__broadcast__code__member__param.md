---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__commander__distribute__broadcast__code__member__param.html
original_path: doxygen/html/structbt__cap__commander__distribute__broadcast__code__member__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Member parameters for distributing broadcast code.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) | [member](#acd5d185c590ea9a64faebd354a3d5d4a) |
|  | Coordinated or ad-hoc set member. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [src\_id](#ad240bb7e1e9ad5c40eb1a031a6fbc2fe) |
|  | Source ID of the receive state. |

## Detailed Description

Member parameters for distributing broadcast code.

## Field Documentation

## [◆ ](#acd5d185c590ea9a64faebd354a3d5d4a)member

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param::member |
| --- |

Coordinated or ad-hoc set member.

## [◆ ](#ad240bb7e1e9ad5c40eb1a031a6fbc2fe)src\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param::src\_id |
| --- |

Source ID of the receive state.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param](structbt__cap__commander__distribute__broadcast__code__member__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
