---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/st,stm32f0-pll-clock.html
original_path: build/dts/api/bindings/clock/st,stm32f0-pll-clock.html
---

# st,stm32f0-pll-clock

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
Main PLL node binding for STM32F0 and STM32F3 devices.

Takes one of clk_hse or clk_hsi as input clock.

Note: Some STM32F0 SoC variants (STM32072 for instance) may also support HSI48
as input clock. This case is not supported yet.

Frequency calculation for output clock is as follows:

  f(PLLCLK) = f(PLLIN) x PLLMUL   --> SYSCLK (System Clock)

  with, depending on the case:
          If input_clk = clk_hse
            f(PLLIN) = f(input_clk) / PREDIV
          If input_clk = clk_hsi
            On STM32F3, STM32F03x, STM32F05x, STM32F030x4, STM32F030x6 and STM32F030x8
              f(PLLIN) = f(input_clk) / 2
            On STM32F04x, STM32F07x, STM32F09x, STM32F070x6, STM32F070xB and STM32F030xC
              f(PLLIN) = f(input_clk) / PREDIV

The PLL output frequency must be set in range 16-48MHz
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `mul` | `int` | ```text PLL multiplication factor for output clock Valid range: 2 - 16 ```  This property is **required**. |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `prediv` | `int` | ```text Configurable prescaler Valid range: 1 - 16 ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32f0-pll-clock” compatible.

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
