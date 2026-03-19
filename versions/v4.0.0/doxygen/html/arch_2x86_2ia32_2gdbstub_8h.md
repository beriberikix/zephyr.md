---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2x86_2ia32_2gdbstub_8h.html
original_path: doxygen/html/arch_2x86_2ia32_2gdbstub_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdbstub.h File Reference

IA-32 specific gdbstub interface header.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](arch_2x86_2ia32_2gdbstub_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gdb\_interrupt\_ctx](structgdb__interrupt__ctx.md) |
|  | GDB interruption context. [More...](structgdb__interrupt__ctx.md#details) |
| struct | [gdb\_ctx](structgdb__ctx.md) |
|  | Architecture specific GDB context. [More...](structgdb__ctx.md#details) |

| Macros | |
| --- | --- |
| #define | [GDB\_STUB\_NUM\_REGISTERS](#a235bb190327ce0586e0b111186fe1b95)   16 |
|  | Number of register used by gdbstub in IA-32. |

| Enumerations | |
| --- | --- |
| enum | [GDB\_REGISTER](#a02deeb8532e144b369c484cdd4bc1a57) {     [GDB\_EAX](#a02deeb8532e144b369c484cdd4bc1a57ab4c205bdcc3be6a5050e7bebd4fb6b66) , [GDB\_ECX](#a02deeb8532e144b369c484cdd4bc1a57abee48d7c6075a3c8928ec45a8a609429) , [GDB\_EDX](#a02deeb8532e144b369c484cdd4bc1a57a22a0a7034fcd3674658eecef1f2dade8) , [GDB\_EBX](#a02deeb8532e144b369c484cdd4bc1a57abaaf1dc478746db2a60681141fc35156) ,     [GDB\_ESP](#a02deeb8532e144b369c484cdd4bc1a57af4f770bdcdbcca2db69c917f2525ea44) , [GDB\_EBP](#a02deeb8532e144b369c484cdd4bc1a57a001777bf465ee869d25c247dd8c4916b) , [GDB\_ESI](#a02deeb8532e144b369c484cdd4bc1a57a0ee89015912e10141cd809b8d0578e6f) , [GDB\_EDI](#a02deeb8532e144b369c484cdd4bc1a57ade30ceaa244559a00e83b0f7a8f669a7) ,     [GDB\_PC](#a02deeb8532e144b369c484cdd4bc1a57a22b538160b178a0438fbaf3596425086) , [GDB\_EFLAGS](#a02deeb8532e144b369c484cdd4bc1a57a8c5ef12c827f25bdb506a9bfd35a4fca) , [GDB\_CS](#a02deeb8532e144b369c484cdd4bc1a57acc9df508ccc4168e9f77e4054d99fd6b) , [GDB\_SS](#a02deeb8532e144b369c484cdd4bc1a57a1cefa340d9b999a519dbb60c18098b28) ,     [GDB\_DS](#a02deeb8532e144b369c484cdd4bc1a57acb0bd3c78585106edca9f1f933d9e715) , [GDB\_ES](#a02deeb8532e144b369c484cdd4bc1a57a9880757bbfebbf1a4cc54fea187209b9) , [GDB\_FS](#a02deeb8532e144b369c484cdd4bc1a57a41774764a1340a3003020ba07b90f175) , [GDB\_GS](#a02deeb8532e144b369c484cdd4bc1a57a97870647fb9b956008034d5b8f07c333) ,     [GDB\_ORIG\_EAX](#a02deeb8532e144b369c484cdd4bc1a57a07753f9e894968bb44a885731d3c6a7c) = 41   } |
|  | IA-32 register used in gdbstub. [More...](#a02deeb8532e144b369c484cdd4bc1a57) |

## Detailed Description

IA-32 specific gdbstub interface header.

## Macro Definition Documentation

## [◆ ](#a235bb190327ce0586e0b111186fe1b95)GDB\_STUB\_NUM\_REGISTERS

| #define GDB\_STUB\_NUM\_REGISTERS   16 |
| --- |

Number of register used by gdbstub in IA-32.

## Enumeration Type Documentation

## [◆ ](#a02deeb8532e144b369c484cdd4bc1a57)GDB\_REGISTER

| enum [GDB\_REGISTER](#a02deeb8532e144b369c484cdd4bc1a57) |
| --- |

IA-32 register used in gdbstub.

| Enumerator | |
| --- | --- |
| GDB\_EAX |  |
| GDB\_ECX |  |
| GDB\_EDX |  |
| GDB\_EBX |  |
| GDB\_ESP |  |
| GDB\_EBP |  |
| GDB\_ESI |  |
| GDB\_EDI |  |
| GDB\_PC |  |
| GDB\_EFLAGS |  |
| GDB\_CS |  |
| GDB\_SS |  |
| GDB\_DS |  |
| GDB\_ES |  |
| GDB\_FS |  |
| GDB\_GS |  |
| GDB\_ORIG\_EAX |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [gdbstub.h](arch_2x86_2ia32_2gdbstub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
