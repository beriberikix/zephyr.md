---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/can/zephyr,fake-can.html
original_path: build/dts/api/bindings/can/zephyr,fake-can.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,fake-can

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
This binding provides a fake CAN controller for use as either a stub or a mock in Zephyr
testing.
```

## Properties

### Top level properties

These property descriptions apply to “zephyr,fake-can”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `bus-speed-data` | `int` | ```text Initial data phase bitrate in bit/s. ```  This property is **required**. |
| `sample-point-data` | `int` | ```text Initial data phase sample point in per mille (e.g. 875 equals 87.5%).  This property is required unless the timing is specified using time quanta based properties (`sjw-data`, `prop-seg-data`, `phase-seg1-data`, and `phase-seg2-data`).  If this property is present, the time quanta based timing properties are ignored. ``` |
| `tx-delay-comp-offset` | `int` |  |
| `bus-speed` | `int` | ```text Initial bitrate in bit/s. ```  This property is **required**. |
| `sample-point` | `int` | ```text Initial sample point in per mille (e.g. 875 equals 87.5%).  This property is required unless the timing is specified using time quanta based properties (`sjw`, `prop-seg`, `phase-seg1`, and `phase-seg2`).  If this property is present, the time quanta based timing properties are ignored. ``` |
| `phys` | `phandle` | ```text Actively controlled CAN transceiver.  Example:   transceiver0: can-phy0 {     compatible = "nxp,tja1040", "can-transceiver-gpio";     standby-gpios = <gpioa 0 GPIO_ACTIVE_HIGH>;     max-bitrate = <1000000>;     #phy-cells = <0>;   };    &can0 {     status = "okay";      phys = <&transceiver0>;   }; ``` |

Deprecated properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `sjw-data` | `int` | ```text Initial time quanta of resynchronization jump width for the data phase (ISO11898-1:2015).  Deprecated in favor of automatic calculation of a suitable default SJW based on existing timing parameters. Default of 1 matches the default value previously used for all in-tree CAN controller devicetree instances.  Applications can still manually set the SJW using the CAN timing APIs. ```  Default value: `1` |
| `prop-seg-data` | `int` | ```text Initial time quanta of propagation segment for the data phase (ISO11898-1:2015). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `phase-seg1-data` | `int` | ```text Initial time quanta of phase buffer 1 segment for the data phase (ISO11898-1:2015). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `phase-seg2-data` | `int` | ```text Initial time quanta of phase buffer 2 segment for the data phase (ISO11898-1:2015). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `sjw` | `int` | ```text Initial time quanta of resynchronization jump width (ISO 11898-1).  Deprecated in favor of automatic calculation of a suitable default SJW based on existing timing parameters. Default of 1 matches the default value previously used for all in-tree CAN controller devicetree instances.  Applications can still manually set the SJW using the CAN timing APIs. ```  Default value: `1` |
| `prop-seg` | `int` | ```text Initial time quanta of propagation segment (ISO 11898-1). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `phase-seg1` | `int` | ```text Initial time quanta of phase buffer 1 segment (ISO 11898-1). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `phase-seg2` | `int` | ```text Initial time quanta of phase buffer 2 segment (ISO 11898-1). Deprecated in favor of setting advanced timing parameters from the application. ``` |

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,fake-can” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `max-bitrate` | `int` | ```text The maximum bitrate supported by the CAN transceiver in bits/s. ```  This property is **required**. |
