---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/pinctrl/nxp,rt-iocon-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/nxp,rt-iocon-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nxp,rt-iocon-pinctrl

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
RT600/RT500 pin control node. This node defines pin configurations in pin
groups, and has the 'pinctrl' node identifier in the SOC's devicetree. Each
group within the pin configuration defines a peripheral's pin configuration.
Each numbered subgroup represents pins with shared configuration for that
peripheral. The 'pinmux' property of each group selects the pins to be
configured with these properties. For example, here is a configuration
for FLEXCOMM0 pins:

pinmux_flexcomm0_usart: pinmux_flexcomm0_usart {
  group0 {
    pinmux = <FC0_TXD_SCL_MISO_WS_PIO0_1>,
            <FC0_RXD_SDA_MOSI_DATA_PIO0_2>;
    slew-rate = "normal";
    drive-strength = "normal";
  };
};

If only the required properties are supplied, the ICON_PIO register will
be assigned the following values:
IOCON_FUNC=<pin mux selection>,
IOCON_PUPDENA = 0,
IOCON_PUPDSEL = 0,
IOCON_IBENA = 0,
IOCON_SLEWRATE = <slew-rate selection>,
IOCON_FULLDRIVE = <drive-strength selection>,
IOCON_AMENA = 0,
IOCON_ODENA = 0,
IOCON_IIENA = 0,

Note the inherited pinctrl properties defined below have the following effects:
drive-open-drain: IOCON_ODENA=1
bias-pull-up: IOCON_PUPDENA=1, IOCON_PUPSEL=1
bias-pull-down: IOCON_PUPDENA=1, IOCON_PUPSEL=0
input-enable: IOCON_IBENA=1
```

## Properties

### Top level properties

These property descriptions apply to “nxp,rt-iocon-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,rt-iocon-pinctrl” compatible.

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
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `pinmux` | `array` | ```text Pin mux selection for this group. See the SOC level pinctrl header file in NXP's HAL for a defined list of these options. ```  This property is **required**. |
| `slew-rate` | `string` | ```text Pin output slew rate. Sets the SLEWRATE field in the IOCON register. 0 SLEWRATE_0- normal mode, output slew rate is standard 1 SLEWRATE_1- slow mode, output slew rate is slower ```  This property is **required**.  Legal values: `'normal'`, `'slow'` |
| `drive-strength` | `string` | ```text Pin output drive strength. Sets the FULLDRIVE field in the IOCON register. 0 FULLDRIVE_0- Normal output drive mode 1 FULLDRIVE_1- Full output drive mode, output strength is twice the drive strength of normal drive mode. ```  This property is **required**.  Legal values: `'normal'`, `'high'` |
| `nxp,invert` | `boolean` | ```text Invert the pin input logic level ``` |
| `nxp,analog-mode` | `boolean` | ```text Set the pin to analog mode. Sets AMENA=1 ``` |
