---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/input/zephyr,input-longpress.html
original_path: build/dts/api/bindings/input/zephyr,input-longpress.html
---

# zephyr,input-longpress

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[subsys/input/input\_longpress.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/input/input_longpress.c).

## Description

```text
Input longpress pseudo-device

Listens for key events as an input and produces key events as output
corresponding to short and long press.

Can be optionally be associated to a specific device to listen for events
only from that device.

Example configuration:

#include <zephyr/dt-bindings/input/input-event-codes.h>

longpress {
        input = <&buttons>;
        compatible = "zephyr,input-longpress";
        input-codes = <INPUT_KEY_0>, <INPUT_KEY_1>;
        short-codes = <INPUT_KEY_A>, <INPUT_KEY_B>;
        long-codes = <INPUT_KEY_X>, <INPUT_KEY_Y>;
        long-delay-ms = <1000>;
};

Example output:

# short press
input event: dev=buttons          SYN type= 1 code= 11 value=1 # INPUT_KEY_0 press
# release before one second
input event: dev=buttons          SYN type= 1 code= 11 value=0 # INPUT_KEY_0 release
input event: dev=longpress        SYN type= 1 code= 30 value=1 # INPUT_KEY_A press
input event: dev=longpress        SYN type= 1 code= 30 value=0 # INPUT_KEY_A release

# long press
input event: dev=buttons          SYN type= 1 code= 11 value=1 # INPUT_KEY_0 press
# hold for more than one second
input event: dev=longpress        SYN type= 1 code= 45 value=1 # INPUT_KEY_X press
# wait for release
input event: dev=buttons          SYN type= 1 code= 11 value=0 # INPUT_KEY_0 release
input event: dev=longpress        SYN type= 1 code= 45 value=0 # INPUT_KEY_X release
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `input` | `phandle` | ```text Input device phandle, if not specified listen for input from all devices. ``` |
| `input-codes` | `array` | ```text Array of input event key codes (INPUT_KEY_* or INPUT_BTN_*). ```  This property is **required**. |
| `short-codes` | `array` | ```text Optional array of key codes to be generated for short press (INPUT_KEY_* or INPUT_BTN_*). ``` |
| `long-codes` | `array` | ```text Array of key codes to be generated for long press (INPUT_KEY_* or INPUT_BTN_*). ```  This property is **required**. |
| `long-delay-ms` | `int` | ```text Time delay to register a long press in milliseconds. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,input-longpress” compatible.

(None)
