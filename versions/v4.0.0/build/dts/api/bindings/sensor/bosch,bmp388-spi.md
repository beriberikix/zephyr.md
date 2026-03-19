---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/bosch,bmp388-spi.html
original_path: build/dts/api/bindings/sensor/bosch,bmp388-spi.html
---

# bosch,bmp388 (on spi bus)

Vendor: [Bosch Sensortec GmbH](../../bindings.md#dt-vendor-bosch)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/bosch/bmp388/bmp388.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp388/bmp388.c).

## Description

```text
Bosch BMP388 pressure sensor accessed through SPI bus
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
| `int-gpios` | `phandle-array` |  |
| `odr` | `string` | ```text Default output data rate in Hz. Only the following values are allowed:   200   - 200     - 5ms  (default; chip reset value)   100   - 100     - 10ms   50    - 50      - 20ms   25    - 25      - 40ms   12.5  - 25/2    - 80ms   6.25  - 25/4    - 160ms   3.125 - 25/8    - 320ms   1.563 - 25/16   - 640ms   .781  - 25/32   - 1.28s   .391  - 25/64   - 2.56s   .195  - 25/128  - 5.12s   .098  - 25/256  - 10.24s   .049  - 25/512  - 20.48s   .024  - 25/1024 - 40.96s   .012  - 25/2048 - 81.92s   .006  - 25/4096 - 163.84s   .003  - 25/8192 - 327.68s ```  Default value: `200`  Legal values: `'200'`, `'100'`, `'50'`, `'25'`, `'12.5'`, `'6.25'`, `'3.125'`, `'1.563'`, `'.781'`, `'.391'`, `'.195'`, `'.098'`, `'.049'`, `'.024'`, `'.012'`, `'.006'`, `'.003'` |
| `osr-press` | `int` | ```text Default pressure oversampling rate. Only the following values are allowed:   1 sample, 16-bit, 2.64 Pa   2 samples, 17-bit, 1.32 Pa   4 samples, 18-bit, 0.66 Pa (default; chip reset value)   8 samples, 19-bit, 0.33 Pa   16 samples, 20-bit, 0.17 Pa   32 Samples, 21-bit, 0.085 Pa ```  Default value: `4`  Legal values: `1`, `2`, `4`, `8`, `16`, `32` |
| `osr-temp` | `int` | ```text Default temperature oversampling rate. Only the following values are allowed:   1 sample, 16-bit, .0050 C (default; chip reset value)   2 samples, 17-bit, .0025 C   4 samples, 18-bit, .0012 C   8 samples, 19-bit, .0006 C   16 samples, 20-bit, .0003 C   32 Samples, 21-bit, .00015 C ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8`, `16`, `32` |
| `iir-filter` | `int` | ```text Default IIR filter coefficient. The default 0 is the chip reset value. ```  Legal values: `0`, `1`, `3`, `7`, `15`, `31`, `63`, `127` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “bosch,bmp388” compatible.

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
