---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fcntl_8h_source.html
original_path: doxygen/html/fcntl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcntl.h

[Go to the documentation of this file.](fcntl_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_POSIX\_FCNTL\_H\_

8#define ZEPHYR\_POSIX\_FCNTL\_H\_

9

10#include <[zephyr/sys/fdtable.h](fdtable_8h.md)>

11

[ 12](fcntl_8h.md#ae036f789407d21f07b211552d67b3214)#define O\_APPEND ZVFS\_O\_APPEND

[ 13](fcntl_8h.md#a1cf6b1de1fffedaa1d26b189e9a8d2cc)#define O\_CREAT ZVFS\_O\_CREAT

[ 14](fcntl_8h.md#a9f5acfe79fafe14b6694447bd0e9f10b)#define O\_EXCL ZVFS\_O\_EXCL

[ 15](fcntl_8h.md#a39d33ce33804efd4d52606d59071c6d8)#define O\_NONBLOCK ZVFS\_O\_NONBLOCK

[ 16](fcntl_8h.md#ad1d67e453fb3031f40f8cd3403773813)#define O\_TRUNC ZVFS\_O\_TRUNC

17

[ 18](fcntl_8h.md#a4dc4d45e07d2abc899bcaf04b2846a87)#define O\_ACCMODE (ZVFS\_O\_RDONLY | ZVFS\_O\_RDWR | ZVFS\_O\_WRONLY)

19

[ 20](fcntl_8h.md#a7a68c9ffaac7dbcd652225dd7c06a54b)#define O\_RDONLY ZVFS\_O\_RDONLY

[ 21](fcntl_8h.md#abb0586253488ee61072b73557eeb873b)#define O\_RDWR ZVFS\_O\_RDWR

[ 22](fcntl_8h.md#a11b644a8526139c4cc1850dac1271ced)#define O\_WRONLY ZVFS\_O\_WRONLY

23

[ 24](fcntl_8h.md#ab93a8621587aba90181efd7d3aeea67e)#define F\_DUPFD ZVFS\_F\_DUPFD

[ 25](fcntl_8h.md#a025fad21a889c79f02ec53abe3526c32)#define F\_GETFL ZVFS\_F\_GETFL

[ 26](fcntl_8h.md#af2939853c650561d3495ed40f68f6249)#define F\_SETFL ZVFS\_F\_SETFL

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 32](fcntl_8h.md#ac843f2e35e60c3bbf1da47d84306f29b)int [open](fcntl_8h.md#ac843f2e35e60c3bbf1da47d84306f29b)(const char \*name, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), ...);

[ 33](fcntl_8h.md#acfc4bf677fc9f8be66d9624175cb3775)int [fcntl](fcntl_8h.md#acfc4bf677fc9f8be66d9624175cb3775)(int fildes, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), ...);

34

35#ifdef \_\_cplusplus

36}

37#endif

38

39#endif /\* ZEPHYR\_POSIX\_FCNTL\_H\_ \*/

[open](fcntl_8h.md#ac843f2e35e60c3bbf1da47d84306f29b)

int open(const char \*name, int flags,...)

[fcntl](fcntl_8h.md#acfc4bf677fc9f8be66d9624175cb3775)

int fcntl(int fildes, int cmd,...)

[fdtable.h](fdtable_8h.md)

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [fcntl.h](fcntl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
