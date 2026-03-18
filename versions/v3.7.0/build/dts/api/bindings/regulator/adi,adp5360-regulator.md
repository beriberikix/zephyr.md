---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/regulator/adi,adp5360-regulator.html
original_path: build/dts/api/bindings/regulator/adi,adp5360-regulator.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# adi,adp5360-regulator

Vendor: [Analog Devices, Inc.](../../bindings.md#dt-vendor-adi)

## Description

```text
Analog Devices ADP3560 PMIC

The PMIC has one buck converter and one buck-boost converter. Both need to be
defined as children nodes, strictly following the BUCK and BUCKBOOST node
names. For example:

pmic@46 {
  compatible = "adi,adp5360";
  reg = <0x46>;
  ...
  regulators {
    compatible = "adi,adp5360-regulator";

    BUCK {
      /* all properties for BUCK */
    };
    BUCKBOOST {
      /* all properties for BUCKBOOST */
    };
  };
};
```

## Properties

### Top level properties

These property descriptions apply to “adi,adp5360-regulator”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,adp5360-regulator” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `regulator-init-microvolt` | `int` | ```text Voltage set during initialisation ``` |
| `regulator-min-microvolt` | `int` | ```text smallest voltage consumers may set ``` |
| `regulator-max-microvolt` | `int` | ```text largest voltage consumers may set ``` |
| `regulator-always-on` | `boolean` | ```text boolean, regulator should never be disabled ``` |
| `regulator-boot-on` | `boolean` | ```text bootloader/firmware enabled regulator. It's expected that this regulator was left on by the bootloader. If the bootloader didn't leave it on then OS should turn it on at boot but shouldn't prevent it from being turned off later. This property is intended to only be used for regulators where software cannot read the state of the regulator. ``` |
| `regulator-boot-off` | `boolean` | ```text Regulator should be disabled on boot. ``` |
| `regulator-initial-mode` | `int` | ```text Initial operating mode. The set of possible operating modes depends on the capabilities of every hardware so each device binding documentation explains which values the regulator supports. ``` |
| `regulator-allowed-modes` | `array` | ```text List of operating modes that software is allowed to configure for the regulator at run-time. Elements may be specified in any order. The set of possible operating modes depends on the capabilities of every hardware so each device binding document explains which values the regulator supports. ``` |
| `adi,switch-delay-us` | `int` | ```text Switch delay time in hysteresis. ```  Legal values: `0`, `5`, `10`, `20` |
| `adi,soft-start-ms` | `int` | ```text Soft start time in milliseconds ```  Legal values: `1`, `8`, `64`, `512` |
| `adi,ilim-milliamp` | `int` | ```text Peak current limit, in milliamperes. Values above 400mA are only applicable to buck boost. ```  Legal values: `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800` |
| `adi,enable-stop-pulse` | `boolean` | ```text With this option selected and the buck/boost enabled, the buck/boost regulator can be stopped using the STP pin. ``` |
| `adi,enable-output-discharge` | `boolean` | ```text Enable output discharge functionality ``` |
