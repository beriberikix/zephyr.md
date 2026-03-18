---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/display/st,stm32-ltdc.html
original_path: build/dts/api/bindings/display/st,stm32-ltdc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32-ltdc

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 LCD-TFT display controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `height` | `int` | ```text Height of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |
| `width` | `int` | ```text Width of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |
| `pixel-format` | `int` | ```text Initial Pixel format for panel attached to this controller. See dt-bindings/display/panel.h for a list ```  This property is **required**. |
| `pinctrl-0` | `phandles` | ```text Provide a pin configuration for using parallel pixel output. In combination with DSI HOST the pin configuration is not necessary due to dedicated (MIPI D-PHY) pins. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `disp-on-gpios` | `phandle-array` | ```text Display on/off GPIO pin. Configure the GPIO polarity (active high/active low) according to LCD datasheet. ``` |
| `bl-ctrl-gpios` | `phandle-array` | ```text Backlight on/off GPIO pin. Configure the GPIO polarity (active high/active low) according to LCD datasheet. ``` |
| `ext-sdram` | `phandle` | ```text External SDRAM in which frame buffer will be stored. If not defined, internal RAM will be used. ``` |
| `def-back-color-red` | `int` | ```text Default display background color - red ``` |
| `def-back-color-green` | `int` | ```text Default display background color - green ``` |
| `def-back-color-blue` | `int` | ```text Default display background color - blue ``` |
| `window0-x0` | `int` | ```text First pixel in x direction on layer 0. Defaults to 0. ``` |
| `window0-x1` | `int` | ```text Last pixel in x direction on layer 0. Defaults to width. ``` |
| `window0-y0` | `int` | ```text First pixel in y direction on layer 0. Defaults to 0. ``` |
| `window0-y1` | `int` | ```text Last pixel in y direction on layer 0. Defaults to height. ``` |
| `display-controller` | `phandle` | ```text Phandle of the display's controller. When provided, it's used to forward some of the configuration calls (e.g. blanking on/off) sent to LTDC device. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-ltdc” compatible.

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
