---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arc_2v2_2misc_8h_source.html
original_path: doxygen/html/arc_2v2_2misc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

misc.h

[Go to the documentation of this file.](arc_2v2_2misc_8h.md)

1/\*

2 \* Copyright (c) 2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_MISC\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_MISC\_H\_

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21#ifndef \_ASMLANGUAGE

22extern unsigned int z\_arc\_cpu\_sleep\_mode;

23

[ 24](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

25

[ 26](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](arc_2v2_2misc_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

27{

28 return [sys\_clock\_cycle\_get\_32](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a)();

29}

30

[ 31](arc_2v2_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](arc_2v2_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

32

[ 33](arc_2v2_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](arc_2v2_2misc_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

34{

35 return [sys\_clock\_cycle\_get\_64](arc_2v2_2misc_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

36}

37#endif

38

39#ifdef \_\_cplusplus

40}

41#endif

42

43#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_MISC\_H\_ \*/

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

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [misc.h](arc_2v2_2misc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
