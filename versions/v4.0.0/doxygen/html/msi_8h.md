---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/msi_8h.html
original_path: doxygen/html/msi_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msi.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/drivers/pcie/pcie.h](drivers_2pcie_2pcie_8h_source.md)>`

[Go to the source code of this file.](msi_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [msix\_vector](structmsix__vector.md) |
| struct | [msi\_vector](structmsi__vector.md) |

| Macros | |
| --- | --- |
| #define | [PCIE\_MSI\_MCR](group__pcie__host__msi__interface.md#ga6363ff201cdaf89434be7f7976218132)   0U |
| #define | [PCIE\_MSI\_MCR\_EN](group__pcie__host__msi__interface.md#ga6d4aa888ca0930998d49abfc21dfc4a0)   0x00010000U /\* enable MSI \*/ |
| #define | [PCIE\_MSI\_MCR\_MMC](group__pcie__host__msi__interface.md#ga273df548ce103502c69a2aaf32940270)   0x000E0000U /\* Multi Messages Capable mask \*/ |
| #define | [PCIE\_MSI\_MCR\_MMC\_SHIFT](group__pcie__host__msi__interface.md#gab0b4bed4d96cc135c38e1762922a6dfc)   17 |
| #define | [PCIE\_MSI\_MCR\_MME](group__pcie__host__msi__interface.md#gae34c85b4346402d14ab7ade656f7874f)   0x00700000U /\* mask of # of enabled IRQs \*/ |
| #define | [PCIE\_MSI\_MCR\_MME\_SHIFT](group__pcie__host__msi__interface.md#ga933abb134aec549761f835f84c0caf53)   20 |
| #define | [PCIE\_MSI\_MCR\_64](group__pcie__host__msi__interface.md#ga8496d1040f5f0388130f3550f27dbf67)   0x00800000U /\* 64-bit MSI \*/ |
| #define | [PCIE\_MSI\_MAP0](group__pcie__host__msi__interface.md#gaf5b03bc395082366b0f4d8a6860753a3)   1U |
| #define | [PCIE\_MSI\_MAP1\_64](group__pcie__host__msi__interface.md#ga7dc1045e58e9e99029d2876adf373f61)   2U |
| #define | [PCIE\_MSI\_MDR\_32](group__pcie__host__msi__interface.md#ga72a3907f5cfba38103db25a8065efe5d)   2U |
| #define | [PCIE\_MSI\_MDR\_64](group__pcie__host__msi__interface.md#ga599d70864c7a8a8d12c56c302f963c75)   3U |
| #define | [PCIE\_MSIX\_MCR](group__pcie__host__msi__interface.md#ga3f684fa1e9eaf5aad844b7f5c5232adb)   0U |
| #define | [PCIE\_MSIX\_MCR\_EN](group__pcie__host__msi__interface.md#gaf309bab15a0118cbc39b3a52354a8067)   0x80000000U /\* Enable MSI-X \*/ |
| #define | [PCIE\_MSIX\_MCR\_FMASK](group__pcie__host__msi__interface.md#ga7186a5d811ab5f486c7eddbb0b2ecffe)   0x40000000U /\* Function Mask \*/ |
| #define | [PCIE\_MSIX\_MCR\_TSIZE](group__pcie__host__msi__interface.md#ga20e8351fd64d8308ff0c94ba02e7c688)   0x07FF0000U /\* Table size mask \*/ |
| #define | [PCIE\_MSIX\_MCR\_TSIZE\_SHIFT](group__pcie__host__msi__interface.md#gabb2e51e10229fe1b5953548a96892005)   16 |
| #define | [PCIE\_MSIR\_TABLE\_ENTRY\_SIZE](group__pcie__host__msi__interface.md#ga0a403e859ea16d24267fed463c214e22)   16 |
| #define | [PCIE\_MSIX\_TR](group__pcie__host__msi__interface.md#ga701825e23994bdf4da4a86b8776c3248)   1U |
| #define | [PCIE\_MSIX\_TR\_BIR](group__pcie__host__msi__interface.md#ga13e9132823fa2361ab25e53c75aa8896)   0x00000007U /\* Table BIR mask \*/ |
| #define | [PCIE\_MSIX\_TR\_OFFSET](group__pcie__host__msi__interface.md#ga44875f9af4865a82438a6a4ec714c6a9)   0xFFFFFFF8U /\* Offset mask \*/ |
| #define | [PCIE\_MSIX\_PBA](group__pcie__host__msi__interface.md#ga6e74db681568d7103100036233e3467d)   2U |
| #define | [PCIE\_MSIX\_PBA\_BIR](group__pcie__host__msi__interface.md#gae259720d8a4af8b2aba0625b41d21d40)   0x00000007U /\* PBA BIR mask \*/ |
| #define | [PCIE\_MSIX\_PBA\_OFFSET](group__pcie__host__msi__interface.md#ga388b54bd3c60cb46940e1b1defc42dad)   0xFFFFFFF8U /\* Offset mask \*/ |
| #define | [PCIE\_VTBL\_MA](group__pcie__host__msi__interface.md#ga33adc70c295b3ba887529fc8f73f6cb4)   0U /\* Msg Address offset \*/ |
| #define | [PCIE\_VTBL\_MUA](group__pcie__host__msi__interface.md#ga5711b93de9c485b321a9dcd01ac53b05)   4U /\* Msg Upper Address offset \*/ |
| #define | [PCIE\_VTBL\_MD](group__pcie__host__msi__interface.md#gaf35ee6cb30ff29ae0f6804f3328a1d1d)   8U /\* Msg Data offset \*/ |
| #define | [PCIE\_VTBL\_VCTRL](group__pcie__host__msi__interface.md#gae354a23e4f62342cfd4e2572068b51a3)   12U /\* Vector control offset \*/ |

| Typedefs | |
| --- | --- |
| typedef struct [msi\_vector](structmsi__vector.md) | [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) |

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_msi\_map](group__pcie__host__msi__interface.md#ga2cdf2a32cb4c6e4d68290a1e9020f4ee) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector) |
|  | Compute the target address for an MSI posted write. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pcie\_msi\_mdr](group__pcie__host__msi__interface.md#gae89ee2177016ab1df94c7f453eb5c25d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector) |
|  | Compute the data for an MSI posted write. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_msi\_enable](group__pcie__host__msi__interface.md#ga57226ef41cee2008a2c92098dd52af6b) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vectors, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Configure the given PCI endpoint to generate MSIs. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_is\_msi](group__pcie__host__msi__interface.md#gac16ef7e19d7584aa2fc3a839b1b8fb01) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Check if the given PCI endpoint supports MSI/MSI-X. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [msi.h](msi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
