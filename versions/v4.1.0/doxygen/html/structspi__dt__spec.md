---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structspi__dt__spec.html
original_path: doxygen/html/structspi__dt__spec.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SPI Interface](group__spi__interface.md)

Complete SPI DT information.
[More...](#details)

`#include <[spi.h](drivers_2spi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [bus](#a37519633ae787ffaa1026e6867d7007a) |
|  | SPI bus. |
| struct [spi\_config](structspi__config.md) | [config](#a88372c17ede2e9dfb0c09c49abebf87e) |
|  | Slave specific configuration. |

## Detailed Description

Complete SPI DT information.

## Field Documentation

## [◆ ](#a37519633ae787ffaa1026e6867d7007a)bus

| const struct [device](structdevice.md)\* spi\_dt\_spec::bus |
| --- |

SPI bus.

## [◆ ](#a88372c17ede2e9dfb0c09c49abebf87e)config

| struct [spi\_config](structspi__config.md) spi\_dt\_spec::config |
| --- |

Slave specific configuration.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[spi.h](drivers_2spi_8h_source.md)

- [spi\_dt\_spec](structspi__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
