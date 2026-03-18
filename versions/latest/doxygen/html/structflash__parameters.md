---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structflash__parameters.html
original_path: doxygen/html/structflash__parameters.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_parameters Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [FLASH Interface](group__flash__interface.md)

Flash memory parameters.
[More...](#details)

`#include <[flash.h](flash_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [write\_block\_size](#a9795a3e4fae4d7b81745e876f62ab3a8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [erase\_value](#a218b0cbc797572ce096d0d6f55475ff9) |

## Detailed Description

Flash memory parameters.

Contents of this structure suppose to be filled in during flash device initialization and stay constant through a runtime.

## Field Documentation

## [◆ ](#a218b0cbc797572ce096d0d6f55475ff9)erase\_value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flash\_parameters::erase\_value |
| --- |

## [◆ ](#a9795a3e4fae4d7b81745e876f62ab3a8)write\_block\_size

| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) flash\_parameters::write\_block\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[flash.h](flash_8h_source.md)

- [flash\_parameters](structflash__parameters.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
