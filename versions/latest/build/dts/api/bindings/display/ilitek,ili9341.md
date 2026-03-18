---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/display/ilitek,ili9341.html
original_path: build/dts/api/bindings/display/ilitek,ili9341.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ilitek,ili9341 (on mipi-dbi bus)

Vendor: [ILI Technology Corporation (ILITEK)](../../bindings.md#dt-vendor-ilitek)

## Description

```text
ILI9341 320x240 display controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `ifmode` | `uint8-array` | ```text RGB interface signal control (IFMOD) register value. ```  Default value: `[64]` |
| `ifctl` | `uint8-array` | ```text Interface control (IFCTL) register value. ```  Default value: `[1, 0, 0]` |
| `pwctrla` | `uint8-array` | ```text Power control A (PWCTRLA) register value. ```  Default value: `[57, 44, 0, 52, 2]` |
| `pwctrlb` | `uint8-array` | ```text Power control B (PWCTRLB) register value. ```  Default value: `[0, 139, 48]` |
| `pwseqctrl` | `uint8-array` | ```text Power on sequence control (PWSEQCTRL) register value. ```  Default value: `[85, 1, 35, 1]` |
| `timctrla` | `uint8-array` | ```text Driver timing control A (TIMCTRLA) register value. ```  Default value: `[132, 17, 122]` |
| `timctrlb` | `uint8-array` | ```text Driver timing control B (TIMCTRLB) register value. ```  Default value: `[0, 0]` |
| `pumpratioctrl` | `uint8-array` | ```text Pump ratio control (PUMPRATIOCTRL) register value. ```  Default value: `[16]` |
| `enable3g` | `uint8-array` | ```text Enable 3G (ENABLE3G) register value. ```  Default value: `[2]` |
| `etmod` | `uint8-array` | ```text Entry Mode Set (ETMOD) register value. ```  Default value: `[6]` |
| `gamset` | `uint8-array` | ```text Gamma set (GAMSET) register value. ```  Default value: `[1]` |
| `frmctr1` | `uint8-array` | ```text Frame rate control (in normal mode / full colors) (FRMCTR1) register value. ```  Default value: `[0, 27]` |
| `disctrl` | `uint8-array` | ```text Display function control (DISCTRL) register value. Note that changing default SS bit value (0) may interfere with display rotation. ```  Default value: `[10, 130, 39, 4]` |
| `pwctrl1` | `uint8-array` | ```text Power control 1 (PWCTRL1) register values. ```  Default value: `[33]` |
| `pwctrl2` | `uint8-array` | ```text Power control 2 (PWCTRL2) register values. ```  Default value: `[16]` |
| `vmctrl1` | `uint8-array` | ```text VCOM control 1 (VMCTRL1) register values. ```  Default value: `[49, 60]` |
| `vmctrl2` | `uint8-array` | ```text VCOM control 2 (VMCTRL2) register values. ```  Default value: `[192]` |
| `pgamctrl` | `uint8-array` | ```text Positive gamma correction (PGAMCTRL) register values. ```  Default value: `[15, 34, 31, 10, 14, 6, 77, 118, 59, 3, 14, 4, 19, 14, 12]` |
| `ngamctrl` | `uint8-array` | ```text Negative gamma correction (NGAMCTRL) register values. ```  Default value: `[12, 35, 38, 4, 16, 4, 57, 36, 75, 3, 11, 11, 51, 55, 15]` |
| `pixel-format` | `int` | ```text Display pixel format. Note that when RGB888 pixel format is selected only 6 color bits are actually used being in practice equivalent to RGB666. ```  Legal values: `0`, `1` |
| `rotation` | `int` | ```text Display rotation (CW) in degrees. ```  Legal values: `0`, `90`, `180`, `270` |
| `display-inversion` | `boolean` | ```text Display inversion mode. Every bit is inverted from the frame memory to the display. ``` |
| `duplex` | `int` | ```text SPI Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Selecting half duplex allows to use SPI MOSI as a bidirectional line, typically used when only one data line is connected. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ``` |
| `mipi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `mipi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `mipi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `mipi-max-frequency` | `int` | ```text Maximum clock frequency of device's MIPI interface in Hz ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `height` | `int` | ```text Height of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |
| `width` | `int` | ```text Width of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ilitek,ili9341” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
