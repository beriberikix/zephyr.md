---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/exti__stm32_8h.html
original_path: doxygen/html/exti__stm32_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exti\_stm32.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](exti__stm32_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_EXTI\_LINE\_NONE](#ac77d469d5ec2ea32fb52b89f062fece5)   0xFFFFFFFFU |
|  | Driver for External interrupt/event controller in STM32 MCUs. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [stm32\_exti\_callback\_t](#a7ee31db62548a8e6977ede220fc3fce9)) (int line, void \*user) |

| Enumerations | |
| --- | --- |
| enum | [stm32\_exti\_trigger](#a2caf7f256985537368b079f565adb9e7) { [STM32\_EXTI\_TRIG\_NONE](#a2caf7f256985537368b079f565adb9e7aa44b00e6dd732140f0c152ec6a5ad0e0) = 0x0 , [STM32\_EXTI\_TRIG\_RISING](#a2caf7f256985537368b079f565adb9e7ac1ab9fda0db1fb1a852bfe358c7e6485) = 0x1 , [STM32\_EXTI\_TRIG\_FALLING](#a2caf7f256985537368b079f565adb9e7a8a53325045c0825c5fd379d83a04f5e4) = 0x2 , [STM32\_EXTI\_TRIG\_BOTH](#a2caf7f256985537368b079f565adb9e7a013afe4b3bfc4921f30dad835e7f87cc) = 0x3 } |
|  | EXTI trigger flags. [More...](#a2caf7f256985537368b079f565adb9e7) |

| Functions | |
| --- | --- |
| void | [stm32\_exti\_enable](#af40d4b71f65e3fc1b6bd3f353e58eaae) (int line) |
|  | enable EXTI interrupt for specific line |
| void | [stm32\_exti\_disable](#a77ed08c11acc54d4d00544b862383ec2) (int line) |
|  | disable EXTI interrupt for specific line |
| void | [stm32\_exti\_trigger](#aefb5e5f4a048cc233df749df9e45ac8a) (int line, int trg) |
|  | set EXTI interrupt line triggers |
| int | [stm32\_exti\_set\_callback](#ac9f5b3e69ef25b3f0855f9bad22c826a) (int line, [stm32\_exti\_callback\_t](#a7ee31db62548a8e6977ede220fc3fce9) cb, void \*data) |
|  | set EXTI interrupt callback |
| void | [stm32\_exti\_unset\_callback](#a1cf8d3d58087960e3f570369172e3015) (int line) |
|  | unset EXTI interrupt callback |

## Macro Definition Documentation

## [◆ ](#ac77d469d5ec2ea32fb52b89f062fece5)STM32\_EXTI\_LINE\_NONE

| #define STM32\_EXTI\_LINE\_NONE   0xFFFFFFFFU |
| --- |

Driver for External interrupt/event controller in STM32 MCUs.

Based on reference manuals: RM0008 Reference Manual: STM32F101xx, STM32F102xx, STM32F103xx, STM32F105xx and STM32F107xx advanced ARM(r)-based 32-bit MCUs and RM0368 Reference manual STM32F401xB/C and STM32F401xD/E advanced ARM(r)-based 32-bit MCUs

Chapter 10.2: External interrupt/event controller (EXTI)

## Typedef Documentation

## [◆ ](#a7ee31db62548a8e6977ede220fc3fce9)stm32\_exti\_callback\_t

| typedef void(\* stm32\_exti\_callback\_t) (int line, void \*user) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a2caf7f256985537368b079f565adb9e7)stm32\_exti\_trigger

| enum [stm32\_exti\_trigger](#a2caf7f256985537368b079f565adb9e7) |
| --- |

EXTI trigger flags.

| Enumerator | |
| --- | --- |
| STM32\_EXTI\_TRIG\_NONE |  |
| STM32\_EXTI\_TRIG\_RISING |  |
| STM32\_EXTI\_TRIG\_FALLING |  |
| STM32\_EXTI\_TRIG\_BOTH |  |

## Function Documentation

## [◆ ](#a77ed08c11acc54d4d00544b862383ec2)stm32\_exti\_disable()

| void stm32\_exti\_disable | ( | int | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

disable EXTI interrupt for specific line

Parameters
:   | line | EXTI# line |
    | --- | --- |

## [◆ ](#af40d4b71f65e3fc1b6bd3f353e58eaae)stm32\_exti\_enable()

| void stm32\_exti\_enable | ( | int | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

enable EXTI interrupt for specific line

Parameters
:   | line | EXTI# line |
    | --- | --- |

## [◆ ](#ac9f5b3e69ef25b3f0855f9bad22c826a)stm32\_exti\_set\_callback()

| int stm32\_exti\_set\_callback | ( | int | *line*, |
| --- | --- | --- | --- |
|  |  | [stm32\_exti\_callback\_t](#a7ee31db62548a8e6977ede220fc3fce9) | *cb*, |
|  |  | void \* | *data* ) |

set EXTI interrupt callback

Parameters
:   | line | EXI# line |
    | --- | --- |
    | cb | user callback |
    | data | user data |

## [◆ ](#aefb5e5f4a048cc233df749df9e45ac8a)stm32\_exti\_trigger()

| void [stm32\_exti\_trigger](#a2caf7f256985537368b079f565adb9e7) | ( | int | *line*, |
| --- | --- | --- | --- |
|  |  | int | *trg* ) |

set EXTI interrupt line triggers

Parameters
:   | line | EXTI# line |
    | --- | --- |
    | trg | OR'ed [stm32\_exti\_trigger](#a2caf7f256985537368b079f565adb9e7) flags |

## [◆ ](#a1cf8d3d58087960e3f570369172e3015)stm32\_exti\_unset\_callback()

| void stm32\_exti\_unset\_callback | ( | int | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

unset EXTI interrupt callback

Parameters
:   | line | EXI# line |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [exti\_stm32.h](exti__stm32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
