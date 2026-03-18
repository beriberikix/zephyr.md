---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/input/gpio-qdec.html
original_path: build/dts/api/bindings/input/gpio-qdec.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# gpio-qdec

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
GPIO based QDEC input device

Implement an input device generating relative axis event reports for a rotary
encoder connected to two GPIOs. The driver is normally idling until it sees a
transition on any of the encoder signal lines, then switches to polling mode
and samples the two signal lines periodically to track the encoder position,
and goes back to idling after the specified timeout.

Example configuration:

#include <zephyr/dt-bindings/input/input-event-codes.h>

qdec {
        compatible = "gpio-qdec";
        gpios = <&gpio0 14 (GPIO_PULL_UP | GPIO_ACTIVE_HIGH)>,
                <&gpio0 13 (GPIO_PULL_UP | GPIO_ACTIVE_HIGH)>;
        steps-per-period = <4>;
        zephyr,axis = <INPUT_REL_WHEEL>;
        sample-time-us = <2000>;
        idle-timeout-ms = <200>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `gpios` | `phandle-array` | ```text GPIO for the A and B encoder signals. ```  This property is **required**. |
| `led-gpios` | `phandle-array` | ```text GPIOs for LED or other components needed for sensing the AB signals. ``` |
| `led-pre-us` | `int` | ```text Time between enabling the led-gpios output pins and reading the encoder state on the input pins, meant to give the state detector (such a phototransistor) time to settle to right state. Required if led-gpios and idle-poll-time-us are specified, can be explicitly set to 0 for no delay. ``` |
| `steps-per-period` | `int` | ```text How many steps to count before reporting an input event. ```  This property is **required**. |
| `zephyr,axis` | `int` | ```text The input code for the axis to report for the device, typically any of INPUT_REL_*. ```  This property is **required**. |
| `sample-time-us` | `int` | ```text How often to sample the A and B signal lines when tracking the encoder movement. ```  This property is **required**. |
| `idle-poll-time-us` | `int` | ```text How often to sample the A and B signal while idling. If unset then the driver will use the GPIO interrupt to exit idle state, and any GPIO specified in led-gpios will be enabled all the time. If non zero, then the driver will poll every idle-poll-time-us microseconds while idle, and only activate led-gpios before sampling the encoder state. ``` |
| `idle-timeout-ms` | `int` | ```text Timeout for the last detected transition before stopping the sampling timer and going back to idle state. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “gpio-qdec” compatible.

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
