---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/usb/uac2/zephyr,uac2.html
original_path: build/dts/api/bindings/usb/uac2/zephyr,uac2.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,uac2

Vendor: [Zephyr-specific binding](../../../bindings.md#dt-vendor-zephyr)

## Description

```text
USB Audio Class 2 instance
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `audio-function` | `int` | ```text Constant, indicating the primary use of this audio function, as intended by the manufacturer. Use Audio Function category codes define from dt-bindings/usb/audio.h. ```  This property is **required**. |
| `interrupt-endpoint` | `boolean` | ```text Enable to support an optional interrupt endpoint to inform the Host about dynamic changes that occur on the different addressable entities. ``` |
| `latency-control` | `string` | ```text Latency Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,uac2” compatible.

(None)
