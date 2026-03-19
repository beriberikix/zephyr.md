---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/usb/uac2/zephyr,uac2-feature-unit.html
original_path: build/dts/api/bindings/usb/uac2/zephyr,uac2-feature-unit.html
---

# zephyr,uac2-feature-unit

Vendor: [Zephyr-specific binding](../../../bindings.md#dt-vendor-zephyr)

## Description

```text
USB Audio Class 2 Feature Unit entity
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `data-source` | `phandle` | ```text Unit or Terminal to which this Feature Unit is connected ``` |
| `mute-control` | `string-array` | ```text Mute Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `volume-control` | `string-array` | ```text Volume Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `bass-control` | `string-array` | ```text Bass Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `mid-control` | `string-array` | ```text Mid Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `treble-control` | `string-array` | ```text Treble Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `graphic-equalizer-control` | `string-array` | ```text Graphic Equalizer capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `automatic-gain-control` | `string-array` | ```text Automatic Gain Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `delay-control` | `string-array` | ```text Delay Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `bass-boost-control` | `string-array` | ```text Bass Boost Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `loundness-control` | `string-array` | ```text Loundness Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `input-gain-control` | `string-array` | ```text Input Gain Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `input-gain-pad-control` | `string-array` | ```text Input Gain Pad Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `phase-inverter-control` | `string-array` | ```text Phase Inverter Control capabilities ```  Legal values: `'read-only'`, `'host-programmable'`, `'not-present'` |
| `underflow-control` | `string-array` | ```text Underflow Control capabilities ```  Legal values: `'read-only'`, `'not-present'` |
| `overflow-control` | `string-array` | ```text Overflow Control capabilities ```  Legal values: `'read-only'`, `'not-present'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,uac2-feature-unit” compatible.

(None)
