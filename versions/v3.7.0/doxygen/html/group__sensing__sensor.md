---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__sensing__sensor.html
original_path: doxygen/html/group__sensing__sensor.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

| Macros | |
| --- | --- |
| #define | [SENSING\_SENSORS\_DT\_DEFINE](#gad5a9ccb04d96efc57078e880ca28b654)(node, reg\_ptr, cb\_list\_ptr, init\_fn, [pm\_device](structpm__device.md), data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...) |
|  | Like [SENSOR\_DEVICE\_DT\_DEFINE()](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c "Like DEVICE_DT_DEFINE() with sensor specifics.") with sensing specifics. |
| #define | [SENSING\_SENSORS\_DT\_INST\_DEFINE](#gae3c7a2acba53cc524a4b1043df49fe85)(inst, ...) |
|  | Like [SENSING\_SENSORS\_DT\_DEFINE()](#gad5a9ccb04d96efc57078e880ca28b654) for an instance of a DT\_DRV\_COMPAT compatible. |

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

[DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)

#define DT\_PROP\_LEN\_OR(node\_id, prop, default\_value)

Like DT\_PROP\_LEN(), but with a fallback to default\_value.

**Definition** devicetree.h:713

[SENSOR\_DEVICE\_DT\_DEFINE](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c)

#define SENSOR\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr,...)

Like DEVICE\_DT\_DEFINE() with sensor specifics.

**Definition** sensor.h:1395

[pm\_device](structpm__device.md)

Runtime PM info for device with generic PM.

**Definition** device.h:163

Like [SENSOR\_DEVICE\_DT\_DEFINE()](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c "Like DEVICE_DT_DEFINE() with sensor specifics.") with sensing specifics.

Defines a sensor which implements the sensor API. May define an element in the sensing sensor iterable section used to enumerate all sensing sensors.

Parameters
:   | node | The devicetree node identifier. |
    | --- | --- |
    | reg\_ptr | Pointer to the device's [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md "Sensor registration information."). |
    | cb\_list\_ptr | Pointer to sensing callback list. |
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

**Definition** devicetree.h:3604

[SENSING\_SENSORS\_DT\_DEFINE](#gad5a9ccb04d96efc57078e880ca28b654)

#define SENSING\_SENSORS\_DT\_DEFINE(node, reg\_ptr, cb\_list\_ptr, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr,...)

Like SENSOR\_DEVICE\_DT\_DEFINE() with sensing specifics.

**Definition** sensing\_sensor.h:369

Like [SENSING\_SENSORS\_DT\_DEFINE()](#gad5a9ccb04d96efc57078e880ca28b654) for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to [SENSING\_SENSORS\_DT\_DEFINE()](#gad5a9ccb04d96efc57078e880ca28b654). |
    | --- | --- |
    | ... | other parameters as expected by [SENSING\_SENSORS\_DT\_DEFINE()](#gad5a9ccb04d96efc57078e880ca28b654). |

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
