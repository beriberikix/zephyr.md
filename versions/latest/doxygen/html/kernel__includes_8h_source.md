---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel__includes_8h_source.html
original_path: doxygen/html/kernel__includes_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel\_includes.h

[Go to the documentation of this file.](kernel__includes_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_KERNEL\_INCLUDES\_H\_

14#define ZEPHYR\_INCLUDE\_KERNEL\_INCLUDES\_H\_

15

16#ifndef ZEPHYR\_INCLUDE\_KERNEL\_H\_

17#error Please do not include kernel-specific headers directly, use <zephyr/kernel.h> instead

18#endif

19

20#include <stddef.h>

21#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

22#include <[limits.h](limits_8h.md)>

23#include <[zephyr/toolchain.h](toolchain_8h.md)>

24#include <[zephyr/linker/sections.h](sections_8h.md)>

25#include <[zephyr/sys/atomic.h](atomic_8h.md)>

26#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

27#include <[zephyr/kernel/internal/sched\_priq.h](sched__priq_8h.md)>

28#include <[zephyr/sys/dlist.h](dlist_8h.md)>

29#include <[zephyr/sys/slist.h](slist_8h.md)>

30#include <[zephyr/sys/sflist.h](sflist_8h.md)>

31#include <[zephyr/sys/util.h](util_8h.md)>

32#include <[zephyr/kernel/obj\_core.h](obj__core_8h.md)>

33#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

34#include <[zephyr/kernel\_version.h](kernel__version_8h.md)>

35#include <[zephyr/syscall.h](syscall_8h.md)>

36#include <[zephyr/sys/printk.h](printk_8h.md)>

37#include <zephyr/arch/cpu.h>

38#include <[zephyr/sys/rb.h](rb_8h.md)>

39#include <[zephyr/sys\_clock.h](include_2zephyr_2sys__clock_8h.md)>

40#include <[zephyr/spinlock.h](spinlock_8h.md)>

41#include <[zephyr/fatal.h](fatal_8h.md)>

42#include <[zephyr/irq.h](irq_8h.md)>

43#include <[zephyr/kernel/thread\_stack.h](kernel_2thread__stack_8h.md)>

44#include <[zephyr/app\_memory/mem\_domain.h](mem__domain_8h.md)>

45#include <[zephyr/sys/kobject.h](include_2zephyr_2sys_2kobject_8h.md)>

46#include <[zephyr/kernel/thread.h](kernel_2thread_8h.md)>

47/\* FIXME This needs to be removed. Exposes some private APIs to SOF \*/

48#include <[zephyr/kernel/internal/smp.h](kernel_2internal_2smp_8h.md)>

49

50#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_INCLUDES\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[atomic.h](atomic_8h.md)

[dlist.h](dlist_8h.md)

[fatal.h](fatal_8h.md)

Fatal error functions.

[kobject.h](include_2zephyr_2sys_2kobject_8h.md)

[sys\_clock.h](include_2zephyr_2sys__clock_8h.md)

Variables needed for system clock.

[types.h](include_2zephyr_2types_8h.md)

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[smp.h](kernel_2internal_2smp_8h.md)

[thread.h](kernel_2thread_8h.md)

[thread\_stack.h](kernel_2thread__stack_8h.md)

Macros for declaring thread stacks.

[kernel\_structs.h](kernel__structs_8h.md)

[kernel\_version.h](kernel__version_8h.md)

[limits.h](limits_8h.md)

[mem\_domain.h](mem__domain_8h.md)

[obj\_core.h](obj__core_8h.md)

[printk.h](printk_8h.md)

[rb.h](rb_8h.md)

[sched\_priq.h](sched__priq_8h.md)

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[sflist.h](sflist_8h.md)

[slist.h](slist_8h.md)

[spinlock.h](spinlock_8h.md)

Public interface for spinlocks.

[syscall.h](syscall_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel\_includes.h](kernel__includes_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
