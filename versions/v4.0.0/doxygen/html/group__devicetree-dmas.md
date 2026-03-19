---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__devicetree-dmas.html
original_path: doxygen/html/group__devicetree-dmas.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree DMA API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_DMAS\_CTLR\_BY\_IDX](#gac74e56d90f8abe4bb0b53acddb618a3a)(node\_id, idx) |
|  | Get the node identifier for the DMA controller from a dmas property at an index. |
| #define | [DT\_DMAS\_CTLR\_BY\_NAME](#ga8c148fc826dee34f5e4601f4a7aa9f55)(node\_id, name) |
|  | Get the node identifier for the DMA controller from a dmas property by name. |
| #define | [DT\_DMAS\_CTLR](#ga09a22a0e5133dc7514680c16373f6ad3)(node\_id) |
|  | Equivalent to [DT\_DMAS\_CTLR\_BY\_IDX(node\_id, 0)](#gac74e56d90f8abe4bb0b53acddb618a3a). |
| #define | [DT\_INST\_DMAS\_CTLR\_BY\_IDX](#ga5dbb1f22a0098a3493fd6f4cef9985a9)(inst, idx) |
|  | Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property at an index. |
| #define | [DT\_INST\_DMAS\_CTLR\_BY\_NAME](#gad098f0b51ee1f629c1259ca346f49303)(inst, name) |
|  | Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property by name. |
| #define | [DT\_INST\_DMAS\_CTLR](#ga32025fb8590eec09adaff23db1138e75)(inst) |
|  | Equivalent to [DT\_INST\_DMAS\_CTLR\_BY\_IDX(inst, 0)](#ga5dbb1f22a0098a3493fd6f4cef9985a9). |
| #define | [DT\_DMAS\_CELL\_BY\_IDX](#ga8aff7a91d19482964b8b56cb558c1b59)(node\_id, idx, cell) |
|  | Get a DMA specifier's cell value at an index. |
| #define | [DT\_INST\_DMAS\_CELL\_BY\_IDX](#gad4e1a8f22b8943328df2a3f8f2a149b7)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value at an index. |
| #define | [DT\_DMAS\_CELL\_BY\_NAME](#ga1b80ae7fee6bcc9aa2ad03435e70dd14)(node\_id, name, cell) |
|  | Get a DMA specifier's cell value by name. |
| #define | [DT\_INST\_DMAS\_CELL\_BY\_NAME](#ga2cc0124a66cf3b9f1c4c506b7f978d30)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value by name. |
| #define | [DT\_DMAS\_HAS\_IDX](#gab789e18935628f40d80f3b64ca5cbe80)(node\_id, idx) |
|  | Is index "idx" valid for a dmas property? |
| #define | [DT\_INST\_DMAS\_HAS\_IDX](#gaff634d5b2a342c73f001a5ee64b70829)(inst, idx) |
|  | Is index "idx" valid for a DT\_DRV\_COMPAT instance's dmas property? |
| #define | [DT\_DMAS\_HAS\_NAME](#ga865adb5b82c63e7f63451b96cd5a6404)(node\_id, name) |
|  | Does a dmas property have a named element? |
| #define | [DT\_INST\_DMAS\_HAS\_NAME](#gad60c155da3d850a61365ca7d12dc1813)(inst, name) |
|  | Does a DT\_DRV\_COMPAT instance's dmas property have a named element? |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga8aff7a91d19482964b8b56cb558c1b59)DT\_DMAS\_CELL\_BY\_IDX

| #define DT\_DMAS\_CELL\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, dmas, idx, cell)

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1536

Get a DMA specifier's cell value at an index.

Example devicetree fragment:

```
dma1: dma@... {
        compatible = "vnd,dma";
        #dma-cells = <2>;
};

dma2: dma@... {
        compatible = "vnd,dma";
        #dma-cells = <2>;
};

n: node {
    dmas = <&dma1 1 0x400>,
           <&dma2 6 0x404>;
};
```

Bindings fragment for the vnd,dma compatible:

```
dma-cells:
  - channel
  - config
```

Example usage:

```
DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 0, channel) // 1
DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 1, channel) // 6
DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 0, config) // 0x400
DT_DMAS_CELL_BY_IDX(DT_NODELABEL(n), 1, config) // 0x404
```

Parameters
:   | node\_id | node identifier for a node with a dmas property |
    | --- | --- |
    | idx | logical index into dmas property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index "idx"

See also
:   [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.")

## [◆ ](#ga1b80ae7fee6bcc9aa2ad03435e70dd14)DT\_DMAS\_CELL\_BY\_NAME

| #define DT\_DMAS\_CELL\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)(node\_id, dmas, name, cell)

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)

#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)

Get a value within a phandle-array specifier by name.

**Definition** devicetree.h:1631

Get a DMA specifier's cell value by name.

Example devicetree fragment:

```
dma1: dma@... {
        compatible = "vnd,dma";
        #dma-cells = <2>;
};

dma2: dma@... {
        compatible = "vnd,dma";
        #dma-cells = <2>;
};

n: node {
    dmas = <&dma1 1 0x400>,
           <&dma2 6 0x404>;
    dma-names = "tx", "rx";
};
```

Bindings fragment for the vnd,dma compatible:

```
dma-cells:
  - channel
  - config
```

Example usage:

```
DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), tx, channel) // 1
DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), rx, channel) // 6
DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), tx, config) // 0x400
DT_DMAS_CELL_BY_NAME(DT_NODELABEL(n), rx, config) // 0x404
```

Parameters
:   | node\_id | node identifier for a node with a dmas property |
    | --- | --- |
    | name | lowercase-and-underscores name of a dmas element as defined by the node's dma-names property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value in the specifier at the named element

See also
:   [DT\_PHA\_BY\_NAME()](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26 "Get a value within a phandle-array specifier by name.")

## [◆ ](#ga09a22a0e5133dc7514680c16373f6ad3)DT\_DMAS\_CTLR

| #define DT\_DMAS\_CTLR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_DMAS\_CTLR\_BY\_IDX](#gac74e56d90f8abe4bb0b53acddb618a3a)(node\_id, 0)

[DT\_DMAS\_CTLR\_BY\_IDX](#gac74e56d90f8abe4bb0b53acddb618a3a)

#define DT\_DMAS\_CTLR\_BY\_IDX(node\_id, idx)

Get the node identifier for the DMA controller from a dmas property at an index.

**Definition** dma.h:51

Equivalent to [DT\_DMAS\_CTLR\_BY\_IDX(node\_id, 0)](#gac74e56d90f8abe4bb0b53acddb618a3a).

Parameters
:   | node\_id | node identifier for a node with a dmas property |
    | --- | --- |

Returns
:   the node identifier for the DMA controller at index 0 in the node's "dmas" property

See also
:   [DT\_DMAS\_CTLR\_BY\_IDX()](#gac74e56d90f8abe4bb0b53acddb618a3a)

## [◆ ](#gac74e56d90f8abe4bb0b53acddb618a3a)DT\_DMAS\_CTLR\_BY\_IDX

| #define DT\_DMAS\_CTLR\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, dmas, idx)

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1757

Get the node identifier for the DMA controller from a dmas property at an index.

Example devicetree fragment:

```
dma1: dma@... { ... };

dma2: dma@... { ... };

n: node {
    dmas = <&dma1 1 2 0x400 0x3>,
            <&dma2 6 3 0x404 0x5>;
};
```

Example usage:

```
DT_DMAS_CTLR_BY_IDX(DT_NODELABEL(n), 0) // DT_NODELABEL(dma1)
DT_DMAS_CTLR_BY_IDX(DT_NODELABEL(n), 1) // DT_NODELABEL(dma2)
```

Parameters
:   | node\_id | node identifier for a node with a dmas property |
    | --- | --- |
    | idx | logical index into dmas property |

Returns
:   the node identifier for the DMA controller referenced at index "idx"

See also
:   [DT\_PROP\_BY\_PHANDLE\_IDX()](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d "Get a property value from a phandle in a property.")

## [◆ ](#ga8c148fc826dee34f5e4601f4a7aa9f55)DT\_DMAS\_CTLR\_BY\_NAME

| #define DT\_DMAS\_CTLR\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, dmas, name)

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1705

Get the node identifier for the DMA controller from a dmas property by name.

Example devicetree fragment:

```
dma1: dma@... { ... };

dma2: dma@... { ... };

n: node {
    dmas = <&dma1 1 2 0x400 0x3>,
            <&dma2 6 3 0x404 0x5>;
    dma-names = "tx", "rx";
};
```

Example usage:

```
DT_DMAS_CTLR_BY_NAME(DT_NODELABEL(n), tx) // DT_NODELABEL(dma1)
DT_DMAS_CTLR_BY_NAME(DT_NODELABEL(n), rx) // DT_NODELABEL(dma2)
```

Parameters
:   | node\_id | node identifier for a node with a dmas property |
    | --- | --- |
    | name | lowercase-and-underscores name of a dmas element as defined by the node's dma-names property |

Returns
:   the node identifier for the DMA controller in the named element

See also
:   [DT\_PHANDLE\_BY\_NAME()](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd "Get a phandle's node identifier from a phandle array by name.")

## [◆ ](#gab789e18935628f40d80f3b64ca5cbe80)DT\_DMAS\_HAS\_IDX

| #define DT\_DMAS\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_P\_dmas\_IDX\_, idx, \_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

Is index "idx" valid for a dmas property?

Parameters
:   | node\_id | node identifier for a node with a dmas property |
    | --- | --- |
    | idx | logical index into dmas property |

Returns
:   1 if the "dmas" property has index "idx", 0 otherwise

## [◆ ](#ga865adb5b82c63e7f63451b96cd5a6404)DT\_DMAS\_HAS\_NAME

| #define DT\_DMAS\_HAS\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_PROP\_HAS\_NAME](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)(node\_id, dmas, name)

[DT\_PROP\_HAS\_NAME](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)

#define DT\_PROP\_HAS\_NAME(node\_id, prop, name)

Is name name available in a foo-names property?

**Definition** devicetree.h:854

Does a dmas property have a named element?

Parameters
:   | node\_id | node identifier for a node with a dmas property |
    | --- | --- |
    | name | lowercase-and-underscores name of a dmas element as defined by the node's dma-names property |

Returns
:   1 if the dmas property has the named element, 0 otherwise

## [◆ ](#gad4e1a8f22b8943328df2a3f8f2a149b7)DT\_INST\_DMAS\_CELL\_BY\_IDX

| #define DT\_INST\_DMAS\_CELL\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), dmas, idx, cell)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into dmas property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index "idx"

See also
:   [DT\_DMAS\_CELL\_BY\_IDX()](#ga8aff7a91d19482964b8b56cb558c1b59)

## [◆ ](#ga2cc0124a66cf3b9f1c4c506b7f978d30)DT\_INST\_DMAS\_CELL\_BY\_NAME

| #define DT\_INST\_DMAS\_CELL\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_DMAS\_CELL\_BY\_NAME](#ga1b80ae7fee6bcc9aa2ad03435e70dd14)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, cell)

[DT\_DMAS\_CELL\_BY\_NAME](#ga1b80ae7fee6bcc9aa2ad03435e70dd14)

#define DT\_DMAS\_CELL\_BY\_NAME(node\_id, name, cell)

Get a DMA specifier's cell value by name.

**Definition** dma.h:220

Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value by name.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a dmas element as defined by the node's dma-names property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value in the specifier at the named element

See also
:   [DT\_DMAS\_CELL\_BY\_NAME()](#ga1b80ae7fee6bcc9aa2ad03435e70dd14)

## [◆ ](#ga32025fb8590eec09adaff23db1138e75)DT\_INST\_DMAS\_CTLR

| #define DT\_INST\_DMAS\_CTLR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_INST\_DMAS\_CTLR\_BY\_IDX](#ga5dbb1f22a0098a3493fd6f4cef9985a9)(inst, 0)

[DT\_INST\_DMAS\_CTLR\_BY\_IDX](#ga5dbb1f22a0098a3493fd6f4cef9985a9)

#define DT\_INST\_DMAS\_CTLR\_BY\_IDX(inst, idx)

Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property at an in...

**Definition** dma.h:102

Equivalent to [DT\_INST\_DMAS\_CTLR\_BY\_IDX(inst, 0)](#ga5dbb1f22a0098a3493fd6f4cef9985a9).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the node identifier for the DMA controller at index 0 in the instance's "dmas" property

See also
:   [DT\_DMAS\_CTLR\_BY\_IDX()](#gac74e56d90f8abe4bb0b53acddb618a3a)

## [◆ ](#ga5dbb1f22a0098a3493fd6f4cef9985a9)DT\_INST\_DMAS\_CTLR\_BY\_IDX

| #define DT\_INST\_DMAS\_CTLR\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_DMAS\_CTLR\_BY\_IDX](#gac74e56d90f8abe4bb0b53acddb618a3a)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into dmas property |

Returns
:   the node identifier for the DMA controller referenced at index "idx"

See also
:   [DT\_DMAS\_CTLR\_BY\_IDX()](#gac74e56d90f8abe4bb0b53acddb618a3a)

## [◆ ](#gad098f0b51ee1f629c1259ca346f49303)DT\_INST\_DMAS\_CTLR\_BY\_NAME

| #define DT\_INST\_DMAS\_CTLR\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_DMAS\_CTLR\_BY\_NAME](#ga8c148fc826dee34f5e4601f4a7aa9f55)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_DMAS\_CTLR\_BY\_NAME](#ga8c148fc826dee34f5e4601f4a7aa9f55)

#define DT\_DMAS\_CTLR\_BY\_NAME(node\_id, name)

Get the node identifier for the DMA controller from a dmas property by name.

**Definition** dma.h:80

Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property by name.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a dmas element as defined by the node's dma-names property |

Returns
:   the node identifier for the DMA controller in the named element

See also
:   [DT\_DMAS\_CTLR\_BY\_NAME()](#ga8c148fc826dee34f5e4601f4a7aa9f55)

## [◆ ](#gaff634d5b2a342c73f001a5ee64b70829)DT\_INST\_DMAS\_HAS\_IDX

| #define DT\_INST\_DMAS\_HAS\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_DMAS\_HAS\_IDX](#gab789e18935628f40d80f3b64ca5cbe80)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_DMAS\_HAS\_IDX](#gab789e18935628f40d80f3b64ca5cbe80)

#define DT\_DMAS\_HAS\_IDX(node\_id, idx)

Is index "idx" valid for a dmas property?

**Definition** dma.h:241

Is index "idx" valid for a DT\_DRV\_COMPAT instance's dmas property?

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into dmas property |

Returns
:   1 if the "dmas" property has a specifier at index "idx", 0 otherwise

## [◆ ](#gad60c155da3d850a61365ca7d12dc1813)DT\_INST\_DMAS\_HAS\_NAME

| #define DT\_INST\_DMAS\_HAS\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[dma.h](devicetree_2dma_8h.md)>`

**Value:**

[DT\_DMAS\_HAS\_NAME](#ga865adb5b82c63e7f63451b96cd5a6404)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_DMAS\_HAS\_NAME](#ga865adb5b82c63e7f63451b96cd5a6404)

#define DT\_DMAS\_HAS\_NAME(node\_id, name)

Does a dmas property have a named element?

**Definition** dma.h:260

Does a DT\_DRV\_COMPAT instance's dmas property have a named element?

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a dmas element as defined by the node's dma-names property |

Returns
:   1 if the dmas property has the named element, 0 otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
