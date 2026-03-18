---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__devicetree-pinctrl.html
original_path: doxygen/html/group__devicetree-pinctrl.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Pin control

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_PINCTRL\_BY\_IDX](#ga24089220a93bc955700fba2c6170090e)(node\_id, pc\_idx, idx) |
|  | Get a node identifier for a phandle in a pinctrl property by index. |
| #define | [DT\_PINCTRL\_0](#gaf4e6f811ea4b1698c048d5dd8bfa604a)(node\_id, idx) |
|  | Get a node identifier from a pinctrl-0 property. |
| #define | [DT\_PINCTRL\_BY\_NAME](#ga1cd336f902738fd684f3d81b3fb6caae)(node\_id, name, idx) |
|  | Get a node identifier for a phandle inside a pinctrl node by name. |
| #define | [DT\_PINCTRL\_NAME\_TO\_IDX](#ga36eb691efc2a4854ccb62555aeade785)(node\_id, name) |
|  | Convert a pinctrl name to its corresponding index. |
| #define | [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN](#ga47b0e5a18919f9f4829209cccbdeb430)(node\_id, pc\_idx) |
|  | Convert a pinctrl property index to its name as a token. |
| #define | [DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN](#gaa6eec236ccde612e88017b027f4ba711)(node\_id, pc\_idx) |
|  | Like [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN()](#ga47b0e5a18919f9f4829209cccbdeb430), but with an uppercased result. |
| #define | [DT\_NUM\_PINCTRLS\_BY\_IDX](#ga6ae1bab2a71cb628405ec43d38705606)(node\_id, pc\_idx) |
|  | Get the number of phandles in a pinctrl property. |
| #define | [DT\_NUM\_PINCTRLS\_BY\_NAME](#gaf96f1c82cc08008882f52e719ecd348c)(node\_id, name) |
|  | Like [DT\_NUM\_PINCTRLS\_BY\_IDX()](#ga6ae1bab2a71cb628405ec43d38705606), but by name instead. |
| #define | [DT\_NUM\_PINCTRL\_STATES](#gaa2a012ce1d9ba026ee90001ae7f80381)(node\_id) |
|  | Get the number of pinctrl properties in a node. |
| #define | [DT\_PINCTRL\_HAS\_IDX](#ga5f1493cbfb7578b8fe3e37953aa9feaa)(node\_id, pc\_idx) |
|  | Test if a node has a pinctrl property with an index. |
| #define | [DT\_PINCTRL\_HAS\_NAME](#gac9cd8112ad745f34eb6f6e4a13d7fd7e)(node\_id, name) |
|  | Test if a node has a pinctrl property with a name. |
| #define | [DT\_INST\_PINCTRL\_BY\_IDX](#ga3388742fe3fb1f32a03566730890eaf0)(inst, pc\_idx, idx) |
|  | Get a node identifier for a phandle in a pinctrl property by index for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_0](#ga3cd59afe76bc5d82b63ef21cae451f11)(inst, idx) |
|  | Get a node identifier from a pinctrl-0 property for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_BY\_NAME](#ga4c171c27a91bd85e49b725bda6c05619)(inst, name, idx) |
|  | Get a node identifier for a phandle inside a pinctrl node for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_NAME\_TO\_IDX](#ga12c18d8d9724d98d121d8118b43686c3)(inst, name) |
|  | Convert a pinctrl name to its corresponding index for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_TOKEN](#ga80c3fb3defb7315877dc48db2932ef70)(inst, pc\_idx) |
|  | Convert a pinctrl index to its name as an uppercased token. |
| #define | [DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN](#ga6d01324cecb6db502c46c42817c56bc9)(inst, pc\_idx) |
|  | Convert a pinctrl index to its name as an uppercased token. |
| #define | [DT\_INST\_NUM\_PINCTRLS\_BY\_IDX](#ga1de8198573428ec717733204d91f0391)(inst, pc\_idx) |
|  | Get the number of phandles in a pinctrl property for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_NUM\_PINCTRLS\_BY\_NAME](#gae253489146c61cb075f06192948275ff)(inst, name) |
|  | Like [DT\_INST\_NUM\_PINCTRLS\_BY\_IDX()](#ga1de8198573428ec717733204d91f0391), but by name instead. |
| #define | [DT\_INST\_NUM\_PINCTRL\_STATES](#ga4e91cf82c2a7aaecdb43761b217231d4)(inst) |
|  | Get the number of pinctrl properties in a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_HAS\_IDX](#ga53f17d0a6061cad7270544068f1cb003)(inst, pc\_idx) |
|  | Test if a DT\_DRV\_COMPAT instance has a pinctrl property with an index. |
| #define | [DT\_INST\_PINCTRL\_HAS\_NAME](#ga0e2af9dde68b57f6b1ffc86143fc2e40)(inst, name) |
|  | Test if a DT\_DRV\_COMPAT instance has a pinctrl property with a name. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga4e91cf82c2a7aaecdb43761b217231d4)DT\_INST\_NUM\_PINCTRL\_STATES

| #define DT\_INST\_NUM\_PINCTRL\_STATES | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_NUM\_PINCTRL\_STATES](#gaa2a012ce1d9ba026ee90001ae7f80381)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

[DT\_NUM\_PINCTRL\_STATES](#gaa2a012ce1d9ba026ee90001ae7f80381)

#define DT\_NUM\_PINCTRL\_STATES(node\_id)

Get the number of pinctrl properties in a node.

**Definition** pinctrl.h:239

Get the number of pinctrl properties in a DT\_DRV\_COMPAT instance.

This is equivalent to [DT\_NUM\_PINCTRL\_STATES(DT\_DRV\_INST(inst))](#gaa2a012ce1d9ba026ee90001ae7f80381).

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   number of pinctrl properties in the instance

## [◆ ](#ga1de8198573428ec717733204d91f0391)DT\_INST\_NUM\_PINCTRLS\_BY\_IDX

| #define DT\_INST\_NUM\_PINCTRLS\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_NUM\_PINCTRLS\_BY\_IDX](#ga6ae1bab2a71cb628405ec43d38705606)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pc\_idx)

[DT\_NUM\_PINCTRLS\_BY\_IDX](#ga6ae1bab2a71cb628405ec43d38705606)

#define DT\_NUM\_PINCTRLS\_BY\_IDX(node\_id, pc\_idx)

Get the number of phandles in a pinctrl property.

**Definition** pinctrl.h:189

Get the number of phandles in a pinctrl property for a DT\_DRV\_COMPAT instance.

This is equivalent to [DT\_NUM\_PINCTRLS\_BY\_IDX(DT\_DRV\_INST(inst),
pc\_idx)](#ga6ae1bab2a71cb628405ec43d38705606).

Parameters
:   | inst | instance number |
    | --- | --- |
    | pc\_idx | index of the pinctrl property itself |

Returns
:   number of phandles in the property with that index

## [◆ ](#gae253489146c61cb075f06192948275ff)DT\_INST\_NUM\_PINCTRLS\_BY\_NAME

| #define DT\_INST\_NUM\_PINCTRLS\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_NUM\_PINCTRLS\_BY\_NAME](#gaf96f1c82cc08008882f52e719ecd348c)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_NUM\_PINCTRLS\_BY\_NAME](#gaf96f1c82cc08008882f52e719ecd348c)

#define DT\_NUM\_PINCTRLS\_BY\_NAME(node\_id, name)

Like DT\_NUM\_PINCTRLS\_BY\_IDX(), but by name instead.

**Definition** pinctrl.h:212

Like [DT\_INST\_NUM\_PINCTRLS\_BY\_IDX()](#ga1de8198573428ec717733204d91f0391), but by name instead.

This is equivalent to [DT\_NUM\_PINCTRLS\_BY\_NAME(DT\_DRV\_INST(inst),
name)](#gaf96f1c82cc08008882f52e719ecd348c).

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of the pinctrl property |

Returns
:   number of phandles in the property with that name

## [◆ ](#ga3cd59afe76bc5d82b63ef21cae451f11)DT\_INST\_PINCTRL\_0

| #define DT\_INST\_PINCTRL\_0 | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_BY\_IDX](#ga24089220a93bc955700fba2c6170090e)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), 0, idx)

[DT\_PINCTRL\_BY\_IDX](#ga24089220a93bc955700fba2c6170090e)

#define DT\_PINCTRL\_BY\_IDX(node\_id, pc\_idx, idx)

Get a node identifier for a phandle in a pinctrl property by index.

**Definition** pinctrl.h:40

Get a node identifier from a pinctrl-0 property for a DT\_DRV\_COMPAT instance.

This is equivalent to:

```
DT_PINCTRL_BY_IDX(DT_DRV_INST(inst), 0, idx)
```

It is provided for convenience since pinctrl-0 is commonly used.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | index into the pinctrl-0 property |

Returns
:   node identifier for the phandle at index idx in the pinctrl-0 property of that instance

## [◆ ](#ga3388742fe3fb1f32a03566730890eaf0)DT\_INST\_PINCTRL\_BY\_IDX

| #define DT\_INST\_PINCTRL\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx*, |
|  |  |  | *idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_BY\_IDX](#ga24089220a93bc955700fba2c6170090e)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pc\_idx, idx)

Get a node identifier for a phandle in a pinctrl property by index for a DT\_DRV\_COMPAT instance.

This is equivalent to [DT\_PINCTRL\_BY\_IDX(DT\_DRV\_INST(inst), pc\_idx, idx)](#ga24089220a93bc955700fba2c6170090e).

Parameters
:   | inst | instance number |
    | --- | --- |
    | pc\_idx | index of the pinctrl property itself |
    | idx | index into the value of the pinctrl property |

Returns
:   node identifier for the phandle at index 'idx' in 'pinctrl-'pc\_idx''

## [◆ ](#ga4c171c27a91bd85e49b725bda6c05619)DT\_INST\_PINCTRL\_BY\_NAME

| #define DT\_INST\_PINCTRL\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_BY\_NAME](#ga1cd336f902738fd684f3d81b3fb6caae)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, idx)

[DT\_PINCTRL\_BY\_NAME](#ga1cd336f902738fd684f3d81b3fb6caae)

#define DT\_PINCTRL\_BY\_NAME(node\_id, name, idx)

Get a node identifier for a phandle inside a pinctrl node by name.

**Definition** pinctrl.h:81

Get a node identifier for a phandle inside a pinctrl node for a DT\_DRV\_COMPAT instance.

This is equivalent to [DT\_PINCTRL\_BY\_NAME(DT\_DRV\_INST(inst), name, idx)](#ga1cd336f902738fd684f3d81b3fb6caae).

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores pinctrl property name |
    | idx | index into the value of the named pinctrl property |

Returns
:   node identifier for the phandle at that index in the pinctrl property

## [◆ ](#ga53f17d0a6061cad7270544068f1cb003)DT\_INST\_PINCTRL\_HAS\_IDX

| #define DT\_INST\_PINCTRL\_HAS\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_HAS\_IDX](#ga5f1493cbfb7578b8fe3e37953aa9feaa)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pc\_idx)

[DT\_PINCTRL\_HAS\_IDX](#ga5f1493cbfb7578b8fe3e37953aa9feaa)

#define DT\_PINCTRL\_HAS\_IDX(node\_id, pc\_idx)

Test if a node has a pinctrl property with an index.

**Definition** pinctrl.h:268

Test if a DT\_DRV\_COMPAT instance has a pinctrl property with an index.

This is equivalent to [DT\_PINCTRL\_HAS\_IDX(DT\_DRV\_INST(inst), pc\_idx)](#ga5f1493cbfb7578b8fe3e37953aa9feaa).

Parameters
:   | inst | instance number |
    | --- | --- |
    | pc\_idx | index of a pinctrl property whose existence to check |

Returns
:   1 if the property exists, 0 otherwise

## [◆ ](#ga0e2af9dde68b57f6b1ffc86143fc2e40)DT\_INST\_PINCTRL\_HAS\_NAME

| #define DT\_INST\_PINCTRL\_HAS\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_HAS\_NAME](#gac9cd8112ad745f34eb6f6e4a13d7fd7e)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_PINCTRL\_HAS\_NAME](#gac9cd8112ad745f34eb6f6e4a13d7fd7e)

#define DT\_PINCTRL\_HAS\_NAME(node\_id, name)

Test if a node has a pinctrl property with a name.

**Definition** pinctrl.h:297

Test if a DT\_DRV\_COMPAT instance has a pinctrl property with a name.

This is equivalent to [DT\_PINCTRL\_HAS\_NAME(DT\_DRV\_INST(inst), name)](#gac9cd8112ad745f34eb6f6e4a13d7fd7e).

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores pinctrl property name to check |

Returns
:   1 if the property exists, 0 otherwise

## [◆ ](#ga80c3fb3defb7315877dc48db2932ef70)DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_TOKEN

| #define DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_TOKEN | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN](#ga47b0e5a18919f9f4829209cccbdeb430)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pc\_idx)

[DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN](#ga47b0e5a18919f9f4829209cccbdeb430)

#define DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(node\_id, pc\_idx)

Convert a pinctrl property index to its name as a token.

**Definition** pinctrl.h:138

Convert a pinctrl index to its name as an uppercased token.

This is equivalent to [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(DT\_DRV\_INST(inst), pc\_idx)](#ga47b0e5a18919f9f4829209cccbdeb430).

Parameters
:   | inst | instance number |
    | --- | --- |
    | pc\_idx | index of the pinctrl property itself |

Returns
:   name of the pin control property as a token

## [◆ ](#ga6d01324cecb6db502c46c42817c56bc9)DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN

| #define DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN](#gaa6eec236ccde612e88017b027f4ba711)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pc\_idx)

[DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN](#gaa6eec236ccde612e88017b027f4ba711)

#define DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(node\_id, pc\_idx)

Like DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(), but with an uppercased result.

**Definition** pinctrl.h:164

Convert a pinctrl index to its name as an uppercased token.

This is equivalent to [DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(DT\_DRV\_INST(inst), idx)](#gaa6eec236ccde612e88017b027f4ba711).

Parameters
:   | inst | instance number |
    | --- | --- |
    | pc\_idx | index of the pinctrl property itself |

Returns
:   name of the pin control property as an uppercase token

## [◆ ](#ga12c18d8d9724d98d121d8118b43686c3)DT\_INST\_PINCTRL\_NAME\_TO\_IDX

| #define DT\_INST\_PINCTRL\_NAME\_TO\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_NAME\_TO\_IDX](#ga36eb691efc2a4854ccb62555aeade785)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_PINCTRL\_NAME\_TO\_IDX](#ga36eb691efc2a4854ccb62555aeade785)

#define DT\_PINCTRL\_NAME\_TO\_IDX(node\_id, name)

Convert a pinctrl name to its corresponding index.

**Definition** pinctrl.h:104

Convert a pinctrl name to its corresponding index for a DT\_DRV\_COMPAT instance.

This is equivalent to [DT\_PINCTRL\_NAME\_TO\_IDX(DT\_DRV\_INST(inst),
name)](#ga36eb691efc2a4854ccb62555aeade785).

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of the pinctrl whose index to get |

Returns
:   integer literal for the index of the pinctrl property with that name

## [◆ ](#gaa2a012ce1d9ba026ee90001ae7f80381)DT\_NUM\_PINCTRL\_STATES

| #define DT\_NUM\_PINCTRL\_STATES | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_PINCTRL\_NUM)

Get the number of pinctrl properties in a node.

This expands to 0 if there are no pinctrl-i properties. Otherwise, it expands to the number of such properties.

Example devicetree fragment:

```
n1: node-1 {
        pinctrl-0 = <...>;
        pinctrl-1 = <...>;
};

n2: node-2 {
};
```

Example usage:

```
DT_NUM_PINCTRL_STATES(DT_NODELABEL(n1)) // 2
DT_NUM_PINCTRL_STATES(DT_NODELABEL(n2)) // 0
```

Parameters
:   | node\_id | node identifier; may or may not have any pinctrl properties |
    | --- | --- |

Returns
:   number of pinctrl properties in the node

## [◆ ](#ga6ae1bab2a71cb628405ec43d38705606)DT\_NUM\_PINCTRLS\_BY\_IDX

| #define DT\_NUM\_PINCTRLS\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_pinctrl\_, pc\_idx, \_LEN)

Get the number of phandles in a pinctrl property.

Example devicetree fragment:

```
n1: node-1 {
        pinctrl-0 = <&foo &bar>;
};

n2: node-2 {
        pinctrl-0 = <&baz>;
};
```

Example usage:

```
DT_NUM_PINCTRLS_BY_IDX(DT_NODELABEL(n1), 0) // 2
DT_NUM_PINCTRLS_BY_IDX(DT_NODELABEL(n2), 0) // 1
```

Parameters
:   | node\_id | node identifier with a pinctrl property |
    | --- | --- |
    | pc\_idx | index of the pinctrl property itself |

Returns
:   number of phandles in the property with that index

## [◆ ](#gaf96f1c82cc08008882f52e719ecd348c)DT\_NUM\_PINCTRLS\_BY\_NAME

| #define DT\_NUM\_PINCTRLS\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_NUM\_PINCTRLS\_BY\_IDX](#ga6ae1bab2a71cb628405ec43d38705606)(node\_id, [DT\_PINCTRL\_NAME\_TO\_IDX](#ga36eb691efc2a4854ccb62555aeade785)(node\_id, name))

Like [DT\_NUM\_PINCTRLS\_BY\_IDX()](#ga6ae1bab2a71cb628405ec43d38705606), but by name instead.

Example devicetree fragment:

```
n: node {
        pinctrl-0 = <&foo &bar>;
        pinctrl-1 = <&baz>
        pinctrl-names = "default", "sleep";
};
```

Example usage:

```
DT_NUM_PINCTRLS_BY_NAME(DT_NODELABEL(n), default) // 2
DT_NUM_PINCTRLS_BY_NAME(DT_NODELABEL(n), sleep)   // 1
```

Parameters
:   | node\_id | node identifier with a pinctrl property |
    | --- | --- |
    | name | lowercase-and-underscores name name of the pinctrl property |

Returns
:   number of phandles in the property with that name

## [◆ ](#gaf4e6f811ea4b1698c048d5dd8bfa604a)DT\_PINCTRL\_0

| #define DT\_PINCTRL\_0 | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[DT\_PINCTRL\_BY\_IDX](#ga24089220a93bc955700fba2c6170090e)(node\_id, 0, idx)

Get a node identifier from a pinctrl-0 property.

This is equivalent to:

```
DT_PINCTRL_BY_IDX(node_id, 0, idx)
```

It is provided for convenience since pinctrl-0 is commonly used.

Parameters
:   | node\_id | node with a pinctrl-0 property |
    | --- | --- |
    | idx | index into the pinctrl-0 property |

Returns
:   node identifier for the phandle at index idx in the pinctrl-0 property of that node

## [◆ ](#ga24089220a93bc955700fba2c6170090e)DT\_PINCTRL\_BY\_IDX

| #define DT\_PINCTRL\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx*, |
|  |  |  | *idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

DT\_CAT6(node\_id, \_P\_pinctrl\_, pc\_idx, \_IDX\_, idx, \_PH)

Get a node identifier for a phandle in a pinctrl property by index.

Example devicetree fragment:

```
n: node {
        pinctrl-0 = <&foo &bar>;
        pinctrl-1 = <&baz &blub>;
}
```

Example usage:

```
DT_PINCTRL_BY_IDX(DT_NODELABEL(n), 0, 1) // DT_NODELABEL(bar)
DT_PINCTRL_BY_IDX(DT_NODELABEL(n), 1, 0) // DT_NODELABEL(baz)
```

Parameters
:   | node\_id | node with a pinctrl-'pc\_idx' property |
    | --- | --- |
    | pc\_idx | index of the pinctrl property itself |
    | idx | index into the value of the pinctrl property |

Returns
:   node identifier for the phandle at index 'idx' in 'pinctrl-'pc\_idx''

## [◆ ](#ga1cd336f902738fd684f3d81b3fb6caae)DT\_PINCTRL\_BY\_NAME

| #define DT\_PINCTRL\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

DT\_CAT6(node\_id, \_PINCTRL\_NAME\_, name, \_IDX\_, idx, \_PH)

Get a node identifier for a phandle inside a pinctrl node by name.

Example devicetree fragment:

```
n: node {
        pinctrl-0 = <&foo &bar>;
        pinctrl-1 = <&baz &blub>;
        pinctrl-names = "default", "sleep";
};
```

Example usage:

```
DT_PINCTRL_BY_NAME(DT_NODELABEL(n), default, 1) // DT_NODELABEL(bar)
DT_PINCTRL_BY_NAME(DT_NODELABEL(n), sleep, 0) // DT_NODELABEL(baz)
```

Parameters
:   | node\_id | node with a named pinctrl property |
    | --- | --- |
    | name | lowercase-and-underscores pinctrl property name |
    | idx | index into the value of the named pinctrl property |

Returns
:   node identifier for the phandle at that index in the pinctrl property

## [◆ ](#ga5f1493cbfb7578b8fe3e37953aa9feaa)DT\_PINCTRL\_HAS\_IDX

| #define DT\_PINCTRL\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_PINCTRL\_IDX\_, pc\_idx, \_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Test if a node has a pinctrl property with an index.

This expands to 1 if the pinctrl-'idx' property exists. Otherwise, it expands to 0.

Example devicetree fragment:

```
n1: node-1 {
        pinctrl-0 = <...>;
        pinctrl-1 = <...>;
};

n2: node-2 {
};
```

Example usage:

```
DT_PINCTRL_HAS_IDX(DT_NODELABEL(n1), 0) // 1
DT_PINCTRL_HAS_IDX(DT_NODELABEL(n1), 1) // 1
DT_PINCTRL_HAS_IDX(DT_NODELABEL(n1), 2) // 0
DT_PINCTRL_HAS_IDX(DT_NODELABEL(n2), 0) // 0
```

Parameters
:   | node\_id | node identifier; may or may not have any pinctrl properties |
    | --- | --- |
    | pc\_idx | index of a pinctrl property whose existence to check |

Returns
:   1 if the property exists, 0 otherwise

## [◆ ](#gac9cd8112ad745f34eb6f6e4a13d7fd7e)DT\_PINCTRL\_HAS\_NAME

| #define DT\_PINCTRL\_HAS\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_PINCTRL\_NAME\_, name, \_EXISTS))

Test if a node has a pinctrl property with a name.

This expands to 1 if the named pinctrl property exists. Otherwise, it expands to 0.

Example devicetree fragment:

```
n1: node-1 {
        pinctrl-0 = <...>;
        pinctrl-names = "default";
};

n2: node-2 {
};
```

Example usage:

```
DT_PINCTRL_HAS_NAME(DT_NODELABEL(n1), default) // 1
DT_PINCTRL_HAS_NAME(DT_NODELABEL(n1), sleep)   // 0
DT_PINCTRL_HAS_NAME(DT_NODELABEL(n2), default) // 0
```

Parameters
:   | node\_id | node identifier; may or may not have any pinctrl properties |
    | --- | --- |
    | name | lowercase-and-underscores pinctrl property name to check |

Returns
:   1 if the property exists, 0 otherwise

## [◆ ](#ga47b0e5a18919f9f4829209cccbdeb430)DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN

| #define DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_PINCTRL\_IDX\_, pc\_idx, \_TOKEN)

Convert a pinctrl property index to its name as a token.

This allows you to get a pinctrl property's name, and "remove the
quotes" from it.

[DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN()](#ga47b0e5a18919f9f4829209cccbdeb430) can only be used if the node has a pinctrl-'pc\_idx' property and a pinctrl-names property element for that index. It is an error to use it in other circumstances.

Example devicetree fragment:

```
n: node {
        pinctrl-0 = <...>;
        pinctrl-1 = <...>;
        pinctrl-names = "default", "f.o.o2";
};
```

Example usage:

```
DT_PINCTRL_IDX_TO_NAME_TOKEN(DT_NODELABEL(n), 0) // default
DT_PINCTRL_IDX_TO_NAME_TOKEN(DT_NODELABEL(n), 1) // f_o_o2
```

The same caveats and restrictions that apply to [DT\_STRING\_TOKEN()](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54 "Get a string property's value as a token.")'s return value also apply here.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pc\_idx | index of a pinctrl property in that node |

Returns
:   name of the pinctrl property, as a token, without any quotes and with non-alphanumeric characters converted to underscores

## [◆ ](#gaa6eec236ccde612e88017b027f4ba711)DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN

| #define DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pc\_idx* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_PINCTRL\_IDX\_, pc\_idx, \_UPPER\_TOKEN)

Like [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN()](#ga47b0e5a18919f9f4829209cccbdeb430), but with an uppercased result.

This does the a similar conversion as [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(node\_id, pc\_idx)](#ga47b0e5a18919f9f4829209cccbdeb430). The only difference is that alphabetical characters in the result are uppercased.

Example devicetree fragment:

```
n: node {
        pinctrl-0 = <...>;
        pinctrl-1 = <...>;
        pinctrl-names = "default", "f.o.o2";
};
```

Example usage:

```
DT_PINCTRL_IDX_TO_NAME_TOKEN(DT_NODELABEL(n), 0) // DEFAULT
DT_PINCTRL_IDX_TO_NAME_TOKEN(DT_NODELABEL(n), 1) // F_O_O2
```

The same caveats and restrictions that apply to [DT\_STRING\_UPPER\_TOKEN()](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f "Like DT_STRING_TOKEN(), but uppercased.")'s return value also apply here.

## [◆ ](#ga36eb691efc2a4854ccb62555aeade785)DT\_PINCTRL\_NAME\_TO\_IDX

| #define DT\_PINCTRL\_NAME\_TO\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pinctrl.h](devicetree_2pinctrl_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_PINCTRL\_NAME\_, name, \_IDX)

Convert a pinctrl name to its corresponding index.

Example devicetree fragment:

```
n: node {
        pinctrl-0 = <&foo &bar>;
        pinctrl-1 = <&baz &blub>;
        pinctrl-names = "default", "sleep";
};
```

Example usage:

```
DT_PINCTRL_NAME_TO_IDX(DT_NODELABEL(n), default) // 0
DT_PINCTRL_NAME_TO_IDX(DT_NODELABEL(n), sleep)   // 1
```

Parameters
:   | node\_id | node identifier with a named pinctrl property |
    | --- | --- |
    | name | lowercase-and-underscores name name of the pinctrl whose index to get |

Returns
:   integer literal for the index of the pinctrl property with that name

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
