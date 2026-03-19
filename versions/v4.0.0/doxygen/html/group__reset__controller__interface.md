---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__reset__controller__interface.html
original_path: doxygen/html/group__reset__controller__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Reset Controller Interface

[Device Driver APIs](group__io__interfaces.md)

Reset Controller Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [reset\_dt\_spec](structreset__dt__spec.md) |
|  | Reset controller device configuration. [More...](structreset__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [RESET\_DT\_SPEC\_GET\_BY\_IDX](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)(node\_id, idx) |
|  | Static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |
| #define | [RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR](#ga594221ce06a743b591ef285856981793)(node\_id, idx, default\_value) |
|  | Like [RESET\_DT\_SPEC\_GET\_BY\_IDX()](#ga9f2e9e2e14a6ec9d2848979c77ecad9b), with a fallback to a default value. |
| #define | [RESET\_DT\_SPEC\_GET](#gac4b466f492ae7a1c4e19647f41749c6b)(node\_id) |
|  | Equivalent to [RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](#ga9f2e9e2e14a6ec9d2848979c77ecad9b). |
| #define | [RESET\_DT\_SPEC\_GET\_OR](#ga66fa2c042d282b34939bc762240d3705)(node\_id, default\_value) |
|  | Equivalent to [RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](#ga594221ce06a743b591ef285856981793). |
| #define | [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX](#ga539688cb73d17aa02b137fc90965350b)(inst, idx) |
|  | Static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")` from a DT\_DRV\_COMPAT instance's Reset Controller property at an index. |
| #define | [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#ga7d14fdead7518b4070ec7123130311b2)(inst, idx, default\_value) |
|  | Static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")` from a DT\_DRV\_COMPAT instance's 'resets' property at an index, with fallback. |
| #define | [RESET\_DT\_SPEC\_INST\_GET](#ga1557bbcabdf02c3db1aa0705ce80baf0)(inst) |
|  | Equivalent to [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](#ga539688cb73d17aa02b137fc90965350b). |
| #define | [RESET\_DT\_SPEC\_INST\_GET\_OR](#gadcb4cd7adabb84a479485da421d39c6c)(inst, default\_value) |
|  | Equivalent to [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](#ga7d14fdead7518b4070ec7123130311b2). |

| Functions | |
| --- | --- |
| int | [reset\_status](#gad58d0bfcf0b9cd4ba11b163e97ba8762) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the reset status. |
| static int | [reset\_status\_dt](#gaa5d00726d387ff44244bc939a943963d) (const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the reset status from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |
| int | [reset\_line\_assert](#gab7b58d253be9083b4ed7c35bc60c6aa6) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Put the device in reset state. |
| static int | [reset\_line\_assert\_dt](#gabfe4a15880e38cbf30e293f9143d5080) (const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec) |
|  | Assert the reset state from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |
| int | [reset\_line\_deassert](#gaadd2d70e57e620e9f12900c561fea941) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Take out the device from reset state. |
| static int | [reset\_line\_deassert\_dt](#ga7c747373b556ee1c00bad4afcdd138c0) (const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec) |
|  | Deassert the reset state from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |
| int | [reset\_line\_toggle](#ga29fb7d474e46d7a5a69ab8fb87ddbc5e) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Reset the device. |
| static int | [reset\_line\_toggle\_dt](#gaf3db170375c24999ea1b1954fb3ae184) (const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec) |
|  | Reset the device from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |

## Detailed Description

Reset Controller Interface.

Since
:   3.1

Version
:   0.2.0

## Macro Definition Documentation

## [◆ ](#gac4b466f492ae7a1c4e19647f41749c6b)RESET\_DT\_SPEC\_GET

| #define RESET\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[reset.h](drivers_2reset_8h.md)>`

**Value:**

[RESET\_DT\_SPEC\_GET\_BY\_IDX](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)(node\_id, 0)

[RESET\_DT\_SPEC\_GET\_BY\_IDX](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)

#define RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)

Static initializer for a reset\_dt\_spec.

**Definition** reset.h:71

Equivalent to [RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](#ga9f2e9e2e14a6ec9d2848979c77ecad9b).

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |

Returns
:   static initializer for a struct [reset\_dt\_spec](structreset__dt__spec.md "Reset controller device configuration.") for the property

See also
:   [RESET\_DT\_SPEC\_GET\_BY\_IDX()](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)

## [◆ ](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)RESET\_DT\_SPEC\_GET\_BY\_IDX

| #define RESET\_DT\_SPEC\_GET\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

**Value:**

{ \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_RESET\_CTLR\_BY\_IDX](group__devicetree-reset-controller.md#gaa730fe6a58ee0a2d9daf7e125048f9e6)(node\_id, idx)), \

.id = [DT\_RESET\_ID\_BY\_IDX](group__devicetree-reset-controller.md#ga4259b4aa8bfe6f4ccb268c180541237d)(node\_id, idx) \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:255

[DT\_RESET\_ID\_BY\_IDX](group__devicetree-reset-controller.md#ga4259b4aa8bfe6f4ccb268c180541237d)

#define DT\_RESET\_ID\_BY\_IDX(node\_id, idx)

Get a Reset Controller specifier's id cell at an index.

**Definition** reset.h:269

[DT\_RESET\_CTLR\_BY\_IDX](group__devicetree-reset-controller.md#gaa730fe6a58ee0a2d9daf7e125048f9e6)

#define DT\_RESET\_CTLR\_BY\_IDX(node\_id, idx)

Get the node identifier for the controller phandle from a "resets" phandle-array property at an index...

**Definition** reset.h:50

Static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`.

This returns a static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")` structure given a devicetree node identifier, a property specifying a Reset Controller and an index.

Example devicetree fragment:

```
 n: node {
    resets = <&reset 10>;
 }
```

Example usage:

```
 const struct reset_dt_spec spec = RESET_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n), 0);
 // Initializes 'spec' to:
 // {
 //         .dev = DEVICE_DT_GET(DT_NODELABEL(reset)),
 //         .id = 10
 // }
```

The 'reset' field must still be checked for readiness, e.g. using [device\_is\_ready()](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb "Verify that a device is ready for use."). It is an error to use this macro unless the node exists, has the given property, and that property specifies a reset controller reset line id as shown above.

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |
    | idx | logical index into "resets" |

Returns
:   static initializer for a struct [reset\_dt\_spec](structreset__dt__spec.md "Reset controller device configuration.") for the property

## [◆ ](#ga594221ce06a743b591ef285856981793)RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR

| #define RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, resets), \

([RESET\_DT\_SPEC\_GET\_BY\_IDX](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)(node\_id, idx)), \

(default\_value))

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3677

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

Like [RESET\_DT\_SPEC\_GET\_BY\_IDX()](#ga9f2e9e2e14a6ec9d2848979c77ecad9b), with a fallback to a default value.

If the devicetree node identifier 'node\_id' refers to a node with a 'resets' property, this expands to [RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)](#ga9f2e9e2e14a6ec9d2848979c77ecad9b). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |
    | idx | logical index into the 'resets' property |
    | default\_value | fallback value to expand to |

Returns
:   static initializer for a struct [reset\_dt\_spec](structreset__dt__spec.md "Reset controller device configuration.") for the property, or default\_value if the node or property do not exist

## [◆ ](#ga66fa2c042d282b34939bc762240d3705)RESET\_DT\_SPEC\_GET\_OR

| #define RESET\_DT\_SPEC\_GET\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *default\_value* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

**Value:**

[RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR](#ga594221ce06a743b591ef285856981793)(node\_id, 0, default\_value)

[RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR](#ga594221ce06a743b591ef285856981793)

#define RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value)

Like RESET\_DT\_SPEC\_GET\_BY\_IDX(), with a fallback to a default value.

**Definition** reset.h:93

Equivalent to [RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](#ga594221ce06a743b591ef285856981793).

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |
    | default\_value | fallback value to expand to |

Returns
:   static initializer for a struct [reset\_dt\_spec](structreset__dt__spec.md "Reset controller device configuration.") for the property, or default\_value if the node or property do not exist

## [◆ ](#ga1557bbcabdf02c3db1aa0705ce80baf0)RESET\_DT\_SPEC\_INST\_GET

| #define RESET\_DT\_SPEC\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[reset.h](drivers_2reset_8h.md)>`

**Value:**

[RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX](#ga539688cb73d17aa02b137fc90965350b)(inst, 0)

[RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX](#ga539688cb73d17aa02b137fc90965350b)

#define RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx)

Static initializer for a reset\_dt\_spec from a DT\_DRV\_COMPAT instance's Reset Controller property at a...

**Definition** reset.h:129

Equivalent to [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](#ga539688cb73d17aa02b137fc90965350b).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   static initializer for a struct [reset\_dt\_spec](structreset__dt__spec.md "Reset controller device configuration.") for the property

See also
:   [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#ga539688cb73d17aa02b137fc90965350b)

## [◆ ](#ga539688cb73d17aa02b137fc90965350b)RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX

| #define RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

**Value:**

[RESET\_DT\_SPEC\_GET\_BY\_IDX](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

Static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")` from a DT\_DRV\_COMPAT instance's Reset Controller property at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into "resets" |

Returns
:   static initializer for a struct [reset\_dt\_spec](structreset__dt__spec.md "Reset controller device configuration.") for the property

See also
:   [RESET\_DT\_SPEC\_GET\_BY\_IDX()](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)

## [◆ ](#ga7d14fdead7518b4070ec7123130311b2)RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR

| #define RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), resets, idx), \

([RESET\_DT\_SPEC\_GET\_BY\_IDX](#ga9f2e9e2e14a6ec9d2848979c77ecad9b)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)), \

(default\_value))

[DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)

#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx)

Is index idx valid for an array type property?

**Definition** devicetree.h:819

Static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")` from a DT\_DRV\_COMPAT instance's 'resets' property at an index, with fallback.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into the 'resets' property |
    | default\_value | fallback value to expand to |

Returns
:   static initializer for a struct [reset\_dt\_spec](structreset__dt__spec.md "Reset controller device configuration.") for the property, or default\_value if the node or property do not exist

## [◆ ](#gadcb4cd7adabb84a479485da421d39c6c)RESET\_DT\_SPEC\_INST\_GET\_OR

| #define RESET\_DT\_SPEC\_INST\_GET\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *default\_value* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

**Value:**

[RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#ga7d14fdead7518b4070ec7123130311b2)(inst, 0, default\_value)

[RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#ga7d14fdead7518b4070ec7123130311b2)

#define RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, idx, default\_value)

Static initializer for a reset\_dt\_spec from a DT\_DRV\_COMPAT instance's 'resets' property at an index,...

**Definition** reset.h:142

Equivalent to [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](#ga7d14fdead7518b4070ec7123130311b2).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | default\_value | fallback value to expand to |

Returns
:   static initializer for a struct [reset\_dt\_spec](structreset__dt__spec.md "Reset controller device configuration.") for the property, or default\_value if the node or property do not exist

## Function Documentation

## [◆ ](#gab7b58d253be9083b4ed7c35bc60c6aa6)reset\_line\_assert()

| int reset\_line\_assert | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

Put the device in reset state.

This function sets/clears the reset bits of the device, depending on the logic level (active-high/active-low).

Parameters
:   | dev | Reset controller device. |
    | --- | --- |
    | id | Reset line. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -ENOSYS | If the functionality is not implemented by the driver. |
    | -errno | Other negative errno in case of failure. |

## [◆ ](#gabfe4a15880e38cbf30e293f9143d5080)reset\_line\_assert\_dt()

| | int reset\_line\_assert\_dt | ( | const struct [reset\_dt\_spec](structreset__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[reset.h](drivers_2reset_8h.md)>`

Assert the reset state from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`.

This is equivalent to:

```
reset_line_assert(spec->dev, spec->id);
```

Parameters
:   | spec | Reset controller specification from devicetree |
    | --- | --- |

Returns
:   a value from [reset\_line\_assert()](#gab7b58d253be9083b4ed7c35bc60c6aa6)

## [◆ ](#gaadd2d70e57e620e9f12900c561fea941)reset\_line\_deassert()

| int reset\_line\_deassert | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

Take out the device from reset state.

This function sets/clears the reset bits of the device, depending on the logic level (active-low/active-high).

Parameters
:   | dev | Reset controller device. |
    | --- | --- |
    | id | Reset line. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -ENOSYS | If the functionality is not implemented by the driver. |
    | -errno | Other negative errno in case of failure. |

## [◆ ](#ga7c747373b556ee1c00bad4afcdd138c0)reset\_line\_deassert\_dt()

| | int reset\_line\_deassert\_dt | ( | const struct [reset\_dt\_spec](structreset__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[reset.h](drivers_2reset_8h.md)>`

Deassert the reset state from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`.

This is equivalent to:

```
reset_line_deassert(spec->dev, spec->id)
```

Parameters
:   | spec | Reset controller specification from devicetree |
    | --- | --- |

Returns
:   a value from [reset\_line\_deassert()](#gaadd2d70e57e620e9f12900c561fea941)

## [◆ ](#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)reset\_line\_toggle()

| int reset\_line\_toggle | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

Reset the device.

This function performs reset for a device (assert + deassert).

Parameters
:   | dev | Reset controller device. |
    | --- | --- |
    | id | Reset line. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -ENOSYS | If the functionality is not implemented by the driver. |
    | -errno | Other negative errno in case of failure. |

## [◆ ](#gaf3db170375c24999ea1b1954fb3ae184)reset\_line\_toggle\_dt()

| | int reset\_line\_toggle\_dt | ( | const struct [reset\_dt\_spec](structreset__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[reset.h](drivers_2reset_8h.md)>`

Reset the device from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`.

This is equivalent to:

```
reset_line_toggle(spec->dev, spec->id)
```

Parameters
:   | spec | Reset controller specification from devicetree |
    | --- | --- |

Returns
:   a value from [reset\_line\_toggle()](#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)

## [◆ ](#gad58d0bfcf0b9cd4ba11b163e97ba8762)reset\_status()

| int reset\_status | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[reset.h](drivers_2reset_8h.md)>`

Get the reset status.

This function returns the reset status of the device.

Parameters
:   | dev | Reset controller device. |
    | --- | --- |
    | id | Reset line. |
    | status | Where to write the reset status. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -ENOSYS | If the functionality is not implemented by the driver. |
    | -errno | Other negative errno in case of failure. |

## [◆ ](#gaa5d00726d387ff44244bc939a943963d)reset\_status\_dt()

| | int reset\_status\_dt | ( | const struct [reset\_dt\_spec](structreset__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[reset.h](drivers_2reset_8h.md)>`

Get the reset status from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`.

This is equivalent to:

reset\_status(spec->dev, spec->id, status);

Parameters
:   | spec | Reset controller specification from devicetree |
    | --- | --- |
    | status | Where to write the reset status. |

Returns
:   a value from [reset\_status()](#gad58d0bfcf0b9cd4ba11b163e97ba8762)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
