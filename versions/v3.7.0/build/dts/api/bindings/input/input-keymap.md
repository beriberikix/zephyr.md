---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/input/input-keymap.html
original_path: build/dts/api/bindings/input/input-keymap.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# input-keymap

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
Row-column to key mapper

Listens for row-column events from the parent device and reports key events.

Example configuration:

#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <zephyr/dt-bindings/input/keymap.h>

kbd {
    ...
    keymap {
        compatible = "input-keymap";
        keymap = <
            MATRIX_KEY(0, 0, INPUT_KEY_1)
            MATRIX_KEY(0, 1, INPUT_KEY_2)
            MATRIX_KEY(0, 2, INPUT_KEY_3)
            MATRIX_KEY(1, 0, INPUT_KEY_4)
            MATRIX_KEY(1, 1, INPUT_KEY_5)
            MATRIX_KEY(1, 2, INPUT_KEY_6)
            MATRIX_KEY(2, 0, INPUT_KEY_7)
            MATRIX_KEY(2, 1, INPUT_KEY_8)
            MATRIX_KEY(2, 2, INPUT_KEY_9)
        >;
        row-size = <3>;
        col-size = <3>;
    };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `keymap` | `array` | ```text List of codes, using the MATRIX_KEY() macro. ```  This property is **required**. |
| `row-size` | `int` | ```text The number of rows in the keymap. ```  This property is **required**. |
| `col-size` | `int` | ```text The number of columns in the keymap. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “input-keymap” compatible.

(None)
