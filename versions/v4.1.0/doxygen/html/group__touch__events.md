---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__touch__events.html
original_path: doxygen/html/group__touch__events.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Touchscreen Event Report API

[Device Driver APIs](group__io__interfaces.md)

Touch Events API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [input\_touchscreen\_common\_config](structinput__touchscreen__common__config.md) |
|  | Common touchscreen config. [More...](structinput__touchscreen__common__config.md#details) |

| Macros | |
| --- | --- |
| #define | [INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT](#gae19dc2c40a8e14d28db614dfd4c5e32b)(node\_id) |
|  | Initialize common touchscreen config from devicetree. |
| #define | [INPUT\_TOUCH\_DT\_INST\_COMMON\_CONFIG\_INIT](#ga354195b719d526cebd63a061e8dc408b)(inst) |
|  | Initialize common touchscreen config from devicetree instance. |
| #define | [INPUT\_TOUCH\_STRUCT\_CHECK](#ga0b82cc636a4b686ee2948dc704fd06f0)(config) |
|  | Validate the offset of the common config structure. |

| Functions | |
| --- | --- |
| void | [input\_touchscreen\_report\_pos](#ga646bb86aa9f942fc3065381bd19e545c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) y, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Common utility for reporting touchscreen position events. |

## Detailed Description

Touch Events API.

Since
:   3.7

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#gae19dc2c40a8e14d28db614dfd4c5e32b)INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT

| #define INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_touch.h](input__touch_8h.md)>`

**Value:**

{ \

.screen\_width = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, screen\_width), \

.screen\_height = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, screen\_height), \

.inverted\_x = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, inverted\_x), \

.inverted\_y = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, inverted\_y), \

.swapped\_x\_y = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, swapped\_x\_y) \

}

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

Initialize common touchscreen config from devicetree.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |

## [◆ ](#ga354195b719d526cebd63a061e8dc408b)INPUT\_TOUCH\_DT\_INST\_COMMON\_CONFIG\_INIT

| #define INPUT\_TOUCH\_DT\_INST\_COMMON\_CONFIG\_INIT | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_touch.h](input__touch_8h.md)>`

**Value:**

[INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT](#gae19dc2c40a8e14d28db614dfd4c5e32b)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

[INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT](#gae19dc2c40a8e14d28db614dfd4c5e32b)

#define INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT(node\_id)

Initialize common touchscreen config from devicetree.

**Definition** input\_touch.h:50

Initialize common touchscreen config from devicetree instance.

Parameters
:   | inst | Instance. |
    | --- | --- |

## [◆ ](#ga0b82cc636a4b686ee2948dc704fd06f0)INPUT\_TOUCH\_STRUCT\_CHECK

| #define INPUT\_TOUCH\_STRUCT\_CHECK | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_touch.h](input__touch_8h.md)>`

**Value:**

BUILD\_ASSERT(offsetof(config, common) == 0, \

"struct input\_touchscreen\_common\_config must be placed first");

Validate the offset of the common config structure.

Parameters
:   | config | Name of the config structure. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga646bb86aa9f942fc3065381bd19e545c)input\_touchscreen\_report\_pos()

| void input\_touchscreen\_report\_pos | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *x*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *y*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[input_touch.h](input__touch_8h.md)>`

Common utility for reporting touchscreen position events.

Parameters
:   | dev | Touchscreen controller |
    | --- | --- |
    | x | X coordinate as reported by the controller |
    | y | Y coordinate as reported by the controller |
    | timeout | Timeout for reporting the event |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
