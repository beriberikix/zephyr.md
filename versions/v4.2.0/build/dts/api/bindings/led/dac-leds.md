---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/led/dac-leds.html
original_path: build/dts/api/bindings/led/dac-leds.html
---

# dac-leds

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

Note

An implementation of a driver matching this compatible is available in
[drivers/led/led\_dac.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/led_dac.c).

## Description

```text
Group of DAC-controlled LEDs.

Each LED is defined in a child node of the dac-leds node.

Here is an example which defines an LED in the node /leds:

/ {
        leds {
                compatible = "dac-leds";
                led_0 {
                        dac-dev = <&dac1>;
                        channel = <0>;
                        resolution = <12>;
                };
                led_1 {
                        dac-dev = <&dac1>;
                        channel = <1>;
                        resolution = <12>;
                        voltage-min-brightness-mv = <1400>;
                        voltage-max-brightness-mv = <2700>;
                        voltage-max-dac-mv = <3300>;
                        output-buffer;
                };
        };
};

Above:

- led_0 uses dac1 channel 0 with 12 bit resolution.
- led_1 uses dac1 channel 1 with 12 bit resolution and setup to supply an LED directly.
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `dac-dev` | `phandle` | ```text Property containing phandle to DAC e.g. &dac. ```  This property is **required**. |
| `channel` | `int` | ```text The DAC channel. ```  This property is **required**. |
| `resolution` | `int` | ```text The DAC resolution to use. ```  This property is **required**. |
| `voltage-min-brightness-mv` | `int` | ```text Voltage at brightness 0%. If not specified the minimum DAC output voltage is used. ``` |
| `voltage-max-brightness-mv` | `int` | ```text Voltage at brightness 100%. If not specified the maximum DAC output voltage is used. ``` |
| `voltage-max-dac-mv` | `int` | ```text The DAC maximum output voltage. Required if voltage-min-brightness-mv or voltage-max-brightness-mv is set. ``` |
| `output-buffer` | `boolean` | ```text Enable the output buffer of the DAC. This is required if it is used to drive an LED directly. ``` |
