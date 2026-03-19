---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/nordic,nrf-hfxo.html
original_path: build/dts/api/bindings/clock/nordic,nrf-hfxo.html
---

# nordic,nrf-hfxo

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic nRF high-frequency crystal oscillator
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**.  Constant value: `32000000` |
| `load-capacitors` | `string` | ```text Type of load capacitors connected to the crystal. If not specified, adjustments may still happen when the device trimming happens during system initialization. ```  Legal values: `'internal'`, `'external'` |
| `load-capacitance-femtofarad` | `int` | ```text Load capacitance in femtofarads. This property is only used when load-capacitors is set to "internal". ```  Legal values: `4000`, `4250`, `4500`, `4750`, `5000`, `5250`, `5500`, `5750`, `6000`, `6250`, `6500`, `6750`, `7000`, `7250`, `7500`, `7750`, `8000`, `8250`, `8500`, `8750`, `9000`, `9250`, `9500`, `9750`, `10000`, `10250`, `10500`, `10750`, `11000`, `11250`, `11500`, `11750`, `12000`, `12250`, `12500`, `12750`, `13000`, `13250`, `13500`, `13750`, `14000`, `14250`, `14500`, `14750`, `15000`, `15250`, `15500`, `15750`, `16000`, `16250`, `16500`, `16750`, `17000` |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-hfxo” compatible.

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
