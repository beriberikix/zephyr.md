---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__device-mmio-toplevel.html
original_path: doxygen/html/group__device-mmio-toplevel.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Top-level MMIO region macros

[Device Model](group__device__model.md) » [Device memory-mapped IO management](group__device-mmio.md)

For drivers which do not use Zephyr's driver model and do not associate struct device with a driver instance.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [DEVICE\_MMIO\_TOPLEVEL](#gad60e6840b8a9c18c19693da0028c2488)(name, node\_id) |
|  | Declare top-level storage for MMIO information, global scope. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_DECLARE](#ga8a712886defe59972f4cf00bb2266f95)(name) |
|  | Provide an extern reference to a top-level MMIO region. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_STATIC](#ga80456633db67dbb23d32e2ae7cc93512)(name, node\_id) |
|  | Declare top-level storage for MMIO information, static scope. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_RAM\_PTR](#ga746bfe0c817dbd60f1c1f60d47f1560e)(name) |
|  | Return a pointer to the RAM storage for a device's toplevel MMIO address. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_ROM\_PTR](#ga2877cda5f9780ecff45a4abe150e2504)(name) |
|  | Return a pointer to the ROM-based storage area for a toplevel MMIO region. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_MAP](#ga6533dfab1e1bab2a11654abf4231379b)(name, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set up memory for a driver'sMMIO region. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_GET](#gaad7ad99277cf2be684bd70c46d358338)(name) |
|  | Obtain the MMIO address for a device declared top-level. |

## Detailed Description

For drivers which do not use Zephyr's driver model and do not associate struct device with a driver instance.

Top-level storage is used instead, with either global or static scope.

This is often useful for interrupt controller and timer drivers.

Currently PCIe devices are not well-supported with this set of macros. Either use Zephyr's driver model for these kinds of devices, or manage memory manually with calls to [device\_map()](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2 "Set linear address for device MMIO access.").

## Macro Definition Documentation

## [◆ ](#gad60e6840b8a9c18c19693da0028c2488)DEVICE\_MMIO\_TOPLEVEL

| #define DEVICE\_MMIO\_TOPLEVEL | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

\_\_pinned\_bss \

mm\_reg\_t Z\_TOPLEVEL\_RAM\_NAME(name); \

\_\_pinned\_rodata \

const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name) = \

Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

Declare top-level storage for MMIO information, global scope.

This is intended for drivers which do not use Zephyr's driver model of config/dev\_data linked to a struct device.

Instead, this is a top-level declaration for the driver's C file. The scope of this declaration is global and may be referenced by other C files, using DEVICE\_MMIO\_TOPLEVEL\_DECLARE.

Parameters
:   | name | Base symbol name |
    | --- | --- |
    | node\_id | Device-tree node identifier for this region |

## [◆ ](#ga8a712886defe59972f4cf00bb2266f95)DEVICE\_MMIO\_TOPLEVEL\_DECLARE

| #define DEVICE\_MMIO\_TOPLEVEL\_DECLARE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

extern [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) Z\_TOPLEVEL\_RAM\_NAME(name); \

extern const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name)

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

Provide an extern reference to a top-level MMIO region.

If a top-level MMIO region defined with DEVICE\_MMIO\_DEFINE needs to be referenced from other C files, this macro provides the necessary extern definitions.

See also
:   [DEVICE\_MMIO\_TOPLEVEL](#gad60e6840b8a9c18c19693da0028c2488)

Parameters
:   | name | Name of the top-level MMIO region |
    | --- | --- |

## [◆ ](#gaad7ad99277cf2be684bd70c46d358338)DEVICE\_MMIO\_TOPLEVEL\_GET

| #define DEVICE\_MMIO\_TOPLEVEL\_GET | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

(([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0))Z\_TOPLEVEL\_RAM\_NAME(name))

Obtain the MMIO address for a device declared top-level.

See also
:   [DEVICE\_MMIO\_GET](group__device-mmio-single.md#ga8cb49d87ef6dc3b017d5b68860530b63 "Obtain the MMIO address for a device.")

Parameters
:   | name | Name of the top-level MMIO region |
    | --- | --- |

Returns
:   [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) linear address of the MMIO region

## [◆ ](#ga6533dfab1e1bab2a11654abf4231379b)DEVICE\_MMIO\_TOPLEVEL\_MAP

| #define DEVICE\_MMIO\_TOPLEVEL\_MAP | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

[device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)(&Z\_TOPLEVEL\_RAM\_NAME(name), \

Z\_TOPLEVEL\_ROM\_NAME(name).phys\_addr, \

Z\_TOPLEVEL\_ROM\_NAME(name).size, ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)))

[device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)

static \_\_boot\_func void device\_map(mm\_reg\_t \*virt\_addr, uintptr\_t phys\_addr, size\_t size, uint32\_t flags)

Set linear address for device MMIO access.

**Definition** device\_mmio.h:97

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

Set up memory for a driver'sMMIO region.

This performs the necessary MMU virtual memory mapping such that [DEVICE\_MMIO\_GET()](group__device-mmio-single.md#ga8cb49d87ef6dc3b017d5b68860530b63 "Obtain the MMIO address for a device.") returns a suitable linear memory address for the MMIO region.

If such operations are not required by the target hardware, this expands to nothing.

This should be called once from the driver's init function.

The flags argument is currently used for caching mode, which should be one of the DEVICE\_CACHE\_\* macros. Unused bits are reserved for future expansion.

Parameters
:   | name | Name of the top-level MMIO region |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | One of the DEVICE\_CACHE\_\* caching modes |

## [◆ ](#ga746bfe0c817dbd60f1c1f60d47f1560e)DEVICE\_MMIO\_TOPLEVEL\_RAM\_PTR

| #define DEVICE\_MMIO\_TOPLEVEL\_RAM\_PTR | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

&Z\_TOPLEVEL\_RAM\_NAME(name)

Return a pointer to the RAM storage for a device's toplevel MMIO address.

Parameters
:   | name | Name of toplevel MMIO region |
    | --- | --- |

Return values
:   | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | pointer to storage location |
    | --- | --- |

## [◆ ](#ga2877cda5f9780ecff45a4abe150e2504)DEVICE\_MMIO\_TOPLEVEL\_ROM\_PTR

| #define DEVICE\_MMIO\_TOPLEVEL\_ROM\_PTR | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

&Z\_TOPLEVEL\_ROM\_NAME(name)

Return a pointer to the ROM-based storage area for a toplevel MMIO region.

Parameters
:   | name | MMIO region name |
    | --- | --- |

Return values
:   | struct | device\_mmio\_rom \* pointer to storage location |
    | --- | --- |

## [◆ ](#ga80456633db67dbb23d32e2ae7cc93512)DEVICE\_MMIO\_TOPLEVEL\_STATIC

| #define DEVICE\_MMIO\_TOPLEVEL\_STATIC | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

\_\_pinned\_bss \

static [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) Z\_TOPLEVEL\_RAM\_NAME(name); \

\_\_pinned\_rodata \

static const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name) = \

Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

Declare top-level storage for MMIO information, static scope.

This is intended for drivers which do not use Zephyr's driver model of config/dev\_data linked to a struct device.

Instead, this is a top-level declaration for the driver's C file. The scope of this declaration is static.

Parameters
:   | name | Name of the top-level MMIO region |
    | --- | --- |
    | node\_id | Device-tree node identifier for this region |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
