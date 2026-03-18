---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structrtio__sqe__pool.html
original_path: doxygen/html/structrtio__sqe__pool.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_sqe\_pool Struct Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

`#include <[rtio.h](rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [rtio\_mpsc](structrtio__mpsc.md) | [free\_q](#a95f516beb25feb60e44b42cd72d115b8) |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pool\_size](#ade3b4354d007fe17a7753c26e2121465) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pool\_free](#af7990b1510ad2343573f3e4e502475b0) |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [pool](#ab2c0394e175bd8c6f0c02edb315b6c9b) |

## Field Documentation

## [◆ ](#a95f516beb25feb60e44b42cd72d115b8)free\_q

| struct [rtio\_mpsc](structrtio__mpsc.md) rtio\_sqe\_pool::free\_q |
| --- |

## [◆ ](#ab2c0394e175bd8c6f0c02edb315b6c9b)pool

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* rtio\_sqe\_pool::pool |
| --- |

## [◆ ](#af7990b1510ad2343573f3e4e502475b0)pool\_free

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rtio\_sqe\_pool::pool\_free |
| --- |

## [◆ ](#ade3b4354d007fe17a7753c26e2121465)pool\_size

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rtio\_sqe\_pool::pool\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[rtio.h](rtio_8h_source.md)

- [rtio\_sqe\_pool](structrtio__sqe__pool.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
