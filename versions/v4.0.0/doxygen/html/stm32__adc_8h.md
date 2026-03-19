---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32__adc_8h.html
original_path: doxygen/html/stm32__adc_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_adc.h File Reference

`#include <[zephyr/dt-bindings/adc/adc.h](dt-bindings_2adc_2adc_8h_source.md)>`

[Go to the source code of this file.](stm32__adc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_ADC\_REG\_MASK](#ad474a8b4b178c53a2ab52ef930c3cc17)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(8) |
| #define | [STM32\_ADC\_REG\_SHIFT](#a10445331738224d612806527c3cebee8)   0U |
| #define | [STM32\_ADC\_SHIFT\_MASK](#a0320e06eac0586ece090140280800997)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5) |
| #define | [STM32\_ADC\_SHIFT\_SHIFT](#a2096ae20f7315d6369bd94fb39bc4e44)   8U |
| #define | [STM32\_ADC\_MASK\_MASK](#a6d3b2a729d45ccf772daa86802a6e4e1)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| #define | [STM32\_ADC\_MASK\_SHIFT](#a908faae004e74ead4a2d7bf45b78afa3)   13U |
| #define | [STM32\_ADC\_REG\_VAL\_MASK](#ae10057d824740b1aba2dc90495d4d0d3)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| #define | [STM32\_ADC\_REG\_VAL\_SHIFT](#a8cc5598e66ddcb8b1b962b01f7dd3de0)   16U |
| #define | [STM32\_ADC\_REAL\_VAL\_MASK](#ac098885afbbe9580ea8e6a2b54137562)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(13) |
| #define | [STM32\_ADC\_REAL\_VAL\_SHIFT](#a0fc4898cb3164f3cc2d1a80b56d60fe6)   19U |
| #define | [STM32\_ADC](#a7ef6d8d5005e78ee779331b13aa80b16)(real\_val, reg\_val, mask, shift, reg) |
|  | STM32 ADC configuration bit field. |
| #define | [STM32\_ADC\_GET\_REAL\_VAL](#a745fea8fd34d5eda4235fc9edccb46a8)(val) |
| #define | [STM32\_ADC\_GET\_REG\_VAL](#a9b31049c0085d1de0fe8016f5d1d059a)(val) |
| #define | [STM32\_ADC\_GET\_MASK](#a05b122d5ee80b69274a2720f98808e05)(val) |
| #define | [STM32\_ADC\_GET\_SHIFT](#a60dd5650c381ba06c55ef2dd822f4ff5)(val) |
| #define | [STM32\_ADC\_GET\_REG](#a7b4c448188161686213b5082f8f86315)(val) |
| #define | [STM32\_ADC\_RES](#ac0daa8666c342a0a4326ec6687dda1b2)(resolution, reg\_val) |
| STM32 ADC clock source | |
| This value is to set <st,adc-clock-source> One or both values may not apply to all series.  Refer to the RefMan | |
| #define | [SYNC](#a9ac82e856c7683e23553431e5224d5f4)   1 |
| #define | [ASYNC](#ad28b60868b6548c43e7a18f30c9b2022)   2 |
| STM32 ADC sequencer type | |
| This value is to set <st,adc-sequencer> One or both values may not apply to all series.  Refer to the RefMan | |
| #define | [NOT\_FULLY\_CONFIGURABLE](#aa71f98fedb3bb493be5ce344ebdd1291)   0 |
| #define | [FULLY\_CONFIGURABLE](#a015cc7f08a85f7dd01f817ac77fa7eb8)   1 |

## Macro Definition Documentation

## [◆ ](#ad28b60868b6548c43e7a18f30c9b2022)ASYNC

| #define ASYNC   2 |
| --- |

## [◆ ](#a015cc7f08a85f7dd01f817ac77fa7eb8)FULLY\_CONFIGURABLE

| #define FULLY\_CONFIGURABLE   1 |
| --- |

## [◆ ](#aa71f98fedb3bb493be5ce344ebdd1291)NOT\_FULLY\_CONFIGURABLE

| #define NOT\_FULLY\_CONFIGURABLE   0 |
| --- |

## [◆ ](#a7ef6d8d5005e78ee779331b13aa80b16)STM32\_ADC

| #define STM32\_ADC | ( |  | *real\_val*, |
| --- | --- | --- | --- |
|  |  |  | *reg\_val*, |
|  |  |  | *mask*, |
|  |  |  | *shift*, |
|  |  |  | *reg* ) |

**Value:**

