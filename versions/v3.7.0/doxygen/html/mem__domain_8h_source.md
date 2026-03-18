---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mem__domain_8h_source.html
original_path: doxygen/html/mem__domain_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_domain.h

[Go to the documentation of this file.](mem__domain_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \* Copyright (c) 2018-2020 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef INCLUDE\_APP\_MEMORY\_MEM\_DOMAIN\_H

9#define INCLUDE\_APP\_MEMORY\_MEM\_DOMAIN\_H

10

11#include <[stdint.h](stdint_8h.md)>

12#include <stddef.h>

13#include <[zephyr/sys/dlist.h](dlist_8h.md)>

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15#include <[zephyr/kernel/thread.h](kernel_2thread_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

26

27#ifdef CONFIG\_USERSPACE

33#ifdef \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK

34#define K\_MEM\_PARTITION\_DEFINE(name, start, size, attr) \

35 \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size); \

36 struct k\_mem\_partition name =\

37 { (uintptr\_t)start, size, attr}

38#else

[ 39](group__mem__domain__apis.md#ga4360fd595cb3fe3a10b58c12ae2b7ece)#define K\_MEM\_PARTITION\_DEFINE(name, start, size, attr) \

40 struct k\_mem\_partition name =\

41 { (uintptr\_t)start, size, attr}

42#endif /\* \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK \*/

43

[ 55](structk__mem__partition.md)struct [k\_mem\_partition](structk__mem__partition.md) {

[ 57](structk__mem__partition.md#a654d19bfd6a1154f410ac6f3c481c5b7) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [start](structk__mem__partition.md#a654d19bfd6a1154f410ac6f3c481c5b7);

[ 59](structk__mem__partition.md#ab3cb68302158f3dced41dbff4cbb226c) size\_t [size](structk__mem__partition.md#ab3cb68302158f3dced41dbff4cbb226c);

[ 61](structk__mem__partition.md#ada951ba1ec9429c98c16761e3093eedb) [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) [attr](structk__mem__partition.md#ada951ba1ec9429c98c16761e3093eedb);

62};

63

[ 80](structk__mem__domain.md)struct [k\_mem\_domain](structk__mem__domain.md) {

81#ifdef CONFIG\_ARCH\_MEM\_DOMAIN\_DATA

82 struct [arch\_mem\_domain](structarch__mem__domain.md) arch;

83#endif /\* CONFIG\_ARCH\_MEM\_DOMAIN\_DATA \*/

[ 85](structk__mem__domain.md#a48cbffd5f2e85bee1b4b5b02b753980e) struct [k\_mem\_partition](structk__mem__partition.md) [partitions](structk__mem__domain.md#a48cbffd5f2e85bee1b4b5b02b753980e)[CONFIG\_MAX\_DOMAIN\_PARTITIONS];

[ 87](structk__mem__domain.md#afc3d3a778e84fe98d778f548d707929a) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [mem\_domain\_q](structk__mem__domain.md#afc3d3a778e84fe98d778f548d707929a);

[ 89](structk__mem__domain.md#abc876ea435863315f66631e28e49ab8a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_partitions](structk__mem__domain.md#abc876ea435863315f66631e28e49ab8a);

90};

91

102extern struct [k\_mem\_domain](structk__mem__domain.md) [k\_mem\_domain\_default](group__mem__domain__apis.md#ga3613abdb546a66059fa3f621a2ebd41a);

103#else

104/\* To support use of IS\_ENABLED for the APIs below \*/

105struct [k\_mem\_domain](structk__mem__domain.md);

106struct [k\_mem\_partition](structk__mem__partition.md);

107#endif /\* CONFIG\_USERSPACE \*/

108

[ 129](group__mem__domain__apis.md#ga8a987bc85c02925685fe87213fe26c5a)int [k\_mem\_domain\_init](group__mem__domain__apis.md#ga8a987bc85c02925685fe87213fe26c5a)(struct [k\_mem\_domain](structk__mem__domain.md) \*domain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_parts,

130 struct [k\_mem\_partition](structk__mem__partition.md) \*parts[]);

131

[ 159](group__mem__domain__apis.md#ga07da0cf76f8db54373b88d40be63b138)int [k\_mem\_domain\_add\_partition](group__mem__domain__apis.md#ga07da0cf76f8db54373b88d40be63b138)(struct [k\_mem\_domain](structk__mem__domain.md) \*domain,

160 struct [k\_mem\_partition](structk__mem__partition.md) \*part);

161

[ 174](group__mem__domain__apis.md#gada4f8ce609d6b720ee88e11544555fc2)int [k\_mem\_domain\_remove\_partition](group__mem__domain__apis.md#gada4f8ce609d6b720ee88e11544555fc2)(struct [k\_mem\_domain](structk__mem__domain.md) \*domain,

175 struct [k\_mem\_partition](structk__mem__partition.md) \*part);

176

[ 188](group__mem__domain__apis.md#ga7b4d6148d9375f020a268961d5afde2d)int [k\_mem\_domain\_add\_thread](group__mem__domain__apis.md#ga7b4d6148d9375f020a268961d5afde2d)(struct [k\_mem\_domain](structk__mem__domain.md) \*domain,

189 [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread);

190

191#ifdef \_\_cplusplus

192}

193#endif

194

196#endif /\* INCLUDE\_APP\_MEMORY\_MEM\_DOMAIN\_H \*/

[dlist.h](dlist_8h.md)

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:50

[k\_mem\_domain\_add\_partition](group__mem__domain__apis.md#ga07da0cf76f8db54373b88d40be63b138)

int k\_mem\_domain\_add\_partition(struct k\_mem\_domain \*domain, struct k\_mem\_partition \*part)

Add a memory partition into a memory domain.

[k\_mem\_domain\_default](group__mem__domain__apis.md#ga3613abdb546a66059fa3f621a2ebd41a)

struct k\_mem\_domain k\_mem\_domain\_default

Default memory domain.

[k\_mem\_domain\_add\_thread](group__mem__domain__apis.md#ga7b4d6148d9375f020a268961d5afde2d)

int k\_mem\_domain\_add\_thread(struct k\_mem\_domain \*domain, k\_tid\_t thread)

Add a thread into a memory domain.

[k\_mem\_domain\_init](group__mem__domain__apis.md#ga8a987bc85c02925685fe87213fe26c5a)

int k\_mem\_domain\_init(struct k\_mem\_domain \*domain, uint8\_t num\_parts, struct k\_mem\_partition \*parts[])

Initialize a memory domain.

[k\_mem\_domain\_remove\_partition](group__mem__domain__apis.md#gada4f8ce609d6b720ee88e11544555fc2)

int k\_mem\_domain\_remove\_partition(struct k\_mem\_domain \*domain, struct k\_mem\_partition \*part)

Remove a memory partition from a memory domain.

[thread.h](kernel_2thread_8h.md)

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:380

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[arch\_mem\_domain](structarch__mem__domain.md)

**Definition** arch.h:46

[k\_mem\_domain](structk__mem__domain.md)

Memory Domain.

**Definition** mem\_domain.h:80

[k\_mem\_domain::partitions](structk__mem__domain.md#a48cbffd5f2e85bee1b4b5b02b753980e)

struct k\_mem\_partition partitions[CONFIG\_MAX\_DOMAIN\_PARTITIONS]

partitions in the domain

**Definition** mem\_domain.h:85

[k\_mem\_domain::num\_partitions](structk__mem__domain.md#abc876ea435863315f66631e28e49ab8a)

uint8\_t num\_partitions

number of active partitions in the domain

**Definition** mem\_domain.h:89

[k\_mem\_domain::mem\_domain\_q](structk__mem__domain.md#afc3d3a778e84fe98d778f548d707929a)

sys\_dlist\_t mem\_domain\_q

Doubly linked list of member threads.

**Definition** mem\_domain.h:87

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[k\_mem\_partition::start](structk__mem__partition.md#a654d19bfd6a1154f410ac6f3c481c5b7)

uintptr\_t start

start address of memory partition

**Definition** mem\_domain.h:57

[k\_mem\_partition::size](structk__mem__partition.md#ab3cb68302158f3dced41dbff4cbb226c)

size\_t size

size of memory partition

**Definition** mem\_domain.h:59

[k\_mem\_partition::attr](structk__mem__partition.md#ada951ba1ec9429c98c16761e3093eedb)

k\_mem\_partition\_attr\_t attr

attribute of memory partition

**Definition** mem\_domain.h:61

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [app\_memory](dir_a5c66281f93d933ad709643c33992dc2.md)
- [mem\_domain.h](mem__domain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
