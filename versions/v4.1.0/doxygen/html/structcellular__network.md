---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcellular__network.html
original_path: doxygen/html/structcellular__network.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cellular\_network Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Cellular Interface](group__cellular__interface.md)

Cellular network structure.
[More...](#details)

`#include <[cellular.h](cellular_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [cellular\_access\_technology](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e) | [technology](#ad7afde61da3322e80f935c2b963eacf0) |
|  | Cellular access technology. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | [bands](#a9313dcce10911b0febd56022c380f283) |
|  | List of bands, as defined by the specified cellular access technology, to enables. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [size](#ab54057fc7cea1387c5ad3694103b0686) |
|  | Size of bands. |

## Detailed Description

Cellular network structure.

## Field Documentation

## [◆ ](#a9313dcce10911b0febd56022c380f283)bands

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)\* cellular\_network::bands |
| --- |

List of bands, as defined by the specified cellular access technology, to enables.

All supported bands are enabled if none are provided.

## [◆ ](#ab54057fc7cea1387c5ad3694103b0686)size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cellular\_network::size |
| --- |

Size of bands.

## [◆ ](#ad7afde61da3322e80f935c2b963eacf0)technology

| enum [cellular\_access\_technology](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e) cellular\_network::technology |
| --- |

Cellular access technology.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[cellular.h](cellular_8h_source.md)

- [cellular\_network](structcellular__network.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
