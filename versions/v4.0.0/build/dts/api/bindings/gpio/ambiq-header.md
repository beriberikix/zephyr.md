---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/gpio/ambiq-header.html
original_path: build/dts/api/bindings/gpio/ambiq-header.html
---

# ambiq-header

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
GPIO pins exposed on Ambiq Apollo4p EVB headers

The Ambiq Apollo4p EVB layout provides 5x16 and 1x20 pin headers.

The binding provides a nexus mapping for these pins as depicted below.

        J7                              J12

VDD_MCU - VDD_MCU -             GPIO22 22 GND     -
VDD_EXT - VDD_EXT -             GPIO23 23 GPIO24 24
nRST    - GND     -             VDD_MCU - GND     -
VDD_EXT - VDD_EXT -             GND     - GPIO64 64
VDD_5V  - VDD_5V  -             GPIO61 61 GPIO65 65
GND     - GND     -             GPIO63 63 GPIO66 66
GND     - GPIO100 100           GPIO62 62 GPIO67 67
VDDH2   - GPIO97  97            GPIO47 47 GPIO68 68
                                GPIO49 49 GPIO69 69
        J9                      GPIO48 48 GPIO70 70

GPIO19 19 GPIO96  96                    J11
GPIO18 18 GPIO95  95
GPIO17 17 GPIO98  98            GPIO53 53 GPIO71 71
GPIO16 16 GPIO99  99            GPIO52 52 GPIO72 72
GPIO15 15 GPIO102 102           GPIO91 91 GPIO73 73
GPIO14 14 GPIO34  34            GPIO90 90 GPIO93 93
GPIO13 13 GPIO35  35            GPIO11 11 GPIO92 92
GPIO12 12 GPIO36  36            GPIO10 10 GPIO33 33
                                GPIO8  8  GPIO32 32
                                GPIO9  9  GPIO31 31

                                        J10

                                GPIO28 28 GPIO60 60
                                GPIO30 30 GPIO59 59
                                GPIO94 94 GPIO58 58
                                GPIO55 55 GPIO7  7
                                GPIO0  0  GPIO54 54
                                GPIO51 51 GPIO1  1
                                GPIO2  2  GPIO50 50
                                GPIO3  3  GPIO4  4

                                  Voltage Header

                                VDD_EXT - VDD_5V -
                                GND     - GND    -
                                BIAS    - BIAS   -
                                GND     - AUDA   -
                                GND     - GND    -
                                D1P     - DON    -
                                D1N     - DOP    -
                                GND     - GND    -
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
may apply to the “ambiq-header” compatible.

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
