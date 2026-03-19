---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/input/zephyr,lvgl-encoder-input.html
original_path: build/dts/api/bindings/input/zephyr,lvgl-encoder-input.html
---

# zephyr,lvgl-encoder-input

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[modules/lvgl/input/lvgl\_encoder\_input.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/input/lvgl_encoder_input.c).

## Description

```text
LVGL encoder indev pseudo-device

Listens for button/encoder input events and routes the
lv_indev_data_t to the underlying encoder lv_indev_t managed by LVGL.

Example configuration:

encoder {
        compatible = "zephyr,lvgl-encoder-input";
        rotation-input-code = <INPUT_REL_Y>;
        button-input-code = <INPUT_KEY_0>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `rotation-input-code` | `int` | ```text Input event code associated with rotation (INPUT_REL_*). ```  This property is **required**. |
| `button-input-code` | `int` | ```text Input event key code for encoder button (INPUT_KEY_* or INPUT_BTN_*). ``` |
| `input` | `phandle` | ```text Input device phandle. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,lvgl-encoder-input” compatible.

(None)
