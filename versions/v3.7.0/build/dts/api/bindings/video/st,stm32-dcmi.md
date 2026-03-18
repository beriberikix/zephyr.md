---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/video/st,stm32-dcmi.html
original_path: build/dts/api/bindings/video/st,stm32-dcmi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32-dcmi

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STMicroelectronics STM32 Digital Camera Memory Interface (DCMI).
Example of node configuration at board level:

&dcmi {
  status = "okay";
  sensor = <&ov2640>;
  pinctrl-0 = <&dcmi_hsync_pa4 &dcmi_pixclk_pa6 &dcmi_vsync_pb7
              &dcmi_d0_pc6 &dcmi_d1_pc7 &dcmi_d2_pe0 &dcmi_d3_pe1
              &dcmi_d4_pe4 &dcmi_d5_pd3 &dcmi_d6_pe5 &dcmi_d7_pe6>;
  pinctrl-names = "default";
  bus-width = <8>;
  hsync-active = <0>;
  vsync-active = <0>;
  pixelclk-active = <1>;
  capture-rate = <1>;
  dmas = <&dma1 0 75 (STM32_DMA_PERIPH_TO_MEMORY | STM32_DMA_PERIPH_NO_INC |
          STM32_DMA_MEM_INC | STM32_DMA_PERIPH_8BITS | STM32_DMA_MEM_32BITS |
          STM32_DMA_PRIORITY_HIGH) STM32_DMA_FIFO_1_4>;

  port {
    dcmi_ep_in: endpoint {
      remote-endpoint = <&ov2640_ep_out>;
    };
  };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `sensor` | `phandle` | ```text phandle of connected sensor device ```  This property is **required**. |
| `bus-width` | `int` | ```text Number of data lines actively used, valid for the parallel busses. ```  This property is **required**.  Default value: `8`  Legal values: `8`, `10`, `12`, `14` |
| `hsync-active` | `int` | ```text Polarity of horizontal synchronization (DCMI_HSYNC_Polarity). 0 Horizontal synchronization active Low. 1 Horizontal synchronization active High.  For example, if DCMI_HSYNC_Polarity is programmed active high: When HSYNC is low, the data is valid. When HSYNC is high, the data is not valid (horizontal blanking). ```  This property is **required**.  Legal values: `0`, `1` |
| `vsync-active` | `int` | ```text Polarity of vertical synchronization (DCMI_VSYNC_Polarity). 0 Vertical synchronization active Low. 1 Vertical synchronization active High.  For example, if DCMI_VSYNC_Polarity is programmed active high: When VSYNC is low, the data is valid. When VSYNC is high, the data is not valid (vertical blanking). ```  This property is **required**.  Legal values: `0`, `1` |
| `pixelclk-active` | `int` | ```text Polarity of pixel clock (DCMI_PIXCK_Polarity). 0 Pixel clock active on Falling edge. 1 Pixel clock active on Rising edge. ```  This property is **required**.  Legal values: `0`, `1` |
| `capture-rate` | `int` | ```text The DCMI can capture all frames or alternate frames. If it is not specified, the default is all frames. 1 Capture all frames. 2 Capture alternate frames. 4 Capture one frame every 4 frames. ```  Default value: `1`  Legal values: `1`, `2`, `4` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-dcmi” compatible.

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
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text phandle of DMA controller. The DMA controller should be compatible with DMA channel specifier. Specifies a phandle reference to the dma controller, the channel number, the slot number, channel configuration and finally features.  dmas = <&dma1 0 75 (STM32_DMA_PERIPH_TO_MEMORY | STM32_DMA_PERIPH_NO_INC |         STM32_DMA_MEM_INC | STM32_DMA_PERIPH_8BITS | STM32_DMA_MEM_32BITS |         STM32_DMA_PRIORITY_HIGH) STM32_DMA_FIFO_1_4>; ```  This property is **required**. |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
