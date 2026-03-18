---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/usb/uac2/zephyr,uac2-audio-streaming.html
original_path: build/dts/api/bindings/usb/uac2/zephyr,uac2-audio-streaming.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,uac2-audio-streaming

Vendor: [Zephyr-specific binding](../../../bindings.md#dt-vendor-zephyr)

## Description

```text
USB Audio Class 2 Audio Streaming interface
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `linked-terminal` | `phandle` | ```text Input or Output Terminal to which this interface is connected. ```  This property is **required**. |
| `active-alternate-setting-control` | `string` | ```text Active Alternate Setting Control capabilities ```  Legal values: `'read-only'` |
| `valid-alternate-settings-control` | `string` | ```text Valid Alternate Settings Control capabilities ```  Legal values: `'read-only'` |
| `external-interface` | `boolean` | ```text Enable if audio stream is not transmitted over USB (Type IV Audio Stream). ``` |
| `implicit-feedback` | `boolean` | ```text Enable implicit feedback on asynchronous endpoint. For IN endpoints this sets endpoint behaviour type to implicit feedback data endpoint. For OUT endpoints setting this property removes explicit feedback endpoint. ``` |
| `pitch-control` | `string` | ```text Pitch Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'` |
| `data-overrun-control` | `string` | ```text Data Overrun capabilities ```  Legal values: `'read-only'` |
| `data-underrun-control` | `string` | ```text Data Underrun capabilities ```  Legal values: `'read-only'` |
| `lock-delay` | `int` | ```text Time it takes this endpoint to reliably lock its internal clock recovery circuitry. Units depend on the lock-delay-units field. Relevant only if linked-terminal's clock is sof-synchronized. ``` |
| `lock-delay-units` | `string` | ```text Units for lock-delay parameter. ```  Legal values: `'milliseconds'`, `'decoded-pcm-samples'` |
| `subslot-size` | `int` | ```text Number of bytes occupied by one audio subslot. Can be 1, 2, 3 or 4. ``` |
| `bit-resolution` | `int` | ```text Number of effectively used bits in audio subslot. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,uac2-audio-streaming” compatible.

(None)
