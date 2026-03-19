---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__device__model.html
original_path: doxygen/html/group__device__model.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Device Model

Device Model.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Device memory-mapped IO management](group__device-mmio.md) |
|  | Definitions and helper macros for managing driver memory-mapped input/output (MMIO) regions appropriately in either RAM or ROM. |

| Data Structures | |
| --- | --- |
| struct | [device\_state](structdevice__state.md) |
|  | Runtime device dynamic structure (in RAM) per driver instance. [More...](structdevice__state.md#details) |
| struct | [device](structdevice.md) |
|  | Runtime device structure (in ROM) per driver instance. [More...](structdevice.md#details) |

| Macros | |
| --- | --- |
| #define | [DEVICE\_HANDLE\_NULL](#ga4dd918c3a59b8afa185a4851165d2ca0)   0 |
|  | Flag value used to identify an unknown device. |
| #define | [DEVICE\_NAME\_GET](#ga430eb7530aeb3cff5708b55f9b571eb9)(dev\_id) |
|  | Expands to the name of a global device object. |
| #define | [DEVICE\_DEFINE](#gac12521f4d900e8947aac45c1b228366d)(dev\_id, name, init\_fn, pm, data, config, level, prio, api) |
|  | Create a device object and set it up for boot time initialization. |
| #define | [DEVICE\_DT\_NAME](#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id) |
|  | Return a string name for a devicetree node. |
| #define | [DEVICE\_DT\_DEFER](#gae16caf17999906091613325f885103cd)(node\_id) |
|  | Determine if a devicetree node initialization should be deferred. |
| #define | [DEVICE\_DT\_DEFINE](#gac49e26fbe91a14307d5ea08d41561dd1)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Create a device object from a devicetree node identifier and set it up for boot time initialization. |
| #define | [DEVICE\_DT\_INST\_DEFINE](#gada5ba4aca9e0662ccebb2232c7256419)(inst, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](#gac49e26fbe91a14307d5ea08d41561dd1), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier. |
| #define | [DEVICE\_DT\_NAME\_GET](#ga8ebbf17ef805817aa638f36f177a1a0e)(node\_id) |
|  | The name of the global device object for `node_id`. |
| #define | [DEVICE\_DT\_GET](#ga9a65996ce21f43acb7db061e23b48ec7)(node\_id) |
|  | Get a [device](structdevice.md "device") reference from a devicetree node identifier. |
| #define | [DEVICE\_DT\_INST\_GET](#ga9165e550ae175ce305eafe33390af78b)(inst) |
|  | Get a [device](structdevice.md "device") reference for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [DEVICE\_DT\_GET\_ANY](#gaadf3ffb63df544eb3de356ab2c5e9e3c)(compat) |
|  | Get a [device](structdevice.md "device") reference from a devicetree compatible. |
| #define | [DEVICE\_DT\_GET\_ONE](#ga39c760429534ef9ae77f3d996987cd2b)(compat) |
|  | Get a [device](structdevice.md "device") reference from a devicetree compatible. |
| #define | [DEVICE\_DT\_GET\_OR\_NULL](#ga6ce1dbfda6847ca6c3858712e9b41989)(node\_id) |
|  | Utility macro to obtain an optional reference to a device. |
| #define | [DEVICE\_DT\_GET\_BY\_IDX](#ga7abe347d0aa972e15d1f35af02265a6b)(node\_id, prop, idx) |
|  | Get a [device](structdevice.md "device") reference from a devicetree phandles by idx. |
| #define | [DEVICE\_GET](#gaf9403e7eb573a30d2dfaed357f4ef3f4)(dev\_id) |
|  | Obtain a pointer to a device object by name. |
| #define | [DEVICE\_DECLARE](#ga4e763eae14dcd41d599c485410ac2983)(dev\_id) |
|  | Declare a static device object. |
| #define | [DEVICE\_INIT\_DT\_GET](#gad829bbf36723e8cb6c3df8f996a908be)(node\_id) |
|  | Get a [init\_entry](structinit__entry.md "init_entry") reference from a devicetree node. |
| #define | [DEVICE\_INIT\_GET](#ga7b7d3030fea734304c61665e75191cc0)(dev\_id) |
|  | Get a [init\_entry](structinit__entry.md "init_entry") reference from a device identifier. |

| Typedefs | |
| --- | --- |
| typedef [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) |
|  | Type used to represent a "handle" for a device. |
| typedef int(\* | [device\_visitor\_callback\_t](#ga9a1118e5c76c44c998f7258a7de0bfbb)) (const struct [device](structdevice.md) \*dev, void \*context) |
|  | Prototype for functions used when iterating over a set of devices. |

| Functions | |
| --- | --- |
| static [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) | [device\_handle\_get](#ga456366a9ca0a8e97484c97c279745203) (const struct [device](structdevice.md) \*dev) |
|  | Get the handle for a given device. |
| static const struct [device](structdevice.md) \* | [device\_from\_handle](#ga73680daef9f8d7dc2541d83d09737f4a) ([device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) dev\_handle) |
|  | Get the device corresponding to a handle. |
| static const [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* | [device\_required\_handles\_get](#ga2157bbfc2deecfae6514f58221663618) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Get the device handles for devicetree dependencies of this device. |
| static const [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* | [device\_injected\_handles\_get](#gae89b0d818c45fdf258c0a421bc103ddc) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Get the device handles for injected dependencies of this device. |
| static const [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* | [device\_supported\_handles\_get](#ga3c9ae15d3224c792b915b107b2d5d00f) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Get the set of handles that this device supports. |
| int | [device\_required\_foreach](#ga6e3b6dbb15ca28d6c94ee07702663245) (const struct [device](structdevice.md) \*dev, [device\_visitor\_callback\_t](#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb, void \*context) |
|  | Visit every device that `dev` directly requires. |
| int | [device\_supported\_foreach](#gaf5fce5e93fd6d5e13aa8b20251b82b2a) (const struct [device](structdevice.md) \*dev, [device\_visitor\_callback\_t](#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb, void \*context) |
|  | Visit every device that `dev` directly supports. |
| const struct [device](structdevice.md) \* | [device\_get\_binding](#ga15386ca9ab38f3e30183c18f604fa835) (const char \*name) |
|  | Get a [device](structdevice.md "device") reference from its [device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d "device::name") field. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [device\_is\_ready](#gaa4944bd850e90cbd52b0489f9b12edfb) (const struct [device](structdevice.md) \*dev) |
|  | Verify that a device is ready for use. |
| int | [device\_init](#gaeea4f9c9f14ab12d224378ab90231c09) (const struct [device](structdevice.md) \*dev) |
|  | Initialize a device. |

## Detailed Description

Device Model.

Since
:   1.0

Version
:   1.1.0

## Macro Definition Documentation

## [◆ ](#ga4e763eae14dcd41d599c485410ac2983)DEVICE\_DECLARE

| #define DEVICE\_DECLARE | ( |  | *dev\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

static const struct [device](structdevice.md) [DEVICE\_NAME\_GET](#ga430eb7530aeb3cff5708b55f9b571eb9)(dev\_id)

[DEVICE\_NAME\_GET](#ga430eb7530aeb3cff5708b55f9b571eb9)

#define DEVICE\_NAME\_GET(dev\_id)

Expands to the name of a global device object.

**Definition** device.h:96

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

Declare a static device object.

This macro can be used at the top-level to declare a device, such that [DEVICE\_GET()](#gaf9403e7eb573a30d2dfaed357f4ef3f4) may be used before the full declaration in [DEVICE\_DEFINE()](#gac12521f4d900e8947aac45c1b228366d).

This is often useful when configuring interrupts statically in a device's init or per-instance config function, as the init function itself is required by [DEVICE\_DEFINE()](#gac12521f4d900e8947aac45c1b228366d) and use of [DEVICE\_GET()](#gaf9403e7eb573a30d2dfaed357f4ef3f4) inside it creates a circular dependency.

Parameters
:   | dev\_id | Device identifier. |
    | --- | --- |

## [◆ ](#gac12521f4d900e8947aac45c1b228366d)DEVICE\_DEFINE

| #define DEVICE\_DEFINE | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api* ) |

`#include <[device.h](device_8h.md)>`

**Value:**

Z\_DEVICE\_STATE\_DEFINE(dev\_id); \

Z\_DEVICE\_DEFINE([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855), dev\_id, name, init\_fn, pm, data, \

config, level, prio, api, \

&Z\_DEVICE\_STATE\_NAME(dev\_id))

[DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)

#define DT\_INVALID\_NODE

Name for an invalid node identifier.

**Definition** devicetree.h:83

Create a device object and set it up for boot time initialization.

This macro defines a [device](structdevice.md "device") that is automatically configured by the kernel during system initialization. This macro should only be used when the device is not being allocated from a devicetree node. If you are allocating a device from a devicetree node, use [DEVICE\_DT\_DEFINE()](#gac49e26fbe91a14307d5ea08d41561dd1) or [DEVICE\_DT\_INST\_DEFINE()](#gada5ba4aca9e0662ccebb2232c7256419) instead.

Parameters
:   | dev\_id | A unique token which is used in the name of the global device structure as a C identifier. |
    | --- | --- |
    | name | A string name for the device, which will be stored in [device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d "device::name"). This name can be used to look up the device with [device\_get\_binding()](#ga15386ca9ab38f3e30183c18f604fa835). This must be less than Z\_DEVICE\_MAX\_NAME\_LEN characters (including terminating [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) in order to be looked up from user mode. |
    | init\_fn | Pointer to the device's initialization function, which will be run by the kernel during system initialization. Can be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4). |
    | pm | Pointer to the device's power management resources, a [pm\_device](structpm__device.md "pm_device"), which will be stored in [device::pm](structdevice.md#a204619a873db1b99ea31f1c190760052 "device::pm") field. Use [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if the device does not use PM. |
    | data | Pointer to the device's private mutable data, which will be stored in [device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e "device::data"). |
    | config | Pointer to the device's private constant data, which will be stored in [device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc "device::config"). |
    | level | The device's initialization level (PRE\_KERNEL\_1, PRE\_KERNEL\_2 or POST\_KERNEL). |
    | prio | The device's priority within its initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api | Pointer to the device's API structure. Can be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4). |

## [◆ ](#gae16caf17999906091613325f885103cd)DEVICE\_DT\_DEFER

| #define DEVICE\_DT\_DEFER | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, zephyr\_deferred\_init)

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

Determine if a devicetree node initialization should be deferred.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |

Returns
:   Boolean stating if node initialization should be deferred.

## [◆ ](#gac49e26fbe91a14307d5ea08d41561dd1)DEVICE\_DT\_DEFINE

| #define DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | ... ) |

`#include <[device.h](device_8h.md)>`

**Value:**

Z\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), init\_fn, pm, data, config, \

level, prio, api, \

&Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)), \

\_\_VA\_ARGS\_\_)

[DEVICE\_DT\_NAME](#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:185

Create a device object from a devicetree node identifier and set it up for boot time initialization.

This macro defines a [device](structdevice.md "device") that is automatically configured by the kernel during system initialization. The global device object's name as a C identifier is derived from the node's dependency ordinal or hash. [device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d "device::name") is set to [DEVICE\_DT\_NAME(node\_id)](#gad864d7a50ee45285dacd68be1e5a49ce).

The device is declared with extern visibility, so a pointer to a global device object can be obtained with [DEVICE\_DT\_GET(node\_id)](#ga9a65996ce21f43acb7db061e23b48ec7) from any source file that includes <[zephyr/device.h](device_8h.md)> (even from extensions, when `CONFIG_LLEXT_EXPORT_DEVICES` is enabled). Before using the pointer, the referenced object should be checked using [device\_is\_ready()](#gaa4944bd850e90cbd52b0489f9b12edfb).

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Pointer to the device's initialization function, which will be run by the kernel during system initialization. Can be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4). |
    | pm | Pointer to the device's power management resources, a [pm\_device](structpm__device.md "pm_device"), which will be stored in [device::pm](structdevice.md#a204619a873db1b99ea31f1c190760052 "device::pm"). Use [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if the device does not use PM. |
    | data | Pointer to the device's private mutable data, which will be stored in [device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e "device::data"). |
    | config | Pointer to the device's private constant data, which will be stored in [device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc "device::config") field. |
    | level | The device's initialization level (PRE\_KERNEL\_1, PRE\_KERNEL\_2 or POST\_KERNEL). |
    | prio | The device's priority within its initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api | Pointer to the device's API structure. Can be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4). |

## [◆ ](#ga9a65996ce21f43acb7db061e23b48ec7)DEVICE\_DT\_GET

| #define DEVICE\_DT\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

(&[DEVICE\_DT\_NAME\_GET](#ga8ebbf17ef805817aa638f36f177a1a0e)(node\_id))

[DEVICE\_DT\_NAME\_GET](#ga8ebbf17ef805817aa638f36f177a1a0e)

#define DEVICE\_DT\_NAME\_GET(node\_id)

The name of the global device object for node\_id.

**Definition** device.h:263

Get a [device](structdevice.md "device") reference from a devicetree node identifier.

Returns a pointer to a device object created from a devicetree node, if any device was allocated by a driver.

If no such device was allocated, this will fail at linker time. If you get an error that looks like undefined reference to \_\_device\_dts\_ord\_<N>, that is what happened. Check to make sure your device driver is being compiled, usually by enabling the Kconfig options it requires.

Parameters
:   | node\_id | A devicetree node identifier |
    | --- | --- |

Returns
:   A pointer to the device object created for that node

## [◆ ](#gaadf3ffb63df544eb3de356ab2c5e9e3c)DEVICE\_DT\_GET\_ANY

| #define DEVICE\_DT\_GET\_ANY | ( |  | *compat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(compat), \

([DEVICE\_DT\_GET](#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)(compat))), \

([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)))

[DEVICE\_DT\_GET](#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:280

[DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)

#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat)

Does the devicetree have a status okay node with a compatible?

**Definition** devicetree.h:3711

[DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)

#define DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat)

Get a node identifier for a status okay node with a compatible.

**Definition** devicetree.h:479

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Get a [device](structdevice.md "device") reference from a devicetree compatible.

If an enabled devicetree node has the given compatible and a device object was created from it, this returns a pointer to that device.

If there no such devices, this returns NULL.

If there are multiple, this returns an arbitrary one.

If this returns non-NULL, the device must be checked for readiness before use, e.g. with [device\_is\_ready()](#gaa4944bd850e90cbd52b0489f9b12edfb).

Parameters
:   | compat | lowercase-and-underscores devicetree compatible |
    | --- | --- |

Returns
:   a pointer to a device, or NULL

## [◆ ](#ga7abe347d0aa972e15d1f35af02265a6b)DEVICE\_DT\_GET\_BY\_IDX

| #define DEVICE\_DT\_GET\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[device.h](device_8h.md)>`

**Value:**

[DEVICE\_DT\_GET](#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, prop, idx))

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1785

Get a [device](structdevice.md "device") reference from a devicetree phandles by idx.

Returns a pointer to a device object referenced by a phandles property, by idx.

Parameters
:   | node\_id | A devicetree node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property with type phandle, phandles, or phandle-array |
    | idx | logical index into `phs`, which must be zero if `phs` has type phandle |

Returns
:   A pointer to the device object created for that node

## [◆ ](#ga39c760429534ef9ae77f3d996987cd2b)DEVICE\_DT\_GET\_ONE

| #define DEVICE\_DT\_GET\_ONE | ( |  | *compat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(compat), \

([DEVICE\_DT\_GET](#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)(compat))), \

([ZERO\_OR\_COMPILE\_ERROR](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)(0)))

[ZERO\_OR\_COMPILE\_ERROR](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)

#define ZERO\_OR\_COMPILE\_ERROR(cond)

0 if cond is true-ish; causes a compile error otherwise.

**Definition** util.h:90

Get a [device](structdevice.md "device") reference from a devicetree compatible.

If an enabled devicetree node has the given compatible and a device object was created from it, this returns a pointer to that device.

If there are no such devices, this will fail at compile time.

If there are multiple, this returns an arbitrary one.

If this returns non-NULL, the device must be checked for readiness before use, e.g. with [device\_is\_ready()](#gaa4944bd850e90cbd52b0489f9b12edfb).

Parameters
:   | compat | lowercase-and-underscores devicetree compatible |
    | --- | --- |

Returns
:   a pointer to a device

## [◆ ](#ga6ce1dbfda6847ca6c3858712e9b41989)DEVICE\_DT\_GET\_OR\_NULL

| #define DEVICE\_DT\_GET\_OR\_NULL | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_STATUS\_OKAY](group__devicetree-generic-exist.md#gaed773a8782fe00db90e8599ff673e8ed)(node\_id), \

([DEVICE\_DT\_GET](#ga9a65996ce21f43acb7db061e23b48ec7)(node\_id)), ([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)))

[DT\_NODE\_HAS\_STATUS\_OKAY](group__devicetree-generic-exist.md#gaed773a8782fe00db90e8599ff673e8ed)

#define DT\_NODE\_HAS\_STATUS\_OKAY(node\_id)

Does a node identifier refer to a node with a status okay?

**Definition** devicetree.h:3690

Utility macro to obtain an optional reference to a device.

If the node identifier refers to a node with status okay, this returns [DEVICE\_DT\_GET(node\_id)](#ga9a65996ce21f43acb7db061e23b48ec7). Otherwise, it returns [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |

Returns
:   a [device](structdevice.md "device") reference for the node identifier, which may be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

## [◆ ](#gada5ba4aca9e0662ccebb2232c7256419)DEVICE\_DT\_INST\_DEFINE

| #define DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[device.h](device_8h.md)>`

**Value:**

[DEVICE\_DT\_DEFINE](#gac49e26fbe91a14307d5ea08d41561dd1)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[DEVICE\_DT\_DEFINE](#gac49e26fbe91a14307d5ea08d41561dd1)

#define DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api,...)

Create a device object from a devicetree node identifier and set it up for boot time initialization.

**Definition** device.h:229

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

Like [DEVICE\_DT\_DEFINE()](#gac49e26fbe91a14307d5ea08d41561dd1), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier.

Parameters
:   | inst | Instance number. The node\_id argument to [DEVICE\_DT\_DEFINE()](#gac49e26fbe91a14307d5ea08d41561dd1) is set to [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible."). |
    | --- | --- |
    | ... | Other parameters as expected by [DEVICE\_DT\_DEFINE()](#gac49e26fbe91a14307d5ea08d41561dd1). |

## [◆ ](#ga9165e550ae175ce305eafe33390af78b)DEVICE\_DT\_INST\_GET

| #define DEVICE\_DT\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

[DEVICE\_DT\_GET](#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Get a [device](structdevice.md "device") reference for an instance of a DT\_DRV\_COMPAT compatible.

This is equivalent to [DEVICE\_DT\_GET(DT\_DRV\_INST(inst))](#ga9a65996ce21f43acb7db061e23b48ec7).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   A pointer to the device object created for that instance

## [◆ ](#gad864d7a50ee45285dacd68be1e5a49ce)DEVICE\_DT\_NAME

| #define DEVICE\_DT\_NAME | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, label, [DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)(node\_id))

[DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)

#define DT\_NODE\_FULL\_NAME(node\_id)

Get a devicetree node's name with unit-address as a string literal.

**Definition** devicetree.h:537

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:935

Return a string name for a devicetree node.

This macro returns a string literal usable as a device's name from a devicetree node identifier.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |

Returns
:   The value of the node's label property, if it has one. Otherwise, the node's full name in node-name@unit-address form.

## [◆ ](#ga8ebbf17ef805817aa638f36f177a1a0e)DEVICE\_DT\_NAME\_GET

| #define DEVICE\_DT\_NAME\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

[DEVICE\_NAME\_GET](#ga430eb7530aeb3cff5708b55f9b571eb9)(Z\_DEVICE\_DT\_DEV\_ID(node\_id))

The name of the global device object for `node_id`.

Returns the name of the global device structure as a C identifier. The device must be allocated using [DEVICE\_DT\_DEFINE()](#gac49e26fbe91a14307d5ea08d41561dd1) or [DEVICE\_DT\_INST\_DEFINE()](#gada5ba4aca9e0662ccebb2232c7256419) for this to work.

This macro is normally only useful within device driver source code. In other situations, you are probably looking for [DEVICE\_DT\_GET()](#ga9a65996ce21f43acb7db061e23b48ec7).

Parameters
:   | node\_id | Devicetree node identifier |
    | --- | --- |

Returns
:   The name of the device object as a C identifier

## [◆ ](#gaf9403e7eb573a30d2dfaed357f4ef3f4)DEVICE\_GET

| #define DEVICE\_GET | ( |  | *dev\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

(&[DEVICE\_NAME\_GET](#ga430eb7530aeb3cff5708b55f9b571eb9)(dev\_id))

Obtain a pointer to a device object by name.

Return the address of a device object created by [DEVICE\_DEFINE()](#gac12521f4d900e8947aac45c1b228366d), using the dev\_id provided to [DEVICE\_DEFINE()](#gac12521f4d900e8947aac45c1b228366d).

Parameters
:   | dev\_id | Device identifier. |
    | --- | --- |

Returns
:   A pointer to the device object created by [DEVICE\_DEFINE()](#gac12521f4d900e8947aac45c1b228366d)

## [◆ ](#ga4dd918c3a59b8afa185a4851165d2ca0)DEVICE\_HANDLE\_NULL

| #define DEVICE\_HANDLE\_NULL   0 |
| --- |

`#include <[device.h](device_8h.md)>`

Flag value used to identify an unknown device.

## [◆ ](#gad829bbf36723e8cb6c3df8f996a908be)DEVICE\_INIT\_DT\_GET

| #define DEVICE\_INIT\_DT\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

(&Z\_INIT\_ENTRY\_NAME([DEVICE\_DT\_NAME\_GET](#ga8ebbf17ef805817aa638f36f177a1a0e)(node\_id)))

Get a [init\_entry](structinit__entry.md "init_entry") reference from a devicetree node.

Parameters
:   | node\_id | A devicetree node identifier |
    | --- | --- |

Returns
:   A pointer to the [init\_entry](structinit__entry.md "init_entry") object created for that node

## [◆ ](#ga7b7d3030fea734304c61665e75191cc0)DEVICE\_INIT\_GET

| #define DEVICE\_INIT\_GET | ( |  | *dev\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

(&Z\_INIT\_ENTRY\_NAME([DEVICE\_NAME\_GET](#ga430eb7530aeb3cff5708b55f9b571eb9)(dev\_id)))

Get a [init\_entry](structinit__entry.md "init_entry") reference from a device identifier.

Parameters
:   | dev\_id | Device identifier. |
    | --- | --- |

Returns
:   A pointer to the [init\_entry](structinit__entry.md "Structure to store initialization entry information.") object created for that device

## [◆ ](#ga430eb7530aeb3cff5708b55f9b571eb9)DEVICE\_NAME\_GET

| #define DEVICE\_NAME\_GET | ( |  | *dev\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

**Value:**

\_CONCAT(\_\_device\_, dev\_id)

Expands to the name of a global device object.

Return the full name of a device object symbol created by [DEVICE\_DEFINE()](#gac12521f4d900e8947aac45c1b228366d), using the dev\_id provided to [DEVICE\_DEFINE()](#gac12521f4d900e8947aac45c1b228366d). This is the name of the global variable storing the device structure, not a pointer to the string in the [device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d "device::name") field.

It is meant to be used for declaring extern symbols pointing to device objects before using the DEVICE\_GET macro to get the device object.

This macro is normally only useful within device driver source code. In other situations, you are probably looking for [device\_get\_binding()](#ga15386ca9ab38f3e30183c18f604fa835).

Parameters
:   | dev\_id | Device identifier. |
    | --- | --- |

Returns
:   The full name of the device object defined by device definition macros.

## Typedef Documentation

## [◆ ](#ga21415b8e9967ecd2c3d3d3b1724f93c3)device\_handle\_t

| typedef [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) |
| --- |

`#include <[device.h](device_8h.md)>`

Type used to represent a "handle" for a device.

Every [device](structdevice.md "device") has an associated handle. You can get a pointer to a [device](structdevice.md "device") from its handle and vice versa, but the handle uses less space than a pointer. The device.h API mainly uses handles to store lists of multiple devices in a compact way.

The extreme values and zero have special significance. Negative values identify functionality that does not correspond to a Zephyr device, such as the system clock or a [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") function.

See also
:   [device\_handle\_get()](#ga456366a9ca0a8e97484c97c279745203)
:   [device\_from\_handle()](#ga73680daef9f8d7dc2541d83d09737f4a)

## [◆ ](#ga9a1118e5c76c44c998f7258a7de0bfbb)device\_visitor\_callback\_t

| typedef int(\* device\_visitor\_callback\_t) (const struct [device](structdevice.md) \*dev, void \*context) |
| --- |

`#include <[device.h](device_8h.md)>`

Prototype for functions used when iterating over a set of devices.

Such a function may be used in API that identifies a set of devices and provides a visitor API supporting caller-specific interaction with each device in the set.

The visit is said to succeed if the visitor returns a non-negative value.

Parameters
:   | dev | a device in the set being iterated |
    | --- | --- |
    | context | state used to support the visitor function |

Returns
:   A non-negative number to allow walking to continue, and a negative error code to case the iteration to stop.

See also
:   [device\_required\_foreach()](#ga6e3b6dbb15ca28d6c94ee07702663245)
:   [device\_supported\_foreach()](#gaf5fce5e93fd6d5e13aa8b20251b82b2a)

## Function Documentation

## [◆ ](#ga73680daef9f8d7dc2541d83d09737f4a)device\_from\_handle()

| | const struct [device](structdevice.md) \* device\_from\_handle | ( | [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) | *dev\_handle* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

Get the device corresponding to a handle.

Parameters
:   | dev\_handle | the device handle |
    | --- | --- |

Returns
:   the device that has that handle, or a null pointer if `dev_handle` does not identify a device.

## [◆ ](#ga15386ca9ab38f3e30183c18f604fa835)device\_get\_binding()

| const struct [device](structdevice.md) \* device\_get\_binding | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

Get a [device](structdevice.md "device") reference from its [device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d "device::name") field.

This function iterates through the devices on the system. If a device with the given `name` field is found, and that device initialized successfully at boot time, this function returns a pointer to the device.

If no device has the given `name`, this function returns [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4).

This function also returns NULL when a device is found, but it failed to initialize successfully at boot time. (To troubleshoot this case, set a breakpoint on your device driver's initialization function.)

Parameters
:   | name | device name to search for. A null pointer, or a pointer to an empty string, will cause NULL to be returned. |
    | --- | --- |

Returns
:   pointer to device structure with the given name; [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if the device is not found or if the device with that name's initialization function failed.

## [◆ ](#ga456366a9ca0a8e97484c97c279745203)device\_handle\_get()

| | [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) device\_handle\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

Get the handle for a given device.

Parameters
:   | dev | the device for which a handle is desired. |
    | --- | --- |

Returns
:   the handle for the device, or DEVICE\_HANDLE\_NULL if the device does not have an associated handle.

## [◆ ](#gaeea4f9c9f14ab12d224378ab90231c09)device\_init()

| int device\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

Initialize a device.

A device whose initialization was deferred (by marking it as zephyr,deferred-init on devicetree) needs to be initialized manually via this call. Note that only devices whose initialization was deferred can be initialized via this call - one can not try to initialize a non initialization deferred device that failed initialization with this call.

Parameters
:   | dev | device to be initialized. |
    | --- | --- |

Return values
:   | -ENOENT | If device was not found - or isn't a deferred one. |
    | --- | --- |
    | -errno | For other errors. |

## [◆ ](#gae89b0d818c45fdf258c0a421bc103ddc)device\_injected\_handles\_get()

| | const [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* device\_injected\_handles\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *count* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

Get the device handles for injected dependencies of this device.

This function returns a pointer to an array of device handles. The length of the array is stored in the `count` parameter.

The array contains a handle for each device that `dev` manually injected as a dependency, via providing extra arguments to Z\_DEVICE\_DEFINE. This does not include transitive dependencies; you must recursively determine those.

Parameters
:   | dev | the device for which injected dependencies are desired. |
    | --- | --- |
    | count | pointer to where this function should store the length of the returned array. No value is stored if the call returns a null pointer. The value may be set to zero if the device has no devicetree dependencies. |

Returns
:   a pointer to a sequence of `*count` device handles, or a null pointer if `dev` does not have any dependency data.

## [◆ ](#gaa4944bd850e90cbd52b0489f9b12edfb)device\_is\_ready()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) device\_is\_ready | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

Verify that a device is ready for use.

Indicates whether the provided device pointer is for a device known to be in a state where it can be used with its standard API.

This can be used with device pointers captured from [DEVICE\_DT\_GET()](#ga9a65996ce21f43acb7db061e23b48ec7), which does not include the readiness checks of [device\_get\_binding()](#ga15386ca9ab38f3e30183c18f604fa835). At minimum this means that the device has been successfully initialized.

Parameters
:   | dev | pointer to the device in question. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If the device is ready for use. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If the device is not ready for use or if a NULL device pointer is passed as argument. |

## [◆ ](#ga6e3b6dbb15ca28d6c94ee07702663245)device\_required\_foreach()

| int device\_required\_foreach | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [device\_visitor\_callback\_t](#ga9a1118e5c76c44c998f7258a7de0bfbb) | *visitor\_cb*, |
|  |  | void \* | *context* ) |

`#include <[device.h](device_8h.md)>`

Visit every device that `dev` directly requires.

Zephyr maintains information about which devices are directly required by another device; for example an I2C-based sensor driver will require an I2C controller for communication. Required devices can derive from statically-defined devicetree relationships or dependencies registered at runtime.

This API supports operating on the set of required devices. Example uses include making sure required devices are ready before the requiring device is used, and releasing them when the requiring device is no longer needed.

There is no guarantee on the order in which required devices are visited.

If the `visitor_cb` function returns a negative value iteration is halted, and the returned value from the visitor is returned from this function.

Note
:   This API is not available to unprivileged threads.

Parameters
:   | dev | a device of interest. The devices that this device depends on will be used as the set of devices to visit. This parameter must not be null. |
    | --- | --- |
    | visitor\_cb | the function that should be invoked on each device in the dependency set. This parameter must not be null. |
    | context | state that is passed through to the visitor function. This parameter may be null if `visitor_cb` tolerates a null `context`. |

Returns
:   The number of devices that were visited if all visits succeed, or the negative value returned from the first visit that did not succeed.

## [◆ ](#ga2157bbfc2deecfae6514f58221663618)device\_required\_handles\_get()

| | const [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* device\_required\_handles\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *count* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

Get the device handles for devicetree dependencies of this device.

This function returns a pointer to an array of device handles. The length of the array is stored in the `count` parameter.

The array contains a handle for each device that `dev` requires directly, as determined from the devicetree. This does not include transitive dependencies; you must recursively determine those.

Parameters
:   | dev | the device for which dependencies are desired. |
    | --- | --- |
    | count | pointer to where this function should store the length of the returned array. No value is stored if the call returns a null pointer. The value may be set to zero if the device has no devicetree dependencies. |

Returns
:   a pointer to a sequence of `count` device handles, or a null pointer if `dev` does not have any dependency data.

## [◆ ](#gaf5fce5e93fd6d5e13aa8b20251b82b2a)device\_supported\_foreach()

| int device\_supported\_foreach | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [device\_visitor\_callback\_t](#ga9a1118e5c76c44c998f7258a7de0bfbb) | *visitor\_cb*, |
|  |  | void \* | *context* ) |

`#include <[device.h](device_8h.md)>`

Visit every device that `dev` directly supports.

Zephyr maintains information about which devices are directly supported by another device; for example an I2C controller will support an I2C-based sensor driver. Supported devices can derive from statically-defined devicetree relationships.

This API supports operating on the set of supported devices. Example uses include iterating over the devices connected to a regulator when it is powered on.

There is no guarantee on the order in which required devices are visited.

If the `visitor_cb` function returns a negative value iteration is halted, and the returned value from the visitor is returned from this function.

Note
:   This API is not available to unprivileged threads.

Parameters
:   | dev | a device of interest. The devices that this device supports will be used as the set of devices to visit. This parameter must not be null. |
    | --- | --- |
    | visitor\_cb | the function that should be invoked on each device in the support set. This parameter must not be null. |
    | context | state that is passed through to the visitor function. This parameter may be null if `visitor_cb` tolerates a null `context`. |

Returns
:   The number of devices that were visited if all visits succeed, or the negative value returned from the first visit that did not succeed.

## [◆ ](#ga3c9ae15d3224c792b915b107b2d5d00f)device\_supported\_handles\_get()

| | const [device\_handle\_t](#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* device\_supported\_handles\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *count* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device.h](device_8h.md)>`

Get the set of handles that this device supports.

This function returns a pointer to an array of device handles. The length of the array is stored in the `count` parameter.

The array contains a handle for each device that `dev` "supports" – that is, devices that require `dev` directly – as determined from the devicetree. This does not include transitive dependencies; you must recursively determine those.

Parameters
:   | dev | the device for which supports are desired. |
    | --- | --- |
    | count | pointer to where this function should store the length of the returned array. No value is stored if the call returns a null pointer. The value may be set to zero if nothing in the devicetree depends on `dev`. |

Returns
:   a pointer to a sequence of `*count` device handles, or a null pointer if `dev` does not have any dependency data.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
