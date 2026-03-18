---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/xtensa_2arch_8h.html
original_path: doxygen/html/xtensa_2arch_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

Xtensa specific kernel interface header This header contains the Xtensa specific kernel interface.
[More...](#details)

`#include <[zephyr/irq.h](irq_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_bitops.h](sys__bitops_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_io.h](arch_2common_2sys__io_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <[zephyr/arch/xtensa/syscall.h](arch_2xtensa_2syscall_8h_source.md)>`  
`#include <[zephyr/arch/xtensa/thread.h](arch_2xtensa_2thread_8h_source.md)>`  
`#include <[zephyr/arch/xtensa/irq.h](arch_2xtensa_2irq_8h_source.md)>`  
`#include <xtensa/config/core.h>`  
`#include <[zephyr/arch/common/addr_types.h](addr__types_8h_source.md)>`  
`#include <[zephyr/arch/xtensa/gdbstub.h](arch_2xtensa_2gdbstub_8h_source.md)>`  
`#include <[zephyr/debug/sparse.h](sparse_8h_source.md)>`  
`#include <[zephyr/arch/xtensa/thread_stack.h](arch_2xtensa_2thread__stack_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/drivers/timer/system_timer.h](system__timer_8h_source.md)>`  
`#include <[zephyr/arch/xtensa/xtensa_mmu.h](xtensa__mmu_8h_source.md)>`  
`#include <[zephyr/arch/xtensa/exception.h](xtensa_2exception_8h_source.md)>`  
`#include <syscalls/arch.h>`

[Go to the source code of this file.](xtensa_2arch_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arch\_mem\_domain](structarch__mem__domain.md) |

| Macros | |
| --- | --- |
| #define | [ARCH\_EXCEPT](#a8d3604770d7735d229e7d2fef4ff590a)(reason\_p) |
| #define | [ARCH\_IRQ\_CONNECT](#accdf8a59e00ac1c1fcedc18b78be4b8a)(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
| #define | [ARCH\_XTENSA\_SET\_RPO\_TLB](#a835f1838cf0cec9c6a16bacc62436f0f)() |
|  | Setup RPO TLB registers. |

| Functions | |
| --- | --- |
| void | [xtensa\_arch\_except](#a789f894256925071f3448cda889abcf5) (int reason\_p) |
|  | Generate hardware exception. |
| void | [xtensa\_arch\_kernel\_oops](#a31f0ccadfc2a2afa0e985d74a0e4c2e9) (int reason\_p, void \*ssf) |
|  | Generate kernel oops. |
| void | [xtensa\_user\_fault](#a0890b1717c7f7b93644c69a3293b7da8) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_k\_cycle\_get\_32](#a9ee9f897ec750957de45bf8d43349d5e) (void) |
|  | Implementation of [arch\_k\_cycle\_get\_32](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e "arch_k_cycle_get_32"). |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_k\_cycle\_get\_64](#acc1ed8d949f694a1d39e389334caf971) (void) |
|  | Implementation of [arch\_k\_cycle\_get\_64](group__arch-timing.md#gacc1ed8d949f694a1d39e389334caf971 "arch_k_cycle_get_64"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_nop](#a0af98dc5138e02248173c30b8f07210f) (void) |
|  | Implementation of [arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154 "arch_nop"). |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [xtensa\_vecbase\_lock](#ac14ee42f2f373cf48fa30a60f3aafc39) (void) |
|  | Lock VECBASE if supported by hardware. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_mem\_coherent](#a8c6bb0f6730c115689452b016ac1761f) (void \*ptr) |
|  | Implementation of [arch\_mem\_coherent](group__arch-userspace.md#ga8c6bb0f6730c115689452b016ac1761f "arch_mem_coherent"). |
| void | [arch\_xtensa\_mmu\_post\_init](#a9f03623f0f77593e60195483ac6b07f9) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_core0) |
|  | Peform additional steps after MMU initialization. |

## Detailed Description

Xtensa specific kernel interface header This header contains the Xtensa specific kernel interface.

It is included by the generic kernel interface header (include/zephyr/arch/cpu.h)

## Macro Definition Documentation

## [◆ ](#a8d3604770d7735d229e7d2fef4ff590a)ARCH\_EXCEPT

| #define ARCH\_EXCEPT | ( |  | *reason\_p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

if ([k\_is\_user\_context](syscall_8h.md#acd625881dd1a23de2573fa86d870df20)()) { \

arch\_syscall\_invoke1(reason\_p, \

K\_SYSCALL\_XTENSA\_USER\_FAULT); \

} else { \

xtensa\_arch\_except(reason\_p); \

} \

CODE\_UNREACHABLE; \

} while (false)

[k\_is\_user\_context](syscall_8h.md#acd625881dd1a23de2573fa86d870df20)

static \_\_pinned\_func bool k\_is\_user\_context(void)

Indicate whether the CPU is currently in user mode.

**Definition** syscall.h:115

## [◆ ](#accdf8a59e00ac1c1fcedc18b78be4b8a)ARCH\_IRQ\_CONNECT

| #define ARCH\_IRQ\_CONNECT | ( |  | *irq\_p*, |
| --- | --- | --- | --- |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *isr\_param\_p*, |
|  |  |  | *flags\_p* ) |

**Value:**

{ \

Z\_ISR\_DECLARE(irq\_p, flags\_p, isr\_p, isr\_param\_p); \

}

## [◆ ](#a835f1838cf0cec9c6a16bacc62436f0f)ARCH\_XTENSA\_SET\_RPO\_TLB

| #define ARCH\_XTENSA\_SET\_RPO\_TLB | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

do { \

register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr = 0, addrincr = 0x20000000; \

FOR\_EACH(\_SET\_ONE\_TLB, (;), 0, 1, 2, 3, 4, 5, 6, 7); \

} while (0)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Setup RPO TLB registers.

## Function Documentation

## [◆ ](#a9ee9f897ec750957de45bf8d43349d5e)arch\_k\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_k\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_k\_cycle\_get\_32](group__arch-timing.md#ga9ee9f897ec750957de45bf8d43349d5e "arch_k_cycle_get_32").

## [◆ ](#acc1ed8d949f694a1d39e389334caf971)arch\_k\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_k\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_k\_cycle\_get\_64](group__arch-timing.md#gacc1ed8d949f694a1d39e389334caf971 "arch_k_cycle_get_64").

## [◆ ](#a8c6bb0f6730c115689452b016ac1761f)arch\_mem\_coherent()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_mem\_coherent | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_mem\_coherent](group__arch-userspace.md#ga8c6bb0f6730c115689452b016ac1761f "arch_mem_coherent").

## [◆ ](#a0af98dc5138e02248173c30b8f07210f)arch\_nop()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_nop | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Implementation of [arch\_nop](group__arch-misc.md#gabb087b9e158824121212d65646ae4154 "arch_nop").

## [◆ ](#a9f03623f0f77593e60195483ac6b07f9)arch\_xtensa\_mmu\_post\_init()

| | void arch\_xtensa\_mmu\_post\_init | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_core0* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

Peform additional steps after MMU initialization.

This performs additional steps related to memory management after the main MMU initialization code. This needs to defined in the SoC layer. Default is do no nothing.

Parameters
:   | is\_core0 | True if this is called while executing on CPU core #0. |
    | --- | --- |

## [◆ ](#a789f894256925071f3448cda889abcf5)xtensa\_arch\_except()

| | void xtensa\_arch\_except | ( | int | *reason\_p* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

Generate hardware exception.

This generates hardware exception which is used by [ARCH\_EXCEPT()](#a8d3604770d7735d229e7d2fef4ff590a).

Parameters
:   | reason\_p | Reason for exception. |
    | --- | --- |

## [◆ ](#a31f0ccadfc2a2afa0e985d74a0e4c2e9)xtensa\_arch\_kernel\_oops()

| | void xtensa\_arch\_kernel\_oops | ( | int | *reason\_p*, | | --- | --- | --- | --- | |  |  | void \* | *ssf* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Generate kernel oops.

This generates kernel oops which is used by [arch\_syscall\_oops()](group__arch-userspace.md#gad53908f229d7e2c333574b009493644b "Induce a kernel oops that appears to come from a specific location.").

Parameters
:   | reason\_p | Reason for exception. |
    | --- | --- |
    | ssf | Stack pointer. |

## [◆ ](#a0890b1717c7f7b93644c69a3293b7da8)xtensa\_user\_fault()

| void xtensa\_user\_fault | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reason* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac14ee42f2f373cf48fa30a60f3aafc39)xtensa\_vecbase\_lock()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void xtensa\_vecbase\_lock | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

Lock VECBASE if supported by hardware.

The bit 0 of VECBASE acts as a lock bit on hardware supporting this feature. When this bit is set, VECBASE cannot be changed until it is cleared by hardware reset. When the hardware does not support this bit, it is hardwired to 0.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [arch.h](xtensa_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
