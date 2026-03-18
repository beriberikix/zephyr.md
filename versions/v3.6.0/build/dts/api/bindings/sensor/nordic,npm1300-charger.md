---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/sensor/nordic,npm1300-charger.html
original_path: build/dts/api/bindings/sensor/nordic,npm1300-charger.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nordic,npm1300-charger

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
NPM1300 PMIC Charger
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `term-microvolt` | `int` | ```text Charge termination voltage in uV. Available range is 3.5 V to 3.65 V and 4.0 V to 4.45 V in 50 mV steps. ```  This property is **required**. |
| `term-warm-microvolt` | `int` | ```text Charge termination voltage when warm in uV. Available range is 3.5 V to 3.65 V and 4.0 V to 4.45 V in 50 mV steps. If omitted, the term-microvolt value will be used. ``` |
| `current-microamp` | `int` | ```text Charge current in uA. Available range is 32 mA to 800 mA in 2mA steps. The value specified will be rounded down to the closest implemented value. ```  This property is **required**. |
| `dischg-limit-microamp` | `int` | ```text Discharge current limit in uA. Available range is 270 mA to 1340 mA in 3.23 mA steps. The value specified will be rounded down to the closest implemented value. ```  This property is **required**. |
| `vbus-limit-microamp` | `int` | ```text Vbus current limit in uA. Available values are 100 mA, or between 500 mA and 1500 mA in 100 mA steps. If omitted, the default value of 100 mA will be used. ``` |
| `thermistor-ohms` | `int` | ```text Thermistor nominal resistance type in ohms. ```  This property is **required**.  Legal values: `10000`, `47000`, `100000` |
| `thermistor-beta` | `int` | ```text Beta value of selected thermistor. ```  This property is **required**. |
| `thermistor-cold-millidegrees` | `int` | ```text Thermistor cold threshold in milli-degrees ``` |
| `thermistor-cool-millidegrees` | `int` | ```text Thermistor cool threshold in milli-degrees ``` |
| `thermistor-warm-millidegrees` | `int` | ```text Thermistor warm threshold in milli-degrees ``` |
| `thermistor-hot-millidegrees` | `int` | ```text Thermistor hot threshold in milli-degrees ``` |
| `charging-enable` | `boolean` | ```text Enable charging. ``` |
| `trickle-microvolt` | `int` | ```text Trickle voltage threshold in uV. Trickle charging is enabled below this value. If omitted the device default of 2.9V is used. ```  Default value: `2900000`  Legal values: `2900000`, `2500000` |
| `term-current-percent` | `int` | ```text Termination current, as a percentage of current-microamp. Charge completes when the charge current falls below this value. If omitted the device default of 10% is used. ```  Default value: `10`  Legal values: `10`, `20` |
| `vbatlow-charge-enable` | `boolean` | ```text Allow charging when below the vbatlow threshold. ``` |
| `disable-recharge` | `boolean` | ```text Disable automatic recharge. ``` |
| `dietemp-stop-millidegrees` | `int` | ```text Die temperature halt threshold in milli-degrees. When die temperature exceeds this threshold, charging will be inhibited. ``` |
| `dietemp-resume-millidegrees` | `int` | ```text Die temperature resume threshold in milli-degrees. When die temperature falls below this threshold, charging will be permitted. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,npm1300-charger” compatible.

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
