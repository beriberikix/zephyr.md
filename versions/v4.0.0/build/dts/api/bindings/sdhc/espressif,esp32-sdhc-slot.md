---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.html
original_path: build/dts/api/bindings/sdhc/espressif,esp32-sdhc-slot.html
---

# espressif,esp32-sdhc-slot

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

Note

An implementation of a driver matching this compatible is available in
[drivers/sdhc/sdhc\_esp32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/sdhc_esp32.c).

## Description

These nodes are “sd” bus nodes.

```text
Espressif ESP32 SDHC controller slot
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `bus-width` | `int` | ```text SD bus width in bits ```  Default value: `4`  Legal values: `1`, `4` |
| `clk-pin` | `int` | ```text Clock pin for ESP32 and SoC models with fixed pins for SDIO. For devices with GPIO matrix support, configuration shall be done using pin control (pinctrl-0 field). ``` |
| `cmd-pin` | `int` | ```text Command pin for ESP32 and SoC models with fixed pins for SDIO. For devices with GPIO matrix support, configuration shall be done using pin control (pinctrl-0 field). ``` |
| `d0-pin` | `int` | ```text Data 0 pin for ESP32 and SoC models with fixed pins for SDIO. For devices with GPIO matrix support, configuration shall be done using pin control (pinctrl-0 field). ``` |
| `d1-pin` | `int` | ```text Data 1 pin for ESP32 and SoC models with fixed pins for SDIO. For devices with GPIO matrix support, configuration shall be done using pin control (pinctrl-0 field). ``` |
| `d2-pin` | `int` | ```text Data 2 pin for ESP32 and SoC models with fixed pins for SDIO. For devices with GPIO matrix support, configuration shall be done using pin control (pinctrl-0 field). ``` |
| `d3-pin` | `int` | ```text Data 3 pin for ESP32 and SoC models with fixed pins for SDIO. For devices with GPIO matrix support, configuration shall be done using pin control (pinctrl-0 field). ``` |
| `pwr-gpios` | `phandle-array` | ```text Power pin This is a configurable pin to deliver power supply to the SD card. It is configured as a GPIO in order to execute power toggles and reinitialize the SD slave when necessary. ``` |
| `max-current-330` | `int` | ```text Max drive current in mA at 3.3V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-current-300` | `int` | ```text Max drive current in mA at 3.0V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-current-180` | `int` | ```text Max drive current in mA at 1.8V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-bus-freq` | `int` | ```text Maximum bus frequency for SD card. This should be the highest frequency the SDHC is capable of negotiating with cards on the bus. ```  Default value: `400000` |
| `min-bus-freq` | `int` | ```text Minimum bus frequency for SD card. This should be the frequency that cards first will select when attached to the SDHC bus ```  Default value: `400000` |
| `power-delay-ms` | `int` | ```text time in ms for SDHC to delay when toggling power to the SD card. This delay gives the card time to power up or down fully ```  Default value: `500` |
| `mmc-hs200-1_8v` | `boolean` | ```text The host controller supports HS200 at 1.8V ``` |
| `mmc-hs400-1_8v` | `boolean` | ```text The host controller supports HS400 at 1.8V ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “espressif,esp32-sdhc-slot” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
