---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/phandles.html
original_path: build/dts/phandles.html
---

# Phandles

The devicetree concept of a *phandle* is very similar to pointers in
C. You can use phandles to refer to nodes in devicetree similarly to the way
you can use pointers to refer to structures in C.

## [Getting phandles](#id3)

The usual way to get a phandle for a devicetree node is from one of its node
labels. For example, with this devicetree:

```dts
/ {
        lbl_a: node-1 {};
        lbl_b: lbl_c: node-2 {};
};
```

You can write the phandle for:

- `/node-1` as `&lbl_a`
- `/node-2` as either `&lbl_b` or `&lbl_c`

Notice how the `&nodelabel` devicetree syntax is similar to the “address of”
C syntax.

## [Using phandles](#id4)

Note

“Type” in this section refers to one of the type names documented in
[Properties](bindings-syntax.md#dt-bindings-properties) in the devicetree bindings documentation.

Here are the main ways you will use phandles.

### [One node: phandle type](#id5)

You can use phandles to refer to `node-b` from `node-a`, where `node-b`
is related to `node-a` in some way.

One common example is when `node-a` represents some hardware that
generates an interrupt, and `node-b` represents the interrupt
controller that receives the asserted interrupt. In this case, you could
write:

```dts
node_b: node-b {
        interrupt-controller;
};

node-a {
        interrupt-parent = <&node_b>;
};
```

This uses the standard `interrupt-parent` property defined in the
devicetree specification to capture the relationship between the two nodes.

These properties have type `phandle`.

### [Zero or more nodes: phandles type](#id6)

You can use phandles to make an array of references to other nodes.

One common example occurs in [pin control](../../hardware/pinctrl/index.md#pinctrl-guide). Pin control
properties like `pinctrl-0`, `pinctrl-1` etc. may contain multiple
phandles, each of which “points” to a node containing information related to
pin configuration for that hardware peripheral. Here’s an example of six
phandles in a single property:

```dts
pinctrl-0 = <&quadspi_clk_pe10 &quadspi_ncs_pe11
             &quadspi_bk1_io0_pe12 &quadspi_bk1_io1_pe13
             &quadspi_bk1_io2_pe14 &quadspi_bk1_io3_pe15>;
```

These properties have type `phandles`.

### [Zero or more nodes with metadata: phandle-array type](#id7)

You can use phandles to refer to and configure one or more resources that are
“owned” by some other node.

This is the most complex case. There are examples and more details in the
next section.

These properties have type `phandle-array`.

## [phandle-array properties](#id8)

These properties are commonly used to specify a resource that is owned by
another node along with additional metadata about the resource.

### [High level description](#id9)

Usually, properties with this type are written like `phandle-array-prop` in
this example:

```dts
node {
        phandle-array-prop = <&foo 1 2>, <&bar 3>, <&baz 4 5>;
};
```

That is, the property’s value is written as a comma-separated sequence of
“groups”, where each “group” is written inside of angle brackets (`< ... >`).
Each “group” starts with a phandle (`&foo`, `&bar`, `&baz`). The values
that follow the phandle in each “group” are called *specifiers*. There are
three specifiers in the above example:

1. `1 2`
2. `3`
3. `4 5`

The phandle in each “group” is used to “point” to the hardware that controls
the resource you are interested in. The specifier describes the resource
itself, along with any additional necessary metadata.

The rest of this section describes a common example. Subsequent sections
document more rules about how to use phandle-array properties in practice.

### [Example phandle-arrays: GPIOs](#id10)

Perhaps the most common use case for phandle-array properties is specifying one
or more GPIOs on your SoC that another chip on your board connects to. For that
reason, we’ll focus on that use case here. However, there are **many other use
cases** that are handled in devicetree with phandle-array properties.

For example, consider an external chip with an interrupt pin that is connected
to a GPIO on your SoC. You will typically need to provide that GPIO’s
information (GPIO controller and pin number) to the [device driver](../../kernel/drivers/index.md#device-model-api) for that chip. You usually also need to provide other
metadata about the GPIO, like whether it is active low or high, what kind of
internal pull resistor within the SoC should be enabled in order to communicate
with the device, etc., to the driver.

In the devicetree, there will be a node that represents the GPIO controller
that controls a group of pins. This reflects the way GPIO IP blocks are usually
developed in hardware. Therefore, there is no single node in the devicetree
that represents a GPIO pin, and you can’t use a single phandle to represent it.

Instead, you would use a phandle-array property, like this:

```text
my-external-ic {
        irq-gpios = <&gpioX pin flags>;
};
```

In this example, `irq-gpios` is a phandle-array property with just one
“group” in its value. `&gpioX` is the phandle for the GPIO controller node
that controls the pin. `pin` is the pin number (0, 1, 2, …). `flags` is a
bit mask describing pin metadata (for example `(GPIO_ACTIVE_LOW |
GPIO_PULL_UP)`); see [include/zephyr/dt-bindings/gpio/gpio.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/gpio/gpio.h) for
more details.

The device driver handling the `my-external-ic` node can then use the
`irq-gpios` property’s value to set up interrupt handling for the chip as it
is used on your board. This lets you configure the device driver in devicetree,
without changing the driver’s source code.

Such properties can contain multiple values as well:

```text
my-other-external-ic {
        handshake-gpios = <&gpioX pinX flagsX>, <&gpioY pinY flagsY>;
};
```

The above example specifies two pins:

- `pinX` on the GPIO controller with phandle `&gpioX`, flags `flagsX`
- `pinY` on `&gpioY`, flags `flagsY`

You may be wondering how the “pin and flags” convention is established and
enforced. To answer this question, we’ll need to introduce a concept called
specifier spaces before moving on to some information about devicetree
bindings.

## [Specifier spaces](#id11)

*Specifier spaces* are a way to allow nodes to describe how you should
use them in phandle-array properties.

We’ll start with an abstract, high level description of how specifier spaces
work in DTS files, before moving on to a concrete example and providing
references to further reading for how this all works in practice using DTS
files and bindings files.

### [High level description](#id12)

As described above, a phandle-array property is a sequence of “groups” of
phandles followed by some number of cells:

```dts
node {
        phandle-array-prop = <&foo 1 2>, <&bar 3>;
};
```

The cells that follow each phandle are called a *specifier*. In this example,
there are two specifiers:

1. `1 2`: two cells
2. `3`: one cell

Every phandle-array property has an associated *specifier space*. This sounds
complex, but it’s really just a way to assign a meaning to the cells that
follow each phandle in a hardware specific way. Every specifier space has a
unique name. There are a few “standard” names for commonly used hardware, but
you can create your own as well.

Devicetree nodes encode the number of cells that must appear in a specifier, by
name, using the `#SPACE_NAME-cells` property. For example, let’s assume that
`phandle-array-prop`‘s specifier space is named `baz`. Then we would need
the `foo` and `bar` nodes to have the following `#baz-cells` properties:

```dts
foo: node@1000 {
        #baz-cells = <2>;
};

bar: node@2000 {
        #baz-cells = <1>;
};
```

Without the `#baz-cells` property, the devicetree tooling would not be able
to validate the number of cells in each specifier in `phandle-array-prop`.

This flexibility allows you to write down an array of hardware resources in a
single devicetree property, even though the amount of metadata you need to
describe each resource might be different for different nodes.

A single node can also have different numbers of cells in different specifier
spaces. For example, we might have:

```dts
foo: node@1000 {
        #baz-cells = <2>;
        #bob-cells = <1>;
};
```

With that, if `phandle-array-prop-2` has specifier space `bob`, we could
write:

```dts
node {
        phandle-array-prop = <&foo 1 2>, <&bar 3>;
        phandle-array-prop-2 = <&foo 4>;
};
```

This flexibility allows you to have a node that manages multiple different
kinds of resources at the same time. The node describes the amount of metadata
needed to describe each kind of resource (how many cells are needed in each
case) using different `#SPACE_NAME-cells` properties.

### [Example specifier space: gpio](#id13)

From the above example, you’re already familiar with how one specifier space
works: in the “gpio” space, specifiers almost always have two cells:

1. a pin number
2. a bit mask of flags related to the pin

Therefore, almost all GPIO controller nodes you will see in practice will look
like this:

```dts
gpioX: gpio-controller@deadbeef {
        gpio-controller;
        #gpio-cells = <2>;
};
```

## [Associating properties with specifier spaces](#id14)

Above, we have described that:

- each phandle-array property has an associated specifier space
- specifier spaces are identified by name
- devicetree nodes use `#SPECIFIER_NAME-cells` properties to
  configure the number of cells which must appear in a specifier

In this section, we explain how phandle-array properties get their specifier
spaces.

### [High level description](#id15)

In general, a `phandle-array` property named `foos` implicitly has
specifier space `foo`. For example:

```yaml
properties:
  dmas:
    type: phandle-array
  pwms:
    type: phandle-array
```

The `dmas` property’s specifier space is “dma”. The `pwm` property’s
specifier space is `pwm`.

### [Special case: GPIO](#id16)

`*-gpios` properties are special-cased so that e.g. `foo-gpios` resolves to
`#gpio-cells` rather than `#foo-gpio-cells`.

### [Manually specifying a space](#id17)

You can manually specify the specifier space for any `phandle-array`
property. See [specifier-space](bindings-syntax.md#dt-bindings-specifier-space).

## [Naming the cells in a specifier](#id18)

You should name the cells in each specifier space your hardware supports when
writing bindings. For details on how to do this, see [Specifier cell names (\*-cells)](bindings-syntax.md#dt-bindings-cells).

This allows C code to query information about and retrieve the values of cells
in a specifier by name using devicetree APIs like these:

- [`DT_PHA_BY_IDX`](../../doxygen/html/group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)
- [`DT_PHA_BY_NAME`](../../doxygen/html/group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)

This feature and these macros are used internally by numerous hardware-specific
APIs. Here are a few examples:

- [`DT_GPIO_PIN_BY_IDX`](../../doxygen/html/group__devicetree-gpio.md#ga8f7d82567056266bab1603865f8b27af)
- [`DT_PWMS_CHANNEL_BY_IDX`](../../doxygen/html/group__devicetree-pwms.md#ga10a372e44c7e3feb551ca996c6ca5a8f)
- [`DT_DMAS_CELL_BY_NAME`](../../doxygen/html/group__devicetree-dmas.md#ga1b80ae7fee6bcc9aa2ad03435e70dd14)
- [`DT_IO_CHANNELS_INPUT_BY_IDX`](../../doxygen/html/group__devicetree-io-channels.md#ga290c912d0a96ba65bb44341a783fac19)
- [`DT_CLOCKS_CELL_BY_NAME`](../../doxygen/html/group__devicetree-clocks.md#gaca32bfb478ac92e6a760ad0761328d5a)

## [See also](#id19)

- [Writing property values](intro-syntax-structure.md#dt-writing-property-values): how to write phandles in devicetree
  properties
- [Properties](bindings-syntax.md#dt-bindings-properties): how to write bindings for properties with
  phandle types (`phandle`, `phandles`, `phandle-array`)
- [specifier-space](bindings-syntax.md#dt-bindings-specifier-space): how to manually specify a phandle-array
  property’s specifier space
