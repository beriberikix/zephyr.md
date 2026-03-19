---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sparc_2arch_8h.html
original_path: doxygen/html/sparc_2arch_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

SPARC specific kernel interface header This header contains the SPARC specific kernel interface.
[More...](#details)

`#include <[zephyr/arch/sparc/exception.h](sparc_2exception_8h_source.md)>`  
`#include <[zephyr/arch/sparc/thread.h](arch_2sparc_2thread_8h_source.md)>`  
`#include <[zephyr/arch/sparc/sparc.h](sparc_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_bitops.h](sys__bitops_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_io.h](arch_2common_2sys__io_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <soc.h>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](sparc_2arch_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   8 |
| #define | [SPARC\_SW\_TRAP\_FLUSH\_WINDOWS](#af489f2ab54555e99f7e0351e95bdadda)   0x03 |
| #define | [SPARC\_SW\_TRAP\_SET\_PIL](#a0db46ead17cf040d99fa5adc10aa1274)   0x09 |
| #define | [SPARC\_SW\_TRAP\_EXCEPT](#a2e78f31907142407cf66518f840ca5e9)   0x0F |
| #define | [STACK\_ROUND\_UP](#a49668abaf6448b75881e21c6a7d4aac6)(x) |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_EXCEPT](#a8d3604770d7735d229e7d2fef4ff590a)(reason\_p) |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_irq\_lock](#a1496f4f860a99f42e1aee15ce5c9b3e2) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_irq\_unlock](#a203e02b994beba0d006dad9f6d797c27) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](#adb441b26ed6818fea4ebba6b8853354b) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_nop](#a0af98dc5138e02248173c30b8f07210f) (void) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_cycle\_get\_32](#a42dcd1878309a82246dbfa26510f868a) (void) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_k\_cycle\_get\_32](#a9ee9f897ec750957de45bf8d43349d5e) (void) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_clock\_cycle\_get\_64](#a25328a181bd0229ef5110c15e8452fc1) (void) |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_k\_cycle\_get\_64](#acc1ed8d949f694a1d39e389334caf971) (void) |

## Detailed Description

SPARC specific kernel interface header This header contains the SPARC specific kernel interface.

It is included by the generic kernel interface header ([arch/cpu.h](cpu_8h.md))

## Macro Definition Documentation

## [◆ ](#a8d3604770d7735d229e7d2fef4ff590a)ARCH\_EXCEPT

| #define ARCH\_EXCEPT | ( |  | *reason\_p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_g1 \_\_asm\_\_("g1") = reason\_p; \

\

\_\_asm\_\_ volatile ( \

"ta %[vector]\n\t" \

: \

: [vector] "i" ([SPARC\_SW\_TRAP\_EXCEPT](#a2e78f31907142407cf66518f840ca5e9)), "r" (\_g1) \

: "memory" \

); \

CODE\_UNREACHABLE; \

} while (false)

[SPARC\_SW\_TRAP\_EXCEPT](#a2e78f31907142407cf66518f840ca5e9)

#define SPARC\_SW\_TRAP\_EXCEPT

**Definition** arch.h:38

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

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

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   8 |
| --- |

## [◆ ](#a2e78f31907142407cf66518f840ca5e9)SPARC\_SW\_TRAP\_EXCEPT

| #define SPARC\_SW\_TRAP\_EXCEPT   0x0F |
| --- |

## [◆ ](#af489f2ab54555e99f7e0351e95bdadda)SPARC\_SW\_TRAP\_FLUSH\_WINDOWS

| #define SPARC\_SW\_TRAP\_FLUSH\_WINDOWS   0x03 |
| --- |

## [◆ ](#a0db46ead17cf040d99fa5adc10aa1274)SPARC\_SW\_TRAP\_SET\_PIL

| #define SPARC\_SW\_TRAP\_SET\_PIL   0x09 |
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
- [sparc](dir_0b6b538994b3c7630127059eac21a61b.md)
- [arch.h](sparc_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
