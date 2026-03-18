---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm64_2arch__inlines_8h_source.html
original_path: doxygen/html/arm64_2arch__inlines_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h

[Go to the documentation of this file.](arm64_2arch__inlines_8h.md)

1/\*

2 \* Copyright 2020 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARCH\_INLINES\_H

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARCH\_INLINES\_H

9

10#ifndef \_ASMLANGUAGE

11

12#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

13#include <[zephyr/arch/arm64/lib\_helpers.h](4_2lib__helpers_8h.md)>

14#include <[zephyr/arch/arm64/tpidrro\_el0.h](tpidrro__el0_8h.md)>

15#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

16

17/\* Note: keep in sync with `get\_cpu` in arch/arm64/core/macro\_priv.inc \*/

[ 18](arm64_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \*[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)(void)

19{

20 return (\_cpu\_t \*)([read\_tpidrro\_el0](4_2lib__helpers_8h.md#a5d96400189d120420955eec6d7229490)() & [TPIDRROEL0\_CURR\_CPU](tpidrro__el0_8h.md#a4f694ec0eb4b87138023e08242aafe7e));

21}

22

[ 23](arm64_2arch__inlines_8h.md#a39935d470a4190bae6e3063b4524e599)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_exception\_depth](arm64_2arch__inlines_8h.md#a39935d470a4190bae6e3063b4524e599)(void)

24{

25 return ([read\_tpidrro\_el0](4_2lib__helpers_8h.md#a5d96400189d120420955eec6d7229490)() & [TPIDRROEL0\_EXC\_DEPTH](tpidrro__el0_8h.md#acde61f1bf3b88e63b6e587528ad001d8)) / [TPIDRROEL0\_EXC\_UNIT](tpidrro__el0_8h.md#a1fe4c8cd6065cb0f174be6ded38fc7a2);

26}

27

[ 28](arm64_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)(void)

29{

30 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cpu\_mpid = [read\_mpidr\_el1](4_2lib__helpers_8h.md#a91995e9b71b5f1f20dedbb03e936f72d)();

31

32 \_\_ASSERT(cpu\_mpid == ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))cpu\_mpid, "mpid extends past 32 bits");

33

34 return ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))cpu\_mpid;

35}

36

[ 37](arm64_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)(void)

38{

39 return CONFIG\_MP\_MAX\_NUM\_CPUS;

40}

41

42#endif /\* !\_ASMLANGUAGE \*/

43#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARCH\_INLINES\_H \*/

[lib\_helpers.h](4_2lib__helpers_8h.md)

[read\_tpidrro\_el0](4_2lib__helpers_8h.md#a5d96400189d120420955eec6d7229490)

static ALWAYS\_INLINE uint64\_t read\_tpidrro\_el0(void)

**Definition** lib\_helpers.h:75

[read\_mpidr\_el1](4_2lib__helpers_8h.md#a91995e9b71b5f1f20dedbb03e936f72d)

static ALWAYS\_INLINE uint64\_t read\_mpidr\_el1(void)

**Definition** lib\_helpers.h:72

[\_\_assert.h](____assert_8h.md)

[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)

static ALWAYS\_INLINE \_cpu\_t \* arch\_curr\_cpu(void)

**Definition** arch\_inlines.h:17

[arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)

static ALWAYS\_INLINE uint32\_t arch\_proc\_id(void)

**Definition** arch\_inlines.h:30

[arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)

static ALWAYS\_INLINE unsigned int arch\_num\_cpus(void)

**Definition** arch\_inlines.h:39

[arch\_exception\_depth](arm64_2arch__inlines_8h.md#a39935d470a4190bae6e3063b4524e599)

static ALWAYS\_INLINE int arch\_exception\_depth(void)

**Definition** arch\_inlines.h:23

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[kernel\_structs.h](kernel__structs_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[tpidrro\_el0.h](tpidrro__el0_8h.md)

tpidrro\_el0 bits allocation

[TPIDRROEL0\_EXC\_UNIT](tpidrro__el0_8h.md#a1fe4c8cd6065cb0f174be6ded38fc7a2)

#define TPIDRROEL0\_EXC\_UNIT

**Definition** tpidrro\_el0.h:25

[TPIDRROEL0\_CURR\_CPU](tpidrro__el0_8h.md#a4f694ec0eb4b87138023e08242aafe7e)

#define TPIDRROEL0\_CURR\_CPU

**Definition** tpidrro\_el0.h:22

[TPIDRROEL0\_EXC\_DEPTH](tpidrro__el0_8h.md#acde61f1bf3b88e63b6e587528ad001d8)

#define TPIDRROEL0\_EXC\_DEPTH

**Definition** tpidrro\_el0.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arch\_inlines.h](arm64_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
