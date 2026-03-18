---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stropts_8h_source.html
original_path: doxygen/html/stropts_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stropts.h

[Go to the documentation of this file.](stropts_8h.md)

1/\*

2 \* Copyright (c) 2024 Abhinav Srivastava

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_STROPTS\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_STROPTS\_H\_

[ 8](stropts_8h.md#ab12b3c3c77f22b0999f6b2cec1812da9)#define RS\_HIPRI BIT(0)

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 14](structstrbuf.md)struct [strbuf](structstrbuf.md) {

[ 15](structstrbuf.md#a7937239c2a6c2a6b4d76f71b96743589) int [maxlen](structstrbuf.md#a7937239c2a6c2a6b4d76f71b96743589);

[ 16](structstrbuf.md#a2ce53f2d390a31cdabe5299c73e489b0) int [len](structstrbuf.md#a2ce53f2d390a31cdabe5299c73e489b0);

[ 17](structstrbuf.md#a421c67aa5a9400a826e8e274f1ffb900) char \*[buf](structstrbuf.md#a421c67aa5a9400a826e8e274f1ffb900);

18};

19

[ 20](stropts_8h.md#a2e8c9b125d5b2b9e9c0f119bb8489c5e)int [putmsg](stropts_8h.md#a2e8c9b125d5b2b9e9c0f119bb8489c5e)(int fildes, const struct [strbuf](structstrbuf.md) \*ctlptr, const struct [strbuf](structstrbuf.md) \*dataptr, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

21

22#ifdef \_\_cplusplus

23}

24#endif

25

26#endif /\* ZEPHYR\_INCLUDE\_POSIX\_STROPTS\_H\_ \*/

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[putmsg](stropts_8h.md#a2e8c9b125d5b2b9e9c0f119bb8489c5e)

int putmsg(int fildes, const struct strbuf \*ctlptr, const struct strbuf \*dataptr, int flags)

[strbuf](structstrbuf.md)

**Definition** stropts.h:14

[strbuf::len](structstrbuf.md#a2ce53f2d390a31cdabe5299c73e489b0)

int len

**Definition** stropts.h:16

[strbuf::buf](structstrbuf.md#a421c67aa5a9400a826e8e274f1ffb900)

char \* buf

**Definition** stropts.h:17

[strbuf::maxlen](structstrbuf.md#a7937239c2a6c2a6b4d76f71b96743589)

int maxlen

**Definition** stropts.h:15

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [stropts.h](stropts_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
