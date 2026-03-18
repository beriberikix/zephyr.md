---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__sensing__sensor.html
original_path: doxygen/html/group__sensing__sensor.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Sensing Sensor API

[Sensing](group__sensing.md)

Sensing Sensor API .
[More...](#details)

| Topics | |
| --- | --- |
|  | [Sensor Callbacks](group__sensing__sensor__callbacks.md) |

| Data Structures | |
| --- | --- |
| struct | [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md) |
|  | Sensor registration information. [More...](structsensing__sensor__register__info.md#details) |
| struct | [sensing\_connection](structsensing__connection.md) |
|  | Connection between a source and sink of sensor data. [More...](structsensing__connection.md#details) |
| struct | [sensing\_sensor](structsensing__sensor.md) |
|  | Internal sensor instance data structure. [More...](structsensing__sensor.md#details) |
| struct | [sensing\_submit\_config](structsensing__submit__config.md) |

| Macros | |
| --- | --- |
| #define | [SENSING\_SENSOR\_INFO\_NAME](#ga4a11557e9d28c75e67f2d21af8dd24d7)(node, idx) |
| #define | [SENSING\_SENSOR\_INFO\_DEFINE](#ga46b8830de0d42506c8804307c515c00b)(node, idx) |
| #define | [SENSING\_CONNECTIONS\_NAME](#ga11f2d720e050f2212b67f2e11fa9677b)(node) |
| #define | [SENSING\_SENSOR\_SOURCE\_NAME](#ga256546e178d1b2e507cb862876fec2d0)(idx, node) |
| #define | [SENSING\_SENSOR\_SOURCE\_EXTERN](#ga3df3d46d0102ec114d9125dcb1474745)(idx, node) |
| #define | [SENSING\_CONNECTION\_INITIALIZER](#ga11ddd317f3aef5edc0f80bad11738612)(source\_name, cb\_list\_ptr) |
| #define | [SENSING\_CONNECTION\_DEFINE](#ga791ffbf312fa2eae23350cd9add0afc3)(idx, node, cb\_list\_ptr) |
| #define | [SENSING\_CONNECTIONS\_DEFINE](#ga5c932e7be9361293a7b5ff3124e9799d)(node, num, cb\_list\_ptr) |
| #define | [SENSING\_SUBMIT\_CFG\_NAME](#gaa0c5eb169a6e3922c091a4bf6ff82478)(node, idx) |
| #define | [SENSING\_SENSOR\_IODEV\_NAME](#ga8c15780ceb1988ab7192c3c3ca70ac82)(node, idx) |
| #define | [SENSING\_SENSOR\_IODEV\_DEFINE](#gafd8cbf368e9fa541ce67013d0e8624f2)(node, idx) |
| #define | [SENSING\_SENSOR\_NAME](#ga4f8a39411260fbfd55258241de9bbb37)(node, idx) |
| #define | [SENSING\_SENSOR\_DEFINE](#gae3588d8dce25ad800bf0633f1b3c6bf7)(node, prop, idx, reg\_ptr, cb\_list\_ptr) |
| #define | [SENSING\_SENSORS\_DEFINE](#ga6fd18be5f503ad4a744df6583495c3fe)(node, reg\_ptr, cb\_list\_ptr) |
| #define | [SENSING\_SENSORS\_DT\_DEFINE](#gad5a9ccb04d96efc57078e880ca28b654)(node, reg\_ptr, cb\_list\_ptr, init\_fn, [pm\_device](structpm__device.md), data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...) |
|  | Like [SENSOR\_DEVICE\_DT\_DEFINE()](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c "Like DEVICE_DT_DEFINE() with sensor specifics.") with sensing specifics. |
| #define | [SENSING\_SENSORS\_DT\_INST\_DEFINE](#gae3c7a2acba53cc524a4b1043df49fe85)(inst, ...) |
|  | Like [SENSING\_SENSORS\_DT\_DEFINE()](#gad5a9ccb04d96efc57078e880ca28b654) for an instance of a DT\_DRV\_COMPAT compatible. |

| Enumerations | |
| --- | --- |
| enum | { [EVENT\_CONFIG\_READY](#ggaafa611add600aa3b2fba2c3e08562a02a78480d5dce2873492e587176880531d8) } |
| enum | { [SENSOR\_LATER\_CFG\_BIT](#ggaf3548dcc45caf8e64b2ecec463bea7e6a079aade4a76672cd9a96d777534fb584) } |

| Functions | |
| --- | --- |
| int | [sensing\_sensor\_get\_reporters](#gab4c41d02b3731e5829a41e1f5f5154a5) (const struct [device](structdevice.md) \*dev, int type, [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*reporter\_handles, int max\_handles) |
|  | Get reporter handles of a given sensor instance by sensor type. |
| int | [sensing\_sensor\_get\_reporters\_count](#ga2c5cfb298b2dfde967edfdd987115021) (const struct [device](structdevice.md) \*dev, int type) |
|  | Get reporters count of a given sensor instance by sensor type. |
| int | [sensing\_sensor\_get\_state](#gab9446a3085b6b05da448dce59db50387) (const struct [device](structdevice.md) \*dev, enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Get this sensor's state. |

## Detailed Description

Sensing Sensor API .

## Macro Definition Documentation

## [◆ ](#ga791ffbf312fa2eae23350cd9add0afc3)SENSING\_CONNECTION\_DEFINE

| #define SENSING\_CONNECTION\_DEFINE | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *node*, |
|  |  |  | *cb\_list\_ptr* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

[SENSING\_CONNECTION\_INITIALIZER](#ga11ddd317f3aef5edc0f80bad11738612)([SENSING\_SENSOR\_SOURCE\_NAME](#ga256546e178d1b2e507cb862876fec2d0)(idx, node), \

cb\_list\_ptr)

[SENSING\_CONNECTION\_INITIALIZER](#ga11ddd317f3aef5edc0f80bad11738612)

#define SENSING\_CONNECTION\_INITIALIZER(source\_name, cb\_list\_ptr)

**Definition** sensing\_sensor.h:137

[SENSING\_SENSOR\_SOURCE\_NAME](#ga256546e178d1b2e507cb862876fec2d0)

#define SENSING\_SENSOR\_SOURCE\_NAME(idx, node)

**Definition** sensing\_sensor.h:130

## [◆ ](#ga11ddd317f3aef5edc0f80bad11738612)SENSING\_CONNECTION\_INITIALIZER

| #define SENSING\_CONNECTION\_INITIALIZER | ( |  | *source\_name*, |
| --- | --- | --- | --- |
|  |  |  | *cb\_list\_ptr* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

{ \

.callback\_list = cb\_list\_ptr, \

.source = &source\_name, \

}

## [◆ ](#ga5c932e7be9361293a7b5ff3124e9799d)SENSING\_CONNECTIONS\_DEFINE

| #define SENSING\_CONNECTIONS\_DEFINE | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *num*, |
|  |  |  | *cb\_list\_ptr* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

[LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)(num, [SENSING\_SENSOR\_SOURCE\_EXTERN](#ga3df3d46d0102ec114d9125dcb1474745), \

(), node) \

static struct [sensing\_connection](structsensing__connection.md) \

[SENSING\_CONNECTIONS\_NAME](#ga11f2d720e050f2212b67f2e11fa9677b)(node)[(num)] = { \

LISTIFY(num, [SENSING\_CONNECTION\_DEFINE](#ga791ffbf312fa2eae23350cd9add0afc3), \

(,), node, cb\_list\_ptr) \

};

[SENSING\_CONNECTIONS\_NAME](#ga11f2d720e050f2212b67f2e11fa9677b)

#define SENSING\_CONNECTIONS\_NAME(node)

**Definition** sensing\_sensor.h:127

[SENSING\_SENSOR\_SOURCE\_EXTERN](#ga3df3d46d0102ec114d9125dcb1474745)

#define SENSING\_SENSOR\_SOURCE\_EXTERN(idx, node)

**Definition** sensing\_sensor.h:134

[SENSING\_CONNECTION\_DEFINE](#ga791ffbf312fa2eae23350cd9add0afc3)

#define SENSING\_CONNECTION\_DEFINE(idx, node, cb\_list\_ptr)

**Definition** sensing\_sensor.h:143

[LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)

#define LISTIFY(LEN, F, sep,...)

Generates a sequence of code with configurable separator.

**Definition** util\_macro.h:442

[sensing\_connection](structsensing__connection.md)

Connection between a source and sink of sensor data.

**Definition** sensing\_sensor.h:71

## [◆ ](#ga11f2d720e050f2212b67f2e11fa9677b)SENSING\_CONNECTIONS\_NAME

| #define SENSING\_CONNECTIONS\_NAME | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

\_CONCAT(\_\_sensing\_connections\_, [DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)(node))

[DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)

#define DEVICE\_DT\_NAME\_GET(node\_id)

The name of the global device object for node\_id.

**Definition** device.h:216

## [◆ ](#gae3588d8dce25ad800bf0633f1b3c6bf7)SENSING\_SENSOR\_DEFINE

| #define SENSING\_SENSOR\_DEFINE | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx*, |
|  |  |  | *reg\_ptr*, |
|  |  |  | *cb\_list\_ptr* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

[SENSING\_SENSOR\_INFO\_DEFINE](#ga46b8830de0d42506c8804307c515c00b)(node, idx) \

SENSING\_SENSOR\_IODEV\_DEFINE(node, idx) \

STRUCT\_SECTION\_ITERABLE([sensing\_sensor](structsensing__sensor.md), \

[SENSING\_SENSOR\_NAME](#ga4f8a39411260fbfd55258241de9bbb37)(node, idx)) = { \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)(node), \

.info = &[SENSING\_SENSOR\_INFO\_NAME](#ga4a11557e9d28c75e67f2d21af8dd24d7)(node, idx), \

.register\_info = reg\_ptr, \

.reporter\_num = [DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)(node, reporters, 0), \

.conns = [SENSING\_CONNECTIONS\_NAME](#ga11f2d720e050f2212b67f2e11fa9677b)(node), \

.iodev = &[SENSING\_SENSOR\_IODEV\_NAME](#ga8c15780ceb1988ab7192c3c3ca70ac82)(node, idx), \

};

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:233

[DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)

#define DT\_PROP\_LEN\_OR(node\_id, prop, default\_value)

Like DT\_PROP\_LEN(), but with a fallback to default\_value.

**Definition** devicetree.h:665

[SENSING\_SENSOR\_INFO\_DEFINE](#ga46b8830de0d42506c8804307c515c00b)

#define SENSING\_SENSOR\_INFO\_DEFINE(node, idx)

**Definition** sensing\_sensor.h:116

[SENSING\_SENSOR\_INFO\_NAME](#ga4a11557e9d28c75e67f2d21af8dd24d7)

#define SENSING\_SENSOR\_INFO\_NAME(node, idx)

**Definition** sensing\_sensor.h:113

[SENSING\_SENSOR\_NAME](#ga4f8a39411260fbfd55258241de9bbb37)

#define SENSING\_SENSOR\_NAME(node, idx)

**Definition** sensing\_sensor.h:179

[SENSING\_SENSOR\_IODEV\_NAME](#ga8c15780ceb1988ab7192c3c3ca70ac82)

#define SENSING\_SENSOR\_IODEV\_NAME(node, idx)

**Definition** sensing\_sensor.h:167

[sensing\_sensor](structsensing__sensor.md)

Internal sensor instance data structure.

**Definition** sensing\_sensor.h:95

## [◆ ](#ga46b8830de0d42506c8804307c515c00b)SENSING\_SENSOR\_INFO\_DEFINE

| #define SENSING\_SENSOR\_INFO\_DEFINE | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

const static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([sensing\_sensor\_info](structsensing__sensor__info.md), \

[SENSING\_SENSOR\_INFO\_NAME](#ga4a11557e9d28c75e67f2d21af8dd24d7)(node, idx)) = { \

.type = [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node, sensor\_types, idx), \

.name = [DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)(node), \

.friendly\_name = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, friendly\_name), \

.vendor = [DT\_NODE\_VENDOR\_OR](group__devicetree-generic-vendor.md#gad91ad9294d36eb151c96e719f1a5b0ef)(node, NULL), \

.model = [DT\_NODE\_MODEL\_OR](group__devicetree-generic-vendor.md#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)(node, NULL), \

.minimal\_interval = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, minimal\_interval),\

};

[DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)

#define DT\_NODE\_FULL\_NAME(node\_id)

Get a devicetree node's name with unit-address as a string literal.

**Definition** devicetree.h:522

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:761

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:615

[DT\_NODE\_MODEL\_OR](group__devicetree-generic-vendor.md#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)

#define DT\_NODE\_MODEL\_OR(node\_id, default\_value)

Get the node's (only) model as a string literal.

**Definition** devicetree.h:2148

[DT\_NODE\_VENDOR\_OR](group__devicetree-generic-vendor.md#gad91ad9294d36eb151c96e719f1a5b0ef)

#define DT\_NODE\_VENDOR\_OR(node\_id, default\_value)

Get the node's (only) vendor as a string literal.

**Definition** devicetree.h:2072

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[sensing\_sensor\_info](structsensing__sensor__info.md)

Sensor basic constant information.

**Definition** sensing.h:126

## [◆ ](#ga4a11557e9d28c75e67f2d21af8dd24d7)SENSING\_SENSOR\_INFO\_NAME

| #define SENSING\_SENSOR\_INFO\_NAME | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

\_CONCAT(\_CONCAT(\_\_sensing\_sensor\_info\_, idx), [DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)(node))

## [◆ ](#gafd8cbf368e9fa541ce67013d0e8624f2)SENSING\_SENSOR\_IODEV\_DEFINE

| #define SENSING\_SENSOR\_IODEV\_DEFINE | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

static struct [sensing\_submit\_config](structsensing__submit__config.md) [SENSING\_SUBMIT\_CFG\_NAME](#gaa0c5eb169a6e3922c091a4bf6ff82478)(node, idx) = { \

.is\_streaming = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, stream\_mode), \

.info\_index = idx, \

}; \

RTIO\_IODEV\_DEFINE([SENSING\_SENSOR\_IODEV\_NAME](#ga8c15780ceb1988ab7192c3c3ca70ac82)(node, idx), \

&\_\_sensing\_iodev\_api, \

&[SENSING\_SUBMIT\_CFG\_NAME](#gaa0c5eb169a6e3922c091a4bf6ff82478)(node, idx));

[SENSING\_SUBMIT\_CFG\_NAME](#gaa0c5eb169a6e3922c091a4bf6ff82478)

#define SENSING\_SUBMIT\_CFG\_NAME(node, idx)

**Definition** sensing\_sensor.h:164

[sensing\_submit\_config](structsensing__submit__config.md)

**Definition** sensing\_sensor.h:156

## [◆ ](#ga8c15780ceb1988ab7192c3c3ca70ac82)SENSING\_SENSOR\_IODEV\_NAME

| #define SENSING\_SENSOR\_IODEV\_NAME | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

\_CONCAT(\_CONCAT(\_\_sensing\_iodev\_, idx), [DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)(node))

## [◆ ](#ga4f8a39411260fbfd55258241de9bbb37)SENSING\_SENSOR\_NAME

| #define SENSING\_SENSOR\_NAME | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

\_CONCAT(\_CONCAT(\_\_sensing\_sensor\_, idx), [DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)(node))

## [◆ ](#ga3df3d46d0102ec114d9125dcb1474745)SENSING\_SENSOR\_SOURCE\_EXTERN

| #define SENSING\_SENSOR\_SOURCE\_EXTERN | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *node* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

extern struct [sensing\_sensor](structsensing__sensor.md) [SENSING\_SENSOR\_SOURCE\_NAME](#ga256546e178d1b2e507cb862876fec2d0)(idx, node); \

## [◆ ](#ga256546e178d1b2e507cb862876fec2d0)SENSING\_SENSOR\_SOURCE\_NAME

| #define SENSING\_SENSOR\_SOURCE\_NAME | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *node* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

[SENSING\_SENSOR\_NAME](#ga4f8a39411260fbfd55258241de9bbb37)([DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node, reporters, idx), \

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node, reporters\_index, idx))

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1580

## [◆ ](#ga6fd18be5f503ad4a744df6583495c3fe)SENSING\_SENSORS\_DEFINE

| #define SENSING\_SENSORS\_DEFINE | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *reg\_ptr*, |
|  |  |  | *cb\_list\_ptr* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

[DT\_FOREACH\_PROP\_ELEM\_VARGS](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)(node, sensor\_types, \

[SENSING\_SENSOR\_DEFINE](#gae3588d8dce25ad800bf0633f1b3c6bf7), reg\_ptr, cb\_list\_ptr)

[DT\_FOREACH\_PROP\_ELEM\_VARGS](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)

#define DT\_FOREACH\_PROP\_ELEM\_VARGS(node\_id, prop, fn,...)

Invokes fn for each element in the value of property prop with multiple arguments.

**Definition** devicetree.h:3012

[SENSING\_SENSOR\_DEFINE](#gae3588d8dce25ad800bf0633f1b3c6bf7)

#define SENSING\_SENSOR\_DEFINE(node, prop, idx, reg\_ptr, cb\_list\_ptr)

**Definition** sensing\_sensor.h:182

## [◆ ](#gad5a9ccb04d96efc57078e880ca28b654)SENSING\_SENSORS\_DT\_DEFINE

| #define SENSING\_SENSORS\_DT\_DEFINE | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *reg\_ptr*, |
|  |  |  | *cb\_list\_ptr*, |
|  |  |  | *init\_fn*, |
|  |  |  | *[pm\_device](structpm__device.md)*, |
|  |  |  | *data\_ptr*, |
|  |  |  | *cfg\_ptr*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api\_ptr*, |
|  |  |  | ... ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

[SENSOR\_DEVICE\_DT\_DEFINE](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c)(node, init\_fn, [pm\_device](structpm__device.md), \

data\_ptr, cfg\_ptr, level, prio, \

api\_ptr, \_\_VA\_ARGS\_\_); \

SENSING\_CONNECTIONS\_DEFINE(node, \

[DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)(node, reporters, 0), \

cb\_list\_ptr); \

SENSING\_SENSORS\_DEFINE(node, reg\_ptr, cb\_list\_ptr);

[SENSOR\_DEVICE\_DT\_DEFINE](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c)

#define SENSOR\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr,...)

Like DEVICE\_DT\_DEFINE() with sensor specifics.

**Definition** sensor.h:1313

[pm\_device](structpm__device.md)

Runtime PM info for device with generic PM.

**Definition** device.h:165

Like [SENSOR\_DEVICE\_DT\_DEFINE()](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c "Like DEVICE_DT_DEFINE() with sensor specifics.") with sensing specifics.

Defines a sensor which implements the sensor API. May define an element in the sensing sensor iterable section used to enumerate all sensing sensors.

Parameters
:   | node | The devicetree node identifier. |
    | --- | --- |
    | reg\_ptr | Pointer to the device's [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md "Sensor registration information."). |
    | cb\_list\_ptr | Pointer to devices callback list. |
    | init\_fn | Name of the init function of the driver. |
    | [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") | PM device resources reference (NULL if device does not use PM). |
    | data\_ptr | Pointer to the device's private data. |
    | cfg\_ptr | The address to the structure containing the configuration information for this instance of the driver. |
    | level | The initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | prio | Priority within the selected initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api\_ptr | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |

## [◆ ](#gae3c7a2acba53cc524a4b1043df49fe85)SENSING\_SENSORS\_DT\_INST\_DEFINE

| #define SENSING\_SENSORS\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

[SENSING\_SENSORS\_DT\_DEFINE](#gad5a9ccb04d96efc57078e880ca28b654)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

[SENSING\_SENSORS\_DT\_DEFINE](#gad5a9ccb04d96efc57078e880ca28b654)

#define SENSING\_SENSORS\_DT\_DEFINE(node, reg\_ptr, cb\_list\_ptr, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr,...)

Like SENSOR\_DEVICE\_DT\_DEFINE() with sensing specifics.

**Definition** sensing\_sensor.h:229

Like [SENSING\_SENSORS\_DT\_DEFINE()](#gad5a9ccb04d96efc57078e880ca28b654) for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to [SENSING\_SENSORS\_DT\_DEFINE()](#gad5a9ccb04d96efc57078e880ca28b654). |
    | --- | --- |
    | ... | other parameters as expected by [SENSING\_SENSORS\_DT\_DEFINE()](#gad5a9ccb04d96efc57078e880ca28b654). |

## [◆ ](#gaa0c5eb169a6e3922c091a4bf6ff82478)SENSING\_SUBMIT\_CFG\_NAME

| #define SENSING\_SUBMIT\_CFG\_NAME | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

**Value:**

\_CONCAT(\_CONCAT(\_\_sensing\_submit\_cfg\_, idx), [DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)(node))

## Enumeration Type Documentation

## [◆ ](#gaf3548dcc45caf8e64b2ecec463bea7e6)anonymous enum

| anonymous enum |
| --- |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

| Enumerator | |
| --- | --- |
| SENSOR\_LATER\_CFG\_BIT |  |

## [◆ ](#gaafa611add600aa3b2fba2c3e08562a02)anonymous enum

| anonymous enum |
| --- |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

| Enumerator | |
| --- | --- |
| EVENT\_CONFIG\_READY |  |

## Function Documentation

## [◆ ](#gab4c41d02b3731e5829a41e1f5f5154a5)sensing\_sensor\_get\_reporters()

| int sensing\_sensor\_get\_reporters | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *type*, |
|  |  | [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \* | *reporter\_handles*, |
|  |  | int | *max\_handles* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

Get reporter handles of a given sensor instance by sensor type.

Parameters
:   | dev | The sensor instance device structure. |
    | --- | --- |
    | type | The given type, [SENSING\_SENSOR\_TYPE\_ALL](group__sensing__sensor__types.md#ga9f6bc03e84167bf0b1ae8ea4fe016223 "SENSING_SENSOR_TYPE_ALL") to get reporters with all types. |
    | max\_handles | The max count of the `reporter_handles` array input. Can get real count number via [sensing\_sensor\_get\_reporters\_count](#ga2c5cfb298b2dfde967edfdd987115021) |
    | reporter\_handles | Input handles array for receiving found reporter sensor instances |

Returns
:   number of reporters found, 0 returned if not found.

## [◆ ](#ga2c5cfb298b2dfde967edfdd987115021)sensing\_sensor\_get\_reporters\_count()

| int sensing\_sensor\_get\_reporters\_count | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *type* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

Get reporters count of a given sensor instance by sensor type.

Parameters
:   | dev | The sensor instance device structure. |
    | --- | --- |
    | type | The sensor type for checking, [SENSING\_SENSOR\_TYPE\_ALL](group__sensing__sensor__types.md#ga9f6bc03e84167bf0b1ae8ea4fe016223 "SENSING_SENSOR_TYPE_ALL") |

Returns
:   Count of reporters by `type`, 0 returned if no reporters by `type`.

## [◆ ](#gab9446a3085b6b05da448dce59db50387)sensing\_sensor\_get\_state()

| int sensing\_sensor\_get\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) \* | *state* ) |

`#include <[sensing_sensor.h](sensing__sensor_8h.md)>`

Get this sensor's state.

Parameters
:   | dev | The sensor instance device structure. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Returned sensor state value |

Returns
:   0 on success or negative error value on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
