---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/st,stm32c0-hsi-clock.html
original_path: build/dts/api/bindings/clock/st,stm32c0-hsi-clock.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32c0-hsi-clock

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 HSI Clock node description for STM32C0 devices
On STM32C0, HSI is a 48MHz fixed clock.

It also produces a HSISYS secondary clk which can be used as system clock
source. In that case, a HSI divisor (ranges from 1 to 128) can be applied:
SYSCLK = HSI48 / HSI DIV
      enum:
      - 1 ==> HSISYS = 48MHZ
      - 2 ==> HSISYS = 24MHZ
      - 4 ==> HSISYS = 12MHZ
      - 8 ==> HSISYS = 6MHZ
      - 16 ==> HSISYS = 3MHZ
      - 32 ==> HSISYS = 1.5MHz
      - 64 ==> HSISYS = 0.75MHZ
      - 128 ==> HSISYS = 0.375MHz
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |
| `hsi-div` | `int` | ```text HSI clock divider. Configures the output HSI clock frequency (HSISYS). ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32c0-hsi-clock” compatible.

(None)
