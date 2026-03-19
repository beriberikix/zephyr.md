---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/display/ftdi,ft800.html
original_path: build/dts/api/bindings/display/ftdi,ft800.html
---

# ftdi,ft800 (on spi bus)

Vendor: [Future Technology Devices International Ltd.](../../bindings.md#dt-vendor-ftdi)

Note

An implementation of a driver matching this compatible is available in
[drivers/misc/ft8xx/ft8xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/misc/ft8xx/ft8xx.c).

## Description

```text
FTDI FT800 graphic controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `irq-gpios` | `phandle-array` | ```text Optional IRQ line of FT800 controller ``` |
| `pclk` | `int` | ```text The value to divide the main clock by for PCLK. If the typical main clock was 48MHz and this value is 5, the PCLK will be 9.6 MHz. Must be positive value to enable the screen ```  This property is **required**. |
| `pclk_pol` | `int` | ```text Polarity of PCLK. If it is set to zero, PCLK polarity is on the rising edge. If it is set to one, PCLK polarity is on the falling edge. ```  This property is **required**. |
| `cspread` | `int` | ```text Controls the transition of RGB signals with PCLK active clock edge. When set to 0, R[7:2],G[7:2] and B[7:2] signals change following the active edge of PCLK. When set to 1, R[7:2] changes a PCLK clock early and B[7:2] a PCLK clock later, which helps reduce the system noise. ```  This property is **required**. |
| `swizzle` | `int` | ```text Controls the arrangement of output RGB pins, which may help support different LCD panel. Please check FT800 Programmers Guide for details. ```  This property is **required**. |
| `vsize` | `int` | ```text Number of visible lines of pixels in one frame ```  This property is **required**. |
| `voffset` | `int` | ```text Number of invisible lines at the beginning of a new frame ```  This property is **required**. |
| `vcycle` | `int` | ```text Number of all lines in a frame. It includes all visible and invisible lines at the beginning and at the end of a frame. ```  This property is **required**. |
| `vsync0` | `int` | ```text Number of lines for the high state of signal VSYNC at the start of new frame. ```  This property is **required**. |
| `vsync1` | `int` | ```text Number of lines for signal VSYNC toggle takes at the start of new frame. ```  This property is **required**. |
| `hsize` | `int` | ```text Number of PCLK cycles per visible part of horizontal line ```  This property is **required**. |
| `hoffset` | `int` | ```text Number of PCLK cycles before pixels are scanned out for given line ```  This property is **required**. |
| `hcycle` | `int` | ```text Number of total PCLK cycles per horizontal line scan. ```  This property is **required**. |
| `hsync0` | `int` | ```text Number of PCLK cycles of HSYNC high state during start of line ```  This property is **required**. |
| `hsync1` | `int` | ```text Number of PCLK cycles for HSYNC toggle during start of line. ```  This property is **required**. |
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
may apply to the “ftdi,ft800” compatible.

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
