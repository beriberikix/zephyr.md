---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/input/zephyr,lvgl-button-input.html
original_path: build/dts/api/bindings/input/zephyr,lvgl-button-input.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,lvgl-button-input

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
LVGL button indev pseudo-device

Listens for button input events and routes the
lv_indev_data_t to the underlying button lv_indev_t managed by LVGL.

Example configuration:

pointer {
        compatible = "zephyr,lvgl-button-input";
        input = <&buttons>;
        input-codes = <INPUT_KEY_0 INPUT_KEY_1>;
        coordinates = <120 220>, <150 250>;
};

When the device receives an input_event with code INPUT_KEY_0
a click event will be performed at (120,220).
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `input-codes` | `array` | ```text Array of input event key codes (INPUT_KEY_* or INPUT_BTN_*). ```  This property is **required**. |
| `coordinates` | `array` | ```text Array of points (x,y) the associated input-code is mapped to. ``` |
| `input` | `phandle` | ```text Input device phandle. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,lvgl-button-input” compatible.

(None)
