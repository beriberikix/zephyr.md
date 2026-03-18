---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pinctrl/nxp,lpc11u6x-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/nxp,lpc11u6x-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nxp,lpc11u6x-pinctrl

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
LPC pinctrl node. This node defines pin configurations in pin groups, and has
the 'pinctrl' node identifier in the SOC's devicetree. Each group within the
pin configuration defines a peripheral's pin configuration. Each numbered
subgroup represents pins with shared configuration for that peripheral. The
'pinmux' property of each group selects the pins to be configured with these
properties. For example, here is a configuration for FLEXCOMM0 pins:

pinmux_flexcomm0_usart: pinmux_flexcomm0_usart {
  group0 {
    pinmux = <FC0_TXD_SCL_MISO_WS_PIO0_30>,
            <FC0_RXD_SDA_MOSI_DATA_PIO0_29>;
    slew-rate = "standard";
  };
};

If only the required properties are supplied, the ICON_PIO register will
be assigned the following values:
IOCON_FUNC=<pin mux selection>,
IOCON_MODE=0,
IOCON_SLEW=<slew-rate selection>,
IOCON_INVERT=0,
IOCON_DIGIMODE=1,
IOCON_OD=0,

Values for I2C type and analog type pins have the following defaults:
IOCON_ASW=0
IOCON_SSEL=0
IOCON_FILTEROFF=1
IOCON_ECS=0
IOCON_EGP=1
IOCON_I2CFILTER=1

Note the inherited pinctrl properties defined below have the following effects:
drive-open-drain: IOCON_OD=1
bias-pull-up: IOCON_MODE=2
bias-pull-down: IOCON_MODE=1
drive-push-pull: IOCON_MODE=3

Note: for the LPC11u6x, the following fields are also supported:
IOCON_HYS- set by input-schmitt-enable
IOCON_S_MODE- set by nxp,digital-filter
IOCON_CLKDIV- set by nxp,filter-clock-div
IOCON_FILTR- set by nxp,analog-filter
```

## Properties

### Top level properties

These property descriptions apply to “nxp,lpc11u6x-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,lpc11u6x-pinctrl” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `nxp,digital-filter` | `int` | ```text Enable digital filter. Set number of clock cycles to use as rejection threshold for input pulses. 0 disables the filter. Only valid for lpc11u6x SOC. Filter defaults to disabled, as this is default reset value for SOC ```  Legal values: `0`, `1`, `2`, `3` |
| `nxp,filter-clock-div` | `int` | ```text set peripheral clock divider for input filter sampling clock IOCONCLKDIV. Only valid for lpc11u6x SOC. Default to 0, as this is the default reset value for the SOC. ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6` |
| `nxp,disable-analog-filter` | `boolean` | ```text Disable fixed 10 ns input glitch analog filter. Only valid for lpc11u6x SOC, on analog pins. Note that this filter is enabled on reset, hence the choice to make disabling the filter opt-in ``` |
| `pinmux` | `array` | ```text Pin mux selection for this group. See the SOC level pinctrl header file in NXP's HAL for a defined list of these options. ```  This property is **required**. |
| `nxp,invert` | `boolean` | ```text Invert the pin input logic level ``` |
| `nxp,analog-mode` | `boolean` | ```text Set the pin to analog mode. Sets DIGIMODE=0, and ASW=1. Only valid for analog type pins. Selects ASW0 on LPC55s3x family ``` |
| `nxp,i2c-filter` | `string` | ```text I2C glitch filter speed. Only valid for I2C mode pins. Fast mode typically only required for High speed I2C. ```  Legal values: `'slow'`, `'fast'` |
| `nxp,i2c-mode` | `boolean` | ```text Enable I2C mode for a pin. If not present, pin is in GPIO mode. Only valid for I2C mode pins ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `input-schmitt-enable` | `boolean` | ```text enable schmitt-trigger mode ``` |
