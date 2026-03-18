---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pinctrl/infineon,xmc4xxx-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/infineon,xmc4xxx-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# infineon,xmc4xxx-pinctrl

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

## Description

```text
The Infineon XMC4XXX pin controller is responsible for connecting peripheral outputs
to specific port/pins (also known as alternate functions) and configures pin properties.

The pinctrl settings are referenced in a device tree peripheral node. For example in a UART
node:

&usic1ch1 {
    compatible = "infineon,xmc4xxx-uart";
    pinctrl-0 = <&uart_tx_p0_1_u1c1 &uart_rx_p0_0_u1c1>;
    pinctrl-names = "default";
    input-src = "DX0D";
    ...
};

pinctrl-0 is the phandle that stores the pin settings for two pins: &uart_tx_p0_1_u1c1
and &uart_rx_p0_0_u1c1. These nodes are pre-defined and their naming convention is designed
to help the user select the correct pin settings. Note the use of peripheral type,
pin direction, port/pin number and USIC in the name.

The pre-defined nodes only set the alternate function of the output pin. The
configuration for the pin (i.e. drive strength) should be set in the board setup.
The set of possible configurations are defined in the properties section below (in addition
to the inherited property-allowlist list from pincfg-node.yaml).

To create a new pin configuration, the user may append to the &pinctrl node, for example

#include <zephyr/dt-bindings/pinctrl/xmc4xxx-pinctrl.h>
&pinctrl {
    my_node_config: my_node_config {
    pinmux = <XMC4XXX_PINMUX_SET(0, 1, 2)>;
    drive-push-pull;
      ... other supported pin configurations ..
};
where XMC4XXX_PINMUX_SET(PORT, PIN, ALTERNATE_FUNCTION) is a helper macro for setting the
alternate function for a given port/pin. Setting ALTERNATE_FUNCTION = 0 means that no
alternate function is selected.

The pinctrl driver only sets the alternate function for output pins. The input mux is
handled by the peripheral drivers. For example the &usic1ch1 node has input-src property for
this purpose. There are no pre-defined nodes for the input mux and this must be properly set
by the user. Refer to the peripheral .yaml file (i.e. infineon,xmc4xxx-uart.yaml) and
XMC4XXX documentation.
```

## Properties

### Top level properties

These property descriptions apply to “infineon,xmc4xxx-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,xmc4xxx-pinctrl” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `pinmux` | `int` | ```text Encodes port/pin and alternate function. See helper macro XMC4XX_PINMUX_SET(). Alternate function is only set for output pins; It selects  ALT1-ALT4 output line in the GPIO element. The alternate function for input pins is handled separately by the peripheral. It is upto the peripheral to configure which input pin to use (For example see parameter input-src in infineon,xmc4xxx-uart.yaml). ```  This property is **required**. |
| `drive-strength` | `string` | ```text Drive strength of the output pin. Following options as in XMC_GPIO_OUTPUT_STRENGTH See xmc4_gpio.h. This only has an effect if the pin is in drive-push-pull mode. ```  This property is **required**.  Legal values: `'strong-sharp-edge'`, `'strong-medium-edge'`, `'strong-soft-edge'`, `'strong-slow-edge'`, `'medium'`, `'medium-unknown1-edge'`, `'medium-unknown2-edge'`, `'weak'` |
| `invert-input` | `boolean` | ```text Inverts the input. ``` |
| `hwctrl` | `string` | ```text Pre-assigns hardware control of the pin to a certain peripheral. ```  This property is **required**.  Legal values: `'disabled'`, `'periph1'`, `'periph2'` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `output-low` | `boolean` | ```text set the pin to output mode with low level ``` |
| `output-high` | `boolean` | ```text set the pin to output mode with high level ``` |
