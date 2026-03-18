---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmipi__dbi__config.html
original_path: doxygen/html/structmipi__dbi__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dbi\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MIPI-DBI driver APIs](group__mipi__dbi__interface.md)

MIPI DBI controller configuration.
[More...](#details)

`#include <[mipi_dbi.h](mipi__dbi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode](#a2eafaaa6cda8f17f4b518c007bb3a7c3) |
|  | MIPI DBI mode (SPI 3 wire or 4 wire). |
| struct [spi\_config](structspi__config.md) | [config](#a50d0893838455e3b8faa29d6459bc9c8) |
|  | SPI configuration. |

## Detailed Description

MIPI DBI controller configuration.

Configuration for MIPI DBI controller write

## Field Documentation

## [◆ ](#a50d0893838455e3b8faa29d6459bc9c8)config

| struct [spi\_config](structspi__config.md) mipi\_dbi\_config::config |
| --- |

SPI configuration.

## [◆ ](#a2eafaaa6cda8f17f4b518c007bb3a7c3)mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mipi\_dbi\_config::mode |
| --- |

MIPI DBI mode (SPI 3 wire or 4 wire).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mipi\_dbi.h](mipi__dbi_8h_source.md)

- [mipi\_dbi\_config](structmipi__dbi__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
