---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/mipi-dsi/nxp,imx-mipi-dsi.html
original_path: build/dts/api/bindings/mipi-dsi/nxp,imx-mipi-dsi.html
---

# nxp,imx-mipi-dsi

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/mipi\_dsi/dsi\_mcux.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/dsi_mcux.c).

## Description

These nodes are “mipi-dsi” bus nodes.

```text
NXP MCUX MIPI DSI
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `nxp,lcdif` | `phandle` | ```text Instance of the LCDIF peripheral. Only required when using the MIPI DSI in video mode. ``` |
| `dpi-color-coding` | `string` | ```text MIPI DPI interface color coding. Sets the distribution of RGB bits within the 24-bit d bus, as specified by the DPI specification. ```  Legal values: `'16-bit-config-1'`, `'16-bit-config-2'`, `'16-bit-config-3'`, `'18-bit-config-1'`, `'18-bit-config-2'`, `'24-bit'` |
| `dpi-pixel-packet` | `string` | ```text MIPI DSI pixel packet type send through DPI interface. ```  Legal values: `'16-bit'`, `'18-bit'`, `'18-bit-loose'`, `'24-bit'` |
| `dpi-video-mode` | `string` | ```text DPI video mode. ```  Legal values: `'non-burst-sync-pulse'`, `'non-burst-sync-event'`, `'burst'` |
| `dpi-bllp-mode` | `string` | ```text Behavior in BLLP (Blanking or Low-Power Interval). ```  Legal values: `'low-power'`, `'blank'`, `'null'` |
| `autoinsert-eotp` | `boolean` | ```text Automatically insert an EoTp short packet when switching from HS to LP mode. ``` |
| `dphy-ref-frequency` | `int` | ```text Maximum clock speed supported by the device, in Hz. ```  This property is **required**. |
| `phy-clock` | `int` | ```text MIPI PHY clock frequency. Should be set to ensure clock frequency is at least (pixel clock * bits per output pixel) / number of mipi data lanes ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,imx-mipi-dsi” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
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
