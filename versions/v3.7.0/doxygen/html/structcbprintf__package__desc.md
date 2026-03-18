---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcbprintf__package__desc.html
original_path: doxygen/html/structcbprintf__package__desc.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cbprintf\_package\_desc Struct Reference

cbprintf package descriptor.
[More...](#details)

`#include <[cbprintf.h](cbprintf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#a02876d066dd9ac4ba5bd3bdc19ff7681) |
|  | Package length (in 32 bit words). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [str\_cnt](#a3614347546912dae53d8f9633299912d) |
|  | Number of appended strings in the package. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ro\_str\_cnt](#ad9878876ae963e93850dcfd8d5df7b2f) |
|  | Number of read-only strings, indexes appended to the package. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rw\_str\_cnt](#ae9695a5e1a4fb70e3be5e9ab63c89937) |
|  | Number of read-write strings, indexes appended to the package. |

## Detailed Description

cbprintf package descriptor.

## Field Documentation

## [◆ ](#a02876d066dd9ac4ba5bd3bdc19ff7681)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cbprintf\_package\_desc::len |
| --- |

Package length (in 32 bit words).

## [◆ ](#ad9878876ae963e93850dcfd8d5df7b2f)ro\_str\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cbprintf\_package\_desc::ro\_str\_cnt |
| --- |

Number of read-only strings, indexes appended to the package.

## [◆ ](#ae9695a5e1a4fb70e3be5e9ab63c89937)rw\_str\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cbprintf\_package\_desc::rw\_str\_cnt |
| --- |

Number of read-write strings, indexes appended to the package.

## [◆ ](#a3614347546912dae53d8f9633299912d)str\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cbprintf\_package\_desc::str\_cnt |
| --- |

Number of appended strings in the package.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[cbprintf.h](cbprintf_8h_source.md)

- [cbprintf\_package\_desc](structcbprintf__package__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
