---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/st,lsm9ds1.html
original_path: build/dts/api/bindings/sensor/st,lsm9ds1.html
---

# st,lsm9ds1 (on i2c bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/st/lsm9ds1/lsm9ds1.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm9ds1/lsm9ds1.c).

## Description

```text
STMicroelectronics LSM9DS1 9-axis IMU (Inertial Measurement Unit) sensor
accessed through I2C bus.

This binding describe only the inertial part : accelerometer and gyroscope.

When setting the accel-range, gyro-range, imu-odr properties in
a .dts or .dtsi file you may include lsm9ds1.h and use the macros
defined there.

Example:
#include <zephyr/dt-bindings/sensor/lsm9ds1.h>

lsm9ds1: lsm9ds1@0 {
  ...

  accel-range = <LSM9DS1_DT_FS_4G>;
  imu-odr   =  <LSM9DS1_IMU_14Hz9>;
  gyro-range = <LSM9DS1_DT_FS_2000DPS>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `accel-range` | `int` | ```text Range of the accelerometer. Unit : g. Default is power-up configuration.  - 0 # LSM9DS1_DT_FS_2G  (0.061 mg/LSB) - 1 # LSM9DS1_DT_FS_16G (0.732 mg/LSB) - 2 # LSM9DS1_DT_FS_4G  (0.122 mg/LSB) - 3 # LSM9DS1_DT_FS_8G  (0.244 mg/LSB) ```  Legal values: `0`, `1`, `2`, `3` |
| `gyro-range` | `int` | ```text Range in dps. Default is power-up configuration.  - 0 # LSM9DS1_DT_FS_245DPS  (8.75  mdps/LSB) - 1 # LSM9DS1_DT_FS_500DPS  (17.50 mdps/LSB) - 3 # LSM9DS1_DT_FS_2000DPS (70    mdps/LSB) ```  Legal values: `0`, `1`, `3` |
| `imu-odr` | `int` | ```text Specify the default accelerometer and gyroscope output data rate expressed in samples per second (Hz). Default is power-up configuration.  - 0x00 # LSM9DS1_IMU_OFF - 0x10 # LSM9DS1_GY_OFF_XL_10Hz - 0x20 # LSM9DS1_GY_OFF_XL_50Hz - 0x30 # LSM9DS1_GY_OFF_XL_119Hz - 0x40 # LSM9DS1_GY_OFF_XL_238Hz - 0x50 # LSM9DS1_GY_OFF_XL_476Hz - 0x60 # LSM9DS1_GY_OFF_XL_952Hz - 0x01 # LSM9DS1_XL_OFF_GY_14Hz9 - 0x02 # LSM9DS1_XL_OFF_GY_59Hz5 - 0x03 # LSM9DS1_XL_OFF_GY_119Hz - 0x04 # LSM9DS1_XL_OFF_GY_238Hz - 0x05 # LSM9DS1_XL_OFF_GY_476Hz - 0x06 # LSM9DS1_XL_OFF_GY_952Hz - 0x11 # LSM9DS1_IMU_14Hz9 - 0x22 # LSM9DS1_IMU_59Hz5 - 0x33 # LSM9DS1_IMU_119Hz - 0x44 # LSM9DS1_IMU_238Hz - 0x55 # LSM9DS1_IMU_476Hz - 0x66 # LSM9DS1_IMU_952Hz - 0x81 # LSM9DS1_XL_OFF_GY_14Hz9_LP - 0x82 # LSM9DS1_XL_OFF_GY_59Hz5_LP - 0x83 # LSM9DS1_XL_OFF_GY_119Hz_LP - 0x91 # LSM9DS1_IMU_14Hz9_LP - 0xA2 # LSM9DS1_IMU_59Hz5_LP - 0xB3 # LSM9DS1_IMU_119Hz_LP ```  Legal values: `0`, `16`, `32`, `48`, `64`, `80`, `96`, `1`, `2`, `3`, `4`, `5`, `6`, `17`, `34`, `51`, `68`, `85`, `102`, `129`, `130`, `131`, `145`, `162`, `179` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,lsm9ds1” compatible.

| Name | Type | Details |
| --- | --- | --- |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
