---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/can/infineon,xmc4xxx-can-node.html
original_path: build/dts/api/bindings/can/infineon,xmc4xxx-can-node.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# infineon,xmc4xxx-can-node

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

## Description

```text
Infineon XMC4xxx CAN Node
```

## Properties

### Top level properties

These property descriptions apply to “infineon,xmc4xxx-can-node”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `bitrate` | `int` | ```text Initial bitrate in bit/s. If this is unset, the initial bitrate is set to CONFIG_CAN_DEFAULT_BITRATE. ``` |
| `sample-point` | `int` | ```text Initial sample point in per mille (e.g. 875 equals 87.5%).  If this is unset (or if it is set to 0), the initial sample point will default to 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. ``` |
| `phys` | `phandle` | ```text Actively controlled CAN transceiver.  Example:   transceiver0: can-phy0 {     compatible = "nxp,tja1040", "can-transceiver-gpio";     standby-gpios = <gpioa 0 GPIO_ACTIVE_HIGH>;     max-bitrate = <1000000>;     #phy-cells = <0>;   };    &can0 {     status = "okay";      phys = <&transceiver0>;   }; ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `clock_div8` | `boolean` | ```text Option enables clock divide by a factor of 8. ``` |
| `input-src` | `string` | ```text Connects the CAN input line to a specific IO. ```  This property is **required**.  Legal values: `'RXDA'`, `'RXDB'`, `'RXDC'`, `'RXDD'`, `'RXDE'`, `'RXDF'`, `'RXDG'`, `'RXDH'` |

Deprecated properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `bus-speed` | `int` | ```text Deprecated. This property has been renamed to bitrate.  Initial bitrate in bit/s. If this is unset, the initial bitrate is set to CONFIG_CAN_DEFAULT_BITRATE. ``` |

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,xmc4xxx-can-node” compatible.

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
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `min-bitrate` | `int` | ```text The minimum bitrate supported by the CAN transceiver in bits/s. ``` |
| `max-bitrate` | `int` | ```text The maximum bitrate supported by the CAN transceiver in bits/s. ```  This property is **required**. |
