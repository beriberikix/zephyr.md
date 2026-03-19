---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/counter/nxp,lptmr.html
original_path: build/dts/api/bindings/counter/nxp,lptmr.html
---

# nxp,lptmr

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/counter/counter\_mcux\_lptmr.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/counter_mcux_lptmr.c).

## Description

```text
NXP LPTMR
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text Counter clock frequency ```  This property is **required**. |
| `prescaler` | `int` | ```text The frequency of the counter is divided by this value. ```  This property is **required**. |
| `clk-source` | `int` | ```text Selects the clock to be used by the LPMTR prescaler/glitch filter. In time counter mode, this field selects the input clock to the prescaler. In pulse counter mode, this field selects the input clock to the glitch filter. The clock connections vary by device, see the device reference manual for more details. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `input-pin` | `int` | ```text When LPTMR is in Pulse mode, this value will be used to determine the "rising-edge source pin" to increment the lptmr counter. ``` |
| `active-low` | `boolean` | ```text When LPTMR is in Pulse mode, this value will set the counter to active low. ``` |
| `resolution` | `int` | ```text Represents the width of the counter in bits. ```  This property is **required**. |
| `prescale-glitch-filter` | `int` | ```text When in prescaler mode, the counter is incremented every   2 ^ [prescaler-glitch-filter] clock cycles. When in pulse mode, the counter is incremented every   2 ^ [prescaler-glitch-filter] rising edges detected   by the pin configured from the input-pin value.   Note, that the pulse mode cannot be 2 ^ 16. ```  Default value: `1`  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16` |
| `timer-mode-sel` | `int` | ```text This value determines rather the LPTMR is configured for Time-Counter mode or for Pulse mode. 0 <- LPTMR is configured for Time Counter Mode. 1 <- LPTMR is configured for Pulse Mode. ```  Legal values: `0`, `1` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,lptmr” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
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
