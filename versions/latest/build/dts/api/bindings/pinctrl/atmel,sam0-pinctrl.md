---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pinctrl/atmel,sam0-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/atmel,sam0-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# atmel,sam0-pinctrl

Vendor: [Atmel Corporation](../../bindings.md#dt-vendor-atmel)

## Description

```text
Atmel SAM0 Pinctrl container node

The Atmel SAM0 pin controller is a singleton node responsible for controlling
pin function selection and pin properties. For example, you can use this node
to route SERCOM0 as UART were RX to pin PAD1 and enable the pull-up resistor
on the pin.

The node has the 'pinctrl' node label set in your SoC's devicetree, so you can
modify it like this:

  &pinctrl {
          /* your modifications go here */
  };

All device pin configurations should be placed in child nodes of the 'pinctrl'
node, as shown in this example:

  /** You can put this in places like a <board>-pinctrl.dtsi file in
    * your board directory, or a devicetree overlay in your application.
    */

  /** include pre-defined combinations for the SoC variant used by the board */
  #include <dt-bindings/pinctrl/samr21g-pinctrl.h>

  &pinctrl {
    /* configuration for the usart0 "default" state */
    sercom0_uart_default: sercom0_uart_default {
      /* group 1 */
      group1 {
        /* configure PA6 as USART0 TX and PA8 as USART0 CTS */
        pinmux = <PA5D_SERCOM0_PAD1>, <PA6D_SERCOM0_PAD2>;
      };
      /* group 2 */
      group2 {
        /* configure PA5 as USART0 RX and PA7 as USART0 RTS */
        pinmux = <PA4D_SERCOM0_PAD0>, <PA7D_SERCOM0_PAD3>;
        /* both PA5 and PA7 have pull-up enabled */
        bias-pull-up;
      };
    };
  };

The 'usart0_default' child node encodes the pin configurations for a
particular state of a device; in this case, the default (that is, active)
state.

As shown, pin configurations are organized in groups within each child node.
Each group can specify a list of pin function selections in the 'pinmux'
property.

A group can also specify shared pin properties common to all the specified
pins, such as the 'bias-pull-up' property in group 2. Here is a list of
supported standard pin properties:

- bias-pull-up: Enable pull-up resistor.
- bias-pull-down: Enable pull-down resistor.
- drive-strength: Increase sink current.
- input-enable: Enable input on pin.
- output-enable: Enable output on a pin without actively driving it.

To link pin configurations with a device, use a pinctrl-N property for some
number N, like this example you could place in your board's DTS file:

  #include "board-pinctrl.dtsi"

  &usart0 {
        pinctrl-0 = <&usart0_default>;
        pinctrl-names = "default";
  };
```

## Properties

### Top level properties

These property descriptions apply to “atmel,sam0-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “atmel,sam0-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**.  Constant value: `1` |
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
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `pinmux` | `array` | ```text An array of pins sharing the same group properties. The pins should be defined using pre-defined macros or, alternatively, using the SAM_PINMUX utility macros depending on the pinmux model used by the SoC series. ```  This property is **required**. |
| `drive-strength` | `int` | ```text The drive strength controls the output driver strength of an I/O pin configured as an output.   0: Pin drive strength is set to normal drive strength.   1: Pin drive strength is set to stronger drive strength. ```  Legal values: `0`, `1` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `output-enable` | `boolean` | ```text enable output on a pin without actively driving it (e.g. enable an output buffer) ``` |
