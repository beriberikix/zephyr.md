---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__arch-gdbstub.html
original_path: doxygen/html/group__arch-gdbstub.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific gdbstub APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| void | [arch\_gdb\_init](#ga21c8a32d35c4d267b8306d595ff1d726) (void) |
|  | Architecture layer debug start. |
| void | [arch\_gdb\_continue](#ga9c130421feeee919651828511743b346) (void) |
|  | Continue running program. |
| void | [arch\_gdb\_step](#ga2aa577d5e55c8b739e2be6187336aaf0) (void) |
|  | Continue with one step. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_gdb\_reg\_readall](#ga5317106a8022bea2a0d42af0789cc016) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen) |
|  | Read all registers, and outputs as hexadecimal string. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_gdb\_reg\_writeall](#ga0ef78d7e193e98549d9665632e53d5ca) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen) |
|  | Take a hexadecimal string and update all registers. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_gdb\_reg\_readone](#gaa3216e9f381f974c374a6399af5cdba5) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) regno) |
|  | Read one register, and outputs as hexadecimal string. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_gdb\_reg\_writeone](#gad717b520d774294bbda78a56cddcaeff) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) regno) |
|  | Take a hexadecimal string and update one register. |
| int | [arch\_gdb\_add\_breakpoint](#gab6f42110cf2340132bf2b3916810c01d) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) kind) |
|  | Add breakpoint or watchpoint. |
| int | [arch\_gdb\_remove\_breakpoint](#ga734041433f69030ad98439d10ef56ad6) (struct [gdb\_ctx](structgdb__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) kind) |
|  | Remove breakpoint or watchpoint. |

## Detailed Description

## Function Documentation

## [◆ ](#gab6f42110cf2340132bf2b3916810c01d)arch\_gdb\_add\_breakpoint()

| int arch\_gdb\_add\_breakpoint | ( | struct [gdb\_ctx](structgdb__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *addr*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *kind* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Add breakpoint or watchpoint.

Parameters
:   | ctx | GDB context |
    | --- | --- |
    | type | Breakpoint or watchpoint type |
    | addr | Address of breakpoint or watchpoint |
    | kind | Size of breakpoint/watchpoint in bytes |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -1 | Error encountered |
    | -2 | Not supported |

## [◆ ](#ga9c130421feeee919651828511743b346)arch\_gdb\_continue()

| void arch\_gdb\_continue | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Continue running program.

Continue software execution.

## [◆ ](#ga21c8a32d35c4d267b8306d595ff1d726)arch\_gdb\_init()

| void arch\_gdb\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Architecture layer debug start.

This function is called by `gdb_init()`

## [◆ ](#ga5317106a8022bea2a0d42af0789cc016)arch\_gdb\_reg\_readall()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_gdb\_reg\_readall | ( | struct [gdb\_ctx](structgdb__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buflen* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Read all registers, and outputs as hexadecimal string.

This reads all CPU registers and outputs as hexadecimal string. The output string must be parsable by GDB.

Parameters
:   | ctx | GDB context |
    | --- | --- |
    | buf | Buffer to output hexadecimal string. |
    | buflen | Length of buffer. |

Returns
:   Length of hexadecimal string written. Return 0 if error or not supported.

## [◆ ](#gaa3216e9f381f974c374a6399af5cdba5)arch\_gdb\_reg\_readone()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_gdb\_reg\_readone | ( | struct [gdb\_ctx](structgdb__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buflen*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *regno* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Read one register, and outputs as hexadecimal string.

This reads one CPU register and outputs as hexadecimal string. The output string must be parsable by GDB.

Parameters
:   | ctx | GDB context |
    | --- | --- |
    | buf | Buffer to output hexadecimal string. |
    | buflen | Length of buffer. |
    | regno | Register number |

Returns
:   Length of hexadecimal string written. Return 0 if error or not supported.

## [◆ ](#ga0ef78d7e193e98549d9665632e53d5ca)arch\_gdb\_reg\_writeall()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_gdb\_reg\_writeall | ( | struct [gdb\_ctx](structgdb__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *hex*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *hexlen* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Take a hexadecimal string and update all registers.

This takes in a hexadecimal string as presented from GDB, and updates all CPU registers with new values.

Parameters
:   | ctx | GDB context |
    | --- | --- |
    | hex | Input hexadecimal string. |
    | hexlen | Length of hexadecimal string. |

Returns
:   Length of hexadecimal string parsed. Return 0 if error or not supported.

## [◆ ](#gad717b520d774294bbda78a56cddcaeff)arch\_gdb\_reg\_writeone()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_gdb\_reg\_writeone | ( | struct [gdb\_ctx](structgdb__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *hex*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *hexlen*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *regno* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Take a hexadecimal string and update one register.

This takes in a hexadecimal string as presented from GDB, and updates one CPU registers with new value.

Parameters
:   | ctx | GDB context |
    | --- | --- |
    | hex | Input hexadecimal string. |
    | hexlen | Length of hexadecimal string. |
    | regno | Register number |

Returns
:   Length of hexadecimal string parsed. Return 0 if error or not supported.

## [◆ ](#ga734041433f69030ad98439d10ef56ad6)arch\_gdb\_remove\_breakpoint()

| int arch\_gdb\_remove\_breakpoint | ( | struct [gdb\_ctx](structgdb__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *addr*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *kind* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Remove breakpoint or watchpoint.

Parameters
:   | ctx | GDB context |
    | --- | --- |
    | type | Breakpoint or watchpoint type |
    | addr | Address of breakpoint or watchpoint |
    | kind | Size of breakpoint/watchpoint in bytes |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -1 | Error encountered |
    | -2 | Not supported |

## [◆ ](#ga2aa577d5e55c8b739e2be6187336aaf0)arch\_gdb\_step()

| void arch\_gdb\_step | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Continue with one step.

Continue software execution until reaches the next statement.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
