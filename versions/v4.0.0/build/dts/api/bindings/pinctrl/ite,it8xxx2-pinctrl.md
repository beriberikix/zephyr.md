---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/ite,it8xxx2-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/ite,it8xxx2-pinctrl.html
---

# ite,it8xxx2-pinctrl

Vendor: [ITE Tech. Inc.](../../bindings.md#dt-vendor-ite)

## Description

```text
The ITE IT8XXX2 pin controller is a node responsible for controlling
pin function selection and pin properties. For example, you can
use this node to route UART1 RX and TX setting the alternate
function on the pin.

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
  #include <dt-bindings/pinctrl/it8xxx2-pinctrl.h>

  &pinctrl {
    /* configuration for I2C0 default state */
    i2c0_clk_pb3_default: i2c0_clk_pb3_default {
            pinmuxs = <&pinctrlb 3 IT8XXX2_ALT_FUNC_1>;
            gpio-voltage = "1p8";
    };
    i2c0_data_pb4_default: i2c0_data_pb4_default {
            pinmuxs = <&pinctrlb 4 IT8XXX2_ALT_FUNC_1>;
            gpio-voltage = "1v8";
    };
    /* configuration for UART0 default state */
    uart1_rx_pb0_default: uart1_rx_pb0_default {
            pinmuxs = <&pinctrlb 0 IT8XXX2_ALT_FUNC_3>;
            bias-pull-up;
    };
    uart1_tx_pb1_default: uart1_tx_pb1_default {
            pinmuxs = <&pinctrlb 1 IT8XXX2_ALT_FUNC_3>;
    };
  };

The 'uart1_rx_pb0_default' child node encodes the pin configurations
for a particular state of a device; in this case, the default
(that is, active) state.

To link pin configurations with a device, use a pinctrl-N property for some
number N, like this example you could place in your board's DTS file:

  #include "board-pinctrl.dtsi"

  &uart0 {
    pinctrl-0 = <&uart1_rx_pb0_default &uart1_tx_pb1_default>;
    pinctrl-1 = <&uart1_rx_pb0_sleep &uart1_tx_pb1_sleep>;
    pinctrl-names = "default", "sleep";
  };
```

## Properties

### Top level properties

These property descriptions apply to “ite,it8xxx2-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ite,it8xxx2-pinctrl” compatible.

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
| `pinmuxs` | `phandle-array` | ```text ITE IT8XXX2 pin's configuration (pinctrl node, pin and function). ```  This property is **required**. |
| `gpio-voltage` | `string` | ```text Pin input voltage selection 3.3V or 1.8V. All gpio pins support 3.3V. This property only needs to be configured if the board specifies a pin as 1.8V. So the default is 3.3V. kSI[7:0] and KSO[15:0] pins only support 3.3V. ```  Default value: `3v3`  Legal values: `'3v3'`, `'1v8'` |
| `drive-strength` | `string` | ```text We can configure this property to drive a high or low current selection. If this property is not configured, it is the default setting. According to the SPEC, the default drive current selection varies from different pins. Define the high level 0b: 8mA            low  level 1b: 4mA or 2mA ```  Legal values: `'high'`, `'low'` |
| `bias-high-impedance` | `boolean` | ```text high impedance mode ("third-state", "floating") ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `bias-pull-pin-default` | `boolean` | ```text use pin's default pull state ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
