---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcan__filter.html
original_path: doxygen/html/structcan__filter.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_filter Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [CAN Interface](group__can__interface.md)

CAN filter structure.
[More...](#details)

`#include <[can.h](drivers_2can_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#adf2b18eab11d360780707478a1f624b9) |
|  | CAN identifier to match. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mask](#a15632117f3f031fbbeb28ef562f9ac94) |
|  | CAN identifier matching mask. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a7616e21f33be5fb43094d44530a1c5de) |
|  | Flags. |

## Detailed Description

CAN filter structure.

## Field Documentation

## [◆ ](#a7616e21f33be5fb43094d44530a1c5de)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_filter::flags |
| --- |

Flags.

See also
:   [CAN\_FILTER\_FLAGS](group__can__interface.md#CAN_FILTER_FLAGS "CAN_FILTER_FLAGS").

## [◆ ](#adf2b18eab11d360780707478a1f624b9)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_filter::id |
| --- |

CAN identifier to match.

## [◆ ](#a15632117f3f031fbbeb28ef562f9ac94)mask

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_filter::mask |
| --- |

CAN identifier matching mask.

If a bit in this mask is 0, the value of the corresponding bit in the [id](#adf2b18eab11d360780707478a1f624b9) field is ignored by the filter.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[can.h](drivers_2can_8h_source.md)

- [can\_filter](structcan__filter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