((((reg) & [STM32\_ADC\_REG\_MASK](#ad474a8b4b178c53a2ab52ef930c3cc17)) << [STM32\_ADC\_REG\_SHIFT](#a10445331738224d612806527c3cebee8)) | \

(((shift) & [STM32\_ADC\_SHIFT\_MASK](#a0320e06eac0586ece090140280800997)) << [STM32\_ADC\_SHIFT\_SHIFT](#a2096ae20f7315d6369bd94fb39bc4e44)) | \

(((mask) & [STM32\_ADC\_MASK\_MASK](#a6d3b2a729d45ccf772daa86802a6e4e1)) << [STM32\_ADC\_MASK\_SHIFT](#a908faae004e74ead4a2d7bf45b78afa3)) | \

(((reg\_val) & [STM32\_ADC\_REG\_VAL\_MASK](#ae10057d824740b1aba2dc90495d4d0d3)) << [STM32\_ADC\_REG\_VAL\_SHIFT](#a8cc5598e66ddcb8b1b962b01f7dd3de0)) | \

(((real\_val) & [STM32\_ADC\_REAL\_VAL\_MASK](#ac098885afbbe9580ea8e6a2b54137562)) << [STM32\_ADC\_REAL\_VAL\_SHIFT](#a0fc4898cb3164f3cc2d1a80b56d60fe6)))

[STM32\_ADC\_SHIFT\_MASK](#a0320e06eac0586ece090140280800997)

#define STM32\_ADC\_SHIFT\_MASK

**Definition** stm32\_adc.h:13

[STM32\_ADC\_REAL\_VAL\_SHIFT](#a0fc4898cb3164f3cc2d1a80b56d60fe6)

#define STM32\_ADC\_REAL\_VAL\_SHIFT

**Definition** stm32\_adc.h:20

[STM32\_ADC\_REG\_SHIFT](#a10445331738224d612806527c3cebee8)

#define STM32\_ADC\_REG\_SHIFT

**Definition** stm32\_adc.h:12

[STM32\_ADC\_SHIFT\_SHIFT](#a2096ae20f7315d6369bd94fb39bc4e44)

#define STM32\_ADC\_SHIFT\_SHIFT

**Definition** stm32\_adc.h:14

[STM32\_ADC\_MASK\_MASK](#a6d3b2a729d45ccf772daa86802a6e4e1)

#define STM32\_ADC\_MASK\_MASK

**Definition** stm32\_adc.h:15

[STM32\_ADC\_REG\_VAL\_SHIFT](#a8cc5598e66ddcb8b1b962b01f7dd3de0)

#define STM32\_ADC\_REG\_VAL\_SHIFT

**Definition** stm32\_adc.h:18

[STM32\_ADC\_MASK\_SHIFT](#a908faae004e74ead4a2d7bf45b78afa3)

#define STM32\_ADC\_MASK\_SHIFT

**Definition** stm32\_adc.h:16

[STM32\_ADC\_REAL\_VAL\_MASK](#ac098885afbbe9580ea8e6a2b54137562)

#define STM32\_ADC\_REAL\_VAL\_MASK

**Definition** stm32\_adc.h:19

[STM32\_ADC\_REG\_MASK](#ad474a8b4b178c53a2ab52ef930c3cc17)

#define STM32\_ADC\_REG\_MASK

**Definition** stm32\_adc.h:11

[STM32\_ADC\_REG\_VAL\_MASK](#ae10057d824740b1aba2dc90495d4d0d3)

#define STM32\_ADC\_REG\_VAL\_MASK

**Definition** stm32\_adc.h:17

STM32 ADC configuration bit field.

- reg (0..0xFF) [ 0 : 7 ]
- shift (0..31) [ 8 : 12 ]
- mask (0x1, 0x3, 0x7) [ 13 : 15 ]
- reg\_val (0..7) [ 16 : 18 ]
- real\_val (0..8191) [ 19 : 31 ]

Parameters
:   | reg | ADC\_x register offset |
    | --- | --- |
    | shift | Position within ADC\_x. |
    | mask | Mask for the ADC\_x field. |
    | reg\_val | Register value (0, 1, ... 7). |
    | real\_val | Real corresponding value (0, 1, ... 8191). |

## [◆ ](#a05b122d5ee80b69274a2720f98808e05)STM32\_ADC\_GET\_MASK

| #define STM32\_ADC\_GET\_MASK | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((val) >> [STM32\_ADC\_MASK\_SHIFT](#a908faae004e74ead4a2d7bf45b78afa3)) & [STM32\_ADC\_MASK\_MASK](#a6d3b2a729d45ccf772daa86802a6e4e1))

## [◆ ](#a745fea8fd34d5eda4235fc9edccb46a8)STM32\_ADC\_GET\_REAL\_VAL

| #define STM32\_ADC\_GET\_REAL\_VAL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((val) >> [STM32\_ADC\_REAL\_VAL\_SHIFT](#a0fc4898cb3164f3cc2d1a80b56d60fe6)) & [STM32\_ADC\_REAL\_VAL\_MASK](#ac098885afbbe9580ea8e6a2b54137562))

## [◆ ](#a7b4c448188161686213b5082f8f86315)STM32\_ADC\_GET\_REG

| #define STM32\_ADC\_GET\_REG | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((val) >> [STM32\_ADC\_REG\_SHIFT](#a10445331738224d612806527c3cebee8)) & [STM32\_ADC\_REG\_MASK](#ad474a8b4b178c53a2ab52ef930c3cc17))

## [◆ ](#a9b31049c0085d1de0fe8016f5d1d059a)STM32\_ADC\_GET\_REG\_VAL

| #define STM32\_ADC\_GET\_REG\_VAL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((val) >> [STM32\_ADC\_REG\_VAL\_SHIFT](#a8cc5598e66ddcb8b1b962b01f7dd3de0)) & [STM32\_ADC\_REG\_VAL\_MASK](#ae10057d824740b1aba2dc90495d4d0d3))

## [◆ ](#a60dd5650c381ba06c55ef2dd822f4ff5)STM32\_ADC\_GET\_SHIFT

| #define STM32\_ADC\_GET\_SHIFT | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((val) >> [STM32\_ADC\_SHIFT\_SHIFT](#a2096ae20f7315d6369bd94fb39bc4e44)) & [STM32\_ADC\_SHIFT\_MASK](#a0320e06eac0586ece090140280800997))

## [◆ ](#a6d3b2a729d45ccf772daa86802a6e4e1)STM32\_ADC\_MASK\_MASK

| #define STM32\_ADC\_MASK\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| --- |

## [◆ ](#a908faae004e74ead4a2d7bf45b78afa3)STM32\_ADC\_MASK\_SHIFT

| #define STM32\_ADC\_MASK\_SHIFT   13U |
| --- |

## [◆ ](#ac098885afbbe9580ea8e6a2b54137562)STM32\_ADC\_REAL\_VAL\_MASK

| #define STM32\_ADC\_REAL\_VAL\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(13) |
| --- |

## [◆ ](#a0fc4898cb3164f3cc2d1a80b56d60fe6)STM32\_ADC\_REAL\_VAL\_SHIFT

| #define STM32\_ADC\_REAL\_VAL\_SHIFT   19U |
| --- |

## [◆ ](#ad474a8b4b178c53a2ab52ef930c3cc17)STM32\_ADC\_REG\_MASK

| #define STM32\_ADC\_REG\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(8) |
| --- |

## [◆ ](#a10445331738224d612806527c3cebee8)STM32\_ADC\_REG\_SHIFT

| #define STM32\_ADC\_REG\_SHIFT   0U |
| --- |

## [◆ ](#ae10057d824740b1aba2dc90495d4d0d3)STM32\_ADC\_REG\_VAL\_MASK

| #define STM32\_ADC\_REG\_VAL\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| --- |

## [◆ ](#a8cc5598e66ddcb8b1b962b01f7dd3de0)STM32\_ADC\_REG\_VAL\_SHIFT

| #define STM32\_ADC\_REG\_VAL\_SHIFT   16U |
| --- |

## [◆ ](#ac0daa8666c342a0a4326ec6687dda1b2)STM32\_ADC\_RES

| #define STM32\_ADC\_RES | ( |  | *resolution*, |
| --- | --- | --- | --- |
|  |  |  | *reg\_val* ) |

**Value:**

[STM32\_ADC](#a7ef6d8d5005e78ee779331b13aa80b16)(resolution, reg\_val, [STM32\_ADC\_RES\_MASK](stm32f1__adc_8h.md#a2a727c7d9a6496b2fdc3da2d24841e3f), [STM32\_ADC\_RES\_SHIFT](stm32f1__adc_8h.md#abd31ebaa20fd7e23b81c61926ff9adbe), \

[STM32\_ADC\_RES\_REG](stm32f1__adc_8h.md#a172393ce17e4f6f94c78b5b171354120))

[STM32\_ADC](#a7ef6d8d5005e78ee779331b13aa80b16)

#define STM32\_ADC(real\_val, reg\_val, mask, shift, reg)

STM32 ADC configuration bit field.

**Definition** stm32\_adc.h:37

[STM32\_ADC\_RES\_REG](stm32f1__adc_8h.md#a172393ce17e4f6f94c78b5b171354120)

#define STM32\_ADC\_RES\_REG

**Definition** stm32f1\_adc.h:18

[STM32\_ADC\_RES\_MASK](stm32f1__adc_8h.md#a2a727c7d9a6496b2fdc3da2d24841e3f)

#define STM32\_ADC\_RES\_MASK

**Definition** stm32f1\_adc.h:20

[STM32\_ADC\_RES\_SHIFT](stm32f1__adc_8h.md#abd31ebaa20fd7e23b81c61926ff9adbe)

#define STM32\_ADC\_RES\_SHIFT

**Definition** stm32f1\_adc.h:19

## [◆ ](#a0320e06eac0586ece090140280800997)STM32\_ADC\_SHIFT\_MASK

| #define STM32\_ADC\_SHIFT\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5) |
| --- |

## [◆ ](#a2096ae20f7315d6369bd94fb39bc4e44)STM32\_ADC\_SHIFT\_SHIFT

| #define STM32\_ADC\_SHIFT\_SHIFT   8U |
| --- |

## [◆ ](#a9ac82e856c7683e23553431e5224d5f4)SYNC

| #define SYNC   1 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [stm32\_adc.h](stm32__adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
