---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/x86_2ia32_2arch_8h.html
original_path: doxygen/html/x86_2ia32_2arch_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

IA-32 specific kernel interface header This header contains the IA-32 specific kernel interface.
[More...](#details)

`#include "[sys_io.h](arch_2x86_2ia32_2sys__io_8h_source.md)"`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/kernel_structs.h](kernel__structs_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/arch/x86/ia32/exception.h](x86_2ia32_2exception_8h_source.md)>`  
`#include <[zephyr/arch/x86/ia32/gdbstub.h](arch_2x86_2ia32_2gdbstub_8h_source.md)>`  
`#include <[zephyr/arch/x86/ia32/thread.h](arch_2x86_2ia32_2thread_8h_source.md)>`  
`#include <[zephyr/arch/x86/ia32/syscall.h](arch_2x86_2ia32_2syscall_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/arch/common/addr_types.h](addr__types_8h_source.md)>`  
`#include <[zephyr/arch/x86/ia32/segmentation.h](segmentation_8h_source.md)>`  
`#include <[zephyr/pm/pm.h](pm_8h_source.md)>`

[Go to the source code of this file.](x86_2ia32_2arch_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [s\_isrList](structs__isrList.md) |

| Macros | |
| --- | --- |
| #define | [CODE\_SEG](#a01cd8f711fd0961b75a23e9d4642d7c3)   0x08 |
| #define | [DATA\_SEG](#aee584332ca956b4e1167180bf9a456bb)   0x10 |
| #define | [MAIN\_TSS](#a5817f0b628919c0d0b092b2a961187e6)   0x18 |
| #define | [DF\_TSS](#a8f9b184e3ebb59e9ec8c62b187b5ad4d)   0x20 |
| #define | [GS\_TLS\_SEG](#abe9fa73b285cb69f2d541fbfd62923fc)   (0x38 | 0x03) |
| #define | [MK\_ISR\_NAME](#a9de710989afc64c692b4366e89c42e9b)(x) |
|  | Macro used internally by NANO\_CPU\_INT\_REGISTER and NANO\_CPU\_INT\_REGISTER\_ASM. |
| #define | [NANO\_CPU\_INT\_REGISTER](#aa4db2c24f5de7f8bae4a0f290fb70456)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), n, p, v, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Connect a routine to an interrupt vector. |
| #define | [IRQSTUBS\_TEXT\_SECTION](#a745054d50f7d95a9cfdb394521cb407f)   ".text.irqstubs" |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_IRQ\_DIRECT\_CONNECT](#a875f2b1ca924721fe3854796bd96c2db)(irq\_p, priority\_p, isr\_p, flags\_p) |
| #define | [ARCH\_ISR\_DIRECT\_PM](#a491cb79acec18c83b9a61b0b45dfab69)() |
| #define | [ARCH\_ISR\_DIRECT\_HEADER](#a6c6d57983c066fe8ab21a78f86f7adb3)() |
| #define | [ARCH\_ISR\_DIRECT\_FOOTER](#aa7c471213fa28b3685f153ea2a72cf9d)(swap) |
| #define | [ARCH\_ISR\_DIRECT\_DECLARE](#a5279598e93dd914614a2ae52557be1a5)(name) |
| #define | [NANO\_SOFT\_IRQ](#ae52cccc5fa73fafe5a7fb60accb11e35)   (([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int) (-1)) |
|  | The NANO\_SOFT\_IRQ macro must be used as the value for the *irq* parameter to NANO\_CPU\_INT\_REGISTER when connecting to an interrupt that does not correspond to any IRQ line (such as spurious vector or SW IRQ). |
| #define | [ARCH\_EXCEPT](#a8d3604770d7735d229e7d2fef4ff590a)(reason\_p) |
| #define | [ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT](#ad0a10d482624ef8d91859f5bcdc2f647)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(void \*)) |

| Typedefs | |
| --- | --- |
| typedef struct [s\_isrList](structs__isrList.md) | [ISR\_LIST](#abd14415ccf779280bd7eac3974b6a378) |

| Functions | |
| --- | --- |
| static void | [arch\_isr\_direct\_header](#ac8579cbf5edce72a6a4bfbbed3166683) (void) |
| void | [arch\_isr\_direct\_footer\_swap](#a4ced4d5bdb1d0f3d069d9384615ed394) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static void | [arch\_isr\_direct\_footer](#a13a88acdff251283bf6f364e4393adaf) (int swap) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#a1496f4f860a99f42e1aee15ce5c9b3e2) (void) |

## Detailed Description

IA-32 specific kernel interface header This header contains the IA-32 specific kernel interface.

It is included by the generic kernel interface header (include/arch/cpu.h)

## Macro Definition Documentation

## [◆ ](#ad0a10d482624ef8d91859f5bcdc2f647)ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT

| #define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(void \*)) |
| --- |

## [◆ ](#a8d3604770d7735d229e7d2fef4ff590a)ARCH\_EXCEPT

| #define ARCH\_EXCEPT | ( |  | *reason\_p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

\_\_asm\_\_ volatile( \

"push %[reason]\n\t" \

"int %[vector]\n\t" \

: \

: [vector] "i" (Z\_X86\_OOPS\_VECTOR), \

[reason] "i" (reason\_p)); \

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

{ \

\_\_asm\_\_ \_\_volatile\_\_( \

".pushsection .intList\n\t" \

".long %c[isr]\_irq%c[irq]\_stub\n\t" /\* ISR\_LIST.fnc \*/ \

".long %c[irq]\n\t" /\* ISR\_LIST.irq \*/ \

".long %c[priority]\n\t" /\* ISR\_LIST.priority \*/ \

".long %c[vector]\n\t" /\* ISR\_LIST.vec \*/ \

".long 0\n\t" /\* ISR\_LIST.dpl \*/ \

".long 0\n\t" /\* ISR\_LIST.tss \*/ \

".popsection\n\t" \

".pushsection " [IRQSTUBS\_TEXT\_SECTION](#a745054d50f7d95a9cfdb394521cb407f) "\n\t" \

".global %c[isr]\_irq%c[irq]\_stub\n\t" \

"%c[isr]\_irq%c[irq]\_stub:\n\t" \

"pushl %[isr\_param]\n\t" \

"pushl %[isr]\n\t" \

"jmp \_interrupt\_enter\n\t" \

".popsection\n\t" \

: \

: [isr] "i" (isr\_p), \

[isr\_param] "i" (isr\_param\_p), \

[priority] "i" (priority\_p), \

[vector] "i" \_VECTOR\_ARG(irq\_p), \

[irq] "i" (irq\_p)); \

z\_irq\_controller\_irq\_config(Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq\_p), (irq\_p), \

(flags\_p)); \

}

[IRQSTUBS\_TEXT\_SECTION](#a745054d50f7d95a9cfdb394521cb407f)

#define IRQSTUBS\_TEXT\_SECTION

**Definition** arch.h:177

## [◆ ](#a875f2b1ca924721fe3854796bd96c2db)ARCH\_IRQ\_DIRECT\_CONNECT

| #define ARCH\_IRQ\_DIRECT\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

NANO\_CPU\_INT\_REGISTER(isr\_p, irq\_p, priority\_p, -1, 0); \

z\_irq\_controller\_irq\_config(Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq\_p), (irq\_p), \

(flags\_p)); \

}

## [◆ ](#a5279598e93dd914614a2ae52557be1a5)ARCH\_ISR\_DIRECT\_DECLARE

| #define ARCH\_ISR\_DIRECT\_DECLARE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static inline int name##\_body(void); \

\_\_attribute\_\_ ((interrupt)) void name(void \*stack\_frame) \

{ \

ARG\_UNUSED(stack\_frame); \

int check\_reschedule; \

ISR\_DIRECT\_HEADER(); \

check\_reschedule = name##\_body(); \

ISR\_DIRECT\_FOOTER(check\_reschedule); \

} \

static inline int name##\_body(void)

## [◆ ](#aa7c471213fa28b3685f153ea2a72cf9d)ARCH\_ISR\_DIRECT\_FOOTER

| #define ARCH\_ISR\_DIRECT\_FOOTER | ( |  | *swap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)(swap)

[arch\_isr\_direct\_footer](arch_2arc_2v2_2irq_8h.md#a678e87bf86d19e45c2fcb95ec969465b)

static void arch\_isr\_direct\_footer(int maybe\_swap)

**Definition** irq.h:98

## [◆ ](#a6c6d57983c066fe8ab21a78f86f7adb3)ARCH\_ISR\_DIRECT\_HEADER

| #define ARCH\_ISR\_DIRECT\_HEADER | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)()

[arch\_isr\_direct\_header](arch_2arc_2v2_2irq_8h.md#a5707c683cd09e9c45a77ac305d9a3513)

static void arch\_isr\_direct\_header(void)

**Definition** irq.h:91

## [◆ ](#a491cb79acec18c83b9a61b0b45dfab69)ARCH\_ISR\_DIRECT\_PM

| #define ARCH\_ISR\_DIRECT\_PM | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

do { } while (false)

## [◆ ](#a01cd8f711fd0961b75a23e9d4642d7c3)CODE\_SEG

| #define CODE\_SEG   0x08 |
| --- |

## [◆ ](#aee584332ca956b4e1167180bf9a456bb)DATA\_SEG

| #define DATA\_SEG   0x10 |
| --- |

## [◆ ](#a8f9b184e3ebb59e9ec8c62b187b5ad4d)DF\_TSS

| #define DF\_TSS   0x20 |
| --- |

## [◆ ](#abe9fa73b285cb69f2d541fbfd62923fc)GS\_TLS\_SEG

| #define GS\_TLS\_SEG   (0x38 | 0x03) |
| --- |

## [◆ ](#a745054d50f7d95a9cfdb394521cb407f)IRQSTUBS\_TEXT\_SECTION

| #define IRQSTUBS\_TEXT\_SECTION   ".text.irqstubs" |
| --- |

## [◆ ](#a5817f0b628919c0d0b092b2a961187e6)MAIN\_TSS

| #define MAIN\_TSS   0x18 |
| --- |

## [◆ ](#a9de710989afc64c692b4366e89c42e9b)MK\_ISR\_NAME

| #define MK\_ISR\_NAME | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_isr\_\_##x

Macro used internally by NANO\_CPU\_INT\_REGISTER and NANO\_CPU\_INT\_REGISTER\_ASM.

Not meant to be used explicitly by platform, driver or application code.

## [◆ ](#aa4db2c24f5de7f8bae4a0f290fb70456)NANO\_CPU\_INT\_REGISTER

| #define NANO\_CPU\_INT\_REGISTER | ( |  | *[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)*, |
| --- | --- | --- | --- |
|  |  |  | *n*, |
|  |  |  | *p*, |
|  |  |  | *v*, |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)* ) |

**Value:**

static [ISR\_LIST](#abd14415ccf779280bd7eac3974b6a378) \_\_attribute\_\_((section(".intList"))) \

\_\_attribute\_\_((used)) [MK\_ISR\_NAME](#a9de710989afc64c692b4366e89c42e9b)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) = \

{ \

.fnc = &([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)), \

.irq = (n), \

.priority = (p), \

.vec = (v), \

.dpl = ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)), \

.tss = 0 \

}

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[MK\_ISR\_NAME](#a9de710989afc64c692b4366e89c42e9b)

#define MK\_ISR\_NAME(x)

Macro used internally by NANO\_CPU\_INT\_REGISTER and NANO\_CPU\_INT\_REGISTER\_ASM.

**Definition** arch.h:59

[ISR\_LIST](#abd14415ccf779280bd7eac3974b6a378)

struct s\_isrList ISR\_LIST

Connect a routine to an interrupt vector.

This macro "connects" the specified routine, *r*, to the specified interrupt vector, *v* using the descriptor privilege level *d*. On the IA-32 architecture, an interrupt vector is a value from 0 to 255. This macro populates the special intList section with the address of the routine, the vector number and the descriptor privilege level. The genIdt tool then picks up this information and generates an actual IDT entry with this information properly encoded.

The *d* argument specifies the privilege level for the interrupt-gate descriptor; (hardware) interrupts and exceptions should specify a level of 0, whereas handlers for user-mode software generated interrupts should specify 3.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Routine to be connected |
    | --- | --- |
    | n | IRQ number |
    | p | IRQ priority |
    | v | Interrupt Vector |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Descriptor Privilege Level |

## [◆ ](#ae52cccc5fa73fafe5a7fb60accb11e35)NANO\_SOFT\_IRQ

| #define NANO\_SOFT\_IRQ   (([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int) (-1)) |
| --- |

The NANO\_SOFT\_IRQ macro must be used as the value for the *irq* parameter to NANO\_CPU\_INT\_REGISTER when connecting to an interrupt that does not correspond to any IRQ line (such as spurious vector or SW IRQ).

## Typedef Documentation

## [◆ ](#abd14415ccf779280bd7eac3974b6a378)ISR\_LIST

| typedef struct [s\_isrList](structs__isrList.md) [ISR\_LIST](#abd14415ccf779280bd7eac3974b6a378) |
| --- |

## Function Documentation

## [◆ ](#a1496f4f860a99f42e1aee15ce5c9b3e2)arch\_irq\_lock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a13a88acdff251283bf6f364e4393adaf)arch\_isr\_direct\_footer()

| | void arch\_isr\_direct\_footer | ( | int | *swap* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4ced4d5bdb1d0f3d069d9384615ed394)arch\_isr\_direct\_footer\_swap()

| void arch\_isr\_direct\_footer\_swap | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac8579cbf5edce72a6a4bfbbed3166683)arch\_isr\_direct\_header()

| | void arch\_isr\_direct\_header | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [arch.h](x86_2ia32_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
