---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.html
original_path: build/dts/api/bindings/pwm/nordic,nrf-sw-pwm.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nordic,nrf-sw-pwm

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
nRFx S/W PWM
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#pwm-cells` | `int` | ```text Number of items to expect in a pwm specifier ```  This property is **required**.  Constant value: `3` |
| `generator` | `phandle` | ```text Reference to TIMER or RTC instance for generating PWM output signals ```  This property is **required**. |
| `clock-prescaler` | `int` | ```text Clock prescaler for RTC or TIMER used for generating PWM output signals.  RTC: needs to be set to 0, which gives 32768 Hz base clock for PWM generation.  TIMER: 16 MHz / 2^prescaler base clock is used for PWM generation. ```  This property is **required**. |
| `channel-gpios` | `phandle-array` | ```text An array of GPIOs assigned as outputs for the PWM channels. The number of items in this array determines the number of channels that this PWM will provide. This value is limited by the number of compare registers in the used RTC/TIMER instance minus 1.  Example:    sw_pwm: sw-pwm {     compatible = "nordic,nrf-sw-pwm";     ...     channel-gpios = <&gpio0 20 GPIO_ACTIVE_HIGH>,                     <&gpio1 12 GPIO_ACTIVE_HIGH>;     ...   };  The above will assign P0.20 as the output for channel 0 and P1.12 as the output for channel 1. Both outputs will be initially configured as active high.  Please note that in the flags cell (the last component of each item of the array) only the GPIO flags that specify the active level are taken into account (any others are ignored), and they are used only when the initial (inactive) state of the outputs is set. After any PWM signal generation is requested for a given channel, the polarity of its output is determined by the flag specified in the request, i.e. PWM_POLARITY_INVERTED or PWM_POLARITY_NORMAL. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-sw-pwm” compatible.

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

## Specifier cell names

- pwm cells: channel, period, flags
