---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__event.html
original_path: doxygen/html/structk__event.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_event Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Event APIs](group__event__apis.md)

Event Structure.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| \_wait\_q\_t | [wait\_q](#a5bacd5f2d34da646d9d7ee229842e432) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [events](#a54c6f5997132e88406ffa5bcc0a10b83) |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#a1f0de9c69f29ad854f3b0d510ceb1efc) |

## Detailed Description

Event Structure.

## Field Documentation

## [◆ ](#a54c6f5997132e88406ffa5bcc0a10b83)events

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_event::events |
| --- |

## [◆ ](#a1f0de9c69f29ad854f3b0d510ceb1efc)lock

| struct [k\_spinlock](structk__spinlock.md) k\_event::lock |
| --- |

## [◆ ](#a5bacd5f2d34da646d9d7ee229842e432)wait\_q

| \_wait\_q\_t k\_event::wait\_q |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_event](structk__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
