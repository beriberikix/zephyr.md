---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/pinctrl/nuvoton,npcx-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/nuvoton,npcx-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nuvoton,npcx-pinctrl

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

## Description

```text
The Nuvoton pin controller is a singleton node responsible for controlling
pin function selection and pin properties. For example, you can use these
nodes to select peripheral pin functions.

Here is a list of supported standard pin properties:
  - bias-pull-down: Enable pull-down resistor.
  - bias-pull-up: Enable pull-up resistor.
  - drive-open-drain: Output driver is open-drain.

Custom pin properties for npcx series are available also:
  - pinmux-locked: Lock pinmux configuration for peripheral device
  - pinmux-gpio: Inverse pinmux back to gpio
  - psl-in-mode: Select the assertion detection mode of PSL input
  - psl-in-pol: Select the assertion detection polarity of PSL input

An example for NPCX7 family, include the chip level pinctrl DTSI file in the
board level DTS:

  #include <nuvoton/npcx/npcx7/npcx7-pinctrl.dtsi>

We want to use the I2C0_0 port of the NPCX7M6FB controller and enable the
internal 3.3V pull-up if its i2c frequency won't exceed 400kHz.

To change a pin's pinctrl default properties, add a reference to the
pin in the board's DTS file and set the properties as below:

  &i2c0_0_sda_scl_gpb4_b5 {
    bias-pull-up; /* Enable internal pull-up for i2c0_0 */
    pinmux-locked; /* Lock pinmuxing */
  };

  &i2c0_0 {
    pinctrl-0 = <&i2c0_0_sda_scl_gpb4_b5>;
    pinctrl-names = "default";
  }
```

## Properties

### Top level properties

These property descriptions apply to “nuvoton,npcx-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,npcx-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `pinmux` | `phandle` | ```text Configurations of pinmux selection ``` |
| `dev-ctl` | `array` | ```text Configurations of device control such as tri-state, io type and so on. ``` |
| `periph-pupd` | `array` | ```text A map to PUPD_ENn register/bit that enable pull-up/down of NPCX peripheral devices. Please don't overwrite this property in the board-level DT driver. ``` |
| `psl-offset` | `int` | ```text Offset to PSL_CTS register that is used for PSL input's status and detection mode. Please don't overwrite this property in the board-level DT driver. ``` |
| `psl-polarity` | `phandle` | ```text A map to DEVALTn that configures detection polarity of PSL input pads. Please don't overwrite this property in the board-level DT driver. ``` |
| `pinmux-locked` | `boolean` | ```text Lock pinmux selection ``` |
| `pinmux-gpio` | `boolean` | ```text Inverse pinmux selection to GPIO ``` |
| `psl-in-mode` | `string` | ```text The assertion detection mode of PSL input selection - "level": Select the detection mode to level detection - "edge": Select the detection mode to edge detection ```  Legal values: `'level'`, `'edge'` |
| `psl-in-pol` | `string` | ```text The assertion detection polarity of PSL input selection - "low-falling": Select the detection polarity to low/falling - "high-rising": Select the detection polarity to high/rising ```  Legal values: `'low-falling'`, `'high-rising'` |
