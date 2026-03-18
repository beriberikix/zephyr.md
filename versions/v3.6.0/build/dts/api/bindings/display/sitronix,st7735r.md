---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/display/sitronix,st7735r.html
original_path: build/dts/api/bindings/display/sitronix,st7735r.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# sitronix,st7735r (on spi bus)

Vendor: [Sitronix Technology Corporation](../../bindings.md#dt-vendor-sitronix)

## Description

```text
ST7735R/ST7735S 160x128 (max) display controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `reset-gpios` | `phandle-array` | ```text RESET pin. The RESET pin of ST7735R is active low. If connected directly the MCU pin should be configured as active low. ``` |
| `cmd-data-gpios` | `phandle-array` | ```text D/CX pin. The D/CX pin of ST7735R is active low (transmission command byte). If connected directly the MCU pin should be configured as active low. ```  This property is **required**. |
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
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
