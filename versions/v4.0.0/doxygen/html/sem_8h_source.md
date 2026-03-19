---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sem_8h_source.html
original_path: doxygen/html/sem_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

22#include <[zephyr/kernel.h](kernel_8h.md)>

23#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

26#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 35](structsys__sem.md)struct [sys\_sem](structsys__sem.md) {

36#ifdef CONFIG\_USERSPACE

[ 37](structsys__sem.md#aa121aa4e951fbf7cd60e7937797f9e4c) struct [k\_futex](structk__futex.md) [futex](structsys__sem.md#aa121aa4e951fbf7cd60e7937797f9e4c);

[ 38](structsys__sem.md#ab8d906d43d61fa13b7dba8107dd35e34) int [limit](structsys__sem.md#ab8d906d43d61fa13b7dba8107dd35e34);

39#else

40 struct k\_sem kernel\_sem;

41#endif

42};

43

49

63#ifdef CONFIG\_USERSPACE

[ 64](group__user__semaphore__apis.md#gad7b4e3a8910b78e4beb0ec20524426e1)#define SYS\_SEM\_DEFINE(\_name, \_initial\_count, \_count\_limit) \

65 struct sys\_sem \_name = { \

66 .futex = { \_initial\_count }, \

67 .limit = \_count\_limit \

68 }; \

69 BUILD\_ASSERT(((\_count\_limit) != 0) && \

70 ((\_initial\_count) <= (\_count\_limit)))

71#else

72/\* Stuff this in the section with the rest of the k\_sem objects, since they

73 \* are identical and can be treated as a k\_sem in the boot initialization code

74 \*/

75#define SYS\_SEM\_DEFINE(\_name, \_initial\_count, \_count\_limit) \

76 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(k\_sem, sys\_sem, \_name) = { \

77 .kernel\_sem = Z\_SEM\_INITIALIZER(\_name.kernel\_sem, \

78 \_initial\_count, \_count\_limit) \

79 }; \

80 BUILD\_ASSERT(((\_count\_limit) != 0) && \

81 ((\_initial\_count) <= (\_count\_limit)))

82#endif

83

[ 97](group__user__semaphore__apis.md#gae20385545bbf7a9dfd59afa74bf1120a)int [sys\_sem\_init](group__user__semaphore__apis.md#gae20385545bbf7a9dfd59afa74bf1120a)(struct [sys\_sem](structsys__sem.md) \*sem, unsigned int initial\_count,

98 unsigned int limit);

99

[ 113](group__user__semaphore__apis.md#gaae32032398db1f693ad3f876863f78b4)int [sys\_sem\_give](group__user__semaphore__apis.md#gaae32032398db1f693ad3f876863f78b4)(struct [sys\_sem](structsys__sem.md) \*sem);

114

[ 129](group__user__semaphore__apis.md#gaf742a29f89a816fa34b8d6d33e221b77)int [sys\_sem\_take](group__user__semaphore__apis.md#gaf742a29f89a816fa34b8d6d33e221b77)(struct [sys\_sem](structsys__sem.md) \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout);

130

[ 140](group__user__semaphore__apis.md#ga7b287ca3cc3ab2766d7c1beec1849894)unsigned int [sys\_sem\_count\_get](group__user__semaphore__apis.md#ga7b287ca3cc3ab2766d7c1beec1849894)(struct [sys\_sem](structsys__sem.md) \*sem);

141

145

146#if defined(\_\_GNUC\_\_)

147static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void z\_sys\_sem\_lock\_onexit(\_\_maybe\_unused int \*rc)

148{

149 \_\_ASSERT(\*rc == 1, "SYS\_SEM\_LOCK exited with goto, break or return, "

150 "use SYS\_SEM\_LOCK\_BREAK instead.");

151}

152#define SYS\_SEM\_LOCK\_ONEXIT \_\_attribute\_\_((\_\_cleanup\_\_(z\_sys\_sem\_lock\_onexit)))

153#else

154#define SYS\_SEM\_LOCK\_ONEXIT

155#endif

156

160

[ 167](group__user__semaphore__apis.md#ga2e5d53d02732b7df60853a00ed240cff)#define SYS\_SEM\_LOCK\_BREAK continue

168

[ 207](group__user__semaphore__apis.md#ga43f2c8aae5ff633364e141a0c0340e93)#define SYS\_SEM\_LOCK(sem) \

208 for (int \_\_rc SYS\_SEM\_LOCK\_ONEXIT = sys\_sem\_take((sem), K\_FOREVER); ({ \

209 \_\_ASSERT(\_\_rc >= 0, "Failed to take sem: %d", \_\_rc); \

210 \_\_rc == 0; \

211 }); \

212 ({ \

213 \_\_rc = sys\_sem\_give((sem)); \

214 \_\_ASSERT(\_\_rc == 0, "Failed to give sem: %d", \_\_rc); \

215 }), \

216 \_\_rc = 1)

217

221

222#ifdef \_\_cplusplus

223}

224#endif

225

226#endif

[\_\_assert.h](____assert_8h.md)

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

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[k\_futex](structk__futex.md)

futex structure

**Definition** kernel.h:2222

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[sys\_sem](structsys__sem.md)

sys\_sem structure

**Definition** sem.h:35

[sys\_sem::futex](structsys__sem.md#aa121aa4e951fbf7cd60e7937797f9e4c)

struct k\_futex futex

**Definition** sem.h:37

[sys\_sem::limit](structsys__sem.md#ab8d906d43d61fa13b7dba8107dd35e34)

int limit

**Definition** sem.h:38

[atomic.h](sys_2atomic_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sem.h](sem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
