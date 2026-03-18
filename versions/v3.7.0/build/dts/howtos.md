---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/howtos.html
original_path: build/dts/howtos.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Devicetree HOWTOs

This page has step-by-step advice for getting things done with devicetree.

Tip

See [Troubleshooting devicetree](troubleshooting.md#dt-trouble) for troubleshooting advice.

## Get your devicetree and generated header

A board’s devicetree ([BOARD.dts](intro-input-output.md#devicetree-in-out-files)) pulls in
common node definitions via `#include` preprocessor directives. This at least
includes the SoC’s `.dtsi`. One way to figure out the devicetree’s contents
is by opening these files, e.g. by looking in
`dts/<ARCH>/<vendor>/<soc>.dtsi`, but this can be time consuming.

If you just want to see the “final” devicetree for your board, build an
application and open the `zephyr.dts` file in the build directory.

Tip

You can build [Hello World](../../samples/hello_world/README.md#hello-world) to see the “base” devicetree for your board
without any additional changes from [overlay files](intro-input-output.md#dt-input-files).

For example, using the [ARM Cortex-M3 Emulation (QEMU)](../../boards/qemu/cortex_m3/doc/index.md#qemu-cortex-m3) board to build [Hello World](../../samples/hello_world/README.md#hello-world):

```shell
# --cmake-only here just forces CMake to run, skipping the
# build process to save time.
west build -b qemu_cortex_m3 samples/hello_world --cmake-only
```

You can change `qemu_cortex_m3` to match your board.

CMake prints the input and output file locations like this:

```text
-- Found BOARD.dts: .../zephyr/boards/arm/qemu_cortex_m3/qemu_cortex_m3.dts
-- Generated zephyr.dts: .../zephyr/build/zephyr/zephyr.dts
-- Generated devicetree_generated.h: .../zephyr/build/zephyr/include/generated/zephyr/devicetree_generated.h
```

The `zephyr.dts` file is the final devicetree in DTS format.

The `devicetree_generated.h` file is the corresponding generated header.

See [Input and output files](intro-input-output.md#devicetree-in-out-files) for details about these files.

## Get a struct device from a devicetree node

When writing Zephyr applications, you’ll often want to get a driver-level
[struct device](../../kernel/drivers/index.md#device-model-api) corresponding to a devicetree node.

For example, with this devicetree fragment, you might want the struct device
for `serial@40002000`:

```devicetree
/ {
        soc {
                serial0: serial@40002000 {
                        status = "okay";
                        current-speed = <115200>;
                        /* ... */
                };
        };

        aliases {
                my-serial = &serial0;
        };

        chosen {
                zephyr,console = &serial0;
        };
};
```

Start by making a [node identifier](api-usage.md#dt-node-identifiers) for the device
you are interested in. There are different ways to do this; pick whichever one
works best for your requirements. Here are some examples:

```c
/* Option 1: by node label */
#define MY_SERIAL DT_NODELABEL(serial0)

/* Option 2: by alias */
#define MY_SERIAL DT_ALIAS(my_serial)

/* Option 3: by chosen node */
#define MY_SERIAL DT_CHOSEN(zephyr_console)

/* Option 4: by path */
#define MY_SERIAL DT_PATH(soc, serial_40002000)
```

Once you have a node identifier there are two ways to proceed. One way to get a
device is to use [`DEVICE_DT_GET()`](../../kernel/drivers/index.md#c.DEVICE_DT_GET "DEVICE_DT_GET"):

```c
const struct device *const uart_dev = DEVICE_DT_GET(MY_SERIAL);

if (!device_is_ready(uart_dev)) {
        /* Not ready, do not use */
        return -ENODEV;
}
```

There are variants of [`DEVICE_DT_GET()`](../../kernel/drivers/index.md#c.DEVICE_DT_GET "DEVICE_DT_GET") such as
[`DEVICE_DT_GET_OR_NULL()`](../../kernel/drivers/index.md#c.DEVICE_DT_GET_OR_NULL "DEVICE_DT_GET_OR_NULL"), [`DEVICE_DT_GET_ONE()`](../../kernel/drivers/index.md#c.DEVICE_DT_GET_ONE "DEVICE_DT_GET_ONE") or
[`DEVICE_DT_GET_ANY()`](../../kernel/drivers/index.md#c.DEVICE_DT_GET_ANY "DEVICE_DT_GET_ANY"). This idiom fetches the device pointer at
build-time, which means there is no runtime penalty. This method is useful if
you want to store the device pointer as configuration data. But because the
device may not be initialized, or may have failed to initialize, you must verify
that the device is ready to be used before passing it to any API functions.
(This check is done for you by [`device_get_binding()`](../../kernel/drivers/index.md#c.device_get_binding "device_get_binding").)

In some situations the device cannot be known at build-time, e.g., if it depends
on user input like in a shell application. In this case you can get the
`struct device` by combining [`device_get_binding()`](../../kernel/drivers/index.md#c.device_get_binding "device_get_binding") with the device
name:

```c
const char *dev_name = /* TODO: insert device name from user */;
const struct device *uart_dev = device_get_binding(dev_name);
```

You can then use `uart_dev` with [Universal Asynchronous Receiver-Transmitter (UART)](../../hardware/peripherals/uart.md#uart-api) API functions like
[`uart_configure()`](../../hardware/peripherals/uart.md#c.uart_configure "uart_configure"). Similar code will work for other device types; just
make sure you use the correct API for the device.

If you’re having trouble, see [Troubleshooting devicetree](troubleshooting.md#dt-trouble). The first thing to check is
that the node has `status = "okay"`, like this:

```c
#define MY_SERIAL DT_NODELABEL(my_serial)

#if DT_NODE_HAS_STATUS(MY_SERIAL, okay)
const struct device *const uart_dev = DEVICE_DT_GET(MY_SERIAL);
#else
#error "Node is disabled"
#endif
```

If you see the `#error` output, make sure to enable the node in your
devicetree. In some situations your code will compile but it will fail to link
with a message similar to:

```text
...undefined reference to `__device_dts_ord_N'
collect2: error: ld returned 1 exit status
```

This likely means there’s a Kconfig issue preventing the device driver from
being built, resulting in a reference that does not exist. If your code compiles
successfully, the last thing to check is if the device is ready, like this:

```c
if (!device_is_ready(uart_dev)) {
     printk("Device not ready\n");
}
```

If you find that the device is not ready, it likely means that the device’s
initialization function failed. Enabling logging or debugging driver code may
help in such situations. Note that you can also use [`device_get_binding()`](../../kernel/drivers/index.md#c.device_get_binding "device_get_binding")
to obtain a reference at runtime. If it returns `NULL` it can either mean that
device’s driver failed to initialize or that it does not exist.

## Find a devicetree binding

[Devicetree bindings](bindings.md#dt-bindings) are YAML files which declare what you can do with the nodes
they describe, so it’s critical to be able to find them for the nodes you are
using.

If you don’t have them already, [Get your devicetree and generated header](#get-devicetree-outputs). To find a node’s
binding, open the generated header file, which starts with a list of nodes in a
block comment:

```c
/*
 * [...]
 * Nodes in dependency order (ordinal and path):
 *   0   /
 *   1   /aliases
 *   2   /chosen
 *   3   /flash@0
 *   4   /memory@20000000
 *          (etc.)
 * [...]
 */
```

Make note of the path to the node you want to find, like `/flash@0`. Search
for the node’s output in the file, which starts with something like this if the
node has a matching binding:

```c
/*
 * Devicetree node:
 *   /flash@0
 *
 * Binding (compatible = soc-nv-flash):
 *   $ZEPHYR_BASE/dts/bindings/mtd/soc-nv-flash.yaml
 * [...]
 */
```

See [Check for missing bindings](troubleshooting.md#missing-dt-binding) for troubleshooting.

## Set devicetree overlays

Devicetree overlays are explained in [Introduction to devicetree](intro.md#devicetree-intro). The CMake
variable **DTC\_OVERLAY\_FILE** contains a space- or semicolon-separated
list of overlay files to use. If **DTC\_OVERLAY\_FILE** specifies multiple
files, they are included in that order by the C preprocessor. A file in a
Zephyr module can be referred to by escaping the Zephyr module dir variable
like `\${ZEPHYR_<module>_MODULE_DIR}/<path-to>/dts.overlay`
when setting the DTC\_OVERLAY\_FILE variable.

You can set **DTC\_OVERLAY\_FILE** to contain exactly the files you want
to use. Here is an [example](../../develop/west/build-flash-debug.md#west-building-dtc-overlay-file) using
`west build`.

If you don’t set **DTC\_OVERLAY\_FILE**, the build system will follow
these steps, looking for files in your application configuration directory to
use as devicetree overlays:

1. If the file `socs/<SOC>_<BOARD_QUALIFIERS>.overlay` exists, it will be used.
2. If the file `boards/<BOARD>.overlay` exists, it will be used in addition to the above.
3. If the current board has [multiple revisions](../../hardware/porting/board_porting.md#porting-board-revisions)
   and `boards/<BOARD>_<revision>.overlay` exists, it will be used in addition to the above.
4. If one or more files have been found in the previous steps, the build system
   stops looking and just uses those files.
5. Otherwise, if `<BOARD>.overlay` exists, it will be used, and the build
   system will stop looking for more files.
6. Otherwise, if `app.overlay` exists, it will be used.

Extra devicetree overlays may be provided using `EXTRA_DTC_OVERLAY_FILE` which
will still allow the build system to automatically use devicetree overlays
described in the above steps.

The build system appends overlays specified in `EXTRA_DTC_OVERLAY_FILE`
to the overlays in `DTC_OVERLAY_FILE` when processing devicetree overlays.
This means that changes made via `EXTRA_DTC_OVERLAY_FILE` have higher
precedence than those made via `DTC_OVERLAY_FILE`.

All configuration files will be taken from the application’s configuration
directory except for files with an absolute path that are given with the
`DTC_OVERLAY_FILE` or `EXTRA_DTC_OVERLAY_FILE` argument.

See [Application Configuration Directory](../../develop/application/index.md#application-configuration-directory)
on how the application configuration directory is defined.

Using [Shields](../../hardware/porting/shields.md#shields) will also add devicetree overlay files.

The **DTC\_OVERLAY\_FILE** value is stored in the CMake cache and used
in successive builds.

The [build system](../index.md#build-overview) prints all the devicetree overlays it
finds in the configuration phase, like this:

```text
-- Found devicetree overlay: .../some/file.overlay
```

## Use devicetree overlays

See [Set devicetree overlays](#set-devicetree-overlays) for how to add an overlay to the build.

Overlays can override node property values in multiple ways.
For example, if your BOARD.dts contains this node:

```devicetree
/ {
        soc {
                serial0: serial@40002000 {
                        status = "okay";
                        current-speed = <115200>;
                        /* ... */
                };
        };
};
```

These are equivalent ways to override the `current-speed` value in an
overlay:

```text
/* Option 1 */
&serial0 {
     current-speed = <9600>;
};

/* Option 2 */
&{/soc/serial@40002000} {
     current-speed = <9600>;
};
```

We’ll use the `&serial0` style for the rest of these examples.

You can add aliases to your devicetree using overlays: an alias is just a
property of the `/aliases` node. For example:

```devicetree
/ {
     aliases {
             my-serial = &serial0;
     };
};
```

Chosen nodes work the same way. For example:

```devicetree
/ {
     chosen {
             zephyr,console = &serial0;
     };
};
```

To delete a property (in addition to deleting properties in general, this is
how to set a boolean property to false if it’s true in BOARD.dts):

```devicetree
&serial0 {
     /delete-property/ some-unwanted-property;
};
```

You can add subnodes using overlays. For example, to configure a SPI or I2C
child device on an existing bus node, do something like this:

```devicetree
/* SPI device example */
&spi1 {
     my_spi_device: temp-sensor@0 {
             compatible = "...";
             label = "TEMP_SENSOR_0";
             /* reg is the chip select number, if needed;
              * If present, it must match the node's unit address. */
             reg = <0>;

             /* Configure other SPI device properties as needed.
              * Find your device's DT binding for details. */
             spi-max-frequency = <4000000>;
     };
};

/* I2C device example */
&i2c2 {
     my_i2c_device: touchscreen@76 {
             compatible = "...";
             label = "TOUCHSCREEN";
             /* reg is the I2C device address.
              * It must match the node's unit address. */
             reg = <76>;

             /* Configure other I2C device properties as needed.
              * Find your device's DT binding for details. */
     };
};
```

Other bus devices can be configured similarly:

- create the device as a subnode of the parent bus
- set its properties according to its binding

Assuming you have a suitable device driver associated with the
`my_spi_device` and `my_i2c_device` compatibles, you should now be able to
enable the driver via Kconfig and [get the struct device](#dt-get-device)
for your newly added bus node, then use it with that driver API.

## Write device drivers using devicetree APIs

“Devicetree-aware” [device drivers](../../kernel/drivers/index.md#device-model-api) should create a
`struct device` for each `status = "okay"` devicetree node with a
particular [compatible](intro-syntax-structure.md#dt-important-props) (or related set of
compatibles) supported by the driver.

Writing a devicetree-aware driver begins by defining a [devicetree binding](bindings.md#dt-bindings) for the devices supported by the driver. Use existing bindings
from similar drivers as a starting point. A skeletal binding to get started
needs nothing more than this:

```yaml
description: <Human-readable description of your binding>
compatible: "foo-company,bar-device"
include: base.yaml
```

See [Find a devicetree binding](#dts-find-binding) for more advice on locating existing bindings.

After writing your binding, your driver C file can then use the devicetree API
to find `status = "okay"` nodes with the desired compatible, and instantiate
a `struct device` for each one. There are two options for instantiating each
`struct device`: using instance numbers, and using node labels.

In either case:

- Each `struct device`‘s name should be set to its devicetree node’s
  `label` property. This allows the driver’s users to [Get a struct device from a devicetree node](#dt-get-device) in
  the usual way.
- Each device’s initial configuration should use values from devicetree
  properties whenever practical. This allows users to configure the driver
  using [devicetree overlays](#use-dt-overlays).

Examples for how to do this follow. They assume you’ve already implemented the
device-specific configuration and data structures and API functions, like this:

```c
/* my_driver.c */
#include <zephyr/drivers/some_api.h>

/* Define data (RAM) and configuration (ROM) structures: */
struct my_dev_data {
     /* per-device values to store in RAM */
};
struct my_dev_cfg {
     uint32_t freq; /* Just an example: initial clock frequency in Hz */
     /* other configuration to store in ROM */
};

/* Implement driver API functions (drivers/some_api.h callbacks): */
static int my_driver_api_func1(const struct device *dev, uint32_t *foo) { /* ... */ }
static int my_driver_api_func2(const struct device *dev, uint64_t bar) { /* ... */ }
static struct some_api my_api_funcs = {
     .func1 = my_driver_api_func1,
     .func2 = my_driver_api_func2,
};
```

### Option 1: create devices using instance numbers

Use this option, which uses [Instance-based APIs](api/api.md#devicetree-inst-apis), if possible. However,
they only work when devicetree nodes for your driver’s `compatible` are all
equivalent, and you do not need to be able to distinguish between them.

To use instance-based APIs, begin by defining `DT_DRV_COMPAT` to the
lowercase-and-underscores version of the compatible that the device driver
supports. For example, if your driver’s compatible is `"vnd,my-device"` in
devicetree, you would define `DT_DRV_COMPAT` to `vnd_my_device` in your
driver C file:

```c
/*
 * Put this near the top of the file. After the includes is a good place.
 * (Note that you can therefore run "git grep DT_DRV_COMPAT drivers" in
 * the zephyr Git repository to look for example drivers using this style).
 */
#define DT_DRV_COMPAT vnd_my_device
```

Important

As shown, the DT\_DRV\_COMPAT macro should have neither quotes nor special
characters. Remove quotes and convert special characters to underscores
when creating `DT_DRV_COMPAT` from the compatible property.

Finally, define an instantiation macro, which creates each `struct device`
using instance numbers. Do this after defining `my_api_funcs`.

```c
/*
 * This instantiation macro is named "CREATE_MY_DEVICE".
 * Its "inst" argument is an arbitrary instance number.
 *
 * Put this near the end of the file, e.g. after defining "my_api_funcs".
 */
#define CREATE_MY_DEVICE(inst)                                       \
     static struct my_dev_data my_data_##inst = {                    \
             /* initialize RAM values as needed, e.g.: */            \
             .freq = DT_INST_PROP(inst, clock_frequency),            \
     };                                                              \
     static const struct my_dev_cfg my_cfg_##inst = {                \
             /* initialize ROM values as needed. */                  \
     };                                                              \
     DEVICE_DT_INST_DEFINE(inst,                                     \
                           my_dev_init_function,                     \
                           NULL,                                     \
                           &my_data_##inst,                          \
                           &my_cfg_##inst,                           \
                           MY_DEV_INIT_LEVEL, MY_DEV_INIT_PRIORITY,  \
                           &my_api_funcs);
```

Notice the use of APIs like [`DT_INST_PROP()`](api/api.md#c.DT_INST_PROP "DT_INST_PROP") and
[`DEVICE_DT_INST_DEFINE()`](../../kernel/drivers/index.md#c.DEVICE_DT_INST_DEFINE "DEVICE_DT_INST_DEFINE") to access devicetree node data. These
APIs retrieve data from the devicetree for instance number `inst` of
the node with compatible determined by `DT_DRV_COMPAT`.

Finally, pass the instantiation macro to [`DT_INST_FOREACH_STATUS_OKAY()`](api/api.md#c.DT_INST_FOREACH_STATUS_OKAY "DT_INST_FOREACH_STATUS_OKAY"):

```c
/* Call the device creation macro for each instance: */
DT_INST_FOREACH_STATUS_OKAY(CREATE_MY_DEVICE)
```

`DT_INST_FOREACH_STATUS_OKAY` expands to code which calls
`CREATE_MY_DEVICE` once for each enabled node with the compatible determined
by `DT_DRV_COMPAT`. It does not append a semicolon to the end of the
expansion of `CREATE_MY_DEVICE`, so the macro’s expansion must end in a
semicolon or function definition to support multiple devices.

### Option 2: create devices using node labels

Some device drivers cannot use instance numbers. One example is an SoC
peripheral driver which relies on vendor HAL APIs specialized for individual IP
blocks to implement Zephyr driver callbacks. Cases like this should use
[`DT_NODELABEL()`](api/api.md#c.DT_NODELABEL "DT_NODELABEL") to refer to individual nodes in the devicetree
representing the supported peripherals on the SoC. The devicetree.h
[Generic APIs](api/api.md#devicetree-generic-apis) can then be used to access node data.

For this to work, your [SoC’s dtsi file](intro-input-output.md#dt-input-files) must define node
labels like `mydevice0`, `mydevice1`, etc. appropriately for the IP blocks
your driver supports. The resulting devicetree usually looks something like
this:

```devicetree
/ {
        soc {
                mydevice0: dev@0 {
                        compatible = "vnd,my-device";
                };
                mydevice1: dev@1 {
                        compatible = "vnd,my-device";
                };
        };
};
```

The driver can use the `mydevice0` and `mydevice1` node labels in the
devicetree to operate on specific device nodes:

```c
/*
 * This is a convenience macro for creating a node identifier for
 * the relevant devices. An example use is MYDEV(0) to refer to
 * the node with label "mydevice0".
 */
#define MYDEV(idx) DT_NODELABEL(mydevice ## idx)

/*
 * Define your instantiation macro; "idx" is a number like 0 for mydevice0
 * or 1 for mydevice1. It uses MYDEV() to create the node label from the
 * index.
 */
#define CREATE_MY_DEVICE(idx)                                        \
     static struct my_dev_data my_data_##idx = {                     \
             /* initialize RAM values as needed, e.g.: */            \
             .freq = DT_PROP(MYDEV(idx), clock_frequency),           \
     };                                                              \
     static const struct my_dev_cfg my_cfg_##idx = { /* ... */ };    \
     DEVICE_DT_DEFINE(MYDEV(idx),                                    \
                     my_dev_init_function,                           \
                     NULL,                                           \
                     &my_data_##idx,                                 \
                     &my_cfg_##idx,                                  \
                     MY_DEV_INIT_LEVEL, MY_DEV_INIT_PRIORITY,        \
                     &my_api_funcs)
```

Notice the use of APIs like [`DT_PROP()`](api/api.md#c.DT_PROP "DT_PROP") and
[`DEVICE_DT_DEFINE()`](../../kernel/drivers/index.md#c.DEVICE_DT_DEFINE "DEVICE_DT_DEFINE") to access devicetree node data.

Finally, manually detect each enabled devicetree node and use
`CREATE_MY_DEVICE` to instantiate each `struct device`:

```c
#if DT_NODE_HAS_STATUS(DT_NODELABEL(mydevice0), okay)
CREATE_MY_DEVICE(0)
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(mydevice1), okay)
CREATE_MY_DEVICE(1)
#endif
```

Since this style does not use `DT_INST_FOREACH_STATUS_OKAY()`, the driver
author is responsible for calling `CREATE_MY_DEVICE()` for every possible
node, e.g. using knowledge about the peripherals available on supported SoCs.

## Device drivers that depend on other devices

At times, one `struct device` depends on another `struct device` and
requires a pointer to it. For example, a sensor device might need a pointer to
its SPI bus controller device. Some advice:

- Write your devicetree binding in a way that permits use of
  [Hardware specific APIs](api/api.md#devicetree-hw-api) from devicetree.h if possible.
- In particular, for bus devices, your driver’s binding should include a
  file like [dts/bindings/spi/spi-device.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/spi/spi-device.yaml) which provides
  common definitions for devices addressable via a specific bus. This enables
  use of APIs like [`DT_BUS()`](api/api.md#c.DT_BUS "DT_BUS") to obtain a node identifier for the bus
  node. You can then [Get a struct device from a devicetree node](#dt-get-device) for the bus in the usual way.

Search existing bindings and device drivers for examples.

## Applications that depend on board-specific devices

One way to allow application code to run unmodified on multiple boards is by
supporting a devicetree alias to specify the hardware specific portions, as is
done in the [Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample. The application can then be configured in
[BOARD.dts](intro-input-output.md#devicetree-in-out-files) files or via [devicetree
overlays](#use-dt-overlays).
