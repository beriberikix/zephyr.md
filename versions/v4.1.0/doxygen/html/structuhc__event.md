---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structuhc__event.html
original_path: doxygen/html/structuhc__event.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uhc\_event Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [USB host controller driver API](group__uhc__api.md)

USB host controller event.
[More...](#details)

`#include <[uhc.h](uhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#acd04587fac14f9a8a91b75642f5b2e82) |
|  | slist node for the message queue |
| enum [uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb) | [type](#a30fddbbe0f15a16320fba3cb4fd81d84) |
|  | Event type. |
| union { |  |
| int   [status](#a5d7e1cc1bcb25e10f009ac3a8acd94b6) |  |
|  | Event status value, if any. [More...](#a5d7e1cc1bcb25e10f009ac3a8acd94b6) |
| struct [uhc\_transfer](structuhc__transfer.md) \*   [xfer](#a03f3cebee6edfaf620a98c198a70dbd0) |  |
|  | Pointer to request used only for UHC\_EVT\_EP\_REQUEST. [More...](#a03f3cebee6edfaf620a98c198a70dbd0) |
| }; |  |
| const struct [device](structdevice.md) \* | [dev](#a055be3fd47e16bc48498163be3e55d09) |
|  | Pointer to controller's device struct. |

## Detailed Description

USB host controller event.

Common structure for all events that originate from the UHC driver and are passed to higher layer using message queue and a callback ([uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9 "Callback to submit UHC event to higher layer.")) provided by higher layer during controller initialization (uhc\_init).

## Field Documentation

## [◆ ](#a2b9e097fbb376dc33de491e103d18e8d)[union]

| union { ... } [uhc\_event](structuhc__event.md) |
| --- |

## [◆ ](#a055be3fd47e16bc48498163be3e55d09)dev

| const struct [device](structdevice.md)\* uhc\_event::dev |
| --- |

Pointer to controller's device struct.

## [◆ ](#acd04587fac14f9a8a91b75642f5b2e82)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) uhc\_event::node |
| --- |

slist node for the message queue

## [◆ ](#a5d7e1cc1bcb25e10f009ac3a8acd94b6)status

| int uhc\_event::status |
| --- |

Event status value, if any.

## [◆ ](#a30fddbbe0f15a16320fba3cb4fd81d84)type

| enum [uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb) uhc\_event::type |
| --- |

Event type.

## [◆ ](#a03f3cebee6edfaf620a98c198a70dbd0)xfer

| struct [uhc\_transfer](structuhc__transfer.md)\* uhc\_event::xfer |
| --- |

Pointer to request used only for UHC\_EVT\_EP\_REQUEST.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[uhc.h](uhc_8h_source.md)

- [uhc\_event](structuhc__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
