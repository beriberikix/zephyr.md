---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__devicetree-reset-controller.html
original_path: doxygen/html/group__devicetree-reset-controller.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree Reset Controller API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_RESET\_CTLR\_BY\_IDX](#gaa730fe6a58ee0a2d9daf7e125048f9e6)(node\_id, idx) |
|  | Get the node identifier for the controller phandle from a "resets" phandle-array property at an index. |
| #define | [DT\_RESET\_CTLR](#ga55afbfa565375eb4b233051f7065e504)(node\_id) |
|  | Equivalent to [DT\_RESET\_CTLR\_BY\_IDX(node\_id, 0)](#gaa730fe6a58ee0a2d9daf7e125048f9e6). |
| #define | [DT\_RESET\_CTLR\_BY\_NAME](#ga5bc0702036df3a38ceb2d2741ee0717d)(node\_id, name) |
|  | Get the node identifier for the controller phandle from a resets phandle-array property by name. |
| #define | [DT\_RESET\_CELL\_BY\_IDX](#ga17918c75ef82acea60d7e65b6f1cee0a)(node\_id, idx, cell) |
|  | Get a reset specifier's cell value at an index. |
| #define | [DT\_RESET\_CELL\_BY\_NAME](#ga102229a7a1a30a29c5a5bf2bb0d42ada)(node\_id, name, cell) |
|  | Get a reset specifier's cell value by name. |
| #define | [DT\_RESET\_CELL](#ga626173f9cd280016f9f743d12bc4c047)(node\_id, cell) |
|  | Equivalent to [DT\_RESET\_CELL\_BY\_IDX(node\_id, 0, cell)](#ga17918c75ef82acea60d7e65b6f1cee0a). |
| #define | [DT\_INST\_RESET\_CTLR\_BY\_IDX](#ga44cc59dc014eb69aacd4b6fedb5b2a54)(inst, idx) |
|  | Get the node identifier for the controller phandle from a "resets" phandle-array property at an index. |
| #define | [DT\_INST\_RESET\_CTLR](#gadc32a356d6a18689ca4a20cc657ce600)(inst) |
|  | Equivalent to [DT\_INST\_RESET\_CTLR\_BY\_IDX(inst, 0)](#ga44cc59dc014eb69aacd4b6fedb5b2a54). |
| #define | [DT\_INST\_RESET\_CTLR\_BY\_NAME](#ga66352f34890886dc20fdaa3a3f9beea9)(inst, name) |
|  | Get the node identifier for the controller phandle from a resets phandle-array property by name. |
| #define | [DT\_INST\_RESET\_CELL\_BY\_IDX](#ga9727e93185d96b84ec2d53ef07597a02)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's reset specifier's cell value at an index. |
| #define | [DT\_INST\_RESET\_CELL\_BY\_NAME](#ga3d914f91e6f1514d2b0d6ec61cf92a5e)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's reset specifier's cell value by name. |
| #define | [DT\_INST\_RESET\_CELL](#gad078f74edd7e672f6c3fda91dec01f12)(inst, cell) |
|  | Equivalent to [DT\_INST\_RESET\_CELL\_BY\_IDX(inst, 0, cell)](#ga9727e93185d96b84ec2d53ef07597a02). |
| #define | [DT\_RESET\_ID\_BY\_IDX](#ga4259b4aa8bfe6f4ccb268c180541237d)(node\_id, idx) |
|  | Get a Reset Controller specifier's id cell at an index. |
| #define | [DT\_RESET\_ID](#gae8a5453df7ac3710858937485a9ee49b)(node\_id) |
|  | Equivalent to [DT\_RESET\_ID\_BY\_IDX(node\_id, 0)](#ga4259b4aa8bfe6f4ccb268c180541237d). |
| #define | [DT\_INST\_RESET\_ID\_BY\_IDX](#gac42ce32f6e5fd1ae2b449bcf60d70afc)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT instance's Reset Controller specifier's id cell value at an index. |
| #define | [DT\_INST\_RESET\_ID](#ga64080e5a9a0a568975323e637127e20f)(inst) |
|  | Equivalent to [DT\_INST\_RESET\_ID\_BY\_IDX(inst, 0)](#gac42ce32f6e5fd1ae2b449bcf60d70afc). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gad078f74edd7e672f6c3fda91dec01f12)DT\_INST\_RESET\_CELL

| #define DT\_INST\_RESET\_CELL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_INST\_RESET\_CELL\_BY\_IDX](#ga9727e93185d96b84ec2d53ef07597a02)(inst, 0, cell)

[DT\_INST\_RESET\_CELL\_BY\_IDX](#ga9727e93185d96b84ec2d53ef07597a02)

#define DT\_INST\_RESET\_CELL\_BY\_IDX(inst, idx, cell)

Get a DT\_DRV\_COMPAT instance's reset specifier's cell value at an index.

**Definition** reset.h:214

Equivalent to [DT\_INST\_RESET\_CELL\_BY\_IDX(inst, 0, cell)](#ga9727e93185d96b84ec2d53ef07597a02).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | cell | lowercase-and-underscores cell name |

Returns
:   the value of the cell inside the specifier at index 0

## [◆ ](#ga9727e93185d96b84ec2d53ef07597a02)DT\_INST\_RESET\_CELL\_BY\_IDX

| #define DT\_INST\_RESET\_CELL\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_RESET\_CELL\_BY\_IDX](#ga17918c75ef82acea60d7e65b6f1cee0a)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx, cell)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

[DT\_RESET\_CELL\_BY\_IDX](#ga17918c75ef82acea60d7e65b6f1cee0a)

#define DT\_RESET\_CELL\_BY\_IDX(node\_id, idx, cell)

Get a reset specifier's cell value at an index.

**Definition** reset.h:121

Get a DT\_DRV\_COMPAT instance's reset specifier's cell value at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into resets property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index "idx"

See also
:   [DT\_RESET\_CELL\_BY\_IDX()](#ga17918c75ef82acea60d7e65b6f1cee0a)

## [◆ ](#ga3d914f91e6f1514d2b0d6ec61cf92a5e)DT\_INST\_RESET\_CELL\_BY\_NAME

| #define DT\_INST\_RESET\_CELL\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_RESET\_CELL\_BY\_NAME](#ga102229a7a1a30a29c5a5bf2bb0d42ada)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, cell)

[DT\_RESET\_CELL\_BY\_NAME](#ga102229a7a1a30a29c5a5bf2bb0d42ada)

#define DT\_RESET\_CELL\_BY\_NAME(node\_id, name, cell)

Get a reset specifier's cell value by name.

**Definition** reset.h:155

Get a DT\_DRV\_COMPAT instance's reset specifier's cell value by name.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a resets element as defined by the node's reset-names property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value in the specifier at the named element

See also
:   [DT\_RESET\_CELL\_BY\_NAME()](#ga102229a7a1a30a29c5a5bf2bb0d42ada)

## [◆ ](#gadc32a356d6a18689ca4a20cc657ce600)DT\_INST\_RESET\_CTLR

| #define DT\_INST\_RESET\_CTLR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_INST\_RESET\_CTLR\_BY\_IDX](#ga44cc59dc014eb69aacd4b6fedb5b2a54)(inst, 0)

[DT\_INST\_RESET\_CTLR\_BY\_IDX](#ga44cc59dc014eb69aacd4b6fedb5b2a54)

#define DT\_INST\_RESET\_CTLR\_BY\_IDX(inst, idx)

Get the node identifier for the controller phandle from a "resets" phandle-array property at an index...

**Definition** reset.h:178

Equivalent to [DT\_INST\_RESET\_CTLR\_BY\_IDX(inst, 0)](#ga44cc59dc014eb69aacd4b6fedb5b2a54).

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   a node identifier for the reset controller at index 0 in "resets"

See also
:   [DT\_RESET\_CTLR()](#ga55afbfa565375eb4b233051f7065e504)

## [◆ ](#ga44cc59dc014eb69aacd4b6fedb5b2a54)DT\_INST\_RESET\_CTLR\_BY\_IDX

| #define DT\_INST\_RESET\_CTLR\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_RESET\_CTLR\_BY\_IDX](#gaa730fe6a58ee0a2d9daf7e125048f9e6)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_RESET\_CTLR\_BY\_IDX](#gaa730fe6a58ee0a2d9daf7e125048f9e6)

#define DT\_RESET\_CTLR\_BY\_IDX(node\_id, idx)

Get the node identifier for the controller phandle from a "resets" phandle-array property at an index...

**Definition** reset.h:50

Get the node identifier for the controller phandle from a "resets" phandle-array property at an index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | logical index into "resets" |

Returns
:   the node identifier for the reset controller referenced at index "idx"

See also
:   [DT\_RESET\_CTLR\_BY\_IDX()](#gaa730fe6a58ee0a2d9daf7e125048f9e6)

## [◆ ](#ga66352f34890886dc20fdaa3a3f9beea9)DT\_INST\_RESET\_CTLR\_BY\_NAME

| #define DT\_INST\_RESET\_CTLR\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_RESET\_CTLR\_BY\_NAME](#ga5bc0702036df3a38ceb2d2741ee0717d)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_RESET\_CTLR\_BY\_NAME](#ga5bc0702036df3a38ceb2d2741ee0717d)

#define DT\_RESET\_CTLR\_BY\_NAME(node\_id, name)

Get the node identifier for the controller phandle from a resets phandle-array property by name.

**Definition** reset.h:89

Get the node identifier for the controller phandle from a resets phandle-array property by name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a resets element as defined by the node's reset-names property |

Returns
:   the node identifier for the reset controller referenced by the named element

See also
:   [DT\_RESET\_CTLR\_BY\_NAME()](#ga5bc0702036df3a38ceb2d2741ee0717d)

## [◆ ](#ga64080e5a9a0a568975323e637127e20f)DT\_INST\_RESET\_ID

| #define DT\_INST\_RESET\_ID | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_INST\_RESET\_ID\_BY\_IDX](#gac42ce32f6e5fd1ae2b449bcf60d70afc)(inst, 0)

[DT\_INST\_RESET\_ID\_BY\_IDX](#gac42ce32f6e5fd1ae2b449bcf60d70afc)

#define DT\_INST\_RESET\_ID\_BY\_IDX(inst, idx)

Get a DT\_DRV\_COMPAT instance's Reset Controller specifier's id cell value at an index.

**Definition** reset.h:289

Equivalent to [DT\_INST\_RESET\_ID\_BY\_IDX(inst, 0)](#gac42ce32f6e5fd1ae2b449bcf60d70afc).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the id cell value at index 0

See also
:   [DT\_INST\_RESET\_ID\_BY\_IDX()](#gac42ce32f6e5fd1ae2b449bcf60d70afc)

## [◆ ](#gac42ce32f6e5fd1ae2b449bcf60d70afc)DT\_INST\_RESET\_ID\_BY\_IDX

| #define DT\_INST\_RESET\_ID\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_RESET\_ID\_BY\_IDX](#ga4259b4aa8bfe6f4ccb268c180541237d)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_RESET\_ID\_BY\_IDX](#ga4259b4aa8bfe6f4ccb268c180541237d)

#define DT\_RESET\_ID\_BY\_IDX(node\_id, idx)

Get a Reset Controller specifier's id cell at an index.

**Definition** reset.h:269

Get a DT\_DRV\_COMPAT instance's Reset Controller specifier's id cell value at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into "resets" |

Returns
:   the id cell value at index "idx"

See also
:   [DT\_RESET\_ID\_BY\_IDX()](#ga4259b4aa8bfe6f4ccb268c180541237d)

## [◆ ](#ga626173f9cd280016f9f743d12bc4c047)DT\_RESET\_CELL

| #define DT\_RESET\_CELL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_RESET\_CELL\_BY\_IDX](#ga17918c75ef82acea60d7e65b6f1cee0a)(node\_id, 0, cell)

Equivalent to [DT\_RESET\_CELL\_BY\_IDX(node\_id, 0, cell)](#ga17918c75ef82acea60d7e65b6f1cee0a).

Parameters
:   | node\_id | node identifier for a node with a resets property |
    | --- | --- |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index 0

See also
:   [DT\_RESET\_CELL\_BY\_IDX()](#ga17918c75ef82acea60d7e65b6f1cee0a)

## [◆ ](#ga17918c75ef82acea60d7e65b6f1cee0a)DT\_RESET\_CELL\_BY\_IDX

| #define DT\_RESET\_CELL\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, resets, idx, cell)

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1359

Get a reset specifier's cell value at an index.

Example devicetree fragment:

```
reset: reset-controller@... {
        compatible = "vnd,reset";
        #reset-cells = <1>;
};

n: node {
        resets = <&reset 10>;
};
```

Bindings fragment for the vnd,reset compatible:

```
reset-cells:
  - id
```

Example usage:

```
DT_RESET_CELL_BY_IDX(DT_NODELABEL(n), 0, id) // 10
```

Parameters
:   | node\_id | node identifier for a node with a resets property |
    | --- | --- |
    | idx | logical index into resets property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index "idx"

See also
:   [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.")

## [◆ ](#ga102229a7a1a30a29c5a5bf2bb0d42ada)DT\_RESET\_CELL\_BY\_NAME

| #define DT\_RESET\_CELL\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)(node\_id, resets, name, cell)

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)

#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)

Get a value within a phandle-array specifier by name.

**Definition** devicetree.h:1454

Get a reset specifier's cell value by name.

Example devicetree fragment:

```
reset: reset-controller@... {
        compatible = "vnd,reset";
        #reset-cells = <1>;
};

n: node {
        resets = <&reset 10>;
        reset-names = "alpha";
};
```

Bindings fragment for the vnd,reset compatible:

```
reset-cells:
  - id
```

Example usage:

```
DT_RESET_CELL_BY_NAME(DT_NODELABEL(n), alpha, id) // 10
```

Parameters
:   | node\_id | node identifier for a node with a resets property |
    | --- | --- |
    | name | lowercase-and-underscores name of a resets element as defined by the node's reset-names property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value in the specifier at the named element

See also
:   [DT\_PHA\_BY\_NAME()](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26 "Get a value within a phandle-array specifier by name.")

## [◆ ](#ga55afbfa565375eb4b233051f7065e504)DT\_RESET\_CTLR

| #define DT\_RESET\_CTLR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_RESET\_CTLR\_BY\_IDX](#gaa730fe6a58ee0a2d9daf7e125048f9e6)(node\_id, 0)

Equivalent to [DT\_RESET\_CTLR\_BY\_IDX(node\_id, 0)](#gaa730fe6a58ee0a2d9daf7e125048f9e6).

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   a node identifier for the reset controller at index 0 in "resets"

See also
:   [DT\_RESET\_CTLR\_BY\_IDX()](#gaa730fe6a58ee0a2d9daf7e125048f9e6)

## [◆ ](#gaa730fe6a58ee0a2d9daf7e125048f9e6)DT\_RESET\_CTLR\_BY\_IDX

| #define DT\_RESET\_CTLR\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, resets, idx)

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1580

Get the node identifier for the controller phandle from a "resets" phandle-array property at an index.

Example devicetree fragment:

```
reset1: reset-controller@... { ... };

reset2: reset-controller@... { ... };

n: node {
        resets = <&reset1 10>, <&reset2 20>;
};
```

Example usage:

```
DT_RESET_CTLR_BY_IDX(DT_NODELABEL(n), 0)) // DT_NODELABEL(reset1)
DT_RESET_CTLR_BY_IDX(DT_NODELABEL(n), 1)) // DT_NODELABEL(reset2)
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into "resets" |

Returns
:   the node identifier for the reset controller referenced at index "idx"

See also
:   [DT\_PHANDLE\_BY\_IDX()](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de "Get a node identifier for a phandle in a property.")

## [◆ ](#ga5bc0702036df3a38ceb2d2741ee0717d)DT\_RESET\_CTLR\_BY\_NAME

| #define DT\_RESET\_CTLR\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, resets, name)

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1528

Get the node identifier for the controller phandle from a resets phandle-array property by name.

Example devicetree fragment:

```
reset1: reset-controller@... { ... };

reset2: reset-controller@... { ... };

n: node {
        resets = <&reset1 10>, <&reset2 20>;
        reset-names = "alpha", "beta";
};
```

Example usage:

```
DT_RESET_CTLR_BY_NAME(DT_NODELABEL(n), alpha) // DT_NODELABEL(reset1)
DT_RESET_CTLR_BY_NAME(DT_NODELABEL(n), beta) // DT_NODELABEL(reset2)
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores name of a resets element as defined by the node's reset-names property |

Returns
:   the node identifier for the reset controller referenced by name

See also
:   [DT\_PHANDLE\_BY\_NAME()](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd "Get a phandle's node identifier from a phandle array by name.")

## [◆ ](#gae8a5453df7ac3710858937485a9ee49b)DT\_RESET\_ID

| #define DT\_RESET\_ID | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_RESET\_ID\_BY\_IDX](#ga4259b4aa8bfe6f4ccb268c180541237d)(node\_id, 0)

Equivalent to [DT\_RESET\_ID\_BY\_IDX(node\_id, 0)](#ga4259b4aa8bfe6f4ccb268c180541237d).

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the id cell value at index 0

See also
:   [DT\_RESET\_ID\_BY\_IDX()](#ga4259b4aa8bfe6f4ccb268c180541237d)

## [◆ ](#ga4259b4aa8bfe6f4ccb268c180541237d)DT\_RESET\_ID\_BY\_IDX

| #define DT\_RESET\_ID\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[reset.h](devicetree_2reset_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, resets, idx, id)

Get a Reset Controller specifier's id cell at an index.

This macro only works for Reset Controller specifiers with cells named "id". Refer to the node's binding to check if necessary.

Example devicetree fragment:

```
reset: reset-controller@... {
        compatible = "vnd,reset";
        #reset-cells = <1>;
};

n: node {
        resets = <&reset 10>;
};
```

Bindings fragment for the vnd,reset compatible:

```
reset-cells:
  - id
```

Example usage:

```
DT_RESET_ID_BY_IDX(DT_NODELABEL(n), 0) // 10
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into "resets" |

Returns
:   the id cell value at index "idx"

See also
:   [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.")

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
