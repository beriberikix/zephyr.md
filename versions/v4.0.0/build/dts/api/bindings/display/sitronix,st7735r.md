---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/display/sitronix,st7735r.html
original_path: build/dts/api/bindings/display/sitronix,st7735r.html
---

# sitronix,st7735r (on mipi-dbi bus)

Vendor: [Sitronix Technology Corporation](../../bindings.md#dt-vendor-sitronix)

Note

An implementation of a driver matching this compatible is available in
[drivers/display/display\_st7735r.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_st7735r.c).

## Description

```text
ST7735R/ST7735S 160x128 (max) display controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `x-offset` | `int` | ```text The column offset in pixels of the LCD to the controller memory ```  This property is **required**. |
| `y-offset` | `int` | ```text The row offset in pixels of the LCD to the controller memory ```  This property is **required**. |
| `madctl` | `int` | ```text Memory Data Access Control ``` |
| `colmod` | `int` | ```text Interface Pixel Format ```  Default value: `6` |
| `pwctr1` | `uint8-array` | ```text Power Control 1 Parameter ```  Default value: `[180, 20, 4]` |
| `pwctr2` | `uint8-array` | ```text Power Control 2 Parameter ```  Default value: `[192]` |
| `pwctr3` | `uint8-array` | ```text Power Control 3 Parameter ```  Default value: `[10, 0]` |
| `pwctr4` | `uint8-array` | ```text Power Control 4 Parameter ```  Default value: `[138, 38]` |
| `pwctr5` | `uint8-array` | ```text Power Control 5 Parameter ```  Default value: `[138, 238]` |
| `gamctrp1` | `uint8-array` | ```text Positive Voltage Gamma Control Parameter ```  This property is **required**. |
| `gamctrn1` | `uint8-array` | ```text Negative Voltage Gamma Control Parameter ```  This property is **required**. |
| `frmctr1` | `uint8-array` | ```text Frame rate control (normal mode / full colors) ```  Default value: `[5, 58, 58]` |
| `frmctr2` | `uint8-array` | ```text Frame rate control (idle mode / 8 colors) ```  Default value: `[5, 58, 58]` |
| `frmctr3` | `uint8-array` | ```text Frame rate control (partial mode / full colors) ```  Default value: `[5, 58, 58, 5, 58, 58]` |
| `caset` | `uint8-array` | ```text Column Address Set ```  Default value: `[0, 0, 0, 127]` |
| `raset` | `uint8-array` | ```text Row Address Set ```  Default value: `[0, 0, 0, 159]` |
| `vmctr1` | `int` | ```text VCOM Control 1 ```  Default value: `10` |
| `invctr` | `int` | ```text Display Inversion Control Set dot inversion or line inversion for each normal/idle/partial mode. ```  Default value: `7` |
| `inversion-on` | `boolean` | ```text Enable Display Inversion Make a drawing with the inverted color of the frame memory. ``` |
| `rgb-is-inverted` | `boolean` | ```text Inverting color format order (RGB->BGR or BGR->RGB) In the case of enabling this option, API reports pixel-format in capabilities as the inverted value of the RGB pixel-format specified in MADCTL. This option is convenient for supporting displays with bugs where the actual color is different from the pixel format of MADCTL. ``` |
| `duplex` | `int` | ```text SPI Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Selecting half duplex allows to use SPI MOSI as a bidirectional line, typically used when only one data line is connected. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ``` |
| `mipi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `mipi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `mipi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `mipi-max-frequency` | `int` | ```text Maximum clock frequency of device's MIPI interface in Hz ``` |
| `mipi-mode` | `int` | ```text MIPI DBI mode in use. Use the macros, not the actual enum value. Here is the concordance list (see dt-bindings/mipi_dbi/mipi_dbi.h)   1     MIPI_DBI_MODE_SPI_3WIRE   2     MIPI_DBI_MODE_SPI_4WIRE   3     MIPI_DBI_MODE_6800_BUS_16_BIT   4     MIPI_DBI_MODE_6800_BUS_9_BIT   5     MIPI_DBI_MODE_6800_BUS_8_BIT   6     MIPI_DBI_MODE_8080_BUS_16_BIT   7     MIPI_DBI_MODE_8080_BUS_9_BIT   8     MIPI_DBI_MODE_8080_BUS_8_BIT ```  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `height` | `int` | ```text Height of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |
| `width` | `int` | ```text Width of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “sitronix,st7735r” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
