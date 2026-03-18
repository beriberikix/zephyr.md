---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__device-mmio-named.html
original_path: doxygen/html/group__device-mmio-named.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Named MMIO region macros

[Device Model](group__device__model.md) » [Device memory-mapped IO management](group__device-mmio.md)

For drivers which need to manage multiple MMIO regions, which will be referenced by name.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [DEVICE\_MMIO\_NAMED\_RAM](#ga92b6570b0f7bd370bbdfbc4e474151e4)(name) |
|  | Declare storage for MMIO data within a device's dev\_data struct. |
| #define | [DEVICE\_MMIO\_NAMED\_RAM\_PTR](#ga42737f178f205bd90d4e523ae5d67a09)(dev, name) |
|  | Return a pointer to the RAM storage for a device's named MMIO address. |
| #define | [DEVICE\_MMIO\_NAMED\_ROM](#gae3ad012160f657451a3f47487510bffb)(name) |
|  | Declare storage for MMIO data within a device's config struct. |
| #define | [DEVICE\_MMIO\_NAMED\_ROM\_PTR](#ga7f018db0d820b72a782759a4b674de94)(dev, name) |
|  | Return a pointer to the ROM-based storage area for a device's MMIO information. |
| #define | [DEVICE\_MMIO\_NAMED\_ROM\_INIT](#ga727a1946d2a315af720706a9c9e80465)(name, node\_id) |
|  | Initialize a named DEVICE\_MMIO\_NAMED\_ROM member. |
| #define | [DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME](#gada46ff611e373bdb26a9473ec7cb0380)(name, node\_id) |
|  | Initialize a named DEVICE\_MMIO\_NAMED\_ROM member using a named DT reg property. |
| #define | [DEVICE\_MMIO\_NAMED\_MAP](#ga1059bb0020656ce6597e29c7dd6680c1)(dev, name, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set up memory for a named MMIO region. |
| #define | [DEVICE\_MMIO\_NAMED\_GET](#ga5ca4b0cf0637f475b5da3b1ec0a7c995)(dev, name) |
|  | Obtain a named MMIO address for a device. |

## Detailed Description

For drivers which need to manage multiple MMIO regions, which will be referenced by name.

## Macro Definition Documentation

## [◆ ](#ga5ca4b0cf0637f475b5da3b1ec0a7c995)DEVICE\_MMIO\_NAMED\_GET

| #define DEVICE\_MMIO\_NAMED\_GET | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

(\*[DEVICE\_MMIO\_NAMED\_RAM\_PTR](#ga42737f178f205bd90d4e523ae5d67a09)((dev), name))

[DEVICE\_MMIO\_NAMED\_RAM\_PTR](#ga42737f178f205bd90d4e523ae5d67a09)

#define DEVICE\_MMIO\_NAMED\_RAM\_PTR(dev, name)

Return a pointer to the RAM storage for a device's named MMIO address.

**Definition** device\_mmio.h:382

Obtain a named MMIO address for a device.

This macro returns the MMIO base address for a named region from the appropriate place within the device object's linked data structures.

This is for drivers which have multiple MMIO regions.

This macro requires that the macros DEV\_DATA and DEV\_CFG are locally defined and return properly typed pointers to the particular dev\_data and config structs for this driver.

See also
:   [DEVICE\_MMIO\_GET](group__device-mmio-single.md#ga8cb49d87ef6dc3b017d5b68860530b63 "Obtain the MMIO address for a device.")

Parameters
:   | dev | Device object |
    | --- | --- |
    | name | Member name for MMIO information, as declared with DEVICE\_MMIO\_NAMED\_RAM/DEVICE\_MMIO\_NAMED\_ROM |

Returns
:   [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) linear address of the MMIO region

## [◆ ](#ga1059bb0020656ce6597e29c7dd6680c1)DEVICE\_MMIO\_NAMED\_MAP

| #define DEVICE\_MMIO\_NAMED\_MAP | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

[device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)([DEVICE\_MMIO\_NAMED\_RAM\_PTR](#ga42737f178f205bd90d4e523ae5d67a09)((dev), name), \

([DEVICE\_MMIO\_NAMED\_ROM\_PTR](#ga7f018db0d820b72a782759a4b674de94)((dev), name)->phys\_addr), \

([DEVICE\_MMIO\_NAMED\_ROM\_PTR](#ga7f018db0d820b72a782759a4b674de94)((dev), name)->size), \

([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)))

[DEVICE\_MMIO\_NAMED\_ROM\_PTR](#ga7f018db0d820b72a782759a4b674de94)

#define DEVICE\_MMIO\_NAMED\_ROM\_PTR(dev, name)

Return a pointer to the ROM-based storage area for a device's MMIO information.

**Definition** device\_mmio.h:435

[device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)

static \_\_boot\_func void device\_map(mm\_reg\_t \*virt\_addr, uintptr\_t phys\_addr, size\_t size, uint32\_t flags)

Set linear address for device MMIO access.

**Definition** device\_mmio.h:97

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

Set up memory for a named MMIO region.

This performs the necessary PCI probing and/or MMU virtual memory mapping such that [DEVICE\_MMIO\_GET(name)](group__device-mmio-single.md#ga8cb49d87ef6dc3b017d5b68860530b63 "Obtain the MMIO address for a device.") returns a suitable linear memory address for the MMIO region.

If such operations are not required by the target hardware, this expands to nothing.

This should be called from the driver's init function, once for each MMIO region that needs to be mapped.

This macro requires that the macros DEV\_DATA and DEV\_CFG are locally defined and return properly typed pointers to the particular dev\_data and config structs for this driver.

The flags argument is currently used for caching mode, which should be one of the DEVICE\_CACHE\_\* macros. Unused bits are reserved for future expansion.

Parameters
:   | dev | Device object |
    | --- | --- |
    | name | Member name for MMIO information, as declared with DEVICE\_MMIO\_NAMED\_RAM/DEVICE\_MMIO\_NAMED\_ROM |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | One of the DEVICE\_CACHE\_\* caching modes |

## [◆ ](#ga92b6570b0f7bd370bbdfbc4e474151e4)DEVICE\_MMIO\_NAMED\_RAM

| #define DEVICE\_MMIO\_NAMED\_RAM | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) name

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

Declare storage for MMIO data within a device's dev\_data struct.

This gets accessed by the [DEVICE\_MMIO\_NAMED\_MAP()](#ga1059bb0020656ce6597e29c7dd6680c1) and [DEVICE\_MMIO\_NAMED\_GET()](#ga5ca4b0cf0637f475b5da3b1ec0a7c995) macros.

Depending on configuration, no memory may be reserved at all. Multiple named regions may be declared.

There must be a corresponding DEVICE\_MMIO\_ROM in config if the physical address is known at build time, but may be omitted if not (such as with PCIe.

Example for a driver named "foo":

struct foo\_driver\_data {

int blarg;

[DEVICE\_MMIO\_NAMED\_RAM](#ga92b6570b0f7bd370bbdfbc4e474151e4)(corge);

[DEVICE\_MMIO\_NAMED\_RAM](#ga92b6570b0f7bd370bbdfbc4e474151e4)(grault);

int wibble;

...

}

[DEVICE\_MMIO\_NAMED\_RAM](#ga92b6570b0f7bd370bbdfbc4e474151e4)

#define DEVICE\_MMIO\_NAMED\_RAM(name)

Declare storage for MMIO data within a device's dev\_data struct.

**Definition** device\_mmio.h:366

No build-time initialization of this memory is necessary; it will be set up in the init function by [DEVICE\_MMIO\_NAMED\_MAP()](#ga1059bb0020656ce6597e29c7dd6680c1).

Parameters
:   | name | Member name to use to store within dev\_data. |
    | --- | --- |

## [◆ ](#ga42737f178f205bd90d4e523ae5d67a09)DEVICE\_MMIO\_NAMED\_RAM\_PTR

| #define DEVICE\_MMIO\_NAMED\_RAM\_PTR | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

(&(DEV\_DATA(dev)->name))

Return a pointer to the RAM storage for a device's named MMIO address.

This macro requires that the macro DEV\_DATA is locally defined and returns a properly typed pointer to the particular dev\_data struct for this driver.

Parameters
:   | dev | device instance object |
    | --- | --- |
    | name | Member name within dev\_data |

Return values
:   | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | pointer to storage location |
    | --- | --- |

## [◆ ](#gae3ad012160f657451a3f47487510bffb)DEVICE\_MMIO\_NAMED\_ROM

| #define DEVICE\_MMIO\_NAMED\_ROM | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

struct z\_device\_mmio\_rom name

Declare storage for MMIO data within a device's config struct.

This gets accessed by [DEVICE\_MMIO\_NAMED\_MAP()](#ga1059bb0020656ce6597e29c7dd6680c1) and [DEVICE\_MMIO\_NAMED\_GET()](#ga5ca4b0cf0637f475b5da3b1ec0a7c995) macros.

What gets stored here varies considerably by configuration. Multiple named regions may be declared. There must be corresponding entries in the dev\_data struct.

This storage is not used if the device is PCIe and may be omitted.

If used, this must be initialized at build time with information from DTS using [DEVICE\_MMIO\_NAMED\_ROM\_INIT()](#ga727a1946d2a315af720706a9c9e80465)

A pointer to this memory may be obtained with [DEVICE\_MMIO\_NAMED\_ROM\_PTR()](#ga7f018db0d820b72a782759a4b674de94).

Example for a driver named "foo":

struct foo\_config {

int bar;

[DEVICE\_MMIO\_NAMED\_ROM](#gae3ad012160f657451a3f47487510bffb)(corge);

[DEVICE\_MMIO\_NAMED\_ROM](#gae3ad012160f657451a3f47487510bffb)(grault);

int baz;

...

}

[DEVICE\_MMIO\_NAMED\_ROM](#gae3ad012160f657451a3f47487510bffb)

#define DEVICE\_MMIO\_NAMED\_ROM(name)

Declare storage for MMIO data within a device's config struct.

**Definition** device\_mmio.h:421

See also
:   [DEVICE\_MMIO\_NAMED\_ROM\_INIT()](#ga727a1946d2a315af720706a9c9e80465)

Parameters
:   | name | Member name to store within config |
    | --- | --- |

## [◆ ](#ga727a1946d2a315af720706a9c9e80465)DEVICE\_MMIO\_NAMED\_ROM\_INIT

| #define DEVICE\_MMIO\_NAMED\_ROM\_INIT | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

.name = Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

Initialize a named DEVICE\_MMIO\_NAMED\_ROM member.

Initialize MMIO-related information within a specific instance of a device config struct, using information from DTS.

Example for an instance of a driver belonging to the "foo" subsystem that will have two regions named 'corge' and 'grault':

struct foo\_config my\_config = {

bar = 7;

[DEVICE\_MMIO\_NAMED\_ROM\_INIT](#ga727a1946d2a315af720706a9c9e80465)(corge, [DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(...));

[DEVICE\_MMIO\_NAMED\_ROM\_INIT](#ga727a1946d2a315af720706a9c9e80465)(grault, [DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(...));

baz = 2;

...

}

[DEVICE\_MMIO\_NAMED\_ROM\_INIT](#ga727a1946d2a315af720706a9c9e80465)

#define DEVICE\_MMIO\_NAMED\_ROM\_INIT(name, node\_id)

Initialize a named DEVICE\_MMIO\_NAMED\_ROM member.

**Definition** device\_mmio.h:463

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

See also
:   [DEVICE\_MMIO\_NAMED\_ROM()](#gae3ad012160f657451a3f47487510bffb)

Parameters
:   | name | Member name within config for the MMIO region |
    | --- | --- |
    | node\_id | DTS node identifier |

## [◆ ](#gada46ff611e373bdb26a9473ec7cb0380)DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME

| #define DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

.name = Z\_DEVICE\_MMIO\_NAMED\_ROM\_INITIALIZER(name, node\_id)

Initialize a named DEVICE\_MMIO\_NAMED\_ROM member using a named DT reg property.

Same as [DEVICE\_MMIO\_NAMED\_ROM\_INIT](#ga727a1946d2a315af720706a9c9e80465) but the size and address are taken from a named DT reg property.

Example for an instance of a driver belonging to the "foo" subsystem that will have two DT-defined regions named 'chip' and 'dale':

foo@E5000000 {

reg = <0xE5000000 0x1000>, <0xE6000000 0x1000>;

reg-names = "chip", "dale";

...

};

struct foo\_config my\_config = {

bar = 7;

[DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME](#gada46ff611e373bdb26a9473ec7cb0380)(chip, [DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(...));

[DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME](#gada46ff611e373bdb26a9473ec7cb0380)(dale, [DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(...));

baz = 2;

...

}

[DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME](#gada46ff611e373bdb26a9473ec7cb0380)

#define DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME(name, node\_id)

Initialize a named DEVICE\_MMIO\_NAMED\_ROM member using a named DT reg property.

**Definition** device\_mmio.h:504

See also
:   [DEVICE\_MMIO\_NAMED\_ROM\_INIT()](#ga727a1946d2a315af720706a9c9e80465)

Parameters
:   | name | Member name within config for the MMIO region and name of the reg property in the DT |
    | --- | --- |
    | node\_id | DTS node identifier |

## [◆ ](#ga7f018db0d820b72a782759a4b674de94)DEVICE\_MMIO\_NAMED\_ROM\_PTR

| #define DEVICE\_MMIO\_NAMED\_ROM\_PTR | ( |  | *dev*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[device_mmio.h](device__mmio_8h.md)>`

**Value:**

(&(DEV\_CFG(dev)->name))

Return a pointer to the ROM-based storage area for a device's MMIO information.

This macro requires that the macro DEV\_CFG is locally defined and returns a properly typed pointer to the particular config struct for this driver.

Parameters
:   | dev | device instance object |
    | --- | --- |
    | name | Member name within config |

Return values
:   | struct | device\_mmio\_rom \* pointer to storage location |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
