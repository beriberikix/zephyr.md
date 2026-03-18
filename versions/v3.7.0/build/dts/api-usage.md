---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api-usage.html
original_path: build/dts/api-usage.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Devicetree access from C/C++

This guide describes Zephyr’s `<zephyr/devicetree.h>` API for reading the
devicetree from C source files. It assumes you’re familiar with the concepts in
[Introduction to devicetree](intro.md#devicetree-intro) and [Devicetree bindings](bindings.md#dt-bindings). See [Devicetree Reference](index.md#dt-reference) for
reference material.

## A note for Linux developers

Linux developers familiar with devicetree should be warned that the API
described here differs significantly from how devicetree is used on Linux.

Instead of generating a C header with all the devicetree data which is then
abstracted behind a macro API, the Linux kernel would instead read the
devicetree data structure in its binary form. The binary representation is
parsed at runtime, for example to load and initialize device drivers.

Zephyr does not work this way because the size of the devicetree binary and
associated handling code would be too large to fit comfortably on the
relatively constrained devices Zephyr supports.

## Node identifiers

To get information about a particular devicetree node, you need a *node
identifier* for it. This is a just a C macro that refers to the node.

These are the main ways to get a node identifier:

By path
:   Use [`DT_PATH()`](api/api.md#c.DT_PATH "DT_PATH") along with the node’s full path in the devicetree,
    starting from the root node. This is mostly useful if you happen to know the
    exact node you’re looking for.

By node label
:   Use [`DT_NODELABEL()`](api/api.md#c.DT_NODELABEL "DT_NODELABEL") to get a node identifier from a [node
    label](intro-syntax-structure.md#dt-node-labels). Node labels are often provided by SoC `.dtsi`
    files to give nodes names that match the SoC datasheet, like `i2c1`,
    `spi2`, etc.

By alias
:   Use [`DT_ALIAS()`](api/api.md#c.DT_ALIAS "DT_ALIAS") to get a node identifier for a property of the
    special `/aliases` node. This is sometimes done by applications (like
    [Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API."), which uses the `led0` alias) that need to
    refer to *some* device of a particular type (“the board’s user LED”) but
    don’t care which one is used.

By instance number
:   This is done primarily by device drivers, as instance numbers are a way to
    refer to individual nodes based on a matching compatible. Get these with
    [`DT_INST()`](api/api.md#c.DT_INST "DT_INST"), but be careful doing so. See below.

By chosen node
:   Use [`DT_CHOSEN()`](api/api.md#c.DT_CHOSEN "DT_CHOSEN") to get a node identifier for `/chosen` node
    properties.

By parent/child
:   Use [`DT_PARENT()`](api/api.md#c.DT_PARENT "DT_PARENT") and [`DT_CHILD()`](api/api.md#c.DT_CHILD "DT_CHILD") to get a node identifier
    for a parent or child node, starting from a node identifier you already have.

Two node identifiers which refer to the same node are identical and can be used
interchangeably.

Here’s a DTS fragment for some imaginary hardware we’ll return to throughout
this file for examples:

```devicetree
/dts-v1/;

/ {

	aliases {
		sensor-controller = &i2c1;
	};

	soc {
		i2c1: i2c@40002000 {
			compatible = "vnd,soc-i2c";
			label = "I2C_1";
			reg = <0x40002000 0x1000>;
			status = "okay";
			clock-frequency = < 100000 >;
		};
	};
};
```

Here are a few ways to get node identifiers for the `i2c@40002000` node:

- `DT_PATH(soc, i2c_40002000)`
- `DT_NODELABEL(i2c1)`
- `DT_ALIAS(sensor_controller)`
- `DT_INST(x, vnd_soc_i2c)` for some unknown number `x`. See the
  [`DT_INST()`](api/api.md#c.DT_INST "DT_INST") documentation for details.

Important

Non-alphanumeric characters like dash (`-`) and the at sign (`@`) in
devicetree names are converted to underscores (`_`). The names in a DTS
are also converted to lowercase.

## Node identifiers are not values

There is no way to store one in a variable. You cannot write:

```c
/* These will give you compiler errors: */

void *i2c_0 = DT_INST(0, vnd_soc_i2c);
unsigned int i2c_1 = DT_INST(1, vnd_soc_i2c);
long my_i2c = DT_NODELABEL(i2c1);
```

If you want something short to save typing, use C macros:

```c
/* Use something like this instead: */

#define MY_I2C DT_NODELABEL(i2c1)

#define INST(i) DT_INST(i, vnd_soc_i2c)
#define I2C_0 INST(0)
#define I2C_1 INST(1)
```

## Property access

The right API to use to read property values depends on the node and property.

- [Checking properties and values](#dt-checking-property-exists)
- [Simple properties](#simple-properties)
- [reg properties](#reg-properties)
- [interrupts properties](#interrupts-properties)
- [phandle properties](#phandle-properties)

### Checking properties and values

You can use [`DT_NODE_HAS_PROP()`](api/api.md#c.DT_NODE_HAS_PROP "DT_NODE_HAS_PROP") to check if a node has a property. For
the [example devicetree](#dt-node-main-ex) above:

```c
DT_NODE_HAS_PROP(DT_NODELABEL(i2c1), clock_frequency)  /* expands to 1 */
DT_NODE_HAS_PROP(DT_NODELABEL(i2c1), not_a_property)   /* expands to 0 */
```

### Simple properties

Use `DT_PROP(node_id, property)` to read basic integer, boolean, string,
numeric array, and string array properties.

For example, to read the `clock-frequency` property’s value in the
[above example](#dt-node-main-ex):

```c
DT_PROP(DT_PATH(soc, i2c_40002000), clock_frequency)  /* This is 100000, */
DT_PROP(DT_NODELABEL(i2c1), clock_frequency)          /* and so is this, */
DT_PROP(DT_ALIAS(sensor_controller), clock_frequency) /* and this. */
```

Important

The DTS property `clock-frequency` is spelled `clock_frequency` in C.
That is, properties also need special characters converted to underscores.
Their names are also forced to lowercase.

Properties with `string` and `boolean` types work the exact same way. The
`DT_PROP()` macro expands to a string literal in the case of strings, and the
number 0 or 1 in the case of booleans. For example:

```c
#define I2C1 DT_NODELABEL(i2c1)

DT_PROP(I2C1, status)  /* expands to the string literal "okay" */
```

Note

Don’t use DT\_NODE\_HAS\_PROP() for boolean properties. Use DT\_PROP() instead
as shown above. It will expand to either 0 or 1 depending on if the property
is present or absent.

Properties with type `array`, `uint8-array`, and `string-array` work
similarly, except `DT_PROP()` expands to an array initializer in these cases.
Here is an example devicetree fragment:

```devicetree
foo: foo@1234 {
        a = <1000 2000 3000>; /* array */
        b = [aa bb cc dd];    /* uint8-array */
        c = "bar", "baz";     /* string-array */
};
```

Its properties can be accessed like this:

```c
#define FOO DT_NODELABEL(foo)

int a[] = DT_PROP(FOO, a);           /* {1000, 2000, 3000} */
unsigned char b[] = DT_PROP(FOO, b); /* {0xaa, 0xbb, 0xcc, 0xdd} */
char* c[] = DT_PROP(FOO, c);         /* {"foo", "bar"} */
```

You can use [`DT_PROP_LEN()`](api/api.md#c.DT_PROP_LEN "DT_PROP_LEN") to get logical array lengths in number of
elements.

```c
size_t a_len = DT_PROP_LEN(FOO, a); /* 3 */
size_t b_len = DT_PROP_LEN(FOO, b); /* 4 */
size_t c_len = DT_PROP_LEN(FOO, c); /* 2 */
```

`DT_PROP_LEN()` cannot be used with the special `reg` or `interrupts`
properties. These have alternative macros which are described next.

### reg properties

See [Important properties](intro-syntax-structure.md#dt-important-props) for an introduction to `reg`.

Given a node identifier `node_id`, `DT_NUM_REGS(node_id)` is the
total number of register blocks in the node’s `reg` property.

You **cannot** read register block addresses and lengths with `DT_PROP(node,
reg)`. Instead, if a node only has one register block, use
[`DT_REG_ADDR()`](api/api.md#c.DT_REG_ADDR "DT_REG_ADDR") or [`DT_REG_SIZE()`](api/api.md#c.DT_REG_SIZE "DT_REG_SIZE"):

- `DT_REG_ADDR(node_id)`: the given node’s register block address
- `DT_REG_SIZE(node_id)`: its size

Use [`DT_REG_ADDR_BY_IDX()`](api/api.md#c.DT_REG_ADDR_BY_IDX "DT_REG_ADDR_BY_IDX") or [`DT_REG_SIZE_BY_IDX()`](api/api.md#c.DT_REG_SIZE_BY_IDX "DT_REG_SIZE_BY_IDX") instead if the
node has multiple register blocks:

- `DT_REG_ADDR_BY_IDX(node_id, idx)`: address of register block at index
  `idx`
- `DT_REG_SIZE_BY_IDX(node_id, idx)`: size of block at index `idx`

The `idx` argument to these must be an integer literal or a macro that
expands to one without requiring any arithmetic. In particular, `idx` cannot
be a variable. This won’t work:

```c
/* This will cause a compiler error. */

for (size_t i = 0; i < DT_NUM_REGS(node_id); i++) {
        size_t addr = DT_REG_ADDR_BY_IDX(node_id, i);
}
```

### interrupts properties

See [Important properties](intro-syntax-structure.md#dt-important-props) for a brief introduction to `interrupts`.

Given a node identifier `node_id`, `DT_NUM_IRQS(node_id)` is the total
number of interrupt specifiers in the node’s `interrupts` property.

The most general purpose API macro for accessing these is
[`DT_IRQ_BY_IDX()`](api/api.md#c.DT_IRQ_BY_IDX "DT_IRQ_BY_IDX"):

```c
DT_IRQ_BY_IDX(node_id, idx, val)
```

Here, `idx` is the logical index into the `interrupts` array, i.e. it is
the index of an individual interrupt specifier in the property. The `val`
argument is the name of a cell within the interrupt specifier. To use this
macro, check the bindings file for the node you are interested in to find the
`val` names.

Most Zephyr devicetree bindings have a cell named `irq`, which is the
interrupt number. You can use [`DT_IRQN()`](api/api.md#c.DT_IRQN "DT_IRQN") as a convenient way to get a
processed view of this value.

Warning

Here, “processed” reflects Zephyr’s devicetree [Scripts and tools](intro-input-output.md#dt-scripts), which
change the `irq` number in [zephyr.dts](intro-input-output.md#devicetree-in-out-files) to
handle hardware constraints on some SoCs and in accordance with Zephyr’s
multilevel interrupt numbering.

This is currently not very well documented, and you’ll need to read the
scripts’ source code and existing drivers for more details if you are writing
a device driver.

### phandle properties

Note

See [Phandles](phandles.md#dt-phandles) for a detailed guide to phandles.

Property values can refer to other nodes using the `&another-node` phandle
syntax introduced in [Writing property values](intro-syntax-structure.md#dt-writing-property-values). Properties which
contain phandles have type `phandle`, `phandles`, or `phandle-array` in
their bindings. We’ll call these “phandle properties” for short.

You can convert a phandle to a node identifier using [`DT_PHANDLE()`](api/api.md#c.DT_PHANDLE "DT_PHANDLE"),
[`DT_PHANDLE_BY_IDX()`](api/api.md#c.DT_PHANDLE_BY_IDX "DT_PHANDLE_BY_IDX"), or [`DT_PHANDLE_BY_NAME()`](api/api.md#c.DT_PHANDLE_BY_NAME "DT_PHANDLE_BY_NAME"), depending on the
type of property you are working with.

One common use case for phandle properties is referring to other hardware in
the tree. In this case, you usually want to convert the devicetree-level
phandle to a Zephyr driver-level [struct device](../../kernel/drivers/index.md#device-model-api).
See [Get a struct device from a devicetree node](howtos.md#dt-get-device) for ways to do that.

Another common use case is accessing specifier values in a phandle array. The
general purpose APIs for this are [`DT_PHA_BY_IDX()`](api/api.md#c.DT_PHA_BY_IDX "DT_PHA_BY_IDX") and [`DT_PHA()`](api/api.md#c.DT_PHA "DT_PHA").
There are also hardware-specific shorthands like [`DT_GPIO_CTLR_BY_IDX()`](api/api.md#c.DT_GPIO_CTLR_BY_IDX "DT_GPIO_CTLR_BY_IDX"),
[`DT_GPIO_CTLR()`](api/api.md#c.DT_GPIO_CTLR "DT_GPIO_CTLR"),
[`DT_GPIO_PIN_BY_IDX()`](api/api.md#c.DT_GPIO_PIN_BY_IDX "DT_GPIO_PIN_BY_IDX"), [`DT_GPIO_PIN()`](api/api.md#c.DT_GPIO_PIN "DT_GPIO_PIN"),
[`DT_GPIO_FLAGS_BY_IDX()`](api/api.md#c.DT_GPIO_FLAGS_BY_IDX "DT_GPIO_FLAGS_BY_IDX"), and [`DT_GPIO_FLAGS()`](api/api.md#c.DT_GPIO_FLAGS "DT_GPIO_FLAGS").

See [`DT_PHA_HAS_CELL_AT_IDX()`](api/api.md#c.DT_PHA_HAS_CELL_AT_IDX "DT_PHA_HAS_CELL_AT_IDX") and [`DT_PROP_HAS_IDX()`](api/api.md#c.DT_PROP_HAS_IDX "DT_PROP_HAS_IDX") for ways to
check if a specifier value is present in a phandle property.

## Other APIs

Here are pointers to some other available APIs.

- [`DT_CHOSEN()`](api/api.md#c.DT_CHOSEN "DT_CHOSEN"), [`DT_HAS_CHOSEN()`](api/api.md#c.DT_HAS_CHOSEN "DT_HAS_CHOSEN"): for properties
  of the special `/chosen` node
- [`DT_HAS_COMPAT_STATUS_OKAY()`](api/api.md#c.DT_HAS_COMPAT_STATUS_OKAY "DT_HAS_COMPAT_STATUS_OKAY"), [`DT_NODE_HAS_COMPAT()`](api/api.md#c.DT_NODE_HAS_COMPAT "DT_NODE_HAS_COMPAT"): global-
  and node-specific tests related to the `compatible` property
- [`DT_BUS()`](api/api.md#c.DT_BUS "DT_BUS"): get a node’s bus controller, if there is one
- [`DT_ENUM_IDX()`](api/api.md#c.DT_ENUM_IDX "DT_ENUM_IDX"): for properties whose values are among a fixed list of
  choices
- [Fixed flash partitions](api/api.md#devicetree-flash-api): APIs for managing fixed flash partitions.
  Also see [Flash map](../../services/storage/flash_map/flash_map.md#flash-map-api), which wraps this in a more user-friendly API.

## Device driver conveniences

Special purpose macros are available for writing device drivers, which usually
rely on [instance identifiers](#dt-node-identifiers).

To use these, you must define `DT_DRV_COMPAT` to the `compat` value your
driver implements support for. This `compat` value is what you would pass to
[`DT_INST()`](api/api.md#c.DT_INST "DT_INST").

If you do that, you can access the properties of individual instances of your
compatible with less typing, like this:

```c
#include <zephyr/devicetree.h>

#define DT_DRV_COMPAT my_driver_compat

/* This is same thing as DT_INST(0, my_driver_compat): */
DT_DRV_INST(0)

/*
 * This is the same thing as
 * DT_PROP(DT_INST(0, my_driver_compat), clock_frequency)
 */
DT_INST_PROP(0, clock_frequency)
```

See [Instance-based APIs](api/api.md#devicetree-inst-apis) for a generic API reference.

## Hardware specific APIs

Convenience macros built on top of the above APIs are also defined to help
readability for hardware specific code. See [Hardware specific APIs](api/api.md#devicetree-hw-api) for
details.

## Generated macros

While the `zephyr/devicetree.h` API is not generated, it does rely on a
generated C header which is put into every application build directory:
[devicetree\_generated.h](intro-input-output.md#dt-outputs). This file contains macros with
devicetree data.

These macros have tricky naming conventions which the [Devicetree API](api/api.md#devicetree-api) API
abstracts away. They should be considered an implementation detail, but it’s
useful to understand them since they will frequently be seen in compiler error
messages.

This section contains an Augmented Backus-Naur Form grammar for these
generated macros, with examples and more details in comments. See [RFC 7405](https://tools.ietf.org/html/rfc7405)
(which extends [RFC 5234](https://tools.ietf.org/html/rfc5234)) for a syntax specification.

```abnf
; An RFC 7405 ABNF grammar for devicetree macros.
;
; This does *not* cover macros pulled out of DT via Kconfig,
; like CONFIG_SRAM_BASE_ADDRESS, etc. It only describes the
; ones that start with DT_ and are directly generated.

; --------------------------------------------------------------------
; dt-macro: the top level nonterminal for a devicetree macro
;
; A dt-macro starts with uppercase "DT_", and is one of:
;
; - a <node-macro>, generated for a particular node
; - some <other-macro>, a catch-all for other types of macros
dt-macro = node-macro / other-macro

; --------------------------------------------------------------------
; node-macro: a macro related to a node

; A macro about a property value
node-macro =  property-macro
; A macro about the pinctrl properties in a node.
node-macro =/ pinctrl-macro
; A macro about the GPIO hog properties in a node.
node-macro =/ gpiohogs-macro
; EXISTS macro: node exists in the devicetree
node-macro =/ %s"DT_N" path-id %s"_EXISTS"
; Bus macros: the plain BUS is a way to access a node's bus controller.
; The additional dt-name suffix is added to match that node's bus type;
; the dt-name in this case is something like "spi" or "i2c".
node-macro =/ %s"DT_N" path-id %s"_BUS" ["_" dt-name]
; The reg property is special and has its own macros.
node-macro =/ %s"DT_N" path-id %s"_REG_NUM"
node-macro =/ %s"DT_N" path-id %s"_REG_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_REG_IDX_" DIGIT
              %s"_VAL_" ( %s"ADDRESS" / %s"SIZE")
node-macro =/ %s"DT_N" path-id %s"_REG_NAME_" dt-name
              %s"_VAL_" ( %s"ADDRESS" / %s"SIZE")
node-macro =/ %s"DT_N" path-id %s"_REG_NAME_" dt-name "_EXISTS"
; The interrupts property is also special.
node-macro =/ %s"DT_N" path-id %s"_IRQ_NUM"
node-macro =/ %s"DT_N" path-id %s"_IRQ_LEVEL"
node-macro =/ %s"DT_N" path-id %s"_IRQ_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_IRQ_IDX_" DIGIT
              %s"_VAL_" dt-name [ %s"_EXISTS" ]
node-macro =/ %s"DT_N" path-id %s"_CONTROLLER"
node-macro =/ %s"DT_N" path-id %s"_IRQ_NAME_" dt-name
              %s"_VAL_" dt-name [ %s"_EXISTS" ]
node-macro =/ %s"DT_N" path-id %s"_IRQ_NAME_" dt-name "_CONTROLLER"
; The ranges property is also special.
node-macro =/ %s"DT_N" path-id %s"_RANGES_NUM"
node-macro =/ %s"DT_N" path-id %s"_RANGES_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_RANGES_IDX_" DIGIT
              %s"_VAL_" ( %s"CHILD_BUS_FLAGS" / %s"CHILD_BUS_ADDRESS" /
                          %s"PARENT_BUS_ADDRESS" / %s"LENGTH")
node-macro =/ %s"DT_N" path-id %s"_RANGES_IDX_" DIGIT
              %s"_VAL_CHILD_BUS_FLAGS_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_RANGE"
; Subnodes of the fixed-partitions compatible get macros which contain
; a unique ordinal value for each partition
node-macro =/ %s"DT_N" path-id %s"_PARTITION_ID" DIGIT
; Macros are generated for each of a node's compatibles;
; dt-name in this case is something like "vnd_device".
node-macro =/ %s"DT_N" path-id %s"_COMPAT_MATCHES_" dt-name
node-macro =/ %s"DT_N" path-id %s"_COMPAT_VENDOR_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_COMPAT_VENDOR_IDX_" DIGIT
node-macro =/ %s"DT_N" path-id %s"_COMPAT_MODEL_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_COMPAT_MODEL_IDX_" DIGIT
; Every non-root node gets one of these macros, which expands to the node
; identifier for that node's parent in the devicetree.
node-macro =/ %s"DT_N" path-id %s"_PARENT"
; These are used internally by DT_FOREACH_PROP_ELEM(_SEP)(_VARGS), which
; iterates over each property element.
node-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_PROP_ELEM"
node-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_PROP_ELEM_SEP"
node-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_PROP_ELEM_VARGS"
node-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_PROP_ELEM_SEP_VARGS"
; These are used by DT_CHILD_NUM and DT_CHILD_NUM_STATUS_OKAY macros
node-macro =/ %s"DT_N" path-id %s"_CHILD_NUM"
node-macro =/ %s"DT_N" path-id %s"_CHILD_NUM_STATUS_OKAY"
; These are used internally by DT_FOREACH_CHILD, which iterates over
; each child node.
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_SEP"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_VARGS"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_SEP_VARGS"
; These are used internally by DT_FOREACH_CHILD_STATUS_OKAY, which iterates
; over each child node with status "okay".
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_STATUS_OKAY"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_STATUS_OKAY_SEP"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_STATUS_OKAY_VARGS"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_STATUS_OKAY_SEP_VARGS"
; These are used internally by DT_FOREACH_NODELABEL and
; DT_FOREACH_NODELABEL_VARGS, which iterate over a node's node labels.
node-macro =/ %s"DT_N" path-id %s"_FOREACH_NODELABEL" [ %s"_VARGS" ]
; These are used internally by DT_NUM_NODELABELS
node-macro =/ %s"DT_N" path-id %s"_NODELABEL_NUM"
; The node's zero-based index in the list of it's parent's child nodes.
node-macro =/ %s"DT_N" path-id %s"_CHILD_IDX"
; The node's status macro; dt-name in this case is something like "okay"
; or "disabled".
node-macro =/ %s"DT_N" path-id %s"_STATUS_" dt-name
; The node's dependency ordinal. This is a non-negative integer
; value that is used to represent dependency information.
node-macro =/ %s"DT_N" path-id %s"_ORD"
; The node's path, as a string literal
node-macro =/ %s"DT_N" path-id %s"_PATH"
; The node's name@unit-addr, as a string literal
node-macro =/ %s"DT_N" path-id %s"_FULL_NAME"
; The dependency ordinals of a node's requirements (direct dependencies).
node-macro =/ %s"DT_N" path-id %s"_REQUIRES_ORDS"
; The dependency ordinals of a node supports (reverse direct dependencies).
node-macro =/ %s"DT_N" path-id %s"_SUPPORTS_ORDS"

; --------------------------------------------------------------------
; pinctrl-macro: a macro related to the pinctrl properties in a node
;
; These are a bit of a special case because they kind of form an array,
; but the array indexes correspond to pinctrl-DIGIT properties in a node.
;
; So they're related to a node, but not just one property within the node.
;
; The following examples assume something like this:
;
;      foo {
;              pinctrl-0 = <&bar>;
;              pinctrl-1 = <&baz>;
;              pinctrl-names = "default", "sleep";
;      };

; Total number of pinctrl-DIGIT properties in the node. May be zero.
;
;   #define DT_N_<node path>_PINCTRL_NUM 2
pinctrl-macro = %s"DT_N" path-id %s"_PINCTRL_NUM"
; A given pinctrl-DIGIT property exists.
;
;     #define DT_N_<node path>_PINCTRL_IDX_0_EXISTS 1
;     #define DT_N_<node path>_PINCTRL_IDX_1_EXISTS 1
pinctrl-macro =/ %s"DT_N" path-id %s"_PINCTRL_IDX_" DIGIT %s"_EXISTS"
; A given pinctrl property name exists.
;
;     #define DT_N_<node path>_PINCTRL_NAME_default_EXISTS 1
;     #define DT_N_<node path>_PINCTRL_NAME_sleep_EXISTS 1
pinctrl-macro =/ %s"DT_N" path-id %s"_PINCTRL_NAME_" dt-name %s"_EXISTS"
; The corresponding index number of a named pinctrl property.
;
;     #define DT_N_<node path>_PINCTRL_NAME_default_IDX 0
;     #define DT_N_<node path>_PINCTRL_NAME_sleep_IDX 1
pinctrl-macro =/ %s"DT_N" path-id %s"_PINCTRL_NAME_" dt-name %s"_IDX"
; The node identifier for the phandle in a named pinctrl property.
;
;    #define DT_N_<node path>_PINCTRL_NAME_default_IDX_0_PH <node id for 'bar'>
;
; There's no need for a separate macro for access by index: that's
; covered by property-macro. We only need this because the map from
; names to properties is implicit in the structure of the DT.
pinctrl-macro =/ %s"DT_N" path-id %s"_PINCTRL_NAME_" dt-name %s"_IDX_" DIGIT %s"_PH"

; --------------------------------------------------------------------
; gpiohogs-macro: a macro related to GPIO hog nodes
;
; The following examples assume something like this:
;
;     gpio1: gpio@... {
;       compatible = "vnd,gpio";
;       #gpio-cells = <2>;
;
;       node-1 {
;               gpio-hog;
;               gpios = <0x0 0x10>, <0x1 0x20>;
;               output-high;
;       };
;
;       node-2 {
;               gpio-hog;
;               gpios = <0x2 0x30>;
;               output-low;
;       };
;     };
;
; Bindings fragment for the vnd,gpio compatible:
;
;     gpio-cells:
;       - pin
;       - flags

; The node contains GPIO hogs.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_EXISTS 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_EXISTS 1
gpioshogs-macro = %s"DT_N" path-id %s"_GPIO_HOGS_EXISTS"
; Number of hogged GPIOs in a node.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_NUM 2
;   #define DT_N_<node-2 path>_GPIO_HOGS_NUM 1
gpioshogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_NUM"
; A given logical GPIO hog array index exists.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_EXISTS 1
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_EXISTS 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_EXISTS 1
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_EXISTS"
; The node identifier for the phandle of a logical index in the GPIO hogs array.
; These macros are currently unused by Zephyr.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_PH <node id for 'gpio1'>
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_PH <node id for 'gpio1'>
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_PH <node id for 'gpio1'>
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_PH"
; The pin cell of a logical index in the GPIO hogs array exists.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_VAL_pin_EXISTS 1
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_VAL_pin_EXISTS 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_VAL_pin_EXISTS 1
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_VAL_pin_EXISTS"
; The value of the pin cell of a logical index in the GPIO hogs array.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_VAL_pin 0
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_VAL_pin 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_VAL_pin 2
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_VAL_pin"
; The flags cell of a logical index in the GPIO hogs array exists.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_VAL_flags_EXISTS 1
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_VAL_flags_EXISTS 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_VAL_flags_EXISTS 1
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_VAL_flags_EXISTS"
; The value of the flags cell of a logical index in the GPIO hogs array.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_VAL_flags 0x10
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_VAL_flags 0x20
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_VAL_flags 0x30
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_VAL_flags"

; --------------------------------------------------------------------
; property-macro: a macro related to a node property
;
; These combine a node identifier with a "lowercase-and-underscores form"
; property name. The value expands to something related to the property's
; value.
;
; The optional prop-suf suffix is when there's some specialized
; subvalue that deserves its own macro, like the macros for an array
; property's individual elements
;
; The "plain vanilla" macro for a property's value, with no prop-suf,
; looks like this:
;
;   DT_N_<node path>_P_<property name>
;
; Components:
;
; - path-id: node's devicetree path converted to a C token
; - prop-id: node's property name converted to a C token
; - prop-suf: an optional property-specific suffix
property-macro =  %s"DT_N" path-id %s"_P_" prop-id [prop-suf]

; --------------------------------------------------------------------
; path-id: a node's path-based macro identifier
;
; This in "lowercase-and-underscores" form. I.e. it is
; the node's devicetree path converted to a C token by changing:
;
; - each slash (/) to _S_
; - all letters to lowercase
; - non-alphanumerics characters to underscores
;
; For example, the leaf node "bar-BAZ" in this devicetree:
;
;   / {
;           foo@123 {
;                   bar-BAZ {};
;           };
;   };
;
; has path-id "_S_foo_123_S_bar_baz".
path-id = 1*( %s"_S_" dt-name )

; ----------------------------------------------------------------------
; prop-id: a property identifier
;
; A property name converted to a C token by changing:
;
; - all letters to lowercase
; - non-alphanumeric characters to underscores
;
; Example node:
;
;   chosen {
;       zephyr,console = &uart1;
;       WHY,AM_I_SHOUTING = "unclear";
;   };
;
; The 'zephyr,console' property has prop-id 'zephyr_console'.
; 'WHY,AM_I_SHOUTING' has prop-id 'why_am_i_shouting'.
prop-id = dt-name

; ----------------------------------------------------------------------
; prop-suf: a property-specific macro suffix
;
; Extra macros are generated for properties:
;
; - that are special to the specification ("reg", "interrupts", etc.)
; - with array types (uint8-array, phandle-array, etc.)
; - with "enum:" in their bindings
; - that have zephyr device API specific macros for phandle-arrays
; - related to phandle specifier names ("foo-names")
;
; Here are some examples:
;
; - _EXISTS: property, index or name existence flag
; - _SIZE: logical property length
; - _IDX_<i>: values of individual array elements
; - _IDX_<DIGIT>_VAL_<dt-name>: values of individual specifier
;   cells within a phandle array
; - _ADDR_<i>: for reg properties, the i-th register block address
; - _LEN_<i>: for reg properties, the i-th register block length
;
; The different cases are not exhaustively documented here to avoid
; this file going stale. Please see devicetree.h if you need to know
; the details.
prop-suf = 1*( "_" gen-name ["_" dt-name] )

; --------------------------------------------------------------------
; other-macro: grab bag for everything that isn't a node-macro.

; See examples below.
other-macro =  %s"DT_N_" alternate-id
; Total count of enabled instances of a compatible.
other-macro =/ %s"DT_N_INST_" dt-name %s"_NUM_OKAY"
; These are used internally by DT_FOREACH_NODE and
; DT_FOREACH_STATUS_OKAY_NODE respectively.
other-macro =/ %s"DT_FOREACH_HELPER"
other-macro =/ %s"DT_FOREACH_OKAY_HELPER"
; These are used internally by DT_FOREACH_STATUS_OKAY,
; which iterates over each enabled node of a compatible.
other-macro =/ %s"DT_FOREACH_OKAY_" dt-name
other-macro =/ %s"DT_FOREACH_OKAY_VARGS_" dt-name
; These are used internally by DT_INST_FOREACH_STATUS_OKAY,
; which iterates over each enabled instance of a compatible.
other-macro =/ %s"DT_FOREACH_OKAY_INST_" dt-name
other-macro =/ %s"DT_FOREACH_OKAY_INST_VARGS_" dt-name
; E.g.: #define DT_CHOSEN_zephyr_flash
other-macro =/ %s"DT_CHOSEN_" dt-name
; Declares that a compatible has at least one node on a bus.
; Example:
;
;   #define DT_COMPAT_vnd_dev_BUS_spi 1
other-macro =/ %s"DT_COMPAT_" dt-name %s"_BUS_" dt-name
; Declares that a compatible has at least one status "okay" node.
; Example:
;
;   #define DT_COMPAT_HAS_OKAY_vnd_dev 1
other-macro =/ %s"DT_COMPAT_HAS_OKAY_" dt-name
; Currently used to allow mapping a lowercase-and-underscores "label"
; property to a fixed-partitions node. See the flash map API docs
; for an example.
other-macro =/ %s"DT_COMPAT_" dt-name %s"_LABEL_" dt-name

; --------------------------------------------------------------------
; alternate-id: another way to specify a node besides a path-id
;
; Example devicetree:
;
;   / {
;           aliases {
;                   dev = &dev_1;
;           };
;
;           soc {
;               dev_1: device@123 {
;                   compatible = "vnd,device";
;               };
;           };
;   };
;
; Node device@123 has these alternate-id values:
;
; - ALIAS_dev
; - NODELABEL_dev_1
; - INST_0_vnd_device
;
; The full alternate-id macros are:
;
;   #define DT_N_INST_0_vnd_device     DT_N_S_soc_S_device_123
;   #define DT_N_ALIAS_dev             DT_N_S_soc_S_device_123
;   #define DT_N_NODELABEL_dev_1       DT_N_S_soc_S_device_123
;
; These mainly exist to allow pasting an alternate-id macro onto a
; "_P_<prop-id>" to access node properties given a node's alias, etc.
;
; Notice that "inst"-type IDs have a leading instance identifier,
; which is generated by the devicetree scripts. The other types of
; alternate-id begin immediately with names taken from the devicetree.
alternate-id =  ( %s"ALIAS" / %s"NODELABEL" ) dt-name
alternate-id =/ %s"INST_" 1*DIGIT "_" dt-name

; --------------------------------------------------------------------
; miscellaneous helper definitions

; A dt-name is one or more:
; - lowercase ASCII letters (a-z)
; - numbers (0-9)
; - underscores ("_")
;
; They are the result of converting names or combinations of names
; from devicetree to a valid component of a C identifier by
; lowercasing letters (in practice, this is a no-op) and converting
; non-alphanumeric characters to underscores.
;
; You'll see these referred to as "lowercase-and-underscores" forms of
; various devicetree identifiers throughout the documentation.
dt-name = 1*( lower / DIGIT / "_" )

; gen-name is used as a stand-in for a component of a generated macro
; name which does not come from devicetree (dt-name covers that case).
;
; - uppercase ASCII letters (a-z)
; - numbers (0-9)
; - underscores ("_")
gen-name = upper 1*( upper / DIGIT / "_" )

; "lowercase ASCII letter" turns out to be pretty annoying to specify
; in RFC-7405 syntax.
;
; This is just ASCII letters a (0x61) through z (0x7a).
lower = %x61-7A

; "uppercase ASCII letter" in RFC-7405 syntax
upper = %x41-5A
```
