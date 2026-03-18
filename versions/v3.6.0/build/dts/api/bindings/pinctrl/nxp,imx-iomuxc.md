---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.html
original_path: build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nxp,imx-iomuxc

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
This compatible binding should be applied to the device's iomuxc DTS node.
the DTS node will be populated with all pinmux options for the specific SOC.
These options can then be used in a pinctrl node with the "nxp,mcux-rt-pinctrl"
compatible string to define pin groups.

The user should not edit the bindings defined within this node to make pinmux
selections, but should instead edit the pinctrl groups for their board.
```

## Properties

### Top level properties

These property descriptions apply to “nxp,imx-iomuxc”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,imx-iomuxc” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `pinmux` | `array` | ```text An array of values defining the pin mux selection, in the following format: <mux_register, mux_val, input_reg, daisy_val, cfg_reg> mux_register: register that will be written to to make mux selection mux_val: value to write to mux_register input_reg: peripheral register that will direct peripheral signal to pin daisy_val: value to write to input_reg cfg_reg: register that will configure pin pull, drive strength, and open drain ```  This property is **required**. |
| `gpr` | `array` | ```text An array of values defining the GPR bit write required, if one exists. Some IOMUXC options require writing to an IOMUXC_GPR register to select them. This array has the following elements: <gpr_reg, gpr_shift, gpr_val> gpr_reg: GPR register address to write to gpr_shift: shift to apply to value before writing gpr_val: value to write ``` |
| `pin-pue` | `boolean` | ```text RT11xx parts have multiple types of IOMUXC registers defined, with different register layouts. This property can be set to indicate to the pinctrl driver the type of register this pinmux represents, and should not be modified by the user. ``` |
| `pin-pdrv` | `boolean` | ```text RT11xx parts have multiple types of IOMUXC registers defined, with different register layouts. This property can be set to indicate to the pinctrl driver the type of register this pinmux represents, and should not be modified by the user. ``` |
| `pin-lpsr` | `boolean` | ```text RT11xx parts have multiple types of IOMUXC registers defined, with different register layouts. This property can be set to indicate to the pinctrl driver the type of register this pinmux represents, and should not be modified by the user. ``` |
| `pin-snvs` | `boolean` | ```text RT11xx parts have multiple types of IOMUXC registers defined, with different register layouts. This property can be set to indicate to the pinctrl driver the type of register this pinmux represents, and should not be modified by the user. ``` |
