---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/st,lsm6dso16is-spi.html
original_path: build/dts/api/bindings/sensor/st,lsm6dso16is-spi.html
---

# st,lsm6dso16is (on spi bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/st/lsm6dso16is/lsm6dso16is.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/lsm6dso16is/lsm6dso16is.c).

## Description

```text
STMicroelectronics LSM6DSO16IS 6-axis IMU (Inertial Measurement Unit) sensor
accessed through SPI bus
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `irq-gpios` | `phandle-array` | ```text DRDY pin  This pin defaults to active high when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `drdy-pin` | `int` | ```text Select DRDY pin number (1 or 2).  This number represents which of the two interrupt pins (INT1 or INT2) the drdy line is attached to. This property is not mandatory and if not present it defaults to 1 which is the configuration at power-up. ```  Default value: `1`  Legal values: `1`, `2` |
| `accel-range` | `int` | ```text Range in g. Default is power-up configuration.  - 0 # LSM6DSO16IS_DT_FS_2G  (0.061 mg/LSB) - 1 # LSM6DSO16IS_DT_FS_16G (0.488 mg/LSB) - 2 # LSM6DSO16IS_DT_FS_4G  (0.122 mg/LSB) - 3 # LSM6DSO16IS_DT_FS_8G  (0.244 mg/LSB) ```  Legal values: `0`, `1`, `2`, `3` |
| `accel-odr` | `int` | ```text Specify the default accelerometer output data rate expressed in samples per second (Hz). The values are taken in accordance to lsm6dso16is_xl_data_rate_t enumerative in hal/st module. Default is power-up configuration.  - 0x00  # LSM6DSO16IS_DT_ODR_OFF - 0x01  # LSM6DSO16IS_DT_ODR_12Hz5_HP - 0x02  # LSM6DSO16IS_DT_ODR_26H_HP - 0x03  # LSM6DSO16IS_DT_ODR_52Hz_HP - 0x04  # LSM6DSO16IS_DT_ODR_104Hz_HP - 0x05  # LSM6DSO16IS_DT_ODR_208Hz_HP - 0x06  # LSM6DSO16IS_DT_ODR_416Hz_HP - 0x07  # LSM6DSO16IS_DT_ODR_833Hz_HP - 0x08  # LSM6DSO16IS_DT_ODR_1667Hz_HP - 0x09  # LSM6DSO16IS_DT_ODR_3333Hz_HP - 0x0a  # LSM6DSO16IS_DT_ODR_6667Hz_HP - 0x11  # LSM6DSO16IS_DT_ODR_12Hz5_LP - 0x12  # LSM6DSO16IS_DT_ODR_26H_LP - 0x13  # LSM6DSO16IS_DT_ODR_52Hz_LP - 0x14  # LSM6DSO16IS_DT_ODR_104Hz_LP - 0x15  # LSM6DSO16IS_DT_ODR_208Hz_LP - 0x16  # LSM6DSO16IS_DT_ODR_416Hz_LP - 0x17  # LSM6DSO16IS_DT_ODR_833Hz_LP - 0x18  # LSM6DSO16IS_DT_ODR_1667Hz_LP - 0x19  # LSM6DSO16IS_DT_ODR_3333Hz_LP - 0x1a  # LSM6DSO16IS_DT_ODR_6667Hz_LP - 0x1b  # LSM6DSO16IS_DT_ODR_1Hz6_LP ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27` |
| `gyro-range` | `int` | ```text Range in dps. Default is power-up configuration.  - 0x0  # LSM6DSO16IS_DT_FS_250DPS  (8.75 mdps/LSB) - 0x1  # LSM6DSO16IS_DT_FS_500DPS  (17.50 mdps/LSB) - 0x2  # LSM6DSO16IS_DT_FS_1000DPS (35 mdps/LSB) - 0x3  # LSM6DSO16IS_DT_FS_2000DPS (70 mdps/LSB) - 0x10 # LSM6DSO16IS_DT_FS_125DPS  (4.375 mdps/LSB) ```  Legal values: `0`, `1`, `2`, `3`, `16` |
| `gyro-odr` | `int` | ```text Specify the default gyro output data rate expressed in samples per second (Hz). The values are taken in accordance to lsm6dso16is_gy_data_rate_t enumerative in hal/st module. Default is power-up configuration.  - 0x00  # LSM6DSO16IS_DT_ODR_OFF - 0x01  # LSM6DSO16IS_DT_ODR_12Hz5_HP - 0x02  # LSM6DSO16IS_DT_ODR_26H_HP - 0x03  # LSM6DSO16IS_DT_ODR_52Hz_HP - 0x04  # LSM6DSO16IS_DT_ODR_104Hz_HP - 0x05  # LSM6DSO16IS_DT_ODR_208Hz_HP - 0x06  # LSM6DSO16IS_DT_ODR_416Hz_HP - 0x07  # LSM6DSO16IS_DT_ODR_833Hz_HP - 0x08  # LSM6DSO16IS_DT_ODR_1667Hz_HP - 0x09  # LSM6DSO16IS_DT_ODR_3333Hz_HP - 0x0a  # LSM6DSO16IS_DT_ODR_6667Hz_HP - 0x11  # LSM6DSO16IS_DT_ODR_12Hz5_LP - 0x12  # LSM6DSO16IS_DT_ODR_26H_LP - 0x13  # LSM6DSO16IS_DT_ODR_52Hz_LP - 0x14  # LSM6DSO16IS_DT_ODR_104Hz_LP - 0x15  # LSM6DSO16IS_DT_ODR_208Hz_LP - 0x16  # LSM6DSO16IS_DT_ODR_416Hz_LP - 0x17  # LSM6DSO16IS_DT_ODR_833Hz_LP - 0x18  # LSM6DSO16IS_DT_ODR_1667Hz_LP - 0x19  # LSM6DSO16IS_DT_ODR_3333Hz_LP - 0x1a  # LSM6DSO16IS_DT_ODR_6667Hz_LP ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26` |
| `drdy-pulsed` | `boolean` | ```text Selects the pulsed mode for data-ready interrupt when enabled, and the latched mode when disabled. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,lsm6dso16is” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
