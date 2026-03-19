---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/stepper/adi/adi,tmc2209.html
original_path: build/dts/api/bindings/stepper/adi/adi,tmc2209.html
---

# adi,tmc2209

Vendor: [Analog Devices, Inc.](../../../bindings.md#dt-vendor-adi)

Note

An implementation of a driver matching this compatible is available in
[drivers/stepper/adi\_tmc/adi\_tmc22xx\_stepper\_controller.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/adi_tmc22xx_stepper_controller.c).

## Description

```text
Analog Devices TMC2209 stepper motor driver.

Example:
tmc2209: tmc2209 {
    compatible = "adi,tmc2209";
    enable-gpios = <&gpio0 0 GPIO_ACTIVE_HIGH>;
    msx-gpios = <&gpio0 1 GPIO_ACTIVE_HIGH>,
                <&gpio0 2 GPIO_ACTIVE_HIGH>;
    step-gpios = <&gpio0 3 GPIO_ACTIVE_HIGH>;
    dir-gpios = <&gpio0 4 GPIO_ACTIVE_HIGH>;
    dual-edge-step;
}
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `msx-gpios` | `phandle-array` | ```text An array of GPIO pins for configuring the microstep resolution of the driver. The pins should be listed in the following order: - MS1 - MS2 ``` |
| `dual-edge-step` | `boolean` | ```text If present, the stepper motor controller supports dual edge step signals. This means that the step signal can be toggled on both the rising and falling edge. ``` |
| `micro-step-res` | `int` | ```text micro-step resolution to be set while initializing the device driver. ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256` |
| `en-gpios` | `phandle-array` | ```text GPIO pins used to control the enable signal of the motor driver. ``` |
| `step-gpios` | `phandle-array` | ```text The GPIO pins used to send step signals to the stepper motor. ``` |
| `dir-gpios` | `phandle-array` | ```text The GPIO pins used to send direction signals to the stepper motor. Pin will be driven high for forward direction and low for reverse direction. ``` |
| `counter` | `phandle` | ```text Counter used for generating step-accurate pulse signals. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,tmc2209” compatible.

(None)
