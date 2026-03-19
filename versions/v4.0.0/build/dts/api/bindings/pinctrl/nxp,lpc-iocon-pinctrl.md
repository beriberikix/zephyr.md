---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/nxp,lpc-iocon-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/nxp,lpc-iocon-pinctrl.html
---

# nxp,lpc-iocon-pinctrl

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

These property descriptions apply to “nxp,lpc-iocon-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,lpc-iocon-pinctrl” compatible.

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
| `pinmux` | `array` | ```text Pin mux selection for this group. See the SOC level pinctrl header file in NXP's HAL for a defined list of these options. ```  This property is **required**. |
| `slew-rate` | `string` | ```text Pin output slew rate. Sets the SLEW field in the IOCON register. defaults to standard slew rate, due to this being the reset value of the field. 0 SLEW_0- standard mode, output slew rate is slower 1 SLEW_1- fast mode, output slew rate is faster ```  Default value: `standard`  Legal values: `'standard'`, `'fast'` |
| `nxp,invert` | `boolean` | ```text Invert the pin input logic level ``` |
| `nxp,analog-mode` | `boolean` | ```text Set the pin to analog mode. Sets DIGIMODE=0, and ASW=1. Only valid for analog type pins. Selects ASW0 on LPC55s3x family ``` |
| `nxp,analog-alt-mode` | `boolean` | ```text Select the pin's alternate analog mode. Valid on LPC55s3x family SOCs when DIGIMODE=0. Only valid for analog type pins. Sets ASW1. ``` |
| `power-source` | `string` | ```text Pin output power source. Only valid for I2C mode pins running in I2C mode. ```  Legal values: `'3v3'`, `'1v8'` |
| `nxp,digital-filter` | `boolean` | ```text Digital input filter. Noise pulses below 10ms are filtered out. ``` |
| `nxp,i2c-filter` | `string` | ```text I2C glitch filter speed. Only valid for I2C mode pins. Fast mode typically only required for High speed I2C. ```  Legal values: `'slow'`, `'fast'` |
| `nxp,i2c-speed` | `string` | ```text I2C speed. Only valid for I2C mode pins. Fast mode should be used for fast mode plus I2C. ```  Legal values: `'slow'`, `'fast'` |
| `nxp,i2c-pullup` | `boolean` | ```text Enable I2C pullup resistor. If not present, pin is open drain in I2C mode. Only valid for I2C mode pins in I2C mode ``` |
| `nxp,i2c-mode` | `boolean` | ```text Enable I2C mode for a pin. If not present, pin is in GPIO mode. Only valid for I2C mode pins ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `input-schmitt-enable` | `boolean` | ```text enable schmitt-trigger mode ``` |
