---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/clock/st,stm32n6-ic-clock-mux.html
original_path: build/dts/api/bindings/clock/st,stm32n6-ic-clock-mux.html
---

# st,stm32n6-ic-clock-mux

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32N6 Divider IC multiplexer.

This node selects a clock input and a divider.

For instance:
  &ic6 {
    pll-src = <2>;
    div = <16>;
    status = "okay";
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pll-src` | `int` | ```text PLL clock source ```  This property is **required**.  Legal values: `1`, `2`, `3`, `4` |
| `ic-div` | `int` | ```text ICx integer division factor The input ICx frequency is divided by the specified value Valid range: 1 - 256 ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32n6-ic-clock-mux” compatible.

(None)
