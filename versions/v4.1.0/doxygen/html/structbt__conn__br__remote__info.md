---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__conn__br__remote__info.html
original_path: doxygen/html/structbt__conn__br__remote__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_br\_remote\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

BR/EDR Connection Remote Info structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [features](#afa19f7db400bb0de234e8cda61f3deaf) |
|  | Remote feature set (pages of bitmasks). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_pages](#a798c179c803e709182a1b0c3594f4a0a) |
|  | Number of pages in the remote feature set. |

## Detailed Description

BR/EDR Connection Remote Info structure.

## Field Documentation

## [◆ ](#afa19f7db400bb0de234e8cda61f3deaf)features

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_conn\_br\_remote\_info::features |
| --- |

Remote feature set (pages of bitmasks).

## [◆ ](#a798c179c803e709182a1b0c3594f4a0a)num\_pages

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_br\_remote\_info::num\_pages |
| --- |

Number of pages in the remote feature set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
