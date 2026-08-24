---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__devicetree-display.html
original_path: doxygen/html/group__devicetree-display.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree Display API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_ZEPHYR\_DISPLAY](#ga265c3a81b2f6962b11931028c8727863)(idx) |
|  | Get display node identifier by logical index from "displays" property of node with compatible "zephyr,displays". |
| #define | [DT\_ZEPHYR\_DISPLAYS\_COUNT](#ga5a5f5bc95a76e4f1d09d970a18e6e5b5) |
|  | Get number of zephyr displays. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga265c3a81b2f6962b11931028c8727863)DT\_ZEPHYR\_DISPLAY

| #define DT\_ZEPHYR\_DISPLAY | ( |  | *idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/devicetree/display.h](devicetree_2display_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)([DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)(zephyr\_displays), displays, idx)

[DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)

#define DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat)

Get a node identifier for a status okay node with a compatible.

**Definition** devicetree.h:479

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1785

Get display node identifier by logical index from "displays" property of node with compatible "zephyr,displays".

Example devicetree fragment:

displays\_node: my-displays {

compatible = "zephyr,displays";

displays = <&n2 &n3>;

status = "okay";

};

n2: node-2 { ... };

n3: node-3 { ... };

Above, displays property has two elements:

- index 0 has phandle &n2, which is node-2's phandle
- index 1 has phandle &n3, which is node-3's phandle

Example usage:

[DT\_ZEPHYR\_DISPLAY](#ga265c3a81b2f6962b11931028c8727863)(0) // node identifier for display node node-2

[DT\_ZEPHYR\_DISPLAY](#ga265c3a81b2f6962b11931028c8727863)(1) // node identifier for display node node-3

[DT\_ZEPHYR\_DISPLAY](#ga265c3a81b2f6962b11931028c8727863)

#define DT\_ZEPHYR\_DISPLAY(idx)

Get display node identifier by logical index from "displays" property of node with compatible "zephyr...

**Definition** display.h:59

Parameters
:   | idx | logical index of display node's phandle in "displays" property |
    | --- | --- |

Returns
:   display node identifier, [DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855 "DT_INVALID_NODE") otherwise

## [◆ ](#ga5a5f5bc95a76e4f1d09d970a18e6e5b5)DT\_ZEPHYR\_DISPLAYS\_COUNT

| #define DT\_ZEPHYR\_DISPLAYS\_COUNT |
| --- |

`#include <[zephyr/devicetree/display.h](devicetree_2display_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(zephyr\_displays), \

([DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)([DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)(zephyr\_displays), displays)), \

([DT\_HAS\_CHOSEN](group__devicetree-generic-chosen.md#ga9df6bacab5f579284f5f3c1e4856cd15)(zephyr\_display)))

[DT\_HAS\_CHOSEN](group__devicetree-generic-chosen.md#ga9df6bacab5f579284f5f3c1e4856cd15)

#define DT\_HAS\_CHOSEN(prop)

Test if the devicetree has a /chosen node.

**Definition** devicetree.h:2922

[DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)

#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat)

Does the devicetree have a status okay node with a compatible?

**Definition** devicetree.h:3711

[DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)

#define DT\_PROP\_LEN(node\_id, prop)

Get a property's logical length.

**Definition** devicetree.h:796

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

Get number of zephyr displays.

Returns
:   number of displays designated by "displays" property of "zephyr,displays" compatible node, if it exists, otherwise 1 if "zephyr,display" chosen property exists, 0 otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
