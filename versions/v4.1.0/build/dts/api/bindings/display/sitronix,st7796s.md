---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/display/sitronix,st7796s.html
original_path: build/dts/api/bindings/display/sitronix,st7796s.html
---

# sitronix,st7796s (on mipi-dbi bus)

Vendor: [Sitronix Technology Corporation](../../bindings.md#dt-vendor-sitronix)

Note

An implementation of a driver matching this compatible is available in
[drivers/display/display\_st7796s.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_st7796s.c).

## Description

```text
ST7796S Display controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `frmctl1` | `uint8-array` | ```text Frame rate control (partial mode / full colors). The default value should result in a framerate of ~41 FPS. ```  Default value: `[160, 16]` |
| `frmctl2` | `uint8-array` | ```text Frame rate control (idle mode / 8 colors). This property sets the division ratio for internal clocks in idle mode ```  Default value: `[0, 16]` |
| `frmctl3` | `uint8-array` | ```text Frame rate control (partial mode / full colors). This property sets the division ratio for internal clocks in partial mode ```  Default value: `[0, 16]` |
| `bpc` | `uint8-array` | ```text Blanking porch control. This sets the vertical and horizontal front/back porch values ```  Default value: `[2, 2, 0, 4]` |
| `dfc` | `uint8-array` | ```text Display function control. Sets display graphical ram mode, as well as gate scan mode ```  Default value: `[128, 2, 59]` |
| `pwr1` | `uint8-array` | ```text Power control parameter 1. Sets AVDDS, AVLCS, and VGHS ```  Default value: `[128, 37]` |
| `pwr2` | `int` | ```text Power control parameter 2. Sets VAP ```  Default value: `19` |
| `pwr3` | `int` | ```text Power control parameter 3. Sets source and gamma current levels ```  Default value: `10` |
| `vcmpctl` | `int` | ```text VCOM control setting. Value starts at 0.300V, and moves upwards in increments of 0.025V. Maximum of 1.875V ```  Default value: `28` |
| `doca` | `uint8-array` | ```text Display output control adjust. Sets display timing controls ```  Default value: `[64, 138, 0, 0, 37, 10, 56, 51]` |
| `pgc` | `uint8-array` | ```text Positive gamma control settings. No default is provided by controller, as this setting is panel specific. ```  This property is **required**. |
| `ngc` | `uint8-array` | ```text Negative gamma control settings. No default is provided by controller, as this setting is panel specific. ```  This property is **required**. |
| `madctl` | `int` | ```text Memory data access control value. This controls the panel color format, as well as rotation settings. ``` |
| `color-invert` | `boolean` | ```text When present, inverts display colors ``` |
| `invert-mode` | `string` | ```text Display inversion control mode. ```  Default value: `1-dot`  Legal values: `'column'`, `'1-dot'`, `'2-dot'` |
| `rgb-is-inverted` | `boolean` | ```text Inverting color format order (RGB->BGR or BGR->RGB) In the case of enabling this option, API reports pixel-format in capabilities as the inverted value of the RGB pixel-format specified in MADCTL. This option is convenient for supporting displays with bugs where the actual color is different from the pixel format of MADCTL. ``` |
| `duplex` | `int` | ```text SPI Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Selecting half duplex allows to use SPI MOSI as a bidirectional line, typically used when only one data line is connected. Use the macros, not the actual enum value. Here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ``` |
| `mipi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `mipi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `mipi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `mipi-max-frequency` | `int` | ```text Maximum clock frequency of device's MIPI interface in Hz ``` |
| `mipi-mode` | `string` | ```text MIPI DBI mode in use. These definitions should match those in dt-bindings/mipi_dbi/mipi_dbi.h ```  Legal values: `'MIPI_DBI_MODE_SPI_3WIRE'`, `'MIPI_DBI_MODE_SPI_4WIRE'`, `'MIPI_DBI_MODE_6800_BUS_16_BIT'`, `'MIPI_DBI_MODE_6800_BUS_9_BIT'`, `'MIPI_DBI_MODE_6800_BUS_8_BIT'`, `'MIPI_DBI_MODE_8080_BUS_16_BIT'`, `'MIPI_DBI_MODE_8080_BUS_9_BIT'`, `'MIPI_DBI_MODE_8080_BUS_8_BIT'` |
| `te-mode` | `string` | ```text MIPI DBI tearing enable signal mode. Defaults to disabled. ```  Default value: `MIPI_DBI_TE_NO_EDGE`  Legal values: `'MIPI_DBI_TE_NO_EDGE'`, `'MIPI_DBI_TE_RISING_EDGE'`, `'MIPI_DBI_TE_FALLING_EDGE'` |
| `te-delay` | `int` | ```text Delay in microseconds to wait before transmitting display data after a tearing enable synchronization signal is seen. Defaults to 0 since most controllers will not need a delay. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `height` | `int` | ```text Height of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |
| `width` | `int` | ```text Width of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “sitronix,st7796s” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
