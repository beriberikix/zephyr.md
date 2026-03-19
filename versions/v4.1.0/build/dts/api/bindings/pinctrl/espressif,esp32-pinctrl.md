---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/espressif,esp32-pinctrl.html
---

# espressif,esp32-pinctrl

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

## Description

```text
ESP32 pin controller

Espressif's pin controller is in charge of controlling pin configurations, pin
functionalities and pin properties as defined by pin states. In its turn, pin
states are composed by groups of pre-defined pin muxing definitions and user
provided pin properties.

Each Zephyr-based application has its own set of pin muxing/pin configuration
requirements. The next steps use ESP-WROVER-KIT's I2C_0 to illustrate how one
could change a node's pin state properties. Though based on a particular board,
the same steps can be tweaked to address specifics of any other target board.

Suppose an application running on top of the ESP-WROVER-KIT board, for some
reason it needs I2C_0's SDA signal to be routed to GPIO_33. When looking at
that board's original device tree source file (i.e., 'esp_wrover_kit.dts'),
you'll notice that the I2C_0 node is already assigned to a pre-defined state.
Below is highlighted the information that most interests us on that file

    #include "esp_wrover_kit-pinctrl.dtsi"

    &i2c0 {
            ...
            pinctrl-0 = <&i2c0_default>;
            pinctrl-names = "default";
    };

From the above excerpt, the pincrl-0 property is assigned the 'i2c0_default'
state value. This and other pin states of the board are defined on another file
(in this case, 'esp_wrover_kit-pinctrl.dtsi') on the same folder of the DTS file.
Check below the excerpt describing I2C_0's default state on that file

    i2c0_default: i2c0_default {
            group1 {
                    pinmux = <I2C0_SDA_GPIO21>,
                             <I2C0_SCL_GPIO22>;
                    bias-pull-up;
                    drive-open-drain;
                    output-high;
            };
    };

Only the 'pinmux' property above is actually required, other properties can
be chosen if meaningful for the target application and, of course, supported
by your target hardware. For example, some custom board may have an external
pull-up resistor soldered to GPIO_21's pin pad, in which case, 'bias-pull-up'
could be no longer required.

Back to our fictional application, the previous I2C_0 state definition does not
meet our expectations as we would like to route I2C_0's SDA signal to GPIO_33
instead of to GPIO_21. To achieve it, we need to update the 'pinmux' property
accordingly.

Note that replacing 'I2C0_SDA_GPIO21' by 'I2C0_SDA_GPIO33' is very tempting and
may even work, however, unless you have checked the hardware documentation first,
it is not recommended. That's because there are no guarantees that a particular
IO pin has the capability to route any specific signal.

The recommendation is to check the pinmux macros definitions available for the
target SoC in the following URL

https://github.com/zephyrproject-rtos/zephyr/tree/main/include/zephyr/dt-bindings/pinctrl

The ESP-WROVER-KIT board is based on the ESP32 SoC, in that case, we search
through the file 'esp32-pinctrl.h' in the above URL. Luckily for us, there is
one definition on that file that corresponds to our needs

    #define I2C0_SDA_GPIO33 \
            ESP32_PINMUX(33, ESP_I2CEXT0_SDA_IN, ESP_I2CEXT0_SDA_OUT)

Now, we go back to edit 'esp_wrover_kit-pinctrl.dtsi' and create a new pin state
on that file (or replace/update the one already defined) using the pinmux macro
definition above, yielding

    i2c0_default: i2c0_default {
            group1 {
                    pinmux = <I2C0_SDA_GPIO33>,
                             <I2C0_SCL_GPIO22>;
                    bias-pull-up;
                    drive-open-drain;
                    output-high;
            };
    };

With proper modifications, the same steps above apply when using different
combinations of boards, SoCs, peripherals and peripheral pins.

Note: Not all pins are available for a given peripheral, it depends if that
      pin supports a set of properties required by the target peripheral.

      When defining a state, the pin muxing information is constrained to
      the definitions at 'hal_espressif', however, pin properties (like
      bias-push-pull, drive-open-drain, etc) can be freely chosen, given the
      property is meaningful to the peripheral signal and that it is also
      available in the target GPIO.

      Another thing worth noting is that all pin properties should be grouped.
      All pins sharing common properties go under a common group (in the above
      example, all pins are in 'group1'). Other peripherals can have more than
      one group.
```

## Properties

### Top level properties

These property descriptions apply to “espressif,esp32-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “espressif,esp32-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `pinmux` | `array` | ```text Each array element represents pin muxing information of an individual pin. The array elements are pre-declared macros taken from Espressif's HAL. ```  This property is **required**. |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `output-enable` | `boolean` | ```text enable output on a pin without actively driving it (e.g. enable an output buffer) ``` |
| `output-low` | `boolean` | ```text set the pin to output mode with low level ``` |
| `output-high` | `boolean` | ```text set the pin to output mode with high level ``` |
