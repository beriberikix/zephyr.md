---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/input/zephyr,input-sdl-touch.html
original_path: build/dts/api/bindings/input/zephyr,input-sdl-touch.html
---

# zephyr,input-sdl-touch

Vendor: [The Zephyr Project](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[drivers/input/input\_sdl\_touch.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_sdl_touch.c).

## Description

```text
SDL based emulated touch panel
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `display` | `phandle` | ```text Handle to the display that the input events are raised for ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,input-sdl-touch” compatible.

(None)
