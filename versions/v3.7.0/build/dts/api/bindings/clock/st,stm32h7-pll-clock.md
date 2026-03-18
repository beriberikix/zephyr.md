---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/st,stm32h7-pll-clock.html
original_path: build/dts/api/bindings/clock/st,stm32h7-pll-clock.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32h7-pll-clock

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
PLL node binding for STM32H7 devices

It can be used to describe 3 different PLLs: PLL1 (Main PLL), PLL2 and PLL3.
Only PLL1 and PLL3 are supported for now.

These PLLs could take one of clk_hse, clk_hsi or clk_csi as input clock, with
an input frequency from 1 to 16 MHz. PLLM factor is used to set the input
clock in this acceptable range.

Each PLL can have up to 3 output clocks and for each output clock, the
frequency can be computed with the following formulae:

  f(PLL_Px) = f(VCOx clock) / PLLPx   -> pllx_p_ck ((pll1_p_ck : sys_ck))
  f(PLL_Qx) = f(VCOx clock) / PLLQx   -> pllx_q_ck
  f(PLL_Rx) = f(VCOx clock) / PLLRx   -> pllx_r_ck

    with f(VCOx clock) = f(REFx_CK) × (PLLNx / PLLMx)

The PLL output frequency must not exceed 80 MHz.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `div-m` | `int` | ```text Division factor for PLLx input clock Valid range: 1 - 63 ```  This property is **required**. |
| `mul-n` | `int` | ```text Main PLL multiplication factor for VCOx Valid range: 4 - 512 ```  This property is **required**. |
| `div-p` | `int` | ```text PLL division factor for pllx_p_ck Valid range: 1 - 128 ``` |
| `div-q` | `int` | ```text PLL division factor for pllx_q_ck Valid range: 1 - 128 ``` |
| `div-r` | `int` | ```text PLL division factor for pllx_r_ck Valid range: 1 - 128 ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32h7-pll-clock” compatible.

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
