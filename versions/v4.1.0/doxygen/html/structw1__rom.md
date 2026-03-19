---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structw1__rom.html
original_path: doxygen/html/structw1__rom.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

w1\_rom Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [1-Wire Interface](group__w1__interface.md) » [1-Wire network layer](group__w1__network.md)

[w1\_rom](structw1__rom.md "w1_rom struct.") struct.
[More...](#details)

`#include <[w1.h](w1_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [family](#adc7f4f9fca172392b11864a17424a14c) |
|  | The 1-Wire family code identifying the slave device type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [serial](#a134ee6d6e5e5eb711caf59449d11732e) [6] |
|  | The serial together with the family code composes the unique 56-bit id. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc](#a73d85d7ce0ef671027c910b9b7a54165) |
|  | 8-bit checksum of the 56-bit unique id. |

## Detailed Description

[w1\_rom](structw1__rom.md "w1_rom struct.") struct.

## Field Documentation

## [◆ ](#a73d85d7ce0ef671027c910b9b7a54165)crc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) w1\_rom::crc |
| --- |

8-bit checksum of the 56-bit unique id.

## [◆ ](#adc7f4f9fca172392b11864a17424a14c)family

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) w1\_rom::family |
| --- |

The 1-Wire family code identifying the slave device type.

An incomplete list of family codes is available at: [https://www.analog.com/en/resources/technical-articles/1wire-software-resource-guide-device-description.html](https://www.analog.com/en/resources/technical-articles/1wire-software-resource-guide-device-description.html) others are documented in the respective device data sheet.

## [◆ ](#a134ee6d6e5e5eb711caf59449d11732e)serial

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) w1\_rom::serial[6] |
| --- |

The serial together with the family code composes the unique 56-bit id.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[w1.h](w1_8h_source.md)

- [w1\_rom](structw1__rom.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
