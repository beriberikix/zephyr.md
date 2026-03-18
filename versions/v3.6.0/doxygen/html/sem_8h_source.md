---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sem_8h_source.html
original_path: doxygen/html/sem_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sem.h

[Go to the documentation of this file.](sem_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_SYS\_SEM\_H\_

14#define ZEPHYR\_INCLUDE\_SYS\_SEM\_H\_

15

16/\*

17 \* sys\_sem exists in user memory working as counter semaphore for

18 \* user mode thread when user mode enabled. When user mode isn't

19 \* enabled, sys\_sem behaves like k\_sem.

20 \*/

21

22#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

23#include <[zephyr/sys/atomic.h](atomic_8h.md)>

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 34](structsys__sem.md)struct [sys\_sem](structsys__sem.md) {

35#ifdef CONFIG\_USERSPACE

[ 36](structsys__sem.md#aa121aa4e951fbf7cd60e7937797f9e4c) struct [k\_futex](structk__futex.md) [futex](structsys__sem.md#aa121aa4e951fbf7cd60e7937797f9e4c);

[ 37](structsys__sem.md#ab8d906d43d61fa13b7dba8107dd35e34) int [limit](structsys__sem.md#ab8d906d43d61fa13b7dba8107dd35e34);

38#else

39 struct k\_sem kernel\_sem;

40#endif

41};

42

48

62#ifdef CONFIG\_USERSPACE

[ 63](group__user__semaphore__apis.md#gad7b4e3a8910b78e4beb0ec20524426e1)#define SYS\_SEM\_DEFINE(\_name, \_initial\_count, \_count\_limit) \

64 struct sys\_sem \_name = { \

65 .futex = { \_initial\_count }, \

66 .limit = \_count\_limit \

67 }; \

68 BUILD\_ASSERT(((\_count\_limit) != 0) && \

69 ((\_initial\_count) <= (\_count\_limit)))

70#else

71/\* Stuff this in the section with the rest of the k\_sem objects, since they

72 \* are identical and can be treated as a k\_sem in the boot initialization code

73 \*/

74#define SYS\_SEM\_DEFINE(\_name, \_initial\_count, \_count\_limit) \

75 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(k\_sem, sys\_sem, \_name) = { \

76 .kernel\_sem = Z\_SEM\_INITIALIZER(\_name.kernel\_sem, \

77 \_initial\_count, \_count\_limit) \

78 }; \

79 BUILD\_ASSERT(((\_count\_limit) != 0) && \

80 ((\_initial\_count) <= (\_count\_limit)))

81#endif

82

[ 96](group__user__semaphore__apis.md#gae20385545bbf7a9dfd59afa74bf1120a)int [sys\_sem\_init](group__user__semaphore__apis.md#gae20385545bbf7a9dfd59afa74bf1120a)(struct [sys\_sem](structsys__sem.md) \*sem, unsigned int initial\_count,

97 unsigned int limit);

98

[ 112](group__user__semaphore__apis.md#gaae32032398db1f693ad3f876863f78b4)int [sys\_sem\_give](group__user__semaphore__apis.md#gaae32032398db1f693ad3f876863f78b4)(struct [sys\_sem](structsys__sem.md) \*sem);

113

[ 128](group__user__semaphore__apis.md#gaf742a29f89a816fa34b8d6d33e221b77)int [sys\_sem\_take](group__user__semaphore__apis.md#gaf742a29f89a816fa34b8d6d33e221b77)(struct [sys\_sem](structsys__sem.md) \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout);

129

[ 139](group__user__semaphore__apis.md#ga7b287ca3cc3ab2766d7c1beec1849894)unsigned int [sys\_sem\_count\_get](group__user__semaphore__apis.md#ga7b287ca3cc3ab2766d7c1beec1849894)(struct [sys\_sem](structsys__sem.md) \*sem);

140

144

145#ifdef \_\_cplusplus

146}

147#endif

148

149#endif

[atomic.h](atomic_8h.md)

[sys\_sem\_count\_get](group__user__semaphore__apis.md#ga7b287ca3cc3ab2766d7c1beec1849894)

unsigned int sys\_sem\_count\_get(struct sys\_sem \*sem)

Get sys\_sem's value.

[sys\_sem\_give](group__user__semaphore__apis.md#gaae32032398db1f693ad3f876863f78b4)

int sys\_sem\_give(struct sys\_sem \*sem)

Give a semaphore.

[sys\_sem\_init](group__user__semaphore__apis.md#gae20385545bbf7a9dfd59afa74bf1120a)

int sys\_sem\_init(struct sys\_sem \*sem, unsigned int initial\_count, unsigned int limit)

Initialize a semaphore.

[sys\_sem\_take](group__user__semaphore__apis.md#gaf742a29f89a816fa34b8d6d33e221b77)

int sys\_sem\_take(struct sys\_sem \*sem, k\_timeout\_t timeout)

Take a sys\_sem.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[k\_futex](structk__futex.md)

futex structure

**Definition** kernel.h:2128

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[sys\_sem](structsys__sem.md)

sys\_sem structure

**Definition** sem.h:34

[sys\_sem::futex](structsys__sem.md#aa121aa4e951fbf7cd60e7937797f9e4c)

struct k\_futex futex

**Definition** sem.h:36

[sys\_sem::limit](structsys__sem.md#ab8d906d43d61fa13b7dba8107dd35e34)

int limit

**Definition** sem.h:37

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sem.h](sem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
