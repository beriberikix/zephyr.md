---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32__adc_8h_source.html
original_path: doxygen/html/stm32__adc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_adc.h

[Go to the documentation of this file.](stm32__adc_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicrelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32\_ADC\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32\_ADC\_H\_

8

9#include <[zephyr/dt-bindings/adc/adc.h](dt-bindings_2adc_2adc_8h.md)>

10

[ 11](stm32__adc_8h.md#ad474a8b4b178c53a2ab52ef930c3cc17)#define STM32\_ADC\_REG\_MASK BIT\_MASK(8)

[ 12](stm32__adc_8h.md#a10445331738224d612806527c3cebee8)#define STM32\_ADC\_REG\_SHIFT 0U

[ 13](stm32__adc_8h.md#a0320e06eac0586ece090140280800997)#define STM32\_ADC\_SHIFT\_MASK BIT\_MASK(5)

[ 14](stm32__adc_8h.md#a2096ae20f7315d6369bd94fb39bc4e44)#define STM32\_ADC\_SHIFT\_SHIFT 8U

[ 15](stm32__adc_8h.md#a6d3b2a729d45ccf772daa86802a6e4e1)#define STM32\_ADC\_MASK\_MASK BIT\_MASK(3)

[ 16](stm32__adc_8h.md#a908faae004e74ead4a2d7bf45b78afa3)#define STM32\_ADC\_MASK\_SHIFT 13U

[ 17](stm32__adc_8h.md#ae10057d824740b1aba2dc90495d4d0d3)#define STM32\_ADC\_REG\_VAL\_MASK BIT\_MASK(3)

[ 18](stm32__adc_8h.md#a8cc5598e66ddcb8b1b962b01f7dd3de0)#define STM32\_ADC\_REG\_VAL\_SHIFT 16U

[ 19](stm32__adc_8h.md#ac098885afbbe9580ea8e6a2b54137562)#define STM32\_ADC\_REAL\_VAL\_MASK BIT\_MASK(13)

[ 20](stm32__adc_8h.md#a0fc4898cb3164f3cc2d1a80b56d60fe6)#define STM32\_ADC\_REAL\_VAL\_SHIFT 19U

21

[ 37](stm32__adc_8h.md#a7ef6d8d5005e78ee779331b13aa80b16)#define STM32\_ADC(real\_val, reg\_val, mask, shift, reg) \

38 ((((reg) & STM32\_ADC\_REG\_MASK) << STM32\_ADC\_REG\_SHIFT) | \

39 (((shift) & STM32\_ADC\_SHIFT\_MASK) << STM32\_ADC\_SHIFT\_SHIFT) | \

40 (((mask) & STM32\_ADC\_MASK\_MASK) << STM32\_ADC\_MASK\_SHIFT) | \

41 (((reg\_val) & STM32\_ADC\_REG\_VAL\_MASK) << STM32\_ADC\_REG\_VAL\_SHIFT) | \

42 (((real\_val) & STM32\_ADC\_REAL\_VAL\_MASK) << STM32\_ADC\_REAL\_VAL\_SHIFT))

43

[ 44](stm32__adc_8h.md#a745fea8fd34d5eda4235fc9edccb46a8)#define STM32\_ADC\_GET\_REAL\_VAL(val) \

45 (((val) >> STM32\_ADC\_REAL\_VAL\_SHIFT) & STM32\_ADC\_REAL\_VAL\_MASK)

46

[ 47](stm32__adc_8h.md#a9b31049c0085d1de0fe8016f5d1d059a)#define STM32\_ADC\_GET\_REG\_VAL(val) \

48 (((val) >> STM32\_ADC\_REG\_VAL\_SHIFT) & STM32\_ADC\_REG\_VAL\_MASK)

49

[ 50](stm32__adc_8h.md#a05b122d5ee80b69274a2720f98808e05)#define STM32\_ADC\_GET\_MASK(val) \

51 (((val) >> STM32\_ADC\_MASK\_SHIFT) & STM32\_ADC\_MASK\_MASK)

52

[ 53](stm32__adc_8h.md#a60dd5650c381ba06c55ef2dd822f4ff5)#define STM32\_ADC\_GET\_SHIFT(val) \

54 (((val) >> STM32\_ADC\_SHIFT\_SHIFT) & STM32\_ADC\_SHIFT\_MASK)

55

[ 56](stm32__adc_8h.md#a7b4c448188161686213b5082f8f86315)#define STM32\_ADC\_GET\_REG(val) \

57 (((val) >> STM32\_ADC\_REG\_SHIFT) & STM32\_ADC\_REG\_MASK)

58

59/\*

60 \* Macro used to store resolution info. STM32\_ADC\_RES\_\* macros are defined in

61 \* respective stm32xx\_adc.h files

62 \*/

[ 63](stm32__adc_8h.md#ac0daa8666c342a0a4326ec6687dda1b2)#define STM32\_ADC\_RES(resolution, reg\_val) \

64 STM32\_ADC(resolution, reg\_val, STM32\_ADC\_RES\_MASK, STM32\_ADC\_RES\_SHIFT, \

65 STM32\_ADC\_RES\_REG)

66

[ 73](stm32__adc_8h.md#a9ac82e856c7683e23553431e5224d5f4)#define SYNC 1

[ 74](stm32__adc_8h.md#ad28b60868b6548c43e7a18f30c9b2022)#define ASYNC 2

76

[ 83](stm32__adc_8h.md#aa71f98fedb3bb493be5ce344ebdd1291)#define NOT\_FULLY\_CONFIGURABLE 0

[ 84](stm32__adc_8h.md#a015cc7f08a85f7dd01f817ac77fa7eb8)#define FULLY\_CONFIGURABLE 1

86

87#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32\_ADC\_H\_ \*/

[adc.h](dt-bindings_2adc_2adc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [stm32\_adc.h](stm32__adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
