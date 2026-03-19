---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmbox__msg.html
original_path: doxygen/html/structmbox__msg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mbox\_msg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MBOX Interface](group__mbox__interface.md)

Message struct (to hold data and its size).
[More...](#details)

`#include <[mbox.h](drivers_2mbox_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const void \* | [data](#aa9b02c7a3b1620ca2c6ffa42528cfe0c) |
|  | Pointer to the data sent in the message. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a9870d0667d97e4d4ab9ba985b75e1dc4) |
|  | Size of the data. |

## Detailed Description

Message struct (to hold data and its size).

## Field Documentation

## [◆ ](#aa9b02c7a3b1620ca2c6ffa42528cfe0c)data

| const void\* mbox\_msg::data |
| --- |

Pointer to the data sent in the message.

## [◆ ](#a9870d0667d97e4d4ab9ba985b75e1dc4)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mbox\_msg::size |
| --- |

Size of the data.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mbox.h](drivers_2mbox_8h_source.md)

- [mbox\_msg](structmbox__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
