---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/mipi-dsi/st,stm32-mipi-dsi.html
original_path: build/dts/api/bindings/mipi-dsi/st,stm32-mipi-dsi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# st,stm32-mipi-dsi

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

These nodes are “mipi-dsi” bus nodes.

```text
STM32 MIPI DSI host
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `resets` | `phandle-array` | ```text Reset information ```  This property is **required**. |
| `hs-active-high` | `boolean` | ```text DSI host horizontal synchronization is active high. ``` |
| `vs-active-high` | `boolean` | ```text DSI host vertical synchronization is active high. ``` |
| `de-active-high` | `boolean` | ```text DSI host data enable is active high. ``` |
| `non-continuous` | `boolean` | ```text DSI host enable non continuous clock. ``` |
| `pll-ndiv` | `int` | ```text DSI host dedicated PLL loop division factor. ```  This property is **required**. |
| `pll-idf` | `int` | ```text DSI host dedicated PLL input division factor. ```  This property is **required**. |
| `pll-odf` | `int` | ```text DSI HOST dedicated PLL output division factor. ```  This property is **required**. |
| `active-errors` | `int` | ```text Indicates which error interrupts will be enabled. This parameter can be any combination of DSI_Error_Data_Type and defaults to HAL_DSI_ERROR_NONE. ``` |
| `lp-rx-filter` | `int` | ```text Use Low-Power Reception Filter. Cutoff frequency of low-pass filter at the input of LPRX. Defaults to 0 which disables the filter. ``` |
| `host-timeouts` | `array` | ```text DSI HOST timeout parameters. ``` |
| `phy-timings` | `array` | ```text DSI HOST PHY timing parameters. ``` |
| `test-pattern` | `int` | ```text Show DSI host color bars, select color bar orientation 0 : Vertical color bars 1 : Horizontal color bars ```  Legal values: `0`, `1` |
| `phy-clock` | `int` | ```text MIPI PHY clock frequency. Should be set to ensure clock frequency is at least (pixel clock * bits per output pixel) / number of mipi data lanes ``` |
| `reset-names` | `string-array` | ```text Name of each reset ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-mipi-dsi” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `clock-names` | `string-array` | ```text "dsiclk" DSI clock enable. "refclk" External crystal or oscillator clock. "pixelclk" LTDC pixel clock. "refclk" and "pixelclk" are only used to retrieve the frequency for timing calculation. ```  This property is **required**. |
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
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
