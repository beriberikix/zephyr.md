---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structrtio__iodev__sqe.html
original_path: doxygen/html/structrtio__iodev__sqe.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_iodev\_sqe Struct Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

Compute the mempool block index for a given pointer.
[More...](#details)

`#include <[rtio.h](rtio_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [rtio\_sqe](structrtio__sqe.md) | [sqe](#a2bd98599678909c0ddb22f879affa12b) |
| struct [mpsc\_node](structmpsc__node.md) | [q](#a9cfdd004b65a5e2bc111bc2fb333498c) |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [next](#a2afb82e550e614f87db7cd1bf2c3a352) |
| struct [rtio](structrtio.md) \* | [r](#a3c3a050793589258eab5ff5ac30f24c8) |

## Detailed Description

Compute the mempool block index for a given pointer.

Parameters
:   | [in] | [r](#a3c3a050793589258eab5ff5ac30f24c8) | RTIO context |
    | --- | --- | --- |
    | [in] | ptr | Memory pointer in the mempool |

Returns
:   Index of the mempool block associated with the pointer. Or UINT16\_MAX if invalid.

IO device submission queue entry

May be cast safely to and from a [rtio\_sqe](structrtio__sqe.md "A submission queue event.") as they occupy the same memory provided by the pool

## Field Documentation

## [◆ ](#a2afb82e550e614f87db7cd1bf2c3a352)next

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* rtio\_iodev\_sqe::next |
| --- |

## [◆ ](#a9cfdd004b65a5e2bc111bc2fb333498c)q

| struct [mpsc\_node](structmpsc__node.md) rtio\_iodev\_sqe::q |
| --- |

## [◆ ](#a3c3a050793589258eab5ff5ac30f24c8)r

| struct [rtio](structrtio.md)\* rtio\_iodev\_sqe::r |
| --- |

## [◆ ](#a2bd98599678909c0ddb22f879affa12b)sqe

| struct [rtio\_sqe](structrtio__sqe.md) rtio\_iodev\_sqe::sqe |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[rtio.h](rtio_2rtio_8h_source.md)

- [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
