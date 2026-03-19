---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__devicetree-mbox.html
original_path: doxygen/html/group__devicetree-mbox.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree MBOX API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_MBOX\_CTLR\_BY\_NAME](#gabb96e9b997d99ed54d167d592d623ff7)(node\_id, name) |
|  | Get the node identifier for the MBOX controller from a mboxes property by name. |
| #define | [DT\_MBOX\_CHANNEL\_BY\_NAME](#ga4ea23945e3aacae6a8daacb4c24c88e4)(node\_id, name) |
|  | Get a MBOX channel value by name. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga4ea23945e3aacae6a8daacb4c24c88e4)DT\_MBOX\_CHANNEL\_BY\_NAME

| #define DT\_MBOX\_CHANNEL\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[mbox.h](devicetree_2mbox_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME\_OR](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)(node\_id, mboxes, name, channel, 0)

[DT\_PHA\_BY\_NAME\_OR](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)

#define DT\_PHA\_BY\_NAME\_OR(node\_id, pha, name, cell, default\_value)

Like DT\_PHA\_BY\_NAME(), but with a fallback to default\_value.

**Definition** devicetree.h:1655

Get a MBOX channel value by name.

Example devicetree fragment:

```
mbox1: mbox@... {
        #mbox-cells = <1>;
};

n: node {
    mboxes = <&mbox1 1>,
             <&mbox1 6>;
    mbox-names = "tx", "rx";
};
```

Bindings fragment for the mbox compatible:

```
mbox-cells:
  - channel
```

Example usage:

```
DT_MBOX_CHANNEL_BY_NAME(DT_NODELABEL(n), tx) // 1
DT_MBOX_CHANNEL_BY_NAME(DT_NODELABEL(n), rx) // 6
```

Parameters
:   | node\_id | node identifier for a node with a mboxes property |
    | --- | --- |
    | name | lowercase-and-underscores name of a mboxes element as defined by the node's mbox-names property |

Returns
:   the channel value in the specifier at the named element or 0 if no channels are supported

See also
:   [DT\_PHA\_BY\_NAME\_OR()](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401 "Like DT_PHA_BY_NAME(), but with a fallback to default_value.")

## [◆ ](#gabb96e9b997d99ed54d167d592d623ff7)DT\_MBOX\_CTLR\_BY\_NAME

| #define DT\_MBOX\_CTLR\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[mbox.h](devicetree_2mbox_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, mboxes, name)

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1705

Get the node identifier for the MBOX controller from a mboxes property by name.

Example devicetree fragment:

```
mbox1: mbox-controller@... { ... };

n: node {
        mboxes = <&mbox1 8>,
                 <&mbox1 9>;
        mbox-names = "tx", "rx";
};
```

Example usage:

```
DT_MBOX_CTLR_BY_NAME(DT_NODELABEL(n), tx) // DT_NODELABEL(mbox1)
DT_MBOX_CTLR_BY_NAME(DT_NODELABEL(n), rx) // DT_NODELABEL(mbox1)
```

Parameters
:   | node\_id | node identifier for a node with a mboxes property |
    | --- | --- |
    | name | lowercase-and-underscores name of a mboxes element as defined by the node's mbox-names property |

Returns
:   the node identifier for the MBOX controller in the named element

See also
:   [DT\_PHANDLE\_BY\_NAME()](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd "Get a phandle's node identifier from a phandle array by name.")

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
