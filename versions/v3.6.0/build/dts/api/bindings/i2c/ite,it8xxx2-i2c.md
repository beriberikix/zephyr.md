---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/i2c/ite,it8xxx2-i2c.html
original_path: build/dts/api/bindings/i2c/ite,it8xxx2-i2c.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ite,it8xxx2-i2c

Vendor: [ITE Tech. Inc.](../../bindings.md#dt-vendor-ite)

## Description

These nodes are “i2c” bus nodes.

```text
ITE it8xxx2 I2C
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `fifo-enable` | `boolean` | ```text FIFO1 supports channel A. FIFO2 supports channel B. ``` |
| `port-num` | `int` | ```text Ordinal identifying the port 0 = SMB_CHANNEL_A, 1 = SMB_CHANNEL_B, 2 = SMB_CHANNEL_C, 3 = I2C_CHANNEL_D, 4 = I2C_CHANNEL_E, 5 = I2C_CHANNEL_F, ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3`, `4`, `5` |
| `channel-switch-sel` | `int` | ```text The default setting is as described below 0 = I2C_CHA_LOCATE: Channel A is located at SMCLK0/SMDAT0 1 = I2C_CHB_LOCATE: Channel B is located at SMCLK1/SMDAT1 2 = I2C_CHC_LOCATE: Channel C is located at SMCLK2/SMDAT2 3 = I2C_CHD_LOCATE: Channel D is located at SMCLK3/SMDAT3 4 = I2C_CHE_LOCATE: Channel E is located at SMCLK4/SMDAT4 5 = I2C_CHF_LOCATE: Channel F is located at SMCLK5/SMDAT5  The following is an example of the 'channel-switch-sel' property being swapped between node &i2c0 and &i2c2 in the application: Note: The property of 'port-num' cannot be changed in the       application.  Channel C is located at SMCLK0/SMDAT0: &i2c0 {        channel-switch-sel = <I2C_CHC_LOCATE>;        pinctrl-0 = <&i2c2_clk_gpf6_default                     &i2c2_data_gpf7_default>;        pinctrl-names = "default";        scl-gpios = <&gpiof 6 0>;        sda-gpios = <&gpiof 7 0>; };  Channel A is located at SMCLK2/SMDAT2: &i2c2 {        channel-switch-sel = <I2C_CHA_LOCATE>;        pinctrl-0 = <&i2c0_clk_gpb3_default                     &i2c0_data_gpb4_default>;        pinctrl-names = "default";        scl-gpios = <&gpiob 3 0>;        sda-gpios = <&gpiob 4 0>; };  If the property of 'channel-switch-sel' is changed, the pinctrl setting and recovery pin in &i2c0 and &i2c2 nodes must also be modified accordingly. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3`, `4`, `5` |
| `scl-gpios` | `phandle-array` | ```text The SCL pin for the selected port. ```  This property is **required**. |
| `sda-gpios` | `phandle-array` | ```text The SDA pin for the selected port. ```  This property is **required**. |
| `clock-gate-offset` | `int` | ```text The clock gate offsets combine the register offset from ECPM_BASE and the mask within that register into one value. ```  This property is **required**. |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `clock-frequency` | `int` | ```text Initial clock frequency in Hz ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ite,it8xxx2-i2c” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
