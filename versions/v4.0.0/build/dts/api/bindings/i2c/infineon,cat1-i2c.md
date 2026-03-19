---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/i2c/infineon,cat1-i2c.html
original_path: build/dts/api/bindings/i2c/infineon,cat1-i2c.html
---

# infineon,cat1-i2c

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

Note

An implementation of a driver matching this compatible is available in
[drivers/i2c/i2c\_ifx\_cat1.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/i2c_ifx_cat1.c).

## Description

These nodes are “i2c” bus nodes.

```text
Infineon CAT1 I2C driver

This driver configures the SCB as an I2C device.

Example devicetree configuration with vl53l0x Time-of-Flight (ToF)
ranging sensor connected on the bus:

i2c3: &scb3 {
    compatible = "infineon,cat1-i2c";
    status = "okay";

    #address-cells = <1>;
    #size-cells = <0>;

    pinctrl-0 = <&p6_0_scb3_i2c_scl &p6_1_scb3_i2c_sda>;
    pinctrl-names = "default";

    vl53l0x@29 {
      compatible = "st,vl53l0x";
      reg = <0x29>;
    };
};

The pinctrl nodes need to be configured as open-drain and
input-enable:

&p6_0_scb3_i2c_scl {
  drive-open-drain;
  input-enable;
};

&p6_1_scb3_i2c_sda {
  drive-open-drain;
  input-enable;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text PORT pin configuration for SCL, SDA signals. We expect that the phandles will reference pinctrl nodes. These nodes will have a nodelabel that matches the Infineon SoC Pinctrl defines and have following format: p<port>_<pin>_<peripheral inst>_<signal>.  Examples:   pinctrl-0 = <&p6_0_scb3_i2c_scl &p6_1_scb3_i2c_sda>; ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `clock-frequency` | `int` | ```text Frequency that the I2C bus runs ``` |
| `sq-size` | `int` | ```text Size of the submission queue for blocking requests ```  Default value: `4` |
| `cq-size` | `int` | ```text Size of the completion queue for blocking requests ```  Default value: `4` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,cat1-i2c” compatible.

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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
