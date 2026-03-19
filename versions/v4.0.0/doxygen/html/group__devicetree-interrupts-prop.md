---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__devicetree-interrupts-prop.html
original_path: doxygen/html/group__devicetree-interrupts-prop.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

interrupts property

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_NUM\_IRQS](#ga2985e5d55d2d9dbbbe93ba855d5db320)(node\_id) |
|  | Get the number of interrupt sources for the node. |
| #define | [DT\_NUM\_NODELABELS](#ga7b63eb05db40d7b95ccb62a9fd1f4404)(node\_id) |
|  | Get the number of node labels that a node has. |
| #define | [DT\_IRQ\_LEVEL](#ga4b6c7ad21691c40047373e5073e740c9)(node\_id) |
|  | Get the interrupt level for the node. |
| #define | [DT\_IRQ\_HAS\_IDX](#ga238a290dc6cea9479104ff8f95de1c4c)(node\_id, idx) |
|  | Is `idx` a valid interrupt index? |
| #define | [DT\_IRQ\_HAS\_CELL\_AT\_IDX](#ga739ebdd4bd01d6b7beb75d915174206f)(node\_id, idx, cell) |
|  | Does an interrupts property have a named cell specifier at an index? |
| #define | [DT\_IRQ\_HAS\_CELL](#gab9c94ee39db7913598a755c6172fe036)(node\_id, cell) |
|  | Equivalent to [DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, 0, cell)](#ga739ebdd4bd01d6b7beb75d915174206f). |
| #define | [DT\_IRQ\_HAS\_NAME](#ga1c757ff5e4d15f1b3020b30f72c0dd5d)(node\_id, name) |
|  | Does an interrupts property have a named specifier value at an index? |
| #define | [DT\_IRQ\_BY\_IDX](#ga3779b2115eac60ab32adfc8d212e973f)(node\_id, idx, cell) |
|  | Get a value within an interrupt specifier at an index. |
| #define | [DT\_IRQ\_BY\_NAME](#ga904917c0a407343ef0185e9e6fe96812)(node\_id, name, cell) |
|  | Get a value within an interrupt specifier by name. |
| #define | [DT\_IRQ](#gabf60fbd528d300a26c0b4e66fe80a53f)(node\_id, cell) |
|  | Get an interrupt specifier's value Equivalent to [DT\_IRQ\_BY\_IDX(node\_id, 0, cell)](#ga3779b2115eac60ab32adfc8d212e973f). |
| #define | [DT\_IRQ\_INTC\_BY\_IDX](#ga061a34529fb2bbac9fe8615056d71ea4)(node\_id, idx) |
|  | Get an interrupt specifier's interrupt controller by index. |
| #define | [DT\_IRQ\_INTC\_BY\_NAME](#gabee933352a948bd824beccc00c13387d)(node\_id, name) |
|  | Get an interrupt specifier's interrupt controller by name. |
| #define | [DT\_IRQ\_INTC](#ga11d2680614de65fd8cb4a3909e93e9c9)(node\_id) |
|  | Get an interrupt specifier's interrupt controller. |
| #define | [DT\_IRQN\_BY\_IDX](#gaad6d6b27ea731a05a186a5dde8757698)(node\_id, idx) |
|  | Get the node's Zephyr interrupt number at index If. |
| #define | [DT\_IRQN](#ga5e00c208388736ce9b5bc0088a77cd95)(node\_id) |
|  | Get a node's (only) irq number. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gabf60fbd528d300a26c0b4e66fe80a53f)DT\_IRQ

| #define DT\_IRQ | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_BY\_IDX](#ga3779b2115eac60ab32adfc8d212e973f)(node\_id, 0, cell)

[DT\_IRQ\_BY\_IDX](#ga3779b2115eac60ab32adfc8d212e973f)

#define DT\_IRQ\_BY\_IDX(node\_id, idx, cell)

Get a value within an interrupt specifier at an index.

**Definition** devicetree.h:2650

Get an interrupt specifier's value Equivalent to [DT\_IRQ\_BY\_IDX(node\_id, 0, cell)](#ga3779b2115eac60ab32adfc8d212e973f).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | cell | cell name specifier |

Returns
:   the named value at that index

## [◆ ](#ga3779b2115eac60ab32adfc8d212e973f)DT\_IRQ\_BY\_IDX

| #define DT\_IRQ\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT5(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell)

Get a value within an interrupt specifier at an index.

It might help to read the argument order as being similar to "node->interrupts[index].cell".

This can be used to get information about an individual interrupt when a device generates more than one.

Example devicetree fragment:

my-serial: serial@abcd1234 {

interrupts = < 33 0 >, < 34 1 >;

};

Assuming the node's interrupt domain has "#interrupt-cells = <2>;" and the individual cells in each interrupt specifier are named "irq" and "priority" by the node's binding, here are some examples:

```
#define SERIAL DT_NODELABEL(my_serial)

Example usage                       Value
-------------                       -----
DT_IRQ_BY_IDX(SERIAL, 0, irq)          33
DT_IRQ_BY_IDX(SERIAL, 0, priority)      0
DT_IRQ_BY_IDX(SERIAL, 1, irq,          34
DT_IRQ_BY_IDX(SERIAL, 1, priority)      1
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into the interrupt specifier array |
    | cell | cell name specifier |

Returns
:   the named value at the specifier given by the index

## [◆ ](#ga904917c0a407343ef0185e9e6fe96812)DT\_IRQ\_BY\_NAME

| #define DT\_IRQ\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT5(node\_id, \_IRQ\_NAME\_, name, \_VAL\_, cell)

Get a value within an interrupt specifier by name.

It might help to read the argument order as being similar to node->interrupts.name.cell.

This can be used to get information about an individual interrupt when a device generates more than one, if the bindings give each interrupt specifier a name.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores interrupt specifier name |
    | cell | cell name specifier |

Returns
:   the named value at the specifier given by the index

## [◆ ](#gab9c94ee39db7913598a755c6172fe036)DT\_IRQ\_HAS\_CELL

| #define DT\_IRQ\_HAS\_CELL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_HAS\_CELL\_AT\_IDX](#ga739ebdd4bd01d6b7beb75d915174206f)(node\_id, 0, cell)

[DT\_IRQ\_HAS\_CELL\_AT\_IDX](#ga739ebdd4bd01d6b7beb75d915174206f)

#define DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, idx, cell)

Does an interrupts property have a named cell specifier at an index?

**Definition** devicetree.h:2591

Equivalent to [DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, 0, cell)](#ga739ebdd4bd01d6b7beb75d915174206f).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | cell | named cell value whose existence to check |

Returns
:   1 if the named cell exists in the interrupt specifier at index 0 0 otherwise.

## [◆ ](#ga739ebdd4bd01d6b7beb75d915174206f)DT\_IRQ\_HAS\_CELL\_AT\_IDX

| #define DT\_IRQ\_HAS\_CELL\_AT\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT6(node\_id, \_IRQ\_IDX\_, idx, \_VAL\_, cell, \_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

Does an interrupts property have a named cell specifier at an index?

If this returns 1, then [DT\_IRQ\_BY\_IDX(node\_id, idx, cell)](#ga3779b2115eac60ab32adfc8d212e973f) is valid. If it returns 0, it is an error to use that macro.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index to check |
    | cell | named cell value whose existence to check |

Returns
:   1 if the named cell exists in the interrupt specifier at index idx 0 otherwise.

## [◆ ](#ga238a290dc6cea9479104ff8f95de1c4c)DT\_IRQ\_HAS\_IDX

| #define DT\_IRQ\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_EXISTS))

Is `idx` a valid interrupt index?

If this returns 1, then [DT\_IRQ\_BY\_IDX(node\_id, idx)](#ga3779b2115eac60ab32adfc8d212e973f) is valid. If it returns 0, it is an error to use that macro with this index.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index to check |

Returns
:   1 if the idx is valid for the interrupt property 0 otherwise.

## [◆ ](#ga1c757ff5e4d15f1b3020b30f72c0dd5d)DT\_IRQ\_HAS\_NAME

| #define DT\_IRQ\_HAS\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_VAL\_irq\_EXISTS))

Does an interrupts property have a named specifier value at an index?

If this returns 1, then [DT\_IRQ\_BY\_NAME(node\_id, name, cell)](#ga904917c0a407343ef0185e9e6fe96812) is valid. If it returns 0, it is an error to use that macro.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores interrupt specifier name |

Returns
:   1 if "name" is a valid named specifier 0 otherwise.

## [◆ ](#ga11d2680614de65fd8cb4a3909e93e9c9)DT\_IRQ\_INTC

| #define DT\_IRQ\_INTC | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_INTC\_BY\_IDX](#ga061a34529fb2bbac9fe8615056d71ea4)(node\_id, 0)

[DT\_IRQ\_INTC\_BY\_IDX](#ga061a34529fb2bbac9fe8615056d71ea4)

#define DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx)

Get an interrupt specifier's interrupt controller by index.

**Definition** devicetree.h:2722

Get an interrupt specifier's interrupt controller.

Note
:   Equivalent to [DT\_IRQ\_INTC\_BY\_IDX(node\_id, 0)](#ga061a34529fb2bbac9fe8615056d71ea4)

gpio0: gpio0 {

interrupt-controller;

#interrupt-cells = <2>;

};

foo: foo {

interrupt-parent = <&gpio0>;

interrupts = <1 1>;

};

bar: bar {

interrupts-extended = <&gpio0 3 3>;

};

pic0: pic0 {

interrupt-controller;

#interrupt-cells = <1>;

qux: qux {

interrupts = <5>;

};

};

Example usage:

```
DT_IRQ_INTC(DT_NODELABEL(foo)) // &gpio0
DT_IRQ_INTC(DT_NODELABEL(bar)) // &gpio0
DT_IRQ_INTC(DT_NODELABEL(qux)) // &pic0
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   node\_id of interrupt specifier's interrupt controller

See also
:   [DT\_IRQ\_INTC\_BY\_IDX()](#ga061a34529fb2bbac9fe8615056d71ea4)

## [◆ ](#ga061a34529fb2bbac9fe8615056d71ea4)DT\_IRQ\_INTC\_BY\_IDX

| #define DT\_IRQ\_INTC\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_IRQ\_IDX\_, idx, \_CONTROLLER)

Get an interrupt specifier's interrupt controller by index.

gpio0: gpio0 {

interrupt-controller;

#interrupt-cells = <2>;

};

foo: foo {

interrupt-parent = <&gpio0>;

interrupts = <1 1>, <2 2>;

};

bar: bar {

interrupts-extended = <&gpio0 3 3>, <&pic0 4>;

};

pic0: pic0 {

interrupt-controller;

#interrupt-cells = <1>;

qux: qux {

interrupts = <5>, <6>;

interrupt-names = "int1", "int2";

};

};

Example usage:

```
DT_IRQ_INTC_BY_IDX(DT_NODELABEL(foo), 0) // &gpio0
DT_IRQ_INTC_BY_IDX(DT_NODELABEL(foo), 1) // &gpio0
DT_IRQ_INTC_BY_IDX(DT_NODELABEL(bar), 0) // &gpio0
DT_IRQ_INTC_BY_IDX(DT_NODELABEL(bar), 1) // &pic0
DT_IRQ_INTC_BY_IDX(DT_NODELABEL(qux), 0) // &pic0
DT_IRQ_INTC_BY_IDX(DT_NODELABEL(qux), 1) // &pic0
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | interrupt specifier's index |

Returns
:   node\_id of interrupt specifier's interrupt controller

## [◆ ](#gabee933352a948bd824beccc00c13387d)DT\_IRQ\_INTC\_BY\_NAME

| #define DT\_IRQ\_INTC\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_IRQ\_NAME\_, name, \_CONTROLLER)

Get an interrupt specifier's interrupt controller by name.

gpio0: gpio0 {

interrupt-controller;

#interrupt-cells = <2>;

};

foo: foo {

interrupt-parent = <&gpio0>;

interrupts = <1 1>, <2 2>;

interrupt-names = "int1", "int2";

};

bar: bar {

interrupts-extended = <&gpio0 3 3>, <&pic0 4>;

interrupt-names = "int1", "int2";

};

pic0: pic0 {

interrupt-controller;

#interrupt-cells = <1>;

qux: qux {

interrupts = <5>, <6>;

interrupt-names = "int1", "int2";

};

};

Example usage:

```
DT_IRQ_INTC_BY_NAME(DT_NODELABEL(foo), int1) // &gpio0
DT_IRQ_INTC_BY_NAME(DT_NODELABEL(foo), int2) // &gpio0
DT_IRQ_INTC_BY_NAME(DT_NODELABEL(bar), int1) // &gpio0
DT_IRQ_INTC_BY_NAME(DT_NODELABEL(bar), int2) // &pic0
DT_IRQ_INTC_BY_NAME(DT_NODELABEL(qux), int1) // &pic0
DT_IRQ_INTC_BY_NAME(DT_NODELABEL(qux), int2) // &pic0
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | interrupt specifier's name |

Returns
:   node\_id of interrupt specifier's interrupt controller

## [◆ ](#ga4b6c7ad21691c40047373e5073e740c9)DT\_IRQ\_LEVEL

| #define DT\_IRQ\_LEVEL | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_IRQ\_LEVEL)

Get the interrupt level for the node.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   interrupt level

## [◆ ](#ga5e00c208388736ce9b5bc0088a77cd95)DT\_IRQN

| #define DT\_IRQN | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQN\_BY\_IDX](#gaad6d6b27ea731a05a186a5dde8757698)(node\_id, 0)

[DT\_IRQN\_BY\_IDX](#gaad6d6b27ea731a05a186a5dde8757698)

#define DT\_IRQN\_BY\_IDX(node\_id, idx)

Get the node's Zephyr interrupt number at index If.

**Definition** devicetree.h:2851

Get a node's (only) irq number.

Equivalent to [DT\_IRQ(node\_id, irq)](#gabf60fbd528d300a26c0b4e66fe80a53f). This is provided as a convenience for the common case where a node generates exactly one interrupt, and the IRQ number is in a cell named irq.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the interrupt number for the node's only interrupt

## [◆ ](#gaad6d6b27ea731a05a186a5dde8757698)DT\_IRQN\_BY\_IDX

| #define DT\_IRQN\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_MULTI\_LEVEL\_INTERRUPTS), \

(DT\_MULTI\_LEVEL\_IRQN\_INTERNAL(node\_id, idx)), \

([DT\_IRQ\_BY\_IDX](#ga3779b2115eac60ab32adfc8d212e973f)(node\_id, idx, irq)))

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

Get the node's Zephyr interrupt number at index If.

```
CONFIG_MULTI_LEVEL_INTERRUPTS
```

is enabled, the interrupt number at index will be multi-level encoded

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into the interrupt specifier array |

Returns
:   the Zephyr interrupt number

## [◆ ](#ga2985e5d55d2d9dbbbe93ba855d5db320)DT\_NUM\_IRQS

| #define DT\_NUM\_IRQS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_IRQ\_NUM)

Get the number of interrupt sources for the node.

Use this instead of [DT\_PROP\_LEN(node\_id, interrupts)](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6 "Get a property's logical length.").

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   Number of interrupt specifiers in the node's "interrupts" property.

## [◆ ](#ga7b63eb05db40d7b95ccb62a9fd1f4404)DT\_NUM\_NODELABELS

| #define DT\_NUM\_NODELABELS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_NODELABEL\_NUM)

Get the number of node labels that a node has.

Example devicetree fragment:

/ {

foo {};

bar: bar@1000 {};

baz: baz2: baz@2000 {};

};

Example usage:

[DT\_NUM\_NODELABELS](#ga7b63eb05db40d7b95ccb62a9fd1f4404)([DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)(foo)) // 0

[DT\_NUM\_NODELABELS](#ga7b63eb05db40d7b95ccb62a9fd1f4404)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(bar)) // 1

[DT\_NUM\_NODELABELS](#ga7b63eb05db40d7b95ccb62a9fd1f4404)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(baz)) // 2

[DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)

#define DT\_PATH(...)

Get a node identifier for a devicetree path.

**Definition** devicetree.h:140

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[DT\_NUM\_NODELABELS](#ga7b63eb05db40d7b95ccb62a9fd1f4404)

#define DT\_NUM\_NODELABELS(node\_id)

Get the number of node labels that a node has.

**Definition** devicetree.h:2558

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   number of node labels that the node has

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
