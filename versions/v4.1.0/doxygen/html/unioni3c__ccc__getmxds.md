---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unioni3c__ccc__getmxds.html
original_path: doxygen/html/unioni3c__ccc__getmxds.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_getmxds Union Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for GETMXDS CCC (Get Max Data Speed).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [maxwr](#a9307643fd53554053b38cda5a0663a13) |  |
|  | maxWr [More...](#a9307643fd53554053b38cda5a0663a13) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [maxrd](#a668e1ed30b96a40534d96e4b56ce7e98) |  |
|  | maxRd [More...](#a668e1ed30b96a40534d96e4b56ce7e98) |
| } | [fmt1](#a242470090b40e40f0b0febfba966d766) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [maxwr](#a9307643fd53554053b38cda5a0663a13) |  |
|  | maxWr [More...](#a9307643fd53554053b38cda5a0663a13) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [maxrd](#a668e1ed30b96a40534d96e4b56ce7e98) |  |
|  | maxRd [More...](#a668e1ed30b96a40534d96e4b56ce7e98) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [maxrdturn](#a3782b5dce0db847362b9413a02d90baa) [3] |  |
|  | Maximum Read Turnaround Time in microsecond. [More...](#a3782b5dce0db847362b9413a02d90baa) |
| } | [fmt2](#adfb70b06d5e769fccc7630a356067fcd) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [wrrdturn](#aa3c5a9fa7bc805d4cd63cb3ba774a808) [5] |  |
|  | Defining Byte 0x00: WRRDTURN. [More...](#aa3c5a9fa7bc805d4cd63cb3ba774a808) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [crhdly1](#ad55160abc13a3ad04d5d6f827714f48b) |  |
|  | Defining Byte 0x91: CRHDLY. [More...](#ad55160abc13a3ad04d5d6f827714f48b) |
| } | [fmt3](#a6bb902a7335f2244365cde9782659dce) |

## Detailed Description

Payload for GETMXDS CCC (Get Max Data Speed).

## Field Documentation

## [◆ ](#ad55160abc13a3ad04d5d6f827714f48b)crhdly1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getmxds::crhdly1 |
| --- |

Defining Byte 0x91: CRHDLY.

- Bit[2]: Set Bus Activity State
- Bit[1:0]: Controller Handoff Activity State

## [◆ ](#a242470090b40e40f0b0febfba966d766)[struct]

| struct { ... } i3c\_ccc\_getmxds::fmt1 |
| --- |

## [◆ ](#adfb70b06d5e769fccc7630a356067fcd)[struct]

| struct { ... } i3c\_ccc\_getmxds::fmt2 |
| --- |

## [◆ ](#a6bb902a7335f2244365cde9782659dce)[struct]

| struct { ... } i3c\_ccc\_getmxds::fmt3 |
| --- |

## [◆ ](#a668e1ed30b96a40534d96e4b56ce7e98)maxrd

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getmxds::maxrd |
| --- |

maxRd

## [◆ ](#a3782b5dce0db847362b9413a02d90baa)maxrdturn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getmxds::maxrdturn[3] |
| --- |

Maximum Read Turnaround Time in microsecond.

This is in little-endian where first byte is LSB.

## [◆ ](#a9307643fd53554053b38cda5a0663a13)maxwr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getmxds::maxwr |
| --- |

maxWr

## [◆ ](#aa3c5a9fa7bc805d4cd63cb3ba774a808)wrrdturn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getmxds::wrrdturn[5] |
| --- |

Defining Byte 0x00: WRRDTURN.

See also
:   [i3c\_ccc\_getmxds::fmt2](#adfb70b06d5e769fccc7630a356067fcd)

---

The documentation for this union was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
