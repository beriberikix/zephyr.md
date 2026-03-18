---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structccs811__configver__type.html
original_path: doxygen/html/structccs811__configver__type.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccs811\_configver\_type Struct Reference

Get information about static CCS811 state.
[More...](#details)

`#include <[ccs811.h](ccs811_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fw\_boot\_version](#a78d15d9b7695cc7dd4251cecd573a18a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fw\_app\_version](#add87f032fef47ad3c4b6415a9aeb829d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [hw\_version](#ad76906d24bd14e63dd7a4c1628fd81cc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode](#aa8dad67bbdd286a54749e421967d228d) |

## Detailed Description

Get information about static CCS811 state.

This includes the configured operating mode as well as hardware and firmware versions.

## Field Documentation

## [◆ ](#add87f032fef47ad3c4b6415a9aeb829d)fw\_app\_version

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccs811\_configver\_type::fw\_app\_version |
| --- |

## [◆ ](#a78d15d9b7695cc7dd4251cecd573a18a)fw\_boot\_version

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccs811\_configver\_type::fw\_boot\_version |
| --- |

## [◆ ](#ad76906d24bd14e63dd7a4c1628fd81cc)hw\_version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccs811\_configver\_type::hw\_version |
| --- |

## [◆ ](#aa8dad67bbdd286a54749e421967d228d)mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccs811\_configver\_type::mode |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/sensor/[ccs811.h](ccs811_8h_source.md)

- [ccs811\_configver\_type](structccs811__configver__type.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
