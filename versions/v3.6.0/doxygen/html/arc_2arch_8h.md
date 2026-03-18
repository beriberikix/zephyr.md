---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arc_2arch_8h.html
original_path: doxygen/html/arc_2arch_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

ARC specific kernel interface header.
[More...](#details)

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/sw_isr_table.h](sw__isr__table_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/arch/arc/thread.h](arch_2arc_2thread_8h_source.md)>`  
`#include <[zephyr/arch/common/sys_bitops.h](sys__bitops_8h_source.md)>`  
`#include "[sys-io-common.h](sys-io-common_8h_source.md)"`  
`#include <[zephyr/arch/arc/v2/exception.h](arc_2v2_2exception_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/irq.h](arch_2arc_2v2_2irq_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/misc.h](arc_2v2_2misc_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/aux_regs.h](aux__regs_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/arcv2_irq_unit.h](arcv2__irq__unit_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/asm_inline.h](arc_2v2_2asm__inline_8h_source.md)>`  
`#include <[zephyr/arch/arc/arc_addr_types.h](arc__addr__types_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/error.h](arc_2v2_2error_8h_source.md)>`

[Go to the source code of this file.](arc_2arch_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARCH\_STACK\_PTR\_ALIGN](#af0f8ad93611d93cd0626914837e761d3)   4 |
| #define | [ARCH\_THREAD\_STACK\_RESERVED](#ace8831316d471ccfb06eeddb6d69d817)   CONFIG\_PRIVILEGED\_STACK\_SIZE |
| #define | [ARCH\_THREAD\_STACK\_SIZE\_ADJUST](#ab76d60bd06e5c5a0f995c6b11bf97fd8)(size) |
| #define | [ARCH\_THREAD\_STACK\_OBJ\_ALIGN](#ab6c1d96f5e018ed166ee401dc84b7ab7)(size) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_partition\_attr\_t](group__xtensa__mmu__apis.md#ga58f790e348e5e1c4a3962a134cfb505f) |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_nop](#a0af98dc5138e02248173c30b8f07210f) (void) |

## Detailed Description

ARC specific kernel interface header.

This header contains the ARC specific kernel interface. It is included by the kernel interface architecture-abstraction header include/arch/cpu.h)

## Macro Definition Documentation

## [◆ ](#af0f8ad93611d93cd0626914837e761d3)ARCH\_STACK\_PTR\_ALIGN

| #define ARCH\_STACK\_PTR\_ALIGN   4 |
| --- |

## [◆ ](#ab6c1d96f5e018ed166ee401dc84b7ab7)ARCH\_THREAD\_STACK\_OBJ\_ALIGN

| #define ARCH\_THREAD\_STACK\_OBJ\_ALIGN | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

Z\_ARC\_MPU\_ALIGN

## [◆ ](#ace8831316d471ccfb06eeddb6d69d817)ARCH\_THREAD\_STACK\_RESERVED

| #define ARCH\_THREAD\_STACK\_RESERVED   CONFIG\_PRIVILEGED\_STACK\_SIZE |
| --- |

## [◆ ](#ab76d60bd06e5c5a0f995c6b11bf97fd8)ARCH\_THREAD\_STACK\_SIZE\_ADJUST

| #define ARCH\_THREAD\_STACK\_SIZE\_ADJUST | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)((size), Z\_ARC\_MPU\_ALIGN))

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:288

## Function Documentation

## [◆ ](#a0af98dc5138e02248173c30b8f07210f)arch\_nop()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_nop | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [arch.h](arc_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
