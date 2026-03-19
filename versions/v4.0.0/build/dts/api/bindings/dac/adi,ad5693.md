---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/dac/adi,ad5693.html
original_path: build/dts/api/bindings/dac/adi,ad5693.html
---

# adi,ad5693

Vendor: [Analog Devices, Inc.](../../bindings.md#dt-vendor-adi)

Note

An implementation of a driver matching this compatible is available in
[drivers/dac/dac\_ad569x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/dac_ad569x.c).

## Description

```text
Driver for AD5693 (16-bit) DAC.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#io-channel-cells` | `int` | This property is **required**.  Constant value: `1` |
| `voltage-reference` | `string` | ```text DAC voltage reference select. - Internal voltage reference - 2.5V (reg: 0). - External voltage reference (reg: 1). The default corresponds to the reset value of the register field. ```  Default value: `internal`  Legal values: `'internal'`, `'external'` |
| `gain` | `string` | ```text Gain selection bit. - Gain of 1 (reg: 0). - Gain of 2 (reg: 1). The default corresponds to the reset value of the register field. ```  Default value: `gain-1`  Legal values: `'gain-1'`, `'gain-2'` |
| `power-down-mode` | `string` | ```text Power-down mode select. - Normal mode (reg: 0). - 1 kOhm output impedance (reg: 1). - 100 kOhm output impedance (reg: 2). - Three-state output impedance (reg: 3). The default corresponds to the reset value of the register field. ```  Default value: `normal`  Legal values: `'normal'`, `'power-down-1k'`, `'power-down-100k'`, `'power-down-3-state'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,ad5693” compatible.

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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

## Specifier cell names

- io-channel cells: output
