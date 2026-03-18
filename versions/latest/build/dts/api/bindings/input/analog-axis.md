---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/input/analog-axis.html
original_path: build/dts/api/bindings/input/analog-axis.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# analog-axis

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
ADC based analog axis input device

Implement an input device generating absolute axis events by periodically
reading from some ADC channels.

Example configuration:

#include <zephyr/dt-bindings/input/input-event-codes.h>

analog_axis {
        compatible = "analog-axis";
        poll-period-ms = <15>;
        axis-x {
                io-channels = <&adc 0>;
                out-deadzone = <8>;
                in-min = <100>;
                in-max = <800>;
                zephyr,axis = <INPUT_ABS_X>;
        };
};
```

## Properties

### Top level properties

These property descriptions apply to “analog-axis”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `poll-period-ms` | `int` | ```text How often to get new ADC samples for the various configured axes in milliseconds. Defaults to 15ms if unspecified. ```  Default value: `15` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “analog-axis” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `io-channels` | `phandle-array` | ```text ADC IO channel to use. ```  This property is **required**. |
| `out-min` | `int` | ```text Minimum value to output on input events. Defaults to 0 if unspecified. ``` |
| `out-max` | `int` | ```text Maximum value to output on input events. Defaults to 255 if unspecified. ```  Default value: `255` |
| `out-deadzone` | `int` | ```text Deadzone for the output center value. If specified output values between the center of the range plus or minus this value will be reported as center. Defaults to 0, no deadzone. ``` |
| `in-min` | `int` | ```text Input value that corresponds to the minimum output value. ```  This property is **required**. |
| `in-max` | `int` | ```text Input value that corresponds to the maximum output value. ```  This property is **required**. |
| `zephyr,axis` | `int` | ```text The input code for the axis to report for the device, typically any of INPUT_ABS_*. ```  This property is **required**. |
| `invert` | `boolean` | ```text If set, invert the raw ADC value before processing it. Useful for differential channels. ``` |
