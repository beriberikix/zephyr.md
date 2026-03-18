---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/sensor/ti,tmag5170.html
original_path: build/dts/api/bindings/sensor/ti,tmag5170.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ti,tmag5170 (on spi bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

## Description

```text
Texas Instruments TMAG5170 high-precision, linear 3D Hall-effect sensor.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `int-gpios` | `phandle-array` | ```text This property specifies the connection to ALERT sensor pin. It will be used by the driver to notify the application about data ready event. For this property to take effect, the TMAG5170_TRIGGER must be set in project configuration ``` |
| `operating-mode` | `int` | ```text Operating mode of the device. 1 - stand-by mode - in this mode the device waits for application to trigger the measurement. 2 - active measure mode - continuous sampling on all enabled channels as fast as possible. Recommended for devices that haven't got strict power requirements and need frequent sampling. 3 - active trigger mode - in this mode, similar to stand-by mode, the device wait for application to trigger the measurement, but the time needed to finish the conversion is shorter than in stand-by mode, on the cost of increased power consumption. 4 - duty-cycled - after each sample the device goes to sleep and then automatically wakes up to take another sample. The sleep time is determined by `sleep-time` property. Recommended for low-power devices that don't need high frequency sampling. ```  This property is **required**.  Legal values: `1`, `2`, `3`, `4` |
| `magnetic-channels` | `string` | ```text Enables data acquisition of the magnetic axis channel(s) If axis is enabled more than once, sensor will do pseudo-simultaneous sampling. Refer to datasheet for more information, By default all axes are enabled (XYZ) to allow the user to check if the sensor work as expected. Following options are allowed: None (chip reset value) X Y XY Z ZX YZ XYZ (default) XYX YXY YZY ZYZ ZXZ XZX XYZYX XYZZYX ```  Default value: `XYZ`  Legal values: `'None'`, `'X'`, `'Y'`, `'XY'`, `'Z'`, `'ZX'`, `'YZ'`, `'XYZ'`, `'XYX'`, `'YXY'`, `'YZY'`, `'ZYZ'`, `'ZXZ'`, `'XZX'`, `'XYZYX'`, `'XYZZYX'` |
| `x-range` | `int` | ```text The maximum and minimum values that can be measured on X axis. The wider the range, the worse the resolution. 0 = ±50mT (TMAG5170A1)/ ±150mT(TMAG5170A2) - (default; chip reset value) 1 = ±25mT (TMAG5170A1)/ ±75mT(TMAG5170A2) 2 = ±100mT (TMAG5170A1)/ ±300mT(TMAG5170A2) ```  Legal values: `0`, `1`, `2` |
| `y-range` | `int` | ```text The maximum and minimum values that can be measured on Y axis. The wider the range, the worse the resolution. 0 = ±50mT (TMAG5170A1)/ ±150mT(TMAG5170A2) - (default; chip reset value) 1 = ±25mT (TMAG5170A1)/ ±75mT(TMAG5170A2) 2 = ±100mT (TMAG5170A1)/ ±300mT(TMAG5170A2) ```  Legal values: `0`, `1`, `2` |
| `z-range` | `int` | ```text The maximum and minimum values that can be measured on Z axis. The wider the range, the worse the resolution. 0 = ±50mT (TMAG5170A1)/ ±150mT(TMAG5170A2) - (default; chip reset value) 1 = ±25mT (TMAG5170A1)/ ±75mT(TMAG5170A2) 2 = ±100mT (TMAG5170A1)/ ±300mT(TMAG5170A2) ```  Legal values: `0`, `1`, `2` |
| `oversampling` | `int` | ```text Enables additional sampling of the sensor data to reduce the noise effect. If temperature channel is enabled, temperature will be oversampled too, unless `disable-temperature-oversampling` property is present. Following options are allowed: 1 (default; chip reset value) 2 4 8 16 32 ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8`, `16`, `32` |
| `enable-temperature-channel` | `boolean` | ```text Enables temperature measurement ``` |
| `magnet-type` | `string` | ```text Enables temperature compensation basing on the type of magnet. Following options are allowed: None (default; chip reset value) NdBFe = 0.12%/deg C SmCo = 0.03%/deg C Ceramic = 0.2%/deg C ```  Default value: `None`  Legal values: `'None'`, `'NdBFe'`, `'SmCo'`, `'Ceramic'` |
| `angle-measurement` | `string` | ```text Enable angle calculation using two axis data: None (default; chip reset value) XY YZ XZ ```  Default value: `None`  Legal values: `'None'`, `'XY'`, `'YZ'`, `'XZ'` |
| `disable-temperature-oversampling` | `boolean` | ```text If true, temperature is always sampled once per conversion set If false, temperature is oversampled according to `oversampling` property. ``` |
| `sleep-time` | `int` | ```text The time in milliseconds the sensor will be in sleep during conversions. For this property to take effect sensor must be in `duty-cycled` mode. Note that to calculate total time between conversions, the conversion time itself must be taken into account. The conversion time is dependent on the values of `oversampling`, `magnetic-channels`, `temperature-channel-enabled` and `disable-temperature-oversampling` properties. Following value are allowed: 1 (default; chip reset value) 5 10 15 20 30 50 100 500 1000 ```  Default value: `1`  Legal values: `1`, `5`, `10`, `15`, `20`, `30`, `50`, `100`, `500`, `1000` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,tmag5170” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
