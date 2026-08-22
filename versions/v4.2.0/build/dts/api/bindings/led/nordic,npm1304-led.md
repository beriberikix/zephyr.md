---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/led/nordic,npm1304-led.html
original_path: build/dts/api/bindings/led/nordic,npm1304-led.html
---

# nordic,npm1304-led

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

Note

An implementation of a driver matching this compatible is available in
[drivers/led/led\_npm13xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/led_npm13xx.c).

## Description

```text
Nordic nPM1304 LED controller

The nPM1304 has three LED outputs.
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
may apply to the “nordic,npm1304-led” compatible.

(None)
