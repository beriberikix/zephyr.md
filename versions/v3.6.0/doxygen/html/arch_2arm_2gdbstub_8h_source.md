---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2arm_2gdbstub_8h_source.html
original_path: doxygen/html/arch_2arm_2gdbstub_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdbstub.h

[Go to the documentation of this file.](arch_2arm_2gdbstub_8h.md)

1/\*

2 \* Copyright (c) 2023 Marek Vedral <vedrama5@fel.cvut.cz>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_AARCH32\_GDBSTUB\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_AARCH32\_GDBSTUB\_H\_

9

10#include <zephyr/arch/arm/exc.h>

11

12#ifndef \_ASMLANGUAGE

13

[ 14](arch_2arm_2gdbstub_8h.md#ae317be4d10650eb7cbb82e712dfea3cf)#define DBGDSCR\_MONITOR\_MODE\_EN 0x8000

15

[ 16](arch_2arm_2gdbstub_8h.md#a32017751414ac0108912b631a7ac2fc0)#define SPSR\_ISETSTATE\_ARM 0x0

[ 17](arch_2arm_2gdbstub_8h.md#a4e3118b8f4d3473750a606e5f4015622)#define SPSR\_ISETSTATE\_JAZELLE 0x2

[ 18](arch_2arm_2gdbstub_8h.md#a5e5065f2d7a76a211a83c196b1b32ffe)#define SPSR\_J 24

[ 19](arch_2arm_2gdbstub_8h.md#a052da1c2631bb0ea9f8670244c22702c)#define SPSR\_T 5

20

21/\* Debug Breakpoint Control Register constants \*/

[ 22](arch_2arm_2gdbstub_8h.md#a01ddae18a481f64f43e45bec4cec862f)#define DBGDBCR\_MEANING\_MASK 0x7

[ 23](arch_2arm_2gdbstub_8h.md#ae980d4c38dc2b9cf9a844ee6c260543c)#define DBGDBCR\_MEANING\_SHIFT 20

[ 24](arch_2arm_2gdbstub_8h.md#a4a8887a30ce534c977025df4cda6ebf3)#define DBGDBCR\_MEANING\_ADDR\_MISMATCH 0x4

[ 25](arch_2arm_2gdbstub_8h.md#a50194abb1647e1d92d01c4ba47a9ec45)#define DBGDBCR\_BYTE\_ADDR\_MASK 0xF

[ 26](arch_2arm_2gdbstub_8h.md#ac87512cf5f50421d9b497257ac57e0e6)#define DBGDBCR\_BYTE\_ADDR\_SHIFT 5

[ 27](arch_2arm_2gdbstub_8h.md#a8a45c188cf3151e9be5be93f30045677)#define DBGDBCR\_BRK\_EN\_MASK 0x1

28

29/\* Regno of the SPSR \*/

[ 30](arch_2arm_2gdbstub_8h.md#a3cd5aa981d967ab54210822bc1a76b68)#define SPSR\_REG\_IDX 25

31/\* Minimal size of the packet - SPSR is the last, 42-nd byte, see packet\_pos array \*/

[ 32](arch_2arm_2gdbstub_8h.md#a6453cecddeb088726f5a2aa150d60666)#define GDB\_READALL\_PACKET\_SIZE (42 \* 8)

33

[ 34](arch_2arm_2gdbstub_8h.md#a4d913f0bcecc023101cde8e72c082d19)#define IFSR\_DEBUG\_EVENT 0x2

35

[ 36](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605ab)enum [AARCH32\_GDB\_REG](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605ab) {

[ 37](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba8cd2a8ec48785abb434cbdfc72ea1219) [R0](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba8cd2a8ec48785abb434cbdfc72ea1219) = 0,

[ 38](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaf8d87ff07efe24755164f550526f4dac) [R1](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaf8d87ff07efe24755164f550526f4dac),

[ 39](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba629d7b403cea5f826352f3aefb9a6d6a) [R2](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba629d7b403cea5f826352f3aefb9a6d6a),

[ 40](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaad0b4725f69a34fed2c914517bcd9baa) [R3](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaad0b4725f69a34fed2c914517bcd9baa),

41 /\* READONLY registers (R4 - R13) except R12 \*/

[ 42](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba3805fd63a00bf220a1e303b977565eb8) [R4](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba3805fd63a00bf220a1e303b977565eb8),

[ 43](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba85be67ddcf5734117ab855cebe9b6563) [R5](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba85be67ddcf5734117ab855cebe9b6563),

[ 44](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba8cd5c4fcc06125ee4035a4f72a29bcba) [R6](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba8cd5c4fcc06125ee4035a4f72a29bcba),

[ 45](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba054fa446dec19779f7d15d8cc5fca5cf) [R7](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba054fa446dec19779f7d15d8cc5fca5cf),

[ 46](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abadaf41609f8eadc7d15918adacc662c59) [R8](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abadaf41609f8eadc7d15918adacc662c59),

[ 47](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba550ff95070e1f18bc610107aaf8e0c2b) [R9](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba550ff95070e1f18bc610107aaf8e0c2b),

[ 48](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaef1c3e581bbab81e38c6d53357760b3c) [R10](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaef1c3e581bbab81e38c6d53357760b3c),

[ 49](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaecda251967ab2413a2db85530a2a8429) [R11](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaecda251967ab2413a2db85530a2a8429),

[ 50](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba49ea06ace91cf41ec29751a4a1d5a7de) [R12](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba49ea06ace91cf41ec29751a4a1d5a7de),

51 /\* Stack pointer - READONLY \*/

[ 52](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba1dd4349b8ea1e5be418ff8b01a25f37a) [R13](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba1dd4349b8ea1e5be418ff8b01a25f37a),

[ 53](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba6d456bf17ff1ba9f670c09ae9abb1305) [LR](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba6d456bf17ff1ba9f670c09ae9abb1305),

[ 54](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46) [PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46),

55 /\* Saved program status register \*/

[ 56](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba34b48af74e3e2ce7523ef539a917dc39) [SPSR](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba34b48af74e3e2ce7523ef539a917dc39),

[ 57](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abab4321f1e50a634d85534d73e468e97dd) [GDB\_NUM\_REGS](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abab4321f1e50a634d85534d73e468e97dd)

58};

59

60/\* required structure \*/

[ 61](structgdb__ctx.md)struct [gdb\_ctx](structgdb__ctx.md) {

62 /\* cause of the exception \*/

[ 63](structgdb__ctx.md#adba5c39e347abc419b365bab2a1a0999) unsigned int [exception](structgdb__ctx.md#adba5c39e347abc419b365bab2a1a0999);

[ 64](structgdb__ctx.md#a3932959d4a31a75c6cf77b42b95bd511) unsigned int [registers](structgdb__ctx.md#a3932959d4a31a75c6cf77b42b95bd511)[[GDB\_NUM\_REGS](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abab4321f1e50a634d85534d73e468e97dd)];

65};

66

67void z\_gdb\_entry(z\_arch\_esf\_t \*esf, unsigned int exc\_cause);

68

69#endif

70

71#endif

[AARCH32\_GDB\_REG](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605ab)

AARCH32\_GDB\_REG

**Definition** gdbstub.h:36

[R7](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba054fa446dec19779f7d15d8cc5fca5cf)

@ R7

**Definition** gdbstub.h:45

[R13](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba1dd4349b8ea1e5be418ff8b01a25f37a)

@ R13

**Definition** gdbstub.h:52

[SPSR](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba34b48af74e3e2ce7523ef539a917dc39)

@ SPSR

**Definition** gdbstub.h:56

[R4](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba3805fd63a00bf220a1e303b977565eb8)

@ R4

**Definition** gdbstub.h:42

[R12](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba49ea06ace91cf41ec29751a4a1d5a7de)

@ R12

**Definition** gdbstub.h:50

[R9](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba550ff95070e1f18bc610107aaf8e0c2b)

@ R9

**Definition** gdbstub.h:47

[R2](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba629d7b403cea5f826352f3aefb9a6d6a)

@ R2

**Definition** gdbstub.h:39

[LR](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba6d456bf17ff1ba9f670c09ae9abb1305)

@ LR

**Definition** gdbstub.h:53

[R5](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba85be67ddcf5734117ab855cebe9b6563)

@ R5

**Definition** gdbstub.h:43

[R0](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba8cd2a8ec48785abb434cbdfc72ea1219)

@ R0

**Definition** gdbstub.h:37

[R6](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605aba8cd5c4fcc06125ee4035a4f72a29bcba)

@ R6

**Definition** gdbstub.h:44

[PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46)

@ PC

**Definition** gdbstub.h:54

[R3](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaad0b4725f69a34fed2c914517bcd9baa)

@ R3

**Definition** gdbstub.h:40

[GDB\_NUM\_REGS](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abab4321f1e50a634d85534d73e468e97dd)

@ GDB\_NUM\_REGS

**Definition** gdbstub.h:57

[R8](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abadaf41609f8eadc7d15918adacc662c59)

@ R8

**Definition** gdbstub.h:46

[R11](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaecda251967ab2413a2db85530a2a8429)

@ R11

**Definition** gdbstub.h:49

[R10](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaef1c3e581bbab81e38c6d53357760b3c)

@ R10

**Definition** gdbstub.h:48

[R1](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaf8d87ff07efe24755164f550526f4dac)

@ R1

**Definition** gdbstub.h:38

[gdb\_ctx](structgdb__ctx.md)

Architecture specific GDB context.

**Definition** gdbstub.h:61

[gdb\_ctx::registers](structgdb__ctx.md#a3932959d4a31a75c6cf77b42b95bd511)

unsigned int registers[GDB\_NUM\_REGS]

**Definition** gdbstub.h:64

[gdb\_ctx::exception](structgdb__ctx.md#adba5c39e347abc419b365bab2a1a0999)

unsigned int exception

Exception reason.

**Definition** gdbstub.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [gdbstub.h](arch_2arm_2gdbstub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
