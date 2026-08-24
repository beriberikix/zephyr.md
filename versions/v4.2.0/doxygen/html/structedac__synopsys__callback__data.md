---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structedac__synopsys__callback__data.html
original_path: doxygen/html/structedac__synopsys__callback__data.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

edac\_synopsys\_callback\_data Struct Reference

`#include <[zephyr/drivers/edac/edac_synopsys.h](edac__synopsys_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [corr\_err\_count](#a71c5e4b31f16927b483e7bd3bf8b6f32) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [corr\_err\_rank](#aece294a29dbd98a3e75f4cfb6c9c79c3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [corr\_err\_bg](#ae6a6c090671e5bfda93b904ee9e95a2b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [corr\_err\_bank](#a749fb5929f89a63cb62fd76f4c143dba) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [corr\_err\_row](#aa549050b7305f4e8bb15f5b849bec165) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [corr\_err\_col](#af23d5d538b8ebe722838a186c6b30909) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [corr\_err\_syndrome](#aca79f779ac263e5344dad5e12ee6d3da) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [corr\_err\_syndrome\_ecc](#a73567e401a706bbf392db489afd72012) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [corr\_err\_bitmask](#a10387f0ff6db7c6a116a8ccb2ba3e7c0) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [corr\_err\_bitmask\_ecc](#a659a7a12f24337cc57ea121e06cbd20c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [uncorr\_err\_count](#aa34f78372e80c57772ea864827a5abe1) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uncorr\_err\_rank](#a07c6bd60a094e5b807df0bf823959a3e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uncorr\_err\_bg](#af148757e829b0e0bfbf575521131f54b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uncorr\_err\_bank](#a8df3545fd3f7dfa8a99dcac90e708ec2) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [uncorr\_err\_row](#a99670584c0c09eaf2e14e6e797ec834d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uncorr\_err\_col](#a17fee6074688540133b07fb0d567857a) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [uncorr\_err\_syndrome](#a3c05b263247c78ac195760f6a73a30b8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uncorr\_err\_syndrome\_ecc](#a36d022f0de8a63581a4a2a95d923e041) |

## Field Documentation

## [◆ ](#a749fb5929f89a63cb62fd76f4c143dba)corr\_err\_bank

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::corr\_err\_bank |
| --- |

## [◆ ](#ae6a6c090671e5bfda93b904ee9e95a2b)corr\_err\_bg

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::corr\_err\_bg |
| --- |

## [◆ ](#a10387f0ff6db7c6a116a8ccb2ba3e7c0)corr\_err\_bitmask

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) edac\_synopsys\_callback\_data::corr\_err\_bitmask |
| --- |

## [◆ ](#a659a7a12f24337cc57ea121e06cbd20c)corr\_err\_bitmask\_ecc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::corr\_err\_bitmask\_ecc |
| --- |

## [◆ ](#af23d5d538b8ebe722838a186c6b30909)corr\_err\_col

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::corr\_err\_col |
| --- |

## [◆ ](#a71c5e4b31f16927b483e7bd3bf8b6f32)corr\_err\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) edac\_synopsys\_callback\_data::corr\_err\_count |
| --- |

## [◆ ](#aece294a29dbd98a3e75f4cfb6c9c79c3)corr\_err\_rank

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::corr\_err\_rank |
| --- |

## [◆ ](#aa549050b7305f4e8bb15f5b849bec165)corr\_err\_row

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) edac\_synopsys\_callback\_data::corr\_err\_row |
| --- |

## [◆ ](#aca79f779ac263e5344dad5e12ee6d3da)corr\_err\_syndrome

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) edac\_synopsys\_callback\_data::corr\_err\_syndrome |
| --- |

## [◆ ](#a73567e401a706bbf392db489afd72012)corr\_err\_syndrome\_ecc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::corr\_err\_syndrome\_ecc |
| --- |

## [◆ ](#a8df3545fd3f7dfa8a99dcac90e708ec2)uncorr\_err\_bank

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::uncorr\_err\_bank |
| --- |

## [◆ ](#af148757e829b0e0bfbf575521131f54b)uncorr\_err\_bg

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::uncorr\_err\_bg |
| --- |

## [◆ ](#a17fee6074688540133b07fb0d567857a)uncorr\_err\_col

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::uncorr\_err\_col |
| --- |

## [◆ ](#aa34f78372e80c57772ea864827a5abe1)uncorr\_err\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) edac\_synopsys\_callback\_data::uncorr\_err\_count |
| --- |

## [◆ ](#a07c6bd60a094e5b807df0bf823959a3e)uncorr\_err\_rank

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::uncorr\_err\_rank |
| --- |

## [◆ ](#a99670584c0c09eaf2e14e6e797ec834d)uncorr\_err\_row

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) edac\_synopsys\_callback\_data::uncorr\_err\_row |
| --- |

## [◆ ](#a3c05b263247c78ac195760f6a73a30b8)uncorr\_err\_syndrome

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) edac\_synopsys\_callback\_data::uncorr\_err\_syndrome |
| --- |

## [◆ ](#a36d022f0de8a63581a4a2a95d923e041)uncorr\_err\_syndrome\_ecc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edac\_synopsys\_callback\_data::uncorr\_err\_syndrome\_ecc |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/edac/[edac\_synopsys.h](edac__synopsys_8h_source.md)

- [edac\_synopsys\_callback\_data](structedac__synopsys__callback__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
