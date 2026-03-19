---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2arc_2v2_2irq_8h.html
original_path: doxygen/html/arch_2arc_2v2_2irq_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h File Reference

ARCv2 public interrupt handling.
[More...](#details)

`#include <[zephyr/arch/arc/v2/aux_regs.h](aux__regs_8h_source.md)>`  
`#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`

[Go to the source code of this file.](arch_2arc_2v2_2irq_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARC\_MP\_PRIMARY\_CPU\_ID](#a55147bf8ba1fd1bb0beef93b7c21c6c2)   0 |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_IRQ\_DIRECT\_CONNECT](#a875f2b1ca924721fe3854796bd96c2db)(irq\_p, priority\_p, isr\_p, flags\_p) |
|  | Configure a 'direct' static interrupt. |
| #define | [ARCH\_ISR\_DIRECT\_HEADER](#a6c6d57983c066fe8ab21a78f86f7adb3)() |
| #define | [ARCH\_ISR\_DIRECT\_FOOTER](#aa7c471213fa28b3685f153ea2a72cf9d)(swap) |
| #define | [ARCH\_ISR\_DIRECT\_DECLARE](#a5279598e93dd914614a2ae52557be1a5)(name) |

| Functions | |
| --- | --- |
| void | [arch\_irq\_enable](#aa278d630653b33cb339621d725ed295a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [arch\_irq\_disable](#a216d692e87bfba955a60f8e570e127df) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| int | [arch\_irq\_is\_enabled](#a3bd8e963a124421bb372dab4bdc6cd83) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| static void | [arch\_isr\_direct\_header](#a5707c683cd09e9c45a77ac305d9a3513) (void) |
| static void | [arch\_isr\_direct\_footer](#a678e87bf86d19e45c2fcb95ec969465b) (int maybe\_swap) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#a1496f4f860a99f42e1aee15ce5c9b3e2) (void) |
|  | Disable all interrupts on the local CPU. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_irq\_unlock](#a203e02b994beba0d006dad9f6d797c27) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](#adb441b26ed6818fea4ebba6b8853354b) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |

## Detailed Description

ARCv2 public interrupt handling.

ARCv2 kernel interrupt handling interface. Included by arc/arch.h.

## Macro Definition Documentation

## [◆ ](#a55147bf8ba1fd1bb0beef93b7c21c6c2)ARC\_MP\_PRIMARY\_CPU\_ID

| #define ARC\_MP\_PRIMARY\_CPU\_ID   0 |
| --- |

## [◆ ](#accdf8a59e00ac1c1fcedc18b78be4b8a)ARCH\_IRQ\_CONNECT

| #define ARCH\_IRQ\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *isr\_param\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

z\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

}

## [◆ ](#a875f2b1ca924721fe3854796bd96c2db)ARCH\_IRQ\_DIRECT\_CONNECT

| #define ARCH\_IRQ\_DIRECT\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

Z\_ISR\_DECLARE\_DIRECT(irq\_p, [ISR\_FLAG\_DIRECT](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19), isr\_p); \

BUILD\_ASSERT(priority\_p || ![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ARC\_FIRQ) || \

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ARC\_FIRQ\_STACK) && \

![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ARC\_STACK\_CHECKING)), \

"irq priority cannot be set to 0 when CONFIG\_ARC\_FIRQ\_STACK" \

"is not configured or CONFIG\_ARC\_FIRQ\_STACK " \

"and CONFIG\_ARC\_STACK\_CHECKING are configured together"); \

z\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

}

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

[ISR\_FLAG\_DIRECT](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19)

#define ISR\_FLAG\_DIRECT

This interrupt gets put directly in the vector table.

**Definition** sw\_isr\_table.h:180

Configure a 'direct' static interrupt.

When firq has no separate stack(CONFIG\_ARC\_FIRQ\_STACK=N), it's not safe to call C ISR handlers because sp will be switched to bank1's sp which is undefined value. So for this case, the priority cannot be set to 0 but next level 1

When firq has separate stack (CONFIG\_ARC\_FIRQ\_STACK=y) but at the same time stack checking is enabled (CONFIG\_ARC\_STACK\_CHECKING=y) the stack checking can raise stack check exception as sp is switched to firq's stack (bank1's sp). So for this case, the priority cannot be set to 0 but next level 1.

Note that for the above cases, if application still wants to use firq by setting priority to 0. Application can call z\_irq\_priority\_set again. Then it's left to application to handle the details of firq

See include/irq.h for details. All arguments must be computable at build time.

## [◆ ](#a5279598e93dd914614a2ae52557be1a5)ARCH\_ISR\_DIRECT\_DECLARE

| #define ARCH\_ISR\_DIRECT\_DECLARE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static inline int name##\_body(void); \

\_\_attribute\_\_ ((\_ARC\_DIRECT\_ISR\_FUNC\_ATTRIBUTE))void name(void) \

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

[arch\_isr\_direct\_footer](#a678e87bf86d19e45c2fcb95ec969465b)(swap)

[arch\_isr\_direct\_footer](#a678e87bf86d19e45c2fcb95ec969465b)

static void arch\_isr\_direct\_footer(int maybe\_swap)

**Definition** irq.h:98

## [◆ ](#a6c6d57983c066fe8ab21a78f86f7adb3)ARCH\_ISR\_DIRECT\_HEADER

| #define ARCH\_ISR\_DIRECT\_HEADER | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[arch\_isr\_direct\_header](#a5707c683cd09e9c45a77ac305d9a3513)()

[arch\_isr\_direct\_header](#a5707c683cd09e9c45a77ac305d9a3513)

static void arch\_isr\_direct\_header(void)

**Definition** irq.h:91

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

## [◆ ](#a1496f4f860a99f42e1aee15ce5c9b3e2)arch\_irq\_lock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Disable all interrupts on the local CPU.

This routine disables interrupts. It can be called from either interrupt or thread level. This routine returns an architecture-dependent lock-out key representing the "interrupt disable state" prior to the call; this key can be passed to [irq\_unlock()](group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57 "Unlock interrupts.") to re-enable interrupts.

The lock-out key should only be used as the argument to the [irq\_unlock()](group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57 "Unlock interrupts.") API. It should never be used to manually re-enable interrupts or to inspect or manipulate the contents of the source register.

This function can be called recursively: it will return a key to return the state of interrupt locking to the previous level.

WARNINGS Invoking a kernel routine with interrupts locked may result in interrupts being re-enabled for an unspecified period of time. If the called routine blocks, interrupts will be re-enabled while another thread executes, or while the system is idle.

The "interrupt disable state" is an attribute of a thread. Thus, if a thread disables interrupts and subsequently invokes a kernel routine that causes the calling thread to block, the interrupt disable state will be restored when the thread is later rescheduled for execution.

Returns
:   An architecture-dependent lock-out key representing the "interrupt disable state" prior to the call.

## [◆ ](#a203e02b994beba0d006dad9f6d797c27)arch\_irq\_unlock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_irq\_unlock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adb441b26ed6818fea4ebba6b8853354b)arch\_irq\_unlocked()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_irq\_unlocked | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a678e87bf86d19e45c2fcb95ec969465b)arch\_isr\_direct\_footer()

| | void arch\_isr\_direct\_footer | ( | int | *maybe\_swap* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5707c683cd09e9c45a77ac305d9a3513)arch\_isr\_direct\_header()

| | void arch\_isr\_direct\_header | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [irq.h](arch_2arc_2v2_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
