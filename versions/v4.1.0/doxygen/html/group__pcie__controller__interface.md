---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__pcie__controller__interface.html
original_path: doxygen/html/group__pcie__controller__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PCI Express Controller Interface

[Device Driver APIs](group__io__interfaces.md)

PCI Express Controller Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [pcie\_ctrl\_driver\_api](structpcie__ctrl__driver__api.md) |
|  | Structure providing callbacks to be implemented for devices that supports the PCI Express Controller API. [More...](structpcie__ctrl__driver__api.md#details) |
| struct | [pcie\_ctrl\_config](structpcie__ctrl__config.md) |
|  | Structure describing a device that supports the PCI Express Controller API. [More...](structpcie__ctrl__config.md#details) |

| Macros | |
| --- | --- |
| #define | [PCIE\_RANGE\_FORMAT](#ga91525130b94b07187633abd1e017aa61)(node\_id, idx) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [pcie\_ctrl\_conf\_read\_t](#gac3d0f7e90bcc30996ce23324d2d7356a)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Function called to read a 32-bit word from an endpoint's configuration space. |
| typedef void(\* | [pcie\_ctrl\_conf\_write\_t](#ga3241acc7de4af2b73cf3f47a25349109)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Function called to write a 32-bit word to an endpoint's configuration space. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pcie\_ctrl\_region\_allocate\_t](#ga62ce18e7495256c148168b773eabd37d)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bar\_size, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_bus\_addr) |
|  | Function called to allocate a memory region subset for an endpoint Base Address Register. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pcie\_ctrl\_region\_get\_allocate\_base\_t](#gaa9d5bd27c841e36f65e65dec0b057e9a)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_base\_addr) |
|  | Function called to get the current allocation base of a memory region subset for an endpoint Base Address Register. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pcie\_ctrl\_region\_translate\_t](#gab144356b1c3ec3754aae0008634f2d2f)) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) bar\_bus\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_addr) |
|  | Function called to translate an endpoint Base Address Register bus-centric address into Physical address. |

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_generic\_ctrl\_conf\_read](#gaa16b59c39f273a654b72d9e209f3ba2e) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) cfg\_addr, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read a 32-bit word from a Memory-Mapped endpoint's configuration space. |
| void | [pcie\_generic\_ctrl\_conf\_write](#ga709ecedbd0585b4eb17fc2f5923a8f61) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) cfg\_addr, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write a 32-bit word to a Memory-Mapped endpoint's configuration space. |
| void | [pcie\_generic\_ctrl\_enumerate](#ga75910ea4255a740b57e35a596a90b7bb) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf\_start) |
|  | Start PCIe Endpoints enumeration. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_ctrl\_conf\_read](#ga1d978b8075191d6e571349684c731a43) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read a 32-bit word from an endpoint's configuration space. |
| static void | [pcie\_ctrl\_conf\_write](#ga5cfe01762e5af8dc0cc5fbd550ff7e74) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write a 32-bit word to an endpoint's configuration space. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_ctrl\_region\_allocate](#ga1de030e2e8b07509d75de5a348297f42) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bar\_size, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_bus\_addr) |
|  | Allocate a memory region subset for an endpoint Base Address Register. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_ctrl\_region\_get\_allocate\_base](#gae7c109ca138adfd906fef5b6f3dca385) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_base\_addr) |
|  | Function called to get the current allocation base of a memory region subset for an endpoint Base Address Register. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_ctrl\_region\_translate](#gae6fa104ea2cc85912ebb1cfe0a1a3ddf) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) bar\_bus\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_addr) |
|  | Translate an endpoint Base Address Register bus-centric address into Physical address. |

## Detailed Description

PCI Express Controller Interface.

## Macro Definition Documentation

## [◆ ](#ga91525130b94b07187633abd1e017aa61)PCIE\_RANGE\_FORMAT

| #define PCIE\_RANGE\_FORMAT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

**Value:**

{ \

.flags = [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX](group__devicetree-ranges-prop.md#ga32a9c873d3ec1f5d7922c38eaafd1af8)(node\_id, idx), \

.pcie\_bus\_addr = [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](group__devicetree-ranges-prop.md#ga449940559213086b15151ec00e46607d)(node\_id, idx), \

.host\_map\_addr = [DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](group__devicetree-ranges-prop.md#ga48d493ad616438ace2396c0312a242ba)(node\_id, idx), \

.map\_length = [DT\_RANGES\_LENGTH\_BY\_IDX](group__devicetree-ranges-prop.md#ga52677a5bc86f9132a09b6bc37153afb2)(node\_id, idx), \

},

[DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX](group__devicetree-ranges-prop.md#ga32a9c873d3ec1f5d7922c38eaafd1af8)

#define DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)

Get the ranges property child bus flags at index.

**Definition** devicetree.h:1996

[DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](group__devicetree-ranges-prop.md#ga449940559213086b15151ec00e46607d)

#define DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)

Get the ranges property child bus address at index.

**Definition** devicetree.h:2045

[DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](group__devicetree-ranges-prop.md#ga48d493ad616438ace2396c0312a242ba)

#define DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)

Get the ranges property parent bus address at index.

**Definition** devicetree.h:2094

[DT\_RANGES\_LENGTH\_BY\_IDX](group__devicetree-ranges-prop.md#ga52677a5bc86f9132a09b6bc37153afb2)

#define DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx)

Get the ranges property length at index.

**Definition** devicetree.h:2143

## Typedef Documentation

## [◆ ](#gac3d0f7e90bcc30996ce23324d2d7356a)pcie\_ctrl\_conf\_read\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* pcie\_ctrl\_conf\_read\_t) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
| --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Function called to read a 32-bit word from an endpoint's configuration space.

Read a 32-bit word from an endpoint's configuration space with the PCI Express Controller configuration space access method (I/O port, memory mapped or custom method)

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | reg | the configuration word index (not address) |

Returns
:   the word read (0xFFFFFFFFU if nonexistent endpoint or word)

## [◆ ](#ga3241acc7de4af2b73cf3f47a25349109)pcie\_ctrl\_conf\_write\_t

| typedef void(\* pcie\_ctrl\_conf\_write\_t) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
| --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Function called to write a 32-bit word to an endpoint's configuration space.

Write a 32-bit word to an endpoint's configuration space with the PCI Express Controller configuration space access method (I/O port, memory mapped or custom method)

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | reg | the configuration word index (not address) |
    | data | the value to write |

## [◆ ](#ga62ce18e7495256c148168b773eabd37d)pcie\_ctrl\_region\_allocate\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* pcie\_ctrl\_region\_allocate\_t) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bar\_size, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_bus\_addr) |
| --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Function called to allocate a memory region subset for an endpoint Base Address Register.

When enumerating PCIe Endpoints, Type0 endpoints can require up to 6 memory zones via the Base Address Registers from I/O or Memory types.

This call allocates such zone in the PCI Express Controller memory regions if such region is available and space is still available.

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | mem | True if the BAR is of memory type |
    | mem64 | True if the BAR is of 64bit memory type |
    | bar\_size | Size in bytes of the Base Address Register as returned by HW |
    | bar\_bus\_addr | bus-centric address allocated to be written in the BAR register |

Returns
:   True if allocation was possible, False if allocation failed

## [◆ ](#gaa9d5bd27c841e36f65e65dec0b057e9a)pcie\_ctrl\_region\_get\_allocate\_base\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* pcie\_ctrl\_region\_get\_allocate\_base\_t) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_base\_addr) |
| --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Function called to get the current allocation base of a memory region subset for an endpoint Base Address Register.

When enumerating PCIe Endpoints, Type1 bridge endpoints requires a range of memory allocated by all endpoints in the bridged bus.

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | mem | True if the BAR is of memory type |
    | mem64 | True if the BAR is of 64bit memory type |
    | align | size to take in account for alignment |
    | bar\_base\_addr | bus-centric address allocation base |

Returns
:   True if allocation was possible, False if allocation failed

## [◆ ](#gab144356b1c3ec3754aae0008634f2d2f)pcie\_ctrl\_region\_translate\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* pcie\_ctrl\_region\_translate\_t) (const struct [device](structdevice.md) \*dev, [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mem64, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) bar\_bus\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*bar\_addr) |
| --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Function called to translate an endpoint Base Address Register bus-centric address into Physical address.

When enumerating PCIe Endpoints, Type0 endpoints can require up to 6 memory zones via the Base Address Registers from I/O or Memory types.

The bus-centric address set in this BAR register is not necessarily accessible from the CPU, thus must be translated by using the PCI Express Controller memory regions translation ranges to permit mapping from the CPU.

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | mem | True if the BAR is of memory type |
    | mem64 | True if the BAR is of 64bit memory type |
    | bar\_bus\_addr | bus-centric address written in the BAR register |
    | bar\_addr | CPU-centric address translated from the bus-centric address |

Returns
:   True if translation was possible, False if translation failed

## Function Documentation

## [◆ ](#ga1d978b8075191d6e571349684c731a43)pcie\_ctrl\_conf\_read()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcie\_ctrl\_conf\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Read a 32-bit word from an endpoint's configuration space.

Read a 32-bit word from an endpoint's configuration space with the PCI Express Controller configuration space access method (I/O port, memory mapped or custom method)

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | reg | the configuration word index (not address) |

Returns
:   the word read (0xFFFFFFFFU if nonexistent endpoint or word)

## [◆ ](#ga5cfe01762e5af8dc0cc5fbd550ff7e74)pcie\_ctrl\_conf\_write()

| | void pcie\_ctrl\_conf\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Write a 32-bit word to an endpoint's configuration space.

Write a 32-bit word to an endpoint's configuration space with the PCI Express Controller configuration space access method (I/O port, memory mapped or custom method)

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | reg | the configuration word index (not address) |
    | data | the value to write |

## [◆ ](#ga1de030e2e8b07509d75de5a348297f42)pcie\_ctrl\_region\_allocate()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_ctrl\_region\_allocate | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *mem*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *mem64*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bar\_size*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *bar\_bus\_addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Allocate a memory region subset for an endpoint Base Address Register.

When enumerating PCIe Endpoints, Type0 endpoints can require up to 6 memory zones via the Base Address Registers from I/O or Memory types.

This call allocates such zone in the PCI Express Controller memory regions if such region is available and space is still available.

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | mem | True if the BAR is of memory type |
    | mem64 | True if the BAR is of 64bit memory type |
    | bar\_size | Size in bytes of the Base Address Register as returned by HW |
    | bar\_bus\_addr | bus-centric address allocated to be written in the BAR register |

Returns
:   True if allocation was possible, False if allocation failed

## [◆ ](#gae7c109ca138adfd906fef5b6f3dca385)pcie\_ctrl\_region\_get\_allocate\_base()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_ctrl\_region\_get\_allocate\_base | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *mem*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *mem64*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *bar\_base\_addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Function called to get the current allocation base of a memory region subset for an endpoint Base Address Register.

When enumerating PCIe Endpoints, Type1 bridge endpoints requires a range of memory allocated by all endpoints in the bridged bus.

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | mem | True if the BAR is of memory type |
    | mem64 | True if the BAR is of 64bit memory type |
    | align | size to take in account for alignment |
    | bar\_base\_addr | bus-centric address allocation base |

Returns
:   True if allocation was possible, False if allocation failed

## [◆ ](#gae6fa104ea2cc85912ebb1cfe0a1a3ddf)pcie\_ctrl\_region\_translate()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_ctrl\_region\_translate | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *mem*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *mem64*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *bar\_bus\_addr*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *bar\_addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Translate an endpoint Base Address Register bus-centric address into Physical address.

When enumerating PCIe Endpoints, Type0 endpoints can require up to 6 memory zones via the Base Address Registers from I/O or Memory types.

The bus-centric address set in this BAR register is not necessarily accessible from the CPU, thus must be translated by using the PCI Express Controller memory regions translation ranges to permit mapping from the CPU.

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | mem | True if the BAR is of memory type |
    | mem64 | True if the BAR is of 64bit memory type |
    | bar\_bus\_addr | bus-centric address written in the BAR register |
    | bar\_addr | CPU-centric address translated from the bus-centric address |

Returns
:   True if translation was possible, False if translation failed

## [◆ ](#gaa16b59c39f273a654b72d9e209f3ba2e)pcie\_generic\_ctrl\_conf\_read()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcie\_generic\_ctrl\_conf\_read | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *cfg\_addr*, |
| --- | --- | --- | --- |
|  |  | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg* ) |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Read a 32-bit word from a Memory-Mapped endpoint's configuration space.

Read a 32-bit word from an endpoint's configuration space from a Memory-Mapped configuration space access method, known as PCI Control Access Method (CAM) or PCIe Extended Control Access Method (ECAM).

Parameters
:   | cfg\_addr | Logical address of Memory-Mapped configuration space |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | reg | the configuration word index (not address) |

Returns
:   the word read (0xFFFFFFFFU if nonexistent endpoint or word)

## [◆ ](#ga709ecedbd0585b4eb17fc2f5923a8f61)pcie\_generic\_ctrl\_conf\_write()

| void pcie\_generic\_ctrl\_conf\_write | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *cfg\_addr*, |
| --- | --- | --- | --- |
|  |  | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Write a 32-bit word to a Memory-Mapped endpoint's configuration space.

Write a 32-bit word to an endpoint's configuration space from a Memory-Mapped configuration space access method, known as PCI Control Access Method (CAM) or PCIe Extended Control Access Method (ECAM).

Parameters
:   | cfg\_addr | Logical address of Memory-Mapped configuration space |
    | --- | --- |
    | bdf | PCI(e) endpoint |
    | reg | the configuration word index (not address) |
    | data | the value to write |

## [◆ ](#ga75910ea4255a740b57e35a596a90b7bb)pcie\_generic\_ctrl\_enumerate()

| void pcie\_generic\_ctrl\_enumerate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf\_start* ) |

`#include <[controller.h](drivers_2pcie_2controller_8h.md)>`

Start PCIe Endpoints enumeration.

Start a PCIe Endpoints enumeration from a Bus number. When on non-x86 architecture or when firmware didn't setup the PCIe Bus hierarchy, the PCIe bus complex must be enumerated to setup the Endpoints Base Address Registers.

Parameters
:   | dev | PCI Express Controller device pointer |
    | --- | --- |
    | bdf\_start | PCI(e) start endpoint (only bus & dev are used to start enumeration) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
