---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcan__device__state.html
original_path: doxygen/html/structcan__device__state.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_device\_state Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [CAN Interface](group__can__interface.md)

CAN specific device state which allows for CAN device class specific additions.
[More...](#details)

`#include <[can.h](drivers_2can_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [device\_state](structdevice__state.md) | [devstate](#a28061ff1193176dd01b7bb9a88f402ec) |
|  | Common device state. |
| struct stats\_can | [stats](#ae05c85eae4f6bee075ffdc4f0ab56f47) |
|  | CAN device statistics. |

## Detailed Description

CAN specific device state which allows for CAN device class specific additions.

## Field Documentation

## [◆ ](#a28061ff1193176dd01b7bb9a88f402ec)devstate

| struct [device\_state](structdevice__state.md) can\_device\_state::devstate |
| --- |

Common device state.

## [◆ ](#ae05c85eae4f6bee075ffdc4f0ab56f47)stats

| struct stats\_can can\_device\_state::stats |
| --- |

CAN device statistics.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[can.h](drivers_2can_8h_source.md)

- [can\_device\_state](structcan__device__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
