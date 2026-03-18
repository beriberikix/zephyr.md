---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__devicetree-clocks.html
original_path: doxygen/html/group__devicetree-clocks.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree Clocks API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_CLOCKS\_HAS\_IDX](#gabfdf51e2b14c05e84366cff1bb056da0)(node\_id, idx) |
|  | Test if a node has a clocks phandle-array property at a given index. |
| #define | [DT\_CLOCKS\_HAS\_NAME](#ga9d32df36dd18c4839e6e9efe509b17a4)(node\_id, name) |
|  | Test if a node has a clock-names array property holds a given name. |
| #define | [DT\_NUM\_CLOCKS](#ga22d4e8621b5bf56ed0ac8295dd11d7e3)(node\_id) |
|  | Get the number of elements in a clocks property. |
| #define | [DT\_CLOCKS\_CTLR\_BY\_IDX](#gab36c92fc26c3517031bce342148308c3)(node\_id, idx) |
|  | Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index. |
| #define | [DT\_CLOCKS\_CTLR](#ga69795ece1f4a46e2c26a8e2dbb452f23)(node\_id) |
|  | Equivalent to [DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, 0)](#gab36c92fc26c3517031bce342148308c3). |
| #define | [DT\_CLOCKS\_CTLR\_BY\_NAME](#gaf4c92378a2599ee7024f914ea3584404)(node\_id, name) |
|  | Get the node identifier for the controller phandle from a clocks phandle-array property by name. |
| #define | [DT\_CLOCKS\_CELL\_BY\_IDX](#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, idx, cell) |
|  | Get a clock specifier's cell value at an index. |
| #define | [DT\_CLOCKS\_CELL\_BY\_NAME](#gaca32bfb478ac92e6a760ad0761328d5a)(node\_id, name, cell) |
|  | Get a clock specifier's cell value by name. |
| #define | [DT\_CLOCKS\_CELL](#ga211bc385cbbb1d8b8fa52e2e0a52d23d)(node\_id, cell) |
|  | Equivalent to [DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, 0, cell)](#ga7db765e869b8455a6c56a8f22a7cc5c8). |
| #define | [DT\_INST\_CLOCKS\_HAS\_IDX](#gaf8ebb6ccd4915cc4069e92f804fb63ac)(inst, idx) |
|  | Equivalent to [DT\_CLOCKS\_HAS\_IDX(DT\_DRV\_INST(inst), idx)](#gabfdf51e2b14c05e84366cff1bb056da0). |
| #define | [DT\_INST\_CLOCKS\_HAS\_NAME](#ga6b2997f105a29ff5c136f3dbb6120287)(inst, name) |
|  | Equivalent to DT\_CLOCK\_HAS\_NAME(DT\_DRV\_INST(inst), name). |
| #define | [DT\_INST\_NUM\_CLOCKS](#gadab88fe4063540efc136e5ae270c7cfa)(inst) |
|  | Equivalent to [DT\_NUM\_CLOCKS(DT\_DRV\_INST(inst))](#ga22d4e8621b5bf56ed0ac8295dd11d7e3). |
| #define | [DT\_INST\_CLOCKS\_CTLR\_BY\_IDX](#gac4a7a89937eae57960a2091d7edc5fd3)(inst, idx) |
|  | Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index. |
| #define | [DT\_INST\_CLOCKS\_CTLR](#gaeebaf3a45822d86dfeb38a3fda66dc54)(inst) |
|  | Equivalent to [DT\_INST\_CLOCKS\_CTLR\_BY\_IDX(inst, 0)](#gac4a7a89937eae57960a2091d7edc5fd3). |
| #define | [DT\_INST\_CLOCKS\_CTLR\_BY\_NAME](#ga209f77daee5016ed0d0d678ec6ec57b7)(inst, name) |
|  | Get the node identifier for the controller phandle from a clocks phandle-array property by name. |
| #define | [DT\_INST\_CLOCKS\_CELL\_BY\_IDX](#ga5bee2e489f0818f0f2d1ec6d195bd3a8)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's clock specifier's cell value at an index. |
| #define | [DT\_INST\_CLOCKS\_CELL\_BY\_NAME](#ga976ab2adb237e5f1e0ba3496e9322d14)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's clock specifier's cell value by name. |
| #define | [DT\_INST\_CLOCKS\_CELL](#gad6a9584690066548b8d61489ad615a45)(inst, cell) |
|  | Equivalent to [DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, 0, cell)](#ga5bee2e489f0818f0f2d1ec6d195bd3a8). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga211bc385cbbb1d8b8fa52e2e0a52d23d)DT\_CLOCKS\_CELL

| #define DT\_CLOCKS\_CELL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_CLOCKS\_CELL\_BY\_IDX](#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, 0, cell)

[DT\_CLOCKS\_CELL\_BY\_IDX](#ga7db765e869b8455a6c56a8f22a7cc5c8)

#define DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, idx, cell)

Get a clock specifier's cell value at an index.

**Definition** clocks.h:207

Equivalent to [DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, 0, cell)](#ga7db765e869b8455a6c56a8f22a7cc5c8).

Parameters
:   | node\_id | node identifier for a node with a clocks property |
    | --- | --- |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index 0

See also
:   [DT\_CLOCKS\_CELL\_BY\_IDX()](#ga7db765e869b8455a6c56a8f22a7cc5c8)

## [◆ ](#ga7db765e869b8455a6c56a8f22a7cc5c8)DT\_CLOCKS\_CELL\_BY\_IDX

| #define DT\_CLOCKS\_CELL\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, clocks, idx, cell)

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1359

Get a clock specifier's cell value at an index.

Example devicetree fragment:

```
clk1: clock-controller@... {
        compatible = "vnd,clock";
        #clock-cells = < 2 >;
};

n: node {
        clocks = < &clk1 10 20 >, < &clk1 30 40 >;
};
```

Bindings fragment for the vnd,clock compatible:

```
clock-cells:
  - bus
  - bits
```

Example usage:

```
DT_CLOCKS_CELL_BY_IDX(DT_NODELABEL(n), 0, bus) // 10
DT_CLOCKS_CELL_BY_IDX(DT_NODELABEL(n), 1, bits) // 40
```

Parameters
:   | node\_id | node identifier for a node with a clocks property |
    | --- | --- |
    | idx | logical index into clocks property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index "idx"

See also
:   [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.")

## [◆ ](#gaca32bfb478ac92e6a760ad0761328d5a)DT\_CLOCKS\_CELL\_BY\_NAME

| #define DT\_CLOCKS\_CELL\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)(node\_id, clocks, name, cell)

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)

#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)

Get a value within a phandle-array specifier by name.

**Definition** devicetree.h:1454

Get a clock specifier's cell value by name.

Example devicetree fragment:

```
clk1: clock-controller@... {
        compatible = "vnd,clock";
        #clock-cells = < 2 >;
};

n: node {
        clocks = < &clk1 10 20 >, < &clk1 30 40 >;
        clock-names = "alpha", "beta";
};
```

Bindings fragment for the vnd,clock compatible:

```
clock-cells:
  - bus
  - bits
```

Example usage:

```
DT_CLOCKS_CELL_BY_NAME(DT_NODELABEL(n), alpha, bus) // 10
DT_CLOCKS_CELL_BY_NAME(DT_NODELABEL(n), beta, bits) // 40
```

Parameters
:   | node\_id | node identifier for a node with a clocks property |
    | --- | --- |
    | name | lowercase-and-underscores name of a clocks element as defined by the node's clock-names property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value in the specifier at the named element

See also
:   [DT\_PHA\_BY\_NAME()](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26 "Get a value within a phandle-array specifier by name.")

## [◆ ](#ga69795ece1f4a46e2c26a8e2dbb452f23)DT\_CLOCKS\_CTLR

| #define DT\_CLOCKS\_CTLR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_CLOCKS\_CTLR\_BY\_IDX](#gab36c92fc26c3517031bce342148308c3)(node\_id, 0)

[DT\_CLOCKS\_CTLR\_BY\_IDX](#gab36c92fc26c3517031bce342148308c3)

#define DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, idx)

Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index...

**Definition** clocks.h:136

Equivalent to [DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, 0)](#gab36c92fc26c3517031bce342148308c3).

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   a node identifier for the clocks controller at index 0 in "clocks"

See also
:   [DT\_CLOCKS\_CTLR\_BY\_IDX()](#gab36c92fc26c3517031bce342148308c3)

## [◆ ](#gab36c92fc26c3517031bce342148308c3)DT\_CLOCKS\_CTLR\_BY\_IDX

| #define DT\_CLOCKS\_CTLR\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, clocks, idx)

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1580

Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index.

Example devicetree fragment:

```
clk1: clock-controller@... { ... };

clk2: clock-controller@... { ... };

n: node {
        clocks = <&clk1 10 20>, <&clk2 30 40>;
};
```

Example usage:

```
DT_CLOCKS_CTLR_BY_IDX(DT_NODELABEL(n), 0)) // DT_NODELABEL(clk1)
DT_CLOCKS_CTLR_BY_IDX(DT_NODELABEL(n), 1)) // DT_NODELABEL(clk2)
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into "clocks" |

Returns
:   the node identifier for the clock controller referenced at index "idx"

See also
:   [DT\_PHANDLE\_BY\_IDX()](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de "Get a node identifier for a phandle in a property.")

## [◆ ](#gaf4c92378a2599ee7024f914ea3584404)DT\_CLOCKS\_CTLR\_BY\_NAME

| #define DT\_CLOCKS\_CTLR\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, clocks, name)

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1528

Get the node identifier for the controller phandle from a clocks phandle-array property by name.

Example devicetree fragment:

```
clk1: clock-controller@... { ... };

clk2: clock-controller@... { ... };

n: node {
        clocks = <&clk1 10 20>, <&clk2 30 40>;
        clock-names = "alpha", "beta";
};
```

Example usage:

```
DT_CLOCKS_CTLR_BY_NAME(DT_NODELABEL(n), beta) // DT_NODELABEL(clk2)
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores name of a clocks element as defined by the node's clock-names property |

Returns
:   the node identifier for the clock controller referenced by name

See also
:   [DT\_PHANDLE\_BY\_NAME()](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd "Get a phandle's node identifier from a phandle array by name.")

## [◆ ](#gabfdf51e2b14c05e84366cff1bb056da0)DT\_CLOCKS\_HAS\_IDX

| #define DT\_CLOCKS\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)(node\_id, clocks, idx)

[DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)

#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx)

Is index idx valid for an array type property?

**Definition** devicetree.h:689

Test if a node has a clocks phandle-array property at a given index.

This expands to 1 if the given index is valid clocks property phandle-array index. Otherwise, it expands to 0.

Example devicetree fragment:

```
n1: node-1 {
        clocks = <...>, <...>;
};

n2: node-2 {
        clocks = <...>;
};
```

Example usage:

```
DT_CLOCKS_HAS_IDX(DT_NODELABEL(n1), 0) // 1
DT_CLOCKS_HAS_IDX(DT_NODELABEL(n1), 1) // 1
DT_CLOCKS_HAS_IDX(DT_NODELABEL(n1), 2) // 0
DT_CLOCKS_HAS_IDX(DT_NODELABEL(n2), 1) // 0
```

Parameters
:   | node\_id | node identifier; may or may not have any clocks property |
    | --- | --- |
    | idx | index of a clocks property phandle-array whose existence to check |

Returns
:   1 if the index exists, 0 otherwise

## [◆ ](#ga9d32df36dd18c4839e6e9efe509b17a4)DT\_CLOCKS\_HAS\_NAME

| #define DT\_CLOCKS\_HAS\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_PROP\_HAS\_NAME](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)(node\_id, clocks, name)

[DT\_PROP\_HAS\_NAME](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)

#define DT\_PROP\_HAS\_NAME(node\_id, prop, name)

Is name name available in a foo-names property?

**Definition** devicetree.h:724

Test if a node has a clock-names array property holds a given name.

This expands to 1 if the name is available as clocks-name array property cell. Otherwise, it expands to 0.

Example devicetree fragment:

```
n1: node-1 {
        clocks = <...>, <...>;
        clock-names = "alpha", "beta";
};

n2: node-2 {
        clocks = <...>;
        clock-names = "alpha";
};
```

Example usage:

```
DT_CLOCKS_HAS_NAME(DT_NODELABEL(n1), alpha) // 1
DT_CLOCKS_HAS_NAME(DT_NODELABEL(n1), beta)  // 1
DT_CLOCKS_HAS_NAME(DT_NODELABEL(n2), beta)  // 0
```

Parameters
:   | node\_id | node identifier; may or may not have any clock-names property. |
    | --- | --- |
    | name | lowercase-and-underscores clock-names cell value name to check |

Returns
:   1 if the clock name exists, 0 otherwise

## [◆ ](#gad6a9584690066548b8d61489ad615a45)DT\_INST\_CLOCKS\_CELL

| #define DT\_INST\_CLOCKS\_CELL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_INST\_CLOCKS\_CELL\_BY\_IDX](#ga5bee2e489f0818f0f2d1ec6d195bd3a8)(inst, 0, cell)

[DT\_INST\_CLOCKS\_CELL\_BY\_IDX](#ga5bee2e489f0818f0f2d1ec6d195bd3a8)

#define DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, idx, cell)

Get a DT\_DRV\_COMPAT instance's clock specifier's cell value at an index.

**Definition** clocks.h:326

Equivalent to [DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, 0, cell)](#ga5bee2e489f0818f0f2d1ec6d195bd3a8).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | cell | lowercase-and-underscores cell name |

Returns
:   the value of the cell inside the specifier at index 0

## [◆ ](#ga5bee2e489f0818f0f2d1ec6d195bd3a8)DT\_INST\_CLOCKS\_CELL\_BY\_IDX

| #define DT\_INST\_CLOCKS\_CELL\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_CLOCKS\_CELL\_BY\_IDX](#ga7db765e869b8455a6c56a8f22a7cc5c8)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx, cell)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

Get a DT\_DRV\_COMPAT instance's clock specifier's cell value at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into clocks property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index "idx"

See also
:   [DT\_CLOCKS\_CELL\_BY\_IDX()](#ga7db765e869b8455a6c56a8f22a7cc5c8)

## [◆ ](#ga976ab2adb237e5f1e0ba3496e9322d14)DT\_INST\_CLOCKS\_CELL\_BY\_NAME

| #define DT\_INST\_CLOCKS\_CELL\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_CLOCKS\_CELL\_BY\_NAME](#gaca32bfb478ac92e6a760ad0761328d5a)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, cell)

[DT\_CLOCKS\_CELL\_BY\_NAME](#gaca32bfb478ac92e6a760ad0761328d5a)

#define DT\_CLOCKS\_CELL\_BY\_NAME(node\_id, name, cell)

Get a clock specifier's cell value by name.

**Definition** clocks.h:243

Get a DT\_DRV\_COMPAT instance's clock specifier's cell value by name.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a clocks element as defined by the node's clock-names property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value in the specifier at the named element

See also
:   [DT\_CLOCKS\_CELL\_BY\_NAME()](#gaca32bfb478ac92e6a760ad0761328d5a)

## [◆ ](#gaeebaf3a45822d86dfeb38a3fda66dc54)DT\_INST\_CLOCKS\_CTLR

| #define DT\_INST\_CLOCKS\_CTLR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_INST\_CLOCKS\_CTLR\_BY\_IDX](#gac4a7a89937eae57960a2091d7edc5fd3)(inst, 0)

[DT\_INST\_CLOCKS\_CTLR\_BY\_IDX](#gac4a7a89937eae57960a2091d7edc5fd3)

#define DT\_INST\_CLOCKS\_CTLR\_BY\_IDX(inst, idx)

Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index...

**Definition** clocks.h:291

Equivalent to [DT\_INST\_CLOCKS\_CTLR\_BY\_IDX(inst, 0)](#gac4a7a89937eae57960a2091d7edc5fd3).

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   a node identifier for the clocks controller at index 0 in "clocks"

See also
:   [DT\_CLOCKS\_CTLR()](#ga69795ece1f4a46e2c26a8e2dbb452f23)

## [◆ ](#gac4a7a89937eae57960a2091d7edc5fd3)DT\_INST\_CLOCKS\_CTLR\_BY\_IDX

| #define DT\_INST\_CLOCKS\_CTLR\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_CLOCKS\_CTLR\_BY\_IDX](#gab36c92fc26c3517031bce342148308c3)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | logical index into "clocks" |

Returns
:   the node identifier for the clock controller referenced at index "idx"

See also
:   [DT\_CLOCKS\_CTLR\_BY\_IDX()](#gab36c92fc26c3517031bce342148308c3)

## [◆ ](#ga209f77daee5016ed0d0d678ec6ec57b7)DT\_INST\_CLOCKS\_CTLR\_BY\_NAME

| #define DT\_INST\_CLOCKS\_CTLR\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_CLOCKS\_CTLR\_BY\_NAME](#gaf4c92378a2599ee7024f914ea3584404)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_CLOCKS\_CTLR\_BY\_NAME](#gaf4c92378a2599ee7024f914ea3584404)

#define DT\_CLOCKS\_CTLR\_BY\_NAME(node\_id, name)

Get the node identifier for the controller phandle from a clocks phandle-array property by name.

**Definition** clocks.h:173

Get the node identifier for the controller phandle from a clocks phandle-array property by name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a clocks element as defined by the node's clock-names property |

Returns
:   the node identifier for the clock controller referenced by the named element

See also
:   [DT\_CLOCKS\_CTLR\_BY\_NAME()](#gaf4c92378a2599ee7024f914ea3584404)

## [◆ ](#gaf8ebb6ccd4915cc4069e92f804fb63ac)DT\_INST\_CLOCKS\_HAS\_IDX

| #define DT\_INST\_CLOCKS\_HAS\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_CLOCKS\_HAS\_IDX](#gabfdf51e2b14c05e84366cff1bb056da0)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_CLOCKS\_HAS\_IDX](#gabfdf51e2b14c05e84366cff1bb056da0)

#define DT\_CLOCKS\_HAS\_IDX(node\_id, idx)

Test if a node has a clocks phandle-array property at a given index.

**Definition** clocks.h:52

Equivalent to [DT\_CLOCKS\_HAS\_IDX(DT\_DRV\_INST(inst), idx)](#gabfdf51e2b14c05e84366cff1bb056da0).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number; may or may not have any clocks property |
    | --- | --- |
    | idx | index of a clocks property phandle-array whose existence to check |

Returns
:   1 if the index exists, 0 otherwise

## [◆ ](#ga6b2997f105a29ff5c136f3dbb6120287)DT\_INST\_CLOCKS\_HAS\_NAME

| #define DT\_INST\_CLOCKS\_HAS\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_CLOCKS\_HAS\_NAME](#ga9d32df36dd18c4839e6e9efe509b17a4)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_CLOCKS\_HAS\_NAME](#ga9d32df36dd18c4839e6e9efe509b17a4)

#define DT\_CLOCKS\_HAS\_NAME(node\_id, name)

Test if a node has a clock-names array property holds a given name.

**Definition** clocks.h:83

Equivalent to DT\_CLOCK\_HAS\_NAME(DT\_DRV\_INST(inst), name).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number; may or may not have any clock-names property. |
    | --- | --- |
    | name | lowercase-and-underscores clock-names cell value name to check |

Returns
:   1 if the clock name exists, 0 otherwise

## [◆ ](#gadab88fe4063540efc136e5ae270c7cfa)DT\_INST\_NUM\_CLOCKS

| #define DT\_INST\_NUM\_CLOCKS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_NUM\_CLOCKS](#ga22d4e8621b5bf56ed0ac8295dd11d7e3)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_NUM\_CLOCKS](#ga22d4e8621b5bf56ed0ac8295dd11d7e3)

#define DT\_NUM\_CLOCKS(node\_id)

Get the number of elements in a clocks property.

**Definition** clocks.h:107

Equivalent to [DT\_NUM\_CLOCKS(DT\_DRV\_INST(inst))](#ga22d4e8621b5bf56ed0ac8295dd11d7e3).

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   number of elements in the clocks property

## [◆ ](#ga22d4e8621b5bf56ed0ac8295dd11d7e3)DT\_NUM\_CLOCKS

| #define DT\_NUM\_CLOCKS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[clocks.h](clocks_8h.md)>`

**Value:**

[DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)(node\_id, clocks)

[DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)

#define DT\_PROP\_LEN(node\_id, prop)

Get a property's logical length.

**Definition** devicetree.h:649

Get the number of elements in a clocks property.

Example devicetree fragment:

```
n1: node-1 {
        clocks = <&foo>, <&bar>;
};

n2: node-2 {
        clocks = <&foo>;
};
```

Example usage:

```
DT_NUM_CLOCKS(DT_NODELABEL(n1)) // 2
DT_NUM_CLOCKS(DT_NODELABEL(n2)) // 1
```

Parameters
:   | node\_id | node identifier with a clocks property |
    | --- | --- |

Returns
:   number of elements in the property

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
