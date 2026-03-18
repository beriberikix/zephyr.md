---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__devicetree-dep-ord.html
original_path: doxygen/html/group__devicetree-dep-ord.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Dependency tracking

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_DEP\_ORD](#ga5b96dccfd349dd0ddba1812aa942c1bd)(node\_id) |
|  | Get a node's dependency ordinal. |
| #define | [DT\_DEP\_ORD\_STR\_SORTABLE](#ga6c31d58b47d826f1a1de1e5d0044e2f7)(node\_id) |
|  | Get a node's dependency ordinal in string sortable form. |
| #define | [DT\_REQUIRES\_DEP\_ORDS](#ga22dd1b0c89eb5ddfbfdd1e723d44f509)(node\_id) |
|  | Get a list of dependency ordinals of a node's direct dependencies. |
| #define | [DT\_SUPPORTS\_DEP\_ORDS](#ga3f559e9a787792685ed08be124b374ae)(node\_id) |
|  | Get a list of dependency ordinals of what depends directly on a node. |
| #define | [DT\_INST\_DEP\_ORD](#ga9c5e6f36c6e7a250368177a9f0713f86)(inst) |
|  | Get a DT\_DRV\_COMPAT instance's dependency ordinal. |
| #define | [DT\_INST\_REQUIRES\_DEP\_ORDS](#gac7d43a7916bdc8c46fafeee0213e538c)(inst) |
|  | Get a list of dependency ordinals of a DT\_DRV\_COMPAT instance's direct dependencies. |
| #define | [DT\_INST\_SUPPORTS\_DEP\_ORDS](#ga027cc1361d1e059dde039926980e26fa)(inst) |
|  | Get a list of dependency ordinals of what depends directly on a DT\_DRV\_COMPAT instance. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga5b96dccfd349dd0ddba1812aa942c1bd)DT\_DEP\_ORD

| #define DT\_DEP\_ORD | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ordinals.h](ordinals_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_ORD)

Get a node's dependency ordinal.

Parameters
:   | node\_id | Node identifier |
    | --- | --- |

Returns
:   the node's dependency ordinal as an integer literal

## [◆ ](#ga6c31d58b47d826f1a1de1e5d0044e2f7)DT\_DEP\_ORD\_STR\_SORTABLE

| #define DT\_DEP\_ORD\_STR\_SORTABLE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ordinals.h](ordinals_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_ORD\_STR\_SORTABLE)

Get a node's dependency ordinal in string sortable form.

Parameters
:   | node\_id | Node identifier |
    | --- | --- |

Returns
:   the node's dependency ordinal as a zero-padded integer literal

## [◆ ](#ga9c5e6f36c6e7a250368177a9f0713f86)DT\_INST\_DEP\_ORD

| #define DT\_INST\_DEP\_ORD | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ordinals.h](ordinals_8h.md)>`

**Value:**

[DT\_DEP\_ORD](#ga5b96dccfd349dd0ddba1812aa942c1bd)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DEP\_ORD](#ga5b96dccfd349dd0ddba1812aa942c1bd)

#define DT\_DEP\_ORD(node\_id)

Get a node's dependency ordinal.

**Definition** ordinals.h:25

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

Get a DT\_DRV\_COMPAT instance's dependency ordinal.

Equivalent to [DT\_DEP\_ORD(DT\_DRV\_INST(inst))](#ga5b96dccfd349dd0ddba1812aa942c1bd).

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   The instance's dependency ordinal

## [◆ ](#gac7d43a7916bdc8c46fafeee0213e538c)DT\_INST\_REQUIRES\_DEP\_ORDS

| #define DT\_INST\_REQUIRES\_DEP\_ORDS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ordinals.h](ordinals_8h.md)>`

**Value:**

[DT\_REQUIRES\_DEP\_ORDS](#ga22dd1b0c89eb5ddfbfdd1e723d44f509)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_REQUIRES\_DEP\_ORDS](#ga22dd1b0c89eb5ddfbfdd1e723d44f509)

#define DT\_REQUIRES\_DEP\_ORDS(node\_id)

Get a list of dependency ordinals of a node's direct dependencies.

**Definition** ordinals.h:51

Get a list of dependency ordinals of a DT\_DRV\_COMPAT instance's direct dependencies.

Equivalent to [DT\_REQUIRES\_DEP\_ORDS(DT\_DRV\_INST(inst))](#ga22dd1b0c89eb5ddfbfdd1e723d44f509).

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   a list of dependency ordinals for the nodes the instance depends on directly

## [◆ ](#ga027cc1361d1e059dde039926980e26fa)DT\_INST\_SUPPORTS\_DEP\_ORDS

| #define DT\_INST\_SUPPORTS\_DEP\_ORDS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ordinals.h](ordinals_8h.md)>`

**Value:**

[DT\_SUPPORTS\_DEP\_ORDS](#ga3f559e9a787792685ed08be124b374ae)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_SUPPORTS\_DEP\_ORDS](#ga3f559e9a787792685ed08be124b374ae)

#define DT\_SUPPORTS\_DEP\_ORDS(node\_id)

Get a list of dependency ordinals of what depends directly on a node.

**Definition** ordinals.h:68

Get a list of dependency ordinals of what depends directly on a DT\_DRV\_COMPAT instance.

Equivalent to [DT\_SUPPORTS\_DEP\_ORDS(DT\_DRV\_INST(inst))](#ga3f559e9a787792685ed08be124b374ae).

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   a list of node identifiers for the nodes that depend directly on the instance

## [◆ ](#ga22dd1b0c89eb5ddfbfdd1e723d44f509)DT\_REQUIRES\_DEP\_ORDS

| #define DT\_REQUIRES\_DEP\_ORDS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ordinals.h](ordinals_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_REQUIRES\_ORDS)

Get a list of dependency ordinals of a node's direct dependencies.

There is a comma after each ordinal in the expansion, **including** the last one:

```
DT_REQUIRES_DEP_ORDS(my_node) // required_ord_1, ..., required_ord_n,
```

The one case [DT\_REQUIRES\_DEP\_ORDS()](#ga22dd1b0c89eb5ddfbfdd1e723d44f509) expands to nothing is when given the root node identifier `DT_ROOT` as argument. The root has no direct dependencies; every other node at least depends on its parent.

Parameters
:   | node\_id | Node identifier |
    | --- | --- |

Returns
:   a list of dependency ordinals, with each ordinal followed by a comma (,), or an empty expansion

## [◆ ](#ga3f559e9a787792685ed08be124b374ae)DT\_SUPPORTS\_DEP\_ORDS

| #define DT\_SUPPORTS\_DEP\_ORDS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ordinals.h](ordinals_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_SUPPORTS\_ORDS)

Get a list of dependency ordinals of what depends directly on a node.

There is a comma after each ordinal in the expansion, **including** the last one:

```
DT_SUPPORTS_DEP_ORDS(my_node) // supported_ord_1, ..., supported_ord_n,
```

[DT\_SUPPORTS\_DEP\_ORDS()](#ga3f559e9a787792685ed08be124b374ae) may expand to nothing. This happens when `node_id` refers to a leaf node that nothing else depends on.

Parameters
:   | node\_id | Node identifier |
    | --- | --- |

Returns
:   a list of dependency ordinals, with each ordinal followed by a comma (,), or an empty expansion

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
