---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/intro-scope-purpose.html
original_path: build/dts/intro-scope-purpose.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Scope and purpose

A *devicetree* is primarily a hierarchical data structure that describes
hardware. The [Devicetree specification](https://www.devicetree.org/) defines its source and binary
representations.

Zephyr uses devicetree to describe:

- the hardware available on its [Supported Boards](../../boards/index.md#boards)
- that hardware’s initial configuration

As such, devicetree is both a hardware description language and a configuration
language for Zephyr. See [Devicetree versus Kconfig](dt-vs-kconfig.md#dt-vs-kconfig) for some comparisons between
devicetree and Zephyr’s other main configuration language, Kconfig.

There are two types of devicetree input files: *devicetree sources* and
*devicetree bindings*. The sources contain the devicetree itself. The bindings
describe its contents, including data types. The [build system](../index.md#build-overview) uses devicetree sources and bindings to produce a generated C
header. The generated header’s contents are abstracted by the `devicetree.h`
API, which you can use to get information from your devicetree.

Here is a simplified view of the process:

![../../_images/zephyr_dt_build_flow.png](../../_images/zephyr_dt_build_flow.png)

Devicetree build flow

All Zephyr and application source code files can include and use
`devicetree.h`. This includes [device drivers](../../kernel/drivers/index.md#device-model-api),
[applications](../../develop/application/index.md#application), [tests](../../develop/test/index.md#testing), the kernel, etc.

The API itself is based on C macros. The macro names all start with `DT_`. In
general, if you see a macro that starts with `DT_` in a Zephyr source file,
it’s probably a `devicetree.h` macro. The generated C header contains macros
that start with `DT_` as well; you might see those in compiler error
messages. You always can tell a generated- from a non-generated macro:
generated macros have some lowercased letters, while the `devicetree.h` macro
names have all capital letters.
