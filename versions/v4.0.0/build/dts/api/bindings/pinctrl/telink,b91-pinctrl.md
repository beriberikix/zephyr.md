---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/telink,b91-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/telink,b91-pinctrl.html
---

# telink,b91-pinctrl

Vendor: [Telink Semiconductor](../../bindings.md#dt-vendor-telink)

Note

An implementation of a driver matching this compatible is available in
[drivers/pinctrl/pinctrl\_b91.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_b91.c).

## Description

```text
The Telink B91 pin controller is a singleton node responsible for
controlling pin function selection and pin properties. For example, you can
use this node to route UART0 TX to pin PB2 and enable the pull-up resistor
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

  /* include pre-defined pins and functions for the SoC used by the board */
  #include <dt-bindings/pinctrl/b91-pinctrl.h>

  &pinctrl {
    /* configuration for UART0 TX default state */
    uart0_tx_pb2_default: uart0_tx_pb2_default {
      /* configure PB2 as B91_FUNC_C */
      pinmux = <B91_PINMUX_SET(B91_PORT_B, B91_PIN_2, B91_FUNC_C)>;
    };
    /* configuration for UART0 RX default state */
    uart0_rx_pb3_default: uart0_rx_pb3_default {
      /* configure PB2 as B91_FUNC_C */
      pinmux = <B91_PINMUX_SET(B91_PORT_B, B91_PIN_3, B91_FUNC_C)>;
    };
  };

The 'uart0_tx_pb2_default' child node encodes the pin configurations
for a particular state of a device; in this case, the default
(that is, active) state. You would specify the low-power configuration for
the same device in a separate child node.

A pin configuration can also specify pin properties such as the
'bias-pull-up' property. Here is a list of supported standard pin
properties:

- bias-disable
- bias-pull-down
- bias-pull-up

To link pin configurations with a device, use a pinctrl-N property for some
number N, like this example you could place in your board's DTS file:

  #include "board-pinctrl.dtsi"

  &uart0 {
    pinctrl-0 = <&uart0_tx_pb2_default &uart0_rx_pb3_default>;
    pinctrl-1 = <&uart0_tx_pb2_sleep &uart0_rx_pb3_sleep>;
    pinctrl-names = "default", "sleep";
  };
```

## Properties

### Top level properties

These property descriptions apply to “telink,b91-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pad-mul-sel` | `int` | ```text PinMux pad_mul_sel register value. Pin functions depend on it.  For instance: Function C of PB2 configs the pin to UART0_TX if pad_mul_sel is set to <1>. But, the same function configs the same pin to DAC_I_DAT2_I if pad_mul_sel is set to <0>.  Refer to the Telink TLSR9 specs to get more information about pins configuration. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “telink,b91-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `pinmux` | `int` | ```text Telink B91 pin's configuration (port, pin and function). ```  This property is **required**. |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
