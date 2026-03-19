---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structarm__mpu__region__attr.html
original_path: doxygen/html/structarm__mpu__region__attr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu\_region\_attr Struct Reference

`#include <[arm_mpu_v7m.h](arm__mpu__v7m_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rasr](#a8e38b1257bba7f67148bd7868f7cde23) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rbar](#a02565921f84b5f03f9f86c67a935b17a): 5 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mair\_idx](#a791b4f41df0ed0cb3eb5e69d944f038e): 3 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r\_limit](#a77b05b42da47d398373dd747112def37) |

## Field Documentation

## [◆ ](#a791b4f41df0ed0cb3eb5e69d944f038e)mair\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) arm\_mpu\_region\_attr::mair\_idx |
| --- |

## [◆ ](#a77b05b42da47d398373dd747112def37)r\_limit

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arm\_mpu\_region\_attr::r\_limit |
| --- |

## [◆ ](#a8e38b1257bba7f67148bd7868f7cde23)rasr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arm\_mpu\_region\_attr::rasr |
| --- |

## [◆ ](#a02565921f84b5f03f9f86c67a935b17a)rbar

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) arm\_mpu\_region\_attr::rbar |
| --- |

---

The documentation for this struct was generated from the following files:

- zephyr/arch/arm/mpu/[arm\_mpu\_v7m.h](arm__mpu__v7m_8h_source.md)
- zephyr/arch/arm/mpu/[arm\_mpu\_v8.h](arm__mpu__v8_8h_source.md)
- zephyr/arch/arm64/cortex\_r/[arm\_mpu.h](4_2cortex__r_2arm__mpu_8h_source.md)

- [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
