---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2arm_2irq_8h.html
original_path: doxygen/html/arch_2arm_2irq_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h File Reference

ARM AArch32 public interrupt handling.
[More...](#details)

`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](arch_2arm_2irq_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IRQ\_ZERO\_LATENCY](#a1b5d8b88524f2fd81f32ed675c832a57)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Set this interrupt up as a zero-latency IRQ. |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_IRQ\_DIRECT\_CONNECT](#a875f2b1ca924721fe3854796bd96c2db)(irq\_p, priority\_p, isr\_p, flags\_p) |
| #define | [ARCH\_ISR\_DIRECT\_PM](#a491cb79acec18c83b9a61b0b45dfab69)() |
| #define | [ARCH\_ISR\_DIRECT\_HEADER](#a6c6d57983c066fe8ab21a78f86f7adb3)() |
| #define | [ARCH\_ISR\_DIRECT\_FOOTER](#aa7c471213fa28b3685f153ea2a72cf9d)(swap) |
| #define | [ARCH\_ISR\_DIAG\_OFF](#aea327928797d5f8a059ee3578cff9f91) |
| #define | [ARCH\_ISR\_DIAG\_ON](#ad6a5dc7416190e63eb601df2d3eab164) |
| #define | [ARCH\_ISR\_DIRECT\_DECLARE](#a5279598e93dd914614a2ae52557be1a5)(name) |

| Functions | |
| --- | --- |
| void | [arch\_irq\_enable](#aa278d630653b33cb339621d725ed295a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [arch\_irq\_disable](#a216d692e87bfba955a60f8e570e127df) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| int | [arch\_irq\_is\_enabled](#a3bd8e963a124421bb372dab4bdc6cd83) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| static void | [arch\_isr\_direct\_header](#ac8579cbf5edce72a6a4bfbbed3166683) (void) |
| static void | [arch\_isr\_direct\_footer](#a678e87bf86d19e45c2fcb95ec969465b) (int maybe\_swap) |

## Detailed Description

ARM AArch32 public interrupt handling.

ARM AArch32-specific kernel interrupt handling interface. Included by [arm/arch.h](arm_2arch_8h.md "ARM AArch32 specific kernel interface header.").

## Macro Definition Documentation

## [◆ ](#accdf8a59e00ac1c1fcedc18b78be4b8a)ARCH\_IRQ\_CONNECT

| #define ARCH\_IRQ\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *isr\_param\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

BUILD\_ASSERT([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ZERO\_LATENCY\_IRQS) || !(flags\_p & [IRQ\_ZERO\_LATENCY](#a1b5d8b88524f2fd81f32ed675c832a57)), \

"ZLI interrupt registered but feature is disabled"); \

\_CHECK\_PRIO(priority\_p, flags\_p) \

Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

z\_arm\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

}

[IRQ\_ZERO\_LATENCY](#a1b5d8b88524f2fd81f32ed675c832a57)

#define IRQ\_ZERO\_LATENCY

Set this interrupt up as a zero-latency IRQ.

**Definition** irq.h:86

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

## [◆ ](#a875f2b1ca924721fe3854796bd96c2db)ARCH\_IRQ\_DIRECT\_CONNECT

| #define ARCH\_IRQ\_DIRECT\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

BUILD\_ASSERT([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ZERO\_LATENCY\_IRQS) || !(flags\_p & [IRQ\_ZERO\_LATENCY](#a1b5d8b88524f2fd81f32ed675c832a57)), \

"ZLI interrupt registered but feature is disabled"); \

\_CHECK\_PRIO(priority\_p, flags\_p) \

Z\_ISR\_DECLARE\_DIRECT(irq\_p, [ISR\_FLAG\_DIRECT](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19), isr\_p); \

z\_arm\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

}

[ISR\_FLAG\_DIRECT](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19)

#define ISR\_FLAG\_DIRECT

This interrupt gets put directly in the vector table.

**Definition** sw\_isr\_table.h:180

## [◆ ](#aea327928797d5f8a059ee3578cff9f91)ARCH\_ISR\_DIAG\_OFF

| #define ARCH\_ISR\_DIAG\_OFF |
| --- |

## [◆ ](#ad6a5dc7416190e63eb601df2d3eab164)ARCH\_ISR\_DIAG\_ON

| #define ARCH\_ISR\_DIAG\_ON |
| --- |

## [◆ ](#a5279598e93dd914614a2ae52557be1a5)ARCH\_ISR\_DIRECT\_DECLARE

| #define ARCH\_ISR\_DIRECT\_DECLARE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static inline int name##\_body(void); \

ARCH\_ISR\_DIAG\_OFF \

\_\_attribute\_\_ ((interrupt ("IRQ"))) void name(void) \

{ \

int check\_reschedule; \

ISR\_DIRECT\_HEADER(); \

check\_reschedule = name##\_body(); \

ISR\_DIRECT\_FOOTER(check\_reschedule); \

} \

ARCH\_ISR\_DIAG\_ON \

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

## [◆ ](#a1b5d8b88524f2fd81f32ed675c832a57)IRQ\_ZERO\_LATENCY

| #define IRQ\_ZERO\_LATENCY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Set this interrupt up as a zero-latency IRQ.

If CONFIG\_ZERO\_LATENCY\_LEVELS is 1 it has a fixed hardware priority level (discarding what was supplied in the interrupt's priority argument). If CONFIG\_ZERO\_LATENCY\_LEVELS is greater 1 it has the priority level assigned by the argument. The interrupt will run even if [irq\_lock()](group__isr__apis.md#ga19fdde73c3b02fcca6cf1d1e67631228 "Lock interrupts.") is active. Be careful!

## Function Documentation

## [◆ ](#a216d692e87bfba955a60f8e570e127df)arch\_irq\_disable()

| | void arch\_irq\_disable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa278d630653b33cb339621d725ed295a)arch\_irq\_enable()

| | void arch\_irq\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3bd8e963a124421bb372dab4bdc6cd83)arch\_irq\_is\_enabled()

| | int arch\_irq\_is\_enabled | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a678e87bf86d19e45c2fcb95ec969465b)arch\_isr\_direct\_footer()

| | void arch\_isr\_direct\_footer | ( | int | *maybe\_swap* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac8579cbf5edce72a6a4bfbbed3166683)arch\_isr\_direct\_header()

| | void arch\_isr\_direct\_header | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [irq.h](arch_2arm_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
