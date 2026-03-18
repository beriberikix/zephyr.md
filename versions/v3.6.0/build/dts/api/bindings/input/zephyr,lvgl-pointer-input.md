---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/input/zephyr,lvgl-pointer-input.html
original_path: build/dts/api/bindings/input/zephyr,lvgl-pointer-input.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,lvgl-pointer-input

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
LVGL pointer indev pseudo-device

Listens for touch input events and routes the
lv_indev_data_t to the underlying pointer lv_indev_t managed by LVGL.

Needs to be associated to a specific device to listen for events
from that device. Example configuration:

pointer {
        compatible = "zephyr,lvgl-pointer-input";
        input = <&input_sdl_touch>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `swap-xy` | `boolean` | ```text Swap x-y axes to align input with the display. ``` |
| `invert-x` | `boolean` | ```text Invert x axes to align input with the display. ``` |
| `invert-y` | `boolean` | ```text Invert y axes to align input with the display. ``` |
| `input` | `phandle` | ```text Input device phandle. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,lvgl-pointer-input” compatible.

(None)
