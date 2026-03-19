---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/st,lis2de12-i2c.html
original_path: build/dts/api/bindings/sensor/st,lis2de12-i2c.html
---

# st,lis2de12 (on i2c bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/st/lis2de12/lis2de12.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lis2de12/lis2de12.c).

## Description

```text
STMicroelectronics LIS2DE12 3-axis ultra-low power accelerometer sensor
accessed through I2C bus
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `int1-gpios` | `phandle-array` | ```text INT1 pin  This pin defaults to active high when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `int2-gpios` | `phandle-array` | ```text INT2 pin  This pin defaults to active high when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `accel-range` | `int` | ```text Range in g. Default is power-up configuration.  0 # LIS2DE12_DT_FS_2G  (15.6 mg/LSB) 1 # LIS2DE12_DT_FS_4G  (31.2 mg/LSB) 2 # LIS2DE12_DT_FS_8G  (62.5 mg/LSB) 3 # LIS2DE12_DT_FS_16G (187.5 mg/LSB) ```  Legal values: `0`, `1`, `2`, `3` |
| `accel-odr` | `int` | ```text Specify the default accelerometer output data rate expressed in samples per second (Hz). The values are taken in accordance to lis2de12_md_t enumerative in hal/st module. Please note that this values will also enable/disable High performance mode. Default is power-up configuration.  0x00 # LIS2DE12_DT_ODR_OFF 0x01 # LIS2DE12_DT_ODR_AT_1Hz 0x02 # LIS2DE12_DT_ODR_AT_10Hz 0x03 # LIS2DE12_DT_ODR_AT_25Hz 0x04 # LIS2DE12_DT_ODR_AT_50Hz 0x05 # LIS2DE12_DT_ODR_AT_100Hz 0x06 # LIS2DE12_DT_ODR_AT_200Hz 0x07 # LIS2DE12_DT_ODR_AT_400Hz 0x08 # LIS2DE12_DT_ODR_AT_1kHz620 0x09 # LIS2DE12_DT_ODR_AT_5kHz376 ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| `drdy-pulsed` | `boolean` | ```text Selects the pulsed mode for data-ready interrupt when enabled, and the latched mode when disabled. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,lis2de12” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text device address on i2c bus ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
