---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/espressif-esp32-gpio_8h.html
original_path: doxygen/html/espressif-esp32-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espressif-esp32-gpio.h File Reference

[Go to the source code of this file.](espressif-esp32-gpio_8h_source.md)

| Macros | |
| --- | --- |
| GPIO drive strength flags | |
| The drive strength flags are a Zephyr specific extension of the standard GPIO flags specified by the Linux GPIO binding.  Only applicable for Espressif ESP32 SoCs.  The interface supports two different drive strengths: DFLT - The lowest drive strength supported by the HW ALT - The highest drive strength supported by the HW | |
| #define | [ESP32\_GPIO\_DS\_DFLT](#adbe5a19bf5ce3d57e5e8fe592022cefb)   (0x0U << ESP32\_GPIO\_DS\_POS) |
|  | Default drive strength. |
| #define | [ESP32\_GPIO\_DS\_ALT](#a20175204db3e520b54ceeafb5029db0c)   (0x3U << ESP32\_GPIO\_DS\_POS) |
|  | Alternative drive strength. |
| GPIO pin input/output enable flags | |
| These flags allow configuring a pin as input or output while keeping untouched its complementary configuration.  By instance, if we configure a GPIO pin as an input and pass the flag ESP32\_GPIO\_PIN\_OUT\_EN, the driver will not disable the pin's output buffer. This functionality can be useful to render a pin both an input and output, for diagnose or testing purposes. | |
| #define | [ESP32\_GPIO\_PIN\_OUT\_EN](#a20dcf1a1a0dc4f18fb688a004151556d)   (1 << 12) |
|  | Keep GPIO pin enabled as output. |
| #define | [ESP32\_GPIO\_PIN\_IN\_EN](#ab87f6a0268cf84c10689cff6f0a6af02)   (1 << 13) |
|  | Keep GPIO pin enabled as input. |

## Macro Definition Documentation

## [◆ ](#a20175204db3e520b54ceeafb5029db0c)ESP32\_GPIO\_DS\_ALT

| #define ESP32\_GPIO\_DS\_ALT   (0x3U << ESP32\_GPIO\_DS\_POS) |
| --- |

Alternative drive strength.

## [◆ ](#adbe5a19bf5ce3d57e5e8fe592022cefb)ESP32\_GPIO\_DS\_DFLT

| #define ESP32\_GPIO\_DS\_DFLT   (0x0U << ESP32\_GPIO\_DS\_POS) |
| --- |

Default drive strength.

## [◆ ](#ab87f6a0268cf84c10689cff6f0a6af02)ESP32\_GPIO\_PIN\_IN\_EN

| #define ESP32\_GPIO\_PIN\_IN\_EN   (1 << 13) |
| --- |

Keep GPIO pin enabled as input.

## [◆ ](#a20dcf1a1a0dc4f18fb688a004151556d)ESP32\_GPIO\_PIN\_OUT\_EN

| #define ESP32\_GPIO\_PIN\_OUT\_EN   (1 << 12) |
| --- |

Keep GPIO pin enabled as output.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [espressif-esp32-gpio.h](espressif-esp32-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
