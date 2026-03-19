---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/gpio/adi,max14916-gpio.html
original_path: build/dts/api/bindings/gpio/adi,max14916-gpio.html
---

# adi,max14916-gpio (on spi bus)

Vendor: [Analog Devices, Inc.](../../bindings.md#dt-vendor-adi)

Note

An implementation of a driver matching this compatible is available in
[drivers/gpio/gpio\_max14916.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/gpio_max14916.c).

## Description

```text
ADI  MAX14916 is octal industrial output with advanced diagnostics
```

## Properties

### Top level properties

These property descriptions apply to “adi,max14916-gpio”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#gpio-cells` | `int` | ```text Number of items to expect in a GPIO specifier ```  This property is **required**.  Constant value: `2` |
| `ngpios` | `int` | ```text Number of gpios supported ```  This property is **required**.  Default value: `32`  Constant value: `8` |
| `drdy-gpios` | `phandle-array` | ```text High-Side Open-Drain Output. READY is passive low when the internal logic supply is higher than the UVLO threshold, indicating that the registers have adequate supply voltage. ``` |
| `fault-gpios` | `phandle-array` | ```text Fault pin indicates when there is Fault state in either FAULT1 or FAULT2 bothe of which are cleaned on read once problem is not persistent ``` |
| `sync-gpios` | `phandle-array` | ```text Latch the data so it could be read (partially duplicate CS) ``` |
| `en-gpios` | `phandle-array` | ```text DOI Enable Pin. Drive the EN pin high to enable the DOI_ outputs. Drive EN low to disable/three-state all DOI_ outputs. ``` |
| `crc-en` | `boolean` | ```text Notify driver if crc pin is enabled. ``` |
| `spi-addr` | `int` | ```text On MAX14906PMB module default address is 0 (A0-LOW, A1-LOW) Selectable device address, configurable from A0 and A1 ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `ow-on-en` | `array` | ```text Default values are from documentation. Enable or disable open-wire-on functionality per channel. - 0 mean disable - 1 mean enable channels indentation start from CH0...CH7 ```  Default value: `[0, 0, 0, 0, 0, 0, 0, 0]` |
| `ow-off-en` | `array` | ```text Default values are from documentation. Enable or disable open-wire-off functionality per channel. - 0 mean disable - 1 mean enable channels indentation start from CH0...CH7 ```  Default value: `[0, 0, 0, 0, 0, 0, 0, 0]` |
| `sh-vdd-en` | `array` | ```text Default values are from documentation. ShVddEN - Short to VDD enable Enable or disable short to VDD functionality per channel. - 0 mean disable - 1 mean enable channels indentation start from CH0...CH3 ```  Default value: `[0, 0, 0, 0, 0, 0, 0, 0]` |
| `fled-set` | `boolean` | ```text Internal fault diagnostics include (if enabled): SafeDemagF_, SHVDD_, VDDOV_, OWOff_, AboveVDD_, CL_, OVL_, VDDOKFault_. ``` |
| `sled-set` | `boolean` | ```text Enable status LEDs ``` |
| `fled-stretch` | `int` | ```text Default values are from documentation. Set minimum on time for FLEDs in case of fault 0 - Disable minimum fault LED (FLED) on-time 1 - Minimum fault LED (FLED) on-time = 1s (typ) 2 - Minimum fault LED (FLED) on-time = 2s (typ) 3 - Minimum fault LED (FLED) on-time = 3s (typ) ```  Legal values: `0`, `1`, `2`, `3` |
| `ffilter-en` | `boolean` | ```text When the fault LEDs (FLEDs) are controlled internally (FLEDSet = 0), open- wire and short-to-V DD diagnostics always use filtering and cannot be disabled by the FFilterEn bit. ``` |
| `filter-long` | `boolean` | ```text false: To select regular blanking time (4ms, typ) for diagnostic fault bits, OWOff_        and SHVDD_ true:  To select long blanking time (8ms, typ) for diagnostic fault bits, OWOff_        and SHVDD_ ``` |
| `flatch-en` | `boolean` | ```text false: Disable latching of diagnostic fault bits in the OvrLdChF, OpnWirChF, and        ShtVDDChF registers true:  Enable latching of diagnostic fault bits in the OvrLdChF, OpnWirChF, and        ShtVDDChF registers ``` |
| `led-cur-lim` | `boolean` | ```text false: Disable fault LEDs (FLEDs) signaling current limit true:  Enable fault LEDs (FLEDs) signaling current limit ``` |
| `vdd-on-thr` | `boolean` | ```text Enable higher voltage thresholds for VDD and VDD_ undervoltage monitoring ``` |
| `synch-wd-en` | `boolean` | ```text The SYNCH watchdog timeout is defined by the WDTo[1:0] bits if the SPI watchdog is enabled. When WDTo[1:0] = 00 (SPI watchdog disabled), the SYNCH watchdog timeout is 600ms (typ) if enabled. ``` |
| `sht-vdd-thr` | `int` | ```text Default values are from documentation. Set threshold voltage for short-to-V DD detection 0: Set threshold voltage for short-to-VDD detection to 9V (typ) 1: Set threshold voltage for short-to-VDD detection to 10V (typ) 2: Set threshold voltage for short-to-VDD detection to 12V (typ) 3: Set threshold voltage for short-to-VDD detection to 14V (typ) ```  Legal values: `0`, `1`, `2`, `3` |
| `ow-off-cs` | `int` | ```text Default values are from documentation. Set the pullup current for open-wire and short-to-VDD detection 0: Set open-wire and short-to-VDD detection current to 60μA (typ) 1: Set open-wire and short-to-VDD detection current to 100μA (typ) 2: Set open-wire and short-to-VDD detection current to 300μA (typ) 3: Set open-wire and short-to-VDD detection current to 600μA (typ) ```  Legal values: `0`, `1`, `2`, `3` |
| `wd-to` | `int` | ```text Default values are from documentation. SPI Watchdog Status, set SPI and SYNCH Watchdog Timeout 0: Disable SPI Watchdog Status and SPI Watchdog Timeout 1: Enable SPI Watchdog Status, set SPI and SYNCH Watchdog Timeout to 200ms (typ) 2: Enable SPI Watchdog Status, set SPI and SYNCH Watchdog Timeout to 600ms (typ) 3: Enable SPI Watchdog Status, set SPI and SYNCH Watchdog Timeout to 1.2s (typ) ```  Legal values: `0`, `1`, `2`, `3` |
| `gpio-controller` | `boolean` | ```text Convey's this node is a GPIO controller ```  This property is **required**. |
| `gpio-reserved-ranges` | `array` | ```text If not all the GPIOs at offsets 0...N-1 are usable for ngpios = <N>, then this property contains an additional set of tuples which specify which GPIOs are unusable. This property indicates the start and size of the GPIOs that can't be used.  For example, setting "gpio-reserved-ranges = <3 2>, <10 1>;" means that GPIO offsets 3, 4, and 10 are not usable, even if ngpios = <18>. ``` |
| `gpio-line-names` | `string-array` | ```text This is an array of strings defining the names of the GPIO lines going out of the GPIO controller ``` |
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
may apply to the “adi,max14916-gpio” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `gpio-hog` | `boolean` | ```text Conveys this node is a GPIO hog. ```  This property is **required**. |
| `gpios` | `array` | ```text This is an array of GPIO specifiers (e.g. pin, flags) to be hogged. The number of array entries must be an integer multiple of the number of GPIO specifier cells for the parent GPIO controller. ```  This property is **required**. |
| `input` | `boolean` | ```text If this property is set, the GPIO is configured as an input. This property takes precedence over the output-low and output-high properties. ``` |
| `output-low` | `boolean` | ```text If this property is set, the GPIO is configured as an output set to logical low. This property takes precedence over the output-high property. ``` |
| `output-high` | `boolean` | ```text If this property is set, the GPIO is configured as an output set to logical high. ``` |
| `line-name` | `string` | ```text Optional GPIO line name. ``` |

## Specifier cell names

- gpio cells: pin, flags
