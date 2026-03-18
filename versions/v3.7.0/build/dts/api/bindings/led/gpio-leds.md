---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/led/gpio-leds.html
original_path: build/dts/api/bindings/led/gpio-leds.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# gpio-leds

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
This allows you to define a group of LEDs. Each LED in the group is
controlled by a GPIO. Each LED is defined in a child node of the
gpio-leds node.

Here is an example which defines three LEDs in the node /leds:

/ {
     leds {
             compatible = "gpio-leds";
             led_0 {
                     gpios = <&gpio0 1 GPIO_ACTIVE_LOW>;
             };
             led_1 {
                     gpios = <&gpio0 2 GPIO_ACTIVE_HIGH>;
             };
             led_2 {
                     gpios = <&gpio1 15 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>;
             };
     };
};

Above:

- led_0 is pin 1 on gpio0. The LED is on when the pin is low,
  and off when the pin is high.
- led_1 is pin 2 on gpio0. The LED is on when the pin is high,
  and off when it is low.
- led_2 is pin 15 on gpio1. The LED is on when the pin is low,
  and the pin's internal pull-up resistor should be enabled.
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `gpios` | `phandle-array` | This property is **required**. |
| `label` | `string` | ```text Human readable string describing the LED. It can be used by an application to identify this LED or to retrieve its number/index (i.e. child node number) on the parent device. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
