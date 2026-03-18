---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/x86_2arch__inlines_8h_source.html
original_path: doxygen/html/x86_2arch__inlines_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h

[Go to the documentation of this file.](x86_2arch__inlines_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \* Copyright (c) 2019 Stephanos Ioannidis <root@stephanos.io>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_INLINES\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_INLINES\_H\_

10

11#ifndef \_ASMLANGUAGE

12

13#include <[zephyr/arch/x86/x86\_acpi.h](x86__acpi_8h.md)>

14

15#if defined(CONFIG\_X86\_64)

16

17#include <[zephyr/arch/x86/intel64/thread.h](arch_2x86_2intel64_2thread_8h.md)>

18#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

19

20static inline struct \_cpu \*[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)(void)

21{

22 struct \_cpu \*cpu;

23

24 \_\_asm\_\_ volatile("movq %%gs:(%c1), %0"

25 : "=r" (cpu)

26 : "i" (offsetof([x86\_tss64\_t](arch_2x86_2intel64_2thread_8h.md#af11b6454439f03e21b92bceff9ed7f00), cpu)));

27

28 return cpu;

29}

30

31static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)(void)

32{

33 /\*

34 \* Placeholder implementation to be replaced with an architecture

35 \* specific call to get processor ID

36 \*/

37 return [arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)()->id;

38}

39

40#endif /\* CONFIG\_X86\_64 \*/

41

[ 42](x86_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)(void)

43{

44 return CONFIG\_MP\_MAX\_NUM\_CPUS;

45}

46

47#endif /\* !\_ASMLANGUAGE \*/

48

49#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_INLINES\_H\_ \*/

[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)

static ALWAYS\_INLINE \_cpu\_t \* arch\_curr\_cpu(void)

**Definition** arch\_inlines.h:17

[arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)

static ALWAYS\_INLINE uint32\_t arch\_proc\_id(void)

**Definition** arch\_inlines.h:30

[arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)

static ALWAYS\_INLINE unsigned int arch\_num\_cpus(void)

**Definition** arch\_inlines.h:39

[thread.h](arch_2x86_2intel64_2thread_8h.md)

[x86\_tss64\_t](arch_2x86_2intel64_2thread_8h.md#af11b6454439f03e21b92bceff9ed7f00)

struct x86\_tss64 x86\_tss64\_t

**Definition** thread.h:96

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[kernel\_structs.h](kernel__structs_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[x86\_acpi.h](x86__acpi_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [arch\_inlines.h](x86_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
