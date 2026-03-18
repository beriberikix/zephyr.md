---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/sdhc/nxp,imx-usdhc.html
original_path: build/dts/api/bindings/sdhc/nxp,imx-usdhc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nxp,imx-usdhc

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

These nodes are “sd” bus nodes.

```text
NXP imx USDHC controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `data-timeout` | `int` | ```text Data timeout, as multiple of the SD clock. See DTOCV field of USDHC ```  Default value: `15` |
| `read-watermark` | `int` | ```text Number of words used as read watermark level in FIFO queue for USDHC ```  Default value: `128` |
| `write-watermark` | `int` | ```text Number of words used as write watermark level in FIFO queue for USDHC ```  Default value: `128` |
| `max_current_330` | `int` | ```text Max drive current in mA at 3.3V. A value of zero indicates no maximum is specified by the driver. ``` |
| `pwr-gpios` | `phandle-array` | ```text Power pin This pin defaults to active high when consumed by the SD card. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `cd-gpios` | `phandle-array` | ```text Detect pin This pin defaults to active low when produced by the SD card. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `no-1-8-v` | `boolean` | ```text When the external SD card circuit does not support 1.8V, add this property to disable 1.8v card voltage of SD card controller. ``` |
| `detect-dat3` | `boolean` | ```text Enable the host to detect an SD card via the DAT3 line of the SD card connection. Requires the board to define a function to pull DAT3 low or high using pullup/pulldown resistors. ``` |
| `max-current-330` | `int` | ```text Max drive current in mA at 3.3V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-current-300` | `int` | ```text Max drive current in mA at 3.0V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-current-180` | `int` | ```text Max drive current in mA at 1.8V. A value of zero indicates no maximum is specified by the driver. ``` |
| `max-bus-freq` | `int` | ```text Maximum bus frequency for SD card. This should be the highest frequency the SDHC is capable of negotiating with cards on the bus. ```  Default value: `400000` |
| `min-bus-freq` | `int` | ```text Minimum bus frequency for SD card. This should be the frequency that cards first will select when attached to the SDHC bus ```  Default value: `400000` |
| `power-delay-ms` | `int` | ```text time in ms for SDHC to delay when toggling power to the SD card. This delay gives the card time to power up or down fully ```  Default value: `500` |
| `mmc-hs200-1_8v` | `boolean` | ```text The host controller supports HS200 at 1.8V ``` |
| `mmc-hs400-1_8v` | `boolean` | ```text The host controller supports HS400 at 1.8V ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,imx-usdhc” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
