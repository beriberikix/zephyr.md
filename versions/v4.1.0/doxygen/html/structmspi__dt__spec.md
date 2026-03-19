---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmspi__dt__spec.html
original_path: doxygen/html/structmspi__dt__spec.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Configure API](group__mspi__configure__api.md)

MSPI DT information.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [bus](#ab21ff3d5959b78f5b5cdc7fcf70e8756) |
|  | MSPI bus. |
| struct [mspi\_cfg](structmspi__cfg.md) | [config](#aaedbcdc55394032e3af50ec7d2e8f439) |
|  | MSPI hardware specific configuration. |

## Detailed Description

MSPI DT information.

## Field Documentation

## [◆ ](#ab21ff3d5959b78f5b5cdc7fcf70e8756)bus

| const struct [device](structdevice.md)\* mspi\_dt\_spec::bus |
| --- |

MSPI bus.

## [◆ ](#aaedbcdc55394032e3af50ec7d2e8f439)config

| struct [mspi\_cfg](structmspi__cfg.md) mspi\_dt\_spec::config |
| --- |

MSPI hardware specific configuration.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_dt\_spec](structmspi__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
