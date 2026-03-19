---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcan__mcan__rx__fifo__hdr.html
original_path: doxygen/html/structcan__mcan__rx__fifo__hdr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_rx\_fifo\_hdr Struct Reference

Bosch M\_CAN Rx Buffer and FIFO Element header.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [ext\_id](#acdea19720ee1d76254b6e9931ffeca07): 29 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [rtr](#aa315257f7f5dcb438ba70c22ced8b9fe): 1 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [xtd](#ab75c330ef4724997f665a84c99ab2c57): 1 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [esi](#a746f7f80e30ac574fcb785e78cbcdf44): 1 |  |
| } |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pad1](#afbdea1a9674af705a4954709e64ed45a): 18 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [std\_id](#ac97eacf0d6cf2ef9ae6454b7604b52b5): 11 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pad2](#a03a015b8195efeda0287b1323de54b3c): 3 |  |
| } |  |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rxts](#ace6229b7580d1954638d1469700f5ebd): 16 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dlc](#a44564c3ab98be8cd92b6f17c9379d045): 4 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [brs](#a35d6a09669761d4b7d60c06e36f74e06): 1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fdf](#a8beb206b8c5ef1dd7c25d17ef5045d55): 1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [res](#a0f95cfa20e9a9e1c75da3afb1dd4542f): 2 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fidx](#ad6bcb3637d79f4e87371dd91fb7a5881): 7 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [anmf](#a6256e635694330dc3428f30387838f96): 1 |

## Detailed Description

Bosch M\_CAN Rx Buffer and FIFO Element header.

See Bosch M\_CAN Users Manual section 2.4.2 for details.

## Field Documentation

## [◆ ](#ac027598afb4bb1802b0168b69d576079)[union]

| union { ... } [can\_mcan\_rx\_fifo\_hdr](structcan__mcan__rx__fifo__hdr.md) |
| --- |

## [◆ ](#a6256e635694330dc3428f30387838f96)anmf

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::anmf |
| --- |

## [◆ ](#a35d6a09669761d4b7d60c06e36f74e06)brs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::brs |
| --- |

## [◆ ](#a44564c3ab98be8cd92b6f17c9379d045)dlc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::dlc |
| --- |

## [◆ ](#a746f7f80e30ac574fcb785e78cbcdf44)esi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::esi |
| --- |

## [◆ ](#acdea19720ee1d76254b6e9931ffeca07)ext\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::ext\_id |
| --- |

## [◆ ](#a8beb206b8c5ef1dd7c25d17ef5045d55)fdf

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::fdf |
| --- |

## [◆ ](#ad6bcb3637d79f4e87371dd91fb7a5881)fidx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::fidx |
| --- |

## [◆ ](#afbdea1a9674af705a4954709e64ed45a)pad1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::pad1 |
| --- |

## [◆ ](#a03a015b8195efeda0287b1323de54b3c)pad2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::pad2 |
| --- |

## [◆ ](#a0f95cfa20e9a9e1c75da3afb1dd4542f)res

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::res |
| --- |

## [◆ ](#aa315257f7f5dcb438ba70c22ced8b9fe)rtr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::rtr |
| --- |

## [◆ ](#ace6229b7580d1954638d1469700f5ebd)rxts

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::rxts |
| --- |

## [◆ ](#ac97eacf0d6cf2ef9ae6454b7604b52b5)std\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::std\_id |
| --- |

## [◆ ](#ab75c330ef4724997f665a84c99ab2c57)xtd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_rx\_fifo\_hdr::xtd |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_rx\_fifo\_hdr](structcan__mcan__rx__fifo__hdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
