---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/usb/uac2/zephyr,uac2.html
original_path: build/dts/api/bindings/usb/uac2/zephyr,uac2.html
---

# zephyr,uac2

Vendor: [Zephyr-specific binding](../../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[subsys/usb/device\_next/class/usbd\_uac2.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/device_next/class/usbd_uac2.c).

## Description

```text
USB Audio Class 2 instance
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `full-speed` | `boolean` | ```text True if this instance is allowed to operate at Full-Speed. ``` |
| `high-speed` | `boolean` | ```text True if this instance is allowed to operate at High-Speed. ``` |
| `audio-function` | `int` | ```text Constant, indicating the primary use of this audio function, as intended by the manufacturer. Use Audio Function category codes define from dt-bindings/usb/audio.h. ```  This property is **required**. |
| `interrupt-endpoint` | `boolean` | ```text Enable to support an optional interrupt endpoint to inform the Host about dynamic changes that occur on the different addressable entities. ``` |
| `latency-control` | `string` | ```text Latency Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,uac2” compatible.

(None)
