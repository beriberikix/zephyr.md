---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm64_2arch_8h_source.html
original_path: doxygen/html/arm64_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](arm64_2arch_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARCH\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARCH\_H\_

18

19/\* Add include for DTS generated information \*/

20#include <[zephyr/devicetree.h](devicetree_8h.md)>

21

22#include <[zephyr/arch/arm64/thread.h](arch_2arm64_2thread_8h.md)>

23#include <[zephyr/arch/arm64/exception.h](arm64_2exception_8h.md)>

24#include <[zephyr/arch/arm64/irq.h](arch_2arm64_2irq_8h.md)>

25#include <[zephyr/arch/arm64/misc.h](arm64_2misc_8h.md)>

26#include <[zephyr/arch/arm64/asm\_inline.h](arm64_2asm__inline_8h.md)>

27#include <[zephyr/arch/arm64/cpu.h](arm64_2cpu_8h.md)>

28#include <zephyr/arch/arm64/macro.inc>

29#include <[zephyr/arch/arm64/sys\_io.h](arch_2arm64_2sys__io_8h.md)>

30#include <[zephyr/arch/arm64/timer.h](4_2timer_8h.md)>

31#include <[zephyr/arch/arm64/error.h](include_2zephyr_2arch_2arm64_2error_8h.md)>

32#include <[zephyr/arch/arm64/mm.h](arch_2arm64_2mm_8h.md)>

33#include <[zephyr/arch/arm64/thread\_stack.h](arch_2arm64_2thread__stack_8h.md)>

34#include <[zephyr/arch/common/addr\_types.h](addr__types_8h.md)>

35#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

36#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

37

38#ifdef \_\_cplusplus

39extern "C" {

40#endif

41

42#ifndef \_ASMLANGUAGE

43

44#include <[zephyr/sys/slist.h](slist_8h.md)>

45

[ 46](structarch__mem__domain.md)struct [arch\_mem\_domain](structarch__mem__domain.md) {

47#ifdef CONFIG\_ARM\_MMU

48 struct [arm\_mmu\_ptables](structarm__mmu__ptables.md) [ptables](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6);

49#endif

[ 50](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5);

51};

52

53#endif /\* \_ASMLANGUAGE \*/

54

55#ifdef \_\_cplusplus

56}

57#endif

58

59#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARCH\_H\_ \*/

[timer.h](4_2timer_8h.md)

[addr\_types.h](addr__types_8h.md)

[irq.h](arch_2arm64_2irq_8h.md)

Cortex-A public interrupt handling.

[mm.h](arch_2arm64_2mm_8h.md)

[sys\_io.h](arch_2arm64_2sys__io_8h.md)

[thread.h](arch_2arm64_2thread_8h.md)

Per-arch thread definition.

[thread\_stack.h](arch_2arm64_2thread__stack_8h.md)

[asm\_inline.h](arm64_2asm__inline_8h.md)

[cpu.h](arm64_2cpu_8h.md)

[exception.h](arm64_2exception_8h.md)

Cortex-A public exception handling.

[misc.h](arm64_2misc_8h.md)

Cortex-A public kernel miscellaneous.

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[error.h](include_2zephyr_2arch_2arm64_2error_8h.md)

ARM AArch64 public error handling.

[slist.h](slist_8h.md)

[arch\_mem\_domain](structarch__mem__domain.md)

**Definition** arch.h:46

[arch\_mem\_domain::node](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5)

sys\_snode\_t node

**Definition** arch.h:50

[arch\_mem\_domain::ptables](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6)

pentry\_t \* ptables

**Definition** mmustructs.h:89

[arm\_mmu\_ptables](structarm__mmu__ptables.md)

**Definition** arm\_mmu.h:133

[sys\_bitops.h](sys__bitops_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arch.h](arm64_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
