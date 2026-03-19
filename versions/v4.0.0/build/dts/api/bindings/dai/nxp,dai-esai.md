---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/dai/nxp,dai-esai.html
original_path: build/dts/api/bindings/dai/nxp,dai-esai.html
---

# nxp,dai-esai

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/dai/nxp/esai](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/nxp/esai).

## Description

```text
NXP Enhanced Serial Audio Interface (ESAI) node
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `dai-index` | `int` | ```text Use this property to specify the index of the DAI. At the moment, this is only used by SOF to fetch the "struct device" associated with the DAI whose index Linux passes to SOF through an IPC. If this property is not specified, the DAI index will be considered 0. ``` |
| `tx-fifo-watermark` | `int` | ```text Use this property to specify the watermark value for the TX FIFO. This value needs to be in FIFO words (NOT BYTES). This value needs to be in the following interval: (0, DEFAULT_FIFO_DEPTH], otherwise a BUILD_ASSERT() failure will be raised. If unspecified, the TX FIFO watermark will be set to DEFAULT_FIFO_DEPTH / 2. ``` |
| `rx-fifo-watermark` | `int` | ```text Use this property to specify the watermark value for the RX FIFO. This values needs to be in FIFO words (NOT BYTES). This value needs to be in the following interval: (0, DEFAULT_FIFO_DEPTH], otherwise a BUILD_ASSERT() failure will be raised. If unspecified, the RX FIFO watermark will be set to DEFAULT_FIFO_DEPTH / 2. ``` |
| `fifo-depth` | `int` | ```text Use this property to set the FIFO depth that will be reported to upper layer applications calling dai_get_properties(). This value should be in the following interval: (0, DEFAULT_FIFO_DEPTH], otherwise a BUILD_ASSERT() failure will be raised. By DEFAULT_FIFO_DEPTH we mean the actual (hardware) value of the FIFO depth. This is needed because some applications (e.g: SOF) use this value directly as the DMA burst size in which case DEFAULT_FIFO_DEPTH cannot be used. Generally, reporting a false FIFO depth should be avoided. Please note that the sanity check for tx/rx-fifo-watermark uses DEFAULT_FIFO_DETPH instead of this value so use with caution. If unsure, it's better to not use this property at all, in which case the reported value will be DEFAULT_FIFO_DEPTH. ``` |
| `word-width` | `int` | ```text This property is used to specify the width of a word. If unspecified, the word width used will be 24. ``` |
| `esai-pin-modes` | `array` | ```text This property is used to configure the ESAI pins. Each ESAI pin supports 4 modes:   1) DISCONNECTED (PDC[i] = 0, PC[i] = 0)   2) GPIO input (PDC[i] = 0, PC[i] = 1)   3) GPIO output (PDC[i] = 1, PC[i] = 0)   4) ESAI (PDC[i] = 1, PC[i] = 1) If pin is not used then DISCONNECTED mode should be used for said pin. If unsure, don't specify this property at all. By default, all pins will be set to ESAI mode. ``` |
| `esai-clock-configuration` | `array` | ```text Use this property to configure the directions of the ESAI clocks (HCLK, BCLK, FSYNC). This provides extra flexibility since the bespoke configuration is not direction-based. The values from this array will overwrite the values set through the bespoke configuration. If unspecified, the values from the bespoke configuration will be used. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,dai-esai” compatible.

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
