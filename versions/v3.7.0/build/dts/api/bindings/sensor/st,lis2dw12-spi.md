---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/sensor/st,lis2dw12-spi.html
original_path: build/dts/api/bindings/sensor/st,lis2dw12-spi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,lis2dw12 (on spi bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STMicroelectronics LIS2DW12 3-axis accelerometer accessed through SPI bus
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
| `irq-gpios` | `phandle-array` | ```text DRDY pin  This pin defaults to active high when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `int-pin` | `int` | ```text Select DRDY pin number (1 or 2).     1 # drdy is generated from INT1    2 # drdy is generated from INT2  This number represents which of the two interrupt pins (INT1 or INT2) the drdy line is attached to. This property is not mandatory and if not present it defaults to 1 which is the configuration at power-up. ```  Default value: `1`  Legal values: `1`, `2` |
| `range` | `int` | ```text Range in g. Default is power-up configuration.    16 # 16g (1.952 mg/LSB)    8 #  8g (0.976 mg/LSB)    4 #  4g (0.488 mg/LSB)    2 #  2g (0.244 mg/LSB) ```  Default value: `2`  Legal values: `16`, `8`, `4`, `2` |
| `odr` | `int` | ```text Output data rate in Hz. Default value is 12.5Hz if this is not set. The output data rates which are represented with fractional numbers are converted into their integer parts (1.65Hz -> 1, 12.5Hz -> 12). If 0 selected as the odr, the accelerometer initializes into power off state. ```  Legal values: `0`, `1`, `12`, `25`, `50`, `100`, `200`, `400`, `800`, `1600` |
| `bw-filt` | `int` | ```text Digital filtering cutoff bandwidth. Default is power-up configuration.  - 0 # LIS2DW12_DT_FILTER_BW_ODR_DIV_2 - 1 # LIS2DW12_DT_FILTER_BW_ODR_DIV_4 - 2 # LIS2DW12_DT_FILTER_BW_ODR_DIV_10 - 3 # LIS2DW12_DT_FILTER_BW_ODR_DIV_20 ```  Legal values: `0`, `1`, `2`, `3` |
| `power-mode` | `int` | ```text Specify the sensor power mode. Default is power-up configuration.  - 0 # LIS2DW12_DT_LP_M1 - 1 # LIS2DW12_DT_LP_M2 - 2 # LIS2DW12_DT_LP_M3 - 3 # LIS2DW12_DT_LP_M4 - 4 # LIS2DW12_DT_HP_MODE ```  Legal values: `0`, `1`, `2`, `3`, `4` |
| `tap-mode` | `int` | ```text Tap mode. Default is power-up configuration.  - 0 # LIS2DW12_DT_SINGLE_TAP - 1 # LIS2DW12_DT_SINGLE_DOUBLE_TAP ```  Legal values: `0`, `1` |
| `tap-threshold` | `array` | ```text Tap X/Y/Z axes threshold. Default is power-up configuration. (X/Y/Z values range from 0x00 to 0x1F)  Thresholds to start the tap-event detection procedure on the X/Y/Z axes. Threshold values for each axis are unsigned 5-bit corresponding to a 2g acceleration full-scale range. A threshold value equal to zero corresponds to disable the tap detection on that axis.  For example, if you want to set the threshold for X to 12, for Z to 14 and want to disable tap detection on Y, you should specify in Device Tree      tap-threshold = <12>, <0>, <14>  which is equivalent to X = 12 * 2g/32 = 750mg and Z = 14 * 2g/32 = 875mg. ```  Default value: `[0, 0, 0]` |
| `tap-shock` | `int` | ```text Tap shock value. Default is power-up configuration. (values range from 0x0 to 0x3) This register represents the maximum time of an over-threshold signal detection to be recognized as a tap event. Where 0 equals 4*1/ODR and 1LSB = 8*1/ODR. ``` |
| `tap-latency` | `int` | ```text Tap latency. Default is power-up configuration. (values range from 0x0 to 0xF) When double-tap recognition is enabled, this register expresses the maximum time between two successive detected taps to determine a double-tap event. Where 0 equals 16*1/ODR and 1LSB = 32*1/ODR. ``` |
| `tap-quiet` | `int` | ```text Expected quiet time after a tap detection. Default is power-up configuration. (values range from 0x0 to 0x3) This register represents the time after the first detected tap in which there must not be any overthreshold event. Where 0 equals 2*1/ODR and 1LSB = 4*1/ODR. ``` |
| `low-noise` | `boolean` | ```text Enables the LOW_NOISE flag in the CTRL6 register. This influences the noise density and the current consumption. See the datasheet for more information. ``` |
| `hp-filter-path` | `boolean` | ```text Sets the Filtered Data Selection bit in the CTRL6 register. When enabled, the high-pass filter path is selected. When disabled, the low-pass filter path is selected. Note that this influences the OUT_REG / FIFO values, but not the Wakeup function. ``` |
| `hp-ref-mode` | `boolean` | ```text Enables the high-pass filter reference mode in the CTRL7 register. When the high-pass filter is configured in reference mode, the output data is calculated as the difference between the input acceleration and the values captured when reference mode was enabled. In this way only the difference is applied without any filtering of the LIS2DW12. Note that this influences both the OUT_REG / FIFO values, as well as the Wakeup function. ``` |
| `drdy-pulsed` | `boolean` | ```text Selects the pulsed mode for data-ready interrupt when enabled, and the latched mode when disabled. Sets the corresponding DRDY_PULSED bit in the CTRL7 register. ``` |
| `ff-duration` | `int` | ```text The freefall duration value represented in milliseconds. If the accelerometer readings of the all axes are lower than the freefall threshold value for the freefall duration long, then a freefall trigger occurs. This value is 5 bits long in the register and 1 LSB = 1 * 1/ODR. This value depends on the ODR. if the data rate change in code with SENSOR ATTR SAMPLING FREQUENCY, It must be set again with SENSOR_ATT_FF_DUR attribute. ST propose 100Hz ODR and 30ms ff-duration for recognize freefall detection refer to ST DT0100 design tip document. ```  Default value: `30` |
| `ff-threshold` | `int` | ```text The freefall threshold value represented in mg. If the accelerometer readings of the all axes are lower than the freefall threshold value for the freefall duration long, then a freefall trigger occurs. This value is 3 bits long. Default value chosen 3 (312 mg) refer to ST DT0100 design tip document.  - 0 # LIS2DW12_DT_FF_THRESHOLD_156_mg - 1 # LIS2DW12_DT_FF_THRESHOLD_219_mg - 2 # LIS2DW12_DT_FF_THRESHOLD_250_mg - 3 # LIS2DW12_DT_FF_THRESHOLD_312_mg - 4 # LIS2DW12_DT_FF_THRESHOLD_344_mg - 5 # LIS2DW12_DT_FF_THRESHOLD_406_mg - 6 # LIS2DW12_DT_FF_THRESHOLD_469_mg - 7 # LIS2DW12_DT_FF_THRESHOLD_500_mg ```  Default value: `3`  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7` |
| `wakeup-duration` | `int` | ```text The wakeup duration. Default value is the register reset value. If the accelerometer readings of the all axes are higher than the wakeup threshold value for the wakeup duration long, then a wakeup trigger occurs. This value is 2 bits long in the register and 1 LSB = 1 * 1/ODR.  - 0 # LIS2DW12_DT_WAKEUP_1_ODR - 1 # LIS2DW12_DT_WAKEUP_2_ODR - 2 # LIS2DW12_DT_WAKEUP_3_ODR - 3 # LIS2DW12_DT_WAKEUP_4_ODR ```  Legal values: `0`, `1`, `2`, `3` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,lis2dw12” compatible.

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
