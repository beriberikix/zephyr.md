---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gd32__exti_8h.html
original_path: doxygen/html/gd32__exti_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32\_exti.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](gd32__exti_8h_source.md)

| Macros | |
| --- | --- |
| EXTI trigger modes. | |
|  | |
| #define | [GD32\_EXTI\_TRIG\_NONE](#aa2b7ef2f0b43317c7c58fe4d53e07a19)   0U |
|  | No trigger. |
| #define | [GD32\_EXTI\_TRIG\_RISING](#a8d9e9cd3451d66f8d6df889ea8d50a3c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Trigger on rising edge. |
| #define | [GD32\_EXTI\_TRIG\_FALLING](#aab892d582f9f266f7d942d238786e306)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Trigger on falling edge. |
| #define | [GD32\_EXTI\_TRIG\_BOTH](#a6e09a28174e0c4b9ec7a79e89199f7e4)   ([GD32\_EXTI\_TRIG\_RISING](#a8d9e9cd3451d66f8d6df889ea8d50a3c) | [GD32\_EXTI\_TRIG\_FALLING](#aab892d582f9f266f7d942d238786e306)) |
|  | Trigger on rising and falling edge. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [gd32\_exti\_cb\_t](#aac1a418b49c19fcf6e0dff2c0a3b7f75)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, void \*user) |
|  | Callback for EXTI interrupt. |

| Functions | |
| --- | --- |
| void | [gd32\_exti\_enable](#ad63c2b15a0f2e0f703255b00b9368232) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line) |
|  | Enable EXTI interrupt for the given line. |
| void | [gd32\_exti\_disable](#a3f0333dce2621c7fed721e37a2413d80) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line) |
|  | Disable EXTI interrupt for the given line. |
| void | [gd32\_exti\_trigger](#ac543badc8874861f866b3bf3eba37e9a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) trigger) |
|  | Configure EXTI interrupt trigger mode for the given line. |
| int | [gd32\_exti\_configure](#a014fba07d150faa8270493bb8257b31b) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, [gd32\_exti\_cb\_t](#aac1a418b49c19fcf6e0dff2c0a3b7f75) cb, void \*user) |
|  | Configure EXTI interrupt callback. |

## Macro Definition Documentation

## [◆ ](#a6e09a28174e0c4b9ec7a79e89199f7e4)GD32\_EXTI\_TRIG\_BOTH

| #define GD32\_EXTI\_TRIG\_BOTH   ([GD32\_EXTI\_TRIG\_RISING](#a8d9e9cd3451d66f8d6df889ea8d50a3c) | [GD32\_EXTI\_TRIG\_FALLING](#aab892d582f9f266f7d942d238786e306)) |
| --- |

Trigger on rising and falling edge.

## [◆ ](#aab892d582f9f266f7d942d238786e306)GD32\_EXTI\_TRIG\_FALLING

| #define GD32\_EXTI\_TRIG\_FALLING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Trigger on falling edge.

## [◆ ](#aa2b7ef2f0b43317c7c58fe4d53e07a19)GD32\_EXTI\_TRIG\_NONE

| #define GD32\_EXTI\_TRIG\_NONE   0U |
| --- |

No trigger.

## [◆ ](#a8d9e9cd3451d66f8d6df889ea8d50a3c)GD32\_EXTI\_TRIG\_RISING

| #define GD32\_EXTI\_TRIG\_RISING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Trigger on rising edge.

## Typedef Documentation

## [◆ ](#aac1a418b49c19fcf6e0dff2c0a3b7f75)gd32\_exti\_cb\_t

| typedef void(\* gd32\_exti\_cb\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, void \*user) |
| --- |

Callback for EXTI interrupt.

## Function Documentation

## [◆ ](#a014fba07d150faa8270493bb8257b31b)gd32\_exti\_configure()

| int gd32\_exti\_configure | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line*, |
| --- | --- | --- | --- |
|  |  | [gd32\_exti\_cb\_t](#aac1a418b49c19fcf6e0dff2c0a3b7f75) | *cb*, |
|  |  | void \* | *user* ) |

Configure EXTI interrupt callback.

Parameters
:   | line | EXTI line. |
    | --- | --- |
    | cb | Callback (NULL to disable). |
    | user | User data (optional). |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EALREADY | If callback is already set and `cb` is not NULL. |

## [◆ ](#a3f0333dce2621c7fed721e37a2413d80)gd32\_exti\_disable()

| void gd32\_exti\_disable | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable EXTI interrupt for the given line.

Parameters
:   | line | EXTI line. |
    | --- | --- |

## [◆ ](#ad63c2b15a0f2e0f703255b00b9368232)gd32\_exti\_enable()

| void gd32\_exti\_enable | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable EXTI interrupt for the given line.

Parameters
:   | line | EXTI line. |
    | --- | --- |

## [◆ ](#ac543badc8874861f866b3bf3eba37e9a)gd32\_exti\_trigger()

| void gd32\_exti\_trigger | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *trigger* ) |

Configure EXTI interrupt trigger mode for the given line.

Parameters
:   | line | EXTI line. |
    | --- | --- |
    | trigger | Trigger mode (see [GD32\_EXTI\_TRIG](#GD32_EXTI_TRIG)). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [gd32\_exti.h](gd32__exti_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
