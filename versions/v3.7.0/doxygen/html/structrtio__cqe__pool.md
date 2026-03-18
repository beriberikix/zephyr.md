---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structrtio__cqe__pool.html
original_path: doxygen/html/structrtio__cqe__pool.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_cqe\_pool Struct Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

`#include <[rtio.h](rtio_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mpsc](structmpsc.md) | [free\_q](#a13bd7991ff5622c1cb5aa6af014aaab3) |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pool\_size](#a43bf4141673c61493644539987f27fb1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pool\_free](#a4fb501a0ba15e2956113deaf4597d846) |
| struct [rtio\_cqe](structrtio__cqe.md) \* | [pool](#a05584219d473fcf85d46757fa9cea703) |

## Field Documentation

## [◆ ](#a13bd7991ff5622c1cb5aa6af014aaab3)free\_q

| struct [mpsc](structmpsc.md) rtio\_cqe\_pool::free\_q |
| --- |

## [◆ ](#a05584219d473fcf85d46757fa9cea703)pool

| struct [rtio\_cqe](structrtio__cqe.md)\* rtio\_cqe\_pool::pool |
| --- |

## [◆ ](#a4fb501a0ba15e2956113deaf4597d846)pool\_free

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rtio\_cqe\_pool::pool\_free |
| --- |

## [◆ ](#a43bf4141673c61493644539987f27fb1)pool\_size

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rtio\_cqe\_pool::pool\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[rtio.h](rtio_2rtio_8h_source.md)

- [rtio\_cqe\_pool](structrtio__cqe__pool.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
