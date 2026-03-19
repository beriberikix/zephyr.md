---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/input/zephyr,input-double-tap.html
original_path: build/dts/api/bindings/input/zephyr,input-double-tap.html
---

# zephyr,input-double-tap

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[subsys/input/input\_double\_tap.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/input_double_tap.c).

## Description

```text
Input double tap pseudo-device

Listens for key events as an input and produces key events as output
corresponding to double taps.

Can be optionally be associated to a specific device to listen for events
only from that device.

Example configuration:

#include <zephyr/dt-bindings/input/input-event-codes.h>

double_tap {
        input = <&buttons>;
        compatible = "zephyr,input-double-tap";
        input-codes = <INPUT_KEY_0>, <INPUT_KEY_1>;
        double-tap-codes = <INPUT_KEY_A>, <INPUT_KEY_B>;
        double-tap-delay-ms = <300>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `input` | `phandle` | ```text Input device phandle, if not specified listen for input from all devices. ``` |
| `input-codes` | `array` | ```text Array of input event key codes (INPUT_KEY_* or INPUT_BTN_*). ```  This property is **required**. |
| `double-tap-codes` | `array` | ```text Array of key codes to be generated for double taps (INPUT_KEY_* or INPUT_BTN_*). ```  This property is **required**. |
| `double-tap-delay-ms` | `int` | ```text Maximum time delay between taps to register a double tap, in milliseconds. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,input-double-tap” compatible.

(None)
