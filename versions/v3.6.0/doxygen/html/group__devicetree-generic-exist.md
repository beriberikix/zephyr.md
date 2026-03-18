---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__devicetree-generic-exist.html
original_path: doxygen/html/group__devicetree-generic-exist.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Existence checks

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_NODE\_EXISTS](#ga9d5cf40051d042b853f6b0088fd4500a)(node\_id) |
|  | Does a node identifier refer to a node? |
| #define | [DT\_NODE\_HAS\_STATUS](#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, status) |
|  | Does a node identifier refer to a node with a status? |
| #define | [DT\_HAS\_COMPAT\_STATUS\_OKAY](#ga916e11b66fdaab46e93c25241b62b52a)(compat) |
|  | Does the devicetree have a status okay node with a compatible? |
| #define | [DT\_NUM\_INST\_STATUS\_OKAY](#ga45c268d7f0d604a72dc0bcf5cd0733b0)(compat) |
|  | Get the number of instances of a given compatible with status okay. |
| #define | [DT\_NODE\_HAS\_COMPAT](#gad8912ba5db980713e72257472ded3ced)(node\_id, compat) |
|  | Does a devicetree node match a compatible? |
| #define | [DT\_NODE\_HAS\_COMPAT\_STATUS](#ga9bf6258fbeb0c5cd1fd15b9c9be9228a)(node\_id, compat, status) |
|  | Does a devicetree node have a compatible and status? |
| #define | [DT\_NODE\_HAS\_PROP](#gacce67bf20541cd2d07d8540058964692)(node\_id, prop) |
|  | Does a devicetree node have a property? |
| #define | [DT\_PHA\_HAS\_CELL\_AT\_IDX](#gacfbd6a2cb3038e5aba1e2216d65ebc78)(node\_id, pha, idx, cell) |
|  | Does a phandle array have a named cell specifier at an index? |
| #define | [DT\_PHA\_HAS\_CELL](#gaece280102681cbadf318c5dabfb3d719)(node\_id, pha, cell) |
|  | Equivalent to [DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, 0, cell)](#gacfbd6a2cb3038e5aba1e2216d65ebc78). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga916e11b66fdaab46e93c25241b62b52a)DT\_HAS\_COMPAT\_STATUS\_OKAY

| #define DT\_HAS\_COMPAT\_STATUS\_OKAY | ( |  | *compat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT(DT\_COMPAT\_HAS\_OKAY\_, compat))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Does the devicetree have a status okay node with a compatible?

Test for whether the devicetree has any nodes with status okay and the given compatible. That is, this returns 1 if and only if there is at least one `node_id` for which both of these expressions return 1:

[DT\_NODE\_HAS\_STATUS](#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, okay)

[DT\_NODE\_HAS\_COMPAT](#gad8912ba5db980713e72257472ded3ced)(node\_id, compat)

[DT\_NODE\_HAS\_STATUS](#ga3b769d8105c7679e1d0575a1e7f1f653)

#define DT\_NODE\_HAS\_STATUS(node\_id, status)

Does a node identifier refer to a node with a status?

**Definition** devicetree.h:3190

[DT\_NODE\_HAS\_COMPAT](#gad8912ba5db980713e72257472ded3ced)

#define DT\_NODE\_HAS\_COMPAT(node\_id, compat)

Does a devicetree node match a compatible?

**Definition** devicetree.h:3252

As usual, both a missing status and an ok status are treated as okay.

Parameters
:   | compat | lowercase-and-underscores compatible, without quotes |
    | --- | --- |

Returns
:   1 if both of the above conditions are met, 0 otherwise

## [◆ ](#ga9d5cf40051d042b853f6b0088fd4500a)DT\_NODE\_EXISTS

| #define DT\_NODE\_EXISTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT(node\_id, \_EXISTS))

Does a node identifier refer to a node?

Tests whether a node identifier refers to a node which exists, i.e. is defined in the devicetree.

It doesn't matter whether or not the node has a matching binding, or what the node's status value is. This is purely a check of whether the node exists at all.

Parameters
:   | node\_id | a node identifier |
    | --- | --- |

Returns
:   1 if the node identifier refers to a node, 0 otherwise.

## [◆ ](#gad8912ba5db980713e72257472ded3ced)DT\_NODE\_HAS\_COMPAT

| #define DT\_NODE\_HAS\_COMPAT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *compat* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT3(node\_id, \_COMPAT\_MATCHES\_, compat))

Does a devicetree node match a compatible?

Example devicetree fragment:

n: node {

compatible = "vnd,specific-device", "generic-device";

}

Example usages which evaluate to 1:

[DT\_NODE\_HAS\_COMPAT](#gad8912ba5db980713e72257472ded3ced)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), vnd\_specific\_device)

[DT\_NODE\_HAS\_COMPAT](#gad8912ba5db980713e72257472ded3ced)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), generic\_device)

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:198

This macro only uses the value of the compatible property. Whether or not a particular compatible has a matching binding has no effect on its value, nor does the node's status.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | compat | lowercase-and-underscores compatible, without quotes |

Returns
:   1 if the node's compatible property contains `compat`, 0 otherwise.

## [◆ ](#ga9bf6258fbeb0c5cd1fd15b9c9be9228a)DT\_NODE\_HAS\_COMPAT\_STATUS

| #define DT\_NODE\_HAS\_COMPAT\_STATUS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *compat*, |
|  |  |  | *status* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_NODE\_HAS\_COMPAT](#gad8912ba5db980713e72257472ded3ced)(node\_id, compat) && [DT\_NODE\_HAS\_STATUS](#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, status)

Does a devicetree node have a compatible and status?

This is equivalent to:

([DT\_NODE\_HAS\_COMPAT](#gad8912ba5db980713e72257472ded3ced)(node\_id, compat) &&

[DT\_NODE\_HAS\_STATUS](#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, status))

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | compat | lowercase-and-underscores compatible, without quotes |
    | status | okay or disabled as a token, not a string |

## [◆ ](#gacce67bf20541cd2d07d8540058964692)DT\_NODE\_HAS\_PROP

| #define DT\_NODE\_HAS\_PROP | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_P\_, prop, \_EXISTS))

Does a devicetree node have a property?

Tests whether a devicetree node has a property defined.

This tests whether the property is defined at all, not whether a boolean property is true or false. To get a boolean property's truth value, use [DT\_PROP(node\_id, prop)](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value.") instead.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   1 if the node has the property, 0 otherwise.

## [◆ ](#ga3b769d8105c7679e1d0575a1e7f1f653)DT\_NODE\_HAS\_STATUS

| #define DT\_NODE\_HAS\_STATUS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *status* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_NODE\_HAS\_STATUS\_INTERNAL(node\_id, status)

Does a node identifier refer to a node with a status?

Example uses:

[DT\_NODE\_HAS\_STATUS](#ga3b769d8105c7679e1d0575a1e7f1f653)([DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)(soc, i2c\_12340000), okay)

[DT\_NODE\_HAS\_STATUS](#ga3b769d8105c7679e1d0575a1e7f1f653)([DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)(soc, i2c\_12340000), disabled)

[DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)

#define DT\_PATH(...)

Get a node identifier for a devicetree path.

**Definition** devicetree.h:142

Tests whether a node identifier refers to a node which:

- exists in the devicetree, and
- has a status property matching the second argument (except that either a missing status or an ok status in the devicetree is treated as if it were okay instead)

Parameters
:   | node\_id | a node identifier |
    | --- | --- |
    | status | a status as one of the tokens okay or disabled, not a string |

Returns
:   1 if the node has the given status, 0 otherwise.

## [◆ ](#ga45c268d7f0d604a72dc0bcf5cd0733b0)DT\_NUM\_INST\_STATUS\_OKAY

| #define DT\_NUM\_INST\_STATUS\_OKAY | ( |  | *compat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[UTIL\_AND](group__sys-util.md#ga26179b776b4a03143e8be1612ef6d853)([DT\_HAS\_COMPAT\_STATUS\_OKAY](#ga916e11b66fdaab46e93c25241b62b52a)(compat), \

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(DT\_N\_INST, DT\_DASH(compat, NUM\_OKAY)))

[DT\_HAS\_COMPAT\_STATUS\_OKAY](#ga916e11b66fdaab46e93c25241b62b52a)

#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat)

Does the devicetree have a status okay node with a compatible?

**Definition** devicetree.h:3212

[UTIL\_AND](group__sys-util.md#ga26179b776b4a03143e8be1612ef6d853)

#define UTIL\_AND(a, b)

Like a && b, but does evaluation and short-circuiting at C preprocessor time.

**Definition** util\_macro.h:391

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Get the number of instances of a given compatible with status okay.

Parameters
:   | compat | lowercase-and-underscores compatible, without quotes |
    | --- | --- |

Returns
:   Number of instances with status okay

## [◆ ](#gaece280102681cbadf318c5dabfb3d719)DT\_PHA\_HAS\_CELL

| #define DT\_PHA\_HAS\_CELL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHA\_HAS\_CELL\_AT\_IDX](#gacfbd6a2cb3038e5aba1e2216d65ebc78)(node\_id, pha, 0, cell)

[DT\_PHA\_HAS\_CELL\_AT\_IDX](#gacfbd6a2cb3038e5aba1e2216d65ebc78)

#define DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, idx, cell)

Does a phandle array have a named cell specifier at an index?

**Definition** devicetree.h:3305

Equivalent to [DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, 0, cell)](#gacfbd6a2cb3038e5aba1e2216d65ebc78).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | cell | lowercase-and-underscores cell name whose existence to check at index `idx` |

Returns
:   1 if the named cell exists in the specifier at index 0, 0 otherwise.

## [◆ ](#gacfbd6a2cb3038e5aba1e2216d65ebc78)DT\_PHA\_HAS\_CELL\_AT\_IDX

| #define DT\_PHA\_HAS\_CELL\_AT\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT8(node\_id, \_P\_, pha, \

\_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

Does a phandle array have a named cell specifier at an index?

If this returns 1, then the phandle-array property `pha` has a cell named `cell` at index `idx`, and therefore [DT\_PHA\_BY\_IDX(node\_id,
pha, idx, cell)](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.") is valid. If it returns 0, it's an error to use [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.") with the same arguments.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | idx | index to check within `pha` |
    | cell | lowercase-and-underscores cell name whose existence to check at index `idx` |

Returns
:   1 if the named cell exists in the specifier at index idx, 0 otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
