---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/pinctrl/adi,max32-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/adi,max32-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# adi,max32-pinctrl

Vendor: [Analog Devices, Inc.](../../bindings.md#dt-vendor-adi)

## Description

```text
MAX32 Pin controller Node
Based on pincfg-node.yaml binding.

Note: `bias-disable`  are default pin configurations.
```

## Properties

### Top level properties

These property descriptions apply to “adi,max32-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,max32-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-strength` | `int` | ```text There are 4 drive strength mode. Mode 0: 1mA Mode 1: 2mA Mode 2: 4mA Mode 3: 8mA Default GPIO output drive strength is mode 0 for MAX32 MCUs. For more information please take a look device user guide, datasheet. ```  Legal values: `0`, `1`, `2`, `3` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `power-source` | `int` | ```text GPIO Supply Voltage Select, Selects the voltage rail used for the pin. 0 or MAX32_VSEL_VDDIO 1 or MAX32_VSEL_VDDIOH ```  Legal values: `0`, `1` |
| `output-enable` | `boolean` | ```text enable output on a pin without actively driving it (e.g. enable an output buffer) ``` |
| `output-low` | `boolean` | ```text set the pin to output mode with low level ``` |
| `output-high` | `boolean` | ```text set the pin to output mode with high level ``` |
| `pinmux` | `int` | ```text Integer array, represents gpio pin number and mux setting. These defines are calculated as: (pin<<8 | port<<4 | function<<0) With: - port: The gpio port index (0, 1, ...) - pin: The pin offset within the port (0, 1, 2, ...) - function: The function number, can be: * 0 : GPIO * 1 : Alternate Function 1 * 2 : Alternate Function 2 * 3 : Alternate Function 3 * 4 : Alternate Function 4 In case selected pin function is GPIO, pin is statically configured as a plain input/output GPIO. Default configuration is input. Output value can be configured by adding 'ouptut-low' or 'output-high' properties to the pin configuration.  To simplify the usage, macro is available to generate "pinmux" field. This macro is available here:   -include/zephyr/dt-bindings/pinctrl/max32-pinctrl.h Some examples of macro usage: P0.9 set as alernate function 1 {   pinmux = <MAX32_PINMUX(0, 9, AF1)>; }; P0.9 set as alernate function 2 {   pinmux = <MAX32_PINMUX(0, 9, AF2)>; }; P0.9 set as GPIO output high {   pinmux = <MAX32_PINMUX(0, 9, GPIO)>;   output-high; }; ```  This property is **required**. |
