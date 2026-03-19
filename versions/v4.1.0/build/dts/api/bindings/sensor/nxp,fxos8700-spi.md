---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/sensor/nxp,fxos8700-spi.html
original_path: build/dts/api/bindings/sensor/nxp,fxos8700-spi.html
---

# nxp,fxos8700 (on spi bus)

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/nxp/fxos8700/fxos8700.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/fxos8700.c).

## Description

```text
FXOS8700 6-axis accelerometer/magnetometer sensor
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
| `reset-gpios` | `phandle-array` | ```text RST pin This pin defaults to active high when consumed by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `int1-gpios` | `phandle-array` | ```text INT1 pin This pin defaults to active low when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `int2-gpios` | `phandle-array` | ```text INT2 pin This pin defaults to active low when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `range` | `int` | ```text Range in g ```  Default value: `8`  Legal values: `8`, `4`, `2` |
| `power-mode` | `int` | ```text Power mode ```  Legal values: `0`, `1`, `2`, `3` |
| `pulse-cfg` | `int` | ```text Pulse configuration register ```  Default value: `63` |
| `pulse-thsx` | `int` | ```text Pulse X-axis threshold Threshold to start the pulse-event detection procedure on the X-axis. Threshold values for each axis are unsigned 7-bit numbers with a fixed resolution of 0.063 g/LSB, corresponding to an 8g acceleration full-scale range. ```  Default value: `32` |
| `pulse-thsy` | `int` | ```text Pulse Y-axis threshold Threshold to start the pulse-event detection procedure on the Y-axis. Threshold values for each axis are unsigned 7-bit numbers with a fixed resolution of 0.063 g/LSB, corresponding to an 8g acceleration full-scale range. ```  Default value: `32` |
| `pulse-thsz` | `int` | ```text Pulse Z-axis threshold Threshold to start the pulse-event detection procedure on the Z-axis. Threshold values for each axis are unsigned 7-bit numbers with a fixed resolution of 0.063 g/LSB, corresponding to an 8g acceleration full-scale range. ```  Default value: `64` |
| `pulse-tmlt` | `int` | ```text Pulse time limit The maximum time interval that can elapse between the start of the acceleration on the selected channel exceeding the specified threshold and the end when the channel acceleration goes back below the specified threshold. The resolution depends upon the sample rate (ODR) and the high-pass filter configuration (HP_FILTER_CUTOFF[pls_hpf_en]). For ODR=800 Hz and pls_hpf_en=0, the resolution is 0.625 ms/LSB. ```  Default value: `24` |
| `pulse-ltcy` | `int` | ```text Pulse latency The time interval that starts after the first pulse detection where the pulse-detection function ignores the start of a new pulse. The resolution depends upon the sample rate (ODR) and the high-pass filter configuration (HP_FILTER_CUTOFF[pls_hpf_en]). For ODR=800 Hz and pls_hpf_en=0, the resolution is 1.25 ms/LSB. ```  Default value: `40` |
| `pulse-wind` | `int` | ```text Pulse window The maximum interval of time that can elapse after the end of the latency interval in which the start of the second pulse event must be detected provided the device has been configured for double pulse detection. The detected second pulse width must be shorter than the time limit constraint specified by the PULSE_TMLT register, but the end of the double pulse need not finish within the time specified by the PULSE_WIND register. The resolution depends upon the sample rate (ODR) and the high-pass filter configuration (HP_FILTER_CUTOFF[pls_hpf_en]). For ODR=800 Hz and pls_hpf_en=0, the resolution is 1.25 ms/LSB. ```  Default value: `60` |
| `mag-vecm-cfg` | `int` | ```text Magnetic vector-magnitude configuration register ```  Default value: `78` |
| `mag-vecm-ths-msb` | `int` | ```text Magnetic vector-magnitude threshold most significant byte. Resolution is 0.1 uT/LSB. ``` |
| `mag-vecm-ths-lsb` | `int` | ```text Magnetic vector-magnitude threshold least significant byte. Resolution is 0.1 uT/LSB. ```  Default value: `90` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,fxos8700” compatible.

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
