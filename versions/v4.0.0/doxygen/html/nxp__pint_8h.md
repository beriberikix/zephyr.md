---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nxp__pint_8h.html
original_path: doxygen/html/nxp__pint_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_pint.h File Reference

`#include <fsl_pint.h>`

[Go to the source code of this file.](nxp__pint_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [nxp\_pint\_cb\_t](#a5ceee20d9c423fe9f80e1d72540b4c73)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*user) |

| Enumerations | |
| --- | --- |
| enum | [nxp\_pint\_trigger](#aea62e6522d0de4c0ce63ae04b2d36f7c) {     [NXP\_PINT\_NONE](#aea62e6522d0de4c0ce63ae04b2d36f7ca8594c4bbe2858dd19a176d851a6175c5) = kPINT\_PinIntEnableNone , [NXP\_PINT\_RISING](#aea62e6522d0de4c0ce63ae04b2d36f7ca20ed11aa9c65c91d30b169ae8a754d40) = kPINT\_PinIntEnableRiseEdge , [NXP\_PINT\_FALLING](#aea62e6522d0de4c0ce63ae04b2d36f7caf77211604686c8e8f16616b25b9ada9e) = kPINT\_PinIntEnableFallEdge , [NXP\_PINT\_BOTH](#aea62e6522d0de4c0ce63ae04b2d36f7caabce56e3c8a6ba8801b0700bfbf52ec2) = kPINT\_PinIntEnableBothEdges ,     [NXP\_PINT\_LOW](#aea62e6522d0de4c0ce63ae04b2d36f7ca115385d1645fa1901b7ffeab07ff6ce7) = kPINT\_PinIntEnableLowLevel , [NXP\_PINT\_HIGH](#aea62e6522d0de4c0ce63ae04b2d36f7cad94f208bdf7029063172c88673d28b24) = kPINT\_PinIntEnableHighLevel   } |
|  | Driver for Pin interrupt and pattern match engine in NXP MCUs. [More...](#aea62e6522d0de4c0ce63ae04b2d36f7c) |

| Functions | |
| --- | --- |
| int | [nxp\_pint\_pin\_enable](#abdfe420166b4d28fd7be112b561228bc) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, enum [nxp\_pint\_trigger](#aea62e6522d0de4c0ce63ae04b2d36f7c) trigger, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wake) |
|  | Enable PINT interrupt source. |
| void | [nxp\_pint\_pin\_disable](#a45daffb706e6e51fb805d1bfbd1c4144) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |
|  | disable PINT interrupt source. |
| int | [nxp\_pint\_pin\_set\_callback](#a086336be48bc780034f74dbd5aff0bd9) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [nxp\_pint\_cb\_t](#a5ceee20d9c423fe9f80e1d72540b4c73) cb, void \*data) |
|  | Install PINT callback. |
| void | [nxp\_pint\_pin\_unset\_callback](#ad7ec8dddcc5a404f38d8d5bb16775a9a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |
|  | Remove PINT callback. |

## Typedef Documentation

## [◆ ](#a5ceee20d9c423fe9f80e1d72540b4c73)nxp\_pint\_cb\_t

| typedef void(\* nxp\_pint\_cb\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*user) |
| --- |

## Enumeration Type Documentation

## [◆ ](#aea62e6522d0de4c0ce63ae04b2d36f7c)nxp\_pint\_trigger

| enum [nxp\_pint\_trigger](#aea62e6522d0de4c0ce63ae04b2d36f7c) |
| --- |

Driver for Pin interrupt and pattern match engine in NXP MCUs.

The Pin interrupt and pattern match engine (PINT) supports sourcing inputs from any pins on GPIO ports 0 and 1 of NXP MCUs featuring the module, and generating interrupts based on these inputs. Pin inputs can generate separate interrupts to the NVIC, or be combined using the PINT's boolean logic based pattern match engine. This driver currently only supports the pin interrupt feature of the PINT.

Pin interrupt sources

Pin interrupt sources available for use.

| Enumerator | |
| --- | --- |
| NXP\_PINT\_NONE |  |
| NXP\_PINT\_RISING |  |
| NXP\_PINT\_FALLING |  |
| NXP\_PINT\_BOTH |  |
| NXP\_PINT\_LOW |  |
| NXP\_PINT\_HIGH |  |

## Function Documentation

## [◆ ](#a45daffb706e6e51fb805d1bfbd1c4144)nxp\_pint\_pin\_disable()

| void nxp\_pint\_pin\_disable | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* | ) |  |
| --- | --- | --- | --- | --- | --- |

disable PINT interrupt source.

Parameters
:   | pin | pin interrupt source to disable |
    | --- | --- |

## [◆ ](#abdfe420166b4d28fd7be112b561228bc)nxp\_pint\_pin\_enable()

| int nxp\_pint\_pin\_enable | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
| --- | --- | --- | --- |
|  |  | enum [nxp\_pint\_trigger](#aea62e6522d0de4c0ce63ae04b2d36f7c) | *trigger*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *wake* ) |

Enable PINT interrupt source.

Parameters
:   | pin | pin to use as interrupt source 0-64, corresponding to GPIO0 pin 1 - GPIO1 pin 31) |
    | --- | --- |
    | trigger | one of [nxp\_pint\_trigger](#aea62e6522d0de4c0ce63ae04b2d36f7c) flags |
    | wake | indicates if the pin should wakeup the system |

## [◆ ](#a086336be48bc780034f74dbd5aff0bd9)nxp\_pint\_pin\_set\_callback()

| int nxp\_pint\_pin\_set\_callback | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
| --- | --- | --- | --- |
|  |  | [nxp\_pint\_cb\_t](#a5ceee20d9c423fe9f80e1d72540b4c73) | *cb*, |
|  |  | void \* | *data* ) |

Install PINT callback.

Parameters
:   | pin | interrupt source to install callback for |
    | --- | --- |
    | cb | callback to install |
    | data | user data to include in callback |

Returns
:   0 on success, or negative value on error

## [◆ ](#ad7ec8dddcc5a404f38d8d5bb16775a9a)nxp\_pint\_pin\_unset\_callback()

| void nxp\_pint\_pin\_unset\_callback | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* | ) |  |
| --- | --- | --- | --- | --- | --- |

Remove PINT callback.

Parameters
:   | pin | interrupt source to remove callback for |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [nxp\_pint.h](nxp__pint_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
