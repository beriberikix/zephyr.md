---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/clock/espressif,esp32-clock.html
original_path: build/dts/api/bindings/clock/espressif,esp32-clock.html
---

# espressif,esp32-clock

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

Note

An implementation of a driver matching this compatible is available in
[drivers/clock\_control/clock\_control\_esp32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_esp32.c).

## Description

```text
ESP32 Clock (Power & Clock Controller Module) Module
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `fast-clk-src` | `int` | ```text RTC fast clock source. - 0: ESP32_RTC_FAST_CLK_SRC_XTAL_D2 - Main XTAL divided by 2 (C3/S3) ESP32_RTC_FAST_CLK_SRC_XTAL_D4 Main XTAL divided by 4 (ESP32/S2) - 1: ESP32_RTC_FAST_CLK_SRC_RC_FAST - 8 MHz ```  This property is **required**.  Legal values: `0`, `1` |
| `slow-clk-src` | `int` | ```text RTC slow clock source. Default to - 0: ESP32_RTC_SLOW_CLK_SRC_RC_SLOW - 136 KHz (C3/S3) - 90 kHz (S2) - 150 kHz (ESP32) - 1: ESP32_RTC_SLOW_CLK_SRC_XTAL32K - 32,768U KHz - 2: ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256 - 17,5 MHz - 9: ESP32_RTC_SLOW_CLK_32K_EXT_OSC - External 32k oscillator connected to 32K_XP pin ```  This property is **required**.  Legal values: `0`, `1`, `2`, `9` |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**.  Constant value: `1` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “espressif,esp32-clock” compatible.

(None)

## Specifier cell names

- clock cells: offset
