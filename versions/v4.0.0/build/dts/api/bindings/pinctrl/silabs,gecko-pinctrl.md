---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/silabs,gecko-pinctrl.html
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
