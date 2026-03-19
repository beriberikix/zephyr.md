---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/sensor/st,lsm6dso16is-spi.html
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
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
