---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/silabs,hfxo.html
original_path: build/dts/api/bindings/clock/silabs,hfxo.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# silabs,hfxo

Vendor: [Silicon Laboratories](../../bindings.md#dt-vendor-silabs)

## Description

```text
Generic fixed-rate clock provider
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `ctune` | `int` | ```text Load capacitance configuration ```  This property is **required**. |
| `precision` | `int` | ```text Precision configuration ```  This property is **required**. |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “silabs,hfxo” compatible.

(None)
