---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__device-mmio-single.html
original_path: doxygen/html/group__device-mmio-single.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Single MMIO region macros

[Device Model](group__device__model.md) » [Device memory-mapped IO management](group__device-mmio.md)

For drivers which need to manage just one MMIO region, the most common case.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [DEVICE\_MMIO\_RAM](#ga47e037f86108c8da12d8a9b9a35e6ad5)   [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) \_mmio |
|  | Declare storage for MMIO information within a device's dev\_data struct. |
| #define | [DEVICE\_MMIO\_RAM\_PTR](#ga63f871dc2ec4c89839a1782e86e292bf)([device](structdevice.md)) |
|  | Return a pointer to the RAM-based storage area for a device's MMIO address. |
| #define | [DEVICE\_MMIO\_ROM](#ga1dfb620f6b3c7ee9b2bc54044d0bc875)   struct z\_device\_mmio\_rom \_mmio |
|  | Declare storage for MMIO data within a device's config struct. |
| #define | [DEVICE\_MMIO\_ROM\_PTR](#ga6246f4c8bc1542d8960d3bda99a592e5)(dev) |
|  | Return a pointer to the ROM-based storage area for a device's MMIO information. |
| #define | [DEVICE\_MMIO\_ROM\_INIT](#ga023516c60725f8c6d62110f74af22549)(node\_id) |
|  | Initialize a DEVICE\_MMIO\_ROM member. |
| #define | [DEVICE\_MMIO\_MAP](#ga8e15770c4ec118edbefc1ef95f1ace80)(dev, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map MMIO memory into the address space. |
| #define | [DEVICE\_MMIO\_GET](#ga8cb49d87ef6dc3b017d5b68860530b63)(dev) |
|  | Obtain the MMIO address for a device. |

## Detailed Description

For drivers which need to manage just one MMIO region, the most common case.

## Macro Definition Documentation

## [◆ ](#ga8cb49d87ef6dc3b017d5b68860530b63)DEVICE\_MMIO\_GET

| #define DEVICE\_MMIO\_GET | ( |  | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

(\*[DEVICE\_MMIO\_RAM\_PTR](#ga63f871dc2ec4c89839a1782e86e292bf)(dev))

[DEVICE\_MMIO\_RAM\_PTR](#ga63f871dc2ec4c89839a1782e86e292bf)

#define DEVICE\_MMIO\_RAM\_PTR(device)

Return a pointer to the RAM-based storage area for a device's MMIO address.

**Definition** device\_mmio.h:197

Obtain the MMIO address for a device.

For most microcontrollers MMIO addresses can be fixed values known at build time, and we can store this in device->config, residing in ROM.

However, some devices can only know their MMIO addresses at runtime, because they need to be memory-mapped into the address space, enumerated from PCI, or both.

This macro returns the linear address of the driver's MMIO region. This is for drivers which have exactly one MMIO region. A call must have been made to [device\_map()](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2 "Set linear address for device MMIO access.") in the driver init function.

Parameters
:   | dev | Device object |
    | --- | --- |

Returns
:   [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) linear address of the MMIO region

## [◆ ](#ga8e15770c4ec118edbefc1ef95f1ace80)DEVICE\_MMIO\_MAP

| #define DEVICE\_MMIO\_MAP | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

[device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)([DEVICE\_MMIO\_RAM\_PTR](#ga63f871dc2ec4c89839a1782e86e292bf)(dev), \

[DEVICE\_MMIO\_ROM\_PTR](#ga6246f4c8bc1542d8960d3bda99a592e5)(dev)->phys\_addr, \

[DEVICE\_MMIO\_ROM\_PTR](#ga6246f4c8bc1542d8960d3bda99a592e5)(dev)->size, \

([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)))

[DEVICE\_MMIO\_ROM\_PTR](#ga6246f4c8bc1542d8960d3bda99a592e5)

#define DEVICE\_MMIO\_ROM\_PTR(dev)

Return a pointer to the ROM-based storage area for a device's MMIO information.

**Definition** device\_mmio.h:241

[device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)

static \_\_boot\_func void device\_map(mm\_reg\_t \*virt\_addr, uintptr\_t phys\_addr, size\_t size, uint32\_t flags)

Set linear address for device MMIO access.

**Definition** device\_mmio.h:97

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

Map MMIO memory into the address space.

This is not intended for PCIe devices; these must be probed at runtime and you will want to make a [device\_map()](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2 "Set linear address for device MMIO access.") call directly, using [DEVICE\_MMIO\_RAM\_PTR()](#ga63f871dc2ec4c89839a1782e86e292bf) as the target virtual address location.

The flags argument is currently used for caching mode, which should be one of the DEVICE\_CACHE\_\* macros. Unused bits are reserved for future expansion.

Parameters
:   | dev | Device object instance |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | cache mode flags |

## [◆ ](#ga47e037f86108c8da12d8a9b9a35e6ad5)DEVICE\_MMIO\_RAM

| #define DEVICE\_MMIO\_RAM   [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) \_mmio |
| --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

Declare storage for MMIO information within a device's dev\_data struct.

This gets accessed by the [DEVICE\_MMIO\_MAP()](#ga8e15770c4ec118edbefc1ef95f1ace80) and [DEVICE\_MMIO\_GET()](#ga8cb49d87ef6dc3b017d5b68860530b63) macros.

Depending on configuration, no memory may be reserved at all. This must be the first member of the data struct.

There must be a corresponding DEVICE\_MMIO\_ROM in config\_info if the physical address is known at build time, but may be omitted if not (such as with PCIe)

Example for a driver named "foo":

struct foo\_driver\_data {

[DEVICE\_MMIO\_RAM](#ga47e037f86108c8da12d8a9b9a35e6ad5);

int wibble;

...

}

[DEVICE\_MMIO\_RAM](#ga47e037f86108c8da12d8a9b9a35e6ad5)

#define DEVICE\_MMIO\_RAM

Declare storage for MMIO information within a device's dev\_data struct.

**Definition** device\_mmio.h:181

No build-time initialization of this memory is necessary; it will be set up in the init function by [DEVICE\_MMIO\_MAP()](#ga8e15770c4ec118edbefc1ef95f1ace80).

A pointer to this memory may be obtained with [DEVICE\_MMIO\_RAM\_PTR()](#ga63f871dc2ec4c89839a1782e86e292bf).

## [◆ ](#ga63f871dc2ec4c89839a1782e86e292bf)DEVICE\_MMIO\_RAM\_PTR

| #define DEVICE\_MMIO\_RAM\_PTR | ( |  | *[device](structdevice.md)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) \*)(([device](structdevice.md))->data)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

Return a pointer to the RAM-based storage area for a device's MMIO address.

This is useful for the target MMIO address location when using [device\_map()](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2 "Set linear address for device MMIO access.") directly.

Parameters
:   | [device](structdevice.md "Runtime device structure (in ROM) per driver instance.") | device node\_id object |
    | --- | --- |

Return values
:   | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | pointer to storage location |
    | --- | --- |

## [◆ ](#ga1dfb620f6b3c7ee9b2bc54044d0bc875)DEVICE\_MMIO\_ROM

| #define DEVICE\_MMIO\_ROM   struct z\_device\_mmio\_rom \_mmio |
| --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

Declare storage for MMIO data within a device's config struct.

This gets accessed by [DEVICE\_MMIO\_MAP()](#ga8e15770c4ec118edbefc1ef95f1ace80) and [DEVICE\_MMIO\_GET()](#ga8cb49d87ef6dc3b017d5b68860530b63) macros.

What gets stored here varies considerably by configuration. This must be the first member of the config struct. There must be a corresponding DEVICE\_MMIO\_RAM in data.

This storage is not used if the device is PCIe and may be omitted.

This should be initialized at build time with information from DTS using [DEVICE\_MMIO\_ROM\_INIT()](#ga023516c60725f8c6d62110f74af22549).

A pointer to this memory may be obtained with [DEVICE\_MMIO\_ROM\_PTR()](#ga6246f4c8bc1542d8960d3bda99a592e5).

Example for a driver named "foo":

struct foo\_config {

[DEVICE\_MMIO\_ROM](#ga1dfb620f6b3c7ee9b2bc54044d0bc875);

int baz;

...

}

[DEVICE\_MMIO\_ROM](#ga1dfb620f6b3c7ee9b2bc54044d0bc875)

#define DEVICE\_MMIO\_ROM

Declare storage for MMIO data within a device's config struct.

**Definition** device\_mmio.h:230

See also
:   [DEVICE\_MMIO\_ROM\_INIT()](#ga023516c60725f8c6d62110f74af22549)

## [◆ ](#ga023516c60725f8c6d62110f74af22549)DEVICE\_MMIO\_ROM\_INIT

| #define DEVICE\_MMIO\_ROM\_INIT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

.\_mmio = Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

Initialize a DEVICE\_MMIO\_ROM member.

Initialize MMIO-related information within a specific instance of a device config struct, using information from DTS.

Example for a driver belonging to the "foo" subsystem:

struct foo\_config my\_config = {

[DEVICE\_MMIO\_ROM\_INIT](#ga023516c60725f8c6d62110f74af22549)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(...)),

.baz = 2;

...

}

[DEVICE\_MMIO\_ROM\_INIT](#ga023516c60725f8c6d62110f74af22549)

#define DEVICE\_MMIO\_ROM\_INIT(node\_id)

Initialize a DEVICE\_MMIO\_ROM member.

**Definition** device\_mmio.h:266

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

See also
:   [DEVICE\_MMIO\_ROM()](#ga1dfb620f6b3c7ee9b2bc54044d0bc875)

Parameters
:   | node\_id | DTS node\_id |
    | --- | --- |

## [◆ ](#ga6246f4c8bc1542d8960d3bda99a592e5)DEVICE\_MMIO\_ROM\_PTR

| #define DEVICE\_MMIO\_ROM\_PTR | ( |  | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

((struct z\_device\_mmio\_rom \*)((dev)->config))

Return a pointer to the ROM-based storage area for a device's MMIO information.

This macro will not work properly if the ROM storage was omitted from the config struct declaration, and should not be used in this case.

Parameters
:   | dev | device instance object |
    | --- | --- |

Return values
:   | struct | device\_mmio\_rom \* pointer to storage location |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
