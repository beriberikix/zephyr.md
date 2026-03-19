---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2arm_2gdbstub_8h.html
original_path: doxygen/html/arch_2arm_2gdbstub_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdbstub.h File Reference

`#include <[zephyr/arch/arm/exception.h](arm_2exception_8h_source.md)>`

[Go to the source code of this file.](arch_2arm_2gdbstub_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gdb\_ctx](structgdb__ctx.md) |
|  | Architecture specific GDB context. [More...](structgdb__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [DBGDSCR\_MONITOR\_MODE\_EN](#ae317be4d10650eb7cbb82e712dfea3cf)   0x8000 |
| #define | [SPSR\_ISETSTATE\_ARM](#a32017751414ac0108912b631a7ac2fc0)   0x0 |
| #define | [SPSR\_ISETSTATE\_JAZELLE](#a4e3118b8f4d3473750a606e5f4015622)   0x2 |
| #define | [SPSR\_J](#a5e5065f2d7a76a211a83c196b1b32ffe)   24 |
| #define | [SPSR\_T](#a052da1c2631bb0ea9f8670244c22702c)   5 |
| #define | [DBGDBCR\_MEANING\_MASK](#a01ddae18a481f64f43e45bec4cec862f)   0x7 |
| #define | [DBGDBCR\_MEANING\_SHIFT](#ae980d4c38dc2b9cf9a844ee6c260543c)   20 |
| #define | [DBGDBCR\_MEANING\_ADDR\_MISMATCH](#a4a8887a30ce534c977025df4cda6ebf3)   0x4 |
| #define | [DBGDBCR\_BYTE\_ADDR\_MASK](#a50194abb1647e1d92d01c4ba47a9ec45)   0xF |
| #define | [DBGDBCR\_BYTE\_ADDR\_SHIFT](#ac87512cf5f50421d9b497257ac57e0e6)   5 |
| #define | [DBGDBCR\_BRK\_EN\_MASK](#a8a45c188cf3151e9be5be93f30045677)   0x1 |
| #define | [SPSR\_REG\_IDX](#a3cd5aa981d967ab54210822bc1a76b68)   25 |
| #define | [GDB\_READALL\_PACKET\_SIZE](#a6453cecddeb088726f5a2aa150d60666)   (42 \* 8) |
| #define | [IFSR\_DEBUG\_EVENT](#a4d913f0bcecc023101cde8e72c082d19)   0x2 |

| Enumerations | |
| --- | --- |
| enum | [AARCH32\_GDB\_REG](#a0d4c0f1339778bac80a5871c979605ab) {     [R0](#a0d4c0f1339778bac80a5871c979605aba8cd2a8ec48785abb434cbdfc72ea1219) = 0 , [R1](#a0d4c0f1339778bac80a5871c979605abaf8d87ff07efe24755164f550526f4dac) , [R2](#a0d4c0f1339778bac80a5871c979605aba629d7b403cea5f826352f3aefb9a6d6a) , [R3](#a0d4c0f1339778bac80a5871c979605abaad0b4725f69a34fed2c914517bcd9baa) ,     [R4](#a0d4c0f1339778bac80a5871c979605aba3805fd63a00bf220a1e303b977565eb8) , [R5](#a0d4c0f1339778bac80a5871c979605aba85be67ddcf5734117ab855cebe9b6563) , [R6](#a0d4c0f1339778bac80a5871c979605aba8cd5c4fcc06125ee4035a4f72a29bcba) , [R7](#a0d4c0f1339778bac80a5871c979605aba054fa446dec19779f7d15d8cc5fca5cf) ,     [R8](#a0d4c0f1339778bac80a5871c979605abadaf41609f8eadc7d15918adacc662c59) , [R9](#a0d4c0f1339778bac80a5871c979605aba550ff95070e1f18bc610107aaf8e0c2b) , [R10](#a0d4c0f1339778bac80a5871c979605abaef1c3e581bbab81e38c6d53357760b3c) , [R11](#a0d4c0f1339778bac80a5871c979605abaecda251967ab2413a2db85530a2a8429) ,     [R12](#a0d4c0f1339778bac80a5871c979605aba49ea06ace91cf41ec29751a4a1d5a7de) , [R13](#a0d4c0f1339778bac80a5871c979605aba1dd4349b8ea1e5be418ff8b01a25f37a) , [LR](#a0d4c0f1339778bac80a5871c979605aba6d456bf17ff1ba9f670c09ae9abb1305) , [PC](#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46) ,     [SPSR](#a0d4c0f1339778bac80a5871c979605aba34b48af74e3e2ce7523ef539a917dc39) , [GDB\_NUM\_REGS](#a0d4c0f1339778bac80a5871c979605abab4321f1e50a634d85534d73e468e97dd)   } |

## Macro Definition Documentation

## [◆ ](#a8a45c188cf3151e9be5be93f30045677)DBGDBCR\_BRK\_EN\_MASK

| #define DBGDBCR\_BRK\_EN\_MASK   0x1 |
| --- |

## [◆ ](#a50194abb1647e1d92d01c4ba47a9ec45)DBGDBCR\_BYTE\_ADDR\_MASK

| #define DBGDBCR\_BYTE\_ADDR\_MASK   0xF |
| --- |

## [◆ ](#ac87512cf5f50421d9b497257ac57e0e6)DBGDBCR\_BYTE\_ADDR\_SHIFT

| #define DBGDBCR\_BYTE\_ADDR\_SHIFT   5 |
| --- |

## [◆ ](#a4a8887a30ce534c977025df4cda6ebf3)DBGDBCR\_MEANING\_ADDR\_MISMATCH

| #define DBGDBCR\_MEANING\_ADDR\_MISMATCH   0x4 |
| --- |

## [◆ ](#a01ddae18a481f64f43e45bec4cec862f)DBGDBCR\_MEANING\_MASK

| #define DBGDBCR\_MEANING\_MASK   0x7 |
| --- |

## [◆ ](#ae980d4c38dc2b9cf9a844ee6c260543c)DBGDBCR\_MEANING\_SHIFT

| #define DBGDBCR\_MEANING\_SHIFT   20 |
| --- |

## [◆ ](#ae317be4d10650eb7cbb82e712dfea3cf)DBGDSCR\_MONITOR\_MODE\_EN

| #define DBGDSCR\_MONITOR\_MODE\_EN   0x8000 |
| --- |

## [◆ ](#a6453cecddeb088726f5a2aa150d60666)GDB\_READALL\_PACKET\_SIZE

| #define GDB\_READALL\_PACKET\_SIZE   (42 \* 8) |
| --- |

## [◆ ](#a4d913f0bcecc023101cde8e72c082d19)IFSR\_DEBUG\_EVENT

| #define IFSR\_DEBUG\_EVENT   0x2 |
| --- |

## [◆ ](#a32017751414ac0108912b631a7ac2fc0)SPSR\_ISETSTATE\_ARM

| #define SPSR\_ISETSTATE\_ARM   0x0 |
| --- |

## [◆ ](#a4e3118b8f4d3473750a606e5f4015622)SPSR\_ISETSTATE\_JAZELLE

| #define SPSR\_ISETSTATE\_JAZELLE   0x2 |
| --- |

## [◆ ](#a5e5065f2d7a76a211a83c196b1b32ffe)SPSR\_J

| #define SPSR\_J   24 |
| --- |

## [◆ ](#a3cd5aa981d967ab54210822bc1a76b68)SPSR\_REG\_IDX

| #define SPSR\_REG\_IDX   25 |
| --- |

## [◆ ](#a052da1c2631bb0ea9f8670244c22702c)SPSR\_T

| #define SPSR\_T   5 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a0d4c0f1339778bac80a5871c979605ab)AARCH32\_GDB\_REG

| enum [AARCH32\_GDB\_REG](#a0d4c0f1339778bac80a5871c979605ab) |
| --- |

| Enumerator | |
| --- | --- |
| R0 |  |
| R1 |  |
| R2 |  |
| R3 |  |
| R4 |  |
| R5 |  |
| R6 |  |
| R7 |  |
| R8 |  |
| R9 |  |
| R10 |  |
| R11 |  |
| R12 |  |
| R13 |  |
| LR |  |
| PC |  |
| SPSR |  |
| GDB\_NUM\_REGS |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [gdbstub.h](arch_2arm_2gdbstub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
