---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mips_2arch_8h.html
original_path: doxygen/html/mips_2arch_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

`#include <[zephyr/arch/mips/thread.h](arch_2mips_2thread_8h_source.md)>`  
`#include <[zephyr/arch/mips/exception.h](mips_2exception_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_bitops.h](sys__bitops_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_io.h](arch_2common_2sys__io_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <mips/mipsregs.h>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](mips_2arch_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   16 |
| #define | [OP\_LOADREG](#a19279c7228621d3232e740aa69de27c3)   lw |
| #define | [OP\_STOREREG](#ab32daf0cef581b53f3553876d4db2714)   sw |
| #define | [CP0\_STATUS\_DEF\_RESTORE](#a26b87470892333da53ff3ecfb4d9226d)   (ST0\_EXL | ST0\_IE) |
| #define | [STACK\_ROUND\_UP](#a49668abaf6448b75881e21c6a7d4aac6)(x) |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
|  | Configure a static interrupt. |

| Functions | |
| --- | --- |
| void | [arch\_irq\_enable](#aa278d630653b33cb339621d725ed295a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [arch\_irq\_disable](#a216d692e87bfba955a60f8e570e127df) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| int | [arch\_irq\_is\_enabled](#a3bd8e963a124421bb372dab4bdc6cd83) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#a1496f4f860a99f42e1aee15ce5c9b3e2) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_irq\_unlock](#a203e02b994beba0d006dad9f6d797c27) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](#adb441b26ed6818fea4ebba6b8853354b) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_nop](#a0af98dc5138e02248173c30b8f07210f) (void) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_cycle\_get\_32](#a42dcd1878309a82246dbfa26510f868a) (void) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_k\_cycle\_get\_32](#a9ee9f897ec750957de45bf8d43349d5e) (void) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_clock\_cycle\_get\_64](#a25328a181bd0229ef5110c15e8452fc1) (void) |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_k\_cycle\_get\_64](#acc1ed8d949f694a1d39e389334caf971) (void) |

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

}

Configure a static interrupt.

All arguments must be computable by the compiler at build time.

Parameters
:   | irq\_p | IRQ line number |
    | --- | --- |
    | priority\_p | Interrupt priority |
    | isr\_p | Interrupt service routine |
    | isr\_param\_p | ISR parameter |
    | flags\_p | IRQ options |

Returns
:   The vector assigned to this interrupt

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   16 |
| --- |

## [◆ ](#a26b87470892333da53ff3ecfb4d9226d)CP0\_STATUS\_DEF\_RESTORE

| #define CP0\_STATUS\_DEF\_RESTORE   (ST0\_EXL | ST0\_IE) |
| --- |

## [◆ ](#a19279c7228621d3232e740aa69de27c3)OP\_LOADREG

| #define OP\_LOADREG   lw |
| --- |

## [◆ ](#ab32daf0cef581b53f3553876d4db2714)OP\_STOREREG

| #define OP\_STOREREG   sw |
| --- |

## [◆ ](#a49668abaf6448b75881e21c6a7d4aac6)STACK\_ROUND\_UP

| #define STACK\_ROUND\_UP | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(x, [ARCH\_STACK\_PTR\_ALIGN](arc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3))

[ARCH\_STACK\_PTR\_ALIGN](arc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)

#define ARCH\_STACK\_PTR\_ALIGN

**Definition** arch.h:98

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:322

## Function Documentation

## [◆ ](#a216d692e87bfba955a60f8e570e127df)arch\_irq\_disable()

| void arch\_irq\_disable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa278d630653b33cb339621d725ed295a)arch\_irq\_enable()

| void arch\_irq\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a3bd8e963a124421bb372dab4bdc6cd83)arch\_irq\_is\_enabled()

| int arch\_irq\_is\_enabled | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a1496f4f860a99f42e1aee15ce5c9b3e2)arch\_irq\_lock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_irq\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a203e02b994beba0d006dad9f6d797c27)arch\_irq\_unlock()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_irq\_unlock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adb441b26ed6818fea4ebba6b8853354b)arch\_irq\_unlocked()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_irq\_unlocked | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9ee9f897ec750957de45bf8d43349d5e)arch\_k\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_k\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acc1ed8d949f694a1d39e389334caf971)arch\_k\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_k\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0af98dc5138e02248173c30b8f07210f)arch\_nop()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_nop | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a42dcd1878309a82246dbfa26510f868a)sys\_clock\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_clock\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a25328a181bd0229ef5110c15e8452fc1)sys\_clock\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_clock\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [mips](dir_fc8c8ea71cc5b300c3fa15bb05243853.md)
- [arch.h](mips_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
