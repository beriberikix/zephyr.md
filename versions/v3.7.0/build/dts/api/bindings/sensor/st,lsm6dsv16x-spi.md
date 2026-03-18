---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/sensor/st,lsm6dsv16x-spi.html
original_path: build/dts/api/bindings/sensor/st,lsm6dsv16x-spi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,lsm6dsv16x (on spi bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STMicroelectronics LSM6DSV16X 6-axis IMU (Inertial Measurement Unit) sensor
accessed through SPI bus
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `int1-gpios` | `phandle-array` | ```text INT1 pin  This pin defaults to active high when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `int2-gpios` | `phandle-array` | ```text INT2 pin  This pin defaults to active high when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `drdy-pin` | `int` | ```text Select DRDY pin number (1 or 2).  This number represents which of the two interrupt pins (INT1 or INT2) the drdy line is attached to. This property is not mandatory and if not present it defaults to 1 which is the configuration at power-up. ```  Default value: `1`  Legal values: `1`, `2` |
| `accel-range` | `int` | ```text Range in g. Default is power-up configuration.  - 0 # LSM6DSV16X_DT_FS_2G  (0.061 mg/LSB) - 1 # LSM6DSV16X_DT_FS_4G  (0.122 mg/LSB) - 2 # LSM6DSV16X_DT_FS_8G  (0.244 mg/LSB) - 3 # LSM6DSV16X_DT_FS_16G (0.488 mg/LSB) ```  Legal values: `0`, `1`, `2`, `3` |
| `accel-odr` | `int` | ```text Specify the default accelerometer output data rate expressed in samples per second (Hz). The values are taken in accordance to lsm6dsv16x_data_rate_t enumerative in hal/st module. Please note that this values will not change the operating mode, which will remain High Performance (device default) Default is power-up configuration.  - 0x00 # LSM6DSV16X_DT_ODR_OFF - 0x01 # LSM6DSV16X_DT_ODR_AT_1Hz875 - 0x02 # LSM6DSV16X_DT_ODR_AT_7Hz5 - 0x03 # LSM6DSV16X_DT_ODR_AT_15Hz - 0x04 # LSM6DSV16X_DT_ODR_AT_30Hz - 0x05 # LSM6DSV16X_DT_ODR_AT_60Hz - 0x06 # LSM6DSV16X_DT_ODR_AT_120Hz - 0x07 # LSM6DSV16X_DT_ODR_AT_240Hz - 0x08 # LSM6DSV16X_DT_ODR_AT_480Hz - 0x09 # LSM6DSV16X_DT_ODR_AT_960Hz - 0x0a # LSM6DSV16X_DT_ODR_AT_1920Hz - 0x0b # LSM6DSV16X_DT_ODR_AT_3840Hz - 0x0c # LSM6DSV16X_DT_ODR_AT_7680Hz - 0x13 # LSM6DSV16X_DT_ODR_HA01_AT_15Hz625 - 0x14 # LSM6DSV16X_DT_ODR_HA01_AT_31Hz25 - 0x15 # LSM6DSV16X_DT_ODR_HA01_AT_62Hz5 - 0x16 # LSM6DSV16X_DT_ODR_HA01_AT_125Hz - 0x17 # LSM6DSV16X_DT_ODR_HA01_AT_250Hz - 0x18 # LSM6DSV16X_DT_ODR_HA01_AT_500Hz - 0x19 # LSM6DSV16X_DT_ODR_HA01_AT_1000Hz - 0x1a # LSM6DSV16X_DT_ODR_HA01_AT_2000Hz - 0x1b # LSM6DSV16X_DT_ODR_HA01_AT_4000Hz - 0x1c # LSM6DSV16X_DT_ODR_HA01_AT_8000Hz - 0x23 # LSM6DSV16X_DT_ODR_HA02_AT_12Hz5 - 0x24 # LSM6DSV16X_DT_ODR_HA02_AT_25Hz - 0x25 # LSM6DSV16X_DT_ODR_HA02_AT_50Hz - 0x26 # LSM6DSV16X_DT_ODR_HA02_AT_100Hz - 0x27 # LSM6DSV16X_DT_ODR_HA02_AT_200Hz - 0x28 # LSM6DSV16X_DT_ODR_HA02_AT_400Hz - 0x29 # LSM6DSV16X_DT_ODR_HA02_AT_800Hz - 0x2a # LSM6DSV16X_DT_ODR_HA02_AT_1600Hz - 0x2b # LSM6DSV16X_DT_ODR_HA02_AT_3200Hz - 0x2c # LSM6DSV16X_DT_ODR_HA02_AT_6400Hz ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `35`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44` |
| `gyro-range` | `int` | ```text Range in dps. Default is power-up configuration.  - 0x0 # LSM6DSV16X_DT_FS_125DPS  (4.375 mdps/LSB) - 0x1 # LSM6DSV16X_DT_FS_250DPS  (8.75 mdps/LSB) - 0x2 # LSM6DSV16X_DT_FS_500DPS  (17.50 mdps/LSB) - 0x3 # LSM6DSV16X_DT_FS_1000DPS (35 mdps/LSB) - 0x4 # LSM6DSV16X_DT_FS_2000DPS (70 mdps/LSB) - 0xc # LSM6DSV16X_DT_FS_4000DPS (140 mdps/LSB) ```  Legal values: `0`, `1`, `2`, `3`, `4`, `12` |
| `gyro-odr` | `int` | ```text Specify the default gyro output data rate expressed in samples per second (Hz). The values are taken in accordance to lsm6dsv16x_data_rate_t enumerative in hal/st module. Please note that these values will not change the operating mode, which will remain High Performance (device default). Moreover, the values here which will be selected in the DT are the only way to specify the odr accuracy even at runtime with SENSOR_ATTR_SAMPLING_FREQUENCY. Default is power-up configuration.  - 0x00 # LSM6DSV16X_DT_ODR_OFF - 0x01 # LSM6DSV16X_DT_ODR_AT_1Hz875 - 0x02 # LSM6DSV16X_DT_ODR_AT_7Hz5 - 0x03 # LSM6DSV16X_DT_ODR_AT_15Hz - 0x04 # LSM6DSV16X_DT_ODR_AT_30Hz - 0x05 # LSM6DSV16X_DT_ODR_AT_60Hz - 0x06 # LSM6DSV16X_DT_ODR_AT_120Hz - 0x07 # LSM6DSV16X_DT_ODR_AT_240Hz - 0x08 # LSM6DSV16X_DT_ODR_AT_480Hz - 0x09 # LSM6DSV16X_DT_ODR_AT_960Hz - 0x0a # LSM6DSV16X_DT_ODR_AT_1920Hz - 0x0b # LSM6DSV16X_DT_ODR_AT_3840Hz - 0x0c # LSM6DSV16X_DT_ODR_AT_7680Hz - 0x13 # LSM6DSV16X_DT_ODR_HA01_AT_15Hz625 - 0x14 # LSM6DSV16X_DT_ODR_HA01_AT_31Hz25 - 0x15 # LSM6DSV16X_DT_ODR_HA01_AT_62Hz5 - 0x16 # LSM6DSV16X_DT_ODR_HA01_AT_125Hz - 0x17 # LSM6DSV16X_DT_ODR_HA01_AT_250Hz - 0x18 # LSM6DSV16X_DT_ODR_HA01_AT_500Hz - 0x19 # LSM6DSV16X_DT_ODR_HA01_AT_1000Hz - 0x1a # LSM6DSV16X_DT_ODR_HA01_AT_2000Hz - 0x1b # LSM6DSV16X_DT_ODR_HA01_AT_4000Hz - 0x1c # LSM6DSV16X_DT_ODR_HA01_AT_8000Hz - 0x23 # LSM6DSV16X_DT_ODR_HA02_AT_12Hz5 - 0x24 # LSM6DSV16X_DT_ODR_HA02_AT_25Hz - 0x25 # LSM6DSV16X_DT_ODR_HA02_AT_50Hz - 0x26 # LSM6DSV16X_DT_ODR_HA02_AT_100Hz - 0x27 # LSM6DSV16X_DT_ODR_HA02_AT_200Hz - 0x28 # LSM6DSV16X_DT_ODR_HA02_AT_400Hz - 0x29 # LSM6DSV16X_DT_ODR_HA02_AT_800Hz - 0x2a # LSM6DSV16X_DT_ODR_HA02_AT_1600Hz - 0x2b # LSM6DSV16X_DT_ODR_HA02_AT_3200Hz - 0x2c # LSM6DSV16X_DT_ODR_HA02_AT_6400Hz ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `35`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44` |
| `drdy-pulsed` | `boolean` | ```text Selects the pulsed mode for data-ready interrupt when enabled, and the latched mode when disabled. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,lsm6dsv16x” compatible.

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
