---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/sensor/ti,ina226.html
original_path: build/dts/api/bindings/sensor/ti,ina226.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ti,ina226 (on i2c bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

## Description

```text
TI INA226 Bidirectional Current and Power Monitor.
The <zephyr/dt-bindings/sensor/ina226.h> file should be included in the
DeviceTree as it provides macros that can be used for initializing the
configuration registers.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `avg-count` | `int` | ```text Number of samples to average (applies to all inputs). Default is the power-on reset value. ```  Default value: `1`  Legal values: `1`, `4`, `16`, `64`, `128`, `256`, `512`, `1024` |
| `vbus-conversion-time-us` | `int` | ```text Vbus conversion time in microseconds. Default is the power-on reset value. ```  Default value: `1100`  Legal values: `140`, `204`, `332`, `588`, `1100`, `2116`, `4156`, `8244` |
| `vshunt-conversion-time-us` | `int` | ```text Vshunt conversion time in microseconds. Default is the power-on reset value. ```  Default value: `1100`  Legal values: `140`, `204`, `332`, `588`, `1100`, `2116`, `4156`, `8244` |
| `operating-mode` | `string` | ```text Selects mode of operation. Default is the power-on reset value. ```  Default value: `Shunt and Bus, Continuous`  Legal values: `'Power-Down (or Shutdown)'`, `'Shunt Voltage, Triggered'`, `'Bus Voltage, Triggered'`, `'Shunt and Bus, Triggered'`, `'Power-Down (or Shutdown)'`, `'Shunt Voltage, Continuous'`, `'Bus Voltage, Continuous'`, `'Shunt and Bus, Continuous'` |
| `current-lsb-microamps` | `int` | ```text Current LSB value in microAmpere. This value gives the measurement resolution for current measurement. Formula: current-lsb [μA] = maximum expected current [μA] / 2^15 Higher resolution means lower range of current measurement, vice versa.  For example, if maximum expected current is 15 [A]:   then, current-lsb [μA] = 15000000 [μA] / 2^15 ~= 457.763 [μA].  Note: rounded values may be used for convenience, e.g. 500uA/LSB. ```  This property is **required**. |
| `rshunt-micro-ohms` | `int` | ```text Shunt resistor value in micro-ohms. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,ina226” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
