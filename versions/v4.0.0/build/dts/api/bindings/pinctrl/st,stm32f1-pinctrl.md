---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/st,stm32f1-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/st,stm32f1-pinctrl.html
---

# st,stm32f1-pinctrl

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32F1 Pin controller Node
Based on pincfg-node.yaml binding.

Note: `bias-disable` and `drive-push-pull` are default pin configurations.
       They will be applied in case no `bias-foo` or `driver-bar` properties
       are set.
```

## Properties

### Top level properties

These property descriptions apply to “st,stm32f1-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `swj-cfg` | `string` | ```text Configures number of pins assigned to the SWJ debug port.  * full         - Full SWJ (JTAG-DP + SW-DP). * no-njtrst    - Full SWJ (JTAG-DP + SW-DP) but without NJTRST.                  Releases: PB4. * jtag-disable - JTAG-DP Disabled and SW-DP Enabled.                  Releases: PA15 PB3 PB4. * disable      - JTAG-DP Disabled and SW-DP Disabled.                  Releases: PA13 PA14 PA15 PB3 PB4.  If absent, then Full SWJ (JTAG-DP + SW-DP) is used (reset state). ```  Default value: `full`  Legal values: `'full'`, `'no-njtrst'`, `'jtag-disable'`, `'disable'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32f1-pinctrl” compatible.

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
| `pinmux` | `int` | ```text Adapted from https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/pinctrl/st,stm32-pinctrl.yaml Integer array, represents gpio pin number and mux setting. These defines are calculated as: ((port * 16 + line) << 8) | (function << 6) | remap) With: - port: The gpio port index (PA = 0, PB = 1, ..., PK = 11) - line: The line offset within the port (PA0 = 0, PA1 = 1, ..., PA15 = 15) - function: The configuration mode, can be: * 0 : Alternate function output * 1 : Input * 2 : Analog * 3 : GPIO output In case selected pin function is GPIO output, pin is statically configured as a plain output GPIO, which configuration can be set by adding 'ouptut-low' or 'output-high' properties to the pinctrl configuration. Default is output-low. - remap: The pin remapping configuration. It allows to assign the pin function to a different peripheral. Remain configuration can be: * 0 : No remap * 1 : Partial remap 1 * 2 : Partial remap 2 * 3 : Partial remap 3 * 4 : Full remap To simplify the usage, macro is available to generate "pinmux" field. This macro is available here:   -include/zephyr/dt-bindings/pinctrl/stm32f1-pinctrl.h Some examples of macro usage:    GPIO A9 set as alternate with no remap ... {          pinmux = <STM32F1_PINMUX('A', 9, ALTERNATE, REMAP_NO)>; };    GPIO A9 set as alternate with full remap ... {          pinmux = <STM32F1_PINMUX('A', 9, ALTERNATE, REMAP_FULL)>; };    GPIO A9 set as input ... {          pinmux = <STM32F1_PINMUX('A', 9, GPIO_IN, REMAP_NO)>; };    GPIO A9 set as output-high ... {          pinmux = <STM32F1_PINMUX('A', 9, GPIO_OUT, REMAP_NO)>;          output-high; }; ```  This property is **required**. |
| `slew-rate` | `string` | ```text Pin output mode, maximum achievable speed. Only applies to output mode (alternate). ```  Default value: `max-speed-10mhz`  Legal values: `'max-speed-10mhz'`, `'max-speed-2mhz'`, `'max-speed-50mhz'` |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `output-low` | `boolean` | ```text set the pin to output mode with low level ``` |
| `output-high` | `boolean` | ```text set the pin to output mode with high level ``` |
