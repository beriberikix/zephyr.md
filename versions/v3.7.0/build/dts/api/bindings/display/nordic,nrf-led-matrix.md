---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/display/nordic,nrf-led-matrix.html
original_path: build/dts/api/bindings/display/nordic,nrf-led-matrix.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nordic,nrf-led-matrix

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Generic LED matrix driven by nRF SoC GPIOs
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `height` | `int` | ```text Height of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |
| `width` | `int` | ```text Width of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |
| `row-gpios` | `phandle-array` | ```text Array of GPIOs to be used as rows of the matrix. ```  This property is **required**. |
| `col-gpios` | `phandle-array` | ```text Array of GPIOs to be used as columns of the matrix. ```  This property is **required**. |
| `pixel-mapping` | `uint8-array` | ```text Array of bytes that specify which rows and columns of the matrix control its particular pixels, line by line. Each byte in this array corresponds to one pixel of the matrix and specifies the row index in the high nibble and the column index in the low nibble.  For example, the following snippet (from the bbc_microbit board DTS):    width = <5>;   height = <5>;   pixel-mapping = [00 13 01 14 02                    23 24 25 26 27                    ...  specifies that: - pixel (0,0) is controlled by row 0 and column 0 - pixel (1,0) is controlled by row 1 and column 3 - pixel (0,1) is controlled by row 2 and column 3 - pixel (1,1) is controlled by row 2 and column 4 and so on. ```  This property is **required**. |
| `refresh-frequency` | `int` | ```text Frequency of refreshing the matrix, in Hz. ```  This property is **required**. |
| `timer` | `phandle` | ```text Reference to a TIMER instance for controlling refreshing of the matrix. ```  This property is **required**. |
| `pwm` | `phandle` | ```text Reference to a PWM instance for generating pulse signals on column GPIOs. If not provided, GPIOTE and PPI channels are allocated and used instead for generating those pulses. ``` |
| `pixel-group-size` | `int` | ```text This value specifies the maximum number of LEDs in one row that can be lit simultaneously. If set to 1, only a single LED is turned on in a particular time slot. Bigger values increase the maximum achievable brightness of the LEDs and lower the CPU load by decreasing the frequency of execution of the timer interrupt handler. In case GPIOTE and PPI channels are used for generating the pixel pulse signals, the number of channels that need to be allocated is equal to this value. If GPIOTE and PPI channels are used, the upper limit for the value is defined by the number of CC channels in the used timer minus one. If PWM is used, the upper limit is the number of PWM channels. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-led-matrix” compatible.

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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
