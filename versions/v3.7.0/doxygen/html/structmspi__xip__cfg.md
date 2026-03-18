---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmspi__xip__cfg.html
original_path: doxygen/html/structmspi__xip__cfg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_xip\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Configure API](group__mspi__configure__api.md)

MSPI controller XIP configuration.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable](#a2ba9873d13a24b5fa42d28e910368486) |
|  | XIP enable. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [address\_offset](#a58c0c05d4fc58704b8b46677b468247c) |
|  | XIP region start address = hardware default + address offset. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [size](#ac393537eb1a209e1c1e41bf639782e72) |
|  | XIP region size. |
| enum [mspi\_xip\_permit](group__mspi__interface.md#ga006a1e32778a02299b3500886bb194fa) | [permission](#a172af688c9f92af04978559697fe230f) |
|  | XIP access permission. |

## Detailed Description

MSPI controller XIP configuration.

## Field Documentation

## [◆ ](#a58c0c05d4fc58704b8b46677b468247c)address\_offset

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_xip\_cfg::address\_offset |
| --- |

XIP region start address = hardware default + address offset.

## [◆ ](#a2ba9873d13a24b5fa42d28e910368486)enable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mspi\_xip\_cfg::enable |
| --- |

XIP enable.

## [◆ ](#a172af688c9f92af04978559697fe230f)permission

| enum [mspi\_xip\_permit](group__mspi__interface.md#ga006a1e32778a02299b3500886bb194fa) mspi\_xip\_cfg::permission |
| --- |

XIP access permission.

## [◆ ](#ac393537eb1a209e1c1e41bf639782e72)size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_xip\_cfg::size |
| --- |

XIP region size.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_xip\_cfg](structmspi__xip__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
