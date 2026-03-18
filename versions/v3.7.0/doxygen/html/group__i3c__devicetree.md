---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__i3c__devicetree.html
original_path: doxygen/html/group__i3c__devicetree.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I3C Devicetree related bits

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

I3C Devicetree related bits.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [I3C\_DEVICE\_ID\_DT](#ga917b45ec38e08d0c464cebe3372b682e)(node\_id) |
|  | Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from devicetree. |
| #define | [I3C\_DEVICE\_ID\_DT\_INST](#gadc45c0fdd41c081a0c3767159aae0c57)(inst) |
|  | Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from devicetree instance. |
| #define | [I3C\_DEVICE\_DESC\_DT](#ga07eca721a06080900d976474138346fc)(node\_id) |
|  | Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree. |
| #define | [I3C\_DEVICE\_DESC\_DT\_INST](#gafb9b50f7d6e288d1722db5b4176742e9)(inst) |
|  | Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree instance. |
| #define | [I3C\_DEVICE\_DESC\_DT\_FILTERED](#gae5c3df5af3fe52476a506c4eff34ca1e)(node\_id) |
|  | Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree. |
| #define | [I3C\_DEVICE\_ARRAY\_DT](#ga88aac6c42bbcd2f3276b6686c6786363)(node\_id) |
|  | Array initializer for a list of [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree. |
| #define | [I3C\_DEVICE\_ARRAY\_DT\_INST](#ga3153fd2d2b68eb760730827f6d6986c5)(inst) |
|  | Array initializer for a list of [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree instance. |
| #define | [I3C\_DEVICE\_DT\_DEFINE](#gaab3219d45b125dd12d583bfd1823a61c)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with I3C target device specifics. |
| #define | [I3C\_DEVICE\_DT\_INST\_DEFINE](#ga77a471977d2c6edc530d3ce0febb8dbe)(inst, ...) |
|  | Like I3C\_TARGET\_DT\_DEFINE() for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [I3C\_I2C\_DEVICE\_DESC\_DT](#gaf317b1bcec787d594d3952dda2b9dc51)(node\_id) |
|  | Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree. |
| #define | [I3C\_I2C\_DEVICE\_DESC\_DT\_INST](#ga4c004a38164a56a1d1d027f2d29974e4)(inst) |
|  | Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree instance. |
| #define | [I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED](#ga703052c71216a4f152028540592ad581)(node\_id) |
|  | Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree. |
| #define | [I3C\_I2C\_DEVICE\_ARRAY\_DT](#ga78f4d3fa3977989a731e33089d535701)(node\_id) |
|  | Array initializer for a list of [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree. |
| #define | [I3C\_I2C\_DEVICE\_ARRAY\_DT\_INST](#gab441564c36a5d7e0856bba5eed51906f)(inst) |
|  | Array initializer for a list of [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree instance. |

## Detailed Description

I3C Devicetree related bits.

## Macro Definition Documentation

## [◆ ](#ga88aac6c42bbcd2f3276b6686c6786363)I3C\_DEVICE\_ARRAY\_DT

| #define I3C\_DEVICE\_ARRAY\_DT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

{ \

DT\_FOREACH\_CHILD\_STATUS\_OKAY( \

node\_id, \

[I3C\_DEVICE\_DESC\_DT\_FILTERED](#gae5c3df5af3fe52476a506c4eff34ca1e)) \

}

[I3C\_DEVICE\_DESC\_DT\_FILTERED](#gae5c3df5af3fe52476a506c4eff34ca1e)

#define I3C\_DEVICE\_DESC\_DT\_FILTERED(node\_id)

Structure initializer for i3c\_device\_desc from devicetree.

**Definition** devicetree.h:90

Array initializer for a list of [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree.

This is a helper macro to generate an array for a list of [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from device tree.

Parameters
:   | node\_id | Devicetree node identifier of the I3C controller |
    | --- | --- |

## [◆ ](#ga3153fd2d2b68eb760730827f6d6986c5)I3C\_DEVICE\_ARRAY\_DT\_INST

| #define I3C\_DEVICE\_ARRAY\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[I3C\_DEVICE\_ARRAY\_DT](#ga88aac6c42bbcd2f3276b6686c6786363)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

[I3C\_DEVICE\_ARRAY\_DT](#ga88aac6c42bbcd2f3276b6686c6786363)

#define I3C\_DEVICE\_ARRAY\_DT(node\_id)

Array initializer for a list of i3c\_device\_desc from devicetree.

**Definition** devicetree.h:102

Array initializer for a list of [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree instance.

This is equivalent to [I3C\_DEVICE\_ARRAY\_DT(DT\_DRV\_INST(inst))](#ga88aac6c42bbcd2f3276b6686c6786363).

Parameters
:   | inst | Devicetree instance number of the I3C controller |
    | --- | --- |

## [◆ ](#ga07eca721a06080900d976474138346fc)I3C\_DEVICE\_DESC\_DT

| #define I3C\_DEVICE\_DESC\_DT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

{ \

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id)), \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)(node\_id), \

.static\_addr = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 0), \

.pid = (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 1) << 32)\

| [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 2), \

.init\_dynamic\_addr = \

DT\_PROP\_OR(node\_id, assigned\_address, 0), \

},

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:246

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3556

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:809

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree.

This helper macro expands to a static initializer for a struct
[i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") by reading the relevant bus and device data from the devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the I3C device whose struct [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") to create an initializer for |
    | --- | --- |

## [◆ ](#gae5c3df5af3fe52476a506c4eff34ca1e)I3C\_DEVICE\_DESC\_DT\_FILTERED

| #define I3C\_DEVICE\_DESC\_DT\_FILTERED | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)([DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 1), \

(), ([I3C\_DEVICE\_DESC\_DT](#ga07eca721a06080900d976474138346fc)(node\_id)))

[I3C\_DEVICE\_DESC\_DT](#ga07eca721a06080900d976474138346fc)

#define I3C\_DEVICE\_DESC\_DT(node\_id)

Structure initializer for i3c\_device\_desc from devicetree.

**Definition** devicetree.h:62

[COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)

#define COND\_CODE\_0(\_flag, \_if\_0\_code, \_else\_code)

Like COND\_CODE\_1() except tests if \_flag is 0.

**Definition** util\_macro.h:195

Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree.

This is mainly used by [I3C\_DEVICE\_ARRAY\_DT()](#ga88aac6c42bbcd2f3276b6686c6786363) to only create a struct if and only if it is an I3C device.

## [◆ ](#gafb9b50f7d6e288d1722db5b4176742e9)I3C\_DEVICE\_DESC\_DT\_INST

| #define I3C\_DEVICE\_DESC\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[I3C\_DEVICE\_DESC\_DT](#ga07eca721a06080900d976474138346fc)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree instance.

This is equivalent to [I3C\_DEVICE\_DESC\_DT(DT\_DRV\_INST(inst))](#ga07eca721a06080900d976474138346fc).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#gaab3219d45b125dd12d583bfd1823a61c)I3C\_DEVICE\_DT\_DEFINE

| #define I3C\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | ... ) |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[DEVICE\_DT\_DEFINE](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)(node\_id, init\_fn, pm, data, config, level, \

prio, api, \_\_VA\_ARGS\_\_)

[DEVICE\_DT\_DEFINE](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)

#define DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api,...)

Create a device object from a devicetree node identifier and set it up for boot time initialization.

**Definition** device.h:195

Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with I3C target device specifics.

Defines a I3C target device which implements the I3C target device API.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Name of the init function of the driver. |
    | pm | PM device resources reference (NULL if device does not use PM). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | level | The initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | prio | Priority within the selected initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |

## [◆ ](#ga77a471977d2c6edc530d3ce0febb8dbe)I3C\_DEVICE\_DT\_INST\_DEFINE

| #define I3C\_DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[I3C\_DEVICE\_DT\_DEFINE](#gaab3219d45b125dd12d583bfd1823a61c)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[I3C\_DEVICE\_DT\_DEFINE](#gaab3219d45b125dd12d583bfd1823a61c)

#define I3C\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api,...)

Like DEVICE\_DT\_DEFINE() with I3C target device specifics.

**Definition** devicetree.h:145

Like I3C\_TARGET\_DT\_DEFINE() for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to I3C\_TARGET\_DT\_DEFINE(). |
    | --- | --- |
    | ... | other parameters as expected by I3C\_TARGET\_DT\_DEFINE(). |

## [◆ ](#ga917b45ec38e08d0c464cebe3372b682e)I3C\_DEVICE\_ID\_DT

| #define I3C\_DEVICE\_ID\_DT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

{ \

.pid = (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 1) << 32)\

| [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 2), \

}

Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from devicetree.

This helper macro expands to a static initializer for a struct
[i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") by reading the relevant device data from devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the I3C device whose struct [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") to create an initializer for |
    | --- | --- |

## [◆ ](#gadc45c0fdd41c081a0c3767159aae0c57)I3C\_DEVICE\_ID\_DT\_INST

| #define I3C\_DEVICE\_ID\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[I3C\_DEVICE\_ID\_DT](#ga917b45ec38e08d0c464cebe3372b682e)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[I3C\_DEVICE\_ID\_DT](#ga917b45ec38e08d0c464cebe3372b682e)

#define I3C\_DEVICE\_ID\_DT(node\_id)

Structure initializer for i3c\_device\_id from devicetree.

**Definition** devicetree.h:35

Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from devicetree instance.

This is equivalent to [I3C\_DEVICE\_ID\_DT(DT\_DRV\_INST(inst))](#ga917b45ec38e08d0c464cebe3372b682e).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#ga78f4d3fa3977989a731e33089d535701)I3C\_I2C\_DEVICE\_ARRAY\_DT

| #define I3C\_I2C\_DEVICE\_ARRAY\_DT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

{ \

DT\_FOREACH\_CHILD\_STATUS\_OKAY( \

node\_id, \

[I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED](#ga703052c71216a4f152028540592ad581)) \

}

[I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED](#ga703052c71216a4f152028540592ad581)

#define I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED(node\_id)

Structure initializer for i3c\_i2c\_device\_desc from devicetree.

**Definition** devicetree.h:196

Array initializer for a list of [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree.

This is a helper macro to generate an array for a list of [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from device tree.

Parameters
:   | node\_id | Devicetree node identifier of the I3C controller |
    | --- | --- |

## [◆ ](#gab441564c36a5d7e0856bba5eed51906f)I3C\_I2C\_DEVICE\_ARRAY\_DT\_INST

| #define I3C\_I2C\_DEVICE\_ARRAY\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[I3C\_I2C\_DEVICE\_ARRAY\_DT](#ga78f4d3fa3977989a731e33089d535701)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[I3C\_I2C\_DEVICE\_ARRAY\_DT](#ga78f4d3fa3977989a731e33089d535701)

#define I3C\_I2C\_DEVICE\_ARRAY\_DT(node\_id)

Array initializer for a list of i3c\_i2c\_device\_desc from devicetree.

**Definition** devicetree.h:208

Array initializer for a list of [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree instance.

This is equivalent to [I3C\_I2C\_DEVICE\_ARRAY\_DT(DT\_DRV\_INST(inst))](#ga78f4d3fa3977989a731e33089d535701).

Parameters
:   | inst | Devicetree instance number of the I3C controller |
    | --- | --- |

## [◆ ](#gaf317b1bcec787d594d3952dda2b9dc51)I3C\_I2C\_DEVICE\_DESC\_DT

| #define I3C\_I2C\_DEVICE\_DESC\_DT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

{ \

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id)), \

.addr = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 0), \

.lvr = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 2), \

},

Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree.

This helper macro expands to a static initializer for a struct
[i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") by reading the relevant bus and device data from the devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the I3C device whose struct [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") to create an initializer for |
    | --- | --- |

## [◆ ](#ga703052c71216a4f152028540592ad581)I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED

| #define I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)([DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, reg, 1), \

([I3C\_I2C\_DEVICE\_DESC\_DT](#gaf317b1bcec787d594d3952dda2b9dc51)(node\_id)), ())

[I3C\_I2C\_DEVICE\_DESC\_DT](#gaf317b1bcec787d594d3952dda2b9dc51)

#define I3C\_I2C\_DEVICE\_DESC\_DT(node\_id)

Structure initializer for i3c\_i2c\_device\_desc from devicetree.

**Definition** devicetree.h:171

Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree.

This is mainly used by [I3C\_I2C\_DEVICE\_ARRAY\_DT()](#ga78f4d3fa3977989a731e33089d535701) to only create a struct if and only if it is an I2C device.

## [◆ ](#ga4c004a38164a56a1d1d027f2d29974e4)I3C\_I2C\_DEVICE\_DESC\_DT\_INST

| #define I3C\_I2C\_DEVICE\_DESC\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](drivers_2i3c_2devicetree_8h.md)>`

**Value:**

[I3C\_I2C\_DEVICE\_DESC\_DT](#gaf317b1bcec787d594d3952dda2b9dc51)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree instance.

This is equivalent to [I3C\_I2C\_DEVICE\_DESC\_DT(DT\_DRV\_INST(inst))](#gaf317b1bcec787d594d3952dda2b9dc51).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
