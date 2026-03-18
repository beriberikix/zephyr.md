---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpcie__ctrl__config.html
original_path: doxygen/html/structpcie__ctrl__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie\_ctrl\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [PCI Express Controller Interface](group__pcie__controller__interface.md)

Structure describing a device that supports the PCI Express Controller API.
[More...](#details)

`#include <[controller.h](drivers_2pcie_2controller_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [cfg\_addr](#a3de0f32aaf3ddb377897974dfdfe67bd) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [cfg\_size](#adb1b8ed76f3f994f2da72c8e8b40d4f0) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [ranges\_count](#a4a620f03546490b65ba4d097329928e8) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [flags](#a90e48aaca78a8284caa449ee3972d87b) |  |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)   [pcie\_bus\_addr](#a45f9fa1124aa64bbfd7ff2c5519cbb4b) |  |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)   [host\_map\_addr](#ace0b3505edc0aff3678a91b630244963) |  |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [map\_length](#ae3dd8d3d72a1597ee135b49e46e31bec) |  |
| } | [ranges](#a1a59bec03927f2c6b5fd0aed8c36e6b4) [] |

## Detailed Description

Structure describing a device that supports the PCI Express Controller API.

## Field Documentation

## [◆ ](#a3de0f32aaf3ddb377897974dfdfe67bd)cfg\_addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) pcie\_ctrl\_config::cfg\_addr |
| --- |

## [◆ ](#adb1b8ed76f3f994f2da72c8e8b40d4f0)cfg\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pcie\_ctrl\_config::cfg\_size |
| --- |

## [◆ ](#a90e48aaca78a8284caa449ee3972d87b)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcie\_ctrl\_config::flags |
| --- |

## [◆ ](#ace0b3505edc0aff3678a91b630244963)host\_map\_addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) pcie\_ctrl\_config::host\_map\_addr |
| --- |

## [◆ ](#ae3dd8d3d72a1597ee135b49e46e31bec)map\_length

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pcie\_ctrl\_config::map\_length |
| --- |

## [◆ ](#a45f9fa1124aa64bbfd7ff2c5519cbb4b)pcie\_bus\_addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) pcie\_ctrl\_config::pcie\_bus\_addr |
| --- |

## [◆ ](#a1a59bec03927f2c6b5fd0aed8c36e6b4)[struct]

| struct { ... } pcie\_ctrl\_config::ranges[] |
| --- |

## [◆ ](#a4a620f03546490b65ba4d097329928e8)ranges\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pcie\_ctrl\_config::ranges\_count |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/pcie/[controller.h](drivers_2pcie_2controller_8h_source.md)

- [pcie\_ctrl\_config](structpcie__ctrl__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
