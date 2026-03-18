---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/riscv_2arch__inlines_8h_source.html
original_path: doxygen/html/riscv_2arch__inlines_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h

[Go to the documentation of this file.](riscv_2arch__inlines_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ARCH\_INLINES\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ARCH\_INLINES\_H\_

9

10#ifndef \_ASMLANGUAGE

11

12#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

13#include "[csr.h](csr_8h.md)"

14

[ 15](riscv_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)(void)

16{

17 return [csr\_read](csr_8h.md#a1b19216c67cb23fc1c46136325b732d9)(mhartid) & (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))CONFIG\_RISCV\_HART\_MASK);

18}

19

[ 20](riscv_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \*[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)(void)

21{

22#if defined(CONFIG\_SMP) || defined(CONFIG\_USERSPACE)

23 return (\_cpu\_t \*)[csr\_read](csr_8h.md#a1b19216c67cb23fc1c46136325b732d9)(mscratch);

24#else

25 return &\_kernel.cpus[0];

26#endif

27}

28

[ 29](riscv_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)(void)

30{

31 return CONFIG\_MP\_MAX\_NUM\_CPUS;

32}

33

34#endif /\* !\_ASMLANGUAGE \*/

35#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ARCH\_INLINES\_H\_ \*/

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

[csr.h](csr_8h.md)

[csr\_read](csr_8h.md#a1b19216c67cb23fc1c46136325b732d9)

#define csr\_read(csr)

**Definition** csr.h:185

[kernel\_structs.h](kernel__structs_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [arch\_inlines.h](riscv_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
