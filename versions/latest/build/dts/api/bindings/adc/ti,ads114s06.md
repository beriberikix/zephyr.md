---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/adc/ti,ads114s06.html
original_path: build/dts/api/bindings/adc/ti,ads114s06.html
---

# ti,ads114s06 (on spi bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

Note

An implementation of a driver matching this compatible is available in
[drivers/adc/adc\_ads1x4s0x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/adc_ads1x4s0x.c).

## Description

These nodes are “ads1x4s0x” bus nodes.

```text
Texas Instrument 6 channels 16 bit SPI ADC
```

## Properties

### Top level properties

These property descriptions apply to “ti,ads114s06”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#io-channel-cells` | `int` | This property is **required**.  Constant value: `1` |
| `reset-gpios` | `phandle-array` | ```text GPIO for reset ``` |
| `drdy-gpios` | `phandle-array` | ```text GPIO for data ready, becomes active when a conversion result is ready ```  This property is **required**. |
| `start-sync-gpios` | `phandle-array` | ```text GPIO for start/sync, used to signal the ADC that a conversion should be started ``` |
| `idac-current` | `int` | ```text IDAC current in microampere, the default value turns the current source off ```  Legal values: `0`, `10`, `50`, `100`, `250`, `500`, `750`, `1000`, `1500`, `2000` |
| `vbias-level` | `int` | ```text bias voltage level: 0 - (AVDD+AVSS)/2, 1 - (AVDD+AVSS)/12 ```  Legal values: `0`, `1` |
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
may apply to the “ti,ads114s06” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ```  Constant value: `1` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Channel identifier. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `zephyr,gain` | `string` | ```text Gain selection: - ADC_GAIN_1_6: x 1/6 - ADC_GAIN_1_5: x 1/5 - ADC_GAIN_1_4: x 1/4 - ADC_GAIN_2_7: x 2/7 - ADC_GAIN_1_3: x 1/3 - ADC_GAIN_2_5: x 2/5 - ADC_GAIN_1_2: x 1/2 - ADC_GAIN_2_3: x 2/3 - ADC_GAIN_4_5: x 4/5 - ADC_GAIN_1:   x 1 - ADC_GAIN_2:   x 2 - ADC_GAIN_3:   x 3 - ADC_GAIN_4:   x 4 - ADC_GAIN_6:   x 6 - ADC_GAIN_8:   x 8 - ADC_GAIN_12:  x 12 - ADC_GAIN_16:  x 16 - ADC_GAIN_24:  x 24 - ADC_GAIN_32:  x 32 - ADC_GAIN_64:  x 64 - ADC_GAIN_128: x 128 ```  This property is **required**.  Legal values: `'ADC_GAIN_1_6'`, `'ADC_GAIN_1_5'`, `'ADC_GAIN_1_4'`, `'ADC_GAIN_2_7'`, `'ADC_GAIN_1_3'`, `'ADC_GAIN_2_5'`, `'ADC_GAIN_1_2'`, `'ADC_GAIN_2_3'`, `'ADC_GAIN_4_5'`, `'ADC_GAIN_1'`, `'ADC_GAIN_2'`, `'ADC_GAIN_3'`, `'ADC_GAIN_4'`, `'ADC_GAIN_6'`, `'ADC_GAIN_8'`, `'ADC_GAIN_12'`, `'ADC_GAIN_16'`, `'ADC_GAIN_24'`, `'ADC_GAIN_32'`, `'ADC_GAIN_64'`, `'ADC_GAIN_128'` |
| `zephyr,reference` | `string` | ```text Reference selection: - ADC_REF_VDD_1:     VDD - ADC_REF_VDD_1_2:   VDD/2 - ADC_REF_VDD_1_3:   VDD/3 - ADC_REF_VDD_1_4:   VDD/4 - ADC_REF_INTERNAL:  Internal - ADC_REF_EXTERNAL0: External, input 0 - ADC_REF_EXTERNAL1: External, input 1 ```  This property is **required**.  Legal values: `'ADC_REF_VDD_1'`, `'ADC_REF_VDD_1_2'`, `'ADC_REF_VDD_1_3'`, `'ADC_REF_VDD_1_4'`, `'ADC_REF_INTERNAL'`, `'ADC_REF_EXTERNAL0'`, `'ADC_REF_EXTERNAL1'` |
| `zephyr,vref-mv` | `int` | ```text This property can be used to specify the voltage (in millivolts) of the reference selected for this channel, so that applications can get that value if needed for some calculations. For the internal reference, the voltage can be usually obtained with a dedicated ADC API call, so there is no need to use this property in that case, but for other references this property can be useful. ``` |
| `zephyr,acquisition-time` | `int` | ```text Acquisition time. Use the ADC_ACQ_TIME macro to compose the value for this property or pass ADC_ACQ_TIME_DEFAULT to use the default setting for a given hardware (e.g. when the hardware does not allow to configure the acquisition time). ```  This property is **required**. |
| `zephyr,differential` | `boolean` | ```text When set, selects differential input mode for the channel. Otherwise, single-ended mode is used unless the zephyr,input-negative property is specified, in which case the differential mode is selected implicitly. ``` |
| `zephyr,input-positive` | `int` | ```text Positive ADC input. Used only for drivers that select the ADC_CONFIGURABLE_INPUTS Kconfig option. ``` |
| `zephyr,input-negative` | `int` | ```text Negative ADC input. Used only for drivers that select the ADC_CONFIGURABLE_INPUTS Kconfig option. When specified, implies the differential input mode for the channel. ``` |
| `zephyr,resolution` | `int` | ```text ADC resolution to be used for the channel. ``` |
| `zephyr,oversampling` | `int` | ```text Oversampling setting to be used for the channel. When specified, each sample is averaged from 2^N conversion results (where N is the provided value). ``` |
| `zephyr,current-source-pin` | `uint8-array` | ```text Output pin selection for the current sources. The actual interpretation depends on the driver. This is used only for drivers which select the ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN Kconfig option. ``` |
| `zephyr,vbias-pins` | `int` | ```text Output pin selection for the bias voltage. The actual interpretation depends on the driver. This is used only for drivers which select the ADC_CONFIGURABLE_VBIAS_PIN Kconfig option. ``` |

## Specifier cell names

- io-channel cells: input
