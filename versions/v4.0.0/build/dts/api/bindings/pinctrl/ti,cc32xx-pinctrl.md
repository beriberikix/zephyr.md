---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/ti,cc32xx-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/ti,cc32xx-pinctrl.html
---

# ti,cc32xx-pinctrl

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

Note

An implementation of a driver matching this compatible is available in
[drivers/pinctrl/pinctrl\_ti\_cc32xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_ti_cc32xx.c).

## Description

```text
The TI CC32XX pin controller is a singleton node responsible for controlling
pin function selection and pin properties. For example, you can
use this node to route UART0 RX to pin 55 and enable the pull-up resistor
on the pin.

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

  /* include pre-defined combinations for the SoC variant used by the board */
  #include <dt-bindings/pinctrl/gd32f450i(g-i-k)xx-pinctrl.h>

  &pinctrl {
    /* configuration for the uart0 "default" state */
    uart0_default: uart0_default {
      /* group 1 */
      group1 {
        /* configure pin 55 as UART0 TX and pin 61 as UART0 CTS */
        pinmux = <UART0_TX_P55>, <UART0_CTS_P61>;
      };
      /* group 2 */
      group2 {
        /* configure pin 57 as UART0 RX and pin 62 as UART0 RTS  */
        pinmux = <UART0_RX_P57>, <UART0_RTS_P62>;
        /* both pin 57 and 62 have pull-up enabled */
        bias-pull-up;
      };
    };

The 'uart0_default' child node encodes the pin configurations for a
particular state of a device; in this case, the default (that is, active)
state.

As shown, pin configurations are organized in groups within each child node.
Each group can specify a list of pin function selections in the 'pinmux'
property.

A group can also specify shared pin properties common to all the specified
pins, such as the 'bias-pull-up' property in group 2. Here is a list of
supported standard pin properties:

- drive-push-pull: Push-pull drive mode (default, not required).
- drive-open-drain: Open-drain drive mode.
- bias-disable: Disable pull-up/down (default, not required).
- bias-pull-up: Enable pull-up resistor.
- bias-pull-down: Enable pull-down resistor.
- drive-strength: Configure drive strength in mA (defaults to 6mA, IC default).

Note that drive and bias options are mutually exclusive.

To link pin configurations with a device, use a pinctrl-N property for some
number N, like this example you could place in your board's DTS file:

   #include "board-pinctrl.dtsi"

   &uart0 {
         pinctrl-0 = <&uart0_default>
         pinctrl-names = "default";
   };
```

## Properties

### Top level properties

These property descriptions apply to “ti,cc32xx-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,cc32xx-pinctrl” compatible.

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

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `pinmux` | `array` | ```text An array of pins sharing the same group properties. The pins should be defined using pre-defined macros or, alternatively, using the TI_CC32XX_PINMUX helper macro. ```  This property is **required**. |
| `drive-strength` | `int` | ```text maximum sink or source current in mA ```  Default value: `6`  Legal values: `0`, `2`, `4`, `6`, `8`, `10`, `12`, `14` |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
