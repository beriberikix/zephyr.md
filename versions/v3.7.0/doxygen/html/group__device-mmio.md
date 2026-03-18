---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__device-mmio.html
original_path: doxygen/html/group__device-mmio.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Device memory-mapped IO management

[Device Model](group__device__model.md)

Definitions and helper macros for managing driver memory-mapped input/output (MMIO) regions appropriately in either RAM or ROM.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Named MMIO region macros](group__device-mmio-named.md) |
|  | For drivers which need to manage multiple MMIO regions, which will be referenced by name. |
|  | [Single MMIO region macros](group__device-mmio-single.md) |
|  | For drivers which need to manage just one MMIO region, the most common case. |
|  | [Top-level MMIO region macros](group__device-mmio-toplevel.md) |
|  | For drivers which do not use Zephyr's driver model and do not associate struct device with a driver instance. |

| Macros | |
| --- | --- |
| #define | [DEVICE\_MMIO\_IS\_IN\_RAM](#gabdae30483b01d470c357571e088dc51a) |

| Functions | |
| --- | --- |
| static \_\_boot\_func void | [device\_map](#ga6b4a9841a5176104e1b63f7475d3d2a2) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) \*virt\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys\_addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set linear address for device MMIO access. |

## Detailed Description

Definitions and helper macros for managing driver memory-mapped input/output (MMIO) regions appropriately in either RAM or ROM.

In most cases drivers will just want to include device.h, but including this separately may be needed for arch-level driver code which uses the DEVICE\_MMIO\_TOPLEVEL variants and including the main device.h would introduce header dependency loops due to that header's reliance on [kernel.h](kernel_8h.md "Public kernel APIs.").

## Macro Definition Documentation

## [◆ ](#gabdae30483b01d470c357571e088dc51a)DEVICE\_MMIO\_IS\_IN\_RAM

| #define DEVICE\_MMIO\_IS\_IN\_RAM |
| --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

## Function Documentation

## [◆ ](#ga6b4a9841a5176104e1b63f7475d3d2a2)device\_map()

| | \_\_boot\_func void device\_map | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) \* | *virt\_addr*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys\_addr*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

Set linear address for device MMIO access.

This function sets the virt\_addr parameter to the correct linear address for the MMIO region.

If the MMU is enabled, mappings may be created in the page tables.

Normally, only a caching mode needs to be set for the 'flags' parameter. The mapped linear address will have read-write access to supervisor mode.

See also
:   k\_map()

Parameters
:   | [out] | virt\_addr | Output linear address storage location, most users will want some [DEVICE\_MMIO\_RAM\_PTR()](group__device-mmio-single.md#ga63f871dc2ec4c89839a1782e86e292bf "Return a pointer to the RAM-based storage area for a device's MMIO address.") value |
    | --- | --- | --- |
    | [in] | phys\_addr | Physical address base of the MMIO region |
    | [in] | size | Size of the MMIO region |
    | [in] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Caching mode and access flags, see K\_MEM\_CACHE\_\* and K\_MEM\_PERM\_\* macros |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
