---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2riscv_2irq_8h.html
original_path: doxygen/html/arch_2riscv_2irq_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h File Reference

RISC-V public interrupt handling.
[More...](#details)

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](arch_2riscv_2irq_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RISCV\_EXC\_ECALLU](#a863dbd3dec399c9997dcabd96fe72330)   8 |
| #define | [RISCV\_EXC\_ECALLM](#a29b9547cc078c8cb9ddcd234119df2dc)   11 |
|  | Environment Call from M-mode. |
| #define | [RISCV\_IRQ\_MSOFT](#a720c7c1a9f6cea6575635614882c64f2)   3 |
|  | Machine Software Interrupt. |
| #define | [RISCV\_IRQ\_MEXT](#aeb7cd87a790fd623f63e098115da5d48)   11 |
|  | Machine External Interrupt. |
| #define | [RISCV\_MCAUSE\_IRQ\_POS](#ae8e815069f84cc2c7e4f7c98046c7726)   31U |
| #define | [RISCV\_MCAUSE\_IRQ\_BIT](#a9a0d46c6f9f854a12aa13111ec9bc1bc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RISCV\_MCAUSE\_IRQ\_POS](#ae8e815069f84cc2c7e4f7c98046c7726)) |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_IRQ\_DIRECT\_CONNECT](#a875f2b1ca924721fe3854796bd96c2db)(irq\_p, priority\_p, isr\_p, flags\_p) |
| #define | [ARCH\_ISR\_DIRECT\_HEADER](#a6c6d57983c066fe8ab21a78f86f7adb3)() |
| #define | [ARCH\_ISR\_DIRECT\_FOOTER](#aa7c471213fa28b3685f153ea2a72cf9d)(swap) |
| #define | [ARCH\_ISR\_DIRECT\_DECLARE](#a5279598e93dd914614a2ae52557be1a5)(name) |

| Functions | |
| --- | --- |
| void | [arch\_irq\_enable](#aa278d630653b33cb339621d725ed295a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [arch\_irq\_disable](#a216d692e87bfba955a60f8e570e127df) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| int | [arch\_irq\_is\_enabled](#a3bd8e963a124421bb372dab4bdc6cd83) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| static void | [arch\_isr\_direct\_header](#ac8579cbf5edce72a6a4bfbbed3166683) (void) |
| static void | [arch\_isr\_direct\_footer](#a13a88acdff251283bf6f364e4393adaf) (int swap) |

## Detailed Description

RISC-V public interrupt handling.

RISC-V-specific kernel interrupt handling interface.

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

Z\_ISR\_DECLARE(irq\_p + CONFIG\_RISCV\_RESERVED\_IRQ\_ISR\_TABLES\_OFFSET, \

0, isr\_p, isr\_param\_p); \

z\_riscv\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

}

## [◆ ](#a875f2b1ca924721fe3854796bd96c2db)ARCH\_IRQ\_DIRECT\_CONNECT

| #define ARCH\_IRQ\_DIRECT\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

Z\_ISR\_DECLARE\_DIRECT(irq\_p + CONFIG\_RISCV\_RESERVED\_IRQ\_ISR\_TABLES\_OFFSET, \

[ISR\_FLAG\_DIRECT](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19), isr\_p); \

z\_riscv\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

z\_riscv\_irq\_vector\_set(irq\_p); \

}

[ISR\_FLAG\_DIRECT](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19)

#define ISR\_FLAG\_DIRECT

This interrupt gets put directly in the vector table.

**Definition** sw\_isr\_table.h:180

## [◆ ](#a5279598e93dd914614a2ae52557be1a5)ARCH\_ISR\_DIRECT\_DECLARE

| #define ARCH\_ISR\_DIRECT\_DECLARE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static inline int name##\_body(void); \

\_\_attribute\_\_ ((interrupt)) void name(void) \

{ \

ISR\_DIRECT\_HEADER(); \

name##\_body(); \

ISR\_DIRECT\_FOOTER(0); \

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

## [◆ ](#a29b9547cc078c8cb9ddcd234119df2dc)RISCV\_EXC\_ECALLM

| #define RISCV\_EXC\_ECALLM   11 |
| --- |

Environment Call from M-mode.

## [◆ ](#a863dbd3dec399c9997dcabd96fe72330)RISCV\_EXC\_ECALLU

| #define RISCV\_EXC\_ECALLU   8 |
| --- |

## [◆ ](#aeb7cd87a790fd623f63e098115da5d48)RISCV\_IRQ\_MEXT

| #define RISCV\_IRQ\_MEXT   11 |
| --- |

Machine External Interrupt.

## [◆ ](#a720c7c1a9f6cea6575635614882c64f2)RISCV\_IRQ\_MSOFT

| #define RISCV\_IRQ\_MSOFT   3 |
| --- |

Machine Software Interrupt.

## [◆ ](#a9a0d46c6f9f854a12aa13111ec9bc1bc)RISCV\_MCAUSE\_IRQ\_BIT

| #define RISCV\_MCAUSE\_IRQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RISCV\_MCAUSE\_IRQ\_POS](#ae8e815069f84cc2c7e4f7c98046c7726)) |
| --- |

## [◆ ](#ae8e815069f84cc2c7e4f7c98046c7726)RISCV\_MCAUSE\_IRQ\_POS

| #define RISCV\_MCAUSE\_IRQ\_POS   31U |
| --- |

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

## [◆ ](#a13a88acdff251283bf6f364e4393adaf)arch\_isr\_direct\_footer()

| | void arch\_isr\_direct\_footer | ( | int | *swap* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac8579cbf5edce72a6a4bfbbed3166683)arch\_isr\_direct\_header()

| | void arch\_isr\_direct\_header | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [irq.h](arch_2riscv_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
