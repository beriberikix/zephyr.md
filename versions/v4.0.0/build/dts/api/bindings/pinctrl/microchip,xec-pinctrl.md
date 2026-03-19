---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/microchip,xec-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/microchip,xec-pinctrl.html
---

# microchip,xec-pinctrl

Vendor: [Microchip Technology Inc.](../../bindings.md#dt-vendor-microchip)

Note

An implementation of a driver matching this compatible is available in
[drivers/pinctrl/pinctrl\_mchp\_xec.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_mchp_xec.c).

## Description

```text
Microchip XEC Pin controller Node
Based on pincfg-node.yaml binding.
The MCHP XEC pin controller is a singleton node responsible for controlling
pin function selection and pin properties. For example, you can use this
node to select peripheral pin functions.

The node has the 'pinctrl' node label set in your SoC's devicetree,
so you can modify it like this:

  &pinctrl {
          /* your modifications go here */
  };

All device pin configurations should be placed in child nodes of the
'pinctrl' node, as in the spi0 example shown at the end:

A group can also specify shared pin properties common to all the specified
pins, such as the 'bias-pull-up' property in group 2. Here is a list of
supported standard pin properties:

- bias-disable: Disable pull-up/down (default behavior, not required).
- bias-pull-down: Enable pull-down resistor.
- bias-pull-up: Enable pull-up resistor.
- drive-push-pull: Output driver is push-pull (default, not required).
- drive-open-drain: Output driver is open-drain.
- output-high: Set output state high when pin configured.
- output-low: Set output state low when pin configured.

Custom pin properties for drive strength and slew rate are available:
- drive-strength
- slew-rate

Driver strength and slew rate hardware defaults vary by SoC and pin.

An example for MEC172x family, include the chip level pinctrl
DTSI file in the board level DTS:

  #include <microchip/mec172x/mec172xnsz-pinctrl.dtsi>

We want to use the shared SPI port of the MEC172x QMSPI controller
and want the chip select 0 to be open-drain.

To change a pin's pinctrl default properties add a reference to the
pin in the board's DTS file and set the properties.

  &spi0 {
    pinctrl-0 = < &shd_cs0_n_gpio055
                  &shd_clk_gpio056
                  &shd_io0_gpio223
                  &shd_io1_gpio224
                  &shd_io3_gpio016 >;
    pinctrl-names = "default";
  }

  &shd_cs0_n_gpio055 {
    drive-open-drain;
  };
```

## Properties

### Top level properties

These property descriptions apply to “microchip,xec-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “microchip,xec-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `pinmux` | `int` | ```text Pinmux selection ```  This property is **required**. |
| `slew-rate` | `string` | ```text Pin speed. The default value of slew-rate is the SoC power-on-reset value. Please refer to the data sheet as a small number of pins may have a different default and some pins do not implement slew rate adjustment. ```  Default value: `no-change`  Legal values: `'no-change'`, `'low-speed'`, `'high-speed'` |
| `drive-strength` | `string` | ```text Pin output drive strength for PIO and PIO-24 pin types. Default is "1x" for most pins. PIO pins are 2, 4, 8, or 12 mA. PIO-24 pins are 4, 8, 16, or 24 mA. Please refer to the data sheet for each pin's PIO type and default drive strength. ```  Default value: `no-change`  Legal values: `'no-change'`, `'1x'`, `'2x'`, `'4x'`, `'6x'` |
| `microchip,output-func-invert` | `boolean` | ```text Invert polarity of an output alternate function. Input functions are not affected. ``` |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `low-power-enable` | `boolean` | ```text enable low power mode ``` |
| `output-disable` | `boolean` | ```text disable output on a pin (e.g. disable an output buffer) ``` |
| `output-enable` | `boolean` | ```text enable output on a pin without actively driving it (e.g. enable an output buffer) ``` |
| `output-low` | `boolean` | ```text set the pin to output mode with low level ``` |
| `output-high` | `boolean` | ```text set the pin to output mode with high level ``` |
