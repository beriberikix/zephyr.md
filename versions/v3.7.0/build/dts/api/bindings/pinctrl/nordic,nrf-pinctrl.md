---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/nordic,nrf-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nordic,nrf-pinctrl

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
The nRF pin controller is a singleton node responsible for controlling
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
    /* configuration for uart0 device, default state */
    uart0_default: uart0_default {
      /* group 1 ('group1' name is arbitrary) */
      group1 {
        /* configure P0.1 as UART_TX and P0.2 as UART_RTS */
        psels = <NRF_PSEL(UART_TX, 0, 1)>, <NRF_PSEL(UART_RTS, 0, 2)>;
      };
      /* group 2 */
      group2 {
        /* configure P0.3 as UART_RX and P0.4 as UART_CTS */
        psels = <NRF_PSEL(UART_RX, 0, 3)>, <NRF_PSEL(UART_CTS, 0, 4)>;
        /* both P0.3 and P0.4 are configured with pull-up */
        bias-pull-up;
      };
    };
  };

The 'uart0_default' child node encodes the pin configurations for a
particular state of a device; in this case, the default (that is, active)
state. You would specify the low-power configuration for the same device
in a separate child node.

As shown, pin configurations are organized in groups within each child node.
Each group can specify a list of pin function selections in the 'psels'
property. The NRF_PSEL macro is used to specify a pin function selection.
If a pin needs to be explicitly disconnected, there is also the
NRF_PSEL_DISCONNECTED macro.
Available pin functions can be found in the
include/zephyr/dt-bindings/pinctrl/nrf-pinctrl.h header file.

A group can also specify shared pin properties common to all the specified
pins, such as the 'bias-pull-up' property in group 2. Here is a list of
supported standard pin properties:

- bias-disable: Disable pull-up/down (default behavior, not required).
- bias-pull-up: Enable pull-up resistor.
- bias-pull-down: Enable pull-down resistor.
- low-power-enable: Configure pin as an input with input buffer
  disconnected.

Note that bias options are mutually exclusive.

To link this pin configuration with a device, use a pinctrl-N property
for some number N, like this example you could place in your board's DTS
file:

   #include "board-pinctrl.dtsi"

   &uart0 {
         pinctrl-0 = <&uart0_default>;
         pinctrl-names = "default";
   };
```

## Properties

### Top level properties

These property descriptions apply to “nordic,nrf-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `low-power-enable` | `boolean` | ```text enable low power mode ``` |
| `psels` | `array` | ```text An array of pins sharing the same group properties. The pins should be defined using the NRF_PSEL utility macro that encodes the port, pin and function. NRF_PSEL_DISCONNECTED is also available to explicitly disconnect a pin. ```  This property is **required**. |
| `nordic,drive-mode` | `int` | ```text Pin output drive mode. Available drive modes are pre-defined in nrf-pinctrl.h. Note that extra modes may not be available on certain devices. Defaults to standard mode for 0 and 1 (NRF_DRIVE_S0S1), the SoC default, except for the "nordic,nrf-twi" and "nordic,nrf-twim" nodes where NRF_DRIVE_S0S1 is always overridden with NRF_DRIVE_S0D1 (standard '0', disconnect '1'). ``` |
| `nordic,invert` | `boolean` | ```text Invert pin polarity (set the active state to low). Only valid for PWM channel output pins. ``` |
