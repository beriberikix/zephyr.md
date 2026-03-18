---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/sensor/st,lsm6dso32-i2c.html
original_path: build/dts/api/bindings/sensor/st,lsm6dso32-i2c.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# st,lsm6dso32 (on i2c bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STMicroelectronics LSM6DSO32 6-axis IMU (Inertial Measurement Unit) sensor
accessed through I2C bus
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `irq-gpios` | `phandle-array` | ```text DRDY pin  This pin defaults to active high when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `int-pin` | `int` | ```text Select DRDY pin number (1 or 2).  This number represents which of the two interrupt pins (INT1 or INT2) the drdy line is attached to. This property is not mandatory and if not present it defaults to 1 which is the configuration at power-up. ```  Default value: `1`  Legal values: `1`, `2` |
| `accel-pm` | `int` | ```text Specify the accelerometer power mode. Default is power-up configuration.  - 0 # LSM6DSO_DT_XL_HP_MODE - 1 # LSM6DSO_DT_XL_LP_NORMAL_MODE - 2 # LSM6DSO_DT_XL_ULP_MODE ```  Legal values: `0`, `1`, `2` |
| `accel-range` | `int` | ```text Range in g. Default is power-up configuration.  - 0 # LSM6DSO_DT_FS_2G  (0.061 mg/LSB) (LSM6DSO32 will be double these values) - 1 # LSM6DSO_DT_FS_16G (0.488 mg/LSB) - 2 # LSM6DSO_DT_FS_4G  (0.122 mg/LSB) - 3 # LSM6DSO_DT_FS_8G  (0.244 mg/LSB) ```  Legal values: `0`, `1`, `2`, `3` |
| `accel-odr` | `int` | ```text Specify the default accelerometer output data rate expressed in samples per second (Hz). Default is power-up configuration.  - 0  # LSM6DSO_DT_ODR_OFF - 1  # LSM6DSO_DT_ODR_12Hz5 - 2  # LSM6DSO_DT_ODR_26H - 3  # LSM6DSO_DT_ODR_52Hz - 4  # LSM6DSO_DT_ODR_104Hz - 5  # LSM6DSO_DT_ODR_208Hz - 6  # LSM6DSO_DT_ODR_417Hz - 7  # LSM6DSO_DT_ODR_833Hz - 8  # LSM6DSO_DT_ODR_1667Hz - 9  # LSM6DSO_DT_ODR_3333Hz - 10 # LSM6DSO_DT_ODR_6667Hz - 11 # LSM6DSO_DT_ODR_1Hz6 ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11` |
| `gyro-pm` | `int` | ```text Specify the gyrometer power mode. Default is power-up configuration.  - 0 # LSM6DSO_DT_GY_HP_MODE - 1 # LSM6DSO_DT_GY_NORMAL_MODE ```  Legal values: `0`, `1` |
| `gyro-range` | `int` | ```text Range in dps. Default is power-up configuration.  - 0 # LSM6DSO_DT_FS_250DPS  (8.75 mdps/LSB) - 1 # LSM6DSO_DT_FS_125DPS  (4.375 mdps/LSB) - 2 # LSM6DSO_DT_FS_500DPS  (17.50 mdps/LSB) - 4 # LSM6DSO_DT_FS_1000DPS (35 mdps/LSB) - 6 # LSM6DSO_DT_FS_2000DPS (70 mdps/LSB) ```  Legal values: `0`, `1`, `2`, `4`, `6` |
| `gyro-odr` | `int` | ```text Specify the default gyro output data rate expressed in samples per second (Hz). Default is power-up configuration.  - 0  # LSM6DSO_DT_ODR_OFF - 1  # LSM6DSO_DT_ODR_12Hz5 - 2  # LSM6DSO_DT_ODR_26H - 3  # LSM6DSO_DT_ODR_52Hz - 4  # LSM6DSO_DT_ODR_104Hz - 5  # LSM6DSO_DT_ODR_208Hz - 6  # LSM6DSO_DT_ODR_417Hz - 7  # LSM6DSO_DT_ODR_833Hz - 8  # LSM6DSO_DT_ODR_1667Hz - 9  # LSM6DSO_DT_ODR_3333Hz - 10 # LSM6DSO_DT_ODR_6667Hz ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |
| `drdy-pulsed` | `boolean` | ```text Selects the pulsed mode for data-ready interrupt when enabled, and the latched mode when disabled. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,lsm6dso32” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
