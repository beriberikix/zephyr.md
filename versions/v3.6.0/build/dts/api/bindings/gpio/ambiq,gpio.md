---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/gpio/ambiq,gpio.html
original_path: build/dts/api/bindings/gpio/ambiq,gpio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ambiq,gpio

Vendor: [Ambiq Micro, Inc.](../../bindings.md#dt-vendor-ambiq)

## Description

```text
Ambiq GPIO provides the GPIO pin mapping for GPIO child nodes.

The Ambiq Apollo4x soc designs a single GPIO port with 128 pins.
It uses 128 continuous 32-bit registers to configure the GPIO pins.
This binding provides a pin mapping to solve the limitation of the maximum
32 pins handling in GPIO driver API.

The Ambiq Apollo4x soc should define one "ambiq,gpio" parent node in soc
devicetree and some child nodes which are compatible with "ambiq,gpio-bank"
under this parent node.

Here is an example of how a "ambiq,gpio" node can be used with the combined
gpio child nodes:

gpio: gpio@40010000 {
  compatible = "ambiq,gpio";
  gpio-map-mask = <0xffffffe0 0xffffffc0>;
  gpio-map-pass-thru = <0x1f 0x3f>;
  gpio-map = <
    0x00 0x0 &gpio0_31 0x0 0x0
    0x20 0x0 &gpio32_63 0x0 0x0
    0x40 0x0 &gpio64_95 0x0 0x0
    0x60 0x0 &gpio96_127 0x0 0x0
  >;
  reg = <0x40010000>;
  #gpio-cells = <2>;
  #address-cells = <1>;
  #size-cells = <0>;
  ranges;

  gpio0_31: gpio0_31@0 {
    compatible = "ambiq,gpio-bank";
    gpio-controller;
    #gpio-cells = <2>;
    reg = <0>;
    interrupts = <56 0>;
    status = "disabled";
  };

  gpio32_63: gpio32_63@80 {
    compatible = "ambiq,gpio-bank";
    gpio-controller;
    #gpio-cells = <2>;
    reg = <0x80>;
    interrupts = <57 0>;
    status = "disabled";
  };

  gpio64_95: gpio64_95@100 {
    compatible = "ambiq,gpio-bank";
    gpio-controller;
    #gpio-cells = <2>;
    reg = <0x100>;
    interrupts = <58 0>;
    status = "disabled";
  };

  gpio96_127: gpio96_127@180 {
    compatible = "ambiq,gpio-bank";
    gpio-controller;
    #gpio-cells = <2>;
    reg = <0x180>;
    interrupts = <59 0>;
    status = "disabled";
  };
};

In the above example, the gpio@40010000 is a "ambiq,gpio" parent node which
provides the base register address 0x40010000. It has four "ambiq,gpio-bank"
child nodes. Each of them covers 32 pins (the default value of "ngpios"
property is 32). The "reg" property of child nodes defines the register
address offset. The register address of pin described in gpio-cells can be
obtained by: base address + child address offset + (pin << 2). For example:
the address of pin 20 of gpio32_63@80 node is (0x40010000 + 0x80 + (20 << 2))
= 0x400100D0 and the real GPIO pin number of this pin in soc is (20 + 32)
= 52.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `gpio-map` | `compound` | This property is **required**. |
| `gpio-map-mask` | `compound` |  |
| `gpio-map-pass-thru` | `compound` |  |
| `#gpio-cells` | `int` | ```text Number of items to expect in a GPIO specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ambiq,gpio” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
