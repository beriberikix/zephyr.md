---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/input/zephyr,lvgl-keypad-input.html
original_path: build/dts/api/bindings/input/zephyr,lvgl-keypad-input.html
---

# zephyr,lvgl-keypad-input

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[modules/lvgl/input/lvgl\_keypad\_input.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/input/lvgl_keypad_input.c).

## Description

```text
LVGL keypad indev pseudo-device

Listens for input events and routes the
lv_indev_data_t to the underlying keypad lv_indev_t managed by LVGL.

The property input-codes can be used to setup a mapping of input codes
to the lvgl keys. There are lvgl keys that have a special function:
https://docs.lvgl.io/master/overview/indev.html#keys.

The pseudo device can be associated to a specific device to listen only
for events from that device. Example configuration:

#include <zephyr/dt-bindings/lvgl/lvgl.h>

keypad {
        compatible = "zephyr,lvgl-keypad-input";
        input = <&buttons>;
        input-codes = <INPUT_KEY_1 INPUT_KEY_2>;
        lvgl-codes = <LV_KEY_NEXT LV_KEY_PREV>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `input-codes` | `array` | ```text Array of input event key codes (INPUT_KEY_* or INPUT_BTN_*). ```  This property is **required**. |
| `lvgl-codes` | `array` | ```text Array of mapped lvgl keys. ```  This property is **required**. |
| `input` | `phandle` | ```text Input device phandle. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,lvgl-keypad-input” compatible.

(None)
