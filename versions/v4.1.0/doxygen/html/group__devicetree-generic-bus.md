---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__devicetree-generic-bus.html
original_path: doxygen/html/group__devicetree-generic-bus.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bus helpers

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_BUS](#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id) |
|  | Node's bus controller. |
| #define | [DT\_ON\_BUS](#gabe5eea44ff838c11dc5b75f9ec2a9317)(node\_id, bus) |
|  | Is a node on a bus of a given type? |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga1082d31ac2dafdf9e085d4c23f2169dc)DT\_BUS

| #define DT\_BUS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_BUS)

Node's bus controller.

Get the node identifier of the node's bus controller. This can be used with [DT\_PROP()](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value.") to get properties of the bus controller.

It is an error to use this with nodes which do not have bus controllers.

Example devicetree fragment:

i2c@deadbeef {

status = "okay";

clock-frequency = < 100000 >;

i2c\_device: accelerometer@12 {

...

};

};

Example usage:

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_BUS](#ga1082d31ac2dafdf9e085d4c23f2169dc)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(i2c\_device)), clock\_frequency) // 100000

[DT\_BUS](#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3861

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   a node identifier for the node's bus controller

## [◆ ](#gabe5eea44ff838c11dc5b75f9ec2a9317)DT\_ON\_BUS

| #define DT\_ON\_BUS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *bus* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT3(node\_id, \_BUS\_, bus))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

Is a node on a bus of a given type?

Example devicetree overlay:

&i2c0 {

temp: temperature-sensor@76 {

compatible = "vnd,some-sensor";

reg = <0x76>;

};

};

Example usage, assuming i2c0 is an I2C bus controller node, and therefore temp is on an I2C bus:

[DT\_ON\_BUS](#gabe5eea44ff838c11dc5b75f9ec2a9317)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(temp), i2c) // 1

[DT\_ON\_BUS](#gabe5eea44ff838c11dc5b75f9ec2a9317)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(temp), spi) // 0

[DT\_ON\_BUS](#gabe5eea44ff838c11dc5b75f9ec2a9317)

#define DT\_ON\_BUS(node\_id, bus)

Is a node on a bus of a given type?

**Definition** devicetree.h:3891

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | bus | lowercase-and-underscores bus type as a C token (i.e. without quotes) |

Returns
:   1 if the node is on a bus of the given type, 0 otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
