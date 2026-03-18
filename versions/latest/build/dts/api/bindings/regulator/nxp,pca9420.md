---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/regulator/nxp,pca9420.html
original_path: build/dts/api/bindings/regulator/nxp,pca9420.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nxp,pca9420

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
NXP PCA9420 PMIC

The PMIC has two buck converters and two LDOs. All need to be defined as
children nodes, strictly following the BUCK1, BUCK2, LDO1 and LDO2 node names.
For example:

pmic@61 {
  reg = <0x61>;
  ...
  BUCK1 {
    /* all properties for BUCK1 */
  };
  BUCK2 {
    /* all properties for BUCK2 */
  };
  LDO1 {
    /* all properties for LDO1 */
  };
  LDO2 {
    /* all properties for LDO2 */
  };
};
```

## Properties

### Top level properties

These property descriptions apply to “nxp,pca9420”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `nxp,enable-modesel-pins` | `boolean` | ```text When enabled, the PMIC will be configured to allow mode selection using the MODESEL0/1 inputs. ``` |
| `nxp,vin-ilim-microamp` | `int` | ```text VIN input current limit, in microamperes. Value reflects typical value, below you can find min/typical/max values:  - 74 mA/85 mA/98 mA - 222 mA/255 mA/293 mA - 370 mA/425 mA/489 mA - 517 mA/595 mA/684 mA - 665 mA/765 mA/880 mA - 813 mA/935 mA/1075 mA - 961 mA/1105 mA/1271 mA  To disable current limit, set property to zero. Defaults to 425mA, the IC default value. ```  Default value: `425000`  Legal values: `85000`, `255000`, `425000`, `595000`, `765000`, `935000`, `1105000` |
| `nxp,asys-uvlo-sel-millivolt` | `int` | ```text ASYS UVLO (under voltage lock out) threshold, in millivolts. Defaults to 2700mV to match the IC default value. ```  Default value: `2700`  Legal values: `2400`, `2500`, `2600`, `2700` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,pca9420” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `enable-inverted` | `boolean` | ```text If the enable bit should be zero to turn the regulator on, add this property. ``` |
| `nxp,mode0-microvolt` | `int` | ```text The voltage level to be configured for mode 0, in microvolts. Setting this value to zero will disable the source in mode 0. ``` |
| `nxp,mode1-microvolt` | `int` | ```text The voltage level to be configured for mode 1, in microvolts. Setting this value to zero will disable the source in mode 1. ``` |
| `nxp,mode2-microvolt` | `int` | ```text The voltage level to be configured for mode 2, in microvolts. Setting this value to zero will disable the source in mode 2. ``` |
| `nxp,mode3-microvolt` | `int` | ```text The voltage level to be configured for mode 3, in microvolts. Setting this value to zero will disable the source in mode 3. ``` |
| `regulator-min-microvolt` | `int` | ```text smallest voltage consumers may set ``` |
| `regulator-max-microvolt` | `int` | ```text largest voltage consumers may set ``` |
| `regulator-always-on` | `boolean` | ```text boolean, regulator should never be disabled ``` |
| `regulator-boot-on` | `boolean` | ```text bootloader/firmware enabled regulator. It's expected that this regulator was left on by the bootloader. If the bootloader didn't leave it on then OS should turn it on at boot but shouldn't prevent it from being turned off later. This property is intended to only be used for regulators where software cannot read the state of the regulator. ``` |
