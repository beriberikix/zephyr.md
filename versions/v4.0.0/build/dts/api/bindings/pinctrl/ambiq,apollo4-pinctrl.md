---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/ambiq,apollo4-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/ambiq,apollo4-pinctrl.html
---

# ambiq,apollo4-pinctrl

Vendor: [Ambiq Micro, Inc.](../../bindings.md#dt-vendor-ambiq)

## Description

```text
The Ambiq Apollo4 pin controller is a node responsible for controlling
pin function selection and pin properties, such as routing a UART0 TX
to pin 60 and enabling the pullup resistor on that pin.

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
  #include <dt-bindings/pinctrl/ambiq-apollo4-pinctrl.h>

  &pinctrl {
    uart0_default: uart0_default {
      group1 {
        pinmux = <UART0TX_P60>;
      };
      group2 {
        pinmux = <UART0RX_P47>;
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
pins, such as the 'input-enable' property in group 2.
```

## Properties

### Top level properties

These property descriptions apply to “ambiq,apollo4-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ambiq,apollo4-pinctrl” compatible.

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
| `drive-strength` | `string` | ```text The drive strength of a pin, relative to full-driver strength. The default value is 0.1, which is the reset value. ```  Default value: `0.1`  Legal values: `'0.1'`, `'0.5'`, `'0.75'`, `'1.0'` |
| `slew-rate` | `string` | ```text Select slew rate for a pin. The default is slow, which is the reset value. ```  Default value: `slow`  Legal values: `'slow'`, `'fast'` |
| `ambiq,pull-up-ohms` | `int` | ```text The pullup resistor value. The default value is 1500 ohms. ```  Default value: `1500`  Legal values: `1500`, `6000`, `12000`, `24000`, `50000`, `100000` |
| `ambiq,iom-nce-module` | `int` | ```text IOM nCE module select, selects the SPI channel (CE) number (0-42).   0,     IOM0CE0 : IOM 0 NCE 0 module   1,     IOM0CE1 : IOM 0 NCE 1 module   2,     IOM0CE2 : IOM 0 NCE 2 module   3,     IOM0CE3 : IOM 0 NCE 3 module   4,     IOM1CE0 : IOM 1 NCE 0 module   5,     IOM1CE1 : IOM 1 NCE 1 module   6,     IOM1CE2 : IOM 1 NCE 2 module   7,     IOM1CE3 : IOM 1 NCE 3 module   8,     IOM2CE0 : IOM 2 NCE 0 module   9,     IOM2CE1 : IOM 2 NCE 1 module   10,    IOM2CE2 : IOM 2 NCE 2 module   11,    IOM2CE3 : IOM 2 NCE 3 module   12,    IOM3CE0 : IOM 3 NCE 0 module   13,    IOM3CE1 : IOM 3 NCE 1 module   14,    IOM3CE2 : IOM 3 NCE 2 module   15,    IOM3CE3 : IOM 3 NCE 3 module   16,    IOM4CE0 : IOM 4 NCE 0 module   17,    IOM4CE1 : IOM 4 NCE 1 module   18,    IOM4CE2 : IOM 4 NCE 2 module   19,    IOM4CE3 : IOM 4 NCE 3 module   20,    IOM5CE0 : IOM 5 NCE 0 module   21,    IOM5CE1 : IOM 5 NCE 1 module   22,    IOM5CE2 : IOM 5 NCE 2 module   23,    IOM5CE3 : IOM 5 NCE 3 module   24,    IOM6CE0 : IOM 6 NCE 0 module   25,    IOM6CE1 : IOM 6 NCE 1 module   26,    IOM6CE2 : IOM 6 NCE 2 module   27,    IOM6CE3 : IOM 6 NCE 3 module   28,    IOM7CE0 : IOM 7 NCE 0 module   29,    IOM7CE1 : IOM 7 NCE 1 module   30,    IOM7CE2 : IOM 7 NCE 2 module   31,    IOM7CE3 : IOM 7 NCE 3 module   32,    MSPI0CEN0 : MSPI 0 NCE 0 module   33,    MSPI0CEN1 : MSPI 0 NCE 1 module   34,    MSPI1CEN0 : MSPI 1 NCE 0 module   35,    MSPI1CEN1 : MSPI 1 NCE 1 module   36,    MSPI2CEN0 : MSPI 2 NCE 0 module   37,    MSPI2CEN1 : MSPI 2 NCE 1 module   38,    DC_DPI_DE : DC DPI DE module   39,    DISP_CONT_CSX : DISP CONT CSX module   40,    DC_SPI_CS_N : DC SPI CS_N module   41,    DC_QSPI_CS_N : DC QSPI CS_N module   42,    DC_RESX : DC module RESX If the pin is not a CE, this descriptor will be ignored. Default value 0, which is the reset value. ``` |
| `ambiq,iom-mspi` | `int` | ```text Indicates the module which uses specific CE pin, 1 if CE is IOM, 0 if MSPI. Default value 0, which is the reset value. If the pin is not a CE, this descriptor will be ignored. ``` |
| `ambiq,iom-num` | `int` | ```text Indicates the instance which uses specific CE pin. IOM number (0-7) or MSPI (0-2). Default value 0, which is the reset value. If the pin is not a CE, this descriptor will be ignored. ``` |
| `ambiq,interrupt-direction` | `int` | ```text Indicates the pininterrupt direction. Default value 0, which is the reset value. ``` |
| `bias-high-impedance` | `boolean` | ```text high impedance mode ("third-state", "floating") ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
