---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structxtensa__mpu__entry.html
original_path: doxygen/html/structxtensa__mpu__entry.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xtensa\_mpu\_entry Struct Reference

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md) » [Xtensa APIs](group__xtensa__apis.md) » [Xtensa Memory Protection Unit (MPU) APIs](group__xtensa__mpu__apis.md)

Foreground MPU Entry.
[More...](#details)

`#include <[mpu.h](xtensa_2mpu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [raw](#a77dc5a2d8512fca38c9c305b722556f5) |  |
|  | Raw value. [More...](#a77dc5a2d8512fca38c9c305b722556f5) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [enable](#af18d88c18df4dfb17ceb78c560bd2e61):1 |  |
|  | Enable bit for this entry. [More...](#af18d88c18df4dfb17ceb78c560bd2e61) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [lock](#a9dbb164dd9e942b0d2e91621724d81ae):1 |  |
|  | Lock bit for this entry. [More...](#a9dbb164dd9e942b0d2e91621724d81ae) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [mbz](#a09cb878dd936700c64c8d2df10b58ed4):3 |  |
|  | Must be zero. [More...](#a09cb878dd936700c64c8d2df10b58ed4) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [start\_addr](#ada352b7ede662f57bb162e5df1f819bd):27 |  |
|  | Start address of this MPU entry. [More...](#ada352b7ede662f57bb162e5df1f819bd) |
| }   [p](#a32bfc370b92a904abe8fe522afb9a813) |
|  | Individual parts. [More...](#a32bfc370b92a904abe8fe522afb9a813) |
| } | [as](#a359f3d970a15c764d5b5cc3ac00b87c0) |
|  | Content of as register for WPTLB. |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [raw](#a77dc5a2d8512fca38c9c305b722556f5) |  |
|  | Raw value. [More...](#a77dc5a2d8512fca38c9c305b722556f5) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [segment](#a26879b4bb6ec5c2040a864a1286b177f):5 |  |
|  | The segment number of this MPU entry. [More...](#a26879b4bb6ec5c2040a864a1286b177f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [mbz1](#a0461da13881e2cde2a8607783073eeec):3 |  |
|  | Must be zero (part 1). [More...](#a0461da13881e2cde2a8607783073eeec) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [access\_rights](#ab4a226d6c492a1fea3e2e4806ea6f041):4 |  |
|  | Access rights associated with this MPU entry. [More...](#ab4a226d6c492a1fea3e2e4806ea6f041) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [memory\_type](#a1b9764368a50f0674ede7bc3450485c7):9 |  |
|  | Memory type associated with this MPU entry. [More...](#a1b9764368a50f0674ede7bc3450485c7) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [mbz2](#af4bb525147d4ba54bf46c626b3c0a888):11 |  |
|  | Must be zero (part 2). [More...](#af4bb525147d4ba54bf46c626b3c0a888) |
| }   [p](#a9fa96af81c4af48faa1084cdde720ca9) |
|  | Individual parts. [More...](#a9fa96af81c4af48faa1084cdde720ca9) |
| } | [at](#a5c41f0a0db9f71e774989dfdc5f05475) |
|  | Content of at register for WPTLB. |

## Detailed Description

Foreground MPU Entry.

This holds the as, at register values for one MPU entry which can be used directly by WPTLB.

## Field Documentation

## [◆ ](#ab4a226d6c492a1fea3e2e4806ea6f041)access\_rights

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::access\_rights |
| --- |

Access rights associated with this MPU entry.

This dictates the access right from the start address of this entry, to the start address of next entry.

Refer to XTENSA\_MPU\_ACCESS\_\* macros for available rights.

## [◆ ](#a359f3d970a15c764d5b5cc3ac00b87c0)[union]

| union { ... } xtensa\_mpu\_entry::as |
| --- |

Content of as register for WPTLB.

This contains the start address, the enable bit, and the lock bit.

## [◆ ](#a5c41f0a0db9f71e774989dfdc5f05475)[union]

| union { ... } xtensa\_mpu\_entry::at |
| --- |

Content of at register for WPTLB.

This contains the memory type, access rights, and the segment number.

## [◆ ](#af18d88c18df4dfb17ceb78c560bd2e61)enable

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::enable |
| --- |

Enable bit for this entry.

Modifying this will also modify the corresponding bit of the MPUENB register.

## [◆ ](#a9dbb164dd9e942b0d2e91621724d81ae)lock

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::lock |
| --- |

Lock bit for this entry.

Usable only if MPULOCKABLE parameter is enabled in processor configuration.

Once set:

- This cannot be cleared until reset.
- This entry can no longer be modified.
- The start address of the next entry also cannot be modified.

## [◆ ](#a09cb878dd936700c64c8d2df10b58ed4)mbz

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::mbz |
| --- |

Must be zero.

## [◆ ](#a0461da13881e2cde2a8607783073eeec)mbz1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::mbz1 |
| --- |

Must be zero (part 1).

## [◆ ](#af4bb525147d4ba54bf46c626b3c0a888)mbz2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::mbz2 |
| --- |

Must be zero (part 2).

## [◆ ](#a1b9764368a50f0674ede7bc3450485c7)memory\_type

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::memory\_type |
| --- |

Memory type associated with this MPU entry.

This dictates the memory type from the start address of this entry, to the start address of next entry.

This affects how the hardware treats the memory, for example, cacheable vs non-cacheable, shareable vs non-shareable. Refer to the Xtensa Instruction Set Architecture (ISA) manual for general description, and the processor manual for processor specific information.

## [◆ ](#a9fa96af81c4af48faa1084cdde720ca9)[struct] [1/2]

| struct { ... } xtensa\_mpu\_entry::p |
| --- |

Individual parts.

## [◆ ](#a32bfc370b92a904abe8fe522afb9a813)[struct] [2/2]

| struct { ... } xtensa\_mpu\_entry::p |
| --- |

Individual parts.

## [◆ ](#a77dc5a2d8512fca38c9c305b722556f5)raw

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::raw |
| --- |

Raw value.

## [◆ ](#a26879b4bb6ec5c2040a864a1286b177f)segment

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::segment |
| --- |

The segment number of this MPU entry.

## [◆ ](#ada352b7ede662f57bb162e5df1f819bd)start\_addr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_mpu\_entry::start\_addr |
| --- |

Start address of this MPU entry.

Effective bits in this portion are affected by the minimum segment size of each MPU entry, ranging from 32 bytes to 4GB.

---

The documentation for this struct was generated from the following file:

- zephyr/arch/xtensa/[mpu.h](xtensa_2mpu_8h_source.md)

- [xtensa\_mpu\_entry](structxtensa__mpu__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
