---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/api.html
original_path: build/dts/api/api.html
---

# Devicetree API

This is a reference page for the `<zephyr/devicetree.h>` API. The API is macro
based. Use of these macros has no impact on scheduling. They can be used from
any calling context and at file scope.

Some of these – the ones beginning with `DT_INST_` – require a special
macro named `DT_DRV_COMPAT` to be defined before they can be used; these are
discussed individually below. These macros are generally meant for use within
[device drivers](../../../kernel/drivers/index.md#device-model-api), though they can be used outside of
drivers with appropriate care.

## [Generic APIs](#id3)

The APIs in this section can be used anywhere and do not require
`DT_DRV_COMPAT` to be defined.

### [Node identifiers and helpers](#id4)

A *node identifier* is a way to refer to a devicetree node at C preprocessor
time. While node identifiers are not C values, you can use them to access
devicetree data in C rvalue form using, for example, the
[Property access](#devicetree-property-access) API.

The root node `/` has node identifier `DT_ROOT`. You can create node
identifiers for other devicetree nodes using [`DT_PATH()`](../../../doxygen/html/group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086),
[`DT_NODELABEL()`](../../../doxygen/html/group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79), [`DT_ALIAS()`](../../../doxygen/html/group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9), and [`DT_INST()`](../../../doxygen/html/group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead).

There are also [`DT_PARENT()`](../../../doxygen/html/group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b) and [`DT_CHILD()`](../../../doxygen/html/group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e) macros which can be
used to create node identifiers for a given node’s parent node or a particular
child node, respectively.

The following macros create or operate on node identifiers.

[Node identifiers and helpers](../../../doxygen/html/group__devicetree-generic-id.md)

Related code samples

- [GPIO with custom Devicetree binding](../../../samples/basic/custom_dts_binding/README.md#gpio-custom-dts-binding "Use custom Devicetree binding to control a GPIO.")Use custom Devicetree binding to control a GPIO.

### [Property access](#id5)

The following general-purpose macros can be used to access node properties.
There are special-purpose APIs for accessing the [ranges property](#devicetree-ranges-property),
[reg property](#devicetree-reg-property) and [interrupts property](#devicetree-interrupts-property).

Property values can be read using these macros even if the node is disabled,
as long as it has a matching binding.

[Property accessors](../../../doxygen/html/group__devicetree-generic-prop.md)

### [`ranges` property](#id6)

Use these APIs instead of [Property access](#devicetree-property-access) to access the
`ranges` property. Because this property’s semantics are defined by the
devicetree specification, these macros can be used even for nodes without
matching bindings. However, they take on special semantics when the node’s
binding indicates it is a PCIe bus node, as defined in the
[PCI Bus Binding to: IEEE Std 1275-1994 Standard for Boot (Initialization Configuration) Firmware](https://www.openfirmware.info/data/docs/bus.pci.pdf)

[ranges property](../../../doxygen/html/group__devicetree-ranges-prop.md)

### [`reg` property](#id7)

Use these APIs instead of [Property access](#devicetree-property-access) to access the
`reg` property. Because this property’s semantics are defined by the
devicetree specification, these macros can be used even for nodes without
matching bindings.

[reg property](../../../doxygen/html/group__devicetree-reg-prop.md)

### [`interrupts` property](#id8)

Use these APIs instead of [Property access](#devicetree-property-access) to access the
`interrupts` property.

Because this property’s semantics are defined by the devicetree specification,
some of these macros can be used even for nodes without matching bindings. This
does not apply to macros which take cell names as arguments.

[interrupts property](../../../doxygen/html/group__devicetree-interrupts-prop.md)

### [For-each macros](#id9)

There is currently only one “generic” for-each macro,
[`DT_FOREACH_CHILD()`](../../../doxygen/html/group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f), which allows iterating over the children of a
devicetree node.

There are special-purpose for-each macros, like
[`DT_INST_FOREACH_STATUS_OKAY()`](../../../doxygen/html/group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7), but these require `DT_DRV_COMPAT` to
be defined before use.

["For-each" macros](../../../doxygen/html/group__devicetree-generic-foreach.md)

### [Existence checks](#id10)

This section documents miscellaneous macros that can be used to test if a node
exists, how many nodes of a certain type exist, whether a node has certain
properties, etc. Some macros used for special purposes (such as
[`DT_IRQ_HAS_IDX()`](../../../doxygen/html/group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c) and all macros which require `DT_DRV_COMPAT`) are
documented elsewhere on this page.

[Existence checks](../../../doxygen/html/group__devicetree-generic-exist.md)

Related code samples

- [GPIO with custom Devicetree binding](../../../samples/basic/custom_dts_binding/README.md#gpio-custom-dts-binding "Use custom Devicetree binding to control a GPIO.")Use custom Devicetree binding to control a GPIO.

### [Inter-node dependencies](#id11)

The `devicetree.h` API has some support for tracking dependencies between
nodes. Dependency tracking relies on a binary “depends on” relation between
devicetree nodes, which is defined as the [transitive closure](https://en.wikipedia.org/wiki/Transitive_closure) of the following “directly
depends on” relation:

- every non-root node directly depends on its parent node
- a node directly depends on any nodes its properties refer to by phandle
- a node directly depends on its `interrupt-parent` if it has an
  `interrupts` property
- a parent node inherits all dependencies from its child nodes

A *dependency ordering* of a devicetree is a list of its nodes, where each node
`n` appears earlier in the list than any nodes that depend on `n`. A node’s
*dependency ordinal* is then its zero-based index in that list. Thus, for two
distinct devicetree nodes `n1` and `n2` with dependency ordinals `d1` and
`d2`, we have:

- `d1 != d2`
- if `n1` depends on `n2`, then `d1 > d2`
- `d1 > d2` does **not** necessarily imply that `n1` depends on `n2`

The Zephyr build system chooses a dependency ordering of the final devicetree
and assigns a dependency ordinal to each node. Dependency related information
can be accessed using the following macros. The exact dependency ordering
chosen is an implementation detail, but cyclic dependencies are detected and
cause errors, so it’s safe to assume there are none when using these macros.

There are instance number-based conveniences as well; see
[`DT_INST_DEP_ORD()`](../../../doxygen/html/group__devicetree-dep-ord.md#ga9c5e6f36c6e7a250368177a9f0713f86) and subsequent documentation.

[Dependency tracking](../../../doxygen/html/group__devicetree-dep-ord.md)

### [Bus helpers](#id12)

Zephyr’s devicetree bindings language supports a `bus:` key which allows
bindings to declare that nodes with a given compatible describe system buses.
In this case, child nodes are considered to be on a bus of the given type, and
the following APIs may be used.

[Bus helpers](../../../doxygen/html/group__devicetree-generic-bus.md)

## [Instance-based APIs](#id13)

These are recommended for use within device drivers. To use them, define
`DT_DRV_COMPAT` to the lowercase-and-underscores compatible the device driver
implements support for. Here is an example devicetree fragment:

```devicetree
serial@40001000 {
        compatible = "vnd,serial";
        status = "okay";
        current-speed = <115200>;
};
```

Example usage, assuming `serial@40001000` is the only enabled node
with compatible `vnd,serial`:

```c
#define DT_DRV_COMPAT vnd_serial
DT_DRV_INST(0)                  // node identifier for serial@40001000
DT_INST_PROP(0, current_speed)  // 115200
```

Warning

Be careful making assumptions about instance numbers. See [`DT_INST()`](../../../doxygen/html/group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)
for the API guarantees.

As shown above, the `DT_INST_*` APIs are conveniences for addressing nodes by
instance number. They are almost all defined in terms of one of the
[Generic APIs](#devicetree-generic-apis). The equivalent generic API can be found by
removing `INST_` from the macro name. For example, `DT_INST_PROP(inst,
prop)` is equivalent to `DT_PROP(DT_DRV_INST(inst), prop)`. Similarly,
`DT_INST_REG_ADDR(inst)` is equivalent to `DT_REG_ADDR(DT_DRV_INST(inst))`,
and so on. There are some exceptions: [`DT_ANY_INST_ON_BUS_STATUS_OKAY()`](../../../doxygen/html/group__devicetree-inst.md#gaa4ff1fe4242399fbd667fbee7e98040a)
and [`DT_INST_FOREACH_STATUS_OKAY()`](../../../doxygen/html/group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7) are special-purpose helpers without
straightforward generic equivalents.

Since `DT_DRV_INST()` requires `DT_DRV_COMPAT` to be defined, it’s an error
to use any of these without that macro defined.

Note that there are also helpers available for
specific hardware; these are documented in [Hardware specific APIs](#devicetree-hw-api).

[Instance-based devicetree APIs](../../../doxygen/html/group__devicetree-inst.md)

## [Hardware specific APIs](#id14)

The following APIs can also be used by including `<devicetree.h>`;
no additional include is needed.

### [CAN](#id15)

These conveniences may be used for nodes which describe CAN
controllers/transceivers, and properties related to them.

[Devicetree CAN API](../../../doxygen/html/group__devicetree-can.md)

### [Clocks](#id16)

These conveniences may be used for nodes which describe clock sources, and
properties related to them.

[Devicetree Clocks API](../../../doxygen/html/group__devicetree-clocks.md)

### [DMA](#id17)

These conveniences may be used for nodes which describe direct memory access
controllers or channels, and properties related to them.

[Devicetree DMA API](../../../doxygen/html/group__devicetree-dmas.md)

### [Fixed flash partitions](#id18)

These conveniences may be used for the special-purpose `fixed-partitions`
compatible used to encode information about flash memory partitions in the
device tree. See See `fixed-partition` for more details.

[Devicetree Fixed Partition API](../../../doxygen/html/group__devicetree-fixed-partition.md)

### [GPIO](#id19)

These conveniences may be used for nodes which describe GPIO controllers/pins,
and properties related to them.

[Devicetree GPIO API](../../../doxygen/html/group__devicetree-gpio.md)

### [IO channels](#id20)

These are commonly used by device drivers which need to use IO
channels (e.g. ADC or DAC channels) for conversion.

[Devicetree IO Channels API](../../../doxygen/html/group__devicetree-io-channels.md)

### [MBOX](#id21)

These conveniences may be used for nodes which describe MBOX controllers/users,
and properties related to them.

[Devicetree MBOX API](../../../doxygen/html/group__devicetree-mbox.md)

### [Pinctrl (pin control)](#id22)

These are used to access pin control properties by name or index.

Devicetree nodes may have properties which specify pin control (sometimes known
as pin mux) settings. These are expressed using `pinctrl-<index>` properties
within the node, where the `<index>` values are contiguous integers starting
from 0. These may also be named using the `pinctrl-names` property.

Here is an example:

```dts
node {
    ...
    pinctrl-0 = <&foo &bar ...>;
    pinctrl-1 = <&baz ...>;
    pinctrl-names = "default", "sleep";
};
```

Above, `pinctrl-0` has name `"default"`, and `pinctrl-1` has name
`"sleep"`. The `pinctrl-<index>` property values contain phandles. The
`&foo`, `&bar`, etc. phandles within the properties point to nodes whose
contents vary by platform, and which describe a pin configuration for the node.

[Pin control](../../../doxygen/html/group__devicetree-pinctrl.md)

### [PWM](#id23)

These conveniences may be used for nodes which describe PWM controllers and
properties related to them.

[Devicetree PWMs API](../../../doxygen/html/group__devicetree-pwms.md)

### [Reset Controller](#id24)

These conveniences may be used for nodes which describe reset controllers and
properties related to them.

[Devicetree Reset Controller API](../../../doxygen/html/group__devicetree-reset-controller.md)

### [SPI](#id25)

These conveniences may be used for nodes which describe either SPI controllers
or devices, depending on the case.

[Devicetree SPI API](../../../doxygen/html/group__devicetree-spi.md)

## [Chosen nodes](#id26)

The special `/chosen` node contains properties whose values describe
system-wide settings. The [`DT_CHOSEN()`](../../../doxygen/html/group__devicetree-generic-chosen.md#ga3412d0acecffa828984cf9e2c89889ed) macro can be used to get a node
identifier for a chosen node.

[Chosen nodes](../../../doxygen/html/group__devicetree-generic-chosen.md)

## [Zephyr-specific chosen nodes](#id27)

The following table documents some commonly used Zephyr-specific chosen nodes.

Sometimes, a chosen node’s label property will be used to set the default value
of a Kconfig option which in turn configures a hardware-specific device. This
is usually for backwards compatibility in cases when the Kconfig option
predates devicetree support in Zephyr. In other cases, there is no Kconfig
option, and the devicetree node is used directly in the source code to select a
device.

Zephyr-specific chosen properties

| Property | Purpose |
| --- | --- |
| zephyr,bt-c2h-uart | Selects the UART used for host communication in the [HCI UART](../../../samples/bluetooth/hci_uart/README.md#bluetooth_hci_uart "Expose a Bluetooth controller to another device or CPU over UART.") |
| zephyr,bt-mon-uart | Sets UART device used for the Bluetooth monitor logging |
| zephyr,bt-hci | Selects the HCI device used by the Bluetooth host stack |
| zephyr,canbus | Sets the default CAN controller |
| zephyr,ccm | Core-Coupled Memory node on some STM32 SoCs |
| zephyr,code-partition | Flash partition that the Zephyr image’s text section should be linked into |
| zephyr,console | Sets UART device used by console driver |
| zephyr,display | Sets the default display controller |
| zephyr,keyboard-scan | Sets the default keyboard scan controller |
| zephyr,dtcm | Data Tightly Coupled Memory node on some Arm SoCs |
| zephyr,entropy | A device which can be used as a system-wide entropy source |
| zephyr,flash | A node whose `reg` is sometimes used to set the defaults for [`CONFIG_FLASH_BASE_ADDRESS`](../../../kconfig.md#CONFIG_FLASH_BASE_ADDRESS "CONFIG_FLASH_BASE_ADDRESS") and [`CONFIG_FLASH_SIZE`](../../../kconfig.md#CONFIG_FLASH_SIZE "CONFIG_FLASH_SIZE") |
| zephyr,flash-controller | The node corresponding to the flash controller device for the `zephyr,flash` node |
| zephyr,gdbstub-uart | Sets UART device used by the [GDB stub](../../../services/debugging/gdbstub.md#gdbstub) subsystem |
| zephyr,ieee802154 | Used by the networking subsystem to set the IEEE 802.15.4 device |
| zephyr,ipc | Used by the OpenAMP subsystem to specify the inter-process communication (IPC) device |
| zephyr,ipc\_shm | A node whose `reg` is used by the OpenAMP subsystem to determine the base address and size of the shared memory (SHM) usable for interprocess-communication (IPC) |
| zephyr,itcm | Instruction Tightly Coupled Memory node on some Arm SoCs |
| zephyr,log-uart | Sets the UART device(s) used by the logging subsystem’s UART backend. If defined, the UART log backend would output to the devices listed in this node. |
| zephyr,ocm | On-chip memory node on Xilinx Zynq-7000 and ZynqMP SoCs |
| zephyr,osdp-uart | Sets UART device used by OSDP subsystem |
| zephyr,ot-uart | Used by the OpenThread to specify UART device for Spinel protocol |
| zephyr,pcie-controller | The node corresponding to the PCIe Controller |
| zephyr,ppp-uart | Sets UART device used by PPP |
| zephyr,settings-partition | Fixed partition node. If defined this selects the partition used by the NVS and FCB settings backends. |
| zephyr,shell-uart | Sets UART device used by serial shell backend |
| zephyr,sram | A node whose `reg` sets the base address and size of SRAM memory available to the Zephyr image, used during linking |
| zephyr,tracing-uart | Sets UART device used by tracing subsystem |
| zephyr,uart-mcumgr | UART used for [Device Management](../../../services/device_mgmt/index.md#device-mgmt) |
| zephyr,uart-pipe | Sets UART device used by serial pipe driver |
| zephyr,usb-device | USB device node. If defined and has a `vbus-gpios` property, these will be used by the USB subsystem to enable/disable VBUS |
| zephyr,led-strip | A LED-strip node which is used to determine the timings of the WS2812 GPIO driver |
| zephyr,touch | touchscreen controller device node. |
