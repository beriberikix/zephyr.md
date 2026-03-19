---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__aics__register__param.html
original_path: doxygen/html/structbt__aics__register__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_aics\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Audio Input Control Service (AICS)](group__bt__aics.md)

Structure for initializing a Audio Input Control Service instance.
[More...](#details)

`#include <[aics.h](aics_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [gain](#a966e9e99544392cdfac264ee6effcc7c) |
|  | Initial audio input gain (-128 to 127). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mute](#ac95e17bc53539deeab5d161ca1b08194) |
|  | Initial audio input mute state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [gain\_mode](#a3658ed1900a44eef84b5602e567fe085) |
|  | Initial audio input mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [units](#a4b2eae9a9716629e9c56ee3e6dc05e44) |
|  | Initial audio input gain units (N \* 0.1 dB). |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [min\_gain](#aac91095a831fe540ee356eb9b9d402d8) |
|  | Initial audio input minimum gain. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [max\_gain](#aa139122e2710d9ec28ec015692545dda) |
|  | Initial audio input maximum gain. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#ad6afebea920fa4c168498ca11778ea7d) |
|  | Initial audio input type. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [status](#a46437f4540d226ce3fbc470448f36e1f) |
|  | Initial audio input status (active/inactive). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [desc\_writable](#acc408a0318b94cdc952ef7d6682e5705) |
|  | Boolean to set whether the description is writable by clients. |
| char \* | [description](#af99d31215008eb201c488a5b1107e009) |
|  | Initial audio input description. |
| struct [bt\_aics\_cb](structbt__aics__cb.md) \* | [cb](#a6c961cde10dbfbaaa26bbc2b5c867001) |
|  | Pointer to the callback structure. |

## Detailed Description

Structure for initializing a Audio Input Control Service instance.

## Field Documentation

## [◆ ](#a6c961cde10dbfbaaa26bbc2b5c867001)cb

| struct [bt\_aics\_cb](structbt__aics__cb.md)\* bt\_aics\_register\_param::cb |
| --- |

Pointer to the callback structure.

## [◆ ](#acc408a0318b94cdc952ef7d6682e5705)desc\_writable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_aics\_register\_param::desc\_writable |
| --- |

Boolean to set whether the description is writable by clients.

## [◆ ](#af99d31215008eb201c488a5b1107e009)description

| char\* bt\_aics\_register\_param::description |
| --- |

Initial audio input description.

## [◆ ](#a966e9e99544392cdfac264ee6effcc7c)gain

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_aics\_register\_param::gain |
| --- |

Initial audio input gain (-128 to 127).

## [◆ ](#a3658ed1900a44eef84b5602e567fe085)gain\_mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_aics\_register\_param::gain\_mode |
| --- |

Initial audio input mode.

## [◆ ](#aa139122e2710d9ec28ec015692545dda)max\_gain

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_aics\_register\_param::max\_gain |
| --- |

Initial audio input maximum gain.

## [◆ ](#aac91095a831fe540ee356eb9b9d402d8)min\_gain

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_aics\_register\_param::min\_gain |
| --- |

Initial audio input minimum gain.

## [◆ ](#ac95e17bc53539deeab5d161ca1b08194)mute

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_aics\_register\_param::mute |
| --- |

Initial audio input mute state.

## [◆ ](#a46437f4540d226ce3fbc470448f36e1f)status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_aics\_register\_param::status |
| --- |

Initial audio input status (active/inactive).

## [◆ ](#ad6afebea920fa4c168498ca11778ea7d)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_aics\_register\_param::type |
| --- |

Initial audio input type.

## [◆ ](#a4b2eae9a9716629e9c56ee3e6dc05e44)units

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_aics\_register\_param::units |
| --- |

Initial audio input gain units (N \* 0.1 dB).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[aics.h](aics_8h_source.md)

- [bt\_aics\_register\_param](structbt__aics__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
