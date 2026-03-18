---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__devicetree-io-channels.html
original_path: doxygen/html/group__devicetree-io-channels.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree IO Channels API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX](#gaf5bbae59dca995d827ff3ec8b9ce187c)(node\_id, idx) |
|  | Get the node identifier for the node referenced by an io-channels property at an index. |
| #define | [DT\_IO\_CHANNELS\_CTLR\_BY\_NAME](#ga1d6422230eb139beec9ac0f25ca2eab3)(node\_id, name) |
|  | Get the node identifier for the node referenced by an io-channels property by name. |
| #define | [DT\_IO\_CHANNELS\_CTLR](#gaef1d0ee74798d9e60f5c5fa0c0f8db48)(node\_id) |
|  | Equivalent to [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, 0)](#gaf5bbae59dca995d827ff3ec8b9ce187c). |
| #define | [DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX](#gacf417be0bda7b8ddfb20503f8d846822)(inst, idx) |
|  | Get the node identifier from a DT\_DRV\_COMPAT instance's io-channels property at an index. |
| #define | [DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_NAME](#gacd4b12a7698d44b56673e66643c2f88f)(inst, name) |
|  | Get the node identifier from a DT\_DRV\_COMPAT instance's io-channels property by name. |
| #define | [DT\_INST\_IO\_CHANNELS\_CTLR](#gaf25c454ac2cf285b3efa2e9a4251dd0e)(inst) |
|  | Equivalent to [DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX(inst, 0)](#gacf417be0bda7b8ddfb20503f8d846822). |
| #define | [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX](#ga290c912d0a96ba65bb44341a783fac19)(node\_id, idx) |
|  | Get an io-channels specifier input cell at an index. |
| #define | [DT\_IO\_CHANNELS\_INPUT\_BY\_NAME](#ga6870a8215f61f87c3cb8f137a7bbbcc3)(node\_id, name) |
|  | Get an io-channels specifier input cell by name. |
| #define | [DT\_IO\_CHANNELS\_INPUT](#gadcb598f00280ae1fa488e7982971e7d6)(node\_id) |
|  | Equivalent to [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, 0)](#ga290c912d0a96ba65bb44341a783fac19). |
| #define | [DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX](#gac396f180ab5b24bdca01c021447a0211)(inst, idx) |
|  | Get an input cell from the "DT\_DRV\_INST(inst)" io-channels property at an index. |
| #define | [DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_NAME](#ga09cbce4296bd4982d2ed1e5cea45da5e)(inst, name) |
|  | Get an input cell from the "DT\_DRV\_INST(inst)" io-channels property by name. |
| #define | [DT\_INST\_IO\_CHANNELS\_INPUT](#ga736d38a4e3a3a5e2e294e50df805c320)(inst) |
|  | Equivalent to [DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX(inst, 0)](#gac396f180ab5b24bdca01c021447a0211). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaf25c454ac2cf285b3efa2e9a4251dd0e)DT\_INST\_IO\_CHANNELS\_CTLR

| #define DT\_INST\_IO\_CHANNELS\_CTLR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX](#gacf417be0bda7b8ddfb20503f8d846822)(inst, 0)

[DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX](#gacf417be0bda7b8ddfb20503f8d846822)

#define DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX(inst, idx)

Get the node identifier from a DT\_DRV\_COMPAT instance's io-channels property at an index.

**Definition** io-channels.h:100

Equivalent to [DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX(inst, 0)](#gacf417be0bda7b8ddfb20503f8d846822).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the node identifier for the node referenced at index 0 in the node's "io-channels" property

See also
:   [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX()](#gaf5bbae59dca995d827ff3ec8b9ce187c)

## [◆ ](#gacf417be0bda7b8ddfb20503f8d846822)DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX

| #define DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_IO\_CHANNELS\_CTLR\_BY\_IDX](#gaf5bbae59dca995d827ff3ec8b9ce187c)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

[DT\_IO\_CHANNELS\_CTLR\_BY\_IDX](#gaf5bbae59dca995d827ff3ec8b9ce187c)

#define DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, idx)

Get the node identifier for the node referenced by an io-channels property at an index.

**Definition** io-channels.h:50

Get the node identifier from a DT\_DRV\_COMPAT instance's io-channels property at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into io-channels property |

Returns
:   the node identifier for the node referenced at index "idx"

See also
:   [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX()](#gaf5bbae59dca995d827ff3ec8b9ce187c)

## [◆ ](#gacd4b12a7698d44b56673e66643c2f88f)DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_NAME

| #define DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_IO\_CHANNELS\_CTLR\_BY\_NAME](#ga1d6422230eb139beec9ac0f25ca2eab3)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_IO\_CHANNELS\_CTLR\_BY\_NAME](#ga1d6422230eb139beec9ac0f25ca2eab3)

#define DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(node\_id, name)

Get the node identifier for the node referenced by an io-channels property by name.

**Definition** io-channels.h:79

Get the node identifier from a DT\_DRV\_COMPAT instance's io-channels property by name.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of an io-channels element as defined by the node's io-channel-names property |

Returns
:   the node identifier for the node referenced at the named element

See also
:   [DT\_IO\_CHANNELS\_CTLR\_BY\_NAME()](#ga1d6422230eb139beec9ac0f25ca2eab3)

## [◆ ](#ga736d38a4e3a3a5e2e294e50df805c320)DT\_INST\_IO\_CHANNELS\_INPUT

| #define DT\_INST\_IO\_CHANNELS\_INPUT | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX](#gac396f180ab5b24bdca01c021447a0211)(inst, 0)

[DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX](#gac396f180ab5b24bdca01c021447a0211)

#define DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX(inst, idx)

Get an input cell from the "DT\_DRV\_INST(inst)" io-channels property at an index.

**Definition** io-channels.h:221

Equivalent to [DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX(inst, 0)](#gac396f180ab5b24bdca01c021447a0211).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the input cell in the specifier at index 0

## [◆ ](#gac396f180ab5b24bdca01c021447a0211)DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX

| #define DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_IO\_CHANNELS\_INPUT\_BY\_IDX](#ga290c912d0a96ba65bb44341a783fac19)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_IO\_CHANNELS\_INPUT\_BY\_IDX](#ga290c912d0a96ba65bb44341a783fac19)

#define DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, idx)

Get an io-channels specifier input cell at an index.

**Definition** io-channels.h:161

Get an input cell from the "DT\_DRV\_INST(inst)" io-channels property at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into io-channels property |

Returns
:   the input cell in the specifier at index "idx"

See also
:   [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX()](#ga290c912d0a96ba65bb44341a783fac19)

## [◆ ](#ga09cbce4296bd4982d2ed1e5cea45da5e)DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_NAME

| #define DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_IO\_CHANNELS\_INPUT\_BY\_NAME](#ga6870a8215f61f87c3cb8f137a7bbbcc3)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_IO\_CHANNELS\_INPUT\_BY\_NAME](#ga6870a8215f61f87c3cb8f137a7bbbcc3)

#define DT\_IO\_CHANNELS\_INPUT\_BY\_NAME(node\_id, name)

Get an io-channels specifier input cell by name.

**Definition** io-channels.h:203

Get an input cell from the "DT\_DRV\_INST(inst)" io-channels property by name.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of an io-channels element as defined by the instance's io-channel-names property |

Returns
:   the input cell in the specifier at the named element

See also
:   [DT\_IO\_CHANNELS\_INPUT\_BY\_NAME()](#ga6870a8215f61f87c3cb8f137a7bbbcc3)

## [◆ ](#gaef1d0ee74798d9e60f5c5fa0c0f8db48)DT\_IO\_CHANNELS\_CTLR

| #define DT\_IO\_CHANNELS\_CTLR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_IO\_CHANNELS\_CTLR\_BY\_IDX](#gaf5bbae59dca995d827ff3ec8b9ce187c)(node\_id, 0)

Equivalent to [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, 0)](#gaf5bbae59dca995d827ff3ec8b9ce187c).

Parameters
:   | node\_id | node identifier for a node with an io-channels property |
    | --- | --- |

Returns
:   the node identifier for the node referenced at index 0 in the node's "io-channels" property

See also
:   [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX()](#gaf5bbae59dca995d827ff3ec8b9ce187c)

## [◆ ](#gaf5bbae59dca995d827ff3ec8b9ce187c)DT\_IO\_CHANNELS\_CTLR\_BY\_IDX

| #define DT\_IO\_CHANNELS\_CTLR\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, io\_channels, idx)

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1628

Get the node identifier for the node referenced by an io-channels property at an index.

Example devicetree fragment:

```
adc1: adc@... { ... };

adc2: adc@... { ... };

n: node {
        io-channels = <&adc1 10>, <&adc2 20>;
};
```

Example usage:

```
DT_IO_CHANNELS_CTLR_BY_IDX(DT_NODELABEL(n), 0) // DT_NODELABEL(adc1)
DT_IO_CHANNELS_CTLR_BY_IDX(DT_NODELABEL(n), 1) // DT_NODELABEL(adc2)
```

Parameters
:   | node\_id | node identifier for a node with an io-channels property |
    | --- | --- |
    | idx | logical index into io-channels property |

Returns
:   the node identifier for the node referenced at index "idx"

See also
:   [DT\_PROP\_BY\_PHANDLE\_IDX()](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d "Get a property value from a phandle in a property.")

## [◆ ](#ga1d6422230eb139beec9ac0f25ca2eab3)DT\_IO\_CHANNELS\_CTLR\_BY\_NAME

| #define DT\_IO\_CHANNELS\_CTLR\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, io\_channels, name)

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1576

Get the node identifier for the node referenced by an io-channels property by name.

Example devicetree fragment:

```
adc1: adc@... { ... };

adc2: adc@... { ... };

n: node {
        io-channels = <&adc1 10>, <&adc2 20>;
        io-channel-names = "SENSOR", "BANDGAP";
};
```

Example usage:

[DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(DT\_NODELABEL(n), sensor)](#ga1d6422230eb139beec9ac0f25ca2eab3) // [DT\_NODELABEL(adc1)](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79 "Get a node identifier for a node label.") [DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(DT\_NODELABEL(n), bandgap)](#ga1d6422230eb139beec9ac0f25ca2eab3) // [DT\_NODELABEL(adc2)](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79 "Get a node identifier for a node label.")

Parameters
:   | node\_id | node identifier for a node with an io-channels property |
    | --- | --- |
    | name | lowercase-and-underscores name of an io-channels element as defined by the node's io-channel-names property |

Returns
:   the node identifier for the node referenced at the named element

See also
:   [DT\_PHANDLE\_BY\_NAME()](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd "Get a phandle's node identifier from a phandle array by name.")

## [◆ ](#gadcb598f00280ae1fa488e7982971e7d6)DT\_IO\_CHANNELS\_INPUT

| #define DT\_IO\_CHANNELS\_INPUT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_IO\_CHANNELS\_INPUT\_BY\_IDX](#ga290c912d0a96ba65bb44341a783fac19)(node\_id, 0)

Equivalent to [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, 0)](#ga290c912d0a96ba65bb44341a783fac19).

Parameters
:   | node\_id | node identifier for a node with an io-channels property |
    | --- | --- |

Returns
:   the input cell in the specifier at index 0

See also
:   [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX()](#ga290c912d0a96ba65bb44341a783fac19)

## [◆ ](#ga290c912d0a96ba65bb44341a783fac19)DT\_IO\_CHANNELS\_INPUT\_BY\_IDX

| #define DT\_IO\_CHANNELS\_INPUT\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, io\_channels, idx, input)

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1407

Get an io-channels specifier input cell at an index.

This macro only works for io-channels specifiers with cells named "input". Refer to the node's binding to check if necessary.

Example devicetree fragment:

```
adc1: adc@... {
        compatible = "vnd,adc";
        #io-channel-cells = <1>;
};

adc2: adc@... {
        compatible = "vnd,adc";
        #io-channel-cells = <1>;
};

n: node {
        io-channels = <&adc1 10>, <&adc2 20>;
};
```

Bindings fragment for the vnd,adc compatible:

io-channel-cells:

- input

Example usage:

```
DT_IO_CHANNELS_INPUT_BY_IDX(DT_NODELABEL(n), 0) // 10
DT_IO_CHANNELS_INPUT_BY_IDX(DT_NODELABEL(n), 1) // 20
```

Parameters
:   | node\_id | node identifier for a node with an io-channels property |
    | --- | --- |
    | idx | logical index into io-channels property |

Returns
:   the input cell in the specifier at index "idx"

See also
:   [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.")

## [◆ ](#ga6870a8215f61f87c3cb8f137a7bbbcc3)DT\_IO\_CHANNELS\_INPUT\_BY\_NAME

| #define DT\_IO\_CHANNELS\_INPUT\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[io-channels.h](io-channels_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)(node\_id, io\_channels, name, input)

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)

#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)

Get a value within a phandle-array specifier by name.

**Definition** devicetree.h:1502

Get an io-channels specifier input cell by name.

This macro only works for io-channels specifiers with cells named "input". Refer to the node's binding to check if necessary.

Example devicetree fragment:

```
adc1: adc@... {
        compatible = "vnd,adc";
        #io-channel-cells = <1>;
};

adc2: adc@... {
        compatible = "vnd,adc";
        #io-channel-cells = <1>;
};

n: node {
        io-channels = <&adc1 10>, <&adc2 20>;
        io-channel-names = "SENSOR", "BANDGAP";
};
```

Bindings fragment for the vnd,adc compatible:

io-channel-cells:

- input

Example usage:

```
DT_IO_CHANNELS_INPUT_BY_NAME(DT_NODELABEL(n), sensor) // 10
DT_IO_CHANNELS_INPUT_BY_NAME(DT_NODELABEL(n), bandgap) // 20
```

Parameters
:   | node\_id | node identifier for a node with an io-channels property |
    | --- | --- |
    | name | lowercase-and-underscores name of an io-channels element as defined by the node's io-channel-names property |

Returns
:   the input cell in the specifier at the named element

See also
:   [DT\_PHA\_BY\_NAME()](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26 "Get a value within a phandle-array specifier by name.")

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
