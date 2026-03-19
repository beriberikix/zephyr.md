---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/i2c/infineon,xmc4xxx-i2c.html
original_path: build/dts/api/bindings/i2c/infineon,xmc4xxx-i2c.html
---

# infineon,xmc4xxx-i2c

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

Note

An implementation of a driver matching this compatible is available in
[drivers/i2c/i2c\_ifx\_xmc4.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/i2c_ifx_xmc4.c).

## Description

These nodes are “i2c” bus nodes.

```text
Infineon XMC4XXX I2C

This driver configures the USIC as an I2C device.

Example devicetree configuration with an adt7420 temperature sensor
connected on the bus:

&usic1ch1 {
    compatible = "infineon,xmc4xxx-i2c";
    status = "okay";

    pinctrl-0 = <&i2c_scl_p0_13_u1c1 &i2c_sda_p3_15_u1c1>;
    pinctrl-names = "default";
    scl-src = "DX1B";
    sda-src = "DX0A";
    interrupts = <94 1>;

    #address-cells = <1>;
    #size-cells = <0>;

    clock-frequency = <I2C_BITRATE_STANDARD>;
    adt7420@48 {
        compatible = "adi,adt7420";
        reg = <0x48>;
    };
};

The pinctrl nodes need to be configured as open-drain and
hwctrl should be disabled:

&i2c_scl_p0_13_u1c1 {
    drive-strength = "strong-sharp-edge";
    drive-open-drain;
    hwctrl = "disabled";
};

&i2c_sda_p3_15_u1c1 {
    drive-strength = "strong-soft-edge";
    drive-open-drain;
    hwctrl = "disabled";
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `scl-src` | `string` | ```text Connects the I2C clock line (USIC DX1 input) to a specific GPIO pin. The USIC DX1 input is a multiplexer which connects to different GPIO pins. Refer to the XMC4XXX reference manual for the GPIO pin/mux mappings. ```  This property is **required**.  Legal values: `'DX1A'`, `'DX1B'`, `'DX1C'`, `'DX1D'`, `'DX1E'`, `'DX1F'`, `'DX1G'` |
| `sda-src` | `string` | ```text Connects the I2C data line (USIC DX0 input) to a specific GPIO pin. The USIC DX0 input is a multiplexer which connects to different GPIO pins. Refer to the XMC4XXX reference manual for the GPIO pin/mux mappings. ```  This property is **required**.  Legal values: `'DX0A'`, `'DX0B'`, `'DX0C'`, `'DX0D'`, `'DX0E'`, `'DX0F'`, `'DX0G'` |
| `pinctrl-0` | `phandles` | ```text PORT pin configuration for SCL, SDA signals. We expect that the phandles will reference pinctrl nodes. These nodes will have a nodelabel that matches the Infineon SoC Pinctrl defines and have following format: i2c_<signal>_p<port>_<pin>_<peripheral inst>  Examples:   pinctrl-0 = <&i2c_scl_p5_2_u2c0 &i2c_sda_p5_0_u2c0>;  The pins should set to open-drain and hwctrl should be disabled.  &i2c_scl_p5_2_u2c0 {     drive-strength = "strong-sharp-edge";     drive-open-drain;     hwctrl = "disabled"; };  In the above example, the pin is both an input and output (as is required for I2C setup). It is internally connected to both DX0 and DOUT0 of USIC2 channel 0. (See XMC4700/4800 reference manual page 18-110, Figure 18-50 for more details). This limits the number of pins that can be used for the I2C module.  To get around this pin limitation, it is possible to use pins that do not have this internal connection, and instead connect the pins externally on the board. For example, for the SDA line on USIC2 channel 0, P3.8 may be used for DOUT0 and P6.5 for DX0. These type of pinctrl nodes will have labels: i2c_sda_dout0_p3_8_u2c0 and i2c_sda_dx0_p6_5_u2c0. The generalized format is: i2c_<signal>_<type>_p<port>_<pin>_<peripheral inst>  An example for SCL and SDA signals on the xmc4700: pinctrl-0 = <&i2c_sda_dout0_p3_8_u2c0 &i2c_sda_dx0_p6_5_u2c0             &i2c_scl_dout1_p3_9_u2c0 &i2c_scl_p5_2_u2c0>;  Externally P3.8 should be connected to P6.5; P3.9 should be connected to P5.2.  Note that any pins that do not have dout0/dx0 or dout1/dx1 can have either function. Thus node i2c_scl_p5_0_u2c0 can be both dout1 and dx1.  For the pin configurations, the output pins (dout0 and dout1) should be set to open-drain while the input pins (dx0 and dx1) should not include this setting.  &i2c_sda_dout0_p3_8_u2c0 {     drive-strength = "strong-sharp-edge";     drive-open-drain;     hwctrl = "disabled"; };  &i2c_scl_dout1_p3_9_u2c0 {     drive-strength = "strong-sharp-edge";     drive-open-drain;     hwctrl = "disabled"; };  &i2c_sda_dx0_p6_5_u2c0 {   /* will require USIC setting sda-src = DX0D */     hwctrl = "disabled"; };  &i2c_scl_p5_2_u2c0 {  /* will require USIC scl-src = DX1A */     hwctrl = "disabled"; }; ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `clock-frequency` | `int` | ```text Initial clock frequency in Hz ``` |
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
may apply to the “infineon,xmc4xxx-i2c” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text IRQ number and priority to use for interrupt driven by I2C. Each USIC must use a certain interrupt range: USIC0 = [84, 89] USIC1 = [90, 95] USIC2 = [96, 101] ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
