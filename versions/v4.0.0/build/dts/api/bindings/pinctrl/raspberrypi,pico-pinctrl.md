---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/raspberrypi,pico-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/raspberrypi,pico-pinctrl.html
---

# raspberrypi,pico-pinctrl

Vendor: [Raspberry Pi Foundation](../../bindings.md#dt-vendor-raspberrypi)

## Description

```text
The RPi Pico pin controller is a node responsible for controlling
pin function selection and pin properties, such as routing a UART0 Rx
to pin 1 and enabling the pullup resistor on that pin.

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
  #include <dt-bindings/pinctrl/rpi-pico-rp2040-pinctrl.h>

  &pinctrl {
    /* configuration for the usart0 "default" state */
    uart0_default: uart0_default {
      /* group 1 */
      group1 {
        /* configure P0 as UART0 TX */
        pinmux = <UART0_TX_P0>;
      };
      /* group 2 */
      group2 {
        /* configure P1 as UART0 RX */
        pinmux = <UART0_RX_P1>;
        /* enable input on pin 1 */
        input-enable;
      };
    };
  };

The 'uart0_default' child node encodes the pin configurations for a
particular state of a device; in this case, the default (that is, active)
state.

As shown, pin configurations are organized in groups within each child node.
Each group can specify a list of pin function selections in the 'pinmux'
property.

A group can also specify shared pin properties common to all the specified
pins, such as the 'input-enable' property in group 2. Here is a list of
supported standard pin properties:

- bias-disable: Disable pull-up/down (default, not required).
- bias-pull-up: Enable pull-up resistor.
- bias-pull-down: Enable pull-down resistor.
- input-enable: Enable input from the pin.
- input-schmitt-enable: Enable input hysteresis.
- drive-strength: Set the drive strength of the pin, in milliamps. Possible
  values are: 2, 4, 8, 12 (default: 4mA)
- slew-rate: If set to 0, slew rate is set to slow. If set to 1, it is set
  to fast.

To link pin configurations with a device, use a pinctrl-N property for some
number N, like this example you could place in your board's DTS file:

   #include "board-pinctrl.dtsi"

   &uart0 {
         pinctrl-0 = <&uart0_default>;
         pinctrl-1 = <&uart0_sleep>;
         pinctrl-names = "default", "sleep";
   };
```

## Properties

### Top level properties

These property descriptions apply to “raspberrypi,pico-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “raspberrypi,pico-pinctrl” compatible.

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
| `pinmux` | `array` | ```text An array of pins sharing the same group properties. Each element of the array is an integer constructed from the pin number and the alternative function of the pin. ```  This property is **required**. |
| `drive-strength` | `int` | ```text The drive strength of a pin, in mA. The default value is 4mA, as this is the power on reset value. ```  Default value: `4`  Legal values: `2`, `4`, `8`, `12` |
| `slew-rate` | `int` | ```text The slew rate of a pin. 0 corresponds to slow, and 1 corresponds to fast. The default value is 0 (slow), as this is the power on reset value. ```  Legal values: `0`, `1` |
| `raspberrypi,oe-override` | `int` | ```text Override output-enable for a pin.  - 0 (RP2_GPIO_OVERRIDE_NORMAL) - drive output enable from selected     peripheral signal. - 1 (RP2_GPIO_OVERRIDE_INVERT) - drive output enable from inverse of     selected peripheral signal. - 2 (RP2_GPIO_OVERRIDE_LOW) - disable output. - 3 (RP2_GPIO_OVERRIDE_HIGH) - enable output.  The default value is 0, as this is the power on reset value. ```  Legal values: `0`, `1`, `2`, `3` |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `input-schmitt-enable` | `boolean` | ```text enable schmitt-trigger mode ``` |
