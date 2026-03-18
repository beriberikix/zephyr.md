---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/st,stm32-hse-clock.html
original_path: build/dts/api/bindings/clock/st,stm32-hse-clock.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32-hse-clock

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 HSE Clock
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |
| `hse-bypass` | `boolean` | ```text HSE crystal oscillator bypass Set to the property to by-pass the oscillator with an external clock. ``` |
| `css-enabled` | `boolean` | ```text HSE clock security system enabled Set the property to enable the clock security system (CSS) for the HSE clock.  If a failure is detected on the HSE clock, the HSE oscillator is automatically disabled, a clock failure event is sent to timers, and a non-maskable interrupt is generated to inform the software about the failure, allowing the MCU to perform rescue operations. See the MCU reference manual for details.  The interaction of CSS and low-power modes is unclear from the documentation. For at least some devices Zephyr will reconfigure the clocks on resuming from low-power modes; this will include re-enabling CSS. However it is important that you verify this for your own hardware. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-hse-clock” compatible.

(None)
