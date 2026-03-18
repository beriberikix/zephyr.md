---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/led/nordic,npm1300-led.html
original_path: build/dts/api/bindings/led/nordic,npm1300-led.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nordic,npm1300-led

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic nPM1300 LED controller

The nPM1300 has three LED outputs.
Each LED can automatically display error or charging status,
or be controlled by software.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `nordic,led0-mode` | `string` | ```text LED 0 mode ```  This property is **required**.  Legal values: `'error'`, `'charging'`, `'host'` |
| `nordic,led1-mode` | `string` | ```text LED 1 mode ```  This property is **required**.  Legal values: `'error'`, `'charging'`, `'host'` |
| `nordic,led2-mode` | `string` | ```text LED 2 mode ```  This property is **required**.  Legal values: `'error'`, `'charging'`, `'host'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,npm1300-led” compatible.

(None)
