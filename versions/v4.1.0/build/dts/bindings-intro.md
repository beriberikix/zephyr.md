---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/bindings-intro.html
original_path: build/dts/bindings-intro.html
---

# Introduction to Devicetree Bindings

Note

For a detailed syntax reference, see [Devicetree bindings syntax](bindings-syntax.md#dt-bindings-file-syntax).

Devicetree nodes are matched to bindings using their [compatible
properties](intro-syntax-structure.md#dt-important-props).

During the [Configuration Phase](../cmake/index.md#build-configuration-phase), the build system tries to match
each node in the devicetree to a binding file. When this succeeds, the build
system uses the information in the binding file both when validating the node’s
contents and when generating macros for the node.

## A simple example

Here is an example devicetree node:

```devicetree
/* Node in a DTS file */
bar-device {
     compatible = "foo-company,bar-device";
     num-foos = <3>;
};
```

Here is a minimal binding file which matches the node:

```yaml
# A YAML binding matching the node

compatible: "foo-company,bar-device"

properties:
  num-foos:
    type: int
    required: true
```

The build system matches the `bar-device` node to its YAML binding because
the node’s `compatible` property matches the binding’s `compatible:` line.

## What the build system does with bindings

The build system uses bindings both to validate devicetree nodes and to convert
the devicetree’s contents into the generated [devicetree\_generated.h](intro-input-output.md#dt-outputs) header file.

For example, the build system would use the above binding to check that the
required `num-foos` property is present in the `bar-device` node, and that
its value, `<3>`, has the correct type.

The build system will then generate a macro for the `bar-device` node’s
`num-foos` property, which will expand to the integer literal `3`. This
macro lets you get the value of the property in C code using the API which is
discussed later in this guide in [Devicetree access from C/C++](api-usage.md#dt-from-c).

For another example, the following node would cause a build error, because it
has no `num-foos` property, and this property is marked required in the
binding:

```devicetree
bad-node {
     compatible = "foo-company,bar-device";
};
```

## Other ways nodes are matched to bindings

If a node has more than one string in its `compatible` property, the build
system looks for compatible bindings in the listed order and uses the first
match.

Take this node as an example:

```devicetree
baz-device {
     compatible = "foo-company,baz-device", "generic-baz-device";
};
```

The `baz-device` node would get matched to a binding with a `compatible:
"generic-baz-device"` line if the build system can’t find a binding with a
`compatible: "foo-company,baz-device"` line.

Nodes without compatible properties can be matched to bindings associated with
their parent nodes. These are called “child bindings”. If a node describes
hardware on a bus, like I2C or SPI, then the bus type is also taken into
account when matching nodes to bindings. (See [On-bus](bindings-syntax.md#dt-bindings-on-bus) for
details).

See [The /zephyr,user node](zephyr-user-node.md#dt-zephyr-user) for information about a special node that doesn’t
require any binding.

## Where bindings are located

Binding file names usually match their `compatible:` lines. For example, the
above example binding would be named `foo-company,bar-device.yaml` by
convention.

The build system looks for bindings in `dts/bindings`
subdirectories of the following places:

- the zephyr repository
- your [application source directory](../../develop/application/index.md#application)
- your [board directory](../../hardware/porting/board_porting.md#board-porting-guide)
- any [shield directories](../../hardware/porting/shields.md#shields)
- any directories manually included in the [DTS\_ROOT](../../develop/application/index.md#dts-root)
  CMake variable
- any [module](../../develop/modules.md#modules) that defines a `dts_root` in its
  [Build settings](../../develop/modules.md#modules-build-settings)

The build system will consider any YAML file in any of these, including in any
subdirectories, when matching nodes to bindings. A file is considered YAML if
its name ends with `.yaml` or `.yml`.

Warning

The binding files must be located somewhere inside the `dts/bindings`
subdirectory of the above places.

For example, if `my-app` is your application directory, then you must
place application-specific bindings inside `my-app/dts/bindings`. So
`my-app/dts/bindings/serial/my-company,my-serial-port.yaml` would be
found, but `my-app/my-company,my-serial-port.yaml` would be ignored.
