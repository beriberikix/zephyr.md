---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/stepper/zephyr,fake-stepper.html
original_path: build/dts/api/bindings/stepper/zephyr,fake-stepper.html
---

# zephyr,fake-stepper

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[drivers/stepper/fake\_stepper\_controller.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/fake_stepper_controller.c).

## Description

```text
This binding provides a fake stepper controller for use as either a stub or a mock in
Zephyr testing.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `invert-direction` | `boolean` | ```text Invert motor direction. ``` |
| `micro-step-res` | `int` | ```text micro-step resolution to be set while initializing the device driver. ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256` |
| `en-gpios` | `phandle-array` | ```text GPIO pins used to control the enable signal of the motor driver. ``` |
| `step-gpios` | `phandle-array` | ```text The GPIO pins used to send step signals to the stepper motor. ``` |
| `dir-gpios` | `phandle-array` | ```text The GPIO pins used to send direction signals to the stepper motor. Pin will be driven high for forward direction and low for reverse direction. ``` |
| `counter` | `phandle` | ```text Counter used for generating step-accurate pulse signals. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,fake-stepper” compatible.

(None)
