---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2xtensa_2gdbstub_8h.html
original_path: doxygen/html/arch_2xtensa_2gdbstub_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdbstub.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <gdbstub/soc.h>`

[Go to the source code of this file.](arch_2xtensa_2gdbstub_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [xtensa\_register](structxtensa__register.md) |
|  | Register description for GDB stub. [More...](structxtensa__register.md#details) |
| struct | [gdb\_ctx](structgdb__ctx.md) |
|  | Architecture specific GDB context. [More...](structgdb__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [XTREG\_GRP\_MASK](#a6d8520d58f7d4a35a8d747a2ea2b8b2e)   0x0F00 |
| #define | [XTREG\_GRP\_GENERAL](#a6c4b0ec6ff50d409949b3eb675101fa9)   0x0000 |
| #define | [XTREG\_GRP\_ADDR](#a4ce12c698d17a8e67b11392362a2a7b8)   0x0100 |
| #define | [XTREG\_GRP\_SPECIAL](#a9cebc8c3e734ccb3997757018014b3e3)   0x0200 |
| #define | [XTREG\_GRP\_USER](#a1b75ea49d7031c3d9b334dcf636727ca)   0x0300 |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gdb\_xtensa\_is\_logical\_addr\_reg](#a60984092197e67f37d85bc8819b97f65) (struct [xtensa\_register](structxtensa__register.md) \*reg) |
|  | Test if the register is a logical address register (A0 - A15). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gdb\_xtensa\_is\_address\_reg](#a1c2969ce9537bb9adca02a37a4a887c5) (struct [xtensa\_register](structxtensa__register.md) \*reg) |
|  | Test if the register is a address register (AR0 - AR31/AR63). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gdb\_xtensa\_is\_special\_reg](#a65288d340838b80be483b62e00be3afa) (struct [xtensa\_register](structxtensa__register.md) \*reg) |
|  | Test if the register is a special register that needs to be accessed via RSR/WSR. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gdb\_xtensa\_is\_user\_reg](#ae2cdfe587c68d6e606df46a646343ae7) (struct [xtensa\_register](structxtensa__register.md) \*reg) |
|  | Test if the register is a user register that needs to be accessed via RUR/WUR. |

## Macro Definition Documentation

## [◆ ](#a4ce12c698d17a8e67b11392362a2a7b8)XTREG\_GRP\_ADDR

| #define XTREG\_GRP\_ADDR   0x0100 |
| --- |

## [◆ ](#a6c4b0ec6ff50d409949b3eb675101fa9)XTREG\_GRP\_GENERAL

| #define XTREG\_GRP\_GENERAL   0x0000 |
| --- |

## [◆ ](#a6d8520d58f7d4a35a8d747a2ea2b8b2e)XTREG\_GRP\_MASK

| #define XTREG\_GRP\_MASK   0x0F00 |
| --- |

## [◆ ](#a9cebc8c3e734ccb3997757018014b3e3)XTREG\_GRP\_SPECIAL

| #define XTREG\_GRP\_SPECIAL   0x0200 |
| --- |

## [◆ ](#a1b75ea49d7031c3d9b334dcf636727ca)XTREG\_GRP\_USER

| #define XTREG\_GRP\_USER   0x0300 |
| --- |

## Function Documentation

## [◆ ](#a1c2969ce9537bb9adca02a37a4a887c5)gdb\_xtensa\_is\_address\_reg()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gdb\_xtensa\_is\_address\_reg | ( | struct [xtensa\_register](structxtensa__register.md) \* | *reg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Test if the register is a address register (AR0 - AR31/AR63).

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if register is AR0 - AR31/AR63 |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if not |

## [◆ ](#a60984092197e67f37d85bc8819b97f65)gdb\_xtensa\_is\_logical\_addr\_reg()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gdb\_xtensa\_is\_logical\_addr\_reg | ( | struct [xtensa\_register](structxtensa__register.md) \* | *reg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Test if the register is a logical address register (A0 - A15).

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if register is A0 - A15 |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if register is not A0 - A15 |

## [◆ ](#a65288d340838b80be483b62e00be3afa)gdb\_xtensa\_is\_special\_reg()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gdb\_xtensa\_is\_special\_reg | ( | struct [xtensa\_register](structxtensa__register.md) \* | *reg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Test if the register is a special register that needs to be accessed via RSR/WSR.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if special register |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if not |

## [◆ ](#ae2cdfe587c68d6e606df46a646343ae7)gdb\_xtensa\_is\_user\_reg()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gdb\_xtensa\_is\_user\_reg | ( | struct [xtensa\_register](structxtensa__register.md) \* | *reg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Test if the register is a user register that needs to be accessed via RUR/WUR.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if user register |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if not |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [gdbstub.h](arch_2xtensa_2gdbstub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
