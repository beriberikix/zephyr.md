---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__mem__partition__attr__t.html
original_path: doxygen/html/structk__mem__partition__attr__t.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_mem\_partition\_attr\_t Struct Reference

`#include <[arm_mpu_v7m.h](arm__mpu__v7m_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rasr\_attr](#a04b3fd9acde8acc4eac37a1354bd7789) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rbar](#a015f590fd186c7042386cbcce25b134f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mair\_idx](#acf7bbe6773a1273b29df31618602ed3c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ap\_attr](#aeb16f8a8402a7190081ac96093189f27) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [attrs](#a4e49930c31e896b9b52867d6b83e3ae7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pmp\_attr](#aa1b529cb23bc5b4060da29d8ac52a124) |

## Field Documentation

## [◆ ](#aeb16f8a8402a7190081ac96093189f27)ap\_attr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mem\_partition\_attr\_t::ap\_attr |
| --- |

## [◆ ](#a4e49930c31e896b9b52867d6b83e3ae7)attrs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mem\_partition\_attr\_t::attrs |
| --- |

## [◆ ](#acf7bbe6773a1273b29df31618602ed3c)mair\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) k\_mem\_partition\_attr\_t::mair\_idx |
| --- |

## [◆ ](#aa1b529cb23bc5b4060da29d8ac52a124)pmp\_attr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k\_mem\_partition\_attr\_t::pmp\_attr |
| --- |

## [◆ ](#a04b3fd9acde8acc4eac37a1354bd7789)rasr\_attr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mem\_partition\_attr\_t::rasr\_attr |
| --- |

## [◆ ](#a015f590fd186c7042386cbcce25b134f)rbar

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) k\_mem\_partition\_attr\_t::rbar |
| --- |

---

The documentation for this struct was generated from the following files:

- zephyr/arch/arm/mpu/[arm\_mpu\_v7m.h](arm__mpu__v7m_8h_source.md)
- zephyr/arch/arm/mpu/[arm\_mpu\_v8.h](arm__mpu__v8_8h_source.md)
- zephyr/arch/arm/mpu/[nxp\_mpu.h](nxp__mpu_8h_source.md)
- zephyr/arch/arm64/[arm\_mmu.h](4_2arm__mmu_8h_source.md)
- zephyr/arch/riscv/[arch.h](riscv_2arch_8h_source.md)

- [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
