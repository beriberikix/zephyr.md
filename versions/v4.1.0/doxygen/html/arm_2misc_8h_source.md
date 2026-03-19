---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm_2misc_8h_source.html
original_path: doxygen/html/arm_2misc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

misc.h

[Go to the documentation of this file.](arm_2misc_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_MISC\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_MISC\_H\_

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21#ifndef \_ASMLANGUAGE

[ 22](arm_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

23

[ 24](arm_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

25{

26 return [sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)();

27}

28

[ 29](arm_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](arc_2v2_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

30

[ 31](arm_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](arc_2v2_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

32{

33 return [sys\_clock\_cycle\_get\_64](arc_2v2_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

34}

35

[ 36](arm_2misc_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arm_2misc_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

37{

38 \_\_asm\_\_ volatile("nop");

39}

40

41#if defined(CONFIG\_USERSPACE)

42extern bool z\_arm\_thread\_is\_in\_user\_mode(void);

43#endif

44

45#if defined(CONFIG\_ARM\_ON\_ENTER\_CPU\_IDLE\_HOOK)

46/\* Prototype of a hook that can be enabled to be called every time the CPU is

47 \* made idle (the calls will be done from k\_cpu\_idle() and k\_cpu\_atomic\_idle()).

48 \* If this hook returns false, the CPU is prevented from entering the actual

49 \* sleep (the WFE/WFI instruction is skipped).

50 \*/

51bool z\_arm\_on\_enter\_cpu\_idle(void);

52#endif

53

54#if defined(CONFIG\_ARM\_ON\_ENTER\_CPU\_IDLE\_PREPARE\_HOOK)

55/\* Prototype of a hook that can be enabled to be called every time the CPU is

56 \* made idle (the calls will be done from k\_cpu\_idle() and k\_cpu\_atomic\_idle()).

57 \* The function is called before interrupts are disabled and can prepare to

58 \* upcoming call to z\_arm\_on\_enter\_cpu\_idle.

59 \*/

60void z\_arm\_on\_enter\_cpu\_idle\_prepare(void);

61#endif

62

63#endif

64

65#ifdef \_\_cplusplus

66}

67#endif

68

69#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_MISC\_H\_ \*/

[sys\_clock\_cycle\_get\_64](arc_2v2_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)

uint64\_t sys\_clock\_cycle\_get\_64(void)

[sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)

uint32\_t sys\_clock\_cycle\_get\_32(void)

[arch\_k\_cycle\_get\_32](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

**Definition** misc.h:26

[arch\_k\_cycle\_get\_64](arc_2v2_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

**Definition** misc.h:33

[arch\_nop](arm_2misc_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** misc.h:36

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [misc.h](arm_2misc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
