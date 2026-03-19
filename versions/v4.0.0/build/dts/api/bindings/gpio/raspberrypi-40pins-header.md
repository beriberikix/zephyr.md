---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/gpio/raspberrypi-40pins-header.html
original_path: build/dts/api/bindings/gpio/raspberrypi-40pins-header.html
---

# raspberrypi-40pins-header

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
GPIO pins exposed on Raspberry Pi 40-pin header.

The Raspberry Pi layout provides a 2x20 pins header.

This binding provides a nexus mapping for 28 pins as depicted below.

    -  3V3                  5V               -
    0  GPIO2/I2C1_SDA       5V               -
    1  GPIO3/I2C1_SCL       GND              -
    2  GPIO4                GPIO14/UART0_TXD 3
    -  GND                  GPIO15/UART0_RXD 4
    5  GPIO17               GPIO18           6
    7  GPIO27               GND              -
    8  GPIO22               GPIO23           9
    -  3V3                  GPIO24           10
    11 GPIO10/SPI0_MOSI     GND              -
    12 GPIO9/SPI0_MISO      GPIO25           13
    14 GPIO11/SPI0_SCLK     GPIO8/SPI0_CE0   15
    -  GND                  GPIO7/SPI0_CE1   16
    17 ID_SD/I2C0_SDA       ID_SC/I2C0_SCL   18
    19 GPIO5                GND              -
    20 GPIO6                GPIO12           21
    22 GPIO13               GND              -
    23 GPIO19               GPIO16           24
    25 GPIO26               GPIO20           26
    -  GND                  GPIO21           27
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
may apply to the “raspberrypi-40pins-header” compatible.

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
