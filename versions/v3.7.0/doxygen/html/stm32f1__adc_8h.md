---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32f1__adc_8h.html
original_path: doxygen/html/stm32f1__adc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f1\_adc.h File Reference

`#include <[zephyr/dt-bindings/adc/stm32_adc.h](stm32__adc_8h_source.md)>`

[Go to the source code of this file.](stm32f1__adc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_ADC\_RES\_REG](#a172393ce17e4f6f94c78b5b171354120)   0xFF |
| #define | [STM32\_ADC\_RES\_SHIFT](#abd31ebaa20fd7e23b81c61926ff9adbe)   0 |
| #define | [STM32\_ADC\_RES\_MASK](#a2a727c7d9a6496b2fdc3da2d24841e3f)   0x00 |
| #define | [STM32\_ADC\_RES\_REG\_VAL](#a2a1f597025647c8f33b562804ce9e312)   0x00 |
| #define | [STM32F1\_ADC\_RES](#ad4bec6dade85253c3ea3152f87786471)(resolution) |

## Macro Definition Documentation

## [◆ ](#a2a727c7d9a6496b2fdc3da2d24841e3f)STM32\_ADC\_RES\_MASK

| #define STM32\_ADC\_RES\_MASK   0x00 |
| --- |

## [◆ ](#a172393ce17e4f6f94c78b5b171354120)STM32\_ADC\_RES\_REG

| #define STM32\_ADC\_RES\_REG   0xFF |
| --- |

## [◆ ](#a2a1f597025647c8f33b562804ce9e312)STM32\_ADC\_RES\_REG\_VAL

| #define STM32\_ADC\_RES\_REG\_VAL   0x00 |
| --- |

## [◆ ](#abd31ebaa20fd7e23b81c61926ff9adbe)STM32\_ADC\_RES\_SHIFT

| #define STM32\_ADC\_RES\_SHIFT   0 |
| --- |

## [◆ ](#ad4bec6dade85253c3ea3152f87786471)STM32F1\_ADC\_RES

| #define STM32F1\_ADC\_RES | ( |  | *resolution* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_ADC\_RES](stm32__adc_8h.md#ac0daa8666c342a0a4326ec6687dda1b2)(resolution, [STM32\_ADC\_RES\_REG\_VAL](#a2a1f597025647c8f33b562804ce9e312))

[STM32\_ADC\_RES](stm32__adc_8h.md#ac0daa8666c342a0a4326ec6687dda1b2)

#define STM32\_ADC\_RES(resolution, reg\_val)

**Definition** stm32\_adc.h:63

[STM32\_ADC\_RES\_REG\_VAL](#a2a1f597025647c8f33b562804ce9e312)

#define STM32\_ADC\_RES\_REG\_VAL

**Definition** stm32f1\_adc.h:21

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [stm32f1\_adc.h](stm32f1__adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
