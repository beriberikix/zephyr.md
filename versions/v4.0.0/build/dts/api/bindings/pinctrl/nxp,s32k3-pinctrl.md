---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/nxp,s32k3-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/nxp,s32k3-pinctrl.html
---

# nxp,s32k3-pinctrl

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
NXP S32 pinctrl node for S32K3 SoCs.

The NXP S32 pin controller is a singleton node responsible for controlling
the pin function selection and pin properties. This node, labeled 'pinctrl' in
the SoC's devicetree, will define pin configurations in pin groups. Each group
within the pin configuration defines the pin configuration for a peripheral,
and each numbered subgroup in the pin group defines all the pins for that
peripheral with the same configuration properties. The 'pinmux' property in
a group selects the pins to be configured, and the remaining properties set
configuration values for those pins.

For example, to configure the pinmux for UART0, modify the 'pinctrl' from your
board or application devicetree overlay as follows:

  /* Include the SoC package header containing the predefined pins definitions */
  #include <nxp/s32/S32K344-257BGA-pinctrl.h>

  &pinctrl {
    uart0_default: uart0_default {
      group1 {
        pinmux = <PTA3_LPUART0_TX_O>;
        output-enable;
      };
      group2 {
        pinmux = <PTA28_LPUART0_RX>;
        input-enable;
      };
    };
  };

The 'uart0_default' node contains the pin configurations for a particular state
of a device. The 'default' state is the active state. Other states for the same
device can be specified in separate child nodes of 'pinctrl'.

In addition to 'pinmux' property, each group can contain other properties such as
'bias-pull-up' or 'slew-rate' that will be applied to all the pins defined in
'pinmux' array. To enable the input buffer use 'input-enable' and to enable the
output buffer use 'output-enable'.

To link the pin configurations with UART0 device, use pinctrl-N property in the
device node, where 'N' is the zero-based state index (0 is the default state).
Following previous example:

  &uart0 {
    pinctrl-0 = <&uart0_default>;
    pinctrl-names = "default";
    status = "okay";
  };

If only the required properties are supplied, the pin configuration register
will be assigned the following values:
  - input and output buffers disabled
  - internal pull not enabled
  - slew rate "fastest"
  - invert disabled
  - drive strength disabled.

Additionally, following settings are currently not supported and default to
the values indicated below:
  - Safe Mode Control (disabled)
  - Pad Keeping (disabled)
  - Input Filter (disabled).
```

## Properties

### Top level properties

These property descriptions apply to “nxp,s32k3-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,s32k3-pinctrl” compatible.

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
| `pinmux` | `array` | ```text An array of pins sharing the same group properties. The pins must be defined using the S32_PINMUX macros that encodes all the pin muxing information in a 32-bit value. ```  This property is **required**. |
| `slew-rate` | `string` | ```text Slew rate control. Can be either slowest or fastest setting. See the SoC reference manual for applicability of this setting. ```  Default value: `fastest`  Legal values: `'fastest'`, `'slowest'` |
| `nxp,invert` | `boolean` | ```text Invert the signal selected by Source Signal Selection (SSS) before transmitting it to the associated destination (chip pin or module port). ``` |
| `nxp,drive-strength` | `boolean` | ```text Drive strength enable. See the SoC reference manual for applicability of this setting. ``` |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `output-enable` | `boolean` | ```text enable output on a pin without actively driving it (e.g. enable an output buffer) ``` |
