---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/fixed-factor-clock.html
original_path: build/dts/api/bindings/clock/fixed-factor-clock.html
---

# fixed-factor-clock

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
Generic fixed factor clock provider
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-div` | `int` | ```text fixed clock divider ``` |
| `clock-mult` | `int` | ```text fixed clock multiplier ``` |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “fixed-factor-clock” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `clocks` | `phandle-array` | ```text input clock source ``` |
