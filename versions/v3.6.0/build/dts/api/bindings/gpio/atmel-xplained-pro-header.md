---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/gpio/atmel-xplained-pro-header.html
original_path: build/dts/api/bindings/gpio/atmel-xplained-pro-header.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# atmel-xplained-pro-header

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
GPIO pins exposed on Atmel Xplained Pro headers.

The Xplained Pro layout provide a standard 20 pin header.  A board can have
one or more headers and can share pins.  The extension headers are given
names EXTn where n ϵ [1…7], n is determined by which ID pin is connected
to the embedded debugger.  A header with ID7 signal from the embedded
debugger connected should be called EXT7. PWR, EXT1, EXT2 and EXT3 are
standard extension headers that have a predefined position according to the
list below:
  * PWR is right angled at the top right hand side of the board. This
  header must always be implemented.
  * EXT1 is right angled at the top right hand side of the board, located
  below the PWR header. This header must always be present.
  * EXT2 is right angled and at the bottom right hand side of the board.
  This header is mandatory for medium and large boards and should not be
  implemented on small boards.
  * EXT3 is right angled pointing downwards
All MCU boards have to implement at least PWR, EXT1, EXT2 (on medium and
large boards), and EXT3. EXT4 to EXT7 can be placed differently depending
on the board design. EXT4 to EXT7 can either be standard extension headers
or application specific headers.

Documentation:
https://www.microchip.com/development-tools/xplained-boards
http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42091-Atmel-Xplained-Pro-Hardware-Development-Kit_User%20Guide.pdf

This binding provides a nexus mapping for 20 pins where pins are disposed
to have a even and odd column:

                       Connector
Bind      Pin Name     Pin   Pin  Pin Name        Bind
                   ID  1       2  GND
  0            ADC(+)  3       4  ADC(-)           1
  2   UART(RTS)/GPIO1  5       6  UART(CTS)/GPIO2  3
  4            PWM(+)  7       8  PWM(-)           5
  6         IRQ/GPIO3  9      10  SPI(CS1)/GPIO4   7
  8          I2C(SDA)  11     12  I2C(SCL)         9
 10          UART(RX)  13     14  UART(TX)         11
 12          SPI(CS0)  15     16  SPI(MOSI)        13
 14         SPI(MISO)  17     18  SPI(SCK)         15
                  GND  19     20  VDD(+3.3V)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `gpio-map` | `compound` | This property is **required**. |
| `gpio-map-mask` | `compound` |  |
| `gpio-map-pass-thru` | `compound` |  |
| `#gpio-cells` | `int` | ```text Number of items to expect in a GPIO specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “atmel-xplained-pro-header” compatible.

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
