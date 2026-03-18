---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/sdhc/cdns,sdhc.html
original_path: build/dts/api/bindings/sdhc/cdns,sdhc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# cdns,sdhc

Vendor: [Cadence Design Systems Inc.](../../bindings.md#dt-vendor-cdns)

## Description

These nodes are “sd” bus nodes.

```text
Cadence SDHC Controller node
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `max-current-330` | `int` | ```text Max drive current in mA at 3.3V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-current-300` | `int` | ```text Max drive current in mA at 3.0V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-current-180` | `int` | ```text Max drive current in mA at 1.8V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-bus-freq` | `int` | ```text Maximum bus frequency for SD card. This should be the highest frequency the SDHC is capable of negotiating with cards on the bus. ```  Default value: `400000` |
| `min-bus-freq` | `int` | ```text Minimum bus frequency for SD card. This should be the frequency that cards first will select when attached to the SDHC bus ```  Default value: `400000` |
| `power-delay-ms` | `int` | ```text time in ms for SDHC to delay when toggling power to the SD card. This delay gives the card time to power up or down fully ```  Default value: `500` |
| `mmc-hs200-1_8v` | `boolean` | ```text The host controller supports HS200 at 1.8V ``` |
| `mmc-hs400-1_8v` | `boolean` | ```text The host controller supports HS400 at 1.8V ``` |
| `resets` | `phandle-array` | ```text Reset information ``` |
| `reset-names` | `string-array` | ```text Name of each reset ``` |
| `clock-frequency` | `int` | ```text clock-frequency for SDHC ``` |
| `power_delay_ms` | `int` | ```text delay required to switch on the SDHC ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “cdns,sdhc” compatible.

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
