---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/led/x-powers,axp192-led.html
original_path: build/dts/api/bindings/led/x-powers,axp192-led.html
---

# x-powers,axp192-led (on axp192 bus)

Vendor: [X-Powers](../../bindings.md#dt-vendor-x-powers)

## Description

```text
AXP192 LED controller

The AXP192 has one LED can automatically display error or charging status,
or be controlled by software.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `x-powers,mode` | `string` | ```text Select the LED control method. If you select "by-reg", you can control it from software. Please refer to the datasheet for details on "by-charge". ```  Legal values: `'by-reg'`, `'by-charge'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “x-powers,axp192-led” compatible.

(None)
