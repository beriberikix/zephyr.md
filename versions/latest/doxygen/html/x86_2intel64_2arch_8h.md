---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/x86_2intel64_2arch_8h.html
original_path: doxygen/html/x86_2intel64_2arch_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

`#include <[zephyr/arch/x86/intel64/thread.h](arch_2x86_2intel64_2thread_8h_source.md)>`  
`#include <[zephyr/arch/x86/thread_stack.h](arch_2x86_2thread__stack_8h_source.md)>`

[Go to the source code of this file.](x86_2intel64_2arch_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [x86\_esf](structx86__esf.md) |
| struct | [x86\_ssf](structx86__ssf.md) |

| Macros | |
| --- | --- |
| #define | [ARCH\_EXCEPT](#a8d3604770d7735d229e7d2fef4ff590a)(reason\_p) |
| #define | [X86\_RESERVE\_IRQ](#a7b93ddbf458746ef3d189dfd10888077)(irq\_p, name) |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT](#ad0a10d482624ef8d91859f5bcdc2f647)   16 |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_write64](#aed9cf591fb95242f161e6fc8719cf3e3) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_read64](#a7ba6099642d909c50219d174c35f6a94) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#a1496f4f860a99f42e1aee15ce5c9b3e2) (void) |

## Macro Definition Documentation

## [◆ ](#ad0a10d482624ef8d91859f5bcdc2f647)ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT

| #define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT   16 |
| --- |

## [◆ ](#a8d3604770d7735d229e7d2fef4ff590a)ARCH\_EXCEPT

| #define ARCH\_EXCEPT | ( |  | *reason\_p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

\_\_asm\_\_ volatile( \

"movq %[reason], %%rax\n\t" \

"int $32\n\t" \

: \

: [reason] "i" (reason\_p)); \

CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

} while (false)

## [◆ ](#accdf8a59e00ac1c1fcedc18b78be4b8a)ARCH\_IRQ\_CONNECT

| #define ARCH\_IRQ\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *isr\_param\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

[X86\_RESERVE\_IRQ](#a7b93ddbf458746ef3d189dfd10888077)(irq\_p, \_CONCAT(\_irq\_alloc\_fixed, \_\_COUNTER\_\_)); \

arch\_irq\_connect\_dynamic(irq\_p, priority\_p, \

(void (\*)(const void \*))isr\_p, \

isr\_param\_p, flags\_p)

[X86\_RESERVE\_IRQ](#a7b93ddbf458746ef3d189dfd10888077)

#define X86\_RESERVE\_IRQ(irq\_p, name)

**Definition** arch.h:123

## [◆ ](#a7b93ddbf458746ef3d189dfd10888077)X86\_RESERVE\_IRQ

| #define X86\_RESERVE\_IRQ | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

## Function Documentation

## [◆ ](#a1496f4f860a99f42e1aee15ce5c9b3e2)arch\_irq\_lock()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a7ba6099642d909c50219d174c35f6a94)sys\_read64()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_read64 | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aed9cf591fb95242f161e6fc8719cf3e3)sys\_write64()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_write64 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *data*, | | --- | --- | --- | --- | |  |  | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *addr* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel64](dir_1abf87bed33eaf4508c3178cbd4d6168.md)
- [arch.h](x86_2intel64_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
