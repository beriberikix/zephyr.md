---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structgdb__ctx.html
original_path: doxygen/html/structgdb__ctx.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdb\_ctx Struct Reference

Architecture specific GDB context.
[More...](#details)

`#include <[gdbstub.h](arch_2arm_2gdbstub_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [exception](#adba5c39e347abc419b365bab2a1a0999) |
|  | Exception reason. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [registers](#a3932959d4a31a75c6cf77b42b95bd511) [[GDB\_NUM\_REGS](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abab4321f1e50a634d85534d73e468e97dd)] |
| struct [xtensa\_register](structxtensa__register.md) \* | [regs](#adb06cbd2bc9f322d692f8a73fb18e99d) |
|  | Register descriptions. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_regs](#a2eb775bca1b96ddfa495620d0a19788d) |
|  | Number of registers. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [seqno](#ac040960f884c235a3b27820d49d30161) |
|  | Sequence number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [a0\_idx](#ac4930a460dc63c823b4e8e13e925c067) |
|  | Index in register descriptions of A0 register. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ar\_idx](#ae73c7bcb4e501c9f28308838f0923cd0) |
|  | Index in register descriptions of AR0 register. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [wb\_idx](#a4094f8ee5045ee6ca97fb256b0a93a41) |
|  | Index in register descriptions of WINDOWBASE register. |

## Detailed Description

Architecture specific GDB context.

## Field Documentation

## [◆ ](#ac4930a460dc63c823b4e8e13e925c067)a0\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gdb\_ctx::a0\_idx |
| --- |

Index in register descriptions of A0 register.

## [◆ ](#ae73c7bcb4e501c9f28308838f0923cd0)ar\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gdb\_ctx::ar\_idx |
| --- |

Index in register descriptions of AR0 register.

## [◆ ](#adba5c39e347abc419b365bab2a1a0999)exception

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int gdb\_ctx::exception |
| --- |

Exception reason.

## [◆ ](#a2eb775bca1b96ddfa495620d0a19788d)num\_regs

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gdb\_ctx::num\_regs |
| --- |

Number of registers.

## [◆ ](#a3932959d4a31a75c6cf77b42b95bd511)registers

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int gdb\_ctx::registers |
| --- |

## [◆ ](#adb06cbd2bc9f322d692f8a73fb18e99d)regs

| struct [xtensa\_register](structxtensa__register.md)\* gdb\_ctx::regs |
| --- |

Register descriptions.

## [◆ ](#ac040960f884c235a3b27820d49d30161)seqno

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gdb\_ctx::seqno |
| --- |

Sequence number.

## [◆ ](#a4094f8ee5045ee6ca97fb256b0a93a41)wb\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gdb\_ctx::wb\_idx |
| --- |

Index in register descriptions of WINDOWBASE register.

---

The documentation for this struct was generated from the following files:

- zephyr/arch/arm/[gdbstub.h](arch_2arm_2gdbstub_8h_source.md)
- zephyr/arch/x86/ia32/[gdbstub.h](arch_2x86_2ia32_2gdbstub_8h_source.md)
- zephyr/arch/xtensa/[gdbstub.h](arch_2xtensa_2gdbstub_8h_source.md)

- [gdb\_ctx](structgdb__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
