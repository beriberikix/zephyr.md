---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/utsname_8h_source.html
original_path: doxygen/html/utsname_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

utsname.h

[Go to the documentation of this file.](utsname_8h.md)

1/\*

2 \* Copyright (c) 2023 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_UTSNAME\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_UTSNAME\_H\_

8

9#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

15/\* These are for compatibility / practicality \*/

16#define \_UTSNAME\_NODENAME\_LENGTH \

17 COND\_CODE\_1(CONFIG\_POSIX\_SINGLE\_PROCESS, (CONFIG\_POSIX\_UNAME\_VERSION\_LEN), (0))

18#define \_UTSNAME\_VERSION\_LENGTH \

19 COND\_CODE\_1(CONFIG\_POSIX\_SINGLE\_PROCESS, (CONFIG\_POSIX\_UNAME\_VERSION\_LEN), (0))

20

[ 21](structutsname.md)struct [utsname](structutsname.md) {

[ 22](structutsname.md#a8bfca811eed8101b2310200a96e9757e) char [sysname](structutsname.md#a8bfca811eed8101b2310200a96e9757e)[sizeof("Zephyr")];

[ 23](structutsname.md#afc4ee8a38fc0d85ac4f8fe1b669c3f74) char [nodename](structutsname.md#afc4ee8a38fc0d85ac4f8fe1b669c3f74)[\_UTSNAME\_NODENAME\_LENGTH + 1];

[ 24](structutsname.md#afcc31cc768b481d10c887dcf56d64a1c) char [release](structutsname.md#afcc31cc768b481d10c887dcf56d64a1c)[sizeof("99.99.99-rc1")];

[ 25](structutsname.md#abe146e9be86c55a25881e6c58ba3ddf0) char [version](structutsname.md#abe146e9be86c55a25881e6c58ba3ddf0)[\_UTSNAME\_VERSION\_LENGTH + 1];

[ 26](structutsname.md#a708b512fcd536a51fa7266899eec3964) char [machine](structutsname.md#a708b512fcd536a51fa7266899eec3964)[sizeof(CONFIG\_ARCH)];

27};

28

[ 29](utsname_8h.md#a1ad7a68f28b58669758da1b12061a81f)int [uname](utsname_8h.md#a1ad7a68f28b58669758da1b12061a81f)(struct [utsname](structutsname.md) \*name);

30

31#ifdef \_\_cplusplus

32}

33#endif

34

35#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_UTSNAME\_H\_ \*/

[utsname](structutsname.md)

**Definition** utsname.h:21

[utsname::machine](structutsname.md#a708b512fcd536a51fa7266899eec3964)

char machine[sizeof(CONFIG\_ARCH)]

**Definition** utsname.h:26

[utsname::sysname](structutsname.md#a8bfca811eed8101b2310200a96e9757e)

char sysname[sizeof("Zephyr")]

**Definition** utsname.h:22

[utsname::version](structutsname.md#abe146e9be86c55a25881e6c58ba3ddf0)

char version[COND\_CODE\_1(CONFIG\_POSIX\_SINGLE\_PROCESS,(CONFIG\_POSIX\_UNAME\_VERSION\_LEN),(0))+1]

**Definition** utsname.h:25

[utsname::nodename](structutsname.md#afc4ee8a38fc0d85ac4f8fe1b669c3f74)

char nodename[COND\_CODE\_1(CONFIG\_POSIX\_SINGLE\_PROCESS,(CONFIG\_POSIX\_UNAME\_VERSION\_LEN),(0))+1]

**Definition** utsname.h:23

[utsname::release](structutsname.md#afcc31cc768b481d10c887dcf56d64a1c)

char release[sizeof("99.99.99-rc1")]

**Definition** utsname.h:24

[util\_macro.h](util__macro_8h.md)

Macro utilities.

[uname](utsname_8h.md#a1ad7a68f28b58669758da1b12061a81f)

int uname(struct utsname \*name)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [utsname.h](utsname_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
