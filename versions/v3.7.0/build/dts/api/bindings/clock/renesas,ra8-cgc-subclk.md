---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/renesas,ra8-cgc-subclk.html
original_path: build/dts/api/bindings/clock/renesas,ra8-cgc-subclk.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# renesas,ra8-cgc-subclk

Vendor: [Renesas Electronics Corporation](../../bindings.md#dt-vendor-renesas)

## Description

```text
Renesas RA8 Sub-Clock
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |
| `drive-capability` | `int` | ```text Sub-Clock Oscillator Drive Capability Switching - 0: Standard (12.5pf) - 1: Lowpower mode 1 (9pf) - 2: Lowpower mode 2 (7pf) - 3: Lowpower mode 3 (4pf) ```  Legal values: `0`, `1`, `2`, `3` |
| `stabilization-time` | `int` | ```text Sub-Clock stabilization time in micro seconds ```  Default value: `1000` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “renesas,ra8-cgc-subclk” compatible.

(None)
