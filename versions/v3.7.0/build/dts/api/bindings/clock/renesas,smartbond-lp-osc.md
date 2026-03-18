---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/renesas,smartbond-lp-osc.html
original_path: build/dts/api/bindings/clock/renesas,smartbond-lp-osc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# renesas,smartbond-lp-osc

Vendor: [Renesas Electronics Corporation](../../bindings.md#dt-vendor-renesas)

## Description

```text
Smartbond low power oscillator
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |
| `settle-time` | `int` | ```text This is only valid for XTAL32K. Time in ms needed to XTAL32K to settle. ```  Default value: `8000` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “renesas,smartbond-lp-osc” compatible.

(None)
