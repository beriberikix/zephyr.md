---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/st,stm32-lse-clock.html
original_path: build/dts/api/bindings/clock/st,stm32-lse-clock.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32-lse-clock

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 LSE Clock
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |
| `driving-capability` | `int` | ```text LSE driving capability, within the range 0 to 3. 0 represents the lowests driving capability, 3 the highest. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `lse-bypass` | `boolean` | ```text LSE crystal oscillator bypass Set the property to by-pass the oscillator with an external clock. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-lse-clock” compatible.

(None)
