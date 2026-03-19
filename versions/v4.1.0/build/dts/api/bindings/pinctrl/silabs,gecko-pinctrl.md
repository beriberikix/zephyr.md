---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/pinctrl/silabs,gecko-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/silabs,gecko-pinctrl.html
---

# silabs,gecko-pinctrl

Vendor: [Silicon Laboratories](../../bindings.md#dt-vendor-silabs)

## Description

```text
The Silabs pin controller is a singleton node responsible for controlling
pin function selection and pin properties. For example, you can use this
node to route UART0 RX to pin P0.1 and enable the pull-up resistor on the
pin.

The node has the 'pinctrl' node label set in your SoC's devicetree,
so you can modify it like this:

  &pinctrl {
          /* your modifications go here */
  };

All device pin configurations should be placed in child nodes of the
'pinctrl' node, as shown in this example:

  /* You can put this in places like a board-pinctrl.dtsi file in
   * your board directory, or a devicetree overlay in your application.
   */
  &pinctrl {
    /* configuration for usart0 device, default state */
    usart0_default: usart0_default {
      /* group 1 ('group1' name is arbitrary) */
      group1 {
        /* configure P0.1 as UART_TX and P0.2 as UART_RTS */
        psels = <GECKO_PSEL(UART_TX, A, 1)>, <GECKO_PSEL(UART_RTS, A, 2)>;
      };
      /* group 2 */
      group2 {
        /* configure P0.3 as UART_RX and P0.4 as UART_CTS */
        psels = <GECKO_PSEL(UART_RX, A, 3)>, <GECKO_PSEL(UART_CTS, A, 4)>;
      };
    };
  };

The 'usart0_default' child node encodes the pin configurations for a
particular state of a device; in this case, the default (that is, active)
state. You would specify the low-power configuration for the same device
in a separate child node.

As shown, pin configurations are organized in groups within each child node.
Each group can specify a list of pin function selections in the 'psels'
property. The GECKO_PSEL macro is used to specify a pin function selection.
Available pin functions can be found in the
include/dt-bindings/pinctrl/gecko-pinctrl.h header file.

To link this pin configuration with a device, use a pinctrl-N property
for some number N, like this example you could place in your board's DTS
file:

   #include "board-pinctrl.dtsi"

   &usart0 {
         pinctrl-0 = <&usart0_default>;
         pinctrl-names = "default";
   };
```

## Properties

### Top level properties

These property descriptions apply to “silabs,gecko-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “silabs,gecko-pinctrl” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-high-impedance` | `boolean` | ```text high impedance mode ("third-state", "floating") ``` |
| `bias-bus-hold` | `boolean` | ```text latch weakly ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `bias-pull-pin-default` | `boolean` | ```text use pin's default pull state ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `drive-open-source` | `boolean` | ```text drive with open source (hardware OR) ``` |
| `drive-strength` | `int` | ```text maximum sink or source current in mA ``` |
| `drive-strength-microamp` | `int` | ```text maximum sink or source current in μA ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `input-disable` | `boolean` | ```text disable input on pin (e.g. disable an input buffer, no effect on output) ``` |
| `input-schmitt-enable` | `boolean` | ```text enable schmitt-trigger mode ``` |
| `input-schmitt-disable` | `boolean` | ```text disable schmitt-trigger mode ``` |
| `input-debounce` | `int` | ```text Takes the debounce time in μsec, as argument or 0 to disable debouncing ``` |
| `power-source` | `int` | ```text select between different power supplies ``` |
| `low-power-enable` | `boolean` | ```text enable low power mode ``` |
| `low-power-disable` | `boolean` | ```text disable low power mode ``` |
| `output-disable` | `boolean` | ```text disable output on a pin (e.g. disable an output buffer) ``` |
| `output-enable` | `boolean` | ```text enable output on a pin without actively driving it (e.g. enable an output buffer) ``` |
| `output-low` | `boolean` | ```text set the pin to output mode with low level ``` |
| `output-high` | `boolean` | ```text set the pin to output mode with high level ``` |
| `sleep-hardware-state` | `boolean` | ```text indicate this is sleep related state which will be programmed into the registers for the sleep state ``` |
| `slew-rate` | `int` | ```text set the slew rate ``` |
| `skew-delay` | `int` | ```text This affects the expected clock skew on input pins and the delay before latching a value to an output pin. Typically indicates how   many double-inverters are used to delay the signal. ``` |

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `psels` | `array` | ```text An array of pins sharing the same group properties. The pins should be defined using the GECKO_PSEL utility macro that encodes the port, pin and function. ```  This property is **required**. |
