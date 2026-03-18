---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm_2arch__inlines_8h_source.html
original_path: doxygen/html/arm_2arch__inlines_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h

[Go to the documentation of this file.](arm_2arch__inlines_8h.md)

1/\*

2 \* Copyright 2022 IoT.bzh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_ARCH\_INLINES\_H

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_ARCH\_INLINES\_H

9

10#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

11#if defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R) || defined(CONFIG\_CPU\_AARCH32\_CORTEX\_A)

12#include <[zephyr/arch/arm/cortex\_a\_r/lib\_helpers.h](cortex__a__r_2lib__helpers_8h.md)>

13#include <[zephyr/arch/arm/cortex\_a\_r/tpidruro.h](tpidruro_8h.md)>

14

15static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \*[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)(void)

16{

17 return (\_cpu\_t \*)([read\_tpidruro](cortex__a__r_2lib__helpers_8h.md#af410cde5864b6e4997a31e2162e4873d)() & [TPIDRURO\_CURR\_CPU](tpidruro_8h.md#a2df1f988f05d98a639935e8cf014a6d1));

18}

19#else

20

21#ifndef CONFIG\_SMP

22static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \*[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)(void)

23{

24 /\* Dummy implementation always return the first cpu \*/

25 return &\_kernel.cpus[0];

26}

27#endif

28#endif

29

[ 30](arm_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)(void)

31{

32 /\*

33 \* Placeholder implementation to be replaced with an architecture

34 \* specific call to get processor ID

35 \*/

36 return [arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)()->id;

37}

38

[ 39](arm_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)(void)

40{

41 return CONFIG\_MP\_MAX\_NUM\_CPUS;

42}

43

44#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_ARCH\_INLINES\_H \*/

[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)

static ALWAYS\_INLINE \_cpu\_t \* arch\_curr\_cpu(void)

**Definition** arch\_inlines.h:17

[arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)

static ALWAYS\_INLINE uint32\_t arch\_proc\_id(void)

**Definition** arch\_inlines.h:30

[arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)

static ALWAYS\_INLINE unsigned int arch\_num\_cpus(void)

**Definition** arch\_inlines.h:39

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[lib\_helpers.h](cortex__a__r_2lib__helpers_8h.md)

[read\_tpidruro](cortex__a__r_2lib__helpers_8h.md#af410cde5864b6e4997a31e2162e4873d)

static ALWAYS\_INLINE uint32\_t read\_tpidruro(void)

**Definition** lib\_helpers.h:75

[kernel\_structs.h](kernel__structs_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[tpidruro.h](tpidruro_8h.md)

tpidruro bits allocation

[TPIDRURO\_CURR\_CPU](tpidruro_8h.md#a2df1f988f05d98a639935e8cf014a6d1)

#define TPIDRURO\_CURR\_CPU

**Definition** tpidruro.h:18

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [arch\_inlines.h](arm_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
