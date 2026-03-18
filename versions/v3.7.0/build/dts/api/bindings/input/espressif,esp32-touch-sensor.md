---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/input/espressif,esp32-touch-sensor.html
original_path: build/dts/api/bindings/input/espressif,esp32-touch-sensor.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# espressif,esp32-touch

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

## Description

```text
Zephyr input touch sensor parent node

This defines a group of touch sensors that can generate input events. Each touch
sensor is defined in a child node of the touch-sensor node and defines a specific key
code.

For example:

#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <zephyr/dt-bindings/input/esp32-touch-sensor-input.h>

&touch {
       compatible = "espressif,esp32-touch";
       status = "okay";

       debounce-interval-ms = <30>;
       href-microvolt = <27000000>;
       lref-microvolt = <500000>;
       href-atten-microvolt = <1000000>;
       filter-mode = <ESP32_TOUCH_FILTER_MODE_IIR_16>;
       filter-debounce-cnt = <1>;
       filter-noise-thr = <ESP32_TOUCH_FILTER_NOISE_THR_4_8TH>;
       filter-jitter-step = <4>;
       filter-smooth-level = <ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_2>;

       touch_sensor_0 {
               channel-num = <1>;
               channel-sens = <20>;
               zephyr,code = <INPUT_KEY_0>;
       };
};
```

## Properties

### Top level properties

These property descriptions apply to “espressif,esp32-touch”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `debounce-interval-ms` | `int` | ```text Debouncing interval time in milliseconds. ```  Default value: `30` |
| `href-microvolt` | `int` | ```text Touch sensor high reference voltage. ```  Default value: `2700000`  Legal values: `2400000`, `2500000`, `2500000`, `2700000` |
| `lref-microvolt` | `int` | ```text Touch sensor low reference voltage. ```  Default value: `500000`  Legal values: `500000`, `600000`, `700000`, `800000` |
| `href-atten-microvolt` | `int` | ```text Touch sensor high reference attenuation voltage. ```  Default value: `1000000`  Legal values: `1500000`, `1000000`, `500000`, `0` |
| `filter-mode` | `int` | ```text Touch sensor IIR filter coefficient. If not specified defaults to ESP32_TOUCH_FILTER_MODE_IIR_16. ```  Default value: `2` |
| `filter-debounce-cnt` | `int` | ```text Touch sensor debounce count. If not specified defaults to 1. ```  Default value: `1` |
| `filter-noise-thr` | `int` | ```text Touch sensor noise threshold coefficient. If not specified defaults to ESP32_TOUCH_FILTER_NOISE_THR_4_8TH. ``` |
| `filter-jitter-step` | `int` | ```text Touch sensor jitter filter step size. If not specified defaults to 4. ```  Default value: `4` |
| `filter-smooth-level` | `int` | ```text Touch sensor level of filter applied on the original data against large noise interference. If not specified defaults to ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_2. ```  Default value: `1` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “espressif,esp32-touch” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `channel-num` | `int` | ```text Touch sensor channel number ```  This property is **required**. |
| `channel-sens` | `int` | ```text Touch sensor channel sensibility in 100th. If not specified defaults to 20. ```  Default value: `20` |
| `zephyr,code` | `int` | ```text Key code to emit. ```  This property is **required**. |
