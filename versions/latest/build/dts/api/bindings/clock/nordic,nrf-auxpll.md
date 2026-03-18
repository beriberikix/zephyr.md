---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/nordic,nrf-auxpll.html
original_path: build/dts/api/bindings/clock/nordic,nrf-auxpll.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nordic,nrf-auxpll

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic Auxiliary PLL (Phase Locked Loop)

The output frequency (f_out) of the auxiliary PLL is calculated as follows:

  f_out = ((R + A * 2^(-16)) * f_src) / B

where:

  - A: nordic,frequency
  - B: nordic,outdiv
  - R: nordic,range (3=low, 4=mid, 5=high, 6=statichigh)
  - f_src: Source frequency, given by clocks
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `nordic,ficrs` | `phandle-array` | ```text FICR entries, e.g. <&ficr OFFSET>. Available offsets (or FICR entries) are available at <zephyr/dt-bindings/misc/nordic-nrf-ficr-*.h>. ```  This property is **required**. |
| `nordic,ficr-names` | `string-array` | ```text Names of each nordic,ficrs entry. ``` |
| `nordic,frequency` | `int` | ```text Value used to set the fractional PLL divider ratio (can be set between divider ratios 4 to 5). Valid values range from 0 to 65535. ```  This property is **required**. |
| `nordic,out-div` | `int` | ```text PLL output divider. ```  Legal values: `1`, `2`, `3`, `4`, `6`, `8`, `12`, `16` |
| `nordic,out-drive` | `int` | ```text Output buffer drive strength. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `nordic,current-tune` | `int` | ```text Constant current tune for the ring oscillator ```  This property is **required**. |
| `nordic,sdm-disable` | `boolean` | ```text Disable sigma-delta modulator ``` |
| `nordic,dither-disable` | `boolean` | ```text Disable dither in sigma-delta modulator ``` |
| `nordic,range` | `string` | ```text PLL loop divider range ```  This property is **required**.  Legal values: `'low'`, `'mid'`, `'high'`, `'statichigh'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-auxpll” compatible.

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
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
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
