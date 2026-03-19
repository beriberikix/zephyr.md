---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/st,stm32wb-pll-clock.html
original_path: build/dts/api/bindings/clock/st,stm32wb-pll-clock.html
---

# st,stm32wb-pll-clock

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32WB and STM32WL PLL node.

It can be used to describe 2 different PLLs: PLL, PLLSAI1.
Only main PLL is supported for now.

These PLLs could take one of clk_hse, clk_hsi or clk_msi as input clock, with
an input frequency from 2.66 to 16 MHz. PLLM factor is used to set the input
clock in this acceptable range.

Each PLL can have up to 3 output clocks and for each output clock, the
frequency can be computed with the following formulae:

  f(PLL_P) = f(VCO clock) / PLLP  --> PLLPCLK
  f(PLL_Q) = f(VCO clock) / PLLQ  --> PLLQCLK
  f(PLL_R) = f(VCO clock) / PLLR  --> PLLRCLK (System Clock)

    with f(VCO clock) = f(PLL clock input) × (PLLN / PLLM)

The PLL output frequency must not exceed:
        - 64 MHz on STM32WB
        - 62 MHz on STM32WL
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `div-m` | `int` | ```text Main PLL division factor for PLL input clock Valid range: 1 - 8 ```  This property is **required**. |
| `mul-n` | `int` | ```text Main PLL multiplication factor for VCO Valid range: 6 - 127 ```  This property is **required**. |
| `div-p` | `int` | ```text Main PLL division factor for PLLPCLK Valid range: 2 - 32 ``` |
| `div-q` | `int` | ```text Main PLL division factor for PLLQCLK Valid range: 2 - 8 ``` |
| `div-r` | `int` | ```text Main PLL division factor for PLLRCLK (system clock) Valid range: 2 - 8 ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32wb-pll-clock” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
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
