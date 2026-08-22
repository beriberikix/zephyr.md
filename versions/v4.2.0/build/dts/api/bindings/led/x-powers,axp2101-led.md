---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/led/x-powers,axp2101-led.html
original_path: build/dts/api/bindings/led/x-powers,axp2101-led.html
---

# x-powers,axp2101-led (on axp2101 bus)

Vendor: [X-Powers](../../bindings.md#dt-vendor-x-powers)

## Description

```text
AXP2101 LED controller

The AXP2101 has one LED can automatically display error or charging status,
or be controlled by software.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `x-powers,mode` | `string` | ```text Select the LED control method. If you select "by-reg", you can control it from software. Please refer to the datasheet for details on "type-a" and "type-b". ```  Legal values: `'type-a'`, `'type-b'`, `'by-reg'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “x-powers,axp2101-led” compatible.

(None)
