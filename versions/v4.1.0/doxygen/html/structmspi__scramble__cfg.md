---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmspi__scramble__cfg.html
original_path: doxygen/html/structmspi__scramble__cfg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_scramble\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Configure API](group__mspi__configure__api.md)

MSPI controller scramble configuration.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable](#a362ce29f7748d28e818e2c809bd4cedd) |
|  | scramble enable |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [address\_offset](#adf56743768432f22f0a5090e1b823a67) |
|  | scramble region start address = hardware default + address offset |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [size](#a8d6d5b47b3d777674b974a6c79337b43) |
|  | scramble region size |

## Detailed Description

MSPI controller scramble configuration.

## Field Documentation

## [◆ ](#adf56743768432f22f0a5090e1b823a67)address\_offset

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_scramble\_cfg::address\_offset |
| --- |

scramble region start address = hardware default + address offset

## [◆ ](#a362ce29f7748d28e818e2c809bd4cedd)enable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mspi\_scramble\_cfg::enable |
| --- |

scramble enable

## [◆ ](#a8d6d5b47b3d777674b974a6c79337b43)size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_scramble\_cfg::size |
| --- |

scramble region size

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_scramble\_cfg](structmspi__scramble__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
