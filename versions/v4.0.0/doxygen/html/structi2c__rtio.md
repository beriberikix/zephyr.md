---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structi2c__rtio.html
original_path: doxygen/html/structi2c__rtio.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_rtio Struct Reference

Driver context for implementing i2c with rtio.
[More...](#details)

`#include <[rtio.h](drivers_2i2c_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct k\_sem | [lock](#a6cc7e4a39d59803334127cf6d2193bd8) |
| struct [k\_spinlock](structk__spinlock.md) | [slock](#a35188f6b135b3feedb1879dd6e0ed76d) |
| struct [rtio](structrtio.md) \* | [r](#a984ecd6802234bda30f835e2707571c2) |
| struct [mpsc](structmpsc.md) | [io\_q](#a35d6b41c23195012c76cf9597f214c60) |
| struct [rtio\_iodev](structrtio__iodev.md) | [iodev](#a4d0d75b7f4b9a16b0156386691eb365a) |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [txn\_head](#aef9f2ffc6128e993d499a4e345c31b05) |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [txn\_curr](#abe0c5e8cdebac52f6c5886ead3eabed3) |
| struct [i2c\_dt\_spec](structi2c__dt__spec.md) | [dt\_spec](#a962efcae6ce0598bfab3b6fc0a91b467) |

## Detailed Description

Driver context for implementing i2c with rtio.

## Field Documentation

## [◆ ](#a962efcae6ce0598bfab3b6fc0a91b467)dt\_spec

| struct [i2c\_dt\_spec](structi2c__dt__spec.md) i2c\_rtio::dt\_spec |
| --- |

## [◆ ](#a35d6b41c23195012c76cf9597f214c60)io\_q

| struct [mpsc](structmpsc.md) i2c\_rtio::io\_q |
| --- |

## [◆ ](#a4d0d75b7f4b9a16b0156386691eb365a)iodev

| struct [rtio\_iodev](structrtio__iodev.md) i2c\_rtio::iodev |
| --- |

## [◆ ](#a6cc7e4a39d59803334127cf6d2193bd8)lock

| struct k\_sem i2c\_rtio::lock |
| --- |

## [◆ ](#a984ecd6802234bda30f835e2707571c2)r

| struct [rtio](structrtio.md)\* i2c\_rtio::r |
| --- |

## [◆ ](#a35188f6b135b3feedb1879dd6e0ed76d)slock

| struct [k\_spinlock](structk__spinlock.md) i2c\_rtio::slock |
| --- |

## [◆ ](#abe0c5e8cdebac52f6c5886ead3eabed3)txn\_curr

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* i2c\_rtio::txn\_curr |
| --- |

## [◆ ](#aef9f2ffc6128e993d499a4e345c31b05)txn\_head

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* i2c\_rtio::txn\_head |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i2c/[rtio.h](drivers_2i2c_2rtio_8h_source.md)

- [i2c\_rtio](structi2c__rtio.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
