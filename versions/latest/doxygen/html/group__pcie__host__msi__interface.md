---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__pcie__host__msi__interface.html
original_path: doxygen/html/group__pcie__host__msi__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PCIe Host MSI Interface

[Device Driver APIs](group__io__interfaces.md) » [PCIe Host Interface](group__pcie__host__interface.md)

PCIe Host MSI Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [msix\_vector](structmsix__vector.md) |
| struct | [msi\_vector](structmsi__vector.md) |

| Macros | |
| --- | --- |
| #define | [PCIE\_MSI\_MCR](#ga6363ff201cdaf89434be7f7976218132)   0U |
| #define | [PCIE\_MSI\_MCR\_EN](#ga6d4aa888ca0930998d49abfc21dfc4a0)   0x00010000U /\* enable MSI \*/ |
| #define | [PCIE\_MSI\_MCR\_MMC](#ga273df548ce103502c69a2aaf32940270)   0x000E0000U /\* Multi Messages Capable mask \*/ |
| #define | [PCIE\_MSI\_MCR\_MMC\_SHIFT](#gab0b4bed4d96cc135c38e1762922a6dfc)   17 |
| #define | [PCIE\_MSI\_MCR\_MME](#gae34c85b4346402d14ab7ade656f7874f)   0x00700000U /\* mask of # of enabled IRQs \*/ |
| #define | [PCIE\_MSI\_MCR\_MME\_SHIFT](#ga933abb134aec549761f835f84c0caf53)   20 |
| #define | [PCIE\_MSI\_MCR\_64](#ga8496d1040f5f0388130f3550f27dbf67)   0x00800000U /\* 64-bit MSI \*/ |
| #define | [PCIE\_MSI\_MAP0](#gaf5b03bc395082366b0f4d8a6860753a3)   1U |
| #define | [PCIE\_MSI\_MAP1\_64](#ga7dc1045e58e9e99029d2876adf373f61)   2U |
| #define | [PCIE\_MSI\_MDR\_32](#ga72a3907f5cfba38103db25a8065efe5d)   2U |
| #define | [PCIE\_MSI\_MDR\_64](#ga599d70864c7a8a8d12c56c302f963c75)   3U |
| #define | [PCIE\_MSIX\_MCR](#ga3f684fa1e9eaf5aad844b7f5c5232adb)   0U |
| #define | [PCIE\_MSIX\_MCR\_EN](#gaf309bab15a0118cbc39b3a52354a8067)   0x80000000U /\* Enable MSI-X \*/ |
| #define | [PCIE\_MSIX\_MCR\_FMASK](#ga7186a5d811ab5f486c7eddbb0b2ecffe)   0x40000000U /\* Function Mask \*/ |
| #define | [PCIE\_MSIX\_MCR\_TSIZE](#ga20e8351fd64d8308ff0c94ba02e7c688)   0x07FF0000U /\* Table size mask \*/ |
| #define | [PCIE\_MSIX\_MCR\_TSIZE\_SHIFT](#gabb2e51e10229fe1b5953548a96892005)   16 |
| #define | [PCIE\_MSIR\_TABLE\_ENTRY\_SIZE](#ga0a403e859ea16d24267fed463c214e22)   16 |
| #define | [PCIE\_MSIX\_TR](#ga701825e23994bdf4da4a86b8776c3248)   1U |
| #define | [PCIE\_MSIX\_TR\_BIR](#ga13e9132823fa2361ab25e53c75aa8896)   0x00000007U /\* Table BIR mask \*/ |
| #define | [PCIE\_MSIX\_TR\_OFFSET](#ga44875f9af4865a82438a6a4ec714c6a9)   0xFFFFFFF8U /\* Offset mask \*/ |
| #define | [PCIE\_MSIX\_PBA](#ga6e74db681568d7103100036233e3467d)   2U |
| #define | [PCIE\_MSIX\_PBA\_BIR](#gae259720d8a4af8b2aba0625b41d21d40)   0x00000007U /\* PBA BIR mask \*/ |
| #define | [PCIE\_MSIX\_PBA\_OFFSET](#ga388b54bd3c60cb46940e1b1defc42dad)   0xFFFFFFF8U /\* Offset mask \*/ |
| #define | [PCIE\_VTBL\_MA](#ga33adc70c295b3ba887529fc8f73f6cb4)   0U /\* Msg Address offset \*/ |
| #define | [PCIE\_VTBL\_MUA](#ga5711b93de9c485b321a9dcd01ac53b05)   4U /\* Msg Upper Address offset \*/ |
| #define | [PCIE\_VTBL\_MD](#gaf35ee6cb30ff29ae0f6804f3328a1d1d)   8U /\* Msg Data offset \*/ |
| #define | [PCIE\_VTBL\_VCTRL](#gae354a23e4f62342cfd4e2572068b51a3)   12U /\* Vector control offset \*/ |

