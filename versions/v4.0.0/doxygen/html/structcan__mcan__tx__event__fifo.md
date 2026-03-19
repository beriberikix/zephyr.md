---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcan__mcan__tx__event__fifo.html
original_path: doxygen/html/structcan__mcan__tx__event__fifo.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_tx\_event\_fifo Struct Reference

Bosch M\_CAN Tx Event FIFO Element.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [ext\_id](#a3b4c61b9edcd1720235c3784131693d1): 29 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [rtr](#a17d5b6caf6519bf199dc179c11550abb): 1 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [xtd](#aac19c259f3e966d771c0088a32cbe47d): 1 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [esi](#a796967d04c60cd9cf423d904c6118944): 1 |  |
| } |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pad1](#a6be85a808788bd611055235b00a9b1f4): 18 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [std\_id](#a7698679cf93c707b423e9c695209f072): 11 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pad2](#a461d68069593b42d6961d6ff0525f783): 3 |  |
| } |  |
| }; |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [txts](#aacc10d577c20325baf54d7bb20e32583) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dlc](#a96aa98b30f603a5c5676e6a244f5d6c9): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [brs](#ac3924771aeb8885b4ad8d59758131b1a): 1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fdf](#a4075852d322da2eb4e3acb9d7c2e6d64): 1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [et](#a23ff309d6fb887166da2290646df200c): 2 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mm](#a4a706b7da7d9354ffc559ec65e1701ca) |

## Detailed Description

Bosch M\_CAN Tx Event FIFO Element.

See Bosch M\_CAN Users Manual section 2.4.4 for details.

## Field Documentation

## [◆ ](#aef931bef947b532d36b2c11f43c3242f)[union]

| union { ... } [can\_mcan\_tx\_event\_fifo](structcan__mcan__tx__event__fifo.md) |
| --- |

## [◆ ](#ac3924771aeb8885b4ad8d59758131b1a)brs

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_event\_fifo::brs |
| --- |

## [◆ ](#a96aa98b30f603a5c5676e6a244f5d6c9)dlc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_event\_fifo::dlc |
| --- |

## [◆ ](#a796967d04c60cd9cf423d904c6118944)esi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_event\_fifo::esi |
| --- |

## [◆ ](#a23ff309d6fb887166da2290646df200c)et

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_event\_fifo::et |
| --- |

## [◆ ](#a3b4c61b9edcd1720235c3784131693d1)ext\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_event\_fifo::ext\_id |
| --- |

## [◆ ](#a4075852d322da2eb4e3acb9d7c2e6d64)fdf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_event\_fifo::fdf |
| --- |

## [◆ ](#a4a706b7da7d9354ffc559ec65e1701ca)mm

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_event\_fifo::mm |
| --- |

## [◆ ](#a6be85a808788bd611055235b00a9b1f4)pad1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_event\_fifo::pad1 |
| --- |

## [◆ ](#a461d68069593b42d6961d6ff0525f783)pad2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_event\_fifo::pad2 |
| --- |

## [◆ ](#a17d5b6caf6519bf199dc179c11550abb)rtr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_event\_fifo::rtr |
| --- |

## [◆ ](#a7698679cf93c707b423e9c695209f072)std\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_event\_fifo::std\_id |
| --- |

## [◆ ](#aacc10d577c20325baf54d7bb20e32583)txts

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_mcan\_tx\_event\_fifo::txts |
| --- |

## [◆ ](#aac19c259f3e966d771c0088a32cbe47d)xtd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_event\_fifo::xtd |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_tx\_event\_fifo](structcan__mcan__tx__event__fifo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
