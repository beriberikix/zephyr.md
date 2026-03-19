---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structosdp__cmd__output.html
original_path: doxygen/html/structosdp__cmd__output.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_cmd\_output Struct Reference

Command sent from CP to Control digital output of PD.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [output\_no](#af5e1d55c987dd82ed4959f251a811846) |
|  | Output number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [control\_code](#a1037244ed5f7c78eab51d6c08130b5d0) |
|  | Control code. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timer\_count](#a4cd89d5c683b31d0e8eaf007443703a6) |
|  | Time in units of 100 ms. |

## Detailed Description

Command sent from CP to Control digital output of PD.

## Field Documentation

## [◆ ](#a1037244ed5f7c78eab51d6c08130b5d0)control\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_output::control\_code |
| --- |

Control code.

- 0 - NOP – do not alter this output
- 1 - set the permanent state to OFF, abort timed operation (if any)
- 2 - set the permanent state to ON, abort timed operation (if any)
- 3 - set the permanent state to OFF, allow timed operation to complete
- 4 - set the permanent state to ON, allow timed operation to complete
- 5 - set the temporary state to ON, resume perm state on timeout
- 6 - set the temporary state to OFF, resume permanent state on timeout

## [◆ ](#af5e1d55c987dd82ed4959f251a811846)output\_no

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_output::output\_no |
| --- |

Output number.

0 = First Output, 1 = Second Output, etc.

## [◆ ](#a4cd89d5c683b31d0e8eaf007443703a6)timer\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) osdp\_cmd\_output::timer\_count |
| --- |

Time in units of 100 ms.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_cmd\_output](structosdp__cmd__output.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
