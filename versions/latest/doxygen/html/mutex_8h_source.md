---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mutex_8h_source.html
original_path: doxygen/html/mutex_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mutex.h

[Go to the documentation of this file.](mutex_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_MUTEX\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_MUTEX\_H\_

9

10/\*

11 \* sys\_mutex behaves almost exactly like k\_mutex, with the added advantage

12 \* that a sys\_mutex instance can reside in user memory.

13 \*

14 \* Further enhancements will support locking/unlocking uncontended sys\_mutexes

15 \* with simple atomic ops instead of syscalls, similar to Linux's

16 \* FUTEX\_LOCK\_PI and FUTEX\_UNLOCK\_PI

17 \*/

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23#ifdef CONFIG\_USERSPACE

24#include <[zephyr/sys/atomic.h](atomic_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/sys\_clock.h](include_2zephyr_2sys__clock_8h.md)>

27

[ 28](structsys__mutex.md)struct [sys\_mutex](structsys__mutex.md) {

29 /\* Currently unused, but will be used to store state for fast mutexes

30 \* that can be locked/unlocked with atomic ops if there is no

31 \* contention

32 \*/

[ 33](structsys__mutex.md#adbb6c644b680b81a11ab183f97102de4) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [val](structsys__mutex.md#adbb6c644b680b81a11ab183f97102de4);

34};

35

41

[ 53](group__user__mutex__apis.md#ga486bd6a11d0b0d312cdf8a6a8f66c1a3)#define SYS\_MUTEX\_DEFINE(name) \

54 struct sys\_mutex name

55

[ 68](group__user__mutex__apis.md#ga5456b75934cb26abc974a45ae82d717b)static inline void [sys\_mutex\_init](group__user__mutex__apis.md#ga5456b75934cb26abc974a45ae82d717b)(struct [sys\_mutex](structsys__mutex.md) \*mutex)

69{

70 ARG\_UNUSED(mutex);

71

72 /\* Nothing to do, kernel-side data structures are initialized at

73 \* boot

74 \*/

75}

76

77\_\_syscall int z\_sys\_mutex\_kernel\_lock(struct [sys\_mutex](structsys__mutex.md) \*mutex,

78 [k\_timeout\_t](structk__timeout__t.md) timeout);

79

80\_\_syscall int z\_sys\_mutex\_kernel\_unlock(struct [sys\_mutex](structsys__mutex.md) \*mutex);

81

[ 102](group__user__mutex__apis.md#ga6887005f8223d4f36de5ae5c02ba4b17)static inline int [sys\_mutex\_lock](group__user__mutex__apis.md#ga6887005f8223d4f36de5ae5c02ba4b17)(struct [sys\_mutex](structsys__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout)

103{

104 /\* For now, make the syscall unconditionally \*/

105 return z\_sys\_mutex\_kernel\_lock(mutex, timeout);

106}

107

[ 125](group__user__mutex__apis.md#ga7d4babcd161600dab5f1842c58be2a1f)static inline int [sys\_mutex\_unlock](group__user__mutex__apis.md#ga7d4babcd161600dab5f1842c58be2a1f)(struct [sys\_mutex](structsys__mutex.md) \*mutex)

126{

127 /\* For now, make the syscall unconditionally \*/

128 return z\_sys\_mutex\_kernel\_unlock(mutex);

129}

130

131#include <syscalls/mutex.h>

132

133#else

134#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

135#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

136

137struct [sys\_mutex](structsys__mutex.md) {

138 struct k\_mutex kernel\_mutex;

139};

140

141#define SYS\_MUTEX\_DEFINE(name) \

142 struct sys\_mutex name = { \

143 .kernel\_mutex = Z\_MUTEX\_INITIALIZER(name.kernel\_mutex) \

144 }

145

146static inline void [sys\_mutex\_init](group__user__mutex__apis.md#ga5456b75934cb26abc974a45ae82d717b)(struct [sys\_mutex](structsys__mutex.md) \*mutex)

147{

148 [k\_mutex\_init](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)(&mutex->kernel\_mutex);

149}

150

151static inline int [sys\_mutex\_lock](group__user__mutex__apis.md#ga6887005f8223d4f36de5ae5c02ba4b17)(struct [sys\_mutex](structsys__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout)

152{

153 return [k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(&mutex->kernel\_mutex, timeout);

154}

155

156static inline int [sys\_mutex\_unlock](group__user__mutex__apis.md#ga7d4babcd161600dab5f1842c58be2a1f)(struct [sys\_mutex](structsys__mutex.md) \*mutex)

157{

158 return [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(&mutex->kernel\_mutex);

159}

160

161#endif /\* CONFIG\_USERSPACE \*/

162

166

167#ifdef \_\_cplusplus

168}

169#endif

170

171#endif /\* ZEPHYR\_INCLUDE\_SYS\_MUTEX\_H\_ \*/

[atomic.h](atomic_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)

int k\_mutex\_unlock(struct k\_mutex \*mutex)

Unlock a mutex.

[k\_mutex\_init](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480)

int k\_mutex\_init(struct k\_mutex \*mutex)

Initialize a mutex.

[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)

int k\_mutex\_lock(struct k\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

[sys\_mutex\_init](group__user__mutex__apis.md#ga5456b75934cb26abc974a45ae82d717b)

static void sys\_mutex\_init(struct sys\_mutex \*mutex)

Initialize a mutex.

**Definition** mutex.h:68

[sys\_mutex\_lock](group__user__mutex__apis.md#ga6887005f8223d4f36de5ae5c02ba4b17)

static int sys\_mutex\_lock(struct sys\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

**Definition** mutex.h:102

[sys\_mutex\_unlock](group__user__mutex__apis.md#ga7d4babcd161600dab5f1842c58be2a1f)

static int sys\_mutex\_unlock(struct sys\_mutex \*mutex)

Unlock a mutex.

**Definition** mutex.h:125

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[sys\_clock.h](include_2zephyr_2sys__clock_8h.md)

Variables needed for system clock.

[types.h](include_2zephyr_2types_8h.md)

[kernel\_structs.h](kernel__structs_8h.md)

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[sys\_mutex](structsys__mutex.md)

**Definition** mutex.h:28

[sys\_mutex::val](structsys__mutex.md#adbb6c644b680b81a11ab183f97102de4)

atomic\_t val

**Definition** mutex.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mutex.h](mutex_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
