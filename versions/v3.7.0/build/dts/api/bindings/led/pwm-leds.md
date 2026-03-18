---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/led/pwm-leds.html
original_path: build/dts/api/bindings/led/pwm-leds.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# pwm-leds

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
PWM LEDs parent node
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `pwms` | `phandle-array` | ```text Reference to a PWM instance.  The period field is used by the set_brightness function of the LED API. Its value should at least be greater that 100 nanoseconds (for a full brigtness granularity) and lesser than 50 milliseconds (average visual persistence time of the human eye). Typical values for the PWM period are 10 or 20 milliseconds. ```  This property is **required**. |
| `label` | `string` | ```text Human readable string describing the LED. It can be used by an application to identify this LED or to retrieve its number/index (i.e. child node number) on the parent device. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
