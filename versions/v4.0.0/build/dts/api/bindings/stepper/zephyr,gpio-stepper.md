---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/stepper/zephyr,gpio-stepper.html
original_path: build/dts/api/bindings/stepper/zephyr,gpio-stepper.html
---

# zephyr,gpio-steppers

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[drivers/stepper/gpio\_stepper\_controller.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/gpio_stepper_controller.c).

## Description

```text
GPIO Stepper Controller cluster for darlington transistor arrays or dual H-bridge

Example:
  /* Lead A is connected Lead C and Lead B is connected to Lead D*/
  stepper {
      compatible = "zephyr,gpio-steppers";
      motor: motor {
          gpios = <&gpioa 9 GPIO_ACTIVE_HIGH>,  /* Lead A1/A */
                  <&gpioc 7 GPIO_ACTIVE_HIGH>,  /* Lead B1/B */
                  <&gpiob 0 GPIO_ACTIVE_HIGH>,  /* Lead A2/C */
                  <&gpioa 7 GPIO_ACTIVE_HIGH>;  /* Lead B2/D */
      };
  };
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `gpios` | `phandle-array` | ```text The gpio pin array on which the stepper inputs are to be connected ```  This property is **required**. |
| `invert-direction` | `boolean` | ```text Invert motor direction. ``` |
| `micro-step-res` | `int` | ```text micro-step resolution to be set while initializing the device driver. ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256` |
