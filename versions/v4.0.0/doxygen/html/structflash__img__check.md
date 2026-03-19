---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structflash__img__check.html
original_path: doxygen/html/structflash__img__check.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_img\_check Struct Reference

[Operating System Services](group__os__services.md) » [Flash image API](group__flash__img__api.md)

Structure for verify flash region integrity.
[More...](#details)

`#include <[flash_img.h](flash__img_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [match](#a6c4aebe9974ddebf0ceafe7f61af8ae9) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [clen](#abac05d254f5fc46093808083c86be379) |
|  | Match vector data. |

## Detailed Description

Structure for verify flash region integrity.

Match vector length is fixed and depends on size from hash algorithm used to verify flash integrity. The current available algorithm is SHA-256.

## Field Documentation

## [◆ ](#abac05d254f5fc46093808083c86be379)clen

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) flash\_img\_check::clen |
| --- |

Match vector data.

## [◆ ](#a6c4aebe9974ddebf0ceafe7f61af8ae9)match

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* flash\_img\_check::match |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/dfu/[flash\_img.h](flash__img_8h_source.md)

- [flash\_img\_check](structflash__img__check.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
