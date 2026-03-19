---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/stepper/ti/ti,drv8424.html
original_path: build/dts/api/bindings/stepper/ti/ti,drv8424.html
---

# ti,drv8424

Vendor: [Texas Instruments](../../../bindings.md#dt-vendor-ti)

Note

An implementation of a driver matching this compatible is available in
[drivers/stepper/ti/drv8424.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/ti/drv8424.c).

## Description

```text
TI DRV8424 stepper motor driver.
SAFETY:
The counter needs to support both set_top_value functionalities: Setting a new top value and
attaching an ISR to the turnaround.
SAFETY:
The step gpio pin needs to be connected directly to the SOC GPIO controller, connecting the
pin to a controller connected via a bus such as i2c or others will lead to undefined behaviour.

Example:
drv8424: drv8424 {
  status = "okay";
  compatible = "ti,drv8424";

  dir-gpios = <&arduino_header 18 0>;
  step-gpios = <&arduino_header 19 0>;
  sleep-gpios = <&arduino_header 15 GPIO_ACTIVE_LOW>;
  en-gpios  = <&arduino_header 14 0>;
  m0-gpios = <&mikroe_stepper_gpios 0 0>;
  m1-gpios = <&mikroe_stepper_gpios 1 0>;
  counter = <&counter2>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `fault-gpios` | `phandle-array` | ```text Fault pin. ``` |
| `sleep-gpios` | `phandle-array` | ```text Sleep pin (active low). ``` |
| `m0-gpios` | `phandle-array` | ```text Microstep configuration pin 0. ```  This property is **required**. |
| `m1-gpios` | `phandle-array` | ```text Microstep configuration pin 1. ```  This property is **required**. |
| `micro-step-res` | `int` | ```text micro-step resolution to be set while initializing the device driver. ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256` |
| `en-gpios` | `phandle-array` | ```text GPIO pins used to control the enable signal of the motor driver. ``` |
| `step-gpios` | `phandle-array` | ```text The GPIO pins used to send step signals to the stepper motor. ``` |
| `dir-gpios` | `phandle-array` | ```text The GPIO pins used to send direction signals to the stepper motor. Pin will be driven high for forward direction and low for reverse direction. ``` |
| `counter` | `phandle` | ```text Counter used for generating step-accurate pulse signals. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,drv8424” compatible.

(None)
