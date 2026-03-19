---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/ene,kb1200-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/ene,kb1200-pinctrl.html
---

# ene,kb1200-pinctrl

Vendor: [ENE Technology, Inc.](../../bindings.md#dt-vendor-ene)

Note

An implementation of a driver matching this compatible is available in
[drivers/pinctrl/pinctrl\_ene\_kb1200.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_ene_kb1200.c).

## Description

```text
The ENE KB1200 pin controller is a singleton node responsible for controlling
pin function selection and pin properties. For example, you can use these
nodes to select peripheral pin functions.

Here is a list of supported standard pin properties:
  - bias-disable: Disable pull-up/down resistor.
  - bias-pull-up: Enable pull-up resistor.
  - bias-pull-down: Enable pull-down resistor.
  - drive-push-pull: Output driver is push-pull.
  - drive-open-drain: Output driver is open-drain.
  - output-disable: Disable GPIO output driver data
  - output-enable: Ensable GPIO output driver data
  - output-high: GPIO output data high
  - output-low: GPIO output data low
  - low-power-enable: Support input data ViH/ViL with low vlotage range(ex. 1.8V domain)

Here is a list of support pinmux type:
  - PINMUX_FUNC_A : GPIO        Function
  - PINMUX_FUNC_B : AltOutput 1 Function
  - PINMUX_FUNC_C : AltOutput 2 Function
  - PINMUX_FUNC_D : AltOutput 3 Function
  - PINMUX_FUNC_E : AltOutput 4 Function
  (Note. Alt-input function does not need to set pinmux type other than PINMUX_FUNC_A)

An example for KB1200, include the chip level pinctrl DTSI file in the
board level DTS:

  #include <ene_kb1200/ene_kb1200-pinctrl.dtsi>

We want to use the I2C0_0 port of the KB1200 controller and enable the
internal 3.3V pull-up if its i2c frequency won't exceed 400kHz. And we
need to set I2C0_0 pinmux type as PINMUX_FUNC_B (the alt-output 1
function) not a GPIO.

To change a pin's pinctrl default properties, add a reference to the
pin in the board's DTS file and set the properties as below:

  &i2c0_0 {
    pinctrl-0 = <&i2c0_clk_gpio2c &i2c0_dat_gpio2d>;
    pinctrl-names = "default";
  }

  /omit-if-no-ref/ i2c0_clk_gpio2c: i2c0_clk_gpio2c {
    pinmux = <ENE_KB1200_PINMUX(0x2C, PINMUX_FUNC_B)>;
    bias-pull-up;
  };
  /omit-if-no-ref/ i2c0_dat_gpio2d: i2c0_dat_gpio2d {
    pinmux = <ENE_KB1200_PINMUX(0x2D, PINMUX_FUNC_B)>;
    bias-pull-up;
  };
```

## Properties

### Top level properties

These property descriptions apply to “ene,kb1200-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ene,kb1200-pinctrl” compatible.

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
