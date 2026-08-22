---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__renesas__elc__interface.html
original_path: doxygen/html/group__renesas__elc__interface.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Renesas ELC driver APIs

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md)

Renesas ELC driver public APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [renesas\_elc\_dt\_spec](structrenesas__elc__dt__spec.md) |
|  | Container for Renesas ELC information specified in devicetree. [More...](structrenesas__elc__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME](#ga32d4b23c3857552a8fe1ca6ce04f97d4)(node\_id, name) |
|  | Get the device pointer from the "renesas-elcs" property by element name. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX](#ga79a705be3efa01b6fcc1413dd4acfec2)(node\_id, idx) |
|  | Get the device pointer from the "renesas-elcs" property by index. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME\_OR\_NULL](#ga996e259c97fc2511086664865b4c0e3d)(node\_id, name) |
|  | Get the device pointer from the "renesas-elcs" property by element name, or return NULL if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX\_OR\_NULL](#ga5e79207cee205406247a972e23360110)(node\_id, idx) |
|  | Get the device pointer from the "renesas-elcs" property by index, or return NULL if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME](#gaab4d583c93f1d5990d4a6733caaded81)(inst, name) |
|  | Get the device pointer from the "renesas-elcs" property by element name for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX](#ga788709121dbfb2db3f74ccf9a9d51002)(inst, idx) |
|  | Get the device pointer from the "renesas-elcs" property by index for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME\_OR\_NULL](#ga1d58940758c664c22cb3e183e9810370)(inst, name) |
|  | Get the device pointer from the "renesas-elcs" property by element name for a DT\_DRV\_COMPAT instance, or return NULL if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX\_OR\_NULL](#ga65ccb580212ee15dc9329d76e810190e)(inst, idx) |
|  | Get the device pointer from the "renesas-elcs" property by index for a DT\_DRV\_COMPAT instance, or return NULL if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME](#ga1f196ad20380dedf193c754906c5ed14)(node\_id, name) |
|  | Get the peripheral cell value from the "renesas-elcs" property by element name. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX](#gace33f51f3a3a2efd42932a816e05be0b)(node\_id, idx) |
|  | Get the peripheral cell value from the "renesas-elcs" property by index. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR](#ga35d7aef6829d74e92fa7c82306711a6c)(node\_id, name, default\_value) |
|  | Get the peripheral cell value from the "renesas-elcs" property by element name, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR](#ga915d2760bd3c8ecf1b689bed286035d8)(node\_id, idx, default\_value) |
|  | Get the peripheral cell value from the "renesas-elcs" property by index, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME](#ga3a0b277cb45636a86bf9b665fd75d133)(inst, name) |
|  | Get the peripheral cell value by element name for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX](#gaeab186e0f09ee56ce87719a7d5566f50)(inst, idx) |
|  | Get the peripheral cell value by index for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME\_OR](#ga0e1c393825d778fd22a9a190eaedc308)(inst, name, default\_value) |
|  | Get the peripheral cell value by element name for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX\_OR](#ga360d362b3fc26afb7cc81bfd28f6fc6a)(inst, idx, default\_value) |
|  | Get the peripheral cell value by index for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME](#ga920e3b26fb52a728ed2a3cd1ab5af7f0)(node\_id, name) |
|  | Get the event cell value from the "renesas-elcs" property by element name. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX](#ga6f3093b0556eb8eb1931e9b8b746245a)(node\_id, idx) |
|  | Get the event cell value from the "renesas-elcs" property by index. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR](#ga41c5adcf8817d529b5521727d9937b42)(node\_id, name, default\_value) |
|  | Get the event cell value from the "renesas-elcs" property by element name, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR](#ga2b0a12781acca4123dd7899446a94b6f)(node\_id, idx, default\_value) |
|  | Get the event cell value from the "renesas-elcs" property by index, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME](#ga86ded9427001c5d3b315b71dcbfad7d0)(inst, name) |
|  | Get the event cell value by element name for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX](#gac5dfa5e30e1ac9ac703842e61dd3fa3b)(inst, idx) |
|  | Get the event cell value by index for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME\_OR](#ga94f2bc95761722c93019371f432da262)(inst, name, default\_value) |
|  | Get the event cell value by element name for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX\_OR](#ga7d57a1a3bf47feda6c2831712bfd033c)(inst, idx, default\_value) |
|  | Get the event cell value by index for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist. |

| Functions | |
| --- | --- |
| int | [renesas\_elc\_software\_event\_generate](#gab3b55b83b38469854aae726a71f6ad55) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event) |
|  | Generate a software event in the Event Link Controller. |
| int | [renesas\_elc\_link\_set](#ga444e17d01310283e61bcde9a1022c47a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event) |
|  | Create a single event link. |
| int | [renesas\_elc\_link\_break](#ga65c950ccf0087c514daf6d543a0a7ecf) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral) |
|  | Break an event link. |
| int | [renesas\_elc\_enable](#gafbffc029fd9482be578bd05cbdb3a03f) (const struct [device](structdevice.md) \*dev) |
|  | Enable the operation of the Event Link Controller. |
| int | [renesas\_elc\_disable](#gaac75089657f841c80225aa40de9c2a93) (const struct [device](structdevice.md) \*dev) |
|  | Disable the operation of the Event Link Controller. |

## Detailed Description

Renesas ELC driver public APIs.

## Macro Definition Documentation

## [◆ ](#ga79a705be3efa01b6fcc1413dd4acfec2)RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX

| #define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, renesas\_elcs, idx))

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:314

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1785

Get the device pointer from the "renesas-elcs" property by index.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |

Returns
:   Device pointer.

## [◆ ](#ga5e79207cee205406247a972e23360110)RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX\_OR\_NULL

| #define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX\_OR\_NULL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DEVICE\_DT\_GET\_OR\_NULL](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)([DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, renesas\_elcs, idx))

[DEVICE\_DT\_GET\_OR\_NULL](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)

#define DEVICE\_DT\_GET\_OR\_NULL(node\_id)

Utility macro to obtain an optional reference to a device.

**Definition** device.h:379

Get the device pointer from the "renesas-elcs" property by index, or return NULL if the property does not exist.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |

Returns
:   Device pointer or NULL.

## [◆ ](#ga32d4b23c3857552a8fe1ca6ce04f97d4)RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME

| #define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, renesas\_elcs, name))

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1733

Get the device pointer from the "renesas-elcs" property by element name.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |

Returns
:   Device pointer.

## [◆ ](#ga996e259c97fc2511086664865b4c0e3d)RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME\_OR\_NULL

| #define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME\_OR\_NULL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DEVICE\_DT\_GET\_OR\_NULL](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)([DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, renesas\_elcs, name))

Get the device pointer from the "renesas-elcs" property by element name, or return NULL if the property does not exist.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |

Returns
:   Device pointer or NULL.

## [◆ ](#ga788709121dbfb2db3f74ccf9a9d51002)RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX

| #define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), renesas\_elcs, idx))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

Get the device pointer from the "renesas-elcs" property by index for a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |

Returns
:   Device pointer.

## [◆ ](#ga65ccb580212ee15dc9329d76e810190e)RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX\_OR\_NULL

| #define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX\_OR\_NULL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DEVICE\_DT\_GET\_OR\_NULL](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)([DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), renesas\_elcs, idx))

Get the device pointer from the "renesas-elcs" property by index for a DT\_DRV\_COMPAT instance, or return NULL if the property does not exist.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |

Returns
:   Device pointer or NULL.

## [◆ ](#gaab4d583c93f1d5990d4a6733caaded81)RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME

| #define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), renesas\_elcs, name))

Get the device pointer from the "renesas-elcs" property by element name for a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |

Returns
:   Device pointer.

## [◆ ](#ga1d58940758c664c22cb3e183e9810370)RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME\_OR\_NULL

| #define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME\_OR\_NULL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DEVICE\_DT\_GET\_OR\_NULL](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)([DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), renesas\_elcs, name))

Get the device pointer from the "renesas-elcs" property by element name for a DT\_DRV\_COMPAT instance, or return NULL if the property does not exist.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |

Returns
:   Device pointer or NULL.

## [◆ ](#ga6f3093b0556eb8eb1931e9b8b746245a)RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX

| #define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, renesas\_elcs, idx, event)

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1564

Get the event cell value from the "renesas-elcs" property by index.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |

Returns
:   Event cell value.

## [◆ ](#ga2b0a12781acca4123dd7899446a94b6f)RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR

| #define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, renesas\_elcs), \

([RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX](#ga6f3093b0556eb8eb1931e9b8b746245a)(node\_id, idx)), \

(default\_value))

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3784

[RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX](#ga6f3093b0556eb8eb1931e9b8b746245a)

#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX(node\_id, idx)

Get the event cell value from the "renesas-elcs" property by index.

**Definition** renesas\_elc.h:264

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

Get the event cell value from the "renesas-elcs" property by index, or return a default value if the property does not exist.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |
    | default\_value | Value to return if the property is not present. |

Returns
:   Event cell value or default\_value.

## [◆ ](#ga920e3b26fb52a728ed2a3cd1ab5af7f0)RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME

| #define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)(node\_id, renesas\_elcs, name, event)

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)

#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)

Get a value within a phandle-array specifier by name.

**Definition** devicetree.h:1659

Get the event cell value from the "renesas-elcs" property by element name.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |

Returns
:   Event cell value.

## [◆ ](#ga41c5adcf8817d529b5521727d9937b42)RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR

| #define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, renesas\_elcs), \

([RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME](#ga920e3b26fb52a728ed2a3cd1ab5af7f0)(node\_id, name)), \

(default\_value))

[RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME](#ga920e3b26fb52a728ed2a3cd1ab5af7f0)

#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME(node\_id, name)

Get the event cell value from the "renesas-elcs" property by element name.

**Definition** renesas\_elc.h:253

Get the event cell value from the "renesas-elcs" property by element name, or return a default value if the property does not exist.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |
    | default\_value | Value to return if the property is not present. |

Returns
:   Event cell value or default\_value.

## [◆ ](#gac5dfa5e30e1ac9ac703842e61dd3fa3b)RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX

| #define RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX](#ga6f3093b0556eb8eb1931e9b8b746245a)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

Get the event cell value by index for a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |

Returns
:   Event cell value.

## [◆ ](#ga7d57a1a3bf47feda6c2831712bfd033c)RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX\_OR

| #define RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR](#ga2b0a12781acca4123dd7899446a94b6f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx, default\_value)

[RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR](#ga2b0a12781acca4123dd7899446a94b6f)

#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value)

Get the event cell value from the "renesas-elcs" property by index, or return a default value if the ...

**Definition** renesas\_elc.h:292

Get the event cell value by index for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |
    | default\_value | Value to return if the property is not present. |

Returns
:   Event cell value or default\_value.

## [◆ ](#ga86ded9427001c5d3b315b71dcbfad7d0)RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME

| #define RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME](#ga920e3b26fb52a728ed2a3cd1ab5af7f0)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

Get the event cell value by element name for a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |

Returns
:   Event cell value.

## [◆ ](#ga94f2bc95761722c93019371f432da262)RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME\_OR

| #define RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR](#ga41c5adcf8817d529b5521727d9937b42)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, default\_value)

[RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR](#ga41c5adcf8817d529b5521727d9937b42)

#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR(node\_id, name, default\_value)

Get the event cell value from the "renesas-elcs" property by element name, or return a default value ...

**Definition** renesas\_elc.h:277

Get the event cell value by element name for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |
    | default\_value | Value to return if the property is not present. |

Returns
:   Event cell value or default\_value.

## [◆ ](#gace33f51f3a3a2efd42932a816e05be0b)RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX

| #define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, renesas\_elcs, idx, peripheral)

Get the peripheral cell value from the "renesas-elcs" property by index.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |

Returns
:   Peripheral cell value.

## [◆ ](#ga915d2760bd3c8ecf1b689bed286035d8)RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR

| #define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, renesas\_elcs), \

([RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX](#gace33f51f3a3a2efd42932a816e05be0b)(node\_id, idx)), \

(default\_value))

[RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX](#gace33f51f3a3a2efd42932a816e05be0b)

#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX(node\_id, idx)

Get the peripheral cell value from the "renesas-elcs" property by index.

**Definition** renesas\_elc.h:164

Get the peripheral cell value from the "renesas-elcs" property by index, or return a default value if the property does not exist.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |
    | default\_value | Value to return if the property is not present. |

Returns
:   Peripheral cell value or default\_value.

## [◆ ](#ga1f196ad20380dedf193c754906c5ed14)RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME

| #define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)(node\_id, renesas\_elcs, name, peripheral)

Get the peripheral cell value from the "renesas-elcs" property by element name.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |

Returns
:   Peripheral cell value.

## [◆ ](#ga35d7aef6829d74e92fa7c82306711a6c)RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR

| #define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, renesas\_elcs), \

([RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME](#ga1f196ad20380dedf193c754906c5ed14)(node\_id, name)), \

(default\_value))

[RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME](#ga1f196ad20380dedf193c754906c5ed14)

#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME(node\_id, name)

Get the peripheral cell value from the "renesas-elcs" property by element name.

**Definition** renesas\_elc.h:153

Get the peripheral cell value from the "renesas-elcs" property by element name, or return a default value if the property does not exist.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |
    | default\_value | Value to return if the property is not present. |

Returns
:   Peripheral cell value or default\_value.

## [◆ ](#gaeab186e0f09ee56ce87719a7d5566f50)RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX

| #define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX](#gace33f51f3a3a2efd42932a816e05be0b)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

Get the peripheral cell value by index for a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |

Returns
:   Peripheral cell value.

## [◆ ](#ga360d362b3fc26afb7cc81bfd28f6fc6a)RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX\_OR

| #define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR](#ga915d2760bd3c8ecf1b689bed286035d8)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx, default\_value)

[RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR](#ga915d2760bd3c8ecf1b689bed286035d8)

#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value)

Get the peripheral cell value from the "renesas-elcs" property by index, or return a default value if...

**Definition** renesas\_elc.h:192

Get the peripheral cell value by index for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | idx | Logical index into the renesas-elcs property. |
    | default\_value | Value to return if the property is not present. |

Returns
:   Peripheral cell value or default\_value.

## [◆ ](#ga3a0b277cb45636a86bf9b665fd75d133)RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME

| #define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME](#ga1f196ad20380dedf193c754906c5ed14)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

Get the peripheral cell value by element name for a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |

Returns
:   Peripheral cell value.

## [◆ ](#ga0e1c393825d778fd22a9a190eaedc308)RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME\_OR

| #define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

**Value:**

[RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR](#ga35d7aef6829d74e92fa7c82306711a6c)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, default\_value)

[RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR](#ga35d7aef6829d74e92fa7c82306711a6c)

#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR(node\_id, name, default\_value)

Get the peripheral cell value from the "renesas-elcs" property by element name, or return a default v...

**Definition** renesas\_elc.h:177

Get the peripheral cell value by element name for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number. |
    | --- | --- |
    | name | Lowercase-and-underscores name as specified in the renesas-elcs-names property. |
    | default\_value | Value to return if the property is not present. |

Returns
:   Peripheral cell value or default\_value.

## Function Documentation

## [◆ ](#gaac75089657f841c80225aa40de9c2a93)renesas\_elc\_disable()

| int renesas\_elc\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

Disable the operation of the Event Link Controller.

This function disables the ELC, stopping event processing.

Parameters
:   | dev | Event Link Controller device. |
    | --- | --- |

Returns
:   0 if successful.
:   A negative errno code on failure.

## [◆ ](#gafbffc029fd9482be578bd05cbdb3a03f)renesas\_elc\_enable()

| int renesas\_elc\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

Enable the operation of the Event Link Controller.

This function enables the ELC so that it can process events.

Parameters
:   | dev | Event Link Controller device. |
    | --- | --- |

Returns
:   0 if successful.
:   A negative errno code on failure.

## [◆ ](#ga65c950ccf0087c514daf6d543a0a7ecf)renesas\_elc\_link\_break()

| int renesas\_elc\_link\_break | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *peripheral* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

Break an event link.

This function breaks an existing event link for the given peripheral.

Parameters
:   | dev | Event Link Controller device. |
    | --- | --- |
    | peripheral | Peripheral ID whose link is to be broken. |

Returns
:   0 if successful.
:   A negative errno code on failure.

## [◆ ](#ga444e17d01310283e61bcde9a1022c47a)renesas\_elc\_link\_set()

| int renesas\_elc\_link\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *peripheral*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

Create a single event link.

This function configures an event link by associating a peripheral with a specific event signal.

Parameters
:   | dev | Event Link Controller device. |
    | --- | --- |
    | peripheral | Peripheral ID to be linked to the event signal. |
    | event | Event signal ID to be associated with the peripheral. |

Returns
:   0 if successful.
:   A negative errno code on failure.

## [◆ ](#gab3b55b83b38469854aae726a71f6ad55)renesas\_elc\_software\_event\_generate()

| int renesas\_elc\_software\_event\_generate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event* ) |

`#include <[zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](renesas__elc_8h.md)>`

Generate a software event in the Event Link Controller.

This function requests the Renesas ELC to generate a software event identified by `event`.

Parameters
:   | dev | The Event Link Controller device. |
    | --- | --- |
    | event | Software event ID to generate. |

Returns
:   0 if successful.
:   A negative errno code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
