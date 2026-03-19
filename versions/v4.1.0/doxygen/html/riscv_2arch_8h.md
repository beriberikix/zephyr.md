---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/riscv_2arch_8h.html
original_path: doxygen/html/riscv_2arch_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

RISCV specific kernel interface header This header contains the RISCV specific kernel interface.
[More...](#details)

`#include <[zephyr/arch/riscv/thread.h](arch_2riscv_2thread_8h_source.md)>`  
`#include <[zephyr/arch/riscv/exception.h](riscv_2exception_8h_source.md)>`  
`#include <[zephyr/arch/riscv/irq.h](arch_2riscv_2irq_8h_source.md)>`  
`#include <[zephyr/arch/riscv/sys_io.h](arch_2riscv_2sys__io_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_bitops.h](sys__bitops_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/arch/riscv/syscall.h](arch_2riscv_2syscall_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/arch/riscv/csr.h](csr_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/arch/riscv/error.h](include_2zephyr_2arch_2riscv_2error_8h_source.md)>`

[Go to the source code of this file.](riscv_2arch_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) |
| struct | [arch\_mem\_domain](structarch__mem__domain.md) |

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   16 |
| #define | [ARCH\_THREAD\_STACK\_RESERVED](#ace8831316d471ccfb06eeddb6d69d817) |
| #define | [ARCH\_THREAD\_STACK\_SIZE\_ADJUST](#ab76d60bd06e5c5a0f995c6b11bf97fd8)(size) |
| #define | [ARCH\_THREAD\_STACK\_OBJ\_ALIGN](#ab6c1d96f5e018ed166ee401dc84b7ab7)(size) |
| #define | [RV\_REGSIZE](#a2e02af37a1fa1fa6b5df7e7e150dcbf3)   4 |
| #define | [RV\_REGSHIFT](#a0175995fb1dea1feffa8ba200245395c)   2 |
| #define | [MSTATUS\_IEN](#a190f193ea2099625861fb58c6e725267)   (1UL << 3) |
| #define | [MSTATUS\_MPP\_M](#aa6621785868a067469e73ac9babeed99)   (3UL << 11) |
| #define | [MSTATUS\_MPIE\_EN](#a6ef6d2229ec2a9328ff08de7dea7cc9c)   (1UL << 7) |
| #define | [MSTATUS\_FS\_OFF](#a6ebe8a2c82f48216c528cc0cc25122c0)   (0UL << 13) |
| #define | [MSTATUS\_FS\_INIT](#a6ca1c1c2ce04e484e7d146febf167dac)   (1UL << 13) |
| #define | [MSTATUS\_FS\_CLEAN](#aef9ff6d95030e46ca86237a320898ca3)   (2UL << 13) |
| #define | [MSTATUS\_FS\_DIRTY](#aa704a5aece9149a30cefae0a0f77f034)   (3UL << 13) |
| #define | [MSTATUS\_DEF\_RESTORE](#a0d401e5c8d9231016dfc0b2b8d53e0e6)   ([MSTATUS\_MPP\_M](#aa6621785868a067469e73ac9babeed99) | [MSTATUS\_MPIE\_EN](#a6ef6d2229ec2a9328ff08de7dea7cc9c)) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#a9b7cc3c51f518517031d76807470aa10) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RO](#a6636a59c913e035646a1a9e5ed61559d) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#a3c52d13e42a66beb72d088ac56388951) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#a708338371e91b5a3f2d44f9ae48849db) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#a706eaa9c515f1cc859d97ef8455b2f2f) |
| #define | [K\_MEM\_PARTITION\_P\_NA\_U\_NA](#a73bc6803ccf24aad395089a4395bd22f) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RWX](#a29db5fb48087c0cae596ff212989ed24) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](#a78f9b21aa8b5c894db28328f5a1e2641) |

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

RISCV specific kernel interface header This header contains the RISCV specific kernel interface.

It is included by the generic kernel interface header ([arch/cpu.h](cpu_8h.md))

## Macro Definition Documentation

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   16 |
| --- |

## [◆ ](#ab6c1d96f5e018ed166ee401dc84b7ab7)ARCH\_THREAD\_STACK\_OBJ\_ALIGN

| #define ARCH\_THREAD\_STACK\_OBJ\_ALIGN | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

Z\_RISCV\_STACK\_PMP\_ALIGN

## [◆ ](#ace8831316d471ccfb06eeddb6d69d817)ARCH\_THREAD\_STACK\_RESERVED

| #define ARCH\_THREAD\_STACK\_RESERVED |
| --- |

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(Z\_RISCV\_STACK\_GUARD\_SIZE + CONFIG\_PRIVILEGED\_STACK\_SIZE, \

Z\_RISCV\_STACK\_PMP\_ALIGN)

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:322

## [◆ ](#ab76d60bd06e5c5a0f995c6b11bf97fd8)ARCH\_THREAD\_STACK\_SIZE\_ADJUST

| #define ARCH\_THREAD\_STACK\_SIZE\_ADJUST | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(size, Z\_RISCV\_STACK\_PMP\_ALIGN)

## [◆ ](#a73bc6803ccf24aad395089a4395bd22f)K\_MEM\_PARTITION\_P\_NA\_U\_NA

| #define K\_MEM\_PARTITION\_P\_NA\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{0})

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:143

## [◆ ](#a706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{0})

## [◆ ](#a708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[PMP\_R](csr_8h.md#a383d3ee4d5727ef3fb4437d954be3b21)})

[PMP\_R](csr_8h.md#a383d3ee4d5727ef3fb4437d954be3b21)

#define PMP\_R

**Definition** csr.h:136

## [◆ ](#a3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{0})

## [◆ ](#a6636a59c913e035646a1a9e5ed61559d)K\_MEM\_PARTITION\_P\_RW\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[PMP\_R](csr_8h.md#a383d3ee4d5727ef3fb4437d954be3b21)})

## [◆ ](#a9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[PMP\_R](csr_8h.md#a383d3ee4d5727ef3fb4437d954be3b21) | [PMP\_W](csr_8h.md#a5f34c98b252436e69ad95e766abf8482)})

[PMP\_W](csr_8h.md#a5f34c98b252436e69ad95e766abf8482)

#define PMP\_W

**Definition** csr.h:137

## [◆ ](#a29db5fb48087c0cae596ff212989ed24)K\_MEM\_PARTITION\_P\_RWX\_U\_RWX

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[PMP\_R](csr_8h.md#a383d3ee4d5727ef3fb4437d954be3b21) | [PMP\_W](csr_8h.md#a5f34c98b252436e69ad95e766abf8482) | [PMP\_X](csr_8h.md#aabfce7f7dde3e93eb596074b4d107bec)})

[PMP\_X](csr_8h.md#aabfce7f7dde3e93eb596074b4d107bec)

#define PMP\_X

**Definition** csr.h:138

## [◆ ](#a78f9b21aa8b5c894db28328f5a1e2641)K\_MEM\_PARTITION\_P\_RX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[PMP\_R](csr_8h.md#a383d3ee4d5727ef3fb4437d954be3b21) | [PMP\_X](csr_8h.md#aabfce7f7dde3e93eb596074b4d107bec)})

## [◆ ](#a0d401e5c8d9231016dfc0b2b8d53e0e6)MSTATUS\_DEF\_RESTORE

| #define MSTATUS\_DEF\_RESTORE   ([MSTATUS\_MPP\_M](#aa6621785868a067469e73ac9babeed99) | [MSTATUS\_MPIE\_EN](#a6ef6d2229ec2a9328ff08de7dea7cc9c)) |
| --- |

## [◆ ](#aef9ff6d95030e46ca86237a320898ca3)MSTATUS\_FS\_CLEAN

| #define MSTATUS\_FS\_CLEAN   (2UL << 13) |
| --- |

## [◆ ](#aa704a5aece9149a30cefae0a0f77f034)MSTATUS\_FS\_DIRTY

| #define MSTATUS\_FS\_DIRTY   (3UL << 13) |
| --- |

## [◆ ](#a6ca1c1c2ce04e484e7d146febf167dac)MSTATUS\_FS\_INIT

| #define MSTATUS\_FS\_INIT   (1UL << 13) |
| --- |

## [◆ ](#a6ebe8a2c82f48216c528cc0cc25122c0)MSTATUS\_FS\_OFF

| #define MSTATUS\_FS\_OFF   (0UL << 13) |
| --- |

## [◆ ](#a190f193ea2099625861fb58c6e725267)MSTATUS\_IEN

| #define MSTATUS\_IEN   (1UL << 3) |
| --- |

## [◆ ](#a6ef6d2229ec2a9328ff08de7dea7cc9c)MSTATUS\_MPIE\_EN

| #define MSTATUS\_MPIE\_EN   (1UL << 7) |
| --- |

## [◆ ](#aa6621785868a067469e73ac9babeed99)MSTATUS\_MPP\_M

| #define MSTATUS\_MPP\_M   (3UL << 11) |
| --- |

## [◆ ](#a0175995fb1dea1feffa8ba200245395c)RV\_REGSHIFT

| #define RV\_REGSHIFT   2 |
| --- |

## [◆ ](#a2e02af37a1fa1fa6b5df7e7e150dcbf3)RV\_REGSIZE

| #define RV\_REGSIZE   4 |
| --- |

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
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [arch.h](riscv_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
