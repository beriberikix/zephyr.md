---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/counter/espressif,esp32-timer.html
original_path: build/dts/api/bindings/counter/espressif,esp32-timer.html
---

# espressif,esp32-timer

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

Note

An implementation of a driver matching this compatible is available in
[drivers/counter/counter\_esp32\_tmr.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/counter_esp32_tmr.c).

## Description

```text
Espressif's general-purpose Timers.
Each Timer is part of a Timer Group and the number of available Timers
is SoC-dependent.

As as example, ESP32 has 4 Timers available, which are split in two
different groups (TIM0_G0, TIM1_G0, TIM0_G1 and TIM1_G1).

In order to use one of the available timers on your application add
a <board>.overlay file with contents as below

  &timer0 {
          status = "okay";
          prescaler = <10>;
  };

From the above, setting 'status' is required while the prescaler is
optional. Check below for more information on the prescaler.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `group` | `int` | ```text The Timer Group index to which a timer belongs. ```  This property is **required**.  Legal values: `0`, `1` |
| `index` | `int` | ```text The index that identifies a timer within a Timer Group. ```  This property is **required**.  Legal values: `0`, `1` |
| `prescaler` | `int` | ```text The prescaler value defines the factor by which the APB clock will be divided. The outcome of which serves as clock reference to the Timer itself.  The allowed values for this property are in the range [2..65535]. Values above that range will be 16-bit-masked. Values 0 and 1 will be forced to 2. ```  Default value: `2` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “espressif,esp32-timer” compatible.

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
