---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h.html
original_path: doxygen/html/mm__drv__intel__adsp__mtl__tlb_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm\_drv\_intel\_adsp\_mtl\_tlb.h File Reference

[Go to the source code of this file.](mm__drv__intel__adsp__mtl__tlb_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [intel\_adsp\_tlb\_api](structintel__adsp__tlb__api.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mm\_save\_context](#aec3b78e74d53f6a9fe6ca029c7d776a5)) (void \*storage\_buffer) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [mm\_get\_storage\_size](#a19135d221cf896eb1795c2f22f6679bc)) (void) |

| Functions | |
| --- | --- |
| void | [adsp\_mm\_restore\_context](#aa98be3168d56e8fb7e183563eb64cbdb) (void \*storage\_buffer) |

## Typedef Documentation

## [◆ ](#a19135d221cf896eb1795c2f22f6679bc)mm\_get\_storage\_size

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mm\_get\_storage\_size) (void) |
| --- |

## [◆ ](#aec3b78e74d53f6a9fe6ca029c7d776a5)mm\_save\_context

| typedef void(\* mm\_save\_context) (void \*storage\_buffer) |
| --- |

## Function Documentation

## [◆ ](#aa98be3168d56e8fb7e183563eb64cbdb)adsp\_mm\_restore\_context()

| void adsp\_mm\_restore\_context | ( | void \* | *storage\_buffer* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mm](dir_464cfbc388e9245b11da9b89dd2be842.md)
- [mm\_drv\_intel\_adsp\_mtl\_tlb.h](mm__drv__intel__adsp__mtl__tlb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
