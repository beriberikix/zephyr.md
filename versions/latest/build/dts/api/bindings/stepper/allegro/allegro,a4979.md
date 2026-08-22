---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/stepper/allegro/allegro,a4979.html
original_path: build/dts/api/bindings/stepper/allegro/allegro,a4979.html
---

# allegro,a4979

Vendor: [Allegro DVT](../../../bindings.md#dt-vendor-allegro)

Note

An implementation of a driver matching this compatible is available in
[drivers/stepper/allegro/a4979.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/allegro/a4979.c).

## Description

```text
Allegro A4979 microstepping stepper motor driver.
A4979 is a flexible microstepping motor driver with built-in translator for easy operation.
It is designed to operate bipolar stepper motors in full-, half-, quarter-, and sixteenth-step
modes.

Example:
a4979: a4979 {
    status = "okay";
    compatible = "allegro,a4979";
    micro-step-res = <2>;
    reset-gpios = <&gpiod 10 GPIO_ACTIVE_HIGH>;
    dir-gpios = <&gpiod 14 GPIO_ACTIVE_HIGH>;
    step-gpios = <&gpiod 15 GPIO_ACTIVE_HIGH>;
    en-gpios = <&gpiod 11 GPIO_ACTIVE_HIGH>;
    m0-gpios = <&gpiod 13 0>;
    m1-gpios = <&gpiod 12 0>;
    counter = <&counter5>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `m0-gpios` | `phandle-array` | ```text Microstep configuration pin 0. ```  This property is **required**. |
| `m1-gpios` | `phandle-array` | ```text Microstep configuration pin 1. ```  This property is **required**. |
| `reset-gpios` | `phandle-array` | ```text Reset pin ```  This property is **required**. |
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
may apply to the “allegro,a4979” compatible.

(None)
