---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__rtio.html
original_path: doxygen/html/structi3c__rtio.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_rtio Struct Reference

Driver context for implementing i3c with rtio.
[More...](#details)

`#include <[rtio.h](drivers_2i3c_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct k\_sem | [lock](#af72118faec547f438b213aff87d5de50) |
| struct [k\_spinlock](structk__spinlock.md) | [slock](#a4ded14f281371d0daa3e7dcf477ab0c9) |
| struct [rtio](structrtio.md) \* | [r](#a9e084adb1e963cd713165c4404aabe5f) |
| struct [mpsc](structmpsc.md) | [io\_q](#ac8f7b2b24c07147d886c307e7af99d4d) |
| struct [rtio\_iodev](structrtio__iodev.md) | [iodev](#a1c73add1e0c1dbf67a5c7a6e4ee1e507) |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [txn\_head](#aea9fa855d6fd273cf672bf440027adb6) |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [txn\_curr](#a70a6f131830ffcb274cf6fdabafb6222) |
| struct [i3c\_device\_desc](structi3c__device__desc.md) \* | [i3c\_desc](#a24da09d1b6ba078444952566efb9bdbd) |

## Detailed Description

Driver context for implementing i3c with rtio.

## Field Documentation

## [◆ ](#a24da09d1b6ba078444952566efb9bdbd)i3c\_desc

| struct [i3c\_device\_desc](structi3c__device__desc.md)\* i3c\_rtio::i3c\_desc |
| --- |

## [◆ ](#ac8f7b2b24c07147d886c307e7af99d4d)io\_q

| struct [mpsc](structmpsc.md) i3c\_rtio::io\_q |
| --- |

## [◆ ](#a1c73add1e0c1dbf67a5c7a6e4ee1e507)iodev

| struct [rtio\_iodev](structrtio__iodev.md) i3c\_rtio::iodev |
| --- |

## [◆ ](#af72118faec547f438b213aff87d5de50)lock

| struct k\_sem i3c\_rtio::lock |
| --- |

## [◆ ](#a9e084adb1e963cd713165c4404aabe5f)r

| struct [rtio](structrtio.md)\* i3c\_rtio::r |
| --- |

## [◆ ](#a4ded14f281371d0daa3e7dcf477ab0c9)slock

| struct [k\_spinlock](structk__spinlock.md) i3c\_rtio::slock |
| --- |

## [◆ ](#a70a6f131830ffcb274cf6fdabafb6222)txn\_curr

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* i3c\_rtio::txn\_curr |
| --- |

## [◆ ](#aea9fa855d6fd273cf672bf440027adb6)txn\_head

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* i3c\_rtio::txn\_head |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[rtio.h](drivers_2i3c_2rtio_8h_source.md)

- [i3c\_rtio](structi3c__rtio.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
