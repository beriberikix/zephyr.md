---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/if_8h_source.html
original_path: doxygen/html/if_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

if.h

[Go to the documentation of this file.](if_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_NET\_IF\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_NET\_IF\_H\_

8

9#ifdef CONFIG\_NET\_INTERFACE\_NAME\_LEN

10#define IF\_NAMESIZE CONFIG\_NET\_INTERFACE\_NAME\_LEN

11#else

[ 12](if_8h.md#aedb93bcce9682d7644080b859849f59d)#define IF\_NAMESIZE 1

13#endif

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](structif__nameindex.md)struct [if\_nameindex](structif__nameindex.md) {

[ 20](structif__nameindex.md#a614c64e1c7abc1e2752860b14061f479) unsigned int [if\_index](structif__nameindex.md#a614c64e1c7abc1e2752860b14061f479);

[ 21](structif__nameindex.md#ab9d0f12e108f5f7ad0fccc951a4211b2) char \*[if\_name](structif__nameindex.md#ab9d0f12e108f5f7ad0fccc951a4211b2);

22};

23

[ 24](if_8h.md#a4da7243450c66298378e0f2d6434b997)char \*[if\_indextoname](if_8h.md#a4da7243450c66298378e0f2d6434b997)(unsigned int ifindex, char \*ifname);

[ 25](if_8h.md#a4349b1231de2572765f6b3771e6023f1)void [if\_freenameindex](if_8h.md#a4349b1231de2572765f6b3771e6023f1)(struct [if\_nameindex](structif__nameindex.md) \*ptr);

[ 26](if_8h.md#aadc0427486b1b97fa250760e8ccd4f7f)struct [if\_nameindex](structif__nameindex.md) \*[if\_nameindex](if_8h.md#aadc0427486b1b97fa250760e8ccd4f7f)(void);

[ 27](if_8h.md#aabacc3c49f072845092730128fbadd93)unsigned int [if\_nametoindex](if_8h.md#aabacc3c49f072845092730128fbadd93)(const char \*ifname);

28

29#ifdef \_\_cplusplus

30}

31#endif

32

33#endif /\* ZEPHYR\_INCLUDE\_POSIX\_NET\_IF\_H\_ \*/

[if\_freenameindex](if_8h.md#a4349b1231de2572765f6b3771e6023f1)

void if\_freenameindex(struct if\_nameindex \*ptr)

[if\_indextoname](if_8h.md#a4da7243450c66298378e0f2d6434b997)

char \* if\_indextoname(unsigned int ifindex, char \*ifname)

[if\_nametoindex](if_8h.md#aabacc3c49f072845092730128fbadd93)

unsigned int if\_nametoindex(const char \*ifname)

[if\_nameindex](if_8h.md#aadc0427486b1b97fa250760e8ccd4f7f)

struct if\_nameindex \* if\_nameindex(void)

[if\_nameindex](structif__nameindex.md)

**Definition** if.h:19

[if\_nameindex::if\_index](structif__nameindex.md#a614c64e1c7abc1e2752860b14061f479)

unsigned int if\_index

**Definition** if.h:20

[if\_nameindex::if\_name](structif__nameindex.md#ab9d0f12e108f5f7ad0fccc951a4211b2)

char \* if\_name

**Definition** if.h:21

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [net](dir_2c168081a5287170970afe4d92a99d1b.md)
- [if.h](if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
