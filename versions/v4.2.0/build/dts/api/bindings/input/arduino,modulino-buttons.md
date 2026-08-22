---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/input/arduino,modulino-buttons.html
original_path: build/dts/api/bindings/input/arduino,modulino-buttons.html
---

# arduino,modulino-buttons

Vendor: [Arduino](../../bindings.md#dt-vendor-arduino)

Note

An implementation of a driver matching this compatible is available in
[drivers/input/input\_modulino\_buttons.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_modulino_buttons.c).

## Description

```text
Arduino Modulino buttons
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `zephyr,codes` | `array` | ```text Key codes to emit, the module has three buttons so this must specify three key codes. ```  This property is **required**. |
| `poll-period-ms` | `int` | ```text How often to poll the buttons over the i2c bus, defaults to 50ms. ```  Default value: `50` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “arduino,modulino-buttons” compatible.

(None)
