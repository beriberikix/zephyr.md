---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/pinctrl/st,stm32-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/st,stm32-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32-pinctrl

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 Pin controller Node
Based on pincfg-node.yaml binding.

Note: `bias-disable` and `drive-push-pull` are default pin configurations.
       They will be applied in case no `bias-foo` or `driver-bar` properties
       are set.
```

## Properties

### Top level properties

These property descriptions apply to “st,stm32-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `remap-pa11` | `boolean` | ```text Remaps the PA11 pin to operate as PA9 pin. Use of this property is restricted to STM32G0 and STM32C0 SoCs. ``` |
| `remap-pa12` | `boolean` | ```text Remaps the PA12 pin to operate as PA10 pin. Use of this property is restricted to STM32G0 and STM32C0 SoCs. ``` |
| `remap-pa11-pa12` | `boolean` | ```text Remaps the PA11/PA12 pin to operate as PA9/PA10 pin. Use of this property is restricted to STM32F070x SoCs. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-pinctrl” compatible.

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
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `output-low` | `boolean` | ```text set the pin to output mode with low level ``` |
| `output-high` | `boolean` | ```text set the pin to output mode with high level ``` |
| `pinmux` | `int` | ```text Reused from https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/pinctrl/st,stm32-pinctrl.yaml Integer array, represents gpio pin number and mux setting. These defines are calculated as: ((port * 16 + line) << 8) | function With: - port: The gpio port index (PA = 0, PB = 1, ..., PK = 11) - line: The line offset within the port (PA0 = 0, PA1 = 1, ..., PA15 = 15) - function: The function number, can be: * 0 : Alternate Function 0 * 1 : Alternate Function 1 * 2 : Alternate Function 2 * ... * 15 : Alternate Function 15 * 16 : Analog * 17 : GPIO In case selected pin function is GPIO, pin is statically configured as a plain input/output GPIO. Default configuration is input. Output value can be configured by adding 'ouptut-low' or 'output-high' properties to the pin configuration.  To simplify the usage, macro is available to generate "pinmux" field. This macro is available here:   -include/zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h Some examples of macro usage:    GPIO A9 set as alternate function 2 ... {          pinmux = <STM32_PINMUX('A', 9, AF2)>; };    GPIO A9 set as analog ... {          pinmux = <STM32_PINMUX('A', 9, ANALOG)>; };    GPIO A9 set as GPIO output high ... {          pinmux = <STM32_PINMUX('A', 9, GPIO)>;          output-high; }; ```  This property is **required**. |
| `slew-rate` | `string` | ```text Pin speed. Default to low-speed. For few pins (PA11 and PB3 depending on SoCs)hardware reset value could differ (very-high-speed). Carefully check reference manual for these pins. ```  Default value: `low-speed`  Legal values: `'low-speed'`, `'medium-speed'`, `'high-speed'`, `'very-high-speed'` |
