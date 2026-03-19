---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/mediatek,mt8195_cpuclk.html
original_path: build/dts/api/bindings/clock/mediatek,mt8195_cpuclk.html
---

# mediatek,mt8195\_cpuclk

Vendor: [MediaTek Inc.](../../bindings.md#dt-vendor-mediatek)

## Description

```text
MediaTek Audio DSP CPU Frequency Control
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `freqs_mhz` | `array` | ```text Available frequencies in ascending order ```  This property is **required**. |
| `cg_reg` | `int` |  |
| `pll_ctrl_reg` | `int` |  |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “mediatek,mt8195\_cpuclk” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
