---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32-common_8h.html
original_path: doxygen/html/stm32-common_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-common.h File Reference

[Go to the source code of this file.](stm32-common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_RESET](#a6a12a4b8c042157a88ddf7da442c137c)(bus, bit) |
|  | Pack RCC register offset and bit in one 32-bit value. |

## Macro Definition Documentation

## [◆ ](#a6a12a4b8c042157a88ddf7da442c137c)STM32\_RESET

| #define STM32\_RESET | ( |  | *bus*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

(((STM32\_RESET\_BUS\_##bus) << 5U) | (bit))

Pack RCC register offset and bit in one 32-bit value.

5 LSBs are used to keep bit number in 32-bit RCC register. Next 12 bits are used to keep RCC register offset. Remaining bits are unused.

Parameters
:   | bus | STM32 bus name (expands to STM32\_RESET\_BUS\_{bus}) |
    | --- | --- |
    | bit | Reset bit |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32-common.h](stm32-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
