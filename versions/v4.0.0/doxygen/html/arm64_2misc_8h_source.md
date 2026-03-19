---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm64_2misc_8h_source.html
original_path: doxygen/html/arm64_2misc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

misc.h

[Go to the documentation of this file.](arm64_2misc_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_MISC\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_MISC\_H\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22#ifndef \_ASMLANGUAGE

[ 23](arm64_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

24

[ 25](arm64_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

26{

27 return [sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)();

28}

29

[ 30](arm64_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](arc_2v2_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

31

[ 32](arm64_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](arc_2v2_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

33{

34 return [sys\_clock\_cycle\_get\_64](arc_2v2_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

35}

36

[ 37](arm64_2misc_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arm_2misc_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

38{

39 \_\_asm\_\_ volatile("nop");

40}

41

42#endif

43

44#ifdef \_\_cplusplus

45}

46#endif

47

48#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_MISC\_H\_ \*/

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
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [misc.h](arm64_2misc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
