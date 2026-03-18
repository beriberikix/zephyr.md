---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/pinctrl/renesas,rcar-pfc.html
original_path: build/dts/api/bindings/pinctrl/renesas,rcar-pfc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# renesas,rcar-pfc

Vendor: [Renesas Electronics Corporation](../../bindings.md#dt-vendor-renesas)

## Description

```text
Renesas R-Car Pin Function Controller node
This binding gives a base representation of the R-Car pins configuration.
The R-Car pin controller is a singleton node responsible for controlling
pin function selection and pin properties. For example, you can use this
node to route CAN0 TX A to pin 'RD', and enable pull-up resistor as well
as driving ability.

The node has the 'pfc' node label set in your SoC's devicetree, so you can
modify it like this:

&pfc {
     /* your modifications go here */
};

All device pin configurations should be placed in child nodes of the
'pfc' node, as shown in this example:
  /* You can put this in places like a board-pinctrl.dtsi file in
   * your board directory, or a devicetree overlay in your application.
   */

  /* include pre-defined pins and functions for the SoC used by the board */
  #include <dt-bindings/pinctrl/renesas/pinctrl-r8a77951.h>

  &pfc {
    /* configuration for can0 data a tx default state */
    can0_data_a_tx_default: can0_data_a_tx_default {
      /* configure PIN_RD as FUNC_CAN0_TX_A */
      pin = <PIN_RD FUNC_CAN0_TX_A>;
    };
    /* configuration for can0 data a rx default state */
    can0_data_a_rx_default: can0_data_a_rx_default {
      /* configure PIN_RD_WR as FUNC_CAN0_RX_A */
      pin = <PIN_RD_WR FUNC_CAN0_RX_A>;
    };
  };

The 'can0_data_a_tx_default' child node encodes the pin configurations
for a particular state of a device; in this case, the default
(that is, active) state. You would specify the low-power configuration for
the same device in a separate child node.

A pin configuration can also specify pin properties such as the
'bias-pull-up' property. Here is a list of supported standard pin
properties:

- bias-disable
- bias-pull-down
- bias-pull-up
- drive-strength
- power-source

To link pin configurations with a device, use a pinctrl-N property for some
number N, like this example you could place in your board's DTS file:

  #include "board-pinctrl.dtsi"

  &can0 {
    pinctrl-0 = <&can0_data_a_tx_default &can0_data_a_rx_default>;
    pinctrl-1 = <&can0_data_a_tx_sleep &can0_data_a_rx_sleep>;
    pinctrl-names = "default", "sleep";
  };
```

## Properties

### Top level properties

These property descriptions apply to “renesas,rcar-pfc”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “renesas,rcar-pfc” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-strength` | `int` | ```text maximum sink or source current in mA ```  Legal values: `3`, `6`, `9`, `12`, `15`, `18`, `21`, `24` |
| `power-source` | `int` | ```text select between different power supplies ``` |
| `pin` | `array` | ```text The array is expected to have up to two elements. The first element is the pin the second optional element is the pin function. ```  This property is **required**. |
