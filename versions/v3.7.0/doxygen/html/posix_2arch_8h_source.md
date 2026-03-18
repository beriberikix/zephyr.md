---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/posix_2arch_8h_source.html
original_path: doxygen/html/posix_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](posix_2arch_8h.md)

1/\*

2 \* Copyright (c) 2010-2014 Wind River Systems, Inc.

3 \* Copyright (c) 2017 Oticon A/S

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

15

16

17#ifndef ZEPHYR\_INCLUDE\_ARCH\_POSIX\_ARCH\_H\_

18#define ZEPHYR\_INCLUDE\_ARCH\_POSIX\_ARCH\_H\_

19

20/\* Add include for DTS generated information \*/

21#include <[zephyr/devicetree.h](devicetree_8h.md)>

22

23#include <[zephyr/toolchain.h](toolchain_8h.md)>

24#include <[zephyr/irq.h](irq_8h.md)>

25#include <[zephyr/arch/posix/exception.h](posix_2exception_8h.md)>

26#include <[zephyr/arch/posix/asm\_inline.h](posix_2asm__inline_8h.md)>

27#include <[zephyr/arch/posix/thread.h](arch_2posix_2thread_8h.md)>

28#include <board\_irq.h> /\* Each board must define this \*/

29#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

30#include <[zephyr/arch/posix/posix\_soc\_if.h](posix__soc__if_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

36#ifdef CONFIG\_64BIT

37#define ARCH\_STACK\_PTR\_ALIGN 8

38#else

[ 39](posix_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 4

40#endif

41

[ 42](posix_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

43

[ 44](posix_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

45{

46 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

47}

48

[ 49](posix_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

50

[ 51](posix_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

52{

53 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

54}

55

[ 56](posix_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

57{

58 \_\_asm\_\_ volatile("nop");

59}

60

[ 61](posix_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

62{

63 return key == false;

64}

65

[ 66](posix_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

67{

68 return [posix\_irq\_lock](posix__soc__if_8h.md#a53106413853e29d1eeebbf1b5c4d36a5)();

69}

70

71

[ 72](posix_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

73{

74 [posix\_irq\_unlock](posix__soc__if_8h.md#abf80b27ff517e32514e952c53e6c67c6)(key);

75}

76

77#ifdef \_\_cplusplus

78}

79#endif

80

81#endif /\* ZEPHYR\_INCLUDE\_ARCH\_POSIX\_ARCH\_H\_ \*/

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[thread.h](arch_2posix_2thread_8h.md)

Per-arch thread definition.

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:63

[arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** arch.h:74

[sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)

uint64\_t sys\_clock\_cycle\_get\_64(void)

[sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)

uint32\_t sys\_clock\_cycle\_get\_32(void)

[arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

**Definition** arch.h:99

[arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

**Definition** arch.h:106

[arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** arch.h:87

[asm\_inline.h](posix_2asm__inline_8h.md)

[exception.h](posix_2exception_8h.md)

[posix\_soc\_if.h](posix__soc__if_8h.md)

[posix\_irq\_lock](posix__soc__if_8h.md#a53106413853e29d1eeebbf1b5c4d36a5)

unsigned int posix\_irq\_lock(void)

[posix\_irq\_unlock](posix__soc__if_8h.md#abf80b27ff517e32514e952c53e6c67c6)

void posix\_irq\_unlock(unsigned int key)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [posix](dir_2eaa0886f2679378503a1f6e740c4205.md)
- [arch.h](posix_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
