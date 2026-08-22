---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/rx_2arch_8h.html
original_path: doxygen/html/rx_2arch_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

Renesas RX specific kernel interface header.
[More...](#details)

`#include <[zephyr/arch/rx/exception.h](rx_2exception_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/arch/rx/thread.h](arch_2rx_2thread_8h_source.md)>`  
`#include <[zephyr/arch/rx/misc.h](rx_2misc_8h_source.md)>`  
`#include <[zephyr/arch/rx/arch_inlines.h](rx_2arch__inlines_8h_source.md)>`  
`#include <[zephyr/arch/rx/error.h](include_2zephyr_2arch_2rx_2error_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_bitops.h](sys__bitops_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_io.h](arch_2common_2sys__io_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <[zephyr/kernel_structs.h](kernel__structs_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`

[Go to the source code of this file.](rx_2arch_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   4 |
| #define | [REG](#a1e07bd4d6286e062b88f8e5c839b1daa)(addr) |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_ISR\_DIRECT\_HEADER](#a6c6d57983c066fe8ab21a78f86f7adb3)() |
| #define | [ARCH\_ISR\_DIRECT\_FOOTER](#ae95db3ae6bb31cc46eb6f500341ad974)(check\_reschedule) |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#a1496f4f860a99f42e1aee15ce5c9b3e2) (void) |
| static void | [arch\_irq\_unlock](#aa2b2745d8e99b8730b44805f4d3bbf05) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](#a1b827afafc622d412962f568b78726dc) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \* | [arch\_curr\_cpu](#a3e8a7515c0c3b8de5a037ce5997c73b0) (void) |

## Detailed Description

Renesas RX specific kernel interface header.

This header contains the Renesas RX specific kernel interface. It is included by the kernel interface architecture-abstraction header (include/zephyr/arch/cpu.h).

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

Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

z\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

}

## [◆ ](#ae95db3ae6bb31cc46eb6f500341ad974)ARCH\_ISR\_DIRECT\_FOOTER

| #define ARCH\_ISR\_DIRECT\_FOOTER | ( |  | *check\_reschedule* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_STACK\_SENTINEL)) { \

z\_check\_stack\_sentinel(); \

} \

irq\_lock(); \

if (check\_reschedule && \_kernel.cpus[0].nested == 1) { \

if (\_kernel.cpus->current->base.prio >= 0 || \

CONFIG\_NUM\_METAIRQ\_PRIORITIES > 0) { \

if (\_kernel.ready\_q.cache != \_kernel.cpus->current) { \

z\_rx\_irq\_exit(); \

} \

} \

} \

\_kernel.cpus[0].nested--; \

}

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

## [◆ ](#a6c6d57983c066fe8ab21a78f86f7adb3)ARCH\_ISR\_DIRECT\_HEADER

| #define ARCH\_ISR\_DIRECT\_HEADER | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

{ \

\_kernel.cpus[0].nested++; \

}

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   4 |
| --- |

## [◆ ](#a1e07bd4d6286e062b88f8e5c839b1daa)REG

| #define REG | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\*(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(addr))

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

## Function Documentation

## [◆ ](#a3e8a7515c0c3b8de5a037ce5997c73b0)arch\_curr\_cpu()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \* arch\_curr\_cpu | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a1496f4f860a99f42e1aee15ce5c9b3e2)arch\_irq\_lock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa2b2745d8e99b8730b44805f4d3bbf05)arch\_irq\_unlock()

| | void arch\_irq\_unlock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a1b827afafc622d412962f568b78726dc)arch\_irq\_unlocked()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_irq\_unlocked | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [rx](dir_eb52b7f9d95392aedf108916f743bdaf.md)
- [arch.h](rx_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
