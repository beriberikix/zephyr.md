---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/intel,adsp-shim-clkctl.html
original_path: build/dts/api/bindings/clock/intel,adsp-shim-clkctl.html
---

# intel,adsp-shim-clkctl

Vendor: [Intel Corporation](../../bindings.md#dt-vendor-intel)

## Description

```text
Intel ADSP clock controlling related constants.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `adsp-clkctl-clk-wovcro` | `int` | ```text Index of WOVCRO clock encoding in the encoding array (if wovcro-supported is true). ``` |
| `adsp-clkctl-clk-lpro` | `int` | ```text Index of LPRO clock encoding in the encoding array. ``` |
| `adsp-clkctl-clk-hpro` | `int` | ```text Index of HPRO clock encoding in the encoding array. ``` |
| `adsp-clkctl-clk-ipll` | `int` | ```text Index of ACE integrated PLL clock encoding in the encoding array. ``` |
| `adsp-clkctl-freq-enc` | `array` | ```text Array that encodes what is needed to enable each clock. ```  This property is **required**. |
| `adsp-clkctl-freq-mask` | `array` | ```text Array that encodes needed masks to enable each clock. ``` |
| `adsp-clkctl-freq-default` | `int` | ```text Index for the default clock. ```  This property is **required**. |
| `adsp-clkctl-freq-lowest` | `int` | ```text Index for the lowest frequency clock. ```  This property is **required**. |
| `wovcro-supported` | `boolean` | ```text If WoV clock ring oscillator is supported. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “intel,adsp-shim-clkctl” compatible.

(None)
