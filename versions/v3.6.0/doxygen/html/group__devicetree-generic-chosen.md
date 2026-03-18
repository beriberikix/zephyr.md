---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__devicetree-generic-chosen.html
original_path: doxygen/html/group__devicetree-generic-chosen.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Chosen nodes

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_CHOSEN](#ga3412d0acecffa828984cf9e2c89889ed)(prop) |
|  | Get a node identifier for a /chosen node property. |
| #define | [DT\_HAS\_CHOSEN](#ga9df6bacab5f579284f5f3c1e4856cd15)(prop) |
|  | Test if the devicetree has a /chosen node. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga3412d0acecffa828984cf9e2c89889ed)DT\_CHOSEN

| #define DT\_CHOSEN | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(DT\_CHOSEN\_, prop)

Get a node identifier for a /chosen node property.

This is only valid to call if [DT\_HAS\_CHOSEN(prop)](#ga9df6bacab5f579284f5f3c1e4856cd15) is 1.

Parameters
:   | prop | lowercase-and-underscores property name for the /chosen node |
    | --- | --- |

Returns
:   a node identifier for the chosen node property

## [◆ ](#ga9df6bacab5f579284f5f3c1e4856cd15)DT\_HAS\_CHOSEN

| #define DT\_HAS\_CHOSEN | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT3(DT\_CHOSEN\_, prop, \_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Test if the devicetree has a /chosen node.

Parameters
:   | prop | lowercase-and-underscores devicetree property |
    | --- | --- |

Returns
:   1 if the chosen property exists and refers to a node, 0 otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
