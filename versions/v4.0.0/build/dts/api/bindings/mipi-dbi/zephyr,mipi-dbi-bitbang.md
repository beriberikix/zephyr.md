---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/mipi-dbi/zephyr,mipi-dbi-bitbang.html
original_path: build/dts/api/bindings/mipi-dbi/zephyr,mipi-dbi-bitbang.html
---

# zephyr,mipi-dbi-bitbang

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[drivers/mipi\_dbi/mipi\_dbi\_bitbang.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/mipi_dbi_bitbang.c).

## Description

These nodes are “mipi-dbi” bus nodes.

```text
MIPI-DBI Mode A and B bit banging controller. This driver emulates MIPI DBI mode A and B (6800
and 8080 parallel interfaces) using GPIO pins.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `dc-gpios` | `phandle-array` | ```text Data/command GPIO pin. Set to low when sending a command, or high when sending data. ```  This property is **required**. |
| `reset-gpios` | `phandle-array` | ```text Reset GPIO pin. Set high to reset the display. ```  This property is **required**. |
| `rd-gpios` | `phandle-array` | ```text Read GPIO pin. Set high when reading from the display. Required for type B (Intel 8080) mode, unused for type A (Motorola 6800). ``` |
| `wr-gpios` | `phandle-array` | ```text Write GPIO pin for type B (Intel 8080) mode, Read/!Write pin for type A (Motorola 6800) mode. ```  This property is **required**. |
| `e-gpios` | `phandle-array` | ```text Clocked enable/strobe pin for type A (Motorola 6800) mode, unused for type B (Intel 8080). Fixed E mode is not supported. ``` |
| `cs-gpios` | `phandle-array` | ```text Chip-select GPIO pin. ```  This property is **required**. |
| `data-gpios` | `phandle-array` | ```text GPIO pins used for the parallel data bus. This must have as many entries as the bus is wide of the selected mipi-mode. ```  This property is **required**. |
| `clock-frequency` | `int` | ```text Clock frequency of the SCL signal of the MBI-DBI peripheral, in Hz ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,mipi-dbi-bitbang” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
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
