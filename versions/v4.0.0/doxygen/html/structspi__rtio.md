---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structspi__rtio.html
original_path: doxygen/html/structspi__rtio.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_rtio Struct Reference

Driver context for implementing SPI with RTIO.
[More...](#details)

`#include <[rtio.h](drivers_2spi_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#a57d4533fa5b8939cdb8ddb6ab8dfada2) |
| struct [rtio](structrtio.md) \* | [r](#a7438ee10b82f0c31f3cb4f40384e7d11) |
| struct [mpsc](structmpsc.md) | [io\_q](#afa7ca567196334bf8dc768c69697b79b) |
| struct [rtio\_iodev](structrtio__iodev.md) | [iodev](#a16fa5e36ced62e267bae60faa1230392) |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [txn\_head](#a2688d4999533c55e7d6a052b579d5a4b) |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [txn\_curr](#add2905749d8c26f7aedd29bcef27dff0) |
| struct [spi\_dt\_spec](structspi__dt__spec.md) | [dt\_spec](#a8ea13c0000663a846f3d131a92d5c9ce) |

## Detailed Description

Driver context for implementing SPI with RTIO.

## Field Documentation

## [◆ ](#a8ea13c0000663a846f3d131a92d5c9ce)dt\_spec

| struct [spi\_dt\_spec](structspi__dt__spec.md) spi\_rtio::dt\_spec |
| --- |

## [◆ ](#afa7ca567196334bf8dc768c69697b79b)io\_q

| struct [mpsc](structmpsc.md) spi\_rtio::io\_q |
| --- |

## [◆ ](#a16fa5e36ced62e267bae60faa1230392)iodev

| struct [rtio\_iodev](structrtio__iodev.md) spi\_rtio::iodev |
| --- |

## [◆ ](#a57d4533fa5b8939cdb8ddb6ab8dfada2)lock

| struct [k\_spinlock](structk__spinlock.md) spi\_rtio::lock |
| --- |

## [◆ ](#a7438ee10b82f0c31f3cb4f40384e7d11)r

| struct [rtio](structrtio.md)\* spi\_rtio::r |
| --- |

## [◆ ](#add2905749d8c26f7aedd29bcef27dff0)txn\_curr

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* spi\_rtio::txn\_curr |
| --- |

## [◆ ](#a2688d4999533c55e7d6a052b579d5a4b)txn\_head

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* spi\_rtio::txn\_head |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/spi/[rtio.h](drivers_2spi_2rtio_8h_source.md)

- [spi\_rtio](structspi__rtio.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
