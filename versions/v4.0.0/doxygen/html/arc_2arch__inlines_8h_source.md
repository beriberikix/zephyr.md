---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arc_2arch__inlines_8h_source.html
original_path: doxygen/html/arc_2arch__inlines_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h

[Go to the documentation of this file.](arc_2arch__inlines_8h.md)

1/\*

2 \* Copyright (c) 2014-2016 Wind River Systems, Inc.

3 \* Copyright (c) 2019 Stephanos Ioannidis <root@stephanos.io>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_ARCH\_INLINES\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_ARCH\_INLINES\_H\_

10

11#ifndef \_ASMLANGUAGE

12

13#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

14

15#include <[zephyr/arch/arc/v2/aux\_regs.h](aux__regs_8h.md)>

16

[ 17](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \*[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)(void)

18{

19#ifdef CONFIG\_SMP

20 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) core;

21

22 core = z\_arc\_v2\_core\_id();

23

24 return &\_kernel.cpus[core];

25#else

26 return &\_kernel.cpus[0];

27#endif /\* CONFIG\_SMP \*/

28}

29

[ 30](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)(void)

31{

32 /\*

33 \* Placeholder implementation to be replaced with an architecture

34 \* specific call to get processor ID

35 \*/

36 return [arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)()->id;

37}

38

[ 39](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)(void)

40{

41 return CONFIG\_MP\_MAX\_NUM\_CPUS;

42}

43

44#endif /\* !\_ASMLANGUAGE \*/

45#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_ARCH\_INLINES\_H\_ \*/

[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)

static ALWAYS\_INLINE \_cpu\_t \* arch\_curr\_cpu(void)

**Definition** arch\_inlines.h:17

[arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)

static ALWAYS\_INLINE uint32\_t arch\_proc\_id(void)

**Definition** arch\_inlines.h:30

[arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)

static ALWAYS\_INLINE unsigned int arch\_num\_cpus(void)

**Definition** arch\_inlines.h:39

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[kernel\_structs.h](kernel__structs_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [arch\_inlines.h](arc_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
