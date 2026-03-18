---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structosdp__cmd__buzzer.html
original_path: doxygen/html/structosdp__cmd__buzzer.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_cmd\_buzzer Struct Reference

Sent from CP to control the behaviour of a buzzer in the PD.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reader](#a0e97e1e33eac4f25e5a05586f8135ab3) |
|  | Reader number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [control\_code](#a16d0f385264e247d942367a6a13a77af) |
|  | Control code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [on\_count](#a9082cf0dd2e3e9d31d95051f2952d611) |
|  | The ON duration of the sound, in units of 100 ms. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [off\_count](#ac83cdb57418fc28f11c686e79e811492) |
|  | The OFF duration of the sound, in units of 100 ms. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rep\_count](#a0ea92ffb8ed7527e0373c0530edfb61d) |
|  | The number of times to repeat the ON/OFF cycle; 0: forever. |

## Detailed Description

Sent from CP to control the behaviour of a buzzer in the PD.

## Field Documentation

## [◆ ](#a16d0f385264e247d942367a6a13a77af)control\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_buzzer::control\_code |
| --- |

Control code.

- 0 - no tone
- 1 - off
- 2 - default tone
- 3+ - TBD

## [◆ ](#ac83cdb57418fc28f11c686e79e811492)off\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_buzzer::off\_count |
| --- |

The OFF duration of the sound, in units of 100 ms.

## [◆ ](#a9082cf0dd2e3e9d31d95051f2952d611)on\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_buzzer::on\_count |
| --- |

The ON duration of the sound, in units of 100 ms.

## [◆ ](#a0e97e1e33eac4f25e5a05586f8135ab3)reader

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_buzzer::reader |
| --- |

Reader number.

0 = First Reader, 1 = Second Reader, etc.

## [◆ ](#a0ea92ffb8ed7527e0373c0530edfb61d)rep\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_buzzer::rep\_count |
| --- |

The number of times to repeat the ON/OFF cycle; 0: forever.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_cmd\_buzzer](structosdp__cmd__buzzer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
