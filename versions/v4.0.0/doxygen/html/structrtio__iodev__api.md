---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structrtio__iodev__api.html
original_path: doxygen/html/structrtio__iodev__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_iodev\_api Struct Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

API that an RTIO IO device should implement.
[More...](#details)

`#include <[rtio.h](rtio_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [submit](#a6cd795906753535571ec1ecc0e0c430c) )(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit to the iodev an entry to work on. |

## Detailed Description

API that an RTIO IO device should implement.

## Field Documentation

## [◆ ](#a6cd795906753535571ec1ecc0e0c430c)submit

| void(\* rtio\_iodev\_api::submit) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
| --- |

Submit to the iodev an entry to work on.

This call should be short in duration and most likely either enqueue or kick off an entry with the hardware.

Parameters
:   | iodev\_sqe | Submission queue entry |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[rtio.h](rtio_2rtio_8h_source.md)

- [rtio\_iodev\_api](structrtio__iodev__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
