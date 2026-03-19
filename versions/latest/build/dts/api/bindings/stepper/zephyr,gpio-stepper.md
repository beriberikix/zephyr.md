---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/stepper/zephyr,gpio-stepper.html
original_path: build/dts/api/bindings/stepper/zephyr,gpio-stepper.html
---

# zephyr,gpio-stepper

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[drivers/stepper/gpio\_stepper\_controller.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/gpio_stepper_controller.c).

## Description

```text
GPIO Stepper Controller for darlington transistor arrays or dual H-bridge

Example:
  /* Lead A is connected Lead C and Lead B is connected to Lead D*/
  stepper: stepper {
      compatible = "zephyr,gpio-stepper";
      gpios = <&gpioa 9 GPIO_ACTIVE_HIGH>,  /* Lead A1/A */
              <&gpioc 7 GPIO_ACTIVE_HIGH>,  /* Lead B1/B */
              <&gpiob 0 GPIO_ACTIVE_HIGH>,  /* Lead A2/C */
              <&gpioa 7 GPIO_ACTIVE_HIGH>;  /* Lead B2/D */
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `gpios` | `phandle-array` | ```text The gpio pin array on which the stepper inputs are to be connected ```  This property is **required**. |
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
may apply to the “zephyr,gpio-stepper” compatible.

(None)