| Typedefs | |
| --- | --- |
| typedef struct [msi\_vector](structmsi__vector.md) | [msi\_vector\_t](#ga9ede6a7a472ee62f0975256a1b5f1231) |

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_msi\_map](#ga2cdf2a32cb4c6e4d68290a1e9020f4ee) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [msi\_vector\_t](#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector) |
|  | Compute the target address for an MSI posted write. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pcie\_msi\_mdr](#gae89ee2177016ab1df94c7f453eb5c25d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [msi\_vector\_t](#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector) |
|  | Compute the data for an MSI posted write. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_msi\_enable](#ga57226ef41cee2008a2c92098dd52af6b) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [msi\_vector\_t](#ga9ede6a7a472ee62f0975256a1b5f1231) \*vectors, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Configure the given PCI endpoint to generate MSIs. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_is\_msi](#gac16ef7e19d7584aa2fc3a839b1b8fb01) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Check if the given PCI endpoint supports MSI/MSI-X. |

## Detailed Description

PCIe Host MSI Interface.

## Macro Definition Documentation

## [◆ ](#gaf5b03bc395082366b0f4d8a6860753a3)PCIE\_MSI\_MAP0

| #define PCIE\_MSI\_MAP0   1U |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga7dc1045e58e9e99029d2876adf373f61)PCIE\_MSI\_MAP1\_64

| #define PCIE\_MSI\_MAP1\_64   2U |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga6363ff201cdaf89434be7f7976218132)PCIE\_MSI\_MCR

| #define PCIE\_MSI\_MCR   0U |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga8496d1040f5f0388130f3550f27dbf67)PCIE\_MSI\_MCR\_64

| #define PCIE\_MSI\_MCR\_64   0x00800000U /\* 64-bit MSI \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga6d4aa888ca0930998d49abfc21dfc4a0)PCIE\_MSI\_MCR\_EN

| #define PCIE\_MSI\_MCR\_EN   0x00010000U /\* enable MSI \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga273df548ce103502c69a2aaf32940270)PCIE\_MSI\_MCR\_MMC

| #define PCIE\_MSI\_MCR\_MMC   0x000E0000U /\* Multi Messages Capable mask \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#gab0b4bed4d96cc135c38e1762922a6dfc)PCIE\_MSI\_MCR\_MMC\_SHIFT

| #define PCIE\_MSI\_MCR\_MMC\_SHIFT   17 |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#gae34c85b4346402d14ab7ade656f7874f)PCIE\_MSI\_MCR\_MME

| #define PCIE\_MSI\_MCR\_MME   0x00700000U /\* mask of # of enabled IRQs \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga933abb134aec549761f835f84c0caf53)PCIE\_MSI\_MCR\_MME\_SHIFT

| #define PCIE\_MSI\_MCR\_MME\_SHIFT   20 |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga72a3907f5cfba38103db25a8065efe5d)PCIE\_MSI\_MDR\_32

| #define PCIE\_MSI\_MDR\_32   2U |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga599d70864c7a8a8d12c56c302f963c75)PCIE\_MSI\_MDR\_64

| #define PCIE\_MSI\_MDR\_64   3U |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga0a403e859ea16d24267fed463c214e22)PCIE\_MSIR\_TABLE\_ENTRY\_SIZE

| #define PCIE\_MSIR\_TABLE\_ENTRY\_SIZE   16 |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga3f684fa1e9eaf5aad844b7f5c5232adb)PCIE\_MSIX\_MCR

| #define PCIE\_MSIX\_MCR   0U |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#gaf309bab15a0118cbc39b3a52354a8067)PCIE\_MSIX\_MCR\_EN

| #define PCIE\_MSIX\_MCR\_EN   0x80000000U /\* Enable MSI-X \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga7186a5d811ab5f486c7eddbb0b2ecffe)PCIE\_MSIX\_MCR\_FMASK

| #define PCIE\_MSIX\_MCR\_FMASK   0x40000000U /\* Function Mask \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga20e8351fd64d8308ff0c94ba02e7c688)PCIE\_MSIX\_MCR\_TSIZE

| #define PCIE\_MSIX\_MCR\_TSIZE   0x07FF0000U /\* Table size mask \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#gabb2e51e10229fe1b5953548a96892005)PCIE\_MSIX\_MCR\_TSIZE\_SHIFT

| #define PCIE\_MSIX\_MCR\_TSIZE\_SHIFT   16 |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga6e74db681568d7103100036233e3467d)PCIE\_MSIX\_PBA

| #define PCIE\_MSIX\_PBA   2U |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#gae259720d8a4af8b2aba0625b41d21d40)PCIE\_MSIX\_PBA\_BIR

| #define PCIE\_MSIX\_PBA\_BIR   0x00000007U /\* PBA BIR mask \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga388b54bd3c60cb46940e1b1defc42dad)PCIE\_MSIX\_PBA\_OFFSET

| #define PCIE\_MSIX\_PBA\_OFFSET   0xFFFFFFF8U /\* Offset mask \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga701825e23994bdf4da4a86b8776c3248)PCIE\_MSIX\_TR

| #define PCIE\_MSIX\_TR   1U |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga13e9132823fa2361ab25e53c75aa8896)PCIE\_MSIX\_TR\_BIR

| #define PCIE\_MSIX\_TR\_BIR   0x00000007U /\* Table BIR mask \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga44875f9af4865a82438a6a4ec714c6a9)PCIE\_MSIX\_TR\_OFFSET

| #define PCIE\_MSIX\_TR\_OFFSET   0xFFFFFFF8U /\* Offset mask \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga33adc70c295b3ba887529fc8f73f6cb4)PCIE\_VTBL\_MA

| #define PCIE\_VTBL\_MA   0U /\* Msg Address offset \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#gaf35ee6cb30ff29ae0f6804f3328a1d1d)PCIE\_VTBL\_MD

| #define PCIE\_VTBL\_MD   8U /\* Msg Data offset \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#ga5711b93de9c485b321a9dcd01ac53b05)PCIE\_VTBL\_MUA

| #define PCIE\_VTBL\_MUA   4U /\* Msg Upper Address offset \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## [◆ ](#gae354a23e4f62342cfd4e2572068b51a3)PCIE\_VTBL\_VCTRL

| #define PCIE\_VTBL\_VCTRL   12U /\* Vector control offset \*/ |
| --- |

`#include <[msi.h](msi_8h.md)>`

## Typedef Documentation

## [◆ ](#ga9ede6a7a472ee62f0975256a1b5f1231)msi\_vector\_t

| typedef struct [msi\_vector](structmsi__vector.md) [msi\_vector\_t](#ga9ede6a7a472ee62f0975256a1b5f1231) |
| --- |

`#include <[msi.h](msi_8h.md)>`

## Function Documentation

## [◆ ](#gac16ef7e19d7584aa2fc3a839b1b8fb01)pcie\_is\_msi()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_is\_msi | ( | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[msi.h](msi_8h.md)>`

Check if the given PCI endpoint supports MSI/MSI-X.

Parameters
:   | bdf | the target PCI endpoint |
    | --- | --- |

Returns
:   true if the endpoint support MSI/MSI-X

## [◆ ](#ga57226ef41cee2008a2c92098dd52af6b)pcie\_msi\_enable()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_msi\_enable | ( | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [msi\_vector\_t](#ga9ede6a7a472ee62f0975256a1b5f1231) \* | *vectors*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *n\_vector*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[msi.h](msi_8h.md)>`

Configure the given PCI endpoint to generate MSIs.

Parameters
:   | bdf | the target PCI endpoint |
    | --- | --- |
    | vectors | an array of allocated vector(s) |
    | n\_vector | the size of the vector array |
    | irq | The IRQ we wish to trigger via MSI. |

Returns
:   true if the endpoint supports MSI, false otherwise.

## [◆ ](#ga2cdf2a32cb4c6e4d68290a1e9020f4ee)pcie\_msi\_map()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcie\_msi\_map | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [msi\_vector\_t](#ga9ede6a7a472ee62f0975256a1b5f1231) \* | *vector*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *n\_vector* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[msi.h](msi_8h.md)>`

Compute the target address for an MSI posted write.

This function is exported by the arch, board or SoC code.

Parameters
:   | irq | The IRQ we wish to trigger via MSI. |
    | --- | --- |
    | vector | The vector for which you want the address (or NULL) |
    | n\_vector | the size of the vector array |

Returns
:   A (32-bit) value for the MSI MAP register.

## [◆ ](#gae89ee2177016ab1df94c7f453eb5c25d)pcie\_msi\_mdr()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pcie\_msi\_mdr | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [msi\_vector\_t](#ga9ede6a7a472ee62f0975256a1b5f1231) \* | *vector* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[msi.h](msi_8h.md)>`

Compute the data for an MSI posted write.

This function is exported by the arch, board or SoC code.

Parameters
:   | irq | The IRQ we wish to trigger via MSI. |
    | --- | --- |
    | vector | The vector for which you want the data (or NULL) |

Returns
:   A (16-bit) value for MSI MDR register.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
