---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32__pwm_8h.html
original_path: doxygen/html/stm32__pwm_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_pwm.h File Reference

[Go to the source code of this file.](stm32__pwm_8h_source.md)

| Macros | |
| --- | --- |
| custom PWM complementary flags for output pins | |
| This flag can be used with any of the pwm\_pin\_set\_\* API calls to indicate that the PWM signal has to be routed to the complementary output channel.  This feature is only available on certain SoC families, refer to the binding's documentation for more details. The custom flags are on the upper 8bits of the [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0 "Provides a type to hold PWM configuration flags.") | |
| #define | [STM32\_PWM\_COMPLEMENTARY](#a8e4959803792254f90bb31e0454a4249)   (1U << 8) |
|  | PWM complementary output pin is enabled. |
| #define | [PWM\_STM32\_COMPLEMENTARY](#ac73e020f7f8787beaa8ddf7871578c6f)   (1U << 8) |

## Macro Definition Documentation

## [◆ ](#ac73e020f7f8787beaa8ddf7871578c6f)PWM\_STM32\_COMPLEMENTARY

| #define PWM\_STM32\_COMPLEMENTARY   (1U << 8) |
| --- |

**[Deprecated](deprecated.md#_deprecated000008)**
:   Use the PWM complementary [STM32\_PWM\_COMPLEMENTARY](#a8e4959803792254f90bb31e0454a4249) flag instead.

## [◆ ](#a8e4959803792254f90bb31e0454a4249)STM32\_PWM\_COMPLEMENTARY

| #define STM32\_PWM\_COMPLEMENTARY   (1U << 8) |
| --- |

PWM complementary output pin is enabled.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pwm](dir_ff747911c88ea6a5644735057b122c0d.md)
- [stm32\_pwm.h](stm32__pwm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
