---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmbox__channel.html
original_path: doxygen/html/structmbox__channel.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mbox\_channel Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MBOX Interface](group__mbox__interface.md)

Provides a type to hold an MBOX channel.
[More...](#details)

`#include <[mbox.h](drivers_2mbox_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#a6fe03cc3209c832b295a2f7ff2ba7c63) |
|  | MBOX device pointer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#a0b8104fdbeca9badb76d7779b6e6f8e4) |
|  | Channel ID. |

## Detailed Description

Provides a type to hold an MBOX channel.

Struct type to hold an MBOX device pointer and the channel ID.

## Field Documentation

## [◆ ](#a6fe03cc3209c832b295a2f7ff2ba7c63)dev

| const struct [device](structdevice.md)\* mbox\_channel::dev |
| --- |

MBOX device pointer.

## [◆ ](#a0b8104fdbeca9badb76d7779b6e6f8e4)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mbox\_channel::id |
| --- |

Channel ID.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mbox.h](drivers_2mbox_8h_source.md)

- [mbox\_channel](structmbox__channel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
