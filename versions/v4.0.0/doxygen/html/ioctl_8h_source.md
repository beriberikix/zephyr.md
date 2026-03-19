---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ioctl_8h_source.html
original_path: doxygen/html/ioctl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ioctl.h

[Go to the documentation of this file.](ioctl_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_IOCTL\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_IOCTL\_H\_

8

9#include <[zephyr/sys/fdtable.h](fdtable_8h.md)>

10

[ 11](ioctl_8h.md#af48a6e38eb0ae226621514b44b9844eb)#define FIONBIO ZFD\_IOCTL\_FIONBIO

[ 12](ioctl_8h.md#ac68826c621a12d91544dab200c86c75a)#define FIONREAD ZFD\_IOCTL\_FIONREAD

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](ioctl_8h.md#a1487536105f7a596481bf6bfa8de99f6)int [ioctl](ioctl_8h.md#a1487536105f7a596481bf6bfa8de99f6)(int fd, unsigned long request, ...);

19

20#ifdef \_\_cplusplus

21}

22#endif

23

24#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_IOCTL\_H\_ \*/

[fdtable.h](fdtable_8h.md)

[ioctl](ioctl_8h.md#a1487536105f7a596481bf6bfa8de99f6)

int ioctl(int fd, unsigned long request,...)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [ioctl.h](ioctl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
