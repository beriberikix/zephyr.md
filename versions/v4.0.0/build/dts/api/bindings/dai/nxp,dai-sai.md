---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/dai/nxp,dai-sai.html
original_path: build/dts/api/bindings/dai/nxp,dai-sai.html
---

# nxp,dai-sai

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/dai/nxp/sai/sai.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dai/nxp/sai/sai.c).

## Description

```text
NXP Synchronous Audio Interface (SAI) node
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `mclk-is-output` | `boolean` | ```text Use this property to set the SAI MCLK as output or as input. By default, if this property is not specified, MCLK will be set as input. Setting the MCLK as output for SAIs which don't support MCLK configuration will result in a BUILD_ASSERT() failure. ``` |
| `rx-fifo-watermark` | `int` | ```text Use this property to specify the watermark value for the TX FIFO. This value needs to be in FIFO words (NOT BYTES). This value needs to be in the following interval: (0, DEFAULT_FIFO_DEPTH], otherwise a BUILD_ASSERT() failure will be raised. ``` |
| `tx-fifo-watermark` | `int` | ```text Use this property to specify the watermark value for the RX FIFO. This value needs to be in FIFO words (NOT BYTES). This value needs to be in the following interval: (0, DEFAULT_FIFO_DEPTH], otherwise a BUILD_ASSERT() failure will be raised. ``` |
| `fifo-depth` | `int` | ```text Use this property to set the FIFO depth that will be reported to other applications calling dai_get_properties(). This value should be in the following interval: (0, DEFAULT_FIFO_DEPTH], otherwise a BUILD_ASSERT() failure will be raised. By DEFAULT_FIFO_DEPTH we mean the actual (hardware) value of the FIFO depth. This is needed because some applications (e.g: SOF) use this value to compute the DMA burst size, in which case DEFAULT_FIFO_DEPTH cannot be used. Generally, reporting a false FIFO depth should be avoided. Please note that the sanity check for tx/rx-fifo-watermark uses DEFAULT_FIFO_DEPTH instead of this value so use with caution. If unsure, it's better to simply not use this property, in which case the reported value will be DEFAULT_FIFO_DEPTH. ``` |
| `dai-index` | `int` | ```text Use this property to specify the index of the DAI. At the moment, this is only used by SOF to fetch the "struct device" associated with the DAI whose index Linux passes to SOF through an IPC. If this property is not specified, the DAI index will be considered 0. ``` |
| `tx-sync-mode` | `int` | ```text Use this property to specify which synchronization mode to use for the transmitter. At the moment, the only supported modes are:   1) The transmitter is ASYNC (0)   2) The transmitter is in SYNC with the receiver (1) If this property is not specified, the transmitter will be set to ASYNC. If one side is SYNC then the other MUST be ASYNC. Failing to meet this condition will result in a failed BUILD_ASSERT(). ```  Legal values: `0`, `1` |
| `rx-sync-mode` | `int` | ```text Use this property to specify which synchronization mode to use for the receiver. At the moment, the only supported modes are:   1) The receiver is ASYNC (0)   2) The receiver is in SYNC with the transmitter (1) If this property is not specified, the receiver will be set to ASYNC. If one side is SYNC then the other MUST be ASYNC. Failing to meet this condition will result in a failed BUILD_ASSERT(). ```  Legal values: `0`, `1` |
| `tx-dataline` | `int` | ```text Use this property to specify which transmission data line the SAI should use. To find out which transmission line you should use you can:   1) Check the TRM and see if your SAI instance is multiline. If not then   you're going to use transmission line 0.   2) If your SAI is multiline then you need to check the datasheet and see   the index of the transmission line that's connected to your consumer   (e.g: the codec). The indexing of the data line starts at 0. If this property is not specified then the index of the transmission data line will be 0. Please note that "channel" and "data line" are synnonyms in this context. ``` |
| `rx-dataline` | `int` | ```text Use this property to specify which receive transmission data line the SAI should use. To find out which receive line you should use you can:   1) Check the TRM and see if your SAI instance is multiline. If not then   you're going to use receive line 0.   2) If your SAI is multiline then you need to check the datasheet and see   the index of the receive line that's connected to your consumer (e.g: the codec). The indexing of the data line starts at 0. If this property is not specified then the index of the receive data line will be 0. Please note that "channel" and "data line" are synnonyms in this context. ``` |
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
may apply to the “nxp,dai-sai” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
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
