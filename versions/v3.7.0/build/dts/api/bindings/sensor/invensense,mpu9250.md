---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/sensor/invensense,mpu9250.html
original_path: build/dts/api/bindings/sensor/invensense,mpu9250.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# invensense,mpu9250 (on i2c bus)

Vendor: [InvenSense Inc.](../../bindings.md#dt-vendor-invensense)

## Description

```text
InvenSense MPU-9250 Nine-Axis (Gyro + Accelerometer + Compass). See more
info at https://www.invensense.com/products/motion-tracking/9-axis/mpu-9250/
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `irq-gpios` | `phandle-array` | ```text The INT signal default configuration is active-high.  The property value should ensure the flags properly describe the signal that is presented to the driver. This property is required when the trigger mode is used. ``` |
| `gyro-sr-div` | `int` | ```text Default gyrscope sample rate divider. This divider is only effective when gyro-dlpf is in range 5-184. rate = sample_rate / (1 + gyro-sr-div) Valid range: 0 - 255 ```  This property is **required**. |
| `gyro-dlpf` | `int` | ```text Default digital low pass filter frequency of gyroscope. Maps to DLPF_CFG field in Configuration setting. ```  This property is **required**.  Legal values: `250`, `184`, `92`, `41`, `20`, `10`, `5`, `3600` |
| `gyro-fs` | `int` | ```text Default full scale of gyroscope. (Unit - DPS). Maps to GYRO_FS_SEL field in Gyroscope Configuration setting. ```  This property is **required**.  Legal values: `250`, `500`, `1000`, `2000` |
| `accel-fs` | `int` | ```text Default full scale of accelerometer. (Unit - g) Maps to ACCEL_FS_SEL field in Accelerometer Configuration setting ```  This property is **required**.  Legal values: `2`, `4`, `8`, `16` |
| `accel-dlpf` | `string` | ```text Default digital low pass filter frequency of accelerometer. Maps to DLPF_CFG field in Accelerometer Configuration 2 setting. ```  This property is **required**.  Legal values: `'218.1'`, `'218.1a'`, `'99'`, `'44.8'`, `'21.2'`, `'10.2'`, `'5.05'`, `'420'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “invensense,mpu9250” compatible.

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
