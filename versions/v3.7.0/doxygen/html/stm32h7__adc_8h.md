---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32h7__adc_8h.html
original_path: doxygen/html/stm32h7__adc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32h7\_adc.h File Reference

`#include <[zephyr/dt-bindings/adc/stm32_adc.h](stm32__adc_8h_source.md)>`

[Go to the source code of this file.](stm32h7__adc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_ADC\_RES\_REG](#a172393ce17e4f6f94c78b5b171354120)   0x0C |
| #define | [STM32\_ADC\_RES\_SHIFT](#abd31ebaa20fd7e23b81c61926ff9adbe)   2 |
| #define | [STM32\_ADC\_RES\_MASK](#a2a727c7d9a6496b2fdc3da2d24841e3f)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| #define | [STM32H72X\_ADC3\_RES\_SHIFT](#afeb903db1eec808d03ba14e8060ce7d0)   3 |
| #define | [STM32H72X\_ADC3\_RES\_MASK](#a104e74f50efbe65cdf928fe5b5632f06)   0x03 |
| #define | [STM32H72X\_ADC3\_RES](#a793aa061c32da1e0ae76d4869719e3ef)(resolution, reg\_val) |

## Macro Definition Documentation

## [◆ ](#a2a727c7d9a6496b2fdc3da2d24841e3f)STM32\_ADC\_RES\_MASK

| #define STM32\_ADC\_RES\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| --- |

## [◆ ](#a172393ce17e4f6f94c78b5b171354120)STM32\_ADC\_RES\_REG

| #define STM32\_ADC\_RES\_REG   0x0C |
| --- |

## [◆ ](#abd31ebaa20fd7e23b81c61926ff9adbe)STM32\_ADC\_RES\_SHIFT

| #define STM32\_ADC\_RES\_SHIFT   2 |
| --- |

## [◆ ](#a793aa061c32da1e0ae76d4869719e3ef)STM32H72X\_ADC3\_RES

| #define STM32H72X\_ADC3\_RES | ( |  | *resolution*, |
| --- | --- | --- | --- |
|  |  |  | *reg\_val* ) |

**Value:**

[STM32\_ADC](stm32__adc_8h.md#a7ef6d8d5005e78ee779331b13aa80b16)(resolution, reg\_val, [STM32H72X\_ADC3\_RES\_MASK](#a104e74f50efbe65cdf928fe5b5632f06), \

[STM32H72X\_ADC3\_RES\_SHIFT](#afeb903db1eec808d03ba14e8060ce7d0), [STM32\_ADC\_RES\_REG](stm32f1__adc_8h.md#a172393ce17e4f6f94c78b5b171354120))

[STM32\_ADC](stm32__adc_8h.md#a7ef6d8d5005e78ee779331b13aa80b16)

#define STM32\_ADC(real\_val, reg\_val, mask, shift, reg)

STM32 ADC configuration bit field.

**Definition** stm32\_adc.h:37

[STM32\_ADC\_RES\_REG](stm32f1__adc_8h.md#a172393ce17e4f6f94c78b5b171354120)

#define STM32\_ADC\_RES\_REG

**Definition** stm32f1\_adc.h:18

[STM32H72X\_ADC3\_RES\_MASK](#a104e74f50efbe65cdf928fe5b5632f06)

#define STM32H72X\_ADC3\_RES\_MASK

**Definition** stm32h7\_adc.h:21

[STM32H72X\_ADC3\_RES\_SHIFT](#afeb903db1eec808d03ba14e8060ce7d0)

#define STM32H72X\_ADC3\_RES\_SHIFT

**Definition** stm32h7\_adc.h:20

## [◆ ](#a104e74f50efbe65cdf928fe5b5632f06)STM32H72X\_ADC3\_RES\_MASK

| #define STM32H72X\_ADC3\_RES\_MASK   0x03 |
| --- |

## [◆ ](#afeb903db1eec808d03ba14e8060ce7d0)STM32H72X\_ADC3\_RES\_SHIFT

| #define STM32H72X\_ADC3\_RES\_SHIFT   3 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [stm32h7\_adc.h](stm32h7__adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
