---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsdio__cis.html
original_path: doxygen/html/structsdio__cis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdio\_cis Struct Reference

SDIO common CIS tuple properties.
[More...](#details)

`#include <[sd_spec.h](sd__spec_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [manf\_id](#a04c8a774c65f683185e5a32e15afb67c) |
|  | manufacturer ID |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [manf\_code](#ad52e1df89176f728734ce0e69fb2b4c8) |
|  | manufacturer code |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [func\_id](#ad38be5cade97ac92de62094d8e3b8549) |
|  | sdio device class function id |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_blk\_size](#a1b340e20630994f91314be17dd9055ca) |
|  | Max transfer block size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_speed](#a56d3ee1d6b8d0d87e0efdbda15b7076d) |
|  | Max transfer speed. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rdy\_timeout](#a86a01890f31788ae5465b1c8dc47bcf2) |
|  | I/O ready timeout. |

## Detailed Description

SDIO common CIS tuple properties.

CIS tuple properties. Note that additional properties exist for functions 1-7, but we do not read this data as the stack does not utilize it.

## Field Documentation

## [◆ ](#ad38be5cade97ac92de62094d8e3b8549)func\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sdio\_cis::func\_id |
| --- |

sdio device class function id

## [◆ ](#ad52e1df89176f728734ce0e69fb2b4c8)manf\_code

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sdio\_cis::manf\_code |
| --- |

manufacturer code

## [◆ ](#a04c8a774c65f683185e5a32e15afb67c)manf\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sdio\_cis::manf\_id |
| --- |

manufacturer ID

## [◆ ](#a1b340e20630994f91314be17dd9055ca)max\_blk\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sdio\_cis::max\_blk\_size |
| --- |

Max transfer block size.

## [◆ ](#a56d3ee1d6b8d0d87e0efdbda15b7076d)max\_speed

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sdio\_cis::max\_speed |
| --- |

Max transfer speed.

## [◆ ](#a86a01890f31788ae5465b1c8dc47bcf2)rdy\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sdio\_cis::rdy\_timeout |
| --- |

I/O ready timeout.

---

The documentation for this struct was generated from the following file:

- zephyr/sd/[sd\_spec.h](sd__spec_8h_source.md)

- [sdio\_cis](structsdio__cis.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
