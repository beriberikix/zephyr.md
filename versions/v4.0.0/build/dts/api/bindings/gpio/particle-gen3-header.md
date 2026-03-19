---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/gpio/particle-gen3-header.html
original_path: build/dts/api/bindings/gpio/particle-gen3-header.html
---

# particle-gen3-header

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
GPIO pins exposed on Particle Gen3 (Feather) headers.

The Particle Gen3 boards are compatible with the Adafruit Feather
"shields" but use a different orientation and pin numbering scheme.

With the board oriented with the micro USB at the top:
* A 12-pin header on the right.  9 pins on this header are exposed
  by this binding
* A 16-pin header.  13 pins on this header are exposed by this
  binding.

This binding provides a nexus mapping for 22 pins where parent pins
0 through 8 correspond to the pins on the 12-pin header, starting
from the bottom; and pins 9 through 21 correspond to pins on the
16-pin header, skipping the bottom pin then assigning 9 through 19,
skipping over GND, and replacing the lower 3V3 with pin 20.  The
physical layout is depicted below.

    21 RESETn
    -  3V3
    20 MODEn
    -  GND
    19 ADC0                  LiPo+   -
    18 ADC1                  ENABLE  -
    17 ADC2                  VBUS    -
    16 ADC3                  PWM1    8
    15 ADC4                  PWM0    7
    14 SS                    PWM1    6
    13 SCK                   PWM1    5
    12 MOSI                  PWM1    4
    11 MISO                  PWM3    3
    10 RX                    PWM3    2
     9 TX                    SCL     1
    -  n/c                   SDA     0
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
may apply to the “particle-gen3-header” compatible.

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
