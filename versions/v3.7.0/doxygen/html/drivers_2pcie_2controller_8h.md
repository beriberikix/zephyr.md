---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2pcie_2controller_8h.html
original_path: doxygen/html/drivers_2pcie_2controller_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

controller.h File Reference

Public APIs for the PCIe Controllers drivers.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](drivers_2pcie_2controller_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) |
|  | Structure providing callbacks to be implemented for devices that supports the PCI Express Controller API. [More...](structpcie__ctrl__driver__api.md#details) |
| struct | [pcie\_ctrl\_config](structpcie__ctrl__config.md) |
|  | Structure describing a device that supports the PCI Express Controller API. [More...](structpcie__ctrl__config.md#details) |

| Macros | |
| --- | --- |
| #define | [PCIE\_RANGE\_FORMAT](group__pcie__controller__interface.md#ga91525130b94b07187633abd1e017aa61)(node\_id, idx) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [pcie\_ctrl\_conf\_read\_t](group__pcie__controller__interface.md#gac3d0f7e90bcc30996ce23324d2d7356a)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Function called to read a 32-bit word from an endpoint's configuration space. |
| typedef void(\* | [pcie\_ctrl\_conf\_write\_t](group__pcie__controller__interface.md#ga3241acc7de4af2b73cf3f47a25349109)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Function called to write a 32-bit word to an endpoint's configuration space. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pcie\_ctrl\_region\_allocate\_t](group__pcie__controller__interface.md#ga62ce18e7495256c148168b773eabd37d)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bar\_size, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_bus\_addr) |
|  | Function called to allocate a memory region subset for an endpoint Base Address Register. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pcie\_ctrl\_region\_get\_allocate\_base\_t](group__pcie__controller__interface.md#gaa9d5bd27c841e36f65e65dec0b057e9a)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_base\_addr) |
|  | Function called to get the current allocation base of a memory region subset for an endpoint Base Address Register. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pcie\_ctrl\_region\_translate\_t](group__pcie__controller__interface.md#gab144356b1c3ec3754aae0008634f2d2f)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) bar\_bus\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_addr) |
|  | Function called to translate an endpoint Base Address Register bus-centric address into Physical address. |

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_generic\_ctrl\_conf\_read](group__pcie__controller__interface.md#gaa16b59c39f273a654b72d9e209f3ba2e) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) cfg\_addr, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read a 32-bit word from a Memory-Mapped endpoint's configuration space. |
| void | [pcie\_generic\_ctrl\_conf\_write](group__pcie__controller__interface.md#ga709ecedbd0585b4eb17fc2f5923a8f61) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) cfg\_addr, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write a 32-bit word to a Memory-Mapped endpoint's configuration space. |
| void | [pcie\_generic\_ctrl\_enumerate](group__pcie__controller__interface.md#ga75910ea4255a740b57e35a596a90b7bb) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf\_start) |
|  | Start PCIe Endpoints enumeration. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_ctrl\_conf\_read](group__pcie__controller__interface.md#ga1d978b8075191d6e571349684c731a43) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read a 32-bit word from an endpoint's configuration space. |
| static void | [pcie\_ctrl\_conf\_write](group__pcie__controller__interface.md#ga5cfe01762e5af8dc0cc5fbd550ff7e74) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write a 32-bit word to an endpoint's configuration space. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_ctrl\_region\_allocate](group__pcie__controller__interface.md#ga1de030e2e8b07509d75de5a348297f42) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bar\_size, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_bus\_addr) |
|  | Allocate a memory region subset for an endpoint Base Address Register. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_ctrl\_region\_get\_allocate\_base](group__pcie__controller__interface.md#gae7c109ca138adfd906fef5b6f3dca385) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_base\_addr) |
|  | Function called to get the current allocation base of a memory region subset for an endpoint Base Address Register. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_ctrl\_region\_translate](group__pcie__controller__interface.md#gae6fa104ea2cc85912ebb1cfe0a1a3ddf) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) bar\_bus\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_addr) |
|  | Translate an endpoint Base Address Register bus-centric address into Physical address. |

## Detailed Description

Public APIs for the PCIe Controllers drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [controller.h](drivers_2pcie_2controller_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
