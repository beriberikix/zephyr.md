---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/regulator/regulator-gpio.html
original_path: build/dts/api/bindings/regulator/regulator-gpio.html
---

# regulator-gpio

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

Note

An implementation of a driver matching this compatible is available in
[drivers/regulator/regulator\_gpio.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/regulator_gpio.c).

## Description

```text
GPIO-controlled voltage of regulators

Example of dts node:
  vccq_sd0: regulator-vccq-sd0 {
    compatible = "regulator-gpio";

    regulator-name = "SD0 VccQ";
    regulator-min-microvolt = <1800000>;
    regulator-max-microvolt = <3300000>;

    enable-gpios = <&gpio5 3 GPIO_ACTIVE_HIGH>;

    gpios = <&gpio5 1 GPIO_ACTIVE_HIGH>, <&gpio5 2 GPIO_ACTIVE_HIGH>;
    states = <3300000 2>, <2700000 1>, <1800000 0>;

    regulator-boot-on;
  };

In the above example, three GPIO pins are used for controlling the regulator:
  * two of them for controlling voltage;
  * third for enabling/disabling the regulator.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `regulator-name` | `string` | ```text A string used as a descriptive name for regulator outputs ```  This property is **required**. |
| `gpios` | `phandle-array` | ```text GPIO to use to switch voltage. ```  This property is **required**. |
| `states` | `array` | ```text Selection of available voltages provided by this regulator and matching GPIO configurations to achieve them. If there are no states in the "states" array, use a fixed regulator instead. First value in an array item is voltage in microvolts and the second is GPIO group state value. ``` |
| `enable-gpios` | `phandle-array` | ```text GPIO to use to enable/disable the regulator.  Unlike the gpio property in the Linux bindings this array must provide the GPIO polarity and open-drain status in the phandle selector. The Linux enable-active-high and gpio-open-drain properties are not valid for Zephyr devicetree files. Moreover, the driver isn't capable of working with more than one GPIO and this property does not have a state array. The driver simply sets or clears the appropriate GPIO bit when it is requested to enable or disable the regulator.  Example:   enable-gpios = <&gpio5 2 GPIO_ACTIVE_HIGH>; ``` |
| `regulator-init-microvolt` | `int` | ```text Voltage set during initialisation ``` |
| `regulator-min-microvolt` | `int` | ```text smallest voltage consumers may set ``` |
| `regulator-max-microvolt` | `int` | ```text largest voltage consumers may set ``` |
| `regulator-always-on` | `boolean` | ```text boolean, regulator should never be disabled ``` |
| `regulator-boot-on` | `boolean` | ```text bootloader/firmware enabled regulator. It's expected that this regulator was left on by the bootloader. If the bootloader didn't leave it on then OS should turn it on at boot but shouldn't prevent it from being turned off later. This property is intended to only be used for regulators where software cannot read the state of the regulator. ``` |
| `startup-delay-us` | `int` | ```text Startup time, in microseconds ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “regulator-gpio” compatible.

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
