---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structpeci__msg.html
original_path: doxygen/html/structpeci__msg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

peci\_msg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [PECI Interface](group__peci__interface.md)

PECI transaction packet format.
[More...](#details)

`#include <[peci.h](peci_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#aa4d6785fc79059dc7e8574010bc29e4c) |
|  | Client address. |
| enum [peci\_command\_code](group__peci__interface.md#gacd243f64973f7bdcc8c999dc14ed2bd6) | [cmd\_code](#a10b270f4669c85a85c6e8f1bef7671e8) |
|  | Command code. |
| struct [peci\_buf](structpeci__buf.md) | [tx\_buffer](#a22e435e110d261b8ecd5180d118ffd2d) |
|  | Pointer to buffer of write data. |
| struct [peci\_buf](structpeci__buf.md) | [rx\_buffer](#abea62e39ca0ac59fca47c2f08a72f1e8) |
|  | Pointer to buffer of read data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a0449f151c62e672553d7d60480e1b995) |
|  | PECI msg flags. |

## Detailed Description

PECI transaction packet format.

## Field Documentation

## [◆ ](#aa4d6785fc79059dc7e8574010bc29e4c)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) peci\_msg::addr |
| --- |

Client address.

## [◆ ](#a10b270f4669c85a85c6e8f1bef7671e8)cmd\_code

| enum [peci\_command\_code](group__peci__interface.md#gacd243f64973f7bdcc8c999dc14ed2bd6) peci\_msg::cmd\_code |
| --- |

Command code.

## [◆ ](#a0449f151c62e672553d7d60480e1b995)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) peci\_msg::flags |
| --- |

PECI msg flags.

## [◆ ](#abea62e39ca0ac59fca47c2f08a72f1e8)rx\_buffer

| struct [peci\_buf](structpeci__buf.md) peci\_msg::rx\_buffer |
| --- |

Pointer to buffer of read data.

## [◆ ](#a22e435e110d261b8ecd5180d118ffd2d)tx\_buffer

| struct [peci\_buf](structpeci__buf.md) peci\_msg::tx\_buffer |
| --- |

Pointer to buffer of write data.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[peci.h](peci_8h_source.md)

- [peci\_msg](structpeci__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
