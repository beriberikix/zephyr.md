---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/can/st,stm32-bxcan.html
original_path: build/dts/api/bindings/can/st,stm32-bxcan.html
---

# st,stm32-bxcan

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/can/can\_stm32\_bxcan.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/can_stm32_bxcan.c).

## Description

```text
STM32 CAN controller
```

## Properties

### Top level properties

These property descriptions apply to “st,stm32-bxcan”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `master-can-reg` | `int` | ```text master can reg when different from current instance ``` |
| `bitrate` | `int` | ```text Initial bitrate in bit/s. If this is unset, the initial bitrate is set to CONFIG_CAN_DEFAULT_BITRATE. ``` |
| `sample-point` | `int` | ```text Initial sample point in per mille (e.g. 875 equals 87.5%).  If this is unset (or if it is set to 0), the initial sample point will default to 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. ``` |
| `phys` | `phandle` | ```text Actively controlled CAN transceiver.  Example:   transceiver0: can-phy0 {     compatible = "nxp,tja1040", "can-transceiver-gpio";     standby-gpios = <gpioa 0 GPIO_ACTIVE_HIGH>;     max-bitrate = <1000000>;     #phy-cells = <0>;   };    &can0 {     status = "okay";      phys = <&transceiver0>;   }; ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `bus-speed` | `int` | ```text Deprecated. This property has been renamed to bitrate.  Initial bitrate in bit/s. If this is unset, the initial bitrate is set to CONFIG_CAN_DEFAULT_BITRATE. ``` |

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-bxcan” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
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
