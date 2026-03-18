---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/gpio/sparkfun,micromod-gpio.html
original_path: build/dts/api/bindings/gpio/sparkfun,micromod-gpio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# sparkfun,micromod-gpio

Vendor: [SparkFun Electronics](../../bindings.md#dt-vendor-sparkfun)

## Description

```text
GPIO pins exposed on micromod headers.

The micromod standard leverages the M.2 connector with 76 pins for
swap between a myriad of supported boards and carriers.

The micromod standard consists of two lanes with the following
supported buses:
* An 6-pin Power Supply header.  No pins on this header are exposed
  by this binding.
* Reset, Boot pins and SWD pins not exposed by this binding.
* 2 UART buses. First with RTS and CTS pins, while the 2nd with only
RX and TX pins. Neither of them are exposed by this binding.
* 2 i2c buses. Only the corresponding interrupt pin is exposed by
this binding.
* 2 SPI buses not exposed by this binding. Only SPI CS control pin
  is exposed by this binding.
* Audio line not exposed by this binding.
* 2 analog pins (A0 and A1).
* 2 digital pins (D0 and D1).
* 12 General purpose pins (G0 - G11).

This binding provides a nexus mapping for the analog, digital and
general purpose gpios in the order depicted below:

  - 00 -> A0                      PIN 34
  - 01 -> A1                      PIN 38
  - 02 -> D0                      PIN 10
  - 03 -> D1/CAM_TRIG             PIN 18
  - 04 -> I2C_INT#                PIN 16
  - 05 -> G0/BUS0                 PIN 40
  - 06 -> G1/BUS1                 PIN 42
  - 07 -> G2/BUS2                 PIN 44
  - 08 -> G3/BUS3                 PIN 46
  - 09 -> G4/BUS4                 PIN 48
  - 10 -> G5/BUS5                 PIN 73
  - 11 -> G6/BUS6                 PIN 71
  - 12 -> G7/BUS7                 PIN 69
  - 13 -> G8                      PIN 67
  - 14 -> G9/ADC_D-/CAM_HSYNC     PIN 65
  - 15 -> G10/ADC_D+/CAM_VSYNC    PIN 63
  - 16 -> G11/SWO                 PIN  8
  - 17 -> SPI_CS                  PIN 55
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
may apply to the “sparkfun,micromod-gpio” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
