---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/raspberrypi,pico-rosc.html
original_path: build/dts/api/bindings/clock/raspberrypi,pico-rosc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# raspberrypi,pico-rosc

Vendor: [Raspberry Pi Foundation](../../bindings.md#dt-vendor-raspberrypi)

## Description

```text
The representation of Raspberry Pi Pico ring oscillator.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `range` | `int` | ```text Specify the number of ring oscillator stages to use.   - LOW: 8 (default)   - MEDIUM: 6   - HIGH: 4   - TOOHIGH: 2 ```  This property is **required**. |
| `stage-drive-strength` | `array` | ```text Specifies the drive strength of the eight stages of the ring oscillator. The valid range of each value is between 0 and 7. ```  This property is **required**. |
| `phase-flip` | `boolean` | ```text Flipping phase-shifter output. ``` |
| `phase` | `int` | ```text The phase-shift value. The valid range is 0 to 3 ``` |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `clock-div` | `int` | ```text fixed clock divider ``` |
| `clock-mult` | `int` | ```text fixed clock multiplier ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “raspberrypi,pico-rosc” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `clocks` | `phandle-array` | ```text input clock source ``` |
