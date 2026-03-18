---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/usb/uac2/zephyr,uac2-clock-source.html
original_path: build/dts/api/bindings/usb/uac2/zephyr,uac2-clock-source.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,uac2-clock-source

Vendor: [Zephyr-specific binding](../../../bindings.md#dt-vendor-zephyr)

## Description

```text
USB Audio Class 2 Clock Source entity
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-type` | `string` | ```text Clock Type indicating whether the Clock Source represents an external clock or an internal clock with either fixed frequency, variable frequency, or programmable frequency. ```  This property is **required**.  Legal values: `'external'`, `'internal-fixed'`, `'internal-variable'`, `'internal-programmable'` |
| `sof-synchronized` | `boolean` | ```text True if clock is synchronized to USB Start of Frame. False if clock is free running. External clock must be free running. ``` |
| `frequency-control` | `string` | ```text Clock Frequency Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'` |
| `validity-control` | `string` | ```text Clock Validity Control capabilities ```  Legal values: `'read-only'` |
| `assoc-terminal` | `phandle` | ```text Input or Output Terminal associated with this Clock Source. Set if clock is derived from USB OUT data endpoint (point the handle to respective Input Terminal) or from input signal on S/PDIF connector. ``` |
| `sampling-frequencies` | `array` | ```text Sampling Frequencies, in Hz, this Clock Source Entity can generate. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,uac2-clock-source” compatible.

(None)
