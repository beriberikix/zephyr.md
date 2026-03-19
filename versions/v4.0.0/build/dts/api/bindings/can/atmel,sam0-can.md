---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/can/atmel,sam0-can.html
original_path: build/dts/api/bindings/can/atmel,sam0-can.html
---

# atmel,sam0-can

Vendor: [Atmel Corporation](../../bindings.md#dt-vendor-atmel)

Note

An implementation of a driver matching this compatible is available in
[drivers/can/can\_sam0.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/can_sam0.c).

## Description

```text
Specialization of Bosch m_can CAN FD controller for Atmel SAM0
```

## Properties

### Top level properties

These property descriptions apply to “atmel,sam0-can”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `divider` | `int` | ```text Clock divider of GLCK7 used by CAN as clock source ```  This property is **required**. |
| `bosch,mram-cfg` | `array` | ```text Bosch M_CAN message RAM configuration. The cells in the array have the following format:  <offset std-filter-elements ext-filter-elements rx-fifo0-elements rx-fifo1-elements rx-buffer-elements tx-event-fifo-elements tx-buffer-elements>  The 'offset' is an address offset of the message RAM where the following elements start from. This is normally set to 0x0 when using a non-shared message RAM. The remaining cells specify how many elements are allocated for each filter type/FIFO/buffer.  The Bosch M_CAN IP supports the following elements: 11-bit Filter    0-128 elements / 0-128 words 29-bit Filter     0-64 elements / 0-128 words Rx FIFO 0                   0-64 elements / 0-1152 words Rx FIFO 1                   0-64 elements / 0-1152 words Rx Buffers          0-64 elements / 0-1152 words Tx Event FIFO     0-32 elements / 0-64 words Tx Buffers          0-32 elements / 0-576 words ```  This property is **required**. |
| `bitrate-data` | `int` | ```text Initial data phase bitrate in bit/s.  If this is unset, the initial data phase bitrate is set to CONFIG_CAN_DEFAULT_BITRATE_DATA. ``` |
| `sample-point-data` | `int` | ```text Initial data phase sample point in per mille (e.g. 875 equals 87.5%).  If this is unset (or if it is set to 0), the initial sample point will default to 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. ``` |
| `bitrate` | `int` | ```text Initial bitrate in bit/s. If this is unset, the initial bitrate is set to CONFIG_CAN_DEFAULT_BITRATE. ``` |
| `sample-point` | `int` | ```text Initial sample point in per mille (e.g. 875 equals 87.5%).  If this is unset (or if it is set to 0), the initial sample point will default to 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. ``` |
| `phys` | `phandle` | ```text Actively controlled CAN transceiver.  Example:   transceiver0: can-phy0 {     compatible = "nxp,tja1040", "can-transceiver-gpio";     standby-gpios = <gpioa 0 GPIO_ACTIVE_HIGH>;     max-bitrate = <1000000>;     #phy-cells = <0>;   };    &can0 {     status = "okay";      phys = <&transceiver0>;   }; ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |

Deprecated properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `bus-speed-data` | `int` | ```text Deprecated. This property has been renamed to bitrate-data.  Initial data phase bitrate in bit/s.  If this is unset, the initial data phase bitrate is set to CONFIG_CAN_DEFAULT_BITRATE_DATA. ``` |
| `bus-speed` | `int` | ```text Deprecated. This property has been renamed to bitrate.  Initial bitrate in bit/s. If this is unset, the initial bitrate is set to CONFIG_CAN_DEFAULT_BITRATE. ``` |

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “atmel,sam0-can” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupt-names` | `string-array` | ```text name of each interrupt ```  This property is **required**. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `clock-names` | `string-array` | ```text name of each clock ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `min-bitrate` | `int` | ```text The minimum bitrate supported by the CAN transceiver in bits/s. ``` |
| `max-bitrate` | `int` | ```text The maximum bitrate supported by the CAN transceiver in bits/s. ```  This property is **required**. |
