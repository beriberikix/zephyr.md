---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/st,stm32wl-hse-clock.html
original_path: build/dts/api/bindings/clock/st,stm32wl-hse-clock.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32wl-hse-clock

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32WL HSE Clock
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |
| `hse-tcxo` | `boolean` | ```text When set, TCXO is selected as external source clock for HSE. Otherwise, external crystal is selected as HSE source clock. ``` |
| `hse-div2` | `boolean` | ```text When set HSE output clock is divided by 2. Otherwise, no prescaler is used. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32wl-hse-clock” compatible.

(None)
