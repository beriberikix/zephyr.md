---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/video/nxp,mipi-csi2rx.html
original_path: build/dts/api/bindings/video/nxp,mipi-csi2rx.html
---

# nxp,mipi-csi2rx

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/video/video\_mcux\_mipi\_csi2rx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/video_mcux_mipi_csi2rx.c).

## Description

```text
NXP MIPI CSI-2 Rx interface
```

## Properties

### Top level properties

These property descriptions apply to “nxp,mipi-csi2rx”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,mipi-csi2rx” compatible.

| Name | Type | Details |
| --- | --- | --- |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

### Level 3 child node properties

| Name | Type | Details |
| --- | --- | --- |
| `remote-endpoint-label` | `string` | ```text Label of the 'remote-endpoint' subnode that interfaces with this endpoint. This property is used as a 'work-around' to be able to declare the remote endpoint and should be replaced by a "remote-endpoint" phandle property when Zephyr devicetree supports circular dependency in the future. ```  This property is **required**. |
| `bus-type` | `int` | ```text Data bus type. ```  Legal values: `1`, `2`, `3`, `4`, `5`, `6` |
| `data-shift` | `int` | ```text On parallel data busses, if bus-width is used to specify the number of data lines, data-shift can be used to specify which data lines are used, e.g. "bus-width=<8>; data-shift=<2>;" means, that lines 9:2 are used. ``` |
| `hsync-active` | `int` | ```text Active state of the HSYNC signal ```  Legal values: `0`, `1` |
| `vsync-active` | `int` | ```text Active state of the VSYNC signal. ```  Legal values: `0`, `1` |
| `pclk-sample` | `int` | ```text Sample data on falling, rising or both edges of the pixel clock signal. ```  Legal values: `0`, `1`, `2` |
| `link-frequencies` | `array` | ```text Allowed data bus frequencies. For MIPI CSI-2, for instance, this is the actual frequency of the bus, not bits per clock per lane value. ``` |
| `clock-lane` | `int` | ```text Physical clock lane index. Position of an entry determines the logical lane number, while the value of an entry indicates physical lane, e.g. for a MIPI CSI-2 bus we could have "clock-lane = <0>;", which places the clock lane on hardware lane 0. This property is valid for serial busses only (e.g. MIPI CSI-2). ``` |
| `data-lanes` | `array` | ```text An array of physical data lane indexes. Position of an entry determines the logical lane number, while the value of an entry indicates physical lane, e.g. for 2-lane MIPI CSI-2 bus we could have "data-lanes = <1 2>;", assuming the clock lane is on hardware lane 0. If the hardware does not support lane reordering, monotonically incremented values shall be used from 0 or 1 onwards, depending on whether or not there is also a clock lane. This property is valid for serial busses only (e.g. MIPI CSI-2). ``` |
| `bus-width` | `int` | ```text Number of data lines actively used, only valid for parallel busses. ``` |
