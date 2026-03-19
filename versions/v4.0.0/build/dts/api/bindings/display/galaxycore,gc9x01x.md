---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/display/galaxycore,gc9x01x.html
original_path: build/dts/api/bindings/display/galaxycore,gc9x01x.html
---

# galaxycore,gc9x01x (on mipi-dbi bus)

Vendor: [Galaxycore, Inc.](../../bindings.md#dt-vendor-galaxycore)

Note

An implementation of a driver matching this compatible is available in
[drivers/display/display\_gc9x01x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_gc9x01x.c).

## Description

```text
GC9X01X display driver.

This driver implements support for various GC9X01X graphics
controllers and different display sizes. It has been validated
for following controllers:
 - GC9101A: (Waveshare 240x240, 1.28inch round lcd display 240x240)

Here is an example to define a display interface:

&spi2 {
  gc9a01a_lcd: gc9a01a_lcd@0 {
    compatible = "galaxycore,gc9x01x";
    reg = <0>;
    spi-max-frequency = <100000000>;
    cmd-data-gpios = <&gpio0 4 GPIO_ACTIVE_HIGH>;
    reset-gpios = <&gpio0 8 GPIO_ACTIVE_LOW>;
    pixel-format = <PANEL_PIXEL_FORMAT_RGB_565>;
    width = <240>;
    height = <240>;
  };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `orientation` | `string` | ```text Display orientation (CW) in degrees. ```  Default value: `normal`  Legal values: `'normal'`, `'90'`, `'180'`, `'270'` |
| `display-inversion` | `boolean` | ```text Display inversion mode. Every bit is inverted from the frame memory to the display. ``` |
| `pwrctrl1` | `uint8-array` | ```text Power-control 1 register value ```  Default value: `[0]` |
| `pwrctrl2` | `uint8-array` | ```text Power-control 2 register value ```  Default value: `[19]` |
| `pwrctrl3` | `uint8-array` | ```text Power-control 3 register value ```  Default value: `[19]` |
| `pwrctrl4` | `uint8-array` | ```text Power-control 4 register value ```  Default value: `[34]` |
| `gamma1` | `uint8-array` | ```text Gamma correction 1 register values (negative polarity) ```  Default value: `[69, 9, 8, 8, 38, 42]` |
| `gamma2` | `uint8-array` | ```text Gamma correction 3 register values ```  Default value: `[67, 112, 114, 54, 55, 111]` |
| `gamma3` | `uint8-array` | ```text Gamma correction 3 register values (positive polarity) ```  Default value: `[69, 9, 8, 8, 38, 42]` |
| `gamma4` | `uint8-array` | ```text Gamma correction 4 register values ```  Default value: `[67, 112, 114, 54, 55, 111]` |
| `framerate` | `uint8-array` | ```text Framerate register value ```  Default value: `[52]` |
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
| `pixel-format` | `int` | ```text Initial Pixel format for panel attached to this controller. See dt-bindings/display/panel.h for a list ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “galaxycore,gc9x01x” compatible.

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
