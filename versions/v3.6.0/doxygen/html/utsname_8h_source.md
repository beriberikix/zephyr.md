---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/utsname_8h_source.html
original_path: doxygen/html/utsname_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

[ 13](structutsname.md)struct [utsname](structutsname.md) {

[ 14](structutsname.md#a8bfca811eed8101b2310200a96e9757e) char [sysname](structutsname.md#a8bfca811eed8101b2310200a96e9757e)[sizeof("Zephyr")];

[ 15](structutsname.md#adb9b79651cf171e090b5e9cf12804320) char [nodename](structutsname.md#adb9b79651cf171e090b5e9cf12804320)[CONFIG\_POSIX\_UNAME\_NODENAME\_LEN + 1];

[ 16](structutsname.md#afcc31cc768b481d10c887dcf56d64a1c) char [release](structutsname.md#afcc31cc768b481d10c887dcf56d64a1c)[sizeof("99.99.99-rc1")];

[ 17](structutsname.md#a5fdfa66e563e8112c517d3cd95133eaf) char [version](structutsname.md#a5fdfa66e563e8112c517d3cd95133eaf)[CONFIG\_POSIX\_UNAME\_VERSION\_LEN + 1];

[ 18](structutsname.md#a708b512fcd536a51fa7266899eec3964) char [machine](structutsname.md#a708b512fcd536a51fa7266899eec3964)[sizeof(CONFIG\_ARCH)];

19};

20

[ 21](utsname_8h.md#a1ad7a68f28b58669758da1b12061a81f)int [uname](utsname_8h.md#a1ad7a68f28b58669758da1b12061a81f)(struct [utsname](structutsname.md) \*name);

22

23#ifdef \_\_cplusplus

24}

25#endif

26

27#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_UTSNAME\_H\_ \*/

[utsname](structutsname.md)

**Definition** utsname.h:13

[utsname::version](structutsname.md#a5fdfa66e563e8112c517d3cd95133eaf)

char version[CONFIG\_POSIX\_UNAME\_VERSION\_LEN+1]

**Definition** utsname.h:17

[utsname::machine](structutsname.md#a708b512fcd536a51fa7266899eec3964)

char machine[sizeof(CONFIG\_ARCH)]

**Definition** utsname.h:18

[utsname::sysname](structutsname.md#a8bfca811eed8101b2310200a96e9757e)

char sysname[sizeof("Zephyr")]

**Definition** utsname.h:14

[utsname::nodename](structutsname.md#adb9b79651cf171e090b5e9cf12804320)

char nodename[CONFIG\_POSIX\_UNAME\_NODENAME\_LEN+1]

**Definition** utsname.h:15

[utsname::release](structutsname.md#afcc31cc768b481d10c887dcf56d64a1c)

char release[sizeof("99.99.99-rc1")]

**Definition** utsname.h:16

[uname](utsname_8h.md#a1ad7a68f28b58669758da1b12061a81f)

int uname(struct utsname \*name)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [utsname.h](utsname_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
