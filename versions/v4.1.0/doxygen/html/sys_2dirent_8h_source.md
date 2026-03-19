---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sys_2dirent_8h_source.html
original_path: doxygen/html/sys_2dirent_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dirent.h

[Go to the documentation of this file.](sys_2dirent_8h.md)

1/\*

2 \* Copyright (c) 2024 Tenstorrent AI ULC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_DIRENT\_H\_

8#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_DIRENT\_H\_

9

10#include <[limits.h](limits_8h.md)>

11

12#include <[zephyr/posix/posix\_features.h](posix__features_8h.md)>

13

14#if !defined(NAME\_MAX) && defined(\_XOPEN\_SOURCE)

15#define NAME\_MAX \_XOPEN\_NAME\_MAX

16#endif

17

18#if !defined(NAME\_MAX) && defined(\_POSIX\_C\_SOURCE)

19#define NAME\_MAX \_POSIX\_NAME\_MAX

20#endif

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 26](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc)typedef void [DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc);

27

[ 28](structdirent.md)struct [dirent](structdirent.md) {

[ 29](structdirent.md#ae4afde6b22d291bf27193ad4fe20b0bf) unsigned int [d\_ino](structdirent.md#ae4afde6b22d291bf27193ad4fe20b0bf);

[ 30](structdirent.md#a493ff210982a02728c1b177139bfdb47) char [d\_name](structdirent.md#a493ff210982a02728c1b177139bfdb47)[NAME\_MAX + 1];

31};

32

33#ifdef \_\_cplusplus

34}

35#endif

36

37#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_DIRENT\_H\_ \*/

[limits.h](limits_8h.md)

[posix\_features.h](posix__features_8h.md)

[dirent](structdirent.md)

**Definition** dirent.h:28

[dirent::d\_name](structdirent.md#a493ff210982a02728c1b177139bfdb47)

char d\_name[NAME\_MAX+1]

**Definition** dirent.h:30

[dirent::d\_ino](structdirent.md#ae4afde6b22d291bf27193ad4fe20b0bf)

unsigned int d\_ino

**Definition** dirent.h:29

[DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc)

void DIR

**Definition** dirent.h:26

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [dirent.h](sys_2dirent_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
