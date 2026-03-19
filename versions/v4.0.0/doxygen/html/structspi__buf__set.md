---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structspi__buf__set.html
original_path: doxygen/html/structspi__buf__set.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_buf\_set Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SPI Interface](group__spi__interface.md)

SPI buffer array structure.
[More...](#details)

`#include <[spi.h](drivers_2spi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [spi\_buf](structspi__buf.md) \* | [buffers](#a2b88917ca29487b2d0b5b63d2083db67) |
|  | Pointer to an array of [spi\_buf](structspi__buf.md "SPI buffer structure."), or NULL. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#abc7c37cffebb7873aaba2e524c9a23dc) |
|  | Length of the array (number of buffers) pointed by *buffers*. |

## Detailed Description

SPI buffer array structure.

## Field Documentation

## [◆ ](#a2b88917ca29487b2d0b5b63d2083db67)buffers

| const struct [spi\_buf](structspi__buf.md)\* spi\_buf\_set::buffers |
| --- |

Pointer to an array of [spi\_buf](structspi__buf.md "SPI buffer structure."), or NULL.

## [◆ ](#abc7c37cffebb7873aaba2e524c9a23dc)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) spi\_buf\_set::count |
| --- |

Length of the array (number of buffers) pointed by *buffers*.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[spi.h](drivers_2spi_8h_source.md)

- [spi\_buf\_set](structspi__buf__set.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
