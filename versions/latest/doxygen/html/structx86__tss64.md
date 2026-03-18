---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structx86__tss64.html
original_path: doxygen/html/structx86__tss64.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

x86\_tss64 Struct Reference

`#include <[thread.h](arch_2x86_2intel64_2thread_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved0](#a3ff44c512471f9cc2c4c6646d238857b) [4] |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [rsp0](#ab6a7bd042da10b4540ac2f208df12dc6) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [rsp1](#a3480fa4dbb902b1432877367643caa67) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [rsp2](#aa57637fcc7fb8d3c3aaba20a904dad8c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved](#acf57e387decb430168f62d02e185b481) [8] |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ist1](#aad1ee7a792e1d84ffbd450aeb2f512c6) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ist2](#a104c0c491e7d42742b971e620c7413c4) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ist3](#a6967793f8c50fff0fe45fe3be89213e0) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ist4](#a5c1639407277f12412aef9a36f62f7f8) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ist5](#ac028c09a272d34ac66cde1556f5b95cb) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ist6](#a2a5dba1c1f8a16f42ff83ce4d34f1873) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ist7](#a652e42fc803a5176f4e1c46588c70204) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved1](#a44383c388151792d34b34d331df8fc4e) [10] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iomapb](#ac83f83b8b8a399ac988911b75d3e66d3) |
| struct \_cpu \* | [cpu](#a34157a050bb727f67286482e6d0c34dd) |
| char \* | [psp](#a959e976899cdcff13cfafba8514489f5) |
| char \* | [usp](#afe97afae56793aae5ed3ba35f4b06143) |

## Field Documentation

## [◆ ](#a34157a050bb727f67286482e6d0c34dd)cpu

| struct \_cpu\* x86\_tss64::cpu |
| --- |

## [◆ ](#ac83f83b8b8a399ac988911b75d3e66d3)iomapb

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x86\_tss64::iomapb |
| --- |

## [◆ ](#aad1ee7a792e1d84ffbd450aeb2f512c6)ist1

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::ist1 |
| --- |

## [◆ ](#a104c0c491e7d42742b971e620c7413c4)ist2

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::ist2 |
| --- |

## [◆ ](#a6967793f8c50fff0fe45fe3be89213e0)ist3

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::ist3 |
| --- |

## [◆ ](#a5c1639407277f12412aef9a36f62f7f8)ist4

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::ist4 |
| --- |

## [◆ ](#ac028c09a272d34ac66cde1556f5b95cb)ist5

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::ist5 |
| --- |

## [◆ ](#a2a5dba1c1f8a16f42ff83ce4d34f1873)ist6

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::ist6 |
| --- |

## [◆ ](#a652e42fc803a5176f4e1c46588c70204)ist7

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::ist7 |
| --- |

## [◆ ](#a959e976899cdcff13cfafba8514489f5)psp

| char\* x86\_tss64::psp |
| --- |

## [◆ ](#acf57e387decb430168f62d02e185b481)reserved

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) x86\_tss64::reserved[8] |
| --- |

## [◆ ](#a3ff44c512471f9cc2c4c6646d238857b)reserved0

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) x86\_tss64::reserved0[4] |
| --- |

## [◆ ](#a44383c388151792d34b34d331df8fc4e)reserved1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) x86\_tss64::reserved1[10] |
| --- |

## [◆ ](#ab6a7bd042da10b4540ac2f208df12dc6)rsp0

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::rsp0 |
| --- |

## [◆ ](#a3480fa4dbb902b1432877367643caa67)rsp1

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::rsp1 |
| --- |

## [◆ ](#aa57637fcc7fb8d3c3aaba20a904dad8c)rsp2

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x86\_tss64::rsp2 |
| --- |

## [◆ ](#afe97afae56793aae5ed3ba35f4b06143)usp

| char\* x86\_tss64::usp |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/arch/x86/intel64/[thread.h](arch_2x86_2intel64_2thread_8h_source.md)

- [x86\_tss64](structx86__tss64.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
