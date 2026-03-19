---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/regulator/nordic,npm1300-regulator.html
original_path: build/dts/api/bindings/regulator/nordic,npm1300-regulator.html
---

# nordic,npm1300-regulator

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

Note

An implementation of a driver matching this compatible is available in
[drivers/regulator/regulator\_npm1300.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/regulator_npm1300.c).

## Description

```text
Nordic nPM1300 PMIC

The PMIC has two buck converters and two LDOs.
The regulators need to be defined as child nodes, strictly following the
BUCK1,2 LDO1..2, node names. For
example:

pmic@6b {
  reg = <0x6b>;
  ...
  regulators {
    compatible = "nordic,npm1300-regulator";

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
};
```

## Properties

### Top level properties

These property descriptions apply to “nordic,npm1300-regulator”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `dvs-gpios` | `phandle-array` | ```text List of SOC GPIOs connected to PMIC GPIOs. Set_dvs_mode will drive these pins as follows:   DVS mode 1 will enable the first pin   DVS mode 2 will enable the second pin   DVS mode 3 will drive the first and second pins   etc. The effect of the mode change is defined by the enable-gpios and pwm_gpios fields for each of the regulator blocks. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,npm1300-regulator” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `retention-microvolt` | `int` | ```text Retention mode voltage in microvolts. ``` |
| `enable-gpios` | `phandle-array` | ```text Regulator enable controlled by specified regulator GPIO pin. When set regulator must be enabled/disabled using set_dvs_mode. ``` |
| `pwm-gpios` | `phandle-array` | ```text Regulator enable controlled by specified regulator GPIO pin. When set regulator must be enabled/disabled using set_dvs_mode. ``` |
| `retention-gpios` | `phandle-array` | ```text Retention mode controlled by specified regulator GPIO pin. ``` |
| `soft-start-microamp` | `int` | ```text Soft start current limit in microamps. ```  Legal values: `10000`, `20000`, `35000`, `50000` |
| `regulator-init-microvolt` | `int` | ```text Voltage set during initialisation ``` |
| `regulator-min-microvolt` | `int` | ```text smallest voltage consumers may set ``` |
| `regulator-max-microvolt` | `int` | ```text largest voltage consumers may set ``` |
| `regulator-min-microamp` | `int` | ```text smallest current consumers may set ``` |
| `regulator-max-microamp` | `int` | ```text largest current consumers may set ``` |
| `regulator-always-on` | `boolean` | ```text boolean, regulator should never be disabled ``` |
| `regulator-boot-on` | `boolean` | ```text bootloader/firmware enabled regulator. It's expected that this regulator was left on by the bootloader. If the bootloader didn't leave it on then OS should turn it on at boot but shouldn't prevent it from being turned off later. This property is intended to only be used for regulators where software cannot read the state of the regulator. ``` |
| `regulator-boot-off` | `boolean` | ```text Regulator should be disabled on boot. ``` |
| `regulator-initial-mode` | `int` | ```text Initial operating mode. The set of possible operating modes depends on the capabilities of every hardware so each device binding documentation explains which values the regulator supports. ``` |
| `regulator-allowed-modes` | `array` | ```text List of operating modes that software is allowed to configure for the regulator at run-time. Elements may be specified in any order. The set of possible operating modes depends on the capabilities of every hardware so each device binding document explains which values the regulator supports. ``` |
| `startup-delay-us` | `int` | ```text Startup time, in microseconds ``` |
| `off-on-delay-us` | `int` | ```text Off to on delay time, in microseconds ``` |
