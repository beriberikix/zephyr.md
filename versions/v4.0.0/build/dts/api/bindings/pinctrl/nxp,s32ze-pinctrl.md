---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/nxp,s32ze-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/nxp,s32ze-pinctrl.html
---

# nxp,s32ze-pinctrl

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
NXP S32 pinctrl node for S32Z/E SoCs.

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
  #include <nxp/s32/S32Z27-BGA594-pinctrl.h>

  &pinctrl {
    uart0_default: uart0_default {
      group1 {
        pinmux = <PB10_LIN_0_TX>;
        output-enable;
      };
      group2 {
        pinmux = <PB11_LIN_0_RX>;
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
will be assigned the following reset values:
  - input and output buffers disabled
  - internal pull not enabled
  - open drain disabled
  - slew rate 4 (see description in property below).
  - termination resistor disabled (affect LVDS pads only).
  - current reference control disabled (affect LVDS pads only).
  - Rx current boost disabled  (affect LVDS pads only).

Additionally:
- Safe Mode is always kept as reset value (disabled).
- Receiver Select is always kept as reset value (enables the differential vref based receiver).
```

## Properties

### Top level properties

These property descriptions apply to “nxp,s32ze-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,s32ze-pinctrl” compatible.

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
| `pinmux` | `array` | ```text An array of pins sharing the same group properties. The pins must be defined using the macros from the SoC package header. These macros encode all the pin muxing information in a 32-bit value. ```  This property is **required**. |
| `slew-rate` | `int` | ```text Slew rate control. Reset value is 4. - For 3.3 V / 1.8 V FAST pads:   0: FMAX_3318 = 208 MHz (at 1.8 V), 166 MHz (at 3.3 V)   4: FMAX_3318 = 166 MHz (at 1.8 V), 150 MHz (at 3.3 V)   5: FMAX_3318 = 150 MHz (at 1.8 V), 133 MHz (at 3.3 V)   6: FMAX_3318 = 133 MHz (at 1.8 V), 100 MHz (at 3.3 V)   7: FMAX_3318 = 100 MHz (at 1.8 V), 83 MHz (at 3.3 V) - For 1.8 V GPIO pads:   0: FMAX_18 = 208 MHz   4: FMAX_18 = 150 MHz   5: FMAX_18 = 133 MHz   6: FMAX_18 = 100 MHz   7: FMAX_18 = 50 MHz - For 3.3 V GPIO pads:   0: Reserved   4: FMAX_33 = 50 MHz   5: FMAX_33 = 50 MHz   6: FMAX_33 = 50 MHz   7: FMAX_33 = 1 MHz ```  Default value: `4`  Legal values: `0`, `4`, `5`, `6`, `7` |
| `nxp,current-reference-control` | `boolean` | ```text This configuration applies the current reference control to the associated pin. It is only applicable to LVDS pads and has no effect on other types of pads ``` |
| `nxp,termination-resistor` | `boolean` | ```text This configuration applies the termination resistor to the associated pin. It is only applicable to LVDS pads and has no effect on other types of pads ``` |
| `nxp,rx-current-boost` | `boolean` | ```text RX LVDS Current Boost Boosts RX IO current. It is only applicable to LVDS pads and has no effect on other types of pads 0: Current reference is 200 μA; supports data rate up to 320 Mbaud 1: Current reference is 1 mA; supports data rate up to 420 Mbaud ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `output-enable` | `boolean` | ```text enable output on a pin without actively driving it (e.g. enable an output buffer) ``` |
